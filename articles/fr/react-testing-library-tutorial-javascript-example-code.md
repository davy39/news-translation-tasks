---
title: React Testing Library – Tutoriel avec des exemples de code JavaScript
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-03-07T22:15:39.000Z'
originalURL: https://freecodecamp.org/news/react-testing-library-tutorial-javascript-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/react-testing-library-guide-1.png
tags: []
seo_title: React Testing Library – Tutoriel avec des exemples de code JavaScript
seo_desc: 'This post will help you to learn what the React Testing Library is, and
  how you can use it to test your React application.

  This tutorial will assume you already know some basic JavaScript and understand
  the basics of how React works.

  React Testing Li...'
---

Cet article vous aidera à comprendre ce qu'est la React Testing Library et comment l'utiliser pour tester votre application React.

Ce tutoriel suppose que vous connaissez déjà les bases de JavaScript et comprenez le fonctionnement de React.

[React Testing Library](https://testing-library.com/docs/react-testing-library/intro) est un outil d'utilitaire de test conçu pour tester l'arborescence DOM réelle rendue par React dans le navigateur. L'objectif de la bibliothèque est de vous aider à écrire des tests qui ressemblent à la manière dont un utilisateur utiliserait votre application. Cela peut vous donner plus de confiance que votre application fonctionne comme prévu lorsqu'un utilisateur réel l'utilise.

La bibliothèque fournit des méthodes utilitaires qui interrogent le DOM de la même manière qu'un utilisateur le ferait. Par exemple, un utilisateur trouverait un bouton pour "Enregistrer" son travail par son texte, donc la bibliothèque vous fournit la méthode `getByText()`. Vous allez en apprendre davantage sur les méthodes de la bibliothèque pour les tests plus tard.

Mais d'abord, voyons un exemple de React Testing Library en action.

## Comment utiliser React Testing Library

Une application React créée avec Create React App (ou CRA) inclut déjà à la fois React Testing Library et Jest par défaut. Vous n'avez donc qu'à écrire votre code de test.

Si vous souhaitez utiliser React Testing Library en dehors d'une application CRA, vous devez installer manuellement React Testing Library et Jest avec NPM :

```shell
npm install --save-dev @testing-library/react jest
```

Vous devez installer Jest car React Testing Library ne fournit que des méthodes pour vous aider à écrire les scripts de test. Vous avez donc toujours besoin d'un framework de test JavaScript pour exécuter le code de test.

Vous pouvez également utiliser d'autres frameworks de test comme Mocha ou Jasmine, mais j'utiliserai Jest car il fonctionne bien avec React et la Testing Library.

Pour ce tutoriel, je vais créer une nouvelle application React avec CRA en utilisant le modèle par défaut :

```shell
npx create-react-app react-test-example
```

Une fois l'application créée, vous devriez avoir un fichier `App.test.js` déjà généré dans le dossier src/. Le contenu du fichier serait le suivant :

```javascript
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

```

Le code de test ci-dessus a utilisé la méthode `render` de React Testing Library pour rendre virtuellement le composant `App` importé du fichier `App.js` et l'ajouter au nœud `document.body`. Vous pouvez accéder au HTML rendu via l'objet `screen`.

Pour voir le résultat de l'appel `render()`, vous pouvez utiliser la méthode `screen.debug()` :

```javascript
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  screen.debug();
});
```

Ensuite, ouvrez votre terminal et exécutez la commande `npm run test`. Vous verrez l'arborescence complète de `document.body` rendue dans votre console :

```html
<body>
  <div>
    <div class="App">
      <header class="App-header">
        <img alt="logo" class="App-logo" src="logo.svg" />
        <p>
          Edit<code> src/App.js </code>and save to reload.
        </p>
        <a
          class="App-link"
          href="https://reactjs.org"
          rel="noopener noreferrer"
          target="_blank"
        >
          Learn React
        </a>
      </header>
    </div>
  </div>
</body>
```

L'objet `screen` contient également les méthodes de test DOM déjà liées. C'est pourquoi le code de test ci-dessus a pu utiliser `screen.getByText()` pour interroger l'élément d'ancrage `<a>` par sa valeur **textContent**.

Enfin, le code de test vérifiera si l'élément de lien est disponible dans l'objet `document` ou non avec la méthode `expect` de Jest :

```javascript
expect(linkElement).toBeInTheDocument();
```

Lorsque l'élément de lien n'est pas trouvé, Jest marquera le test comme **échoué**.

## Méthodes de React Testing Library pour trouver des éléments

La plupart de vos cas de test React doivent utiliser des méthodes pour trouver des éléments. React Testing Library vous fournit plusieurs méthodes pour trouver un élément par des attributs spécifiques en plus de la méthode `getByText()` ci-dessus :

* `getByText()` : trouve l'élément par sa valeur textContent
* `getByRole()` : par sa valeur d'attribut `role`
* `getByLabelText()` : par sa valeur d'attribut `label`
* `getByPlaceholderText()` : par sa valeur d'attribut `placeholder`
* `getByAltText()` : par sa valeur d'attribut `alt`
* `getByDisplayValue()` : par sa valeur d'attribut `value`, généralement pour les éléments `<input>`
* `getByTitle()` : par sa valeur d'attribut `title`

Et lorsque ces méthodes ne suffisent pas, vous pouvez utiliser la méthode `getByTestId()`, qui vous permet de trouver un élément par son attribut `data-testid` :

```javascript
import { render, screen } from '@testing-library/react';

render(<div data-testid="custom-element" />);
const element = screen.getByTestId('custom-element');
```

Mais comme la sélection d'éléments à l'aide d'attributs `data-testid` ne ressemble pas à la manière dont un utilisateur réel utiliserait votre application, la documentation recommande de l'utiliser uniquement en dernier recours lorsque toutes les autres méthodes échouent à trouver votre élément. Généralement, la recherche par Texte, Rôle ou Libellé devrait couvrir la plupart des cas.

## Comment tester les événements générés par l'utilisateur avec React Testing Library

Outre la vérification de la présence d'éléments dans le corps de votre document, React Testing Library vous aide également à tester les événements générés par l'utilisateur, comme le clic sur un bouton et la saisie de valeurs dans une zone de texte.

La bibliothèque `user-event` est une bibliothèque compagnon pour simuler l'interaction utilisateur-navigateur. Supposons que vous avez un composant de bouton pour basculer entre les thèmes Clair et Sombre comme suit :

```javascript
import React, { useState } from "react";

function App() {
  const [theme, setTheme] = useState("light");

  const toggleTheme = () => {
    const nextTheme = theme === "light" ? "dark" : "light";
    setTheme(nextTheme);
  };

  return <button onClick={toggleTheme}>
      Current theme: {theme}
    </button>;
}

export default App;

```

Ensuite, vous créez un test qui trouve le bouton et simule un événement de clic en utilisant la méthode `userEvent.click()`. Une fois le bouton cliqué, vous pouvez vérifier que le test est un succès en inspectant si le texte de l'élément bouton contient "dark" ou non :

```javascript
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import App from "./App";

test("Test theme button toggle", () => {
  render(<App />);
  const buttonEl = screen.getByText(/Current theme/i);
    
  userEvent.click(buttonEl);
  expect(buttonEl).toHaveTextContent(/dark/i);
});
```

Et c'est ainsi que vous pouvez simuler des événements utilisateur avec React Testing Library. La bibliothèque `user-event` dispose également de plusieurs autres méthodes comme `dblClick` pour double-cliquer sur un élément et `type` pour taper dans une zone de texte. Vous pouvez consulter la [documentation de la bibliothèque `user-event`](https://testing-library.com/docs/ecosystem-user-event) pour plus d'informations.

## Conclusion

> Plus vos tests ressemblent à la manière dont votre logiciel est utilisé, plus ils peuvent vous donner de confiance.   
> (Source : [Kent C. Dodds](https://twitter.com/kentcdodds/status/977018512689455106), Auteur de React Testing Library)

Un utilisateur réel ne verra pas les détails d'implémentation comme l'état ou les props actuellement dans vos composants React. Ils ne voient que les éléments HTML rendus dans le navigateur. React Testing Library vous encourage à tester le comportement de votre application plutôt que les détails d'implémentation.

En testant votre application de la manière dont un utilisateur l'utiliserait, vous pouvez être confiant que votre application se comportera comme prévu lorsque tous les cas de test auront passé. Pour plus d'informations, vous pouvez visiter la [documentation de React Testing Library](https://testing-library.com/docs/react-testing-library/example-intro).

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !