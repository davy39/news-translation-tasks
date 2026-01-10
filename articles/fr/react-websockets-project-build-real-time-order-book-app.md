---
title: Projet React + WebSockets – Construire une Application de Carnet d'Ordres en
  Temps Réel
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2022-04-19T17:15:27.000Z'
originalURL: https://freecodecamp.org/news/react-websockets-project-build-real-time-order-book-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/react-and-websockets-articlde.png
tags:
- name: React
  slug: react
- name: Redux
  slug: redux
- name: styled-components
  slug: styled-components
- name: websocket
  slug: websocket
seo_title: Projet React + WebSockets – Construire une Application de Carnet d'Ordres
  en Temps Réel
seo_desc: 'In this tutorial, we will see how to build an Order Book web application,
  that we''ll use to display real-time cryptocurrency info.

  We will use React with Typescript for creating the UI, Redux for managing the application
  state, and styled-components ...'
---

Dans ce tutoriel, nous verrons comment construire une application web de carnet d'ordres, que nous utiliserons pour afficher des informations sur les cryptomonnaies en temps réel.

Nous utiliserons [React avec TypeScript](https://create-react-app.dev/docs/adding-typescript/) pour créer l'interface utilisateur, [Redux](https://redux.js.org/) pour gérer l'état de l'application, et [styled-components](https://styled-components.com/) pour appliquer les styles. Et enfin, mais non des moindres, nous utiliserons [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) pour récupérer les flux de données.

### Dépôt GitHub

💡 Si vous souhaitez passer la lecture, [ici](https://github.com/mihailgaberov/orderbook) 👁️ est le dépôt GitHub avec un [README](https://github.com/mihailgaberov/orderbook/blob/main/README.md) détaillé 🙍‍♂️, et [ici](https://orderbook-mihailgaberov.vercel.app/) vous pouvez voir la démo en direct.

## Qu'est-ce qu'un Carnet d'Ordres ?

Un [Carnet d'Ordres](https://www.coindesk.com/crypto-trading-101-how-to-read-an-exchange-order-book) est une application qui affiche généralement des informations liées à l'achat et à la vente de produits.

💡 Le cas d'utilisation le plus courant est l'affichage de données pour divers actifs, tels que des actions, des obligations, des devises et même des cryptomonnaies.

## Pourquoi aurais-je besoin d'un Carnet d'Ordres ?

En pratique, les carnets d'ordres sont utilisés par les traders pour surveiller les fluctuations du prix d'achat et du prix de vente de certains produits – devises, actions, etc.

Cela se produit en temps réel, donc les changements peuvent être très rapides. C'est là que les WebSockets seront utiles, comme vous le verrez plus tard.

Dans le passé, les gens faisaient quelque chose de similaire sur papier, mais la partie "en temps réel" était impossible, bien sûr.

Un carnet d'ordres régulier a généralement deux côtés : l'achat (ou l'offre), affiché en vert à gauche, et la vente (ou la demande), en rouge, à droite.

![Classic Orderbook](https://www.freecodecamp.org/news/content/images/2021/09/image-43.png align="left")

*Carnet d'ordres classique*

## Le Plan pour notre Application de Carnet d'Ordres

Notre application de carnet d'ordres se composera de cinq parties :

* vue principale du carnet d'ordres

* boîte de sélection de regroupement

* bouton Basculer le Flux

* bouton Arrêter le Flux

* Message de Statut.

La conception de l'application ressemblera à ce qui est montré ci-dessous. Notez que le composant Message de Statut, que vous verrez dans mon implémentation, est absent sur ces captures d'écran :

![Desktop layout](https://www.freecodecamp.org/news/content/images/2021/09/image-60.png align="left")

*Disposition de bureau*

![Mobile layout](https://www.freecodecamp.org/news/content/images/2021/09/image-61.png align="left")

*Disposition mobile*

## **Fonctionnalités de l'Application**

### Carnet d'ordres

Le carnet d'ordres a deux côtés : le côté achat et le côté vente.

Les deux côtés contiennent des informations sur le nombre d'ordres ouverts à chaque niveau de prix.

Chaque niveau affiche :

* **Prix** : c'est ce qui définit le niveau. Comme les ordres doivent être placés à un prix qui est un multiple de la taille de tick du marché sélectionné (0,5), chaque niveau sera un incrément de 0,5 (tant qu'il y a un ordre ouvert à ce niveau).

* **Taille** : la quantité totale de contrats dérivés des ordres ouverts qui ont été placés à ce niveau.

* **Total** : le montant cumulé des contrats dérivés des ordres ouverts qui résident dans le carnet à ce niveau et au-dessus. Pour calculer le total d'un niveau donné, nous prenons la taille du niveau actuel et additionnons les tailles menant à ce niveau de prix dans le carnet d'ordres. Le total est également utilisé pour calculer le visualiseur de profondeur (barres colorées derrière les niveaux). La profondeur de chaque niveau est calculée en prenant le total de ce niveau en pourcentage du total le plus élevé dans le carnet.

### Boîte de Sélection de Regroupement

Par défaut, les ordres sont regroupés par la taille de tick du marché sélectionné (0,5).

Le basculement possible du regroupement est entre 0,5, 1, 2,5 pour le marché XBTUSD et 0,05, 0,1 et 0,25 pour le marché ETHUSD.

Pour regrouper les niveaux, nous combinons les niveaux arrondis à la taille de groupe la plus proche – par exemple, si nous changeons notre regroupement de 0,5 à 1, nous combinerions les données des prix 1000 et 1000,5 et les afficherions sous un seul niveau dans le carnet d'ordres avec le prix 1000.

### Bouton Basculer le Flux

Ce bouton bascule le marché sélectionné entre PI_XBTUSD et PI_ETHUSD. Ce sont les deux marchés que nous prendrons en charge → Bitcoin/USD et Ethereum/USD.

Il prend en charge la logique de regroupement dynamique et gère les regroupements pour XBT (0,5, 1, 2,5) et les regroupements pour ETH (0,05, 0,1, 0,25).

### Bouton Arrêter le Flux

Cliquer sur ce bouton arrête le flux.

Ensuite, cliquer sur ce bouton une deuxième fois relance le flux.

### Message de Statut

Ce message affichera le marché actuellement sélectionné. Il affichera également un message indiquant que le flux est arrêté.

## Pile Technologique pour notre Application

Voici une liste des principales technologies que nous utiliserons :

* [React avec TypeScript](https://create-react-app.dev/docs/adding-typescript/) (`yarn create react-app my-app --template typescript`) — une bibliothèque d'interface utilisateur que nous utiliserons pour construire les interfaces utilisateur de notre application.

* [Redux](https://redux.js.org/) — une bibliothèque de gestion d'état que nous utiliserons pour gérer l'état de notre application.

* [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) — L'objet `WebSocket` fournit l'API pour créer et gérer une connexion [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) à un serveur, ainsi que pour envoyer et recevoir des données sur la connexion. Nous l'utiliserons pour implémenter la logique de consommation des flux en direct ainsi que pour pouvoir arrêter et relancer.

* [styled-components](https://www.styled-components.com/docs) — une bibliothèque CSS-in-JS qui vous permet de définir les styles CSS de vos composants en utilisant des littéraux de gabarit ES6. Nous l'utiliserons pour ajouter des styles à notre application et rendre l'apparence et la convivialité belles. Elle utilise des littéraux de gabarit étiquetés pour styliser vos composants et supprime le mappage entre les composants et les styles. Cela signifie que lorsque vous définissez vos styles, vous créez en fait un composant React normal qui a vos styles attachés.

* [react-testing-library](https://github.com/testing-library/react-testing-library) — La `React Testing Library` est une solution très légère pour tester les composants React. Nous l'utiliserons pour tester les composants d'interface utilisateur de notre application.

* [Jest](https://jestjs.io/) - un Framework de Test JavaScript qui est devenu la norme de facto lorsque nous parlons de tester des applications React. Nous l'utiliserons pour écrire quelques tests unitaires qui couvriront les fonctions de réducteur que nous avons dans notre application.

## Comment Construire l'Application

À partir de ce point, je vais essayer de vous guider à travers le processus que j'ai suivi lors de la construction de cette application.

💡 Je dois dire que ce que je vous montre ici est juste **une façon** de créer une telle application – mais ce n'est pas **la façon** à aucun égard. Probablement, des personnes avec plus d'expérience en crypto le feraient mieux.

### Structure du Projet

La structure du projet est assez simple. Nous utilisons React et styled-components, ce qui rend cette façon de structurer très pratique.

Voyons d'abord à quoi cela ressemble, puis je vous expliquerai le quoi et le pourquoi.

![Project structure](https://www.freecodecamp.org/news/content/images/2021/10/image-31.png align="left")

*Structure du projet*

Comme vous pouvez le voir sur l'image ci-dessus, j'ai organisé la plupart des composants dans des dossiers. Chaque dossier contient un fichier `index.tsx`, un fichier `styles.tsx` et un fichier `.test.tsx`.

**index.tsx** – contient le code responsable de la logique du composant.

**styles.tsx** – contient le code responsable du style du composant. C'est là que styled-components brille.

**.test.tsx** – ceux-ci contiennent les tests unitaires des composants.

Permettez-moi de vous donner un bref résumé de l'idée derrière chacun des composants dans le dossier `components`. En commençant par le haut vers le bas :

[Button](https://github.com/mihailgaberov/orderbook/tree/main/src/components/Button) rend un bouton avec une couleur de fond donnée et un titre. Il est utilisé pour les deux boutons dans le pied de page, `Toggle Feed` et `Kill Feed / Renew Feed`.

[DepthVisualizer](https://github.com/mihailgaberov/orderbook/tree/main/src/components/DepthVisualizer) est le composant responsable du dessin des arrière-plans rouges et verts que vous voyez derrière les nombres. Il le fait en rendant une ligne (un élément HTML `div`) avec une largeur donnée, une position étant à gauche (Bids) ou à droite (Asks).

[Footer](https://github.com/mihailgaberov/orderbook/tree/main/src/components/Footer) – eh bien, il n'y a pas grand-chose à dire ici, il contient les deux boutons utilisés dans l'application.

[GroupingSelectBox](https://github.com/mihailgaberov/orderbook/tree/main/src/components/GroupingSelectBox) rend la boîte de sélection que nous utilisons pour changer la valeur de regroupement, en utilisant le réducteur setGrouping pour modifier l'état de l'application lorsque le regroupement est modifié.

[Header](https://github.com/mihailgaberov/orderbook/tree/main/src/components/Header) rend le titre de l'application ainsi que le composant GroupingSelectBox.

[Loader](https://github.com/mihailgaberov/orderbook/tree/main/src/components/Loader) rend l'animation de chargement implémentée en utilisant [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG).

[Order Book](https://github.com/mihailgaberov/orderbook/tree/main/src/components/OrderBook) contient la logique principale de l'application. Les composants séparés sont situés dans des sous-dossiers, et la logique de gestion d'état Redux est également ici.

[Spread](https://github.com/mihailgaberov/orderbook/tree/main/src/components/Spread) rend la valeur de l'écart, affichée au milieu de l'en-tête (en vue bureau). Le composant lui-même contient des méthodes courtes pour calculer le montant lui-même et la valeur en pourcentage.

[StatusMessage](https://github.com/mihailgaberov/orderbook/tree/main/src/components/StatusMessage) est un petit composant utilisé pour afficher les *messages de statut*. Il montre essentiellement quel marché est actuellement affiché et si le flux est arrêté.

### **Performance de Rendu**

Voici un bon moment pour parler un peu de la *performance de rendu* et du *style en ligne*.

Le **rendu** est le processus par lequel React demande à vos composants de décrire à quoi ils veulent que leur section de l'interface utilisateur ressemble, en fonction de la combinaison actuelle de props et d'état.

Ce processus est déclenché par un changement de l'état dans votre composant. Ce changement peut être causé par certaines des props étant modifiées ou par une logique interne du composant.

Le point ici est que lorsque le re-rendu se produit inutilement, cela réduit les performances de notre application. C'est exactement ce qui m'est arrivé lorsque j'ai introduit l'implémentation initiale du composant *DepthVisualizer*. Il utilisait styled-components, c'est-à-dire JavaScript, pour la partie dessin.

Pour résoudre ce problème, j'ai modifié le composant pour utiliser des styles en ligne, c'est-à-dire du CSS pur, au lieu d'une approche CSS dans JS. En d'autres termes, mon goulot d'étranglement était l'utilisation d'animations JavaScript, ce qui est une raison célèbre de réduction des performances.

Voici à quoi cela ressemble maintenant :

```jsx
const DepthVisualizer: FunctionComponent<DepthVisualizerProps> = ({windowWidth, depth, orderType }) => {
  return <div style={{
    backgroundColor: `${orderType === OrderType.BIDS ? DepthVisualizerColors.BIDS : DepthVisualizerColors.ASKS}`,
    height: "1.250em",
    width: `${depth}%`,
    position: "relative",
    top: 21,
    left: `${orderType === OrderType.BIDS && windowWidth > MOBILE_WIDTH ? `${100 - depth}%` : 0}`,
    marginTop: -24,
    zIndex: 1,
  }} />;
};

export default DepthVisualizer;
```

Le *style en ligne* consiste à écrire votre CSS avec votre balisage, en tant que valeurs pour l'attribut `style`. Ce n'est pas considéré comme une bonne pratique, mais comme vous pouvez le voir ici, il y a des cas où il est nécessaire de l'utiliser.

💡 Habituellement, vous extrairiez votre code CSS dans un fichier séparé.

[Footer](https://github.com/mihailgaberov/orderbook/tree/main/src/components/Footer) un simple composant factice utilisé pour rendre les deux boutons dans le pied de page de l'application.

Les composants factices, également connus sous le nom de composants sans état ou de représentation, sont des composants qui ne contiennent pas d'état et sont généralement utilisés uniquement pour visualiser des données de quelque manière. Ces données sont transmises via les props. Par exemple, le drapeau `isFeedKilled` dans le composant ci-dessus.

Si un tel composant doit exécuter une sorte d'interaction, il le fait généralement en acceptant (à nouveau via les props, par exemple `toggleFeedCallback`) des fonctions de rappel qui peuvent être exécutées lorsque cette interaction se produit. Par exemple, cliquer sur un bouton.

De l'autre côté, nous pourrions avoir des composants intelligents ou avec état. Ce sont ceux qui sont connectés à l'état de l'application et peuvent le manipuler directement. Habituellement, ce sont ceux qui lisent les données de l'état et les transmettent aux composants sans état via leurs props.

[GroupingSelectBox](https://github.com/mihailgaberov/orderbook/tree/main/src/components/GroupingSelectBox) contient l'élément Select que vous pouvez utiliser pour basculer entre les regroupements.

[Header](https://github.com/mihailgaberov/orderbook/blob/main/src/components/Header/index.tsx) est la partie d'en-tête de l'application. Il s'occupe de définir correctement la disposition composée du titre 'Order Book' à gauche et de la boîte de sélection à droite.

[Loader](https://github.com/mihailgaberov/orderbook/tree/main/src/components/Loader) est utilisé comme indicateur lorsque les données n'ont pas encore été chargées. Il utilise une animation SVG que j'ai trouvée en ligne.

[Order Book](https://github.com/mihailgaberov/orderbook/tree/main/src/components/OrderBook) est là où se passe la vraie chose. Celui-ci se compose de quelques composants plus petits :

* [TableContainer](https://github.com/mihailgaberov/orderbook/blob/d8db0239763dce32fbcae499a6b7deefed9f684f/src/components/OrderBook/styles.tsx#L21) – utilisé pour styliser les vues des côtés Odds et Bets.

* [TitleRow](https://github.com/mihailgaberov/orderbook/blob/main/src/components/OrderBook/TitleRow/index.tsx) – c'est le composant responsable de l'affichage des titres des colonnes : prix, taille et total, respectivement.

### Comment Construire l'Interface Utilisateur avec React et styled-components

Lorsque nous parlons de structure basée sur les composants, comme celle que [React](https://reactjs.org/) nous fournit, la [bibliothèque styled-components](https://styled-components.com/) est probablement l'un des premiers choix que vous pourriez faire lorsque le style est nécessaire.

Comme le dit [Josh Comeau](https://www.joshwcomeau.com/) dans son article détaillé [article](https://www.joshwcomeau.com/css/styled-components/) :

> 💡 C'est un outil merveilleux. À bien des égards, il a changé ma façon de penser l'architecture CSS et m'a aidé à garder ma base de code propre et modulaire, tout comme React !

Comme le suggère le nom de la bibliothèque, nous pouvons facilement styliser nos composants en utilisant le [modèle CSS-in-JS](https://reactjs.org/docs/faq-styling.html#what-is-css-in-js). Voici un exemple de la façon dont je l'ai utilisé pour écrire les styles de mon composant `Button` :

```jsx
import styled from "styled-components";

interface ContainerProps {
  backgroundColor: string;
}

export const Container = styled.button<ContainerProps>`
  padding: .3em .7em;
  margin: 1em;
  border-radius: 4px;
  border: none;
  color: white;
  background: ${props => props.backgroundColor};
  font-family: "Calibri", sans-serif;
  font-size: 1.2em;
  
  &:hover {
    cursor: pointer;
    opacity: .8;
  }
`
```

Remarquez comment j'utilise une `interface` dans mon fichier de styles, ainsi que la propriété `background` transmise en tant qu'argument via `props`. Cela fait partie de l'histoire CSS-in-JS.

La possibilité d'utiliser du code CSS en JavaScript ou (comme certains pourraient dire) vice versa est très pratique. Par exemple, lorsque nous avons besoin qu'un composant ait un aspect différent en fonction de quelque chose, nous pouvons transmettre via ses props un paramètre pour définir cela.

Comme chaque style est en fait un composant, cette façon d'écrire des styles ressemble beaucoup à l'écriture de composants React. Je veux dire, en fin de compte, tout est des composants, n'est-ce pas ?

### Détection de la Visibilité de la Page et Réactivité

Tout en travaillant sur cette application, j'ai lu à plusieurs endroits que, pour les applications qui prennent en charge des mises à jour rapides, il est bon de mettre en œuvre un mécanisme pour mettre en pause l'ensemble lorsque l'application n'est pas utilisée par l'utilisateur. Par exemple, lorsque l'utilisateur minimise la fenêtre du navigateur ou ouvre simplement un autre onglet.

Puisque notre carnet d'ordres consomme beaucoup de nouveaux morceaux de données chaque seconde via WSS, j'ai décidé de mettre en œuvre un tel mécanisme également.

Ce que cela fait est :

* il montre un chargeur lorsque les données ne sont pas encore là

* il change le titre méta pour signifier que l'application est en mode `pause`

* il reprend le travail une fois que la fenêtre de l'application est au premier plan

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-114.png align="left")

*Mode actif*

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-115.png align="left")

*Mode pause*

Vous pouvez voir l'implémentation complète [ici](https://github.com/mihailgaberov/orderbook/blob/main/src/App.tsx).

La partie essentielle se trouve dans le hook useEffect, qui n'est déclenché qu'une seule fois lorsque l'application est rendue pour la première fois.

Là, nous tirons parti de l'API de visibilité de la page en attachant les écouteurs nécessaires. Ensuite, dans les [gestionnaires](https://github.com/mihailgaberov/orderbook/blob/e74dfad48990ff1a1f12ac45f5a065cc5044ee75/src/App.tsx#L61), nous exécutons simplement la logique que nous voulons.

### Détection de la Taille de la Fenêtre

Dans presque toutes les applications qui ont un certain niveau de réactivité, vous avez besoin d'une logique pour détecter les changements de la taille de la fenêtre et prendre des mesures en conséquence.

En d'autres termes, vous devez savoir quand votre application est visualisée dans une certaine taille d'écran, afin que vous puissiez organiser vos composants et ajuster vos styles pour que tout ait l'air bien et en place.

Cela est particulièrement valable pour les applications mobiles, où la réactivité est essentielle.

Notre implémentation de la détection des changements de taille de la fenêtre est basée sur la propriété `innerWidth` de l'objet [fenêtre du navigateur](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerWidth) et l'événement `onresize` qui est déclenché lorsqu'il est redimensionné.

J'attache un écouteur pour cet événement dans un hook `useEffect` dans le [fichier App.tsx](https://github.com/mihailgaberov/orderbook/blob/bd24e610e9fc4e271a6820a297b78decf4950fd9/src/App.tsx#L32). Ensuite, chaque fois que la taille de la fenêtre change, je définis la nouvelle largeur sur une variable d'état via le hook `setWindowWidth`.

```jsx
const [windowWidth, setWindowWidth] = useState(0);
...
...

// Détection de la largeur de la fenêtre
useEffect(() => {
  window.onresize = () => {
    setWindowWidth(window.innerWidth);
  }
  setWindowWidth(() => window.innerWidth);
}, []);
```

Ensuite, propagez cette variable vers le bas à travers tous les composants intéressés et utilisez-la en conséquence. Par exemple, voici comment je l'utilise dans [Order Book/index.tsx](https://github.com/mihailgaberov/orderbook/blob/main/src/components/OrderBook/index.tsx) afin de savoir quand et où rendre le composant TitleRow.

```jsx
{windowWidth > MOBILE_WIDTH && <TitleRow windowWidth={windowWidth} reversedFieldsOrder={false} />}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-142.png align="left")

*Composant TitleRow - vue bureau*

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-143.png align="left")

*Composant TitleRow - vue mobile*

Notez qu'il apparaît à différentes positions selon que vous voyez l'application sur bureau ou mobile.

Vous pouvez jeter un coup d'œil au [composant](https://github.com/mihailgaberov/orderbook/blob/main/src/components/OrderBook/TitleRow/index.tsx) lui-même et voir une approche similaire d'utilisation de la largeur de la fenêtre.

### Gestion d'État avec Redux

Comme vous l'avez probablement deviné, j'ai utilisé [Redux](https://redux.js.org/) pour gérer l'état de l'application.

La logique principale derrière cela est concentrée dans le [orderbookSlice](https://github.com/mihailgaberov/orderbook/blob/main/src/components/OrderBook/orderbookSlice.ts) reducer. Dans les lignes suivantes, je vais vous guider à travers et voir comment et pourquoi je l'ai construit de cette manière.

Tout d'abord, nous définissons l'interface et l'état initial de nos données de carnet d'ordres. L'état initial contient les valeurs par défaut dont nous avons besoin au démarrage de l'application.

```jsx
export interface OrderbookState {
  market: string;
  rawBids: number[][];
  bids: number[][];
  maxTotalBids: number;
  rawAsks: number[][];
  asks: number[][];
  maxTotalAsks: number;
  groupingSize: number;
}

const initialState: OrderbookState = {
  market: 'PI_XBTUSD', // PI_ETHUSD
  rawBids: [],
  bids: [],
  maxTotalBids: 0,
  rawAsks: [],
  asks: [],
  maxTotalAsks: 0,
  groupingSize: 0.5
};
```

Ensuite, il y a quelques méthodes courtes et explicites qui aident à manipuler les données des niveaux :

```jsx
const removePriceLevel = (price: number, levels: number[][]): number[][] => levels.filter(level => level[0] !== price);

const updatePriceLevel = (updatedLevel: number[], levels: number[][]): number[][] => {
  return levels.map(level => {
    if (level[0] === updatedLevel[0]) {
      level = updatedLevel;
    }
    return level;
  });
};

const levelExists = (deltaLevelPrice: number, currentLevels: number[][]): boolean => currentLevels.some(level => level[0] === deltaLevelPrice);

const addPriceLevel = (deltaLevel: number[], levels: number[][]): number[][] => {
  return [ ...levels, deltaLevel ];
};
```

Ensuite, la vraie magie opère. Si la taille retournée par un delta est 0, alors ce niveau de prix doit être supprimé du carnet d'ordres. Sinon, vous pouvez écraser en toute sécurité l'état de ce niveau de prix avec les nouvelles données retournées par ce delta.

```jsx
/** Les ordres retournés par le flux sont au format
 de [price, size][].
 * @param currentLevels Niveaux de prix existants - `bids` ou `asks`
 * @param orders Mise à jour d'un niveau de prix
 */
const applyDeltas = (currentLevels: number[][], orders: number[][]): number[][] => {
  let updatedLevels: number[][] = currentLevels;

  orders.forEach((deltaLevel) => {
    const deltaLevelPrice = deltaLevel[0];
    const deltaLevelSize = deltaLevel[1];

    // Si la nouvelle taille est zéro - supprimer le niveau de prix
    if (deltaLevelSize === 0 && updatedLevels.length > ORDERBOOK_LEVELS) {
      updatedLevels = removePriceLevel(deltaLevelPrice, updatedLevels);
    } else {
      // Si le niveau de prix existe et que la taille n'est pas zéro, le mettre à jour
      if (levelExists(deltaLevelPrice, currentLevels)) {
        updatedLevels = updatePriceLevel(deltaLevel, updatedLevels);
      } else {
        // Si le niveau de prix n'existe pas dans le carnet d'ordres et qu'il y a moins de 25 niveaux, l'ajouter
        if (updatedLevels.length < ORDERBOOK_LEVELS) {
          updatedLevels = addPriceLevel(deltaLevel, updatedLevels);
        }
      }
    }
  });

  return updatedLevels;
}
```

Ce qui suit après cela, ce sont quelques méthodes d'assistance. Permettez-moi de dire quelques mots sur chacune d'elles maintenant :

* [addTotalSums](https://github.com/mihailgaberov/orderbook/blob/e74dfad48990ff1a1f12ac45f5a065cc5044ee75/src/components/OrderBook/orderbookSlice.ts#L82) – avec l'aide de cette méthode, nous parcourons les données des ordres, bids ou asks, et calculons pour chacun d'eux la somme totale. La valeur de la somme totale est ensuite utilisée pour réaliser les visualisations de fond.

* [addDepths](https://github.com/mihailgaberov/orderbook/blob/e74dfad48990ff1a1f12ac45f5a065cc5044ee75/src/components/OrderBook/orderbookSlice.ts#L99) – nous utilisons cette méthode pour calculer la soi-disant *profondeur* pour chaque ordre. Ces valeurs seront utilisées plus tard par le composant de mesure de profondeur pour afficher les lignes rouges et vertes en arrière-plan.

* [getMaxTotalSum](https://github.com/mihailgaberov/orderbook/blob/e74dfad48990ff1a1f12ac45f5a065cc5044ee75/src/components/OrderBook/orderbookSlice.ts#L113) – celle-ci retourne la valeur maximale de toutes les sommes totales.

Tout ce qui suit est ce que nous utilisons pour créer l'état de l'application. Selon la [documentation de Redux Toolkit](https://redux-toolkit.js.org/rtk-query/overview#create-an-api-slice), elle utilise l'API `createSlice` pour créer le *slice*.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-116.png align="left")

*État Redux*

La création d'un slice nécessite un nom de chaîne pour identifier le slice, une valeur d'état initiale, et une ou plusieurs fonctions de réducteur pour définir comment l'état peut être mis à jour.

Une fois qu'un slice est créé, nous pouvons exporter les créateurs d'actions Redux générés et la fonction de réducteur pour le slice entier.

Les dernières lignes consistent en les exports en question – créateurs d'actions, sélecteurs de slices d'état et le réducteur principal.

```jsx
export const { addBids, addAsks, addExistingState, setGrouping, clearOrdersState } = orderbookSlice.actions;
```

```jsx
export const selectBids = (state: RootState): number[][] => state.orderbook.bids;
export const selectAsks = (state: RootState): number[][] => state.orderbook.asks;
export const selectGrouping = (state: RootState): number => state.orderbook.groupingSize;
export const selectMarket = (state: RootState): string => state.orderbook.market;
```

```jsx
export default orderbookSlice.reducer;
```

Avec tout cela, notre logique de manipulation d'état est complète. 🎉

Maintenant, il est temps de jeter un coup d'œil au protocole que nous avons utilisé dans notre application pour tirer parti de tous ces changements rapides dans les données que nous consommons.

### Protocole WebSocket (WSS)

Comme vous l'avez peut-être remarqué, nous utilisons le protocole de communication [Web Socket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) pour récupérer des données dans notre application. Nous utilisons également ses fonctionnalités, comme vous le verrez dans un instant, pour accomplir d'autres choses (comme basculer les flux et s'abonner/désabonner du canal de données).

[Ici](https://github.com/mihailgaberov/orderbook/blob/main/src/components/OrderBook/index.tsx) se trouve comment je l'ai utilisé.

Au lieu d'essayer de m'appuyer sur une implémentation manuelle, j'ai utilisé le package [react-use-websocket](https://www.npmjs.com/package/react-use-websocket). Il vous donne tout ce dont vous avez besoin lorsque vous souhaitez utiliser WSS dans une application React. Si vous souhaitez entrer dans les détails à ce sujet, vous pouvez consulter leur [documentation](https://github.com/robtaussig/react-use-websocket#readme).

### Quelques mots sur mon implémentation

Ce dont nous avons besoin en premier, c'est l'URL du point de terminaison d'où proviennent les flux de données. Je suis sûr qu'il existe plusieurs options lorsque nous parlons de cryptomonnaies. Dans notre application, j'ai utilisé celle fournie par [www.cryptofacilities.com/](http://www.cryptofacilities.com/).

```jsx
const WSS_FEED_URL: string = 'wss://www.cryptofacilities.com/ws/v1';
```

Ensuite, la seule chose que nous devons faire pour commencer à consommer les données est de mettre le hook `useWebSocket` au travail. Comme vous l'avez probablement deviné, ce hook est fourni par le package mentionné ci-dessus.

```jsx
import useWebSocket from ["react-use-websocket"](<https://github.com/robtaussig/react-use-websocket>);

...
...
...

const { sendJsonMessage, getWebSocket } = useWebSocket(WSS_FEED_URL, {
    onOpen: () => console.log('Connexion WebSocket ouverte.'),
    onClose: () => console.log('Connexion WebSocket fermée.'),
    shouldReconnect: (closeEvent) => true,
    onMessage: (event: WebSocketEventMap['message']) =>  processMessages(event)
  });
```

Nous passons le point de terminaison comme premier argument et quelques fonctions de rappel après cela. Celles-ci nous aident à effectuer certaines actions lorsque l'un des événements suivants se produit :

* `onOpen` – ce qu'il faut faire lorsque la connexion WebSocket est établie.

* `onClose` – ce qu'il faut faire lorsque la connexion WebSocket est terminée.

* `shouldReconnect` – ce n'est qu'un drapeau, indiquant si nous voulons une reconnexion automatique lorsque la connexion est interrompue pour une raison quelconque.

* `onMessage` – c'est l'événement principal qui nous apporte les morceaux de données (j'appelle la méthode `processMessage` chaque fois que cela se produit. Cela signifie que chaque fois qu'un nouveau morceau de données est reçu, nous le traitons et l'affichons respectivement).

Ci-dessous se trouve la méthode en question. Elle fait simplement deux choses :

* Soit elle appelle une méthode appelée `process` (sans jeu de mots 😄) – cette méthode est appelée chaque fois que de nouvelles données pour les offres ou les demandes sont reçues et elle les traite en conséquence.

* Elle envoie un événement qui utilise l'une des [fonctions de réducteur](https://github.com/mihailgaberov/orderbook/blob/e74dfad48990ff1a1f12ac45f5a065cc5044ee75/src/components/OrderBook/orderbookSlice.ts#L148) que nous avons vues précédemment. Cette fonction crée pratiquement l'état initial de notre application.

Afin de décider si nous ajoutons des données à l'état actuel ou si nous devons l'initialiser, nous vérifions une propriété appelée `numLevels`. C'est quelque chose qui provient de l'API, la toute première fois que nous établissons la connexion WebSocket.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-117.png align="left")

*Charge utile initiale*

Le reste du code que vous voyez dans ce [fichier](https://github.com/mihailgaberov/orderbook/blob/main/src/components/OrderBook/index.tsx) est principalement pour préparer et rendre les résultats à l'écran.

La partie la plus intéressante serait la méthode `buildPriceLevels` qui est utilisée pour les deux moitiés – les offres et les demandes. Elle trie les données, effectue les calculs nécessaires et les transmet aux composants pertinents pour les visualiser. Ce sont `DepthVisualizer` et `PriceLevelRow` que j'ai mentionnés plus tôt dans cet article.

## Regroupement

Le regroupement est une partie importante du fonctionnement du carnet d'ordres, car il définit par quelle taille de ticket les ordres sont regroupés.

Dans notre application, j'ai implémenté une fonctionnalité de basculement par marché, qui permet de les regrouper comme suit :

* Entre 0,5, 1, 2,5 pour le marché XBTUSD.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-118.png align="left")

*Regroupement du marché XBTUSD*

* Entre 0,05, 0,1 et 0,25 pour le marché ETHUSD.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-119.png align="left")

*Regroupement du marché ETHUSD*

Il y a un petit extrait que j'ai créé en essayant de comprendre comment implémenter la logique de regroupement. Vous pouvez le trouver [ici](https://gist.github.com/mihailgaberov/5faa2c1c3e4fd3e0593ad68861b989ce).

De plus, en dehors de cet extrait, lors du développement de cela, j'ai effectué plus de quelques expériences en dehors du projet lui-même. Et juste parce que ce sont des fichiers locaux sur mon ordinateur, je vais les publier ici pour ceux d'entre vous qui sont encore plus curieux.

C'est un petit projet npm secondaire qui n'a qu'une seule dépendance. Voici le fichier package.json :

```jsx
{
  "name": "grouping",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "dependencies": {
    "lodash.groupby": "^4.6.0"
  }
}
```

Et voici le code lui-même :

```jsx
const bids = [
    [
        50163,
        110
    ],
    [
        50162,
        13140
    ],
    [
        50158,
        3763
    ],
    [
        50156,
        1570
    ],
    [
        50155,
        21997
    ],
    [
        50152.5,
        450
    ],
    [
        50151,
        4669
    ],
    [
        50150.5,
        10329
    ],
    [
        50150,
        2500
    ],
    [
        50149.5,
        450
    ],
    [
        50149,
        4022
    ],
    [
        50148,
        20000
    ],
    [
        50147,
        5166
    ],
    [
        50146.5,
        5274
    ],
    [
        50145,
        174609
    ],
    [
        50143,
        20000
    ],
    [
        50141,
        28000
    ],
    [
        50140.5,
        5000
    ],
    [
        50138,
        6000
    ],
    [
        50132.5,
        4529
    ],
    [
        50132,
        4755
    ],
    [
        50131,
        12483
    ],
    [
        50128.5,
        61115
    ],
    [
        50128,
        23064
    ],
    [
        50125.5,
        181363
    ]
]

/* function roundDownNearest(num, acc) {
    if (acc < 0) {
        return Math.floor(num * acc) / acc;
    } else {
        return Math.floor(num / acc) * acc;
    }
} */

/* function groupByTicketSize(ticketSize, levels) {
    const result = levels.map((element, idx) => {
        const nextLevel = levels[idx + 1];

        if (nextLevel) {
            const currentPrice = element[0];
            const currentSize = element[1];
            const nextPrice = nextLevel[0];
            const nextSize = nextLevel[1];
            console.log("current level: ", element)
            console.log("next level: ", nextLevel)

            element[0] = roundDownNearest(currentPrice, ticketSize);

            if (currentPrice - nextPrice < ticketSize) {
                element[1] = currentSize + nextSize;
            }
            console.log("==================================> Result: ", element)

            return element;
        }

    }).filter(Boolean); 
   

    console.log("============================================================");
    console.log(result)
} */

const test = [
    [1004.5, 1],
    [1001.5, 1],
    [1001,   1],
    [1000.5, 1],
    [1000,   1],
    [999.5,  1],
    [999,    1],
    [990,    1],
    [988,    1]
]

function groupByTicketSize(ticketSize, levels) {
    const result = [];

    for (let i = 0; i < levels.length; i++) {
        console.log(levels[i])
        const prevLevel = levels[i-1]
        const level1 = levels[i]
        const level2 = levels[i+1]

        if (prevLevel && level1 && level1[0] - ticketSize === prevLevel) return

        if (level2 && level1[0] - level2[0] < ticketSize) {
            const newLevel = [level2[0], level1[1] + level2[1]];
            console.log("newLevel", newLevel)
            result.push(newLevel);
        } else {
            result.push(level1)
        }
    }

    console.log("============================================================");
    console.log(result)
}

// groupByTicketSize(1, bids);
groupByTicketSize(1, test);
```

## Comment Effectuer des Tests Unitaires sur l'Application

Pour effectuer des tests unitaires, j'ai utilisé [react-testing-library](https://testing-library.com/docs/react-testing-library/intro/).

L'idée principale derrière cela est que le développeur doit écrire des tests uniquement pour ce que l'utilisateur verra et avec quoi il interagira. Il n'y a pas beaucoup d'intérêt à tester les détails d'implémentation.

💡 Imaginez, juste pour vous donner un exemple, que vous avez implémenté un composant de liste qui affiche simplement des lignes de données textuelles. Disons quelque chose comme une liste de tâches.

Ensuite, imaginez que ces données proviennent d'un appel d'API sous forme de tableau. Une structure de données que vous pourriez facilement parcourir via diverses méthodes – une sorte de cycle de boucle, comme for() ou while(). Ou vous pourriez utiliser une autre approche plus fonctionnelle, disons la méthode .map().

Maintenant, demandez-vous – pour l'utilisateur final, celui qui verra simplement les données textuelles listées, votre implémentation a-t-elle de l'importance ? Tant que tout fonctionne comme prévu et de manière performante, la réponse est « non, cela n'a pas d'importance ».

C'est ce que vos tests doivent refléter.

Dans le contexte de notre application Order Book, chaque fichier de test est situé dans le même répertoire que le fichier d'implémentation. La plupart des tests sont courts et explicites, en raison du fait que ceux-ci testent principalement la logique de rendu et uniquement le [chemin heureux](https://en.wikipedia.org/wiki/Happy_path).

Par exemple, jetons un coup d'œil aux tests du composant bouton ci-dessous :

```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import Button from './index';

test('renders button with title', () => {
  render(<Button backgroundColor={'red'} callback={jest.fn} title={'Toggle'} />);
  const btnElement = screen.getByText(/Toggle/i);
  expect(btnElement).toBeInTheDocument();
});
```

Il vérifie simplement que le composant est rendu correctement et qu'il affiche ce que nous attendons que l'utilisateur voie. Ce qui est le titre *Toggle* dans ce cas.

Pour tester les [réducteurs](https://github.com/mihailgaberov/orderbook/blob/main/src/components/OrderBook/orderbookSlice.test.ts), j'ai utilisé [Jest](https://jestjs.io/), car c'est la seule partie non visuelle que nous couvrirons. Ces tests sont également assez simples et explicites. Je les utilise pour tester si l'état initial de l'application est en place et pour voir que l'ajout de niveaux de prix à cet état fonctionne correctement.

## Comment Déployer l'Application sur Vercel

Enfin – le moment du déploiement. 🎉

Après avoir terminé le développement et les tests de notre application, mettons-la en ligne.

J'ai utilisé la plateforme [Vercel](https://vercel.com/) à cette fin. Ils offrent une interface assez riche et facile à utiliser ainsi que des intégrations pour toutes les plateformes de contrôle de source célèbres – y compris, bien sûr, GitHub (où vit notre dépôt d'application).

En supposant que vous avez un compte GitHub, ce que vous devez faire si vous souhaitez le déployer vous-même est de vous connecter avec celui-ci [ici](https://vercel.com/login).

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-120.png align="left")

*Écran de connexion Vercel*

Cliquez sur le bouton *+Nouveau Projet* dans le coin supérieur droit. Ensuite, importez votre dépôt Git en utilisant les options fournies dans l'écran qui s'ouvre. Voici à quoi ressemble le mien :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-121.png align="left")

*Écran d'importation du dépôt Git Vercel*

Après avoir importé le projet, vous pourrez effectuer le déploiement réel. Une fois terminé, Vercel générera des URL pour vous permettre d'accéder à votre application nouvellement déployée.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-122.png align="left")

*Écran de déploiement de production Vercel*

Et je pense que vous recevrez un e-mail vous informant si votre déploiement a réussi. Cet e-mail contient également ces URL.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-123.png align="left")

*E-mail de déploiement réussi de Vercel*

Félicitations ! 👍🏻

Vous avez maintenant votre propre [application de carnet d'ordres](https://orderbook-mihailgaberov.vercel.app/) en ligne et opérationnelle.

## Comment Ajouter un Badge de Build sur GitHub

Ce n'est pas lié au carnet d'ordres, mais j'ai décidé de le partager avec vous ici quand même. Il s'agit de ces petits détails qui rendent le tableau d'ensemble d'une certaine manière plus complet et attrayant.

Peut-être que certains d'entre vous se sont demandés comment obtenir l'un de ces soi-disant *badges* ?

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-124.png align="left")

Voici la réponse : [https://shields.io/](https://shields.io/).

Vous allez dans la [section Autres](https://shields.io/category/other) et trouvez l'option Déploiements GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-125.png align="left")

Ensuite, cliquez dessus et suivez les instructions.

Il y a une chose de plus que vous devez faire pour que cela fonctionne pleinement. Vous allez dans votre dépôt GitHub → [Actions](https://github.com/mihailgaberov/orderbook/actions) et créez un nouveau fichier de workflow. Vous pouvez simplement copier le contenu du [mien depuis ici](https://github.com/mihailgaberov/orderbook/actions/runs/2143399541/workflow). Nommez-le *main.yml*.

Ce que cela fera, c'est exécuter les tâches définies dans ce fichier. Dans notre cas, il s'agit simplement de la tâche de build qui consiste essentiellement à lancer une nouvelle build et à exécuter les tests.

Après avoir terminé cela, vous devez simplement ajouter les lignes suivantes à votre fichier [README](https://github.com/mihailgaberov/orderbook/blob/main/README.md) :

```markdown
<!-- prettier-ignore-start -->
[![Tests](<https://github.com/mihailgaberov/orderbook/actions/workflows/main.yml/badge.svg>)](<https://github.com/mihailgaberov/orderbook/actions/workflows/main.yml>)
[![Build Status][build-badge]][build]

[build-badge]: <https://img.shields.io/github/deployments/mihailgaberov/orderbook/production?label=vercel&logoColor=vercel>
[build]: <https://github.com/mihailgaberov/orderbook/deployments>
<!-- prettier-ignore-end -->
```

💡 N'oubliez pas de mettre vos propres détails dans les URL, c'est-à-dire votre nom d'utilisateur GitHub et le nom de votre dépôt.

Après avoir poussé ces changements, vous devriez voir les badges affichés sur votre README : 🧑‍💻.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-126.png align="left")

*Badges GitHub*

## Conclusion

Si vous lisez ceci depuis le début, je vous nommerai champion. 🍾

Cela a été un long voyage, mais j'espère intéressant et amusant à parcourir avec moi !

Maintenant, il est temps de résumer ce que nous avons fait ici et d'essayer d'extraire quelques informations utiles qui nous aideront dans nos futurs défis de développement.

Je vais exposer ci-dessous mon opinion sur ce qui a été le plus difficile dans la construction de cette application. Et je serai encore plus impatient de découvrir ce qui est le vôtre.

### Performance de Rendu

Cela m'a vraiment mordu au début, lorsque je construisais l'interface utilisateur et que j'essayais d'implémenter le dessin des lignes de niveaux de prix.

J'ai mentionné plus tôt comment j'ai réussi à résoudre ce problème et je pense que c'est quelque chose que je me souviendrai certainement.

### Fonctionnalité de Regroupement

L'implémentation de cela a également été un peu difficile car il y avait plusieurs facteurs que je devais prendre en compte. À cause du marché dans lequel nous sommes et de la plage dans laquelle je devais effectuer les calculs.

Cela m'a pris un certain temps pour le peaufiner (souvenez-vous du mini-projet secondaire et de l'extrait que j'ai partagé dans les sections précédentes) et je pense toujours qu'il pourrait être amélioré encore plus. Essayez de basculer entre les marchés et les valeurs de regroupement plusieurs fois et observez les résultats.

### Espace pour Amélioration

Une chose déjà mentionnée est certainement le regroupement. Ce qui devrait également améliorer la visualisation des parties rouges et vertes – elles (presque) toujours devraient former un triangle non idéal.

Si nous essayons de regarder le tableau d'ensemble, cette application de carnet d'ordres peut faire partie d'un écran de tableau de bord rempli d'autres widgets également, et ils peuvent tous interagir entre eux.

Par exemple, changer le regroupement du carnet d'ordres pour refléter le changement des vues dans les autres widgets également – disons montrer un graphique de marché comme celui ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-127.png align="left")

Je ne mentionne même pas l'ajout de nouveaux marchés comme une *amélioration*, car c'est un peu clair. Mais cela devrait être pris en compte lors de la construction de la fonctionnalité pour les marchés actuels, afin de le faire de manière à ce qu'il soit facilement extensible. De sorte que l'ajout d'un nouveau marché au carnet d'ordres soit une tâche triviale et rapide à faire.

Je pense que c'est tout de ma part.

Merci d'avoir lu ! 🙏

## Références

Voici quelques liens que vous pourriez trouver utiles à lire :

[The styled-components Happy Path](https://www.joshwcomeau.com/css/styled-components/)

[Blogged Answers: A (Mostly) Complete Guide to React Rendering Behavior](https://blog.isquaredsoftware.com/2020/05/blogged-answers-a-mostly-complete-guide-to-react-rendering-behavior/#what-is-rendering)