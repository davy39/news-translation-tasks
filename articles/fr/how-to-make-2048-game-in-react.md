---
title: Tutoriel React – Comment construire le jeu 2048 en React
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2021-09-08T01:38:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-2048-game-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/thumb.png
tags:
- name: Game Development
  slug: game-development
- name: React
  slug: react
seo_title: Tutoriel React – Comment construire le jeu 2048 en React
seo_desc: "Today you will learn how to build your own clone of the 2048 game in React.\
  \ \nWhat makes this article unique is that we will focus on creating delightful\
  \ animations. Aside from React, we will use TypeScript and we'll make some CSS transitions\
  \ using LE..."
---

Aujourd'hui, vous allez apprendre à créer votre propre clone du jeu 2048 en React. 

Ce qui rend cet article unique, c'est que nous allons nous concentrer sur la création d'animations délicieuses. En plus de React, nous allons utiliser TypeScript et nous allons créer quelques transitions CSS en utilisant LESS. 

Nous n'allons utiliser que des interfaces React modernes telles que les hooks et l'API Context. 

Cet article contient quelques ressources externes telles que :

* [Jeu 2048 (GitHub Pages)](https://mateuszsokola.github.io/2048-in-react/)
* [Exemples d'animations pour 2048 (GitHub Pages)](https://mateuszsokola.github.io/2048-animation-examples/)
* [Code Source (GitHub)](https://github.com/mateuszsokola/2048-in-react)
* ...et une vidéo YouTube. Il m'a fallu plus d'un mois pour préparer ce tutoriel, alors cela signifierait beaucoup pour moi si vous la regardez, aimez-la et vous abonnez à ma chaîne.

%[https://youtu.be/vI0QArPnkUc]

Merci !

## Règles du jeu 2048

Dans ce jeu, le joueur doit combiner des tuiles contenant les mêmes nombres jusqu'à atteindre le nombre 2048. Les tuiles ne peuvent contenir que des valeurs entières commençant par 2, et qui sont une puissance de deux, comme 2, 4, 8, 16, 32, et ainsi de suite. 

Idéalement, le joueur devrait atteindre la tuile 2048 dans le plus petit nombre d'étapes possible. Le plateau a une dimension de 4 x 4 tuiles, de sorte qu'il peut contenir jusqu'à 16 tuiles. Si le plateau est plein, et qu'il n'y a plus de mouvement possible comme fusionner des tuiles ensemble - la partie est terminée.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/giphy.gif)

En créant ce tutoriel, j'ai pris des raccourcis pour me concentrer sur les mécanismes du jeu et les animations. Qu'ai-je supprimé ?

* Dans notre exemple, le jeu crée toujours une nouvelle tuile avec le nombre 2. Mais dans la version correcte, il devrait générer un nombre aléatoire (soit 2 soit 4 - pour rendre le jeu plus difficile). 
* De plus, nous ne gérerons pas les victoires et les défaites. Vous pouvez continuer à jouer après avoir atteint le nombre 2048, et rien ne se passe lorsque le plateau est insoluble - vous devez cliquer sur le bouton de réinitialisation. 
* J'ai sauté le système de score.

Si vous le souhaitez, vous pouvez implémenter ces fonctionnalités manquantes par vous-même. Il suffit de forker mon dépôt et de l'implémenter sur votre propre configuration.

## Structure du projet

L'application contient les éléments suivants :

* Board (composant) – responsable du rendu des tuiles. Il expose un hook appelé `useBoard`.
* Grid (composant) – rend une grille 4x4.
* Tile (composant) – responsable de toutes les animations liées à la tuile, et du rendu de la tuile elle-même.
* Game (composant) – combine tous les éléments ci-dessus. Il inclut un hook `useGame` qui est responsable de l'application des règles et des contraintes du jeu.

## Comment construire le composant Tile

Nous voulons investir plus de temps dans les animations, alors je vais commencer l'histoire par le composant Tile. En fin de compte, ce composant est responsable de toutes les animations du jeu. 

Il n'y a que deux animations assez simples dans 2048 – la surbrillance des tuiles et leur glissement sur le plateau. Nous pouvons gérer ces animations avec des transitions CSS en déclarant les styles suivants :

```style.less
.tile {
  // ...
  transition-property: transform;
  transition-duration: 100ms;
  transform: scale(1);
}
```

À l'instant actuel, j'ai défini une seule transition qui mettra en surbrillance la tuile lorsqu'elle est créée ou fusionnée. Nous allons la laisser comme ça pour l'instant. 

Considérons comment les métadonnées de la tuile sont censées être structurées, afin que nous puissions les utiliser facilement. J'ai décidé de l'appeler `TileMeta` puisque nous ne voulons pas avoir de conflit de nom avec d'autres entités comme le composant Tile :

```typescript.tsx
type TileMeta = {
  id: number;
  position: [number, number];
  value: number;
  mergeWith?: number;
};
```

* `id` – l'identifiant unique de la tuile. Il est important pour que le DOM React ne ré-affiche pas toutes les tuiles à partir de zéro à chaque changement. Sinon, nous verrions toutes les tuiles mises en surbrillance à chaque action du joueur.
* `position` – la position de la tuile sur le plateau. C'est un tableau avec deux éléments, les coordonnées `x` et `y` (les valeurs possibles sont `0` - `3` dans les deux cas).
* `value` – la valeur de la tuile. Seulement les puissances de deux, en commençant par `2`.
* `mergeWith` – (optionnel) l'id de la tuile qui va absorber la tuile actuelle. Si elle est présente, la tuile doit être fusionnée dans une autre tuile et disparaître.

## Comment créer et fusionner des tuiles

Nous voulons somehow mettre en évidence que la tuile a changé après l'action du joueur. Je pense que la meilleure façon serait de changer l'échelle de la tuile pour indiquer qu'une nouvelle tuile a été créée ou qu'une tuile a été modifiée.

```typescript.tsx
export const Tile = ({ value, position }: Props) => {
  const [scale, setScale] = useState(1);

  const prevValue = usePrevProps<number>(value);

  const isNew = prevCoords === undefined;
  const hasChanged = prevValue !== value;
  const shallAnimate = isNew || hasChanged;

  useEffect(() => {
    if (shallAnimate) {
      setScale(1.1);
      setTimeout(() => setScale(1), 100);
    }
  }, [shallAnimate, scale]);

  const style = {
    transform: `scale(${scale})`,
  };

  return (
    <div className={`tile tile-${value}`} style={style}>
      {value}
    </div>
  );
};

```

Pour déclencher l'animation, nous devons considérer deux cas :

* une nouvelle tuile – la valeur précédente sera `null`. 
* la tuile a changé de valeur – la valeur précédente sera différente de la valeur actuelle. 

Et le résultat est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/giphy--1-.gif)

Vous avez peut-être remarqué que j'utilise un hook personnalisé appelé `usePrevProps`. Il aide à suivre les valeurs précédentes des propriétés du composant (props). 

J'aurais pu utiliser des références pour récupérer les valeurs précédentes, mais cela aurait encombré mon composant. J'ai décidé de l'extraire dans un hook autonome, afin que le code soit lisible et que je puisse utiliser ce hook à d'autres endroits.

Si vous souhaitez l'utiliser dans votre projet, copiez simplement ce snippet :

```typescript.ts
import { useEffect, useRef } from "react";

/**
 * `usePrevProps` stocke la valeur précédente de la prop.
 *
 * @param {K} value
 * @returns {K | undefined}
 */
export const usePrevProps = <K = any>(value: K) => {
  const ref = useRef<K>();

  useEffect(() => {
    ref.current = value;
  });

  return ref.current;
};

```

## Comment faire glisser les tuiles sur le plateau

Le jeu aura l'air saccadé sans l'animation de glissement des tuiles sur le plateau. Nous pouvons facilement créer cette animation en utilisant des transitions CSS. 

Le plus pratique sera d'utiliser les propriétés responsables du positionnement, telles que `left` et `top`. Nous devons donc modifier nos styles CSS pour qu'ils ressemblent à ceci :

```style.less
.tile {
  position: absolute;
  // ...
  transition-property: left, top, transform;
  transition-duration: 250ms, 250ms, 100ms;
  transform: scale(1);
}
```

Une fois que nous avons déclaré les styles, nous pouvons implémenter la logique responsable du changement de position d'une tuile sur le plateau.

```typescript.tsx
export const Tile = ({ value, position, zIndex }: Props) => {
  const [boardWidthInPixels, tileCount] = useBoard();
  // ...

  useEffect(() => {
    // ...
  }, [shallAnimate, scale]);

  const positionToPixels = (position: number) => {
    return (position / tileCount) * (boardWidthInPixels as number);
  };

  const style = {
    top: positionToPixels(position[1]),
    left: positionToPixels(position[0]),
    transform: `scale(${scale})`,
    zIndex,
  };

  // ...
};

```

Comme vous pouvez le voir, l'équation dans la fonction `positionToPixels` doit connaître la position de la tuile, le nombre total de tuiles par ligne et colonne, et la longueur totale du plateau en pixels (largeur ou hauteur – même chose, c'est un carré). La valeur calculée est transmise à l'élément HTML en tant que style en ligne.

Attendez une minute... mais qu'en est-il du hook `useBoard` et de la propriété `zIndex` ? 

* `useBoard` nous permet d'accéder aux propriétés du plateau dans les composants enfants sans les transmettre. Le composant Tile doit connaître la largeur et le nombre total de tuiles pour trouver le bon emplacement sur le plateau. Grâce à l'API Context de React, nous pouvons partager des propriétés à travers plusieurs couches de composants sans polluer leurs propriétés (props).
* `zIndex` est une propriété CSS qui définit l'ordre des tuiles dans la pile. Dans notre cas, c'est l'id de la tuile. Comme vous pouvez le voir sur le gif ci-dessous, les tuiles peuvent être empilées les unes sur les autres, donc le `zIndex` nous permet de spécifier celle qui sera au-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/a.gif)

## Comment construire le plateau

Une autre partie importante du jeu est le plateau. Le composant Board est responsable du rendu de la grille et des tuiles. 

Il semble que le plateau ait une logique métier dupliquée avec le composant Tile, mais il y a une petite différence. Le plateau contient des informations sur sa taille (largeur et hauteur), et le nombre de colonnes et de lignes. C'est l'inverse de la tuile qui ne connaît que sa propre position.  

```typescript.tsx
type Props = {
  tiles: TileMeta[];
  tileCountPerRow: number;
};

const Board = ({ tiles, tileCountPerRow = 4 }: Props) => {
  const containerWidth = tileTotalWidth * tileCountPerRow;
  const boardWidth = containerWidth + boardMargin;

  const tileList = tiles.map(({ id, ...restProps }) => (
    <Tile key={`tile-${id}`} {...restProps} zIndex={id} />
  ));

  return (
    <div className="board" style={{ width: boardWidth }}>
      <BoardProvider containerWidth={containerWidth} tileCountPerRow={tileCountPerRow}>
        <div className="tile-container">{tileList}</div>
        <Grid />
      </BoardProvider>
    </div>
  );
};

```

Le composant Board utilise le `BoardProvider` pour distribuer la largeur du conteneur de tuiles et le nombre de tuiles par ligne et colonne à toutes les tuiles et au composant de grille. 

```typescript.tsx
const BoardContext = React.createContext({
  containerWidth: 0,
  tileCountPerRow: 4,
});

type Props = {
  containerWidth: number;
  tileCountPerRow: number;
  children: any;
};

const BoardProvider = ({
  children,
  containerWidth = 0,
  tileCountPerRow = 4,
}: Props) => {
  return (
    <BoardContext.Provider value={{ containerWidth, tileCountPerRow }}>
      {children}
    </BoardContext.Provider>
  );
};

```

Le `BoardProvider` utilise l'API Context de React pour propager les propriétés vers chaque enfant. Si un composant doit utiliser une valeur disponible sur le fournisseur, il peut la récupérer en appelant le hook `useBoard`. 

Je vais sauter ce sujet puisque j'en ai parlé plus en détail dans ma [vidéo sur les Feature Toggles dans React](https://youtu.be/H9Tx5SqWX9o). Si vous souhaitez en apprendre davantage, vous pouvez la regarder.

```typescript.tsx
const useBoard = () => {
  const { containerWidth, tileCount } = useContext(BoardContext);

  return [containerWidth, tileCount] as [number, number];
};

```

## Comment construire le composant Game

Maintenant, nous pouvons spécifier les règles du jeu et exposer l'interface pour jouer au jeu. Je vais commencer par la navigation puisque cela vous aidera à comprendre pourquoi la logique du jeu est implémentée de cette manière. 

```typescript.tsx
import { useThrottledCallback } from "use-debounce";

const Game = () => {
  const [tiles, moveLeft, moveRight, moveUp, moveDown] = useGame();

  const handleKeyDown = (e: KeyboardEvent) => {
  	// désactive le défilement de la page avec les flèches du clavier
    e.preventDefault();
  
    switch (e.code) {
      case "ArrowLeft":
        moveLeft();
        break;
      case "ArrowRight":
        moveRight();
        break;
      case "ArrowUp":
        moveUp();
        break;
      case "ArrowDown":
        moveDown();
        break;
    }
  };

  // protège le réducteur contre une inondation d'événements.
  const throttledHandleKeyDown = useThrottledCallback(
    handleKeyDown,
    animationDuration,
    { leading: true, trailing: false }
  );

  useEffect(() => {
    window.addEventListener("keydown", throttledHandleKeyDown);

    return () => {
      window.removeEventListener("keydown", throttledHandleKeyDown);
    };
  }, [throttledHandleKeyDown]);

  return <Board tiles={tiles} tileCountPerRow={4} />;
};
```

Comme vous pouvez le voir, la logique du jeu sera gérée par le hook `useGame` qui expose les propriétés et méthodes suivantes :

* `tiles` – un tableau de tuiles disponibles sur le plateau. Il utilise le type `TileMeta` décrit ci-dessus.
* `moveLeft` – une fonction qui fait glisser toutes les tuiles vers le côté gauche du plateau.
* `moveRight` – une fonction qui fait glisser toutes les tuiles vers le côté droit du plateau.
* `moveUp` – une fonction qui fait glisser toutes les tuiles vers le haut du plateau.
* `moveDown` – une fonction qui fait glisser toutes les tuiles vers le bas du plateau.

Nous utilisons le callback `throttledHandleKeyDown` pour empêcher les joueurs d'inonder le jeu avec des tonnes de mouvements en même temps. En gros, le joueur doit attendre que l'animation soit terminée avant de pouvoir déclencher un autre mouvement. 

Ce mécanisme est appelé throttling. J'ai décidé d'utiliser le hook `useThrottledCallback` du package `use-debounce`. 

## Comment utiliser le hook useGame

J'ai mentionné ci-dessus que le composant Game gérera également les règles du jeu. Nous allons extraire la logique du jeu dans un hook plutôt que de l'écrire directement sur le composant (puisque nous ne voulons pas encombrer le code).

Le hook useGame est basé sur le hook `useReducer` qui est un hook intégré dans React. Je vais commencer par définir la forme de l'état du réducteur. 

```typescript.tsx
type TileMap = { 
  [id: number]: TileMeta;
}

type State = {
  tiles: TileMap;
  inMotion: boolean;
  hasChanged: boolean;
  byIds: number[];
};

```

L'état contient les champs suivants :

* `tiles` – une table de hachage responsable du stockage des tuiles. La table de hachage facilite la recherche d'entrées par leurs clés, donc c'est un parfait pour nous puisque nous voulons trouver des tuiles par leurs ids.
* `byIds` – un tableau contenant tous les ids dans l'ordre attendu (c'est-à-dire, ascendant). Nous devons garder le bon ordre des tuiles, afin que React ne ré-affiche pas tout le plateau à chaque fois que nous changeons l'état.
* `hasChange` – suit les changements de tuiles. Si rien n'a changé, la nouvelle tuile ne sera pas générée.
* `inMotion` – détermine si les tuiles sont encore en mouvement. Si elles le sont, la nouvelle tuile ne sera pas générée jusqu'à ce que le mouvement soit terminé.

### Actions

`useReducer` nécessite de spécifier les actions qui sont prises en charge par ce réducteur. 

```typescript.tsx
type Action =
  | { type: "CREATE_TILE"; tile: TileMeta }
  | { type: "UPDATE_TILE"; tile: TileMeta }
  | { type: "MERGE_TILE"; source: TileMeta; destination: TileMeta }
  | { type: "START_MOVE" }
  | { type: "END_MOVE" };
```

À quoi servent ces actions ?

* `CREATE_TILE` – crée une nouvelle tuile et l'ajoute à la table de hachage `tiles`. Elle change le drapeau `hasChange` en `false` puisque cette action est toujours déclenchée lorsqu'une nouvelle tuile est ajoutée au plateau. 
* `UPDATE_TILE` – met à jour une tuile existante. Elle ne modifie pas l'id, ce qui est important pour garder les animations fonctionnelles. Nous l'utiliserons pour repositionner la tuile et changer sa valeur (pendant les fusions). De plus, elle change le drapeau `hasChange` en `true`.
* `MERGE_TILE` – fusionne une tuile source dans une tuile de destination. Après cette opération, la tuile de destination changera sa valeur (la valeur de la tuile source sera ajoutée à celle-ci). Et elle supprimera la tuile source de la table `tiles` et du tableau `byIds`.
* `START_MOVE` – indique au réducteur qu'il doit s'attendre à plusieurs actions, donc il doit attendre que toutes les animations soient terminées avant de pouvoir générer une nouvelle tuile.
* `END_MOVE` – indique au réducteur que toutes les actions ont été terminées et qu'il peut créer une nouvelle tuile en toute sécurité.

Si vous le souhaitez, vous pouvez écrire la logique de ce réducteur par vous-même ou copier la mienne :

```typescript.tsx
type TileMap = { 
  [id: number]: TileMeta;
}

type State = {
  tiles: TileMap;
  inMotion: boolean;
  hasChanged: boolean;
  byIds: number[];
};

type Action =
  | { type: "CREATE_TILE"; tile: TileMeta }
  | { type: "UPDATE_TILE"; tile: TileMeta }
  | { type: "MERGE_TILE"; source: TileMeta; destination: TileMeta }
  | { type: "START_MOVE" }
  | { type: "END_MOVE" };

const initialState: State = {
  tiles: {},
  byIds: [],
  hasChanged: false,
  inMotion: false,
};

const GameReducer = (state: State, action: Action) => {
  switch (action.type) {
    case "CREATE_TILE":
      return {
        ...state,
        tiles: {
          ...state.tiles,
          [action.tile.id]: action.tile,
        },
        byIds: [...state.byIds, action.tile.id],
        hasChanged: false,
      };
    case "UPDATE_TILE":
      return {
        ...state,
        tiles: {
          ...state.tiles,
          [action.tile.id]: action.tile,
        },
        hasChanged: true,
      };
    case "MERGE_TILE":
      const {
        [action.source.id]: source,
        [action.destination.id]: destination,
        ...restTiles
      } = state.tiles;
      return {
        ...state,
        tiles: {
          ...restTiles,
          [action.destination.id]: {
            id: action.destination.id,
            value: action.source.value + action.destination.value,
            position: action.destination.position,
          },
        },
        byIds: state.byIds.filter((id) => id !== action.source.id),
        hasChanged: true,
      };
    case "START_MOVE":
      return {
        ...state,
        inMotion: true,
      };
    case "END_MOVE":
      return {
        ...state,
        inMotion: false,
      };
    default:
      return state;
  }
};

```

Si vous ne comprenez pas pourquoi nous avons défini ces actions, ne vous inquiétez pas – maintenant nous allons implémenter un hook qui, je l'espère, éclaircira cela.

### Comment implémenter le hook

Examinons la fonction qui est responsable des mouvements du joueur. Nous allons nous concentrer uniquement sur le mouvement vers la gauche, car les autres sont presque identiques.

```typescript.tsx
  const moveLeftFactory = () => {
    const retrieveTileIdsByRow = (rowIndex: number) => {
      const tileMap = retrieveTileMap();

      const tileIdsInRow = [
        tileMap[tileIndex * tileCount + 0],
        tileMap[tileIndex * tileCount + 1],
        tileMap[tileIndex * tileCount + 2],
        tileMap[tileIndex * tileCount + 3],
      ];

      const nonEmptyTiles = tileIdsInRow.filter((id) => id !== 0);
      return nonEmptyTiles;
    };

    const calculateFirstFreeIndex = (
      tileIndex: number,
      tileInRowIndex: number,
      mergedCount: number,
      _: number
    ) => {
      return tileIndex * tileCount + tileInRowIndex - mergedCount;
    };

    return move.bind(this, retrieveTileIdsByRow, calculateFirstFreeIndex);
  };
  
  const moveLeft = moveLeftFactory();
```

Comme vous pouvez le voir, j'ai décidé de lier deux callbacks à la fonction `move`. Cette technique est appelée l'inversion de contrôle – afin que le consommateur de la fonction puisse injecter ses propres valeurs dans la fonction exécutée. 

Si vous ne savez pas comment fonctionne `bind`, vous devriez apprendre à ce sujet car c'est une question très courante lors des entretiens d'embauche. 

Le premier callback appelé `retrieveTileIdsByRow` est responsable de la recherche de toutes les tuiles non vides disponibles dans une ligne (pour les mouvements horizontaux – gauche ou droite). Si le joueur effectue des mouvements verticaux (haut ou bas), nous chercherons toutes les tuiles dans une colonne.

Le deuxième callback appelé `calculateFirstFreeIndex` trouve la position la plus proche de la bordure du plateau en fonction des paramètres donnés tels que l'index de la tuile, l'index de la tuile dans la ligne ou la colonne, le nombre de tuiles fusionnées et l'index maximum possible. 

Maintenant, nous allons examiner la logique métier de la fonction `move`. J'ai expliqué le code de cette fonction dans les commentaires. L'algorithme peut être un peu complexe, et je crois qu'il sera plus facile à comprendre si je documente le code ligne par ligne :

```typescript.tsx
  type RetrieveTileIdsByRowOrColumnCallback = (tileIndex: number) => number[];

  type CalculateTileIndex = (
    tileIndex: number,
    tileInRowIndex: number,
    mergedCount: number,
    maxIndexInRow: number
  ) => number;

  const move = (
    retrieveTileIdsByRowOrColumn: RetrieveTileIdsByRowOrColumnCallback,
    calculateFirstFreeIndex: CalculateTileIndex
  ) => {
    // les nouvelles tuiles ne peuvent pas être créées pendant le mouvement.
    dispatch({ type: "START_MOVE" });

    const maxIndex = tileCount - 1;

    // itère à travers chaque ligne ou colonne (dépend du type de mouvement - vertical ou horizontal).
    for (let tileIndex = 0; tileIndex < tileCount; tileIndex += 1) {
      // récupère les tuiles dans la ligne ou la colonne.
      const availableTileIds = retrieveTileIdsByRowOrColumn(tileIndex);

      // previousTile est utilisé pour déterminer si la tuile peut être fusionnée avec la tuile actuelle.
      let previousTile: TileMeta | undefined;
      // mergeCount aide à remplir les écarts créés par les fusions de tuiles - deux tuiles deviennent une.
      let mergedTilesCount = 0;

      // itère à travers les tuiles disponibles.
      availableTileIds.forEach((tileId, nonEmptyTileIndex) => {
        const currentTile = tiles[tileId];

        // si la tuile précédente a la même valeur que la tuile actuelle, elles doivent être fusionnées ensemble.
        if (
          previousTile !== undefined &&
          previousTile.value === currentTile.value
        ) {
          const tile = {
            ...currentTile,
            position: previousTile.position,
            mergeWith: previousTile.id,
          } as TileMeta;

          // retarde la fusion de 250ms, afin que l'animation de glissement puisse être complétée.
          throttledMergeTile(tile, previousTile);
          // la tuile précédente doit être effacée car une seule tuile peut être fusionnée une seule fois par mouvement.
          previousTile = undefined;
          // incrémente le compteur de fusions pour corriger la position des tuiles consécutives afin d'éliminer les écarts
          mergedTilesCount += 1;

          return updateTile(tile);
        }

        // sinon - les tuiles précédentes et actuelles sont différentes - déplace la tuile vers le premier espace libre.
        const tile = {
          ...currentTile,
          position: indexToPosition(
            calculateFirstFreeIndex(
              tileIndex,
              nonEmptyTileIndex,
              mergedTilesCount,
              maxIndex
            )
          ),
        } as TileMeta;

        // la tuile précédente devient la tuile actuelle pour vérifier si la tuile suivante peut être fusionnée avec celle-ci.
        previousTile = tile;

        // seulement si la tuile a changé de position, elle sera mise à jour
        if (didTileMove(currentTile, tile)) {
          return updateTile(tile);
        }
      });
    }

    // attend jusqu'à la fin de toutes les animations.
    setTimeout(() => dispatch({ type: "END_MOVE" }), animationDuration);
  };
```

Le code complet de ce hook compte plus de 400 lignes de code, alors au lieu de le coller ici, j'ai décidé de le garder sur GitHub – alors s'il vous plaît [consultez le code complet là-bas](https://github.com/mateuszsokola/2048-in-react/blob/master/src/components/Game/hooks/useGame/useGame.ts).

## Devoirs

J'ai mentionné ci-dessus que quelques fonctionnalités sont manquantes. Si vous voulez comprendre le code en profondeur, vous pourriez forker mon dépôt et implémenter les fonctionnalités suivantes :

* score – vous pouvez définir votre propre algorithme.
* prise en charge des victoires et des défaites.
* pour la génération de nouvelles tuiles, choisissez une valeur de tuile aléatoire - soit 2 soit 4. Le 4 ne devrait pas apparaître moins de 5% du temps.

Si vous voulez que je passe en revue votre code, vous pouvez m'inviter à votre pull request sur GitHub - mon nom d'utilisateur est mateuszsokola. Peut-être que je ferai une vidéo sur la façon dont je passe en revue votre code.

## Résumé 

J'espère que vous avez apprécié mon tutoriel. Cette fois, j'ai décidé de me concentrer sur l'essence du sujet plutôt que sur la construction de React et CSS de base, donc j'ai sauté ces parties de base. Je crois que cela rend cet article plus facile à digérer. 

Des commentaires ou des questions ? [Criez-moi sur Twitter](https://twitter.com/msokola) !

Si vous avez trouvé cet article utile, veuillez le partager, afin que plus de développeurs puissent en apprendre. Occasionnellement, je [publie des vidéos sur ma chaîne YouTube](https://www.youtube.com/channel/UCJV16_5c4A0amyBZSI4yP6A), et ce serait génial si vous vous abonnez à ma chaîne, aimez la vidéo et laissez un commentaire sous votre vidéo préférée.

Restez à l'écoute !