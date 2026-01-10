---
title: Comment déployer des fonctions cloud dynamiques dans React et React Native
  avec Easybase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-13T18:37:52.000Z'
originalURL: https://freecodecamp.org/news/cloud-functions-in-react-with-easybase
coverImage: https://cdn-media-2.freecodecamp.org/w1280/606b5c58d5756f080ba94a3a.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: Comment déployer des fonctions cloud dynamiques dans React et React Native
  avec Easybase
seo_desc: "By Michael Bagley\nCloud functions are stateless, single-purpose code snippets\
  \ that can be invoked programmatically or through other event-driven processes.\
  \ \nThese code snippets are not built into your application, as a traditional function\
  \ would be. ..."
---

Par Michael Bagley

Les fonctions cloud sont des extraits de code sans état, à usage unique, qui peuvent être invoqués de manière programmatique ou via d'autres processus pilotés par événements. 

Ces extraits de code ne sont pas intégrés à votre application, comme le serait une fonction traditionnelle. Ils sont plutôt **stockés dans un conteneur cloud** maintenu par un fournisseur. Ils peuvent être modifiés en direct et masquer la logique métier du code front-end disponible localement.

React et React Native peuvent grandement bénéficier de cette méthode de développement d'applications grâce à leur style de programmation déclaratif. Les événements dans l'UI peuvent appeler votre fonction de manière prévisible et compatible avec React. Essayons cela !

## **Installation**

Nous allons commencer par créer une toute nouvelle application React ou React Native. Le moyen le plus simple de créer l'un de ces projets est d'utiliser `npx`, qui est inclus avec une installation standard de Node.js. Si vous n'avez pas ces modules installés, vous pouvez [les installer ici](https://nodejs.org/en/). 

À partir de là, nous pouvons créer un nouveau projet comme suit :

React : `npx create-react-app my-cloud-app`

React Native : `npx create-react-native-app`

Une fois l'installation terminée, déplacez-vous dans votre nouveau répertoire de projet et exécutez `npm run start`. Voici à quoi ressemble mon projet React de départ :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-11.03.51-AM.png)

## **Exemple de projet React**

Le projet React que je vais créer est un **simple récupérateur de prix de cryptomonnaies**. 

L'interface utilisateur comportera une zone de texte et un bouton où les utilisateurs pourront soumettre le symbole d'une cryptomonnaie comme 'BTC' ou 'ETH'. À partir de là, le front-end appellera une fonction serverless, hébergée par Easybase. La fonction cloud appellera une API et retournera le prix spécifié en USD.

Tout d'abord, ajoutons ces éléments d'interface à nos éléments React. Ouvrez `src/App.js` et videz le composant sous la balise racine `header`. Pour commencer, nous aurons besoin de quatre éléments :

1. Une zone de texte
2. Un élément de texte pour indiquer à l'utilisateur de saisir un symbole de cryptomonnaie
3. Un bouton pour invoquer la fonction cloud en fonction de la saisie de la zone de texte
4. Enfin, nous avons besoin d'un autre élément de texte pour afficher le résultat produit

Votre fonction `App` peut maintenant ressembler à ce qui suit :

```jsx
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Entrez le symbole de la cryptomonnaie :</p>
        <input placeholder="BTC, ETH, etc." type="text" />
        <button>Go</button>
        <p>Résultat :</p>
      </header>
    </div>
  );
}
```

Enregistrez ce fichier et votre nouvelle application ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-11.46.38-AM.png)

**Super !** Maintenant, nous devons rendre notre application stateful, de sorte que nous sauvegardions la saisie de l'utilisateur et que nous ayons un callback pour notre bouton. 

Nous utiliserons le hook `useState` de React pour stocker et afficher la saisie de l'utilisateur. Créez également une fonction asynchrone appelée `buttonCallback` qui est déclenchée lorsque l'utilisateur clique sur le bouton 'Go'. Pour l'instant, cette fonction se contentera d'imprimer la saisie de la zone de texte.

Voici mon implémentation de `src/App.js` pour référence :

```jsx
import { useState } from 'react';
import './App.css';

function App() {
  const [inputVal, setInputVal] = useState("");

  async function buttonCallback() {
    console.log(inputVal);
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>Entrez le symbole de la cryptomonnaie :</p>
        <input placeholder="BTC, ETH, etc." type="text" value={inputVal} onChange={e => setInputVal(e.target.value)} />
        <button onClick={buttonCallback}>Go</button>
        <p>Résultat :</p>
      </header>
    </div>
  );
}

export default App;
```

## **Comment déployer votre fonction cloud**

Jusqu'à présent, **tout fonctionne comme prévu**. Il est temps de déployer un extrait de code dans le cloud. [Créez un compte gratuit sur easybase.io](https://easybase.io/) et cliquez sur le bouton **'+'** en bas à gauche de la vue.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-1.04.33-PM.png)

Sélectionnez le modèle _Hello World_ et suivez les étapes. Cela ouvrira une fonction qui retourne simplement ce qui est passé pour la valeur de _message_ dans le corps de la requête.

L'éditeur de code [Monaco](https://microsoft.github.io/monaco-editor/) est intégré directement au site web, donc nous pouvons coder en direct dans notre navigateur web ! 

Nous allons avoir besoin d'un package de npm qui nous aide à faire des requêtes vers des API externes. Ouvrez `package.json` et ajoutez le module _[cross-fetch](https://www.npmjs.com/package/cross-fetch)_ avec la version appropriée (lorsque nous sauvegardons notre fonction, ce module sera automatiquement installé) :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-1.12.00-PM.png)

Maintenant, rouvrez `handler.js` et importez le module nouvellement installé en haut du fichier avec `var fetch = require('cross-fetch');`.

Lorsque nous faisons notre requête depuis le front-end, nous passerons un objet avec la clé `cryptoSymbol` représentant la valeur de saisie de la zone de texte. Donc, créons une variable pour sauvegarder cela. N'oubliez pas que `event.body` fera référence à ce qui est passé dans la fonction via le corps de la requête.

```js
const cryptoSymbol = event.body.cryptoSymbol;
```

Nous allons utiliser l'API [Cryptonator](https://www.cryptonator.com/api/) pour récupérer les prix actuels. La route pour obtenir les prix est `https://api.cryptonator.com/api/ticker/**_pair_name_**` où `**_pair_name_**` est le symbole donné (trois lettres) suivi de '-usd'. 

La raison pour laquelle nous suivons le nom de la paire avec '-usd' est que nous voulons obtenir le prix de la cryptomonnaie donnée en dollars, mais vous pourriez utiliser un autre symbole pour une conversion de prix d'actifs différente. Créons une variable pour cette URL :

```js
const nexchangeUrl = `https://api.cryptonator.com/api/ticker/${cryptoSymbol}-usd`;
```

Voici le **modèle complet** pour notre nouvelle fonction :

```js
var fetch = require('cross-fetch');

module.exports = async (event, context) => {
  const cryptoSymbol = event.body.cryptoSymbol;
  const nexchangeUrl = `https://api.cryptonator.com/api/ticker/${cryptoSymbol}-usd`;

  const res = await fetch(nexchangeUrl);
  const resJson = await res.json();
  if (resJson.success) {
    return context.succeed(resJson.ticker.price);
  } else {
    return context.fail("Le symbole n'existe pas");
  }
}
```

Note : `context.succeed` et `context.fail` envoient tous deux ce qui est passé au client demandeur.

Enregistrez la fonction :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-1.50.55-PM.png)

Nous pouvons développer la ligne **Deploy** et tester la fonction. Ajoutez `cryptoSymbol` au corps de l'entrée avec la valeur d'un symbole de crypto (BTC, ETH, etc).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-1.52.58-PM.png)

**Félicitations, votre fonction cloud fonctionne !** La première fois que vous appelez votre fonction, cela peut prendre quelques secondes, car elle effectue un _démarrage à froid_. Les démarrages à froid se produisent lorsque votre fonction n'a pas été invoquée récemment, elle est donc déchargée du back-end du fournisseur. Elle sera réactive lorsqu'elle sera appelée activement.

Maintenant, retournons à notre application React/React Native. Rendez-vous dans votre répertoire de projet et installez la bibliothèque [`easybase-react`](https://github.com/easybase/easybase-react).

```bash
cd my-cloud-app
npm install easybase-react
```

Maintenant, dans notre fichier `src/App.js`, nous pouvons importer une fonction appelée `[callFunction](https://easybase.io/docs/easybase-react/modules/_callfunction_.html#callfunction)` depuis ce package nouvellement installé avec `import { callFunction } from 'easybase-react'.

Cette fonction prend deux paramètres :

1. La route de la fonction (disponible sous **Deploy** --> Deploy)
2. Objet du corps de la requête, accessible dans `event.body` de notre fonction cloud (Optionnel)

Voici où vous pouvez trouver votre route de fonction :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-5.48.34-PM.png)

Dans notre fonction `buttonCallback`, utilisez la fonction importée `callFunction` pour invoquer notre fonction cloud comme détaillé. **Notez que `callFunction` est asynchrone**  les deux méthodes de programmation fonctionneront :

```js
const result = await callFunction('YOUR-CUSTOM-ROUTE', { cryptoSymbol: "BTC" });
console.log(result);

// OU

callFunction('YOUR-CUSTOM-ROUTE', { cryptoSymbol: "BTC" }).then(result => console.log(result));
```

Dans notre application, nous voulons afficher le résultat dans la dernière balise `<p>`. Nous allons faire cela avec une autre instance `useState`, de sorte que la balise ressemblera maintenant à `<p>Résultat : {resultVal}</p>`. La variable `resultVal` sera définie dans notre fonction `buttonCallback` comme suit :

```js
  async function buttonCallback() {
    const result = await callFunction('YOUR-CUSTOM-ROUTE', { cryptoSymbol: inputVal });
    setResultVal(`${inputVal} coûte actuellement $${result}`);
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-12-at-6.03.36-PM.png)

Saisissez un symbole de crypto dans la zone de texte et cliquez sur 'Go'  cela fonctionne ! Pour référence, voici mon implémentation complète (n'hésitez pas à prendre ce code et à lui donner un style pour un look et une sensation uniques) :

```jsx
import { useState } from 'react';
import './App.css';
import { callFunction } from 'easybase-react';

function App() {
  const [inputVal, setInputVal] = useState("");
  const [resultVal, setResultVal] = useState("");

  async function buttonCallback() {
    const result = await callFunction('YOUR-CUSTOM-ROUTE', { cryptoSymbol: inputVal });
    setResultVal(`${inputVal} coûte actuellement $${result}`);
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>Entrez le symbole de la cryptomonnaie :</p>
        <input placeholder="BTC, ETH, etc." type="text" value={inputVal} onChange={e => setInputVal(e.target.value)} />
        <button onClick={buttonCallback}>Go</button>
        <p>Résultat : {resultVal}</p>
      </header>
    </div>
  );
}

export default App;

```

## **Conclusion**

J'espère que ce bref tutoriel a été utile pour ceux qui s'intéressent à l'informatique en cloud et au développement d'applications serverless ! [Il existe de nombreux frameworks/bibliothèques différents disponibles pour développer des interfaces utilisateur et des applications](https://easybase.io/best-javascript-framework-library-quiz/), mais React et React Native se sont avérés être de grandes options robustes avec des communautés dynamiques.

Pour ceux qui sont intéressés, voici quelques [informations complètes sur l'utilisation d'Easybase avec React/React Native](https://easybase.io/react/). Le package [`easybase-react`](https://github.com/easybase/easybase-react) peut gérer d'autres modules d'application tels que l'authentification des utilisateurs.

Votre fonction serverless restera inactive dans le cloud lorsqu'il n'y a pas de trafic, **évitant ainsi tout frais**. Si votre application connaît une augmentation de l'utilisation, le fournisseur cloud sera là pour fournir de manière _élastique_ les performances requises. 

[Cette infrastructure, connue sous le nom d'informatique serverless, met le fardeau de la gestion, de la mise à l'échelle et de la préparation sur l'hôte](https://easybase.io/about/2021/01/30/What-Is-a-Serverless-Application/). Le meilleur aspect est qu'il n'y a aucune maintenance requise de votre part. Consultez également mon autre tutoriel sur [freeCodeCamp concernant les bases de données serverless pour React & React Native](https://www.freecodecamp.org/news/how-to-add-a-serverless-database-to-react-projects-and-web-apps/). 

_Merci d'avoir lu et bon codage !_