---
title: Comment ajouter un hook de base de données sans faille à vos projets React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-12T21:17:09.000Z'
originalURL: https://freecodecamp.org/news/add-a-database-hook-to-react-and-react-native
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/caspar-camille-rubin-0qvBNep1Y04-unsplash-1.jpg
tags:
- name: database
  slug: database
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment ajouter un hook de base de données sans faille à vos projets React
seo_desc: "By Michael Bagley\nIntroduction\nReact is one of the best libraries for\
  \ creating stateful interfaces, and is an essential part of the internet as we know\
  \ it. \nMany web apps including Twitter, Facebook, Instagram, and Airbnb depend\
  \ on this library to de..."
---

Par Michael Bagley

## Introduction

React est l'une des meilleures bibliothèques pour créer des interfaces étatiques, et fait partie intégrante d'Internet tel que nous le connaissons.

De nombreuses applications web, dont Twitter, Facebook, Instagram et Airbnb, dépendent de cette bibliothèque pour fournir des applications étatiques et multiplateformes à des _milliards_ d'utilisateurs. Elle continue d'être l'une des bibliothèques les plus populaires de sa catégorie.

## React Hooks – Un changement de jeu

React 16.8 a introduit un **nouveau modèle de développement** appelé _hooks_. Cette nouvelle fonctionnalité a propulsé la bibliothèque à un tout nouveau niveau et a rendu plus facile que jamais l'écriture et la compréhension des composants dans le contexte de fonctions, plutôt que de classes.

Regardez [ce Gif](https://twitter.com/prchdk/status/1056960391543062528) pour voir à quel point ces composants fonctionnels peuvent être plus efficaces du point de vue du développeur :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/ezgif.com-gif-maker-10.43.02-AM-2.gif)
_Twitter : Pavel @prchdk_

Il existe divers types de hooks dans React, et il y a une raison à cela. Différentes tâches nécessitent différents hooks, de la sauvegarde de variables à la mémorisation de fonctions.

Beaucoup de ces hooks comportent ce qu'on appelle un _tableau de dépendances_. Le hook surveille les changements des variables dans le tableau, et se réexécute si des changements sont observés.

Prenons l'exemple du hook `useEffect`. Ce hook s'exécute lorsqu'un composant est monté pour la première fois et chaque fois que les variables étatiques dans ce tableau de dépendances changent :

```js
const [count, setCount] = useState(0);

useEffect(() => {
  console.log(count); 
}, [count]);
```

Dans l'extrait de code ci-dessus, `count` sera enregistré dans deux situations :

1. Lorsque le composant est monté pour la première fois
2. Lorsque vous utilisez `setCount` pour changer la valeur de `count`

Bien qu'il y ait [beaucoup plus à explorer concernant les hooks](https://reactjs.org/docs/hooks-reference.html), comprendre le concept ci-dessus est essentiel pour la suite de cet article. C'est parce que nous allons démontrer comment vous pouvez utiliser ce tableau de dépendances pour récupérer automatiquement vos données centrales, de manière similaire à la réexécution du hook `useEffect`.

## Configuration de la base de données

Presque chaque instance de production d'une application React utilise une base de données à un moment donné, que ce soit pour stocker des informations utilisateur, des informations commerciales ou des données API.

Il existe de nombreuses façons d'implémenter une base de données dans vos applications React ou React Native, mais il y a quelques méthodes spécifiques qui s'intègrent parfaitement avec les modèles de programmation React, et spécifiquement les _hooks_.

Parmi les diverses solutions hébergées pour vos applications React, vous trouverez le plus d'avantages à utiliser [l'architecture serverless](https://easybase.io/about/2021/01/30/What-Is-a-Serverless-Application/). Je pourrais écrire sur tous les avantages de l'architecture serverless, mais cela pourrait bien être un article à part entière. Juste pour en lister quelques-uns :

* Mise à l'échelle automatique à la demande
* Super facile à déployer
* Oubliez la gestion et la maintenance du serveur
* Plus de temps pour l'UI/UX
* Les coûts généraux passent à 0

La méthode démontrée ci-dessous combine tous les avantages du développement d'applications serverless avec un hook personnalisé qui fonctionne _sans faille_ avec l'écosystème de programmation React.

Pour ceux qui se demandent, oui, la bibliothèque présentée ci-dessous fonctionne également avec React Native pour les développeurs mobile-first.

Nous allons finir par avoir un hook appelé `useReturn` qui retournera toujours une instance fraîche d'une requête donnée. Cela ressemblera à quelque chose comme ceci :

```jsx
const [minRating, setMinRating] = useState(0);
const { frame } = useReturn(() => /* Votre requête */, [minRating])

return <div>{frame.map(ele => <Card {...ele} />)}</div>
```

Ne vous inquiétez pas si cela semble incohérent pour l'instant. Vous pourrez adapter votre cas d'utilisation parfaitement dans quelques minutes.

Notez que dans l'exemple, l'instance `frame`, qui est un tableau d'enregistrements de votre base de données, sera mise à jour dans deux situations :

1. `minRating` (ou tout ce qui est dans le tableau de dépendances) change
2. Une autre instance de la base de données (`db`) crée, met à jour ou supprime des données

## Configuration de React

Cette section démontrera brièvement comment créer un projet React. Si vous êtes déjà familier, n'hésitez pas à passer à la partie suivante.

L'équipe de développement de React a créé un script facile à utiliser appelé `create-react-app`. Le seul prérequis est que votre machine ait `node` et `npm` installés, ce dont vous aurez besoin de toute façon.

Suivez donc [les instructions ici](https://nodejs.org/en/download/) pour installer rapidement ces packages si vous ne les avez pas déjà.

Ouvrez l'invite de commande ou le terminal dans le répertoire où vous souhaitez placer votre nouveau projet. Exécutez la commande suivante :

```
# npx create-react-app serverless-app
```

Une fois ce processus terminé, allez dans le répertoire `serverless-app` et démarrez le projet comme suit :

```
# cd serverless-app
# npm run start
```

Cela créera une instance locale de votre application qui se rechargera automatiquement (connu sous le nom de _hot loading_) lorsque vos fichiers situés dans le dossier `src/` seront modifiés. Une fenêtre de navigateur devrait s'ouvrir automatiquement. Si ce n'est pas le cas, ouvrez votre navigateur web et rendez-vous sur `http://localhost:3000`.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-07-at-6.24.05-PM-1.png)

## Configuration d'Easybase

Installons une bibliothèque appelée `easybase-react` en nous rendant dans notre répertoire de projet et en exécutant `npm install easybase-react`. C'est la seule dépendance dont nous aurons besoin pour cette démonstration.

Ensuite, créez un compte sur [easybase.io](https://easybase.io) (vous pouvez utiliser le niveau gratuit).

Une fois connecté, utilisez le bouton '**+ Create**' pour créer une nouvelle table. Nommons-la _MY TABLE_ et donnons-lui trois colonnes : rating (nombre), poster (image) et title (chaîne de caractères).

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-07-at-7.32.27-PM-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-07-at-7.38.46-PM-1.png)

Cliquez sur _next_ et terminez la création de votre nouvelle table. Elle s'ouvrira automatiquement, mais vous pouvez également développer le bouton _Tables_ dans le tiroir de gauche pour la sélectionner là aussi.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-07-at-7.44.11-PM-1.png)

À des fins de démonstration, ajoutons une ligne d'exemple afin de pouvoir l'afficher dans notre application React. Utilisez le bouton '**+**' en haut à gauche de la table pour ajouter une nouvelle ligne.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-07-at-7.47.40-PM-1.png)

Mon exemple présentera des données de films, mais n'hésitez pas à utiliser le type de données qui convient le mieux à votre application.

La dernière étape avant de retourner au code est de créer un nouveau _Project_ dans l'interface Easybase. Cela nous donnera un fichier de configuration qui donnera à notre application un accès sécurisé à la base de données. Gardez ce fichier de configuration privé, car il contient des informations d'identification qui peuvent être utilisées pour accéder à vos données.

Dans le tiroir de gauche, allez dans '**Projects > Create Project**'.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-07-at-7.51.18-PM-1.png)

Allez dans _permissions_. Cliquez sur le nom de votre table et activez '**Users not signed in > Read, Write**'.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-08-at-1.32.24-PM-1.png)

**N'oubliez pas de cliquer sur 'Save'.**

Enfin, allez dans l'onglet _Project Token_ et téléchargez votre jeton de configuration personnalisé.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-08-at-1.33.20-PM-1.png)

Placez ce jeton dans votre projet React à côté de `App.js`, de sorte que la structure ressemble à quelque chose comme ceci :

```
├ ...
├ ebconfig.js
├ App.css
├ App.js
├ index.js
└ ...
```

Maintenant, retournons au code. Ouvrez le fichier `src/index.js` dans votre projet React. Tout d'abord, importez _EasybaseProvider_ depuis le package `easybase-react` que nous avons installé précédemment **et** notre jeton personnalisé `ebconfig.js`. Ensuite, enveloppez `<App />` avec `<EasybaseProvider ebconfig={ebconfig} >` :

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import ebconfig from './ebconfig'; // Ajoutez ceci
import { EasybaseProvider } from 'easybase-react'; // Ajoutez ceci

ReactDOM.render(
  <React.StrictMode>
    <EasybaseProvider ebconfig={ebconfig}> {/* <-- */}
      <App />
    </EasybaseProvider> {/* <-- */}
  </React.StrictMode>,
  document.getElementById('root')
);
```

**N'oubliez pas de passer votre fichier de configuration dans la prop _ebconfig_.**

Cette configuration, connue sous le nom de _provider pattern_, donne à tous les composants de notre projet React un accès valide au contexte de ce fournisseur et c'est la meilleure façon d'organiser l'état à travers vos composants (en plus, c'est nativement supporté). Dans notre cas, c'est un hook appelé `useEasybase`.

### Hook useEasybase

À ce stade, la configuration du projet est complète. Rendez-vous dans `src/App.js`, supprimez les imports et tout ce qui se trouve dans la fonction `App`.

Maintenant, configurons notre premier composant avec le package `easybase-react`. Ce processus peut être répliqué dans votre projet pour [n'importe quelle des propriétés de](https://easybase.io/docs/easybase-react/interfaces/types_types.contextvalue.html) `[useEasybase](https://easybase.io/docs/easybase-react/interfaces/types_types.contextvalue.html)` [(P.S. il y en a beaucoup)](https://easybase.io/docs/easybase-react/interfaces/types_types.contextvalue.html).

Tout d'abord, importez `useEasybase` depuis le package `easybase-react`. Récupérons `useReturn`, `db`, et `e` comme suit :

```jsx
import { useEasybase } from 'easybase-react';

function App() {
  const { useReturn, db, e } = useEasybase();
  return (
  
  );
}

export default App;
```

Vous vous demandez probablement – quelles sont ces fonctions ?

`db` – Comme son nom l'indique, cette fonction nous donne accès à notre base de données. Elle fonctionne comme suit :

```js
let records = await db('MY TABLE').return().all()
```

C'est un exemple très simple, mais la fonction `db` est assez puissante. [En savoir plus ici.](https://easybase.github.io/EasyQB/)

`e` – Cela signifie _expressions_. Utilisez-le dans la fonction `db` pour construire des requêtes dans la fonction `.where` de `db`. Utilisez des fonctions telles que [`eq` (égale)](https://easybase.github.io/EasyQB/docs/operations.html#equal), [`neq` (non égale)](https://easybase.github.io/EasyQB/docs/operations.html#not-equal), [`lt` (inférieure à)](https://easybase.github.io/EasyQB/docs/operations.html#less-than), [`or` (OU)](https://easybase.github.io/EasyQB/docs/operations.html#or), [et bien d'autres](https://easybase.github.io/EasyQB/docs/operations.html) sous la forme `e.eq("column_name", value)`. Cela interrogerait les enregistrements où _column_name_ est égal à la valeur de _value_.

Maintenant, nous pouvons utiliser les _expressions_ pour faire une requête composée :

```js
let records = await db('MY TABLE').return(e.avg('rating')).where(e.or(e.like('title', 'T%'), e.lt('rating', 80))).all();

// e.avg = Retourne la moyenne de 'rating' où :
//   e.or = Instruction OR sur : 
//     e.like = motif de correspondance de chaîne [title commence par 'T'] 
//     e.lt = inférieur à [rating < 80]
```

[Il y a beaucoup plus d'opérations disponibles pour vous, y compris des agrégateurs puissants](https://easybase.github.io/EasyQB/docs/operations.html).

`useReturn` – Enfin, voici le hook mentionné précédemment. Il fonctionne en enveloppant la fonction `db`. Le hook s'abonne automatiquement aux changements dans `db`. Plus important encore, il nous donnera accès à un tableau de données étatiques, appelé `frame`.

```js
const { useReturn, db, e } = useEasybase();
const { frame } = useReturn(() => db().return()
  .where(e.gt('rating', minRating)) // Où rating > minRating     
  .limit(limit),                    // Limiter la longueur de la requête 
[minRating, limit]); // Retourne également quelques helpers : 
                     //   'error' - any
                     //   'loading' - boolean
                     //   'manualFetch' - async function
                     //   'unsubscribe' - function
```

**N'utilisez pas `.all` ou `.one` dans le hook `useReturn`**, cela est géré automatiquement. Pour plus d'informations, [consultez la documentation ici](https://easybase.io/docs/easybase-react/interfaces/types_types.contextvalue.html#usereturn).

### Le premier composant

Utilisons ces fonctions dans notre fichier `src/App.js` vide comme suit :

```jsx
import { useEasybase } from "easybase-react";

function App() {
  const { useReturn, db, e } = useEasybase();
  const { frame } = useReturn(() => db("MY TABLE").return(), []);
  
  return (
    <div>{frame.map(ele => JSON.stringify(ele))}</div>
  );
}

export default App;
```

À titre de démonstration, cela affichera simplement une représentation sous forme de chaîne de l'enregistrement unique qui se trouve actuellement dans la table :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-11.15.46-AM-1.png)

**Félicitations, votre base de données est en ligne et fonctionne.** Maintenant, implémentons un composant personnalisé, appelé `<Card />`, qui donnera à nos enregistrements une structure dans l'UI (n'hésitez pas à mettre ces composants dans des fichiers séparés pour l'organisation) :

```jsx
function Card({ rating, poster, title, _key }) {
  const cardStyle = {
    display: "inline-block",
    margin: 10,
    padding: 10,
    borderRadius: 10,
    background: "#eaeaea",
    minWidth: 200,
  };

  return (
    <div style={cardStyle}>
      <img 
        src={poster} 
        style={{ height: 300, minWidth: 200 }} 
      />
      <h2>{title}</h2>
      <h4>Rating: {rating}</h4>
    </div>
  );
}

function App() {
  const { useReturn, db, e } = useEasybase();
  const { frame } = useReturn(() => db("MY TABLE").return(), []);

  return (
    <div style={{ textAlign: "center", display: "inline-block" }}>
      {frame.map(ele => <Card {...ele} />)}
    </div>
  );
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-1.26.45-PM-1.png)

Cela a l'air _beaucoup_ mieux. Pour des raisons de brièveté, je vais garder mon style simple. N'hésitez pas à donner au projet votre propre apparence !

Vous pouvez voir que le `<Card />` utilise toutes les propriétés de l'enregistrement original comme ses props, plus une prop appelée __key_. __key_ est un identifiant unique pour chaque enregistrement qui est retourné avec les autres propriétés. Cela sera très utile pour interroger et mettre à jour des enregistrements spécifiques. Plus d'informations à ce sujet plus tard.

### Insérer un enregistrement

Maintenant, implémentons rapidement un moyen d'ajouter une nouvelle carte à notre base de données. Cela démontrera également comment le hook `useReturn` se rafraîchit automatiquement lorsque nous ajoutons un enregistrement avec différents composants.

Après avoir _mappé_ le tableau frame, affichons un nouveau bouton :

```jsx
// ...

function AddCardButton() {
  const addCardStyle = {
    background: "#ea55aa",
    display: "inline-block",
    width: 200,
    borderRadius: 10,
    cursor: "pointer",
  };

  return (
    <div style={addCardStyle}>
      <h2 style={{ color: "#fff" }}>Add Card</h2>
    </div>
  );
}

function App() {
  const { useReturn, db, e } = useEasybase();
  const { frame } = useReturn(() => db("MY TABLE").return(), []);

  return (
    <div style={{ textAlign: "center", display: "inline-block" }}>
      {frame.map(ele => <Card {...ele} />)}
      <AddCardButton /> {/* <- Nouveau bouton */}
    </div>
  );
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-1.26.26-PM-1.png)

Il existe de nombreuses façons différentes de collecter les entrées utilisateur dans une application React ou React Native. Dans ce cas, j'utiliserai la fonction intégrée `[prompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt)`, mais vous pouvez utiliser des formulaires, des dialogues, etc.

Une fois que nous avons collecté les détails du nouvel enregistrement, téléchargez-les en utilisant la fonction `db`. Donc, utilisons à nouveau le hook `[useEasybase](https://easybase.io/docs/easybase-react/interfaces/types_types.contextvalue.html)`. Au lieu de `.return`, nous utiliserons `[.insert](https://easybase.github.io/EasyQB/docs/insert_queries.html#insert)` (nous explorerons le téléchargement d'images plus tard).

En code, l'implémentation pourrait ressembler à ceci :

```jsx
function AddCardButton() {
  // ...
  
  const { db } = useEasybase();
  async function addCardClick() {
    let title = prompt("Please enter a movie title");
    let rating = prompt("Please enter the rating for this movie");
    if (!rating || !title) {
      return;
    }

    db("MY TABLE")
      .insert({ title, rating: Number(rating) })
      .one();
  }

  return (
    <div style={addCardStyle} onClick={addCardClick}> {/* <- onClick */}
      <h2 style={{ color: "#fff" }}>Add Card</h2>
    </div>
  );
}
```

Cliquez sur ce nouveau bouton et entrez quelques valeurs.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-1.39.55-PM-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-1.40.46-PM-1.png)

**Le voilà, le nouvel enregistrement !**

Enfin, ajoutons l'image correspondante avec la fonction `[setImage](https://easybase.io/docs/easybase-react/interfaces/types_types.contextvalue.html#setimage)`, depuis `useEasybase`. Les médias (image, vidéo, fichier) sont traités différemment des autres valeurs et doivent être _téléversés_, plutôt que _insérés_.

C'est ici que nous pouvons enfin utiliser cette propriété **_key** pour identifier de manière unique l'enregistrement actuel. Cette propriété est également couramment utilisée avec `db.set`, `db.delete`, et ainsi de suite.

Lorsque l'utilisateur clique sur une image (ou l'espace vide de l'image), il pourra téléverser une nouvelle image. `useReturn` démontrera une fois de plus qu'il rafraîchit automatiquement les nouvelles données.

Retournez au composant `<Card />` et utilisez le hook `useEasybase`. Utiliser une entrée _cachée_ est une astuce courante pour faire apparaître une image comme une entrée de fichier également :

```jsx
function Card({ rating, poster, title, _key }) {
  // ...

  const { setImage } = useEasybase();
  async function onFileChange(e) {
    if (e.target.files[0]) {
      await setImage(_key, "poster", e.target.files[0], "MY TABLE");
    }
  }

  return (
    <div style={cardStyle}>
      <input id={"fileInput" + _key} hidden type="file" onChange={onFileChange} />
      <img
        src={poster}
        style={{ height: 300, minWidth: 200 }}
        onClick={_ => document.getElementById("fileInput" + _key).click()}
      />
      <h2>{title}</h2>
      <h4>Rating: {rating}</h4>
    </div>
  );
}
```

Maintenant, cliquer sur une image `<Card />` fera apparaître un sélecteur de fichiers. Utilisez ce sélecteur pour téléverser une image depuis votre machine.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-3.58.27-PM-1.png)

**Ça marche !** Les images téléversées seront disponibles via le CDN Easybase et attachées à votre enregistrement. Le `frame` devrait les afficher automatiquement.

Remarquez que ces changements sont également reflétés dans l'application web Easybase :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-4.59.46-PM-1.png)

### Requête

Ajoutons un composant de plus pour démontrer comment utiliser le _tableau de dépendances_ du hook `useReturn`.

À titre de démonstration, je vais implémenter une entrée numérique qui, lorsqu'elle est modifiée, met à jour la requête utilisée dans le hook `useReturn`.

Typiquement, vous utiliserez une _expression_ dans la fonction `db.where` pour ces requêtes étatiques. Voici un exemple simple, enveloppant la racine `<App />` et ajoutant une entrée contrôlée. Remarquez la nouvelle variable _ratingMin_ :

```jsx
import { useEasybase } from "easybase-react";

// ...

function App() {
  const [ratingMin, setRatingMin] = useState(0); // <- pour la nouvelle entrée
  const { useReturn, db, e } = useEasybase();
  const { frame } = useReturn(() => db("MY TABLE").return(), []);

  return (
    <div>
      <div style={{ textAlign: "center", display: "inline-block" }}>
        {frame.map(ele => <Card {...ele} />)}
        <AddCardButton />
      </div>
      <p>
        Rating filter:
        <input
          type="number"
          value={ratingMin} // entrée contrôlée
          onChange={e => setRatingMin(Number(e.target.value))}
        />
      </p>
    </div>
  );
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-5.55.55-PM-1.png)

Il ne reste plus qu'à utiliser _ratingMin_ dans la fonction `db` **et** à le placer dans le _tableau de dépendances_. Nous utiliserons `e.gte('rating', ratingMin)` pour interroger les enregistrements avec une 'rating' (nom de colonne) supérieure ou égale à `ratingMin` :

```js
function App() {
  const [ratingMin, setRatingMin] = useState(0); // <- pour la nouvelle entrée
  const { useReturn, db, e } = useEasybase();
  const { frame } = useReturn(
    () => db("MY TABLE").return().where(e.gte("rating", ratingMin)),
    [ratingMin]
  );
  // ...
}
```

Et voilà, votre `frame` répond aux changements d'état et met à jour la requête en conséquence :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-6.05.10-PM-1.png)

Vous pouvez ajouter autant d'enregistrements que vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-09-at-6.19.14-PM-1.png)

Tous ces changements seront synchronisés avec votre base de données distante. Astuce pro : utilisez `[.limit](https://easybase.github.io/EasyQB/docs/select_queries.html#limit)` et `[.offset](https://easybase.github.io/EasyQB/docs/select_queries.html#offset)` pour implémenter la pagination si vous avez des milliers ou même des dizaines de milliers d'enregistrements.

## Conclusion

Le package [`easybase-react`](https://github.com/easybase/easybase-react) propose de nombreuses fonctions utiles que vous trouverez probablement utiles, notamment en ce qui concerne l'authentification des utilisateurs et la base de données.

Si vous souhaitez voir toutes les fonctionnalités de cette bibliothèque avec React et React Native, [consultez ce guide](https://easybase.io/react/).

Le [constructeur de requêtes présenté dans cet article](https://easybase.github.io/EasyQB/) fonctionne de manière similaire à la syntaxe utilisée dans la base de données de Firebase et est assez flexible. Par exemple, un cas d'utilisation avancé serait de sélectionner des colonnes avec des _agrégateurs_, tels que `[e.min](https://easybase.github.io/EasyQB/docs/operations.html#minimum)` et `[e.max](https://easybase.github.io/EasyQB/docs/operations.html#maximum)`.

De plus, si vous avez une logique métier plus complexe dans votre application, essayez le gestionnaire `[dbEventListener](https://easybase.io/docs/easybase-react/interfaces/types_types.contextvalue.html#dbeventlistener)`. Cela exécutera une fonction de rappel chaque fois qu'une instance `db` exécute une requête. Il est également retourné par le hook `useEasybase`.

**Merci d'avoir lu !** Il s'agit d'une introduction brève et simple à un hook de base de données compatible avec React et à la _programmation serverless_, une architecture de programmation populaire parmi les individus et les petites équipes.

Cette popularité vient de l'absence d'une configuration backend traditionnelle, qui implique des coûts, du temps et une gestion importants.

J'espère que ce guide a aidé ceux qui sont intéressés à déployer des applications React/React Native prêtes pour la production avec le hook `useReturn` d'Easybase.