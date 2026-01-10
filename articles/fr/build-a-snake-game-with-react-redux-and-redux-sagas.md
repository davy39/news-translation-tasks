---
title: Comment créer un jeu Snake avec React, Redux et Redux Saga
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2022-02-09T18:03:35.000Z'
originalURL: https://freecodecamp.org/news/build-a-snake-game-with-react-redux-and-redux-sagas
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/pexels-pixabay-80474.jpg
tags:
- name: Games
  slug: games
- name: React
  slug: react
- name: Redux
  slug: redux
- name: TypeScript
  slug: typescript
seo_title: Comment créer un jeu Snake avec React, Redux et Redux Saga
seo_desc: "In this article, I am going to walk you through creating a snake game using\
  \ a React application. It is a simple 2d game built using TypeScript, and we won't\
  \ need to use any third-party graphics libraries to build it. \nThis is what we'll\
  \ make in this ..."
---

Dans cet article, je vais vous guider à travers la création d'un jeu Snake en utilisant une application React. Il s'agit d'un simple jeu 2D construit avec TypeScript, et nous n'aurons pas besoin d'utiliser de bibliothèques graphiques tierces pour le construire.

Voici ce que nous allons créer dans ce tutoriel :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ezgif.com-gif-maker--2-.gif)

Snake est un jeu amusant que vous avez peut-être joué sur d'anciens téléphones comme les Nokia 3310.

Le concept derrière ce jeu est simple : le serpent se déplace à l'intérieur d'une boîte, et une fois qu'il capture le fruit/l'objet, vos points augmentent et le serpent grandit. Si le serpent heurte les limites de la boîte ou entre en collision avec lui-même, alors la partie est terminée.

Cet article vous fournira toutes les compétences/étapes nécessaires pour créer votre propre jeu Snake à partir de zéro. Nous examinerons d'abord les structures de code et leur logique. Ensuite, j'expliquerai comment elles fonctionnent lorsqu'elles sont toutes connectées.

Sans plus attendre, commençons.

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Qu'est-ce qu'un jeu Snake ? Que allons-nous utiliser ?](#heading-questcequunsnakegamequeallonsnousutiliser)
* [Qu'est-ce que Redux ? Pourquoi l'utilisons-nous ?](#heading-questcereduxpourquoilutilisonsnous)
* [Qu'est-ce que Redux-saga ? Pourquoi l'utilisons-nous ?](#heading-questcereduxsagapourquoilutilisonsnous)
* [Description du cas d'utilisation](#heading-descriptionducasdutilisation)
* [Configuration de l'application et de la couche de données](#heading-configurationdelapplicationetdelacouchededonnees)
* [Comprendre la couche UI](#heading-comprendrelacoucheui)
* [Tableau Canvas](#heading-tableaucanvas)
* [Dessin des objets](#heading-dessindesobjets)
* [Déplacement du serpent sur le tableau](#heading-deplacementduserpentsurletableau)
* [Dessin du fruit à une position aléatoire](#heading-dessindufruitapositionaleatoire)
* [Calculateur de score](#heading-calculateurdescore)
* [Composant d'instructions](#heading-composantdinstructions)
* [Jeu final](#heading-jeufinal)
* [Résumé](#heading-resume)

## Prérequis

Avant de commencer à lire cet article, vous devriez avoir une compréhension de base des sujets suivants :
- Diagrammes de classes : Nous allons les utiliser pour présenter notre exemple. Voici quelques ressources que vous pouvez utiliser pour en apprendre davantage à leur sujet :
    - [Diagrammes de classes](https://drawio-app.com/uml-class-diagrams-in-draw-io/)
    - [Cours sur les diagrammes UML](https://www.freecodecamp.org/news/uml-diagrams-full-course/)
- [Diagramme de contexte et diagrammes de conteneurs](https://www.notion.so/JS-Classes-a-boon-to-the-society-6360d1a702fe49da9b7ba98b0e03fe37)
- [React](https://reactjs.org/)
- Générateurs :
    - [Générateurs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
    - [Fonctions génératrices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)

## Qu'est-ce qu'un jeu Snake ? Que allons-nous utiliser ?

Un jeu Snake est un jeu d'arcade qui implique un serpent se déplaçant à l'intérieur d'une boîte. Votre score augmente en fonction du nombre d'objets/fruits que le serpent mange. Cela augmentera également la taille du serpent. Si le serpent entre en collision avec lui-même ou avec la limite de la boîte, alors la partie est terminée.

Vous pouvez en savoir plus sur l'histoire ou les origines du jeu dans le lien Wiki [ici](https://en.wikipedia.org/wiki/Snake_(video_game_genre)).

Nous allons utiliser les outils suivants pour construire notre jeu :

* Redux : Pour créer et gérer l'état global de l'application.
* Redux-saga : Un middleware Redux que nous utiliserons pour gérer les tâches asynchrones.
* Balise HTML Canvas : Nous l'utiliserons pour dessiner des objets comme un serpent et le fruit.
* React : Bibliothèque UI.
* Chakra-UI : Bibliothèque de composants.

## Qu'est-ce que Redux ? Pourquoi l'utilisons-nous ?

Redux est un conteneur d'état qui vous aide à créer et gérer l'état global de votre application. Redux se compose de quelques parties de base comme :

1. État global
2. Magasin Redux
3. Actions et créateurs d'actions
4. Réducteurs

Vous pouvez tout apprendre sur les sujets ci-dessus et sur le fonctionnement interne de Redux dans la section de démarrage de la documentation Redux [ici](https://redux.js.org/introduction/getting-started).

Nous utilisons la bibliothèque de gestion d'état Redux car elle nous aidera à gérer notre état global de manière plus simple. Elle nous permettra d'éviter le prop drilling. Elle nous permettra également d'effectuer des actions asynchrones complexes via des middlewares.

Vous pouvez en savoir plus sur les middlewares [ici](https://redux.js.org/understanding/history-and-design/middleware).

## Qu'est-ce que Redux-saga ? Pourquoi l'utilisons-nous ?

Redux-saga est un middleware qui nous aide à intercepter entre l'action dispatchée et le réducteur du magasin Redux. Cela nous permet d'effectuer certains effets secondaires entre l'action dispatchée et le réducteur, tels que la récupération de données, l'écoute d'actions particulières ou la mise en place d'abonnements, le déclenchement d'actions, et plus encore.

Redux saga utilise des générateurs et des fonctions génératrices. Une saga typique ressemblerait à ceci :

```javascript
function* performAction() {
    yield put({
        type: COPY_DATA,
        payload: "Hello"
    });
}
```

`performAction` est une fonction génératrice. Cette fonction génératrice exécutera la fonction `put`. Elle crée un objet et le retourne à la saga, indiquant quel type d'action doit être exécuté avec quelle charge utile. Ensuite, l'appel `put` retourne un descripteur d'objet indiquant quelle saga peut le prendre plus tard et exécuter l'action particulière.

**NOTE :** Vous pouvez en savoir plus sur les générateurs et les fonctions génératrices en vous référant à la section des prérequis.

Maintenant, la question se pose : *Pourquoi utilisons-nous le middleware redux-saga ?* La réponse est simple :

1. Il fournit un meilleur moyen d'écrire des cas de test unitaires, ce qui nous aidera à tester les fonctions génératrices de manière plus simple.
2. Il peut vous aider à effectuer beaucoup d'effets secondaires et à fournir un meilleur contrôle sur les changements. Un exemple est lorsque vous voulez surveiller si une action X particulière est exécutée, puis effectuer l'action Y. Des fonctions comme `takeEvery`, `all`, et ainsi de suite rendent simple l'exécution de ces opérations. Nous en discuterons davantage dans une section ultérieure.

Si vous n'êtes pas familier avec redux-saga, je vous recommande vivement de consulter la documentation [ici](https://redux-saga.js.org/docs/introduction/GettingStarted/).

## Description du cas d'utilisation

**NOTE :** Les diagrammes de contexte, de conteneur et de classe dessinés dans cet article de blog ne suivent pas exactement les conventions exactes de ces diagrammes. Je les ai approximés ici pour que vous puissiez comprendre les concepts de base.

Avant de commencer, je vous suggère de lire sur les modèles c4, les diagrammes de conteneur et les diagrammes de contexte. Vous pouvez trouver des ressources à leur sujet dans la section des prérequis.

Dans cet article, nous allons considérer le cas d'utilisation suivant : _Créer un jeu Snake_.

Le cas d'utilisation est assez explicite, et nous avons discuté de ce que le jeu Snake implique ci-dessus. Ci-dessous se trouve le diagramme de contexte pour notre cas d'utilisation :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/contextDiagram.png)
_Diagramme de contexte du jeu Snake_

Notre diagramme de contexte est assez simple. Le joueur interagit avec l'UI. Plongeons plus profondément dans le conteneur du tableau de jeu UI et explorons quels autres systèmes sont présents à l'intérieur.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Untitled--2-.png)
_Diagramme de conteneur pour le jeu Snake_

Comme vous pouvez le voir sur le diagramme ci-dessus, notre UI de tableau de jeu est divisée en deux couches :

1. Couche UI
2. Couche de données

La couche UI se compose des composants suivants :

1. **Calculateur de score** : Il s'agit d'un composant qui affichera le score chaque fois que le serpent mangera le fruit.
2. **Tableau Canvas** : Il s'agit d'un composant qui gère la partie principale de l'UI de notre jeu. Sa fonctionnalité de base est de dessiner le serpent sur le canevas et d'effacer le canevas. Il gère également les responsabilités suivantes :
    1. Il détecte si le serpent est entré en collision avec lui-même ou avec les murs de délimitation (détection de collision).
    2. Aide à déplacer le serpent sur le tableau avec les événements du clavier.
    3. Réinitialise le jeu lorsque la partie est terminée.
3. **Instructions** : Il fournit les instructions pour jouer au jeu, ainsi que le bouton de réinitialisation.
4. **Utilitaires** : Il s'agit des fonctions utilitaires que nous utiliserons dans toute l'application selon les besoins.

Parlons maintenant de la couche de données. Elle se compose des composants suivants :

1. **Redux-saga** : Ensemble de fonctions génératrices qui effectueront certaines actions.
2. **Actions et créateurs d'actions** : Il s'agit de l'ensemble de constantes et de fonctions qui aideront à dispatcher les actions appropriées.
3. **Réducteurs** : Cela nous aidera à répondre aux diverses actions dispatchées par les créateurs d'actions et les sagas.

Nous allons approfondir tous ces composants et voir comment ils fonctionnent collectivement dans les sections suivantes. Tout d'abord, initialisons notre projet et configurons notre couche de données, c'est-à-dire le magasin Redux.

## Configuration de l'application et de la couche de données

Avant de commencer à comprendre nos composants de jeu, configurons d'abord notre application React et la couche de données.

Le jeu est construit avec React. Je recommande vivement d'utiliser le modèle [create-react-app](https://create-react-app.dev/) pour installer toutes les choses nécessaires pour démarrer votre application React.

Pour créer un projet CRA (create-react-app), nous devons d'abord l'installer. Tapez la commande suivante dans votre terminal :

```shell
npm install -g create-react-app
```

**Note :** Avant d'exécuter cette commande, assurez-vous d'avoir installé Node.js dans votre système. Suivez ce [lien](https://nodejs.org/en/download/package-manager/) pour l'installer.

Ensuite, nous allons commencer par créer notre projet. Appelons-le snake-game. Tapez la commande suivante dans votre terminal pour créer le projet :

```shell
npx create-react-app snake-game
```

Cela peut prendre quelques minutes pour se terminer. Une fois cela terminé, accédez à votre nouveau projet créé en utilisant la commande suivante :

```shell
cd snake-game
```

Une fois dans le projet, tapez la commande suivante pour démarrer le projet :

```shell
npm run start
```

Cette commande ouvrira un nouvel onglet dans votre navigateur avec le logo React tournant sur la page comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-16.png)
_page initiale de create-react-app_

Maintenant, notre configuration initiale du projet est terminée. Configurons notre couche de données (le magasin Redux). Notre couche de données nécessite que nous installions les packages suivants :

* Redux
* Redux-saga

Tout d'abord, commençons par installer ces packages. Avant de commencer, assurez-vous d'être dans le répertoire du projet. Tapez la commande suivante dans le terminal :

```shell
npm install redux react-redux redux-saga
```

Une fois ces packages installés, nous allons d'abord configurer notre magasin Redux. Pour commencer, créons un dossier nommé `store` :

```shell
mkdir store
```

Ce dossier `store` contiendra tous les fichiers liés à Redux. Nous allons organiser notre dossier store de la manière suivante :

```shell
store/
├── actions
│   └── index.ts
├── reducers
│   └── index.ts
├── sagas
│   └── index.ts
└── index.ts
```

Discutons de ce que fait chacun des fichiers :

* `action/index.tsx` : Ce fichier contient des constantes qui représentent des actions que notre application peut effectuer et dispatcher vers le magasin Redux. Un exemple d'une telle constante d'action ressemble à ceci :

```javascript
export const MOVE_RIGHT = "MOVE_RIGHT"
```

Nous utiliserons la même constante d'action pour créer une fonction qui retournera un objet avec les propriétés suivantes :

* `type` : Type d'action, c'est-à-dire la constante d'action
* `payload` : données supplémentaires qui agissent comme une charge utile.

Ces fonctions qui retournent un objet avec la propriété `type` sont appelées créateurs d'actions. Nous utilisons ces fonctions pour dispatcher des actions à notre magasin Redux.

L'attribut `payload` signifie que, avec l'action, nous pouvons également passer des données supplémentaires qui peuvent être utilisées pour stocker ou mettre à jour la valeur à l'intérieur de l'état global.

**NOTE** : Il est obligatoire d'avoir la propriété `type` retournée par le créateur d'action. La propriété `payload` est facultative. De plus, le nom de la propriété `payload` peut être n'importe quoi.

Regardons un exemple de créateur d'action :

```javascript
//Sans payload
export const moveRight = () => ({
	type: MOVE_RIGHT
});

//Avec payload
export const moveRight = (data: string) => ({
	type: MOVE_RIGHT,
	payload: data
});
```

Maintenant que nous savons ce que sont les actions et les créateurs d'actions, nous pouvons passer à la configuration de notre prochain artefact qui est un réducteur.

Les réducteurs sont des fonctions qui retournent un nouvel état global chaque fois qu'une action est dispatchée. Ils prennent l'état global actuel et retournent le nouvel état en fonction de l'action qui est dispatchée/appelée. Cet nouvel état est calculé en fonction de l'état précédent.

Nous devons être prudents ici et ne pas effectuer d'effets secondaires à l'intérieur de cette fonction. Nous ne devons pas altérer l'état global, mais plutôt retourner l'état mis à jour en tant que nouvel objet lui-même. Par conséquent, la fonction réductrice doit être une fonction pure.

Assez parlé des réducteurs. Jetons un coup d'œil à nos réducteurs d'exemple :

```javascript
const GlobalState = {
    data: ""
};

const gameReducer = (state = GlobalState, action) => {
    switch (action.type) {
        case "MOVE_RIGHT":
            /**
             * Effectuer un certain ensemble d'opérations
             */
            return {
                ...state, data: action.payload
            };

        default:
            return state;
    }
}
```

Dans cet exemple, nous avons créé une fonction réductrice appelée `gameReducer`. Elle prend l'état (paramètre par défaut en tant qu'état global) et une action. Chaque fois que nous avons `action.type` qui correspond au cas de commutation, elle effectue une action particulière, comme retourner un nouvel état basé sur l'action.

Le fichier `sagas/index.ts` contiendra toutes les sagas que nous utiliserons dans notre application. Nous avons une compréhension de base des sagas que nous avons brièvement expliquée dans les sections ci-dessus. Nous approfondirons cette section lorsque nous commencerons réellement l'implémentation du jeu Snake.

Maintenant que nous avons une compréhension de base des artefacts impliqués dans la création de notre magasin Redux, créons `store/index.ts` comme suit :

```javascript
import {
    createStore,
    applyMiddleware
} from "redux";
import createSagaMiddleware from "redux-saga";
import gameReducer from "./reducers";
import watcherSagas from "./sagas";
const sagaMiddleware = createSagaMiddleware();

const store = createStore(gameReducer, applyMiddleware(sagaMiddleware));

sagaMiddleware.run(watcherSagas);
export default store;
```

Nous allons d'abord importer notre réducteur et la saga. Ensuite, nous allons utiliser la fonction `createSagaMiddleware()` pour créer un middleware saga.

Ensuite, nous allons le connecter à notre magasin en le passant comme argument à la fonction `applyMiddleware` à l'intérieur de `createStore` que vous utilisez pour créer un magasin. Nous allons également passer `gameReducer` à cette fonction afin qu'un réducteur soit mappé à notre magasin.

Enfin, nous allons exécuter notre sagaMiddleware en utilisant ce code :

```javascript
sagaMiddleware.run(watcherSagas);
```

Notre dernière étape consiste à injecter ce `store` au niveau supérieur de notre application React en utilisant le composant `Provider` fourni par `react-redux`. Vous pouvez le faire comme suit :

```jsx
import { Provider } from "react-redux";
import store from "./store";

const App = () => {
  return (
    <Provider store={store}>
    //   Composants enfants...
    </Provider>
  );
};

export default App;
```

J'ai également installé chakra-UI comme bibliothèque de composants UI pour notre projet. Pour installer chakra-UI, tapez la commande suivante :

```shell
npm install @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@^5
```

Nous devons également configurer le `ChakraProvider` qui ira dans notre fichier `App.tsx`. Notre fichier `App.tsx` mis à jour ressemblera à ceci :

```jsx
import { ChakraProvider, Container, Heading } from "@chakra-ui/react";
import { Provider } from "react-redux";
import store from "./store";

const App = () => {
  return (
    <Provider store={store}>
      <ChakraProvider>
        <Container maxW="container.lg" centerContent>
          <Heading as="h1" size="xl">SNAKE GAME</Heading>
	//Composants enfants
        </Container>
      </ChakraProvider>
    </Provider>
  );
};

export default App;
```

## Comprendre la couche UI

Commençons par comprendre la dynamique de notre jeu Snake du point de vue de l'UI. Avant de commencer, notre jeu Snake final ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/snake-game.png)

La couche UI se compose de 3 couches : **Calculateur de score**, **Tableau Canvas** et **Instructions**. Le diagramme ci-dessous montre ces sections :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Untitled--3-.png)

Plongeons plus profondément dans chacune de ces sections pour comprendre comment fonctionne notre jeu Snake.

## Tableau Canvas

Nous allons commencer par comprendre le tableau Canvas :

* Notre tableau Canvas aura des dimensions de `hauteur : 600, largeur : 1000`
* Ce tableau entier est divisé en blocs de taille `20x20`. C'est-à-dire que chaque objet dessiné sur ce tableau a une `hauteur de 20` et une `largeur de 20`.
* Nous utilisons l'élément HTML `<canvas>` pour dessiner les formes dans le composant du tableau Canvas.

Dans notre projet, nous écrivons le composant du tableau Canvas dans le fichier `components/CanvasBoard.tsx`. Maintenant que notre compréhension de base est claire concernant le composant CanvasBoard, commençons à construire ce composant.

Créez un composant simple qui retourne un élément canvas comme ci-dessous :

```jsx
export interface ICanvasBoard {
  height: number;
  width: number;
}

const CanvasBoard = ({ height, width }: ICanvasBoard) => {
  return (
    <canvas
      style={{
        border: "3px solid black",
      }}
      height={height}
      width={width}
    />
  );
};
```

Appelez ce composant dans notre fichier `App.tsx` avec une largeur et une hauteur de 1000 et 600 comme prop comme ci-dessous :

```jsx
import { ChakraProvider, Container, Heading } from "@chakra-ui/react";
import { Provider } from "react-redux";
import CanvasBoard from "./components/CanvasBoard";
import ScoreCard from "./components/ScoreCard";
import store from "./store";

const App = () => {
  return (
    <Provider store={store}>
      <ChakraProvider>
        <Container maxW="container.lg" centerContent>
          <Heading as="h1" size="xl">SNAKE GAME</Heading>
          <CanvasBoard height={600} width={1000} /> //Composant Canvasboard ajouté 
        </Container>
      </ChakraProvider>
    </Provider>
  );
};

export default App;
```

Cela créera une simple boîte de hauteur=600 et de largeur=1000 avec une bordure noire comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/snakeCanvas1.png)
_Un élément canvas vide avec une largeur=1000 et une hauteur=600_

Maintenant, dessinons un serpent au centre de ce canvas. Mais avant de pouvoir commencer à dessiner, nous devons obtenir le contexte de cet élément `canvas`.

Le contexte d'un élément canvas vous fournit toutes les informations dont vous avez besoin concernant l'élément canvas. Il vous donne les dimensions du canvas et vous aide également à dessiner sur le canvas.

Pour obtenir le contexte de notre élément canvas, nous devons appeler la fonction `getCanvas('2d')` qui retourne le contexte 2d du canvas. Le type de retour de cette fonction est l'interface `CanvasRenderingContext2D`.

Pour faire cela en JS pur, nous ferions quelque chose comme ci-dessous :

```javascript
const canvas = document.querySelector('canvas');
const canvasCtx = canvas.getContext('2d');
```

Mais pour le faire en React, nous devons créer une `ref` et la passer à l'élément canvas afin de pouvoir l'adresser plus tard dans différents hooks. Pour ce faire dans notre application, créez une `ref` en utilisant le hook `useRef` :

```jsx
const canvasRef = useRef<HTMLCanvasElement | null>(null);
```

Passez la ref dans notre élément `canvas` :

```jsx
<canvas
  ref={canvasRef}
  style={{
    border: "3px solid black",
  }}
  height={height}
  width={width}
/>;

```

Une fois que la `canvasRef` est passée dans l'élément `canvas`, nous pouvons l'utiliser à l'intérieur d'un hook `useEffect` et stocker le contexte dans une variable d'état.

```jsx
export interface ICanvasBoard {
  height: number;
  width: number;
}

const CanvasBoard = ({ height, width }: ICanvasBoard) => {
  const canvasRef = (useRef < HTMLCanvasElement) | (null > null);
  const [context, setContext] =
    (useState < CanvasRenderingContext2D) | (null > null);

  useEffect(() => {
    //Dessiner sur le canvas à chaque fois
    setContext(canvasRef.current && canvasRef.current.getContext("2d")); //stocker dans la variable d'état
  }, [context]);

  return (
    <canvas
      ref={canvasRef}	
      style={{
        border: "3px solid black",
      }}
      height={height}
      width={width}
    />
  );
};

```

## Dessin des objets

Après avoir obtenu le contexte, nous devons effectuer les tâches suivantes à chaque fois qu'un composant est mis à jour :

1. Effacer le canvas
2. Dessiner le serpent avec la position actuelle
3. Dessiner un fruit à une position aléatoire à l'intérieur de la boîte

Nous allons effacer le canvas plusieurs fois, nous allons donc en faire une fonction utilitaire. Pour cela, créons un dossier appelé `utilities` :

```shell
mkdir utilities
cd utilities
touch index.tsx
```

La commande ci-dessus créera également un fichier `index.tsx` à l'intérieur du dossier utilities. Ajoutez le code ci-dessous dans le fichier `utilities/index.tsx` :

```javascript
export const clearBoard = (context: CanvasRenderingContext2D | null) => {
  if (context) {
    context.clearRect(0, 0, 1000, 600);
  }
};
```

La fonction `clearBoard` est assez simple. Elle effectue les actions suivantes :

1. Elle accepte les objets de contexte de canvas 2d comme argument.
2. Elle vérifie que le contexte n'est pas null ou undefined.
3. La fonction `clearRect` effacera tous les pixels ou objets présents à l'intérieur du rectangle. Cette fonction prendra la largeur et la hauteur comme argument pour le rectangle à effacer.

Nous utiliserons cette fonction `clearBoard` à l'intérieur de notre `CanvasBoard` useEffect pour effacer le canvas chaque fois que le composant est mis à jour. Pour différencier les différents `useEffects`, nous nommerons l'useEffect ci-dessus useEffect1.

Maintenant, commençons par dessiner le serpent et le fruit à une position aléatoire. Puisque nous allons dessiner les objets plusieurs fois, nous créerons une fonction utilitaire appelée `drawObject`. Ajoutez le code ci-dessous dans le fichier `utilities/index.tsx` :

```javascript
export interface IObjectBody {
  x: number;
  y: number;
}

export const drawObject = (
  context: CanvasRenderingContext2D | null,
  objectBody: IObjectBody[],
  fillColor: string,
  strokeStyle = "#146356"
) => {
  if (context) {
    objectBody.forEach((object: IObjectBody) => {
      context.fillStyle = fillColor;
      context.strokeStyle = strokeStyle;
      context?.fillRect(object.x, object.y, 20, 20);
      context?.strokeRect(object.x, object.y, 20, 20);
    });
  }
};
```

La fonction `drawObject` accepte les arguments suivants :

1. `context` – Un objet de contexte de canvas 2D pour dessiner l'objet sur le canvas.
2. `objectBody` – Il s'agit d'un tableau d'objets, chaque objet ayant les propriétés `x` et `y`, comme l'interface `IObjectBody`.
3. `fillColor` – Couleur à remplir à l'intérieur de l'objet.
4. `strokeStyle` – Couleur à remplir dans le contour de l'objet. Par défaut, `#146356`.

Cette fonction vérifie si le contexte est undefined ou null. Ensuite, elle itère sur `objectBody` via forEach. Pour chaque objet, elle effectue les opérations suivantes :

1. Elle assignera `fillStyle` et `strokeStyle` à l'intérieur du contexte.
2. Elle utilisera `fillReact` pour créer un rectangle rempli avec les coordonnées `object.x` et `object.y` avec une taille de `20x20`
3. Enfin, elle utilisera `strokeRect` pour créer un rectangle contour avec les coordonnées `object.x` et `object.y` avec une taille de `20x20`

Pour dessiner le serpent, nous devons maintenir la position du serpent. Pour cela, nous pouvons utiliser notre outil de gestion d'état global `redux`.

Nous devons mettre à jour notre fichier `reducers/index.ts`. Puisque nous voulons suivre la position du serpent, nous l'ajouterons à notre état global comme suit :

```javascript
interface ISnakeCoord {
  x: number;
  y: number;
}

export interface IGlobalState {
  snake: ISnakeCoord[] | [];
}

const globalState: IGlobalState = {
  //Position du serpent entier
  snake: [
    { x: 580, y: 300 },
    { x: 560, y: 300 },
    { x: 540, y: 300 },
    { x: 520, y: 300 },
    { x: 500, y: 300 },
  ],
};
```

Appelons cet état dans notre composant `CanvasBoard`. Nous utiliserons le hook `useSelector` de react-redux pour obtenir l'état requis du magasin. Ce qui suit nous donnera l'état global du `snake` :

```javascript
const snake1 = useSelector((state: IGlobalState) => state.snake);
```

Intégrons cela dans notre composant `CanvasBoard` et passons-le à notre fonction `drawObject` pour voir le résultat :

```jsx
//Importation des modules nécessaires
import { useSelector } from "react-redux";
import { clearBoard, drawObject, generateRandomPosition } from "../utils";

export interface ICanvasBoard {
  height: number;
  width: number;
}

const CanvasBoard = ({ height, width }: ICanvasBoard) => {
	const canvasRef = useRef<HTMLCanvasElement | null>(null);
	const [context, setContext] = useState<CanvasRenderingContext2D | null>(null);
	const snake1 = useSelector((state: IGlobalState) => state.snake);
	const [pos, setPos] = useState<IObjectBody>(
	    generateRandomPosition(width - 20, height - 20)
	  );

	useEffect(() => {
	  //Dessiner sur le canvas à chaque fois
	 setContext(canvasRef.current && canvasRef.current.getContext("2d")); //stocker dans la variable d'état
		drawObject(context, snake1, "#91C483"); //Dessine le serpent à la position requise
		drawObject(context, [pos], "#676FA3"); //Dessine le fruit aléatoirement
	}, [context])

  return (
    <canvas
      style={{
        border: "3px solid black",
      }}
      height={height}
      width={width}
    />
  );
};
```

Voyons à quoi ressemblera le résultat lorsque le serpent est dessiné :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/snake_only.png)
_Dessin du serpent_

## Déplacement du serpent sur le tableau

Maintenant que nous avons notre serpent dessiné sur le canvas, apprenons à déplacer le serpent sur le tableau.

Le mouvement du serpent est simple. Il doit toujours suivre les points ci-dessous :

1. Si le serpent se déplace horizontalement, alors il ne peut se déplacer que vers le haut, le bas et dans la direction dans laquelle il se déplace actuellement. Par exemple, si le serpent se déplace vers la droite, alors il peut se déplacer vers le haut ou le bas ou continuer à se déplacer vers la droite.
2. Si le serpent se déplace verticalement, alors il ne peut se déplacer que vers la droite, la gauche ou continuer dans la direction dans laquelle il se déplace actuellement. Par exemple, si le serpent se déplace vers le haut, alors il peut se déplacer vers la droite ou la gauche (ou continuer vers le haut).
3. Le serpent ne peut pas se déplacer dans la direction opposée à celle de la direction actuelle. C'est-à-dire, si le serpent se déplace vers la gauche, alors il ne peut pas se déplacer vers la droite immédiatement. De même, s'il va vers le haut, il ne peut pas aller vers le bas.

Pour le mouvement fluide de notre serpent, le serpent doit toujours se déplacer de manière rectangulaire. Et il doit répondre aux points ci-dessus pour avoir ce mouvement.

Le diagramme ci-dessous aide à résumer comment le mouvement du serpent fonctionne dans toute l'application :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/temp.png)
_Explication du mouvement du serpent_

**NOTE :** Dans le diagramme ci-dessus, tout le mouvement du serpent commence avec le composant `CanvasBoard`.

**INDICE :** Ne vous inquiétez pas si vous ne pouvez pas suivre le diagramme ci-dessus. Lisez simplement les sections suivantes pour plus de clarté.

Pour maintenir le mouvement du serpent, nous allons introduire une autre variable d'état dans notre état global appelée `disallowedDirection`. Le but de cette variable est de suivre la direction opposée du mouvement du serpent.

Par exemple, si le serpent se déplace vers la gauche, alors `disallowedDirection` sera défini sur droite. Donc, pour résumer, nous suivons cette direction afin que nous puissions éviter que le serpent ne se déplace dans sa direction opposée.

Créons cette variable dans notre état global :

```javascript
interface ISnakeCoord {
  x: number;
  y: number;
}

export interface IGlobalState {
  snake: ISnakeCoord[] | [];
  disallowedDirection: string;
}

const globalState: IGlobalState = {
	//Position du serpent entier
  snake: [
    { x: 580, y: 300 },
    { x: 560, y: 300 },
    { x: 540, y: 300 },
    { x: 520, y: 300 },
    { x: 500, y: 300 },
  ],
	disallowedDirection: ""
};
```

Maintenant, créons quelques actions et créateurs d'actions qui nous aideront à déplacer le serpent.

Nous aurons deux types d'actions pour ce cas :

- Actions pour les sagas
    - Ce sont les actions qui seront dispatchées depuis le composant `CanvasBoard`. Ces actions seront :
        - MOVE_RIGHT
        - MOVE_LEFT
        - MOVE_UP
        - MOVE_DOWN
- Actions pour les réducteurs
    - Ce sont les actions qui seront yieldées par la saga pour propager les appels aux réducteurs. Ces actions seront :
        - RIGHT
        - LEFT
        - UP
        - DOWN

Nous examinerons de plus près ces actions dans les sections à venir.

Nous allons créer une autre action appelée `SET_DIS_DIRECTION` pour définir la variable d'état `disallowedDirection`.

Créons quelques créateurs d'actions pour le mouvement du serpent :

* `setDisDirection` – Ce créateur d'action sera utilisé pour définir `disallowedDirection` via l'action `SET_DIS_DIRECTION`. Voici le code pour ce créateur d'action :

```javascript
export const setDisDirection = (direction: string) => ({
  type: SET_DIS_DIRECTION,
  payload: direction
});
```

* `makeMove` – Cela sera utilisé pour définir/mettre à jour les nouvelles coordonnées du serpent en mettant à jour la variable d'état `snake`. Voici le code pour ce créateur d'action :

```javascript
export const makeMove = (dx: number, dy: number, move: string) => ({
  type: move,
  payload: [dx, dy]
});
```

Les paramètres `dx` et `dy` sont les deltas. Ils indiquent au magasin Redux de combien nous devons augmenter/diminuer les coordonnées de chaque bloc de serpent pour déplacer le serpent dans la direction donnée.

Le paramètre `move` est utilisé pour spécifier dans quelle direction le serpent se déplacera. Nous examinerons ces créateurs d'actions bientôt dans les sections à venir.

Enfin, notre fichier `actions/index.ts` mis à jour ressemblera à ceci :

```javascript
export const MOVE_RIGHT = "MOVE_RIGHT";
export const MOVE_LEFT = "MOVE_LEFT";
export const MOVE_UP = "MOVE_UP";
export const MOVE_DOWN = "MOVE_DOWN";

export const RIGHT = "RIGHT";
export const LEFT = "LEFT";
export const UP = "UP";
export const DOWN = "DOWN";

export const SET_DIS_DIRECTION = "SET_DIS_DIRECTION";

export interface ISnakeCoord {
  x: number;
  y: number;
}
export const makeMove = (dx: number, dy: number, move: string) => ({
  type: move,
  payload: [dx, dy]
});

export const setDisDirection = (direction: string) => ({
  type: SET_DIS_DIRECTION,
  payload: direction
});
```

Maintenant, jetons un coup d'œil à la logique que nous utilisons pour déplacer le serpent en fonction des actions ci-dessus. Tous les mouvements du serpent seront suivis par les actions suivantes :
- RIGHT
- LEFT
- UP
- DOWN

Toutes ces actions sont les éléments de base du mouvement du serpent. Ces actions, lorsqu'elles sont dispatchées, mettront toujours à jour l'état global du `snake` en fonction de la logique que nous décrivons ci-dessous. Et elles calculeront les nouvelles coordonnées du serpent à chaque mouvement.

Pour calculer les nouvelles coordonnées du serpent après chaque mouvement, nous utiliserons la logique suivante :

1. Copier les coordonnées dans une nouvelle variable appelée `newSnake`
2. Ajouter au début de `newSnake` les nouvelles coordonnées x et y. Ces attributs x et y de ces coordonnées sont mis à jour en ajoutant les valeurs x et y de la charge utile de l'action.
3. Enfin, supprimer la dernière entrée du tableau `newSnake`.

Maintenant que nous avons une certaine compréhension de la façon dont le serpent se déplace, ajoutons les cas suivants dans notre `gameReducer` :

```javascript
    case RIGHT:
    case LEFT:
    case UP:
    case DOWN: {
      let newSnake = [...state.snake];
      newSnake = [{
        //Nouvelles coordonnées x et y
        x: state.snake[0].x + action.payload[0],
        y: state.snake[0].y + action.payload[1],
      }, ...newSnake];
      newSnake.pop();

      return {
        ...state,
        snake: newSnake,
      };
    }
```

Pour chaque mouvement du serpent, nous mettons à jour les nouvelles coordonnées x et y qui sont augmentées par les charges utiles `action.payload[0]` et `action.payload[1]`. Nous avons réussi à configurer les actions, les créateurs d'actions et la logique du réducteur.

Nous sommes prêts à utiliser tout cela dans notre composant `CanvasBoard`.

Tout d'abord, ajoutons un hook useEffect dans notre composant `CanvasBoard`. Nous utiliserons ce hook pour attacher/ajouter un gestionnaire d'événements. Ce gestionnaire d'événements sera attaché à l'événement `keypress`. Nous utilisons cet événement car chaque fois que nous appuyons sur les touches `w` `a` `s` `d`, nous devons pouvoir contrôler le mouvement du serpent.

Notre useEffect ressemblera à ceci :

```javascript
useEffect(() => {
    window.addEventListener("keypress", handleKeyEvents);

    return () => {
      window.removeEventListener("keypress", handleKeyEvents);
    };
  }, [disallowedDirection, handleKeyEvents]); 
```

Il fonctionne de la manière suivante :

1. Au montage du composant, l'écouteur d'événement avec la fonction de rappel `handleKeyEvents` est attaché à l'objet window.
2. Au démontage du composant, l'écouteur d'événement est supprimé de l'objet window.
3. Si un changement se produit dans la direction ou la fonction `handleKeyEvents`, nous réexécuterons cet useEffect. Par conséquent, nous avons ajouté `disallowedDirection` et `handleKeyEvents` dans le tableau de dépendances.

Jetons un coup d'œil à la création de la fonction de rappel `handleKeyEvents`. Voici le code pour celle-ci :

```javascript
const handleKeyEvents = useCallback(
    (event: KeyboardEvent) => {
      if (disallowedDirection) {
        switch (event.key) {
          case "w":
            moveSnake(0, -20, disallowedDirection);
            break;
          case "s":
            moveSnake(0, 20, disallowedDirection);
            break;
          case "a":
            moveSnake(-20, 0, disallowedDirection);
            break;
          case "d":
            event.preventDefault();
            moveSnake(20, 0, disallowedDirection);
            break;
        }
      } else {
        if (
          disallowedDirection !== "LEFT" &&
          disallowedDirection !== "UP" &&
          disallowedDirection !== "DOWN" &&
          event.key === "d"
        )
          moveSnake(20, 0, disallowedDirection); //Déplacer vers la DROITE au début
      }
    },
    [disallowedDirection, moveSnake]
  );
```

Nous avons enveloppé cette fonction avec un hook `useCallback`. Cela est dû au fait que nous voulons la version mémorisée de cette fonction qui est appelée à chaque changement d'état (c'est-à-dire, au changement de `disallowedDirection` et `moveSnake`). Cette fonction est appelée à chaque touche pressée sur le clavier.

Cette fonction de rappel de gestionnaire d'événements sert les objectifs suivants :

* Si `disallowedDirection` est vide, alors nous nous assurons que le jeu ne commencera que lorsque l'utilisateur appuiera sur la touche `d`. Cela signifie que le jeu commence uniquement lorsque le serpent se déplace vers la droite.

**NOTE** : Initialement, la valeur de la variable d'état global `disallowedDirection` est une chaîne vide. De cette manière, nous savons que si sa valeur est vide, alors c'est le début du jeu.

Une fois le jeu commencé, `disallowedDirection` ne sera pas vide et écoutera toutes les pressions de touches du clavier telles que `w` `s` et `a`.

Enfin, à chaque pression de touche, nous appelons la fonction appelée `moveSnake`. Nous allons l'examiner de plus près dans la section suivante.

La fonction `moveSnake` est une fonction qui dispatch une action passée au créateur d'action `makeMove`. Cette fonction accepte trois arguments :

1. **dx** - **Delta pour l'axe x**. Cela indique de combien le serpent doit se déplacer le long de l'axe x. Si `dx` est positif, alors il se déplace vers la droite, s'il est négatif, il se déplace vers la gauche.
2. **dy - Delta pour l'axe y**. Cela indique de combien le serpent doit se déplacer le long de l'axe y. Si `dy` est positif, alors il se déplace vers le bas, s'il est négatif, il se déplace vers le haut.
3. **disallowedDirection -** Cette valeur indique que le serpent ne doit pas se déplacer dans la direction opposée. Il s'agit d'une action qui est capturée par notre middleware saga.

Le code de la fonction `moveSnake` ressemblera à ceci :

```javascript
const moveSnake = useCallback(
    (dx = 0, dy = 0, ds: string) => {
      if (dx > 0 && dy === 0 && ds !== "RIGHT") {
        dispatch(makeMove(dx, dy, MOVE_RIGHT));
      }

      if (dx < 0 && dy === 0 && ds !== "LEFT") {
        dispatch(makeMove(dx, dy, MOVE_LEFT));
      }

      if (dx === 0 && dy < 0 && ds !== "UP") {
        dispatch(makeMove(dx, dy, MOVE_UP));
      }

      if (dx === 0 && dy > 0 && ds !== "DOWN") {
        dispatch(makeMove(dx, dy, MOVE_DOWN));
      }
    },
    [dispatch]
  );
```

La fonction `moveSnake` est une fonction simple qui vérifie les conditions :

1. Si dx > 0, et que `disallowedDirection` n'est pas `RIGHT`, alors il peut se déplacer dans la direction DROITE.
2. Si dx < 0, et que `disallowedDirection` n'est pas `LEFT`, alors il peut se déplacer dans la direction GAUCHE.
3. Si dy > 0, et que `disallowedDirection` n'est pas `DOWN`, alors il peut se déplacer dans la direction BAS.
4. Si dy < 0, et que `disallowedDirection` n'est pas `UP`, alors il peut se déplacer dans la direction HAUT.

Cette valeur `disallowedDirection` est définie dans nos sagas dont nous parlerons plus en détail dans les sections ultérieures de cet article. Si nous revisitons la fonction `handleKeyEvents`, elle a maintenant beaucoup plus de sens. Passons en revue un exemple ici :

* Supposons que vous souhaitez déplacer le serpent vers la DROITE. Alors cette fonction détectera que la touche `d` est pressée.
* Une fois cette touche pressée, elle appelle la fonction `makeMove` (condition de début du jeu) avec `dx` à 20 (+ve), `dy` à 0, et la `disallowedDirection` précédemment définie est appelée ici.

De cette manière, nous faisons déplacer le serpent dans une direction particulière. Maintenant, jetons un coup d'œil aux `sagas` que nous avons utilisées, et comment elles gèrent le mouvement du serpent.

Créons un fichier appelé `saga/index.ts`. Ce fichier contiendra toutes nos sagas. Ce n'est pas une règle, mais en général, nous créons deux sagas.

La première est la saga qui dispatch les actions réelles au magasin, appelons cela la _saga worker_. La seconde est la saga watcher qui surveille toute action qui est dispatchée, appelons cela la _saga watcher_.

Maintenant, nous devons créer une saga watcher qui surveillera les actions suivantes : `MOVE_RIGHT`, `MOVE_LEFT`, `MOVE_UP`, `MOVE_DOWN`.

```javascript
function* watcherSaga() {
	yield takeLatest(
      [MOVE_RIGHT, MOVE_LEFT, MOVE_UP, MOVE_DOWN],
      moveSaga
    ); 
}
```

Cette saga watcher surveillera les actions ci-dessus et exécutera la fonction `moveSaga` qui est une saga worker.

Vous remarquerez que nous avons utilisé une nouvelle fonction nommée `takeLatest`. Cette fonction appellera la saga worker et annulera tout appel de saga précédent si l'une des actions mentionnées dans le premier argument est dispatchée.

D'après les mots de la documentation [redux-saga](https://redux-saga.js.org/docs/api/#takelatestpattern-saga-args) :

> `takeLatest(pattern, saga, ...args)`[](https://redux-saga.js.org/docs/api/#takelatestpattern-saga-args)
> 
> 
> Forks a
0`saga`
0on each action dispatched to the Store that matches
0`pattern`. And automatically cancels any previous
0`saga`
0task started previously if it's still running.
> 
> - Each time an action is dispatched to the store. And if this action matches
0`pattern`,
0`takeLatest`
0starts a new
0`saga`
0task in the background. If a
0`saga`
0task was started previously (on the last action dispatched before the actual action), and if this task is still running, the task will be cancelled.
> - `pattern: String | Array | Function`
0- for more information see docs for
0`[take(pattern)](https://redux-saga.js.org/docs/api/#takepattern)`
> - `saga: Function`
0- a Generator function
> - `args: Array<any>`
0- arguments to be passed to the started task.
0`takeLatest`
0will add the incoming action to the argument list (i.e. the action will be the last argument provided to
0`saga`)

Maintenant, créons une saga worker appelée `moveSaga` qui dispatchera réellement les actions au magasin Redux :

```javascript
export function* moveSaga(params: {
    type: string;
    payload: ISnakeCoord;
  }): Generator<
    | PutEffect<{ type: string; payload: ISnakeCoord }>
    | PutEffect<{ type: string; payload: string }>
    | CallEffect<true>
  > {
    while (true) {
	//dispatches movement actions
	 yield put({
           type: params.type.split("_")[1],
           payload: params.payload,
	  }); 

      //Dispatches SET_DIS_DIRECTION action
      switch (params.type.split("_")[1]) {
        case RIGHT:
          yield put(setDisDirection(LEFT));
          break;

        case LEFT:
          yield put(setDisDirection(RIGHT));
          break;

        case UP:
          yield put(setDisDirection(DOWN));
          break;

        case DOWN:
          yield put(setDisDirection(UP));
          break;
      }
      yield delay(100);
    }
  }
```

La saga worker `moveSaga` effectue les fonctions suivantes :

1. Elle s'exécute dans une boucle infinie.
2. Donc, une fois qu'une direction est donnée, c'est-à-dire si la touche `d` est pressée et que l'action `MOVE_RIGHT` est dispatchée, alors elle commence à dispatcher la même action jusqu'à ce qu'une nouvelle action (c'est-à-dire une direction) soit donnée. Cela est géré par l'extrait de code suivant :

```javascript
yield put({
    type: params.type.split("_")[1],
    payload: params.payload,
});
```

3. Une fois l'action ci-dessus dispatchée, nous définissons la direction interdite sur la direction opposée, ce qui est pris en charge par le créateur d'action `setDisDirection`.

Maintenant, intégrons ces sagas dans notre fichier `sagas/index.ts` :

```javascript
import {
    CallEffect,
    delay,
    put,
    PutEffect,
    takeLatest
} from "redux-saga/effects";
import {
    DOWN,
    ISnakeCoord,
    LEFT,
    MOVE_DOWN,
    MOVE_LEFT,
    MOVE_RIGHT,
    MOVE_UP, RIGHT,
    setDisDirection, UP
} from "../actions";
  
  export function* moveSaga(params: {
    type: string;
    payload: ISnakeCoord;
  }): Generator<
    | PutEffect<{ type: string; payload: ISnakeCoord }>
    | PutEffect<{ type: string; payload: string }>
    | CallEffect<true>
  > {
    while (true) {
      yield put({
        type: params.type.split("_")[1],
        payload: params.payload,
      });
      switch (params.type.split("_")[1]) {
        case RIGHT:
          yield put(setDisDirection(LEFT));
          break;
  
        case LEFT:
          yield put(setDisDirection(RIGHT));
          break;
  
        case UP:
          yield put(setDisDirection(DOWN));
          break;
  
        case DOWN:
          yield put(setDisDirection(UP));
          break;
      }
      yield delay(100);
    }
  }
  
  function* watcherSagas() {
    yield takeLatest(
      [MOVE_RIGHT, MOVE_LEFT, MOVE_UP, MOVE_DOWN],
      moveSaga
    );
  }
  
  export default watcherSagas;
```

Maintenant, mettons à jour notre composant `CanvasBoard` pour incorporer ces changements.

```jsx
//Importation des modules nécessaires
import { useSelector } from "react-redux";
import { drawObject, generateRandomPosition } from "../utils";

export interface ICanvasBoard {
    height: number;
    width: number;
}

const CanvasBoard = ({ height, width }: ICanvasBoard) => {
    const canvasRef = useRef < HTMLCanvasElement | null > (null);
    const [context, setContext] = useState < CanvasRenderingContext2D | null > (null);
    const snake1 = useSelector((state: IGlobalState) => state.snake);
    const [pos, setPos] = useState < IObjectBody > (
        generateRandomPosition(width - 20, height - 20)
    );

    const moveSnake = useCallback(
        (dx = 0, dy = 0, ds: string) => {
            if (dx > 0 && dy === 0 && ds !== "RIGHT") {
                dispatch(makeMove(dx, dy, MOVE_RIGHT));
            }

            if (dx < 0 && dy === 0 && ds !== "LEFT") {
                dispatch(makeMove(dx, dy, MOVE_LEFT));
            }

            if (dx === 0 && dy < 0 && ds !== "UP") {
                dispatch(makeMove(dx, dy, MOVE_UP));
            }

            if (dx === 0 && dy > 0 && ds !== "DOWN") {
                dispatch(makeMove(dx, dy, MOVE_DOWN));
            }
        },
        [dispatch]
    );

    const handleKeyEvents = useCallback(
        (event: KeyboardEvent) => {
            if (disallowedDirection) {
                switch (event.key) {
                    case "w":
                        moveSnake(0, -20, disallowedDirection);
                        break;
                    case "s":
                        moveSnake(0, 20, disallowedDirection);
                        break;
                    case "a":
                        moveSnake(-20, 0, disallowedDirection);
                        break;
                    case "d":
                        event.preventDefault();
                        moveSnake(20, 0, disallowedDirection);
                        break;
                }
            } else {
                if (
                    disallowedDirection !== "LEFT" &&
                    disallowedDirection !== "UP" &&
                    disallowedDirection !== "DOWN" &&
                    event.key === "d"
                )
                    moveSnake(20, 0, disallowedDirection); //Déplacer vers la DROITE au début
            }
        },
        [disallowedDirection, moveSnake]
    );
    useEffect(() => {
        //Dessiner sur le canvas à chaque fois
        setContext(canvasRef.current && canvasRef.current.getContext("2d")); //stocker dans la variable d'état
					clearBoard(context);
        drawObject(context, snake1, "#91C483"); //Dessine le serpent à la position requise
    }, [context]);

    useEffect(() => {
        window.addEventListener("keypress", handleKeyEvents);

        return () => {
            window.removeEventListener("keypress", handleKeyEvents);
        };
    }, [disallowedDirection, handleKeyEvents]);

    return (
        <canvas
            style={{
                border: "3px solid black",
            }}
            height={height}
            width={width}
        />
    );
};
```

Une fois que vous avez apporté ces modifications, vous pouvez essayer de déplacer le serpent. Et voilà ! Vous verrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ezgif.com-gif-maker--3-.gif)
_Déplacement du serpent sur le tableau_

## Dessin du fruit à une position aléatoire

Pour dessiner un fruit à une position aléatoire sur le tableau, nous utiliserons la fonction utilitaire `generateRandomPosition`. Jetons un coup d'œil à cette fonction :

```javascript
function randomNumber(min: number, max: number) {
  let random = Math.random() * max;
  return random - (random % 20);
}
export const generateRandomPosition = (width: number, height: number) => {
  return {
    x: randomNumber(0, width),
    y: randomNumber(0, height),
  };
};
```

Il s'agit d'une fonction qui générera des coordonnées x et y aléatoires en multiples de 20. Ces coordonnées seront toujours inférieures à la largeur et à la hauteur du tableau. Elle accepte `width` et `height` comme arguments.

Une fois que nous avons cette fonction, nous pouvons l'utiliser pour dessiner le fruit à une position aléatoire à l'intérieur du tableau.

Tout d'abord, créons une variable d'état `pos` qui contiendra initialement une position aléatoire.

```javascript
const [pos, setPos] = useState<IObjectBody>(generateRandomPosition(width - 20, height - 20));
```

Ensuite, nous dessinerons le fruit via notre fonction `drawObject`. Après cela, nous mettrons légèrement à jour notre hook `useEffect` :

```javascript
 useEffect(() => {
        //Dessiner sur le canvas à chaque fois
        setContext(canvasRef.current &&   canvasRef.current.getContext("2d")); //stocker dans la variable d'état
        
        clearBoard(context);
        
        drawObject(context, snake1, "#91C483"); //Dessine le serpent à la position requise
        
        drawObject(context, [pos], "#676FA3"); //Dessine l'objet aléatoirement
    }, [context]);
```

Une fois que nous avons apporté les modifications, notre tableau ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/snake_fruit.png)
_Serpent et fruit dessinés sur le tableau_

## Calculateur de score

Le score du jeu est calculé en fonction du nombre de fruits que le serpent a consommés sans entrer en collision avec lui-même ou avec la limite de la boîte. Si le serpent consomme le fruit, alors la taille du serpent augmente. S'il entre en collision avec le bord de la boîte, alors la partie est terminée.

Maintenant que nous savons quels sont nos critères pour calculer le score, voyons comment nous calculons la récompense.

### Calcul de la récompense

La récompense après que le serpent a consommé le fruit est la suivante :

1. Augmenter la taille du serpent.
2. Augmenter le score.
3. Placer le nouveau fruit à un autre emplacement aléatoire.

Si le serpent consomme le fruit, alors nous devons augmenter la taille du serpent. Il s'agit d'une tâche très simple, nous pouvons simplement ajouter les nouvelles coordonnées x et y qui sont inférieures de 20 au dernier élément du tableau d'état global `snake`. Par exemple, si le serpent a les coordonnées suivantes :

```javascript
{
snake: [
    { x: 580, y: 300 },
    { x: 560, y: 300 },
    { x: 540, y: 300 },
    { x: 520, y: 300 },
    { x: 500, y: 300 },
  ],
}
```

Nous devons simplement ajouter l'objet suivant au tableau snake : `{ x: 480, y: 280 }`

De cette manière, nous augmentons la taille du serpent ainsi que nous ajoutons la nouvelle partie/bloc à la fin de celui-ci. Pour que cela soit implémenté via Redux et redux-saga, nous aurons besoin de l'action et du créateur d'action suivants :

```javascript
export const INCREMENT_SCORE = "INCREMENT_SCORE"; //action

export const increaseSnake = () => ({  //créateur d'action
    type: INCREASE_SNAKE
  });
```

Nous mettrons également à jour notre `gameReducer` pour accommoder ces changements. Nous ajouterons le cas suivant :

```javascript
case INCREASE_SNAKE:
      const snakeLen = state.snake.length;
      return {
        ...state,
        snake: [
          ...state.snake,
          {
            x: state.snake[snakeLen - 1].x - 20,
            y: state.snake[snakeLen - 1].y - 20,
          },
        ],
      };
```

Dans notre composant `CanvasBoard`, nous introduirons d'abord une variable d'état appelée `isConsumed`. Cette variable vérifiera si le fruit est consommé ou non.

```javascript
const [isConsumed, setIsConsumed] = useState<boolean>(false);
```

Dans notre hook `useEffect` où nous dessinons notre `snake` et le `fruit` juste en dessous, nous ajouterons la condition suivante :

```javascript
//Lorsque l'objet est consommé
    if (snake1[0].x === pos?.x && snake1[0].y === pos?.y) {
      setIsConsumed(true);
    }
```

La condition ci-dessus vérifiera si la tête du serpent `snake[0]` est égale à `pos`, ou la position du fruit. Si c'est vrai, alors elle définira la variable d'état `isConsumed` à vrai.

Une fois le fruit consommé, nous devons augmenter la taille du serpent. Nous pouvons le faire facilement via un autre `useEffect`. Créons un autre `useEffect` et appelons le créateur d'action `increaseSnake` :

```javascript
//useEffect2
useEffect(() => {
    if (isConsumed) {
      //Augmenter la taille du serpent lorsque l'objet est consommé avec succès
      dispatch(increaseSnake());
    }
  }, [isConsumed]);
```

Maintenant que nous avons augmenté la taille du serpent, voyons comment nous pouvons mettre à jour le score et générer un nouveau fruit à une autre position aléatoire.

Pour générer un nouveau fruit à une autre position aléatoire, nous mettons à jour la variable d'état `pos` qui réexécutera l'useEffect1 et dessinera l'objet à `pos`. Nous devons mettre à jour notre useEffect1 avec une nouvelle dépendance de `pos` et mettre à jour useEffect2 comme suit :

```javascript
useEffect(() => {
    //Générer un nouvel objet
    if (isConsumed) {
      const posi = generateRandomPosition(width - 20, height - 20);
      setPos(posi);
      setIsConsumed(false);

      //Augmenter la taille du serpent lorsque l'objet est consommé avec succès
      dispatch(increaseSnake());
    }
  }, [isConsumed, pos, height, width, dispatch]);
```

Une dernière chose à faire dans ce système de récompense est de mettre à jour le score chaque fois que le serpent mange le fruit. Pour ce faire, suivez les étapes ci-dessous :

1. Introduisez une nouvelle variable d'état global appelée `score`. Mettons à jour notre état global comme suit dans le fichier `reducers/index.ts` :

```javascript
export interface IGlobalState {
  snake: ISnakeCoord[] | [];
  disallowedDirection: string;
  score: number;
}

const globalState: IGlobalState = {
  snake: [
    { x: 580, y: 300 },
    { x: 560, y: 300 },
    { x: 540, y: 300 },
    { x: 520, y: 300 },
    { x: 500, y: 300 },
  ],
  disallowedDirection: "",
  score: 0,
};
```

2. Créez l'action et le créateur d'action suivants dans notre fichier `actions/index.ts` :

```javascript
export const INCREMENT_SCORE = "INCREMENT_SCORE"; //action

//créateur d'action :
export const scoreUpdates = (type: string) => ({
  type
});
```

3. Ensuite, mettons à jour notre réducteur pour gérer l'action `INCREMENT_SCORE`. Cela incrémentera simplement le score de l'état global de un.

```javascript
case INCREMENT_SCORE:
      return {
        ...state,
        score: state.score + 1,
      };
```

4. Ensuite, nous mettons à jour notre état de score, en dispatchant l'action `INCREMENT_SCORE` chaque fois que le serpent attrape le fruit. Pour cela, nous pouvons mettre à jour notre useEffect2 comme suit :

```javascript
useEffect(() => {
    //Générer un nouvel objet
    if (isConsumed) {
      const posi = generateRandomPosition(width - 20, height - 20);
      setPos(posi);
      setIsConsumed(false);

      //Augmenter la taille du serpent lorsque l'objet est consommé avec succès
      dispatch(increaseSnake());

      //Incrémenter le score
      dispatch(scoreUpdates(INCREMENT_SCORE));
    }
  }, [isConsumed, pos, height, width, dispatch]);
```

5. Enfin, nous créons un composant appelé `ScoreCard`. Cela affichera le score actuel du joueur. Nous le stockerons dans le fichier `components/ScoreCard.tsx`.

```jsx
import { Heading } from "@chakra-ui/react";
import { useSelector } from "react-redux";
import { IGlobalState } from "../store/reducers";

const ScoreCard = () => {
    const score = useSelector((state: IGlobalState) => state.score);
    return (
        <Heading as="h2" size="md" mt={5} mb={5}>Score actuel : {score}</Heading>
    );
}

export default ScoreCard;
```

Après cela, nous devons également ajouter le composant `ScoreCard` dans le fichier `App.tsx` pour l'afficher sur notre page.

```jsx
import { ChakraProvider, Container, Heading } from "@chakra-ui/react";
import { Provider } from "react-redux";
import CanvasBoard from "./components/CanvasBoard";
import ScoreCard from "./components/ScoreCard";
import store from "./store";

const App = () => {
  return (
    <Provider store={store}>
      <ChakraProvider>
        <Container maxW="container.lg" centerContent>
          <Heading as="h1" size="xl">SNAKE GAME</Heading>
          <ScoreCard />
          <CanvasBoard height={600} width={1000} />
        </Container>
      </ChakraProvider>
    </Provider>
  );
};

export default App;
```

Une fois que tout est en place, notre serpent aura un système de récompense complet qui augmente la taille du serpent pour mettre à jour le score.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ezgif.com-gif-maker--4-.gif)
_Joueur jouant au serpent avec le score et la longueur du serpent mis à jour._

### Détection de collision

Dans cette section, nous allons voir comment implémenter la détection de collision pour notre jeu Snake.

Dans notre jeu Snake, si une collision est détectée, alors la partie est terminée, c'est-à-dire que le jeu s'arrête. Il y a deux conditions pour que les collisions se produisent :

1. Le serpent entre en collision avec les limites de la boîte, ou
2. Le serpent entre en collision avec lui-même.

Jetons un coup d'œil à la première condition. Supposons que la tête du serpent touche les limites de la boîte. Dans ce cas, nous arrêterons immédiatement le jeu.

Pour que cela soit incorporé dans notre jeu, nous devons faire ce qui suit :

1. Créer une action et un créateur d'action comme ci-dessous :

```javascript
export const STOP_GAME = "STOP_GAME"; //action

//créateur d'action
export const stopGame = () => ({
  type: STOP_GAME
});
```

2. Nous devons également mettre à jour notre fichier `sagas/index.ts`. Nous allons nous assurer que la saga arrête de dispatcher des actions une fois que l'action `STOP_GAME` est rencontrée.

```javascript
export function* moveSaga(params: {
  type: string;
  payload: ISnakeCoord;
}): Generator<
  | PutEffect<{ type: string; payload: ISnakeCoord }>
  | PutEffect<{ type: string; payload: string }>
  | CallEffect<true>
> {
  while (params.type !== STOP_GAME) {
    yield put({
      type: params.type.split("_")[1],
      payload: params.payload,
    });
    switch (params.type.split("_")[1]) {
      case RIGHT:
        yield put(setDisDirection(LEFT));
        break;

      case LEFT:
        yield put(setDisDirection(RIGHT));
        break;

      case UP:
        yield put(setDisDirection(DOWN));
        break;

      case DOWN:
        yield put(setDisDirection(UP));
        break;
    }
    yield delay(100);
  }
}

function* watcherSagas() {
  yield takeLatest(
    [MOVE_RIGHT, MOVE_LEFT, MOVE_UP, MOVE_DOWN, STOP_GAME],
    moveSaga
  );
}
```

3. Enfin, nous devons mettre à jour notre useEffect1 en ajoutant la condition suivante :

```jsx
if ( //Vérifie si la tête du serpent est hors des limites de la boîte
      snake1[0].x >= width ||
      snake1[0].x <= 0 ||
      snake1[0].y <= 0 ||
      snake1[0].y >= height
    ) {
      setGameEnded(true);
      dispatch(stopGame());
      window.removeEventListener("keypress", handleKeyEvents);
    }
```

Nous supprimons également l'écouteur d'événement `handleKeyEvents`. Cela garantira que, une fois la partie terminée, le joueur ne pourra plus déplacer le serpent.

Enfin, voyons comment nous pouvons détecter l'auto-collision du serpent. Nous allons utiliser une fonction utilitaire appelée `hasSnakeCollided`. Elle accepte deux paramètres : le premier est le tableau du serpent, et le second est la tête du serpent. Si la tête du serpent touche une partie de lui-même, alors elle retourne vrai, sinon elle retourne faux.

La fonction `hasSnakeCollided` ressemblera à ceci :

```javascript
export const hasSnakeCollided = (
  snake: IObjectBody[],
  currentHeadPos: IObjectBody
) => {
  let flag = false;
  snake.forEach((pos: IObjectBody, index: number) => {
    if (
      pos.x === currentHeadPos.x &&
      pos.y === currentHeadPos.y &&
      index !== 0
    ) {
      flag = true;
    }
  });

  return flag;
};
```

Nous devons légèrement mettre à jour notre useEffect1 en mettant à jour la condition de détection de collision comme ceci :

```javascript
if (  
      //Vérifie si le serpent est entré en collision avec lui-même 
      hasSnakeCollided(snake1, snake1[0]) ||
      
      //Vérifie si la tête du serpent est hors des limites de la boîte
      snake1[0].x >= width ||
      snake1[0].x <= 0 ||
      snake1[0].y <= 0 ||
      snake1[0].y >= height
    ) {
      setGameEnded(true);
      dispatch(stopGame());
      window.removeEventListener("keypress", handleKeyEvents);
    }
```

Notre useEffect1 ressemblera finalement à ceci :

```javascript
//useEffect1
useEffect(() => {
    //Dessiner sur le canvas à chaque fois
    setContext(canvasRef.current && canvasRef.current.getContext("2d"));
    clearBoard(context);
    drawObject(context, snake1, "#91C483");
    drawObject(context, [pos], "#676FA3"); //Dessine l'objet aléatoirement

    //Lorsque l'objet est consommé
    if (snake1[0].x === pos?.x && snake1[0].y === pos?.y) {
      setIsConsumed(true);
    }

    if (
      hasSnakeCollided(snake1, snake1[0]) ||
      snake1[0].x >= width ||
      snake1[0].x <= 0 ||
      snake1[0].y <= 0 ||
      snake1[0].y >= height
    ) {
      setGameEnded(true);
      dispatch(stopGame());
      window.removeEventListener("keypress", handleKeyEvents);
    } else setGameEnded(false);
  }, [context, pos, snake1, height, width, dispatch, handleKeyEvents]);
```

Notre jeu ressemblera à ceci une fois que nous aurons ajouté le système de détection de collision :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ezgif.com-gif-maker--5-.gif)
_Détection de collision_

## Composant d'instructions

Nous sommes dans la phase finale du jeu ! Notre dernier composant sera le composant `Instruction`. Il contiendra des instructions sur le jeu comme la condition initiale du jeu, les touches à utiliser et un bouton de réinitialisation.

Commençons par créer un fichier appelé `components/Instructions.tsx`. Placez le code ci-dessous dans ce fichier :

```jsx
import { Box, Button, Flex, Heading, Kbd } from "@chakra-ui/react";

export interface IInstructionProps {
  resetBoard: () => void;
}
const Instruction = ({ resetBoard }: IInstructionProps) => (
  <Box mt={3}>
    <Heading as="h6" size="lg">
      Comment jouer
    </Heading>
    <Heading as="h5" size="sm" mt={1}>
    NOTE: Démarrez le jeu en appuyant sur <Kbd>d</Kbd>
    </Heading>
    <Flex flexDirection="row" mt={3}>
      <Flex flexDirection={"column"}>
        <span>
          <Kbd>w</Kbd> Monter
        </span>
        <span>
          <Kbd>a</Kbd> Aller à gauche
        </span>
        <span>
          <Kbd>s</Kbd> Descendre
        </span>
        <span>
          <Kbd>d</Kbd> Aller à droite
        </span>
      </Flex>
      <Flex flexDirection="column">
        <Button onClick={() => resetBoard()}>Réinitialiser le jeu</Button>
      </Flex>
    </Flex>
  </Box>
);

export default Instruction; 
```

Le composant `Instruction` acceptera `resetBoard` comme prop, qui est une fonction qui aidera l'utilisateur lorsque le jeu est terminé ou lorsqu'il souhaite réinitialiser le jeu.

Avant de plonger dans la fonction `resetBoard`, nous devons apporter les mises à jour suivantes dans notre magasin Redux et saga :

1. Ajoutez l'action et le créateur d'action suivants dans le fichier `actions/index.ts` :

```javascript
export const RESET_SCORE = "RESET_SCORE"; //action
export const RESET = "RESET"; //action

//Créateur d'action :
export const resetGame = () => ({
  type: RESET
});
```

2. Ensuite, ajoutez la condition suivante dans notre `sagas/index.ts`. Nous allons nous assurer que la saga cesse de dispatcher des actions une fois que les actions `RESET` et `STOP_GAME` sont rencontrées.

```javascript
export function* moveSaga(params: {
  type: string;
  payload: ISnakeCoord;
}): Generator<
  | PutEffect<{ type: string; payload: ISnakeCoord }>
  | PutEffect<{ type: string; payload: string }>
  | CallEffect<true>
> {
  while (params.type !== RESET && params.type !== STOP_GAME) {
    yield put({
      type: params.type.split("_")[1],
      payload: params.payload,
    });
    switch (params.type.split("_")[1]) {
      case RIGHT:
        yield put(setDisDirection(LEFT));
        break;

      case LEFT:
        yield put(setDisDirection(RIGHT));
        break;

      case UP:
        yield put(setDisDirection(DOWN));
        break;

      case DOWN:
        yield put(setDisDirection(UP));
        break;
    }
    yield delay(100);
  }
}

function* watcherSagas() {
  yield takeLatest(
    [MOVE_RIGHT, MOVE_LEFT, MOVE_UP, MOVE_DOWN, RESET, STOP_GAME],
    moveSaga
  );
}
```

3. Enfin, nous mettons à jour notre fichier `reducers/index.ts` pour le cas `RESET_SCORE` comme suit :

```javascript
case RESET_SCORE:
      return { ...state, score: 0 };
```

Une fois nos sagas et réducteurs mis à jour, nous pouvons examiner quelles opérations la fonction de rappel `resetBoard` effectuera.

La fonction `resetBoard` effectue les opérations suivantes :

1. Supprime l'écouteur d'événement `handleKeyEvents`
2. Dispatch les actions nécessaires pour réinitialiser le jeu.
3. Dispatch l'action pour réinitialiser le score.
4. Efface le canvas.
5. Dessine à nouveau le serpent à sa position initiale
6. Dessine le fruit à une nouvelle position aléatoire.
7. Enfin, ajoute l'écouteur d'événement `handleKeyEvents` pour l'événement `keypress`.

Voici à quoi ressemblera notre fonction `resetBoard` :

```javascript
const resetBoard = useCallback(() => {
    window.removeEventListener("keypress", handleKeyEvents);
    dispatch(resetGame());
    dispatch(scoreUpdates(RESET_SCORE));
    clearBoard(context);
    drawObject(context, snake1, "#91C483");
    drawObject(
      context,
      [generateRandomPosition(width - 20, height - 20)],
      "#676FA3"
    ); //Dessine l'objet aléatoirement
    window.addEventListener("keypress", handleKeyEvents);
  }, [context, dispatch, handleKeyEvents, height, snake1, width]);
```

Vous devez placer cette fonction à l'intérieur du composant `CanvasBoard` et passer la fonction `resetBoard` comme prop à la fonction `Instruction` comme ci-dessous :

```jsx
<>
      <canvas
        ref={canvasRef}
        style={{
          border: `3px solid ${gameEnded ? "red" : "black"}`,
        }}
        width={width}
        height={height}
      />
      <Instruction resetBoard={resetBoard} />
    </>
```

Une fois cela placé, nous aurons le composant d'instruction configuré comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-17.png)
_Instructions avec bouton de réinitialisation_

## Jeu final

Si vous avez suivi jusqu'à ce point, alors félicitations ! Vous avez réussi à créer un jeu Snake amusant avec React, Redux et redux-sagas. Une fois que toutes ces choses sont connectées, votre jeu ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ezgif.com-gif-maker--2--1.gif)
_Le jeu Snake complet_

## Résumé

Voici comment vous pouvez construire un jeu Snake à partir de zéro. Vous pouvez trouver le code source complet du jeu dans le dépôt ci-dessous :

[https://github.com/keyurparalkar/snake-game](https://github.com/keyurparalkar/snake-game)

Si vous avez aimé l'idée de construire votre propre jeu Snake à partir de zéro, vous pouvez le faire passer à un niveau supérieur en construisant ces améliorations :

* Construire le jeu Snake avec three.js
* Ajouter un tableau de scores en ligne

Merci d'avoir lu !

Suivez-moi sur [Twitter](https://twitter.com/keurplkar), [GitHub](https://github.com/keyurparalkar), et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).