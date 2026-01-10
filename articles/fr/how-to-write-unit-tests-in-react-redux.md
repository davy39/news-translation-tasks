---
title: Guide des tests unitaires React + Redux Testing Toolkit
subtitle: ''
author: Matthes B.
co_authors: []
series: null
date: '2022-11-09T15:32:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-unit-tests-in-react-redux
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-scott-webb-1527893.jpg
tags:
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Software Testing
  slug: software-testing
- name: unit testing
  slug: unit-testing
seo_title: Guide des tests unitaires React + Redux Testing Toolkit
seo_desc: 'In this step-by-step tutorial, you''ll learn how to easily start with Unit
  Tests in React. You''ll learn how to write tests for Redux states as well as fundamental
  Redux slice tests using the React Testing Library and Jest.

  🔐 Here''s What We''ll Cover


  ...'
---

Dans ce tutoriel pas à pas, vous apprendrez comment commencer facilement avec les tests unitaires dans React. Vous apprendrez à écrire des tests pour les états Redux ainsi que des tests fondamentaux pour les slices Redux en utilisant la React Testing Library et Jest.

## **\ud83d\udd10 Voici ce que nous allons couvrir**

* Vous verrez à quel point il est facile de configurer vos premiers tests unitaires dans React.
* Vous améliorerez vos connaissances générales sur React.
* Vous comprendrez pourquoi le développement piloté par les tests (TDD) est utile pour votre flux de travail de codage.

## **\ud83d\udcdd** Prérequis

* Vous devez être familier avec la structure de base du flux de travail React (y compris les composants fonctionnels et les hooks).
* Vous devez avoir une connaissance de base de Redux (j'utilise Redux Toolkit pour ce guide).
* Vous n'avez pas besoin de connaissances préalables sur les tests.
* J'utilise l'approche d'installation `npm`, pas celle de `yarn`.

## **\ud83c\udfaf** L'objectif

En apprenant les concepts avancés de React, vous allez probablement rencontrer le sujet des tests. Savoir travailler avec des tests automatiques est également très pratique pour tout développeur frontend en devenir. 

Cependant, lorsque j'apprenais moi-même React, j'ai eu du mal à trouver des informations sur la façon d'implémenter des tests pour des bibliothèques comme Redux (même si c'est une bibliothèque avec laquelle je travaille tout le temps). 

De plus, j'ai constaté que faire des tests de composants dans React est pratiquement impossible si vous ne savez pas comment travailler avec la bibliothèque Redux.

J'ai donc pris le temps de lire la documentation Redux et j'ai fait des allers-retours avec celle-ci. Ensuite, j'ai décidé d'écrire un guide de démarrage pratique pour les tests unitaires dans React, y compris Redux, pour partager ce que j'ai appris. 

Puisque je souhaite adopter une approche moderne, je vais également utiliser le Redux Toolkit. Nous allons couvrir l'implémentation de Redux dans ce guide.

### Ce que nous allons couvrir :

Pour commencer, je vais fournir quelques informations générales sur les tests avant de passer directement à la création des premiers tests unitaires généraux. 

Ensuite, je donnerai un aperçu rapide de la façon d'implémenter une logique Redux Toolkit. 

Puis nous travaillerons sur quelques tests unitaires au sein d'une application qui utilise Redux Toolkit. Pour cette étape, nous ajusterons nos tests précédemment créés au nouvel environnement Redux.

Ceci est un guide pas à pas. Si vous êtes nouveau dans les tests, je recommande de suivre ce guide dans l'ordre, de haut en bas.

J'ai également créé un [dépôt GitHub public](https://github.com/Matthes-Baer/unit-test-redux-article-app) pour ce guide avec quelques commentaires. Vous pouvez l'utiliser si vous souhaitez chercher quelque chose sans avoir à parcourir ce guide dans son intégralité à nouveau.

## Table des matières

1. [Quels sont les différents types de tests ?](#quest-ce-que-les-differents-types-de-tests)
2. [Comment configurer votre environnement de test React](#comment-configurer-votre-environnement-de-test-react)
3. [Vérifiez votre application React créée](#heading-verifiez-votre-application-react-creee)
4. [Comment créer votre premier test unitaire](#comment-creer-votre-premier-test-unitaire)
5. [Comment créer un test échouant intentionnellement](#comment-creer-un-test-echouant-intentionnellement)
6. [Comment créer quelques tests supplémentaires](#heading-comment-creer-quelques-tests-supplementaires)
7. [Comment effectuer des tests avec le React Redux Toolkit](#heading-comment-effectuer-des-tests-avec-le-react-redux-toolkit)
8. [Perspectives pour les tests avancés](#heading-perspectives-pour-les-tests-avances)

## \ud83d\udccb Quels sont les différents types de tests ?

Ce guide rapide ne vous fournira pas de connaissances théoriques détaillées sur tous les [différents types de tests existants](https://www.freecodecamp.org/news/types-of-software-testing/). À ce stade, vous devez simplement comprendre qu'il existe généralement trois types de tests :

* Tests unitaires
* Tests d'intégration
* Tests de bout en bout

Pour le dire simplement : vous pouvez voir ces trois types de tests comme généralement croissants en complexité. 

Alors que les [tests unitaires](https://www.freecodecamp.org/news/unit-tests-explained/) couvrent des fonctions et des composants individuels, les tests d'intégration se concentrent généralement sur plusieurs fonctions et leurs connexions entre elles. Les [tests de bout en bout](https://www.freecodecamp.org/news/end-to-end-testing-tutorial/) sont encore plus complexes et donnent des informations sur plusieurs structures de fonctions et de composants. 

Il existe d'autres concepts de test, mais ces trois-là sont les plus importants pour les développeurs web, par exemple.

Encore une fois, cela est vraiment simplifié. Mais dans ce cas, il est suffisant de savoir que les tests unitaires sont essentiellement les tests les moins complexes parmi ces trois.

Il est également assez facile de travailler avec des tests unitaires dès que vous avez une compréhension de base de la façon dont les tests fonctionnent en général.

Je voudrais également souligner rapidement qu'il existe principalement deux façons de tester votre application.

* Tests manuels
* Tests automatiques

Les tests manuels sont probablement ce que vous faites déjà pour toutes vos applications que vous créez. Lorsque vous testez manuellement votre application, vous démarrez essentiellement votre application React avec `npm run start` et cliquez réellement sur des boutons pour vérifier si la fonction correspondante fonctionne.

Les tests automatiques, en revanche, sont essentiellement des fonctions que vous créez et qui vérifient automatiquement votre application pour voir si les étapes respectives que vous avez définies dans ces tests fonctionnent. Ce type de test automatique est extrêmement important pour les grands projets. 

Avec cette approche automatique, il est également beaucoup plus facile de mettre à l'échelle vos tests. En fin de compte, vous avez beaucoup de tests qui testent automatiquement toute votre application en un temps relativement court. Ces tests peuvent vous aider à repérer toute erreur potentielle qui aurait pu se produire pendant le développement. Cela prendrait beaucoup plus de temps si vous deviez constamment revenir pour tester manuellement votre application.

Savoir travailler avec des tests automatiques est également généralement un grand plus pour votre CV en tant que développeur frontend.

## \ud83d\udd27 Comment configurer votre environnement de test React

Afin de commencer de manière pratique, nous allons directement plonger dans notre application React. 

Vous verrez que la configuration d'un environnement de test est relativement facile dans React – ou, pour être plus précis, React le fait tout pour vous pendant la configuration d'installation régulière.

Par conséquent, je crée une application React avec la ligne suivante :

`npx create-react-app <nom de votre application>`

Après cette étape, nous avons besoin de tout ce qui doit être ajouté pour utiliser Redux dans notre application React :

* **React Redux :** `npm install react-redux` (fournit certains hooks obligatoires, par exemple)
* **React Redux Toolkit :** `npm install @reduxjs/toolkit` (fournit la logique pour créer un store ou des slices, par exemple)

Il est intéressant de noter qu'il existe également le **Redux core** (`npm install redux`). Mais cela fait déjà partie de l'installation de React Redux Toolkit, donc nous n'avons pas à l'installer ici aussi. 

Si vous souhaitiez utiliser React sans le React Redux Toolkit, alors vous devriez séparément vous tourner vers l'installation du Redux core.

Vous pouvez également créer une nouvelle application React à partir de zéro avec `npx create-react-app my-app --template redux` qui inclut le React Redux Toolkit, le React core, React Redux, ainsi qu'un modèle du React Redux Toolkit. 

Choisissez cette approche si vous n'avez pas d'applications React existantes, car c'est probablement plus pratique.

Sous le capot, vous avez maintenant une application qui utilise la **React Testing library** combinée avec **Jest** (un framework de test). Ensemble, ils ont pratiquement tout ce dont vous aurez besoin pour tester votre application React. 

Vous n'avez pas à installer autre chose pour ce but. Ces outils sont fournis avec une installation standard de React.

## \ud83d\udd0e Vérifiez votre application React créée

Lorsque vous entrez dans votre application React nouvellement créée, vous trouverez la structure de dossiers et de fichiers à laquelle vous êtes probablement familier. Parmi d'autres, il y a le fichier `App.js`, qui est créé comme ceci :

```javascript
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
```

Dans le dossier `src`, vous avez également le fichier `App.test.js`. Ce fichier est en fait un premier test qui est sorti de la boîte avec l'installation de React. Ce fichier est structuré comme ceci :

```javascript
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

Même sans comprendre pleinement ce que sont `render` ou `screen`, par exemple, nous pouvons voir que quelque chose se passe avec notre composant `App`. En fait, il s'agit d'un test unitaire qui se concentre sur une partie spécifique du composant `App`.

Bien que ce premier modèle pour un test soit une représentation pratique de l'apparence d'un test, j'aimerais créer un fichier de test à partir de zéro.

De manière générale, les tests sont séparés en différentes suites de tests. Ces suites de tests sont généralement un groupe de tests qui se concentrent sur le même composant, par exemple. Les tests au sein de la même suite de tests ont essentiellement le même sujet superordonné.

Pour vérifier cela, essayez d'entrer `npm run test` dans votre terminal lorsque vous êtes dans votre application React. 

Il pourrait dire quelque chose comme "Il n'y a pas de nouveaux tests ou de changements depuis le dernier commit" – dans ce cas, entrez simplement `a` dans le terminal pour exécuter tous les tests indépendamment.

En fin de compte, vous devriez pouvoir voir ceci dans le terminal :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-124.png)
_Résultat de `npm run test`_

En haut, vous pouvez voir que le fichier `App.test.js` a réussi. En gros, tous les tests de ce fichier ont été réussis. 

En dessous, vous pouvez voir `renders learn react link` : il s'agit de la description de ce test particulier, que nous pouvons définir individuellement. Nous reviendrons sur ce point plus tard.

Plus bas, nous pouvons enfin voir les suites de tests et les tests. Comme vous pouvez le voir, nous avons une suite de tests et un test. Pour être plus précis, nous avons une suite de tests qui inclut ce test. 

Plus tard, vous reconnaîtrez que nous utiliserons environ 1 à 3 suites de tests alors qu'il y aura environ 5+ tests, par exemple. Encore une fois, les suites de tests fournissent essentiellement une structure qui regroupe les tests individuels.

Les snapshots ne sont pas importants pour votre cas spécifique.

Les [snapshots](https://jestjs.io/docs/snapshot-testing) sont un concept avancé pour les tests. Ainsi, un snapshot de référence (comme une image qui a été prise) est comparé avec la version après que certaines actions ont eu lieu. Cela peut aider à vérifier si l'interface utilisateur reste la même après certaines actions ou si certains changements se sont produits soudainement.

Je ne me concentrerai pas sur les tests avec snapshots dans cet article. C'est un sujet que vous pourriez vouloir consulter après avoir compris quelques bases des tests unitaires.

## \ud83d\udd28 Comment créer votre premier test unitaire

Maintenant que nous avons examiné un test unitaire, plongeons dans le premier test que nous allons construire à partir de zéro.

Pour cela, j'aimerais créer un nouveau dossier appelé `__tests__`. C'est courant lorsque vous travaillez avec des tests ou que vous consultez d'autres applications. 

Je déplace également le fichier `App.test.js` déjà disponible dans ce dossier. Cela ne change rien au résultat.

Notre structure de dossiers ressemble maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-125.png)
_structure générale des dossiers avec `__tests__`_

Dans `__tests__`, nous créons le fichier `myFirstTesting.test.js`. Nous avons besoin de cette structure de fichier `<nom du test>.test.js`. Vous pouvez également créer un fichier de test avec `<nom du test>.spec.js` – les deux approches fonctionneront de la même manière.

Notre première étape consiste à importer le composant `App.js` : `import App from "../App";`.

Pour créer notre premier test, nous devons utiliser la fonction `test()`. Vous pourriez également utiliser `it()`. Les deux donneront le même résultat. 

Le premier paramètre de cette fonction doit être une chaîne de caractères, qui décrit ce que nous allons tester (vous vous souvenez de l'histoire avec "renders learn react link" dans le fichier de test que nous avons vu ?). Cela va vous aider à avoir un aperçu plus précis après avoir exécuté tous les tests. 

Dans ce cas, j'utiliserai la description `"renders logo in App component"`. Le deuxième paramètre est une autre fonction pour laquelle nous utilisons une fonction fléchée anonyme. Notre fichier `myFirstTesting.test.js` ressemble maintenant à ceci :

```javascript
import App from "../App";

test("renders logo in App component", () => {

})
```

Même s'il ne se passe pas grand-chose, essayons d'entrer `npm run test` à nouveau. Nous trouverons le résultat suivant dans notre terminal :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-126.png)

Par conséquent, nous avons maintenant deux fichiers de test, ce qui donne deux suites de tests et deux tests.

Maintenant, nous aimerions réellement tester quelque chose. Puisque nous avons ajouté la description `"renders logo in App component"`, nous allons tester exactement cela. 

Pour ce faire, nous avons besoin de la fonction `render()`, que nous utiliserons chaque fois que nous voudrons réellement rendre un composant de notre application.

Pour ajouter la fonction `render()`, nous devons l'importer de la bibliothèque React Testing, qui fait déjà partie de notre application React sans aucune autre installation. 

Pendant que nous sommes à cette étape d'importation, importons également `screen` (également partie de la bibliothèque React Testing). Il fournit l'accès à différentes fonctions qui examineront l'écran actuel après qu'un élément a été rendu et trouveront des éléments spécifiques, par exemple.

Après avoir ajouté ces deux imports, notre fichier `myFirstTesting.test.js` ressemble maintenant à ceci :

```javascript
import App from "../App";
import { render, screen } from "@testing-library/react";

test("renders logo in App component", () => {

})
```

Maintenant que nous avons tout cela, commençons réellement à travailler sur notre test.

Tout d'abord, nous devons rendre notre composant. Rappelez-vous que les tests sont autonomes et ne savent pas que nous avons un `App.js` avec le contenu correspondant dans notre application React. Nous devons individuellement dire au test spécifique qu'un composant existe en le rendant avec `render()` en haut du test. Cela va ressembler à ceci : `render(<App />);`.

Maintenant que nous avons rendu le composant `App.js` dans ce test, nous devrions essayer de vérifier si une partie spécifique du contenu peut être trouvée par le test. De cette façon, nous pouvons réellement tester si `App.js` a été rendu comme il était censé l'être. 

En supposant que quelque chose a mal tourné, nous ne serions pas en mesure de trouver le logo React, par exemple, qui fait actuellement partie du composant `App.js`.

Nous allons donc essayer de trouver ce logo, qui est un élément `img`. Pour ce faire, nous pouvons utiliser la fonction `getByAltText()` qui trouve un élément par son attribut `alt` spécifique, qui est couramment utilisé pour les images. Nous avons accès à cette fonction avec `screen` que nous avons importé précédemment. 

Nous avons maintenant cette expression : `screen.getByAltText("logo")`. Donc le test regarde l'écran où nous avons rendu le composant `App.js` auparavant, puis obtient un élément, qui a un attribut `alt` de `"logo"`. Nous allons connecter tout cela à une variable. 

Notre fichier de test ressemble maintenant à ceci :

```javascript
import App from "../App";
import { render, screen } from "@testing-library/react";

test("renders logo in App component", () => {
  render(<App />);
  const image = screen.getByAltText("logo");
})
```

Il existe un ensemble de fonctions différentes comme `getByAltText()` que vous pouvez utiliser pour rechercher des éléments avec un contenu textuel spécifique, un rôle spécifique comme un bouton, ou même avec un identifiant de test que vous pouvez ajouter à l'élément réel.

Vous avez également la possibilité de rechercher plusieurs éléments. En dehors de cela, vous n'avez pas à utiliser une chaîne de caractères comme paramètre. Une expression régulière avec `/logo/i` est également réalisable, par exemple. Nous utiliserons différentes façons de trouver des éléments tout au long de ce guide de démarrage.

Pour la dernière étape, nous devons utiliser `expect()`, que nous utilisons pour voir quel comportement nous pouvons attendre. Dans ce cas, nous nous attendons à ce que notre variable `image` fasse partie du composant et existe donc. 

Pour cette approche, notre fichier ressemblerait à ceci :

```javascript
import App from "../App";
import { render, screen } from "@testing-library/react";

test("renders logo in App component", () => {
  render(<App />);
  const image = screen.getByAltText("logo");
  expect(image).toBeInTheDocument();
})
```

## \u2757 Comment créer un test échouant intentionnellement

Si nous exécutons maintenant nos tests avec `npm run test`, tout passera. Maintenant, essayons d'inverser cette logique pour créer un test échouant. De cette façon, nous pouvons vérifier si ce test a réellement un impact ou non. 

Pour ce faire, nous pouvons aller dans notre fichier `App.js` et changer l'attribut `alt` pour l'image du logo. Si vous le changez en `alt="loo"`, le test échouera et il vous donnera quelques informations.

Dans notre cas, cependant, j'aimerais changer quelque chose sur le test lui-même pour le faire échouer et vous montrer une autre expression qu'il est utile de connaître. Au lieu de `expect(image).toBeInTheDocument();`, nous pouvons également taper `expect(image).not.toBeInTheDocument();`. Donc ici nous avons ajouté un `not`. Cela a essentiellement inversé la logique, et maintenant le test s'attend à ce qu'aucun élément image n'existe.

Si nous essayons maintenant d'exécuter le test, nous trouverons le message d'erreur suivant dans notre terminal :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-127.png)
_Le message d'erreur que nous obtenons_

Vous pouvez voir que le test s'attendait à ce qu'il n'y ait pas d'élément tel que `image`. Cependant, il a trouvé quelque chose et a donc répondu avec un message d'erreur.

Vous n'avez pas à faire échouer intentionnellement tous vos tests pour vérifier s'ils fonctionnent ou non. Je voulais juste vous montrer à quoi ressemblerait un test échouant.

## \u270f\fe0f Comment créer quelques tests supplémentaires

Maintenant que nous avons terminé notre premier test et que nous avons quelques connaissances de base sur ce à quoi nous attendre lorsque nous travaillons avec des tests unitaires, nous allons examiner quelques autres exemples de tests.

Pour créer un scénario plus réaliste, je vais ajouter un composant supplémentaire, que nous insérerons dans le composant `App.js`.

Pour cette étape, nous créons d'abord un dossier appelé `components` dans notre dossier `src`. Ce n'est pas une obligation, mais il est courant de structurer vos fichiers de cette manière.

Dans le dossier `components`, nous créons `List.js`. Notre structure de dossiers ressemble maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-155.png)
_structure actuelle des dossiers_

Maintenant, essayons de suivre davantage un flux de travail de développement piloté par les tests (TDD), qui est assez moderne. Je ne dis pas nécessairement que cela est toujours recommandé. Mais une approche TDD est considérée comme une meilleure pratique par de plus en plus de personnes de nos jours. 

Bien sûr, dans ce tutoriel, nous ne parlons "que" des tests unitaires et non des tests d'intégration ou de bout en bout, mais le flux de travail général TDD est similaire pour les trois catégories de tests.

Ainsi, en utilisant cette approche de développement piloté par les tests, nous ajoutons essentiellement des tests et travaillons sur notre application simultanément. 

Pour être plus précis, nous créons même des tests pour des composants et des parties de fonctions individuelles avant même d'implémenter cette logique testée dans votre application. 

Il y a donc beaucoup d'allers-retours au lieu de créer tous les tests à la fois à la fin.

### Comment démarrer la configuration pour `List.js`

Dans notre exemple, nous avons ajouté le composant `List.js`. Dans ce composant, j'aimerais ajouter une liste avec un bouton. Lorsque l'utilisateur clique sur le bouton, il ajoute quelque chose à la liste (un objet avec plusieurs clés et valeurs).

Pour avoir une sorte de cadre, je vais d'abord ajouter quelques éléments `div` et des éléments similaires à notre composant `List.js` avant de plonger dans la logique réelle.

Le composant `List.js` ressemble maintenant à ceci :

```javascript
const List = () => {
  return (
    <div
      style={{ marginLeft: "auto", marginTop: "500px", marginBottom: "500px" }}
    >
      <h1>This is a list</h1>
      <ul style={{ listStyleType: "none" }}>
        <li>This is the first list entry</li>
      </ul>
      <button>This button can add a new entry to the list</button>
    </div>
  );
};

export default List;

```

J'ai également ajouté le composant `List.js` en tant qu'enfant à `App.js` (en dessous de toutes les autres choses dans `App.js`) afin qu'il soit visible sans changer autre chose.

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-156.png)
_Comment cela ressemble_

Cela ne vous fera pas gagner de compétitions de style, mais c'est suffisant pour notre cas.

### Configuration du test pour `List.js`

Puisque nous voulons tester pendant que nous travaillons sur notre composant, je vais maintenant sauter directement à la partie des tests même si rien ne s'est vraiment passé dans notre composant `List.js` en termes de fonctions de clic, par exemple.

Nous pourrions créer un nouveau fichier de test, mais j'aimerais vous montrer une nouvelle fonction que nous pouvons utiliser pour nos suites de tests spécifiquement. Cette fonction s'appelle `describe()` et peut être utile pour structurer davantage nos tests.

Pour utiliser `describe()`, nous allons dans `myFirstTesting.test.js` dans `__tests__`. En ce moment, ce fichier sert essentiellement de suite de tests pour le test que nous avons spécifiquement créé pour le composant `App.js`. Mais j'aimerais avoir deux suites de tests dans ce fichier de test : une pour les tests `App.js` et une pour les tests `List.js`.

Pour cette étape, j'utilise la fonction `describe()`, qui fonctionne essentiellement comme la fonction `test()` en termes de paramètres. 

Le premier paramètre sera une chaîne de caractères, décrivant la suite de tests respective. Le deuxième paramètre est une fonction, qui inclut ensuite nos fonctions `test()` avec leurs éléments.

Cela ressemblera à ceci dans notre cas :

```javascript
import App from "../App";
import { render, screen } from "@testing-library/react";

describe("App.js component", () => {
  test("renders logo in App component", () => {
    render(<App />);
    const image = screen.getByAltText("logo");
    expect(image).toBeInTheDocument();
  });
});

describe("List.js component", () => {
  test("example", () => {});
});

```

Avant de sauter dans ce nouveau test, j'aimerais en fait ajouter quelque chose pour le test `App.js`. Puisque nous avons ce bloc `describe()`, nous pourrions simplement ajouter une nouvelle fonction `test()` – et c'est ce que je vais faire.

Voir le nouveau test ajouté décrit avec `"renders List.js component in App.js"` :

```javascript
import App from "../App";
import { render, screen } from "@testing-library/react";

describe("App.js component", () => {
  test("renders logo in App component", () => {
    render(<App />);
    const image = screen.getByAltText("logo");
    expect(image).toBeInTheDocument();
  });
  
   test("renders List.js component in App.js", () => {
    render(<App />);
    const textInListJS = screen.getByText(/This is a list/i);
    expect(textInListJS).toBeInTheDocument();
  });
});

describe("List.js component", () => {
  test("example", () => {});
});

```

Je rends donc le composant `App.js` et je recherche du texte via une expression régulière, qui fait partie du composant `List.js`. Ce test peut être compris comme un test de rendu pour `List.js`. Si `List.js` n'avait pas pu être rendu dans `App.js`, ce test n'aurait pas réussi.

Si vous êtes confus que cela fonctionne sans utiliser séparément `render()` sur le composant `List.js`, rappelez-vous que `List.js` fait partie de `App.js` et que tout ce qui est à l'intérieur de `App.js` sera rendu dans des conditions typiques. Si vous essayiez de rechercher une phrase de texte qui n'existe pas dans `List.js`, ce nouveau test échouerait. Pour l'instant, dans notre cas, il réussit.

J'aimerais également souligner que vous pouvez avoir plusieurs fonctions `expect()` dans le même test. Par conséquent, nous aurions également pu structurer ce nouveau test comme ceci :

```javascript
import App from "../App";
import { render, screen } from "@testing-library/react";

describe("App.js component", () => {
  test("renders logo in App component", () => {
    render(<App />);
    const image = screen.getByAltText("logo");
    const textInListJS = screen.getByText(/This is a list/i);
    
    expect(image).toBeInTheDocument();
    expect(textInListJS).toBeInTheDocument();
  });
});

describe("List.js component", () => {
  test("example", () => {});
});

```

Cela fonctionnerait également parfaitement dans notre cas. Et cela peut être utile dans des situations où vous testez des éléments qui sont directement connectés les uns aux autres et ont les mêmes exigences pour être rendus. 

Mais gardez à l'esprit que dans notre cas, nous aurions dû ajuster la description de ce test. C'est parce que `"renders logo in App component"` n'est plus correct si nous testons plus que cela dans ce test. Donc, revenons à la structure avec deux tests séparés pour l'instant. Mais gardez à l'esprit que vous êtes capable de travailler comme cela.

### Retour au test pour `List.js`

Maintenant, j'aimerais travailler avec le deuxième bloc `describe()` que nous avons créé il y a quelques instants, où nous voulons travailler avec des tests spécifiquement pour le composant `List.js`.

Puisque nous visons une approche de développement piloté par les tests, nous devrions réfléchir à ce que nous allons construire, écrire un test, puis implémenter cette logique dans notre composant.

Nous voulons créer une simple liste dans notre composant `List.js`. Il y aura donc un tableau, que nous parcourrons avec `map()`. 

Pour cette approche, nous utiliserons le hook `useState()` afin d'avoir un état qui peut s'ajuster dynamiquement (le tableau des éléments de la liste). Notre premier test sera de vérifier si la longueur de ce tableau dans son état initial est égale à `1`.

Pour trouver les éléments dans cet état, nous utiliserons la méthode `getAllByTestId()`, qui nous permet de rechercher des éléments spécifiques que nous avons marqués avec un `data-testid` dans le frontend. 

Le test avec la description `"renders initial state of listData state"` que j'ai créé est maintenant inclus :

```javascript
import App from "../App";
import { render, screen } from "@testing-library/react";

describe("App.js component", () => {
  test("renders logo in App component", () => {
    render(<App />);
    const image = screen.getByAltText("logo");
    expect(image).toBeInTheDocument();
  });
  
  test("renders List.js component in App.js", () => {
    render(<App />);
    const textInListJS = screen.getByText(/This is a list/i);
    expect(textInListJS).toBeInTheDocument();
  });
});

describe("List.js component", () => {
   test("renders initial state of listData state", () => {
    render(<List />);
    const list = screen.getAllByTestId("list-item");
    expect(list.length).toEqual(1);
  });
});

```

Pour l'instant, ce test échouera, bien sûr, car nous n'avons pas encore ajouté cette logique au composant.

J'ai donc ajusté le composant `List.js`. Il ressemble maintenant à ceci :

```javascript
import { useState } from "react";

const List = () => {
  const initialState = [
    {
      id: `${new Date().getSeconds()}`,
      description: "This is something",
      significance: 7,
    },
  ];
  const [listData, setListData] = useState(initialState);

  return (
    <div
      style={{ marginLeft: "auto", marginTop: "500px", marginBottom: "500px" }}
    >
      <h1>This is a list</h1>
      <ul style={{ listStyleType: "none" }}>
        {listData.map((listItem) => {
          return (
            <li key={listItem.id} data-testid="list-item">
              {listItem.description}
            </li>
          );
        })}
      </ul>
      <button>This button can add a new entry to the list</button>
    </div>
  );
};

export default List;

```

Ce qui a été ajouté est le tableau d'état `listData` via un hook `useState()` ainsi qu'un `initialState`, que j'ai initialisé avec un objet tout en haut. J'ai également utilisé la fonction `map()` pour parcourir ce `listData` afin de créer une liste. 

Pour chaque élément `<li>`, j'ajoute une clé et un `data-testid`. Ce `data-testid` est l'identifiant dont nous avons besoin pour notre test afin de trouver les éléments respectifs.

Sur notre application réelle, nous pouvons voir le `listItem.description` pour cet état initial :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-165.png)

Ainsi, en testant manuellement (en regardant réellement notre application dans le navigateur), nous pouvons voir que cela devrait fonctionner. Si nous exécutons maintenant nos tests, nous verrons également que le test que nous avons créé a réussi.

### Comment ajouter un objet à l'état

Maintenant, testons quelque chose de plus excitant : la logique pour ajouter un nouvel objet à cet état `listData`. Encore une fois, nous commencerons par travailler sur notre test avant d'implémenter la logique requise dans le composant React.

Avec ce nouveau test ajouté décrit par `"adds a new data entry to listData after button click"`, notre fichier de test ressemble maintenant à ceci :

```javascript
import App from "../App";
import List from "../components/List";
import { render, screen } from "@testing-library/react";

import userEvent from "@testing-library/user-event";

describe("App.js component", () => {
  test("renders logo in App component", () => {
    render(<App />);
    const image = screen.getByAltText("logo");
    expect(image).toBeInTheDocument();
  });

  test("renders List.js component in App.js", () => {
    render(<App />);
    const textInListJS = screen.getByText(/This is a list/i);
    expect(textInListJS).toBeInTheDocument();
  });
});

describe("List.js component", () => {
  test("renders initial state of listData state", () => {
    render(<List />);
    const list = screen.getAllByTestId("list-item");
    expect(list.length).toEqual(1);
  });

  test("adds a new data entry to listData after button click", () => {
    render(<List />);
    let listItems = screen.getAllByTestId("list-item");
    const button = screen.getByRole("button", {
      name: /This button can add a new entry to the list/i,
    });

    expect(list.length).toEqual(1);
    userEvent.click(button);
    list = screen.getAllByTestId("list-item");
    expect(list.length).toEqual(2);
  });
});

```

En bas, vous pouvez voir ce test. Par conséquent, nous rendons d'abord le composant `List.js` avant de rechercher tous les éléments de liste disponibles auxquels nous avons attribué un identifiant de test. Vous verrez exactement où nous avons mis l'identifiant de test dans quelques instants.

Nous devons également rechercher le bouton que nous voulons tester pour voir si le clic dessus ajoute quelque chose à la liste. Nous faisons cela avec `getByRole()` qui attend un rôle comme `"button"` ou `"table"` en tant que premier paramètre, par exemple (il y a un ensemble de rôles différents que vous pouvez cibler). Le deuxième paramètre est optionnel et est un objet qui peut recevoir une valeur pour la clé `name`.

`name` est pratiquement le contenu textuel que nous avons spécifiquement pour le bouton dans ce cas. Ce deuxième paramètre optionnel est utile lorsque vous avez plusieurs éléments de type `"button"` dans votre composant et que vous souhaitez obtenir un bouton spécifique parmi ceux-ci.

Après avoir obtenu les `listItems` ainsi que le `button`, nous commençons par un premier `expect()` pour tester essentiellement l'état initial. Dans cet état initial, nous nous attendons à n'avoir qu'un seul élément de liste.

Ensuite, avec l'aide de `userEvent`, nous allons cliquer sur le bouton. Vous pourriez également utiliser `fireEvent` pour cette situation (`userEvent` est encore assez nouveau par rapport à l'approche `fireEvent`). Les deux fonctionneront, et les deux sont utiles pour toute action où vous souhaitez interagir avec des éléments spécifiques. Dans ce cas, je veux simuler un clic sur un bouton.

Les tests suivent généralement un modèle "arranger -> agir -> affirmer" que vous pouvez suivre pour les structurer. Dans la partie "arranger", vous initialisez et obtenez tous les éléments nécessaires. Avec la partie "agir", vous simuleriez un clic de souris (comme dans notre cas), par exemple. Avec "affirmer", vous vérifiez si tout se comporte comme vous l'attendiez.

Dans un autre cas, vous pourriez simuler le changement de la valeur d'un champ de saisie avec `fireEvent.change(inputField, { target: { value: someValueVariable } })`, par exemple. Peut-être souhaitez-vous mettre l'accent sur un champ de saisie ou même faire glisser un élément - de telles actions peuvent être simulées via `fireEvent` et `userEvent`.

Après le clic sur le bouton, il a de nouveau recherché tous les `listItems` puisque la valeur actuelle de cette variable serait toujours `1` de l'initialisation précédente. Dès que cette étape est terminée, il utilise une autre fonction `expect()` pour vérifier si la longueur du tableau `listItems` est maintenant égale à `2` et non `1`.

Maintenant que nous avons notre logique de test, sautons à nouveau au composant `List.js` et implémentons la logique correspondante :

```javascript
import { useState } from "react";

const List = () => {
  const initialState = [
    {
      id: `${new Date().getSeconds()}`,
      description: "This is something",
      significance: 7,
    },
  ];
  const [listData, setListData] = useState(initialState);

  return (
    <div
      style={{ marginLeft: "auto", marginTop: "500px", marginBottom: "500px" }}
    >
      <h1>This is a list</h1>
      <ul style={{ listStyleType: "none" }}>
        {listData.map((listItem) => {
          return (
            <li key={listItem.id} data-testid="list-item">
              {listItem.description}
            </li>
          );
        })}
      </ul>
      <button
        onClick={() =>
          setListData([
            ...listData,
            { id: 999, description: "999", significance: 100 },
          ])
        }
      >
        This button can add a new entry to the list
      </button>
    </div>
  );
};

export default List;

```

La seule partie qui a changé est le bouton en bas de ce fichier. J'ai donc ajouté une fonction qui est appelée lors du clic sur ce bouton. La fonction ajuste ensuite l'état actuel de `listData` qui est responsable du rendu de notre liste. J'ai copié l'état actuel avec un opérateur de propagation et j'ai ensuite ajouté un autre objet codé en dur comme nouvelle entrée pour cette liste. 

Bien sûr, il existe des moyens plus créatifs de remplir les valeurs pour les clés `id`, `description` et `significance`.

J'aimerais également souligner que vous avez la possibilité de créer une fonction séparée en dehors de `return()` et d'accéder à cette fonction comme ceci : `onClick={separateFunctionToAddObjectToState}` sur le même élément de bouton. Cela fonctionnerait également sans avoir à rendre quelque chose d'additionnel dans le test.

Si nous exécutons maintenant notre test, nous verrons qu'il réussit. Si vous essayez de vous attendre toujours à une longueur de `1` après avoir cliqué sur le bouton, le test échouera comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-192.png)
_alerte d'erreur pour une longueur de 1_

Donc, cela fait effectivement ce qu'il est censé faire.

## \ud83d\udd27 Configuration pour Redux

Après avoir travaillé avec des états locaux via le hook `useState()`, j'aimerais travailler sur les mêmes fichiers et les ajuster pour Redux (ou le Redux Toolkit, pour être précis). 

Je ne vais pas approfondir ce qu'est réellement Redux et ce que chaque terme comme `action`, `store` ou `reducer` signifie en détail – car cela mériterait un tout nouveau guide. Si vous voulez cela, vous pouvez [lire ce guide sur les bases de Redux](https://www.freecodecamp.org/news/redux-for-beginners/).

Au lieu de cela, je vais donner un bref aperçu et montrer quels fichiers j'ajoute et modifie. Ensuite, je parlerai de la façon de gérer la méthode `render()`, y compris le fournisseur de store Redux, qui peut causer beaucoup de frustration lors des tests si vous ne le connaissez pas.

### Structure globale des dossiers :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-14.png)
_structure globale actuelle des dossiers avec le React Redux Toolkit_

Vous pouvez voir que j'ai ajouté un dossier `app` (pour le store) ainsi qu'un dossier `features` (pour la slice).

### Fichier `index.js` mis à jour :

```javascript
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { Provider } from "react-redux";
import store from "./app/store";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);
```

Vous pouvez voir que j'ai ajouté un `provider` et que je l'ai enveloppé autour de l'application afin que nous ayons accès au store depuis n'importe où.

### Fichier `store.js` créé :

```javascript
import { configureStore } from "@reduxjs/toolkit";
import { ListSlice } from "../features/ListSlice";

const store = configureStore({
  reducer: {
    listReducers: listSlice.reducer,
  },
});

export default store;

```

Dans ce fichier, nous avons créé le store requis pour l'implémentation de Redux.

### Fichier `ListSlice.js` créé dans le dossier `features` :

```javascript
import { createSlice } from "@reduxjs/toolkit";

export const initialState = {
  value: [
    {
      id: `${new Date().getSeconds()}`,
      description: "This is something",
      significance: 7,
    },
  ],
};

export const ListSlice = createSlice({
  name: "listReducers",
  initialState,
  reducers: {},
});

export const { } = ListSlice.actions;
export default ListSlice.reducer;

```

Ici, nous avons créé la slice que nous avons ajoutée au store. Remarquez que je n'ai pas encore ajouté de reducer. Cette slice contient simplement l'état correspondant actuel.

### Fichier `List.js` mis à jour dans le dossier `components` :

```javascript
import { useSelector, useDispatch } from "react-redux";

const List = () => {
  const listState = useSelector((state) => state.listReducers.value);
  const dispatch = useDispatch(); // not used right now

  return (
    <div
      style={{ marginLeft: "auto", marginTop: "500px", marginBottom: "500px" }}
    >
      <h1>This is a list</h1>
      <ul style={{ listStyleType: "none" }}>
        {listState.map((listItem) => {
          return (
            <li key={listItem.id} data-testid="list-item">
              {listItem.description}
            </li>
          );
        })}
      </ul>
      <button>This button can add a new entry to the list</button>
    </div>
  );
};

export default List;

```

Sur le frontend, nous avons remplacé l'état local (en utilisant le hook useState) par l'état Redux (en utilisant le hook useSelector). Vous verrez également que j'ai ajusté le bouton. Il n'y a plus de fonction de clic (nous reviendrons sur ce point plus tard).

## \ud83d\udd0e Comment effectuer des tests avec le React Redux Toolkit

Maintenant que nous avons mis à jour et créé tous les fichiers nécessaires pour la logique du React Redux Toolkit, j'aimerais exécuter un test rapide de tous les tests que nous avons précédemment créés.

Le résultat est que tous les tests ont échoué :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-15.png)

Gardez à l'esprit que j'ai ajusté le bouton dans `List.js`, par exemple, donc le test correspondant était censé échouer. Cependant, tous les tests n'auraient pas dû échouer.

Les environnements de test fonctionnent dans leur propre monde. Ils ne savent pas si vous enveloppez un fournisseur quelque part dans `index.js` et activez la logique Redux. Donc les tests essaient toujours de faire fonctionner le rendu sans Redux. Mais notre application dépend maintenant de Redux pour gérer notre état principal.

Cela signifie que nous devons ajuster la fonction `render()` pour que cette fonction soit effectivement alignée avec la logique Redux.

Une méthode pour faire fonctionner cela est d'introduire une fonction d'assistance, que nous stockerons dans un nouveau dossier appelé `utils`. Le fichier s'appellera `utils-for-tests.jsx`. Le contenu ressemblera à ceci :

```javascript
import React from "react";
import { render } from "@testing-library/react";
import { configureStore } from "@reduxjs/toolkit";
import { Provider } from "react-redux";
// As a basic setup, import your same slice reducers
import { ListSlice } from "../features/ListSlice";

export function renderWithProviders(
  ui,
  {
    preloadedState = {},
    // Automatically create a store instance if no store was passed in
    store = configureStore({
      reducer: { listReducers: ListSlice.reducer },
      preloadedState,
    }),
    ...renderOptions
  } = {}
) {
  function Wrapper({ children }) {
    return <Provider store={store}>{children}</Provider>;
  }

  // Return an object with the store and all of RTL's query functions
  return { store, ...render(ui, { wrapper: Wrapper, ...renderOptions }) };
}

```

Ces informations de code peuvent être trouvées dans la [documentation Redux](https://redux.js.org/usage/writing-tests). Vous pouvez presque tout copier et coller pour votre application.

Mais vous devez ajuster les slices qui sont utilisées. Puisque dans notre application il n'y a que le `ListSlice`, nous n'avons pas grand-chose à ajouter. Il suffit d'importer cela et de mettre à jour le contenu de la fonction `configureStore()`, comme nous l'avons géré dans notre fichier `store.js`.

Cette étape est nécessaire pour simuler essentiellement toute la logique Redux et la rassembler en une nouvelle fonction `render()`.

Avec cela, nous pouvons importer cette nouvelle fonction dans nos fichiers de test (`App.test.js` et `myFirstTesting.test.js`) puis remplacer toutes les fonctions `render()` par `renderWithProviders()`. Le fichier `App.test.js`, par exemple, ressemble maintenant à ceci :

```javascript
import { screen } from "@testing-library/react";
import App from "../App";
import { renderWithProviders } from "../utils/utils-for-tests";

test("renders learn react link", () => {
  renderWithProviders(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

```

Il n'y a pas grand-chose de plus à faire ! Si nous exécutons maintenant nos tests à nouveau (et commentons ce test qui va échouer de toute façon car la logique du bouton n'est plus active), cela fonctionnera à nouveau.

### Test des slices

Une autre partie passionnante des tests avec Redux est le test des slices. Si vous avez créé votre application avec le modèle React Redux Toolkit, alors vous serez fourni avec quelques tests correspondants.

Pour notre cas, je souhaite également implémenter un nouveau fichier de test où nous testerons spécifiquement `ListSlice.js` et sa logique Redux correspondante.

Pour cette slice, nous devons importer la slice et les reducers correspondants que nous voulons tester. Pour commencer, je vais importer la slice et tester si elle est initialisée avec l'initialState.

Ce n'est en fait pas l'approche TDD puisque nous avons déjà testé manuellement cette partie. Néanmoins, j'aimerais implémenter un test automatique également :

```javascript
import ListSlice, { initialState } from "../features/ListSlice";

describe("tests for ListSlice", () => {
  test("initialize slice with initialValue", () => {
    const listSliceInit = ListSlice(initialState, { type: "unknown" });
    expect(listSliceInit).toBe(initialState);
  });
});

```

Remarquez que j'utilise `.spec` au lieu de `.test`. Cela n'a pas d'importance. Vous pouvez choisir l'un ou l'autre. Dans ce cas, j'opte pour `.spec` pour vous rappeler que c'est également une option viable.

Rappelez-vous également que nous avons exporté l'initialState dans notre slice (voir ci-dessus). Nous sommes donc en mesure de l'importer ici.

Autre que cela, nous sommes déjà familiers avec l'environnement `describe()`, qui inclut un `test()`. Dans ce test, j'initialise une variable `listSliceInit`, qui contiendra la valeur que nous recevons après que l'opération de slice a eu lieu.

Pour cette opération, nous utilisons `ListSlice` comme une fonction et incluons l'état initial comme premier argument (dans ce cas `initialState`). Le deuxième argument sera un reducer dans la plupart des cas. 

Mais dans ce cas, nous n'avons pas besoin d'entrer un reducer. Au lieu de cela, nous utilisons un objet avec `type: "unknown"`. Cela indique essentiellement à la fonction que nous ne voulons pas effectuer d'opérations supplémentaires.

Par conséquent, `listSliceInit` devrait maintenant inclure notre valeur d'état, qui inclut un tableau avec une entrée. Le test correspondant réussira.

Pour forcer un échec, j'entre `expect(listSliceInit).toBe({ value: [] });` au lieu de la fonction `expect()` précédente. Donc au lieu de notre `initialState`, nous nous attendons à ce qu'il ait un tableau vide. Maintenant, notre environnement de test nous dira ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-24.png)
_test échouant_

Donc, il nous dit en fait exactement ce qu'il attendait – dans ce cas, il s'attendait à `initialState`.

Ensuite, j'aimerais tester un reducer. Cependant, nous n'en avons pas encore ajouté. Je vais donc ajuster `ListSlice` dans le fichier `ListSlice.js` comme ceci :

```javascript
export const ListSlice = createSlice({
  name: "listReducers",
  initialState,
  reducers: {
    testAddReducer: (state, action) => {
      state.value.push(action.payload);
    },
  },
});
```

Ainsi, j'ai ajouté `testAddReducer()`, qui est responsable de l'ajout d'un élément supplémentaire à la valeur de l'état actuel, qu'il reçoit via une entrée du dispatch (via `action.payload`).

Si nous revenons maintenant au fichier `listSlice.spec.js`, j'ajoute un autre test unitaire :

```javascript
import ListSlice, { initialState, testAddReducer } from "../features/ListSlice";

describe("tests for ListSlice", () => {
  test("initialize slice with initialValue", () => {
    const listSliceInit = ListSlice(initialState, { type: "unknown" });
    expect(listSliceInit).toBe(initialState);
  });

  test("testAddReducer", () => {
    const testData = {
      id: `${new Date().getSeconds()}`,
      description: "This is for the test section",
      significance: 5,
    };

    const afterReducerOperation = ListSlice(
      initialState,
      testAddReducer(testData)
    );

    expect(afterReducerOperation).toStrictEqual({
      value: [initialState.value.at(0), testData],
    });
  });
});

```

J'ai ajouté le test pour `testAddReducer`. Vous pouvez voir que j'ai également importé le reducer.

Tout d'abord, j'initialise une nouvelle variable, `testData`, qui contient les données que je souhaite ajouter à l'état actuel.

Après cela, nous suivons la même structure qu'auparavant avec `afterReducerOperation`. Mais au lieu de ce `type: "unknown"`, nous ajoutons le reducer comme deuxième argument. Cela reçoit le `testData` comme paramètre – essentiellement comme vous le verriez dans un dispatch.

Ensuite, nous nous attendons à ce que la variable `afterReducerOperation` soit strictement égale à la valeur d'un tableau, qui a deux entrées : `initialState.value.at(0)` (la première entrée de notre `initialState`) et `testData`. Et ce test réussira comme nous l'avons effectivement attendu.

Si nous essayons d'entrer d'autres entrées ou de changer les entrées actuelles, vous pourriez voir ce test échouer :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-25.png)
_erreur forcée : j'ai ajouté une troisième entrée au tableau_

### Comment faire fonctionner à nouveau la fonction de clic du bouton

Souvenez-vous du clic du bouton dans le composant `List.js` (pour ajouter quelque chose à l'état `listData`) qui ne fonctionnait plus après avoir changé pour la configuration Redux ? Mettons rapidement cela à jour pour faire fonctionner cette logique dans un environnement Redux pour l'exhaustivité. Puisque nous avons le reducer requis maintenant, ce sera une étape facile.

Pour faire fonctionner le test à nouveau, qui ajoutait un nouvel élément à l'état, nous devons l'ajuster un peu sur le frontend pour implémenter la logique Redux. (Auparavant, nous utilisions le hook useState pour un état local.)

Pour cette étape, nous utilisons la fonction `dispatch()` afin d'atteindre le `testAddReducer` :

```javascript
import { useSelector, useDispatch } from "react-redux";
import { testAddReducer } from "../features/ListSlice";

const List = () => {
  const listState = useSelector((state) => state.listReducers.value);
  const dispatch = useDispatch();

  return (
    <div
      style={{ marginLeft: "auto", marginTop: "500px", marginBottom: "500px" }}
    >
      <h1>This is a list</h1>
      <ul style={{ listStyleType: "none" }}>
        {listState.map((listItem) => {
          return (
            <li key={listItem.id} data-testid="list-item">
              {listItem.description}
            </li>
          );
        })}
      </ul>
      <button
        onClick={() =>
          dispatch(
            testAddReducer({
              id: `${new Date().getSeconds()}1`,
              description: "This is added",
              significance: 5,
            })
          )
        }
      >
        This button can add a new entry to the list
      </button>
    </div>
  );
};

export default List;

```

En dehors de la logique du bouton, rien d'autre n'a changé dans ce fichier.

Dans le test correspondant (dans `myFirstTesting.test.js`, rien n'a changé), si nous testons maintenant tout – y compris ce test mis à jour – nous verrons que tout fonctionne bien :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-34.png)
_exécution finale du test_

Et c'est à peu près tout pour les tests unitaires fondamentaux des slices et de Redux en général !

## \ud83d\udd2d Perspectives pour les tests avancés

Il existe différents sujets comme les [thunks](https://redux-toolkit.js.org/api/createAsyncThunk) (ou [RTK Query](https://redux-toolkit.js.org/rtk-query/overview) comme alternative) qui pourraient également être testés. Mais je considère cela comme un sujet avancé, et cela prendrait un peu plus de temps pour expliquer ces processus.

Si vous ne visez pas à devenir un expert en tests à ce stade, les sujets que nous avons discutés pour les tests unitaires dans Redux dans ce tutoriel devraient être suffisants pour vous.

De manière générale, je recommanderais de plonger plus profondément dans les soi-disant mocks, spies, et aussi les snapshots. Ceux-ci seront utiles si vous travaillez sur d'autres tests plus avancés. 

Le truc avec `renderWithProvider()` est essentiellement basé sur un tel mock – là, nous avons artificiellement créé un store avec des reducers et un provider pour créer cette nouvelle fonction `render()`. Donc les mocks sont particulièrement utiles pour toute bibliothèque tierce, par exemple. 

Comme je l'ai dit, cependant, les mocks, les spies et les snapshots sont plus un sujet avancé à comprendre.

## \ud83d\udce3 Opportunités d'apprentissage supplémentaires

J'ai récemment commencé à travailler sur mon premier [cours Udemy gratuit](https://www.udemy.com/user/matthes-bar/). Bien que ce premier cours gratuit couvre les bases du React Redux Toolkit avec un audio en allemand et des sous-titres en anglais ajoutés manuellement, je prévois également de publier d'autres cours Udemy entièrement en anglais à l'avenir. 

J'apprécierais vraiment que vous consultiez ce cours gratuit afin de me fournir quelques commentaires.