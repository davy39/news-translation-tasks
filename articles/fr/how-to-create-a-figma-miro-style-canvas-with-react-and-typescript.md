---
title: Comment créer une toile de style Figma / Miro avec React et TypeScript
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2024-03-16T12:59:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-figma-miro-style-canvas-with-react-and-typescript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727437264136/a99a5516-2b24-40b2-a22f-973b28043f07.png
tags:
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Comment créer une toile de style Figma / Miro avec React et TypeScript
seo_desc: 'Miro and Figma are online collaborative canvas type tools that became very
  popular during the pandemic.

  Instead of sticking post it notes on a physical wall, you can now add virtual post
  its (and a dizzying array of other things) to a virtual canvas....'
---

Miro et Figma sont des outils de toile collaborative en ligne qui sont devenus très populaires pendant la pandémie.

Au lieu de coller des post-it sur un mur physique, vous pouvez maintenant ajouter des post-it virtuels (et une multitude d'autres choses) à une toile virtuelle. Cela permet aux équipes de collaborer virtuellement de manière familière comme dans le monde physique.

Figma et Miro sont des produits matures et volumineux, et ils contournent entièrement HTML et CSS. Ils utilisent des technologies comme WebAssembly, WebGL, C++ et similaires, en raison de leurs exigences de performance extrêmement élevées.

Mais nous pouvons créer des fonctionnalités similaires de type toile virtuelle, sans la complexité, en utilisant React, TypeScript et quelques packages. Nous allons prendre en charge un type de "carte", qui contiendra simplement du texte, pour garder ce guide concis, mais il est facile d'étendre la solution pour prendre en charge des cas d'utilisation plus élaborés.

Les fonctionnalités que nous allons implémenter sont :

* Faire glisser les cartes sur la toile
  
* Ajouter de nouvelles cartes à la toile
  
* Faire défiler et zoomer sur la toile
  

Cet article est un guide étape par étape décrivant comment créer ces fonctionnalités, et il y a un code compagnon sur GitHub avec des démonstrations en direct.

Notre solution construite à partir de zéro ne sera pas aussi rapide que Figma ou Miro, mais si vos besoins sont plus simples, elle sera probablement suffisante.

## Aperçu du projet

Nous utiliserons [DndKit](https://dndkit.com/) pour le glisser-déposer et [D3 Zoom](https://github.com/d3/d3-zoom) pour le défilement et le zoom. J'ai trouvé ces deux outils très agréables à utiliser.

Le [code est sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-3), et il y a une [démonstration en direct](https://ceddlyburge.github.io/react-figma-miro-canvas-part-3/) pour que vous puissiez l'essayer.

Il n'y a que 4 composants (`App`, `Canvas`, `Draggable` et `Addable`), et seulement environ 250 lignes de code.

Ce guide est destiné aux développeurs React / TypeScript de niveau intermédiaire. Il sera beaucoup plus facile si vous comprenez déjà les [composants](https://react.dev/learn/your-first-component#defining-a-component), les [hooks](https://react.dev/blog/2023/03/16/introducing-react-dev#going-all-in-on-modern-react-with-hooks), [comment penser en React](https://react.dev/learn/thinking-in-react), l'[état](https://react.dev/reference/react/useState), les [refs mutables](https://react.dev/reference/react/useRef) et des choses comme ça.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/part-3.gif align="left")

*Capture d'écran montrant la solution finale de la toile*

D'accord, maintenant pour voir comment vous pouvez réellement construire cela, plongeons-nous dedans.

## **Étape 1 – Comment faire glisser les cartes sur la toile**

Pour commencer, nous utiliserons [DndKit](https://dndkit.com/) pour faire glisser les cartes sur une toile. Nous installerons les outils nécessaires pour construire le projet, créerons un simple type `Card`, et créerons des composants `App`, `Canvas` et `Draggable` simples.

Le composant `App` stocke l'état `card` et rend le `Canvas`.

Le composant `Canvas` s'intègre avec DndKit, met à jour l'état `card` et rend les `cards` en tant que composants `Draggable`.

Le composant `Draggable` s'intègre avec DndKit et utilise le style CSS pour se positionner correctement sur la toile.

[Code de l'étape 1 sur GitHub.](https://github.com/ceddlyburge/react-figma-miro-canvas-part-1)

Voici une capture d'écran de ce que nous allons construire dans cette partie, et il y a aussi une [démonstration en direct](https://ceddlyburge.github.io/react-figma-miro-canvas-part-1/) que vous pouvez essayer vous-même :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/part-1.gif align="left")

*Capture d'écran montrant la partie 1 de la solution de la toile*

### Configuration du projet

Nous créons un nouveau projet avec Vite et installons DndKit en utilisant les commandes suivantes :

```bash
npm create vite@latest figma-miro-canvas -- --template react-ts
npm install
npm install @dnd-kit/core
```

### **App.tsx**

Le composant `App` stocke l'état `card` et rend le `Canvas`.

Nous ajoutons un type `Card`, dans cette démonstration, les cartes contiendront simplement du texte. `UniqueIdentifier` provient de DndKit et semble effrayant, mais ce n'est qu'un `String | number`. `Coordinates` provient également de DndKit et contient les positions x et y.

```tsx
export type Card = {  
  id: UniqueIdentifier;
  coordinates: Coordinates;
  text: string;
};
```

Nous devons ensuite créer quelques cartes et les passer à la toile.

```tsx
export const App = () => {
  const [cards, setCards] = useState<Card[]>([
    { id: "Hello", coordinates: { x: 0, y: 0 }, text: "Hello" },
  ]);
  
  return (<Canvas cards={cards} />);
}
```

[App.tsx sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-1/blob/main/src/App.tsx)

### **Canvas.tsx**

Le composant `Canvas` s'intègre avec DndKit, met à jour l'état `card` et rend les `cards` en tant que composants `Draggable`.

Il prend `cards` et `setCards` en tant que props, car l'état est stocké plus haut dans l'arborescence dans `App`. Ce n'est pas strictement nécessaire pour l'instant, mais cela sera utile dans les étapes ultérieures.

```tsx
type Props = {
  cards: Card[];
  setCards: (cards: Card[]) => void;
}
```

Nous ajoutons une fonction pour appeler `setCards` avec une mise à jour après qu'une opération de glisser-déposer a été complétée. Cela ajoute simplement la distance de glisser / delta aux valeurs x et y pour la carte qui était en train d'être glissée.

L'événement `DragEndEvent` provient de DndKit et inclut l'élément `active` en cours de glisser, nous pouvons donc l'utiliser pour déterminer quelle `card` mettre à jour.

```tsx
const updateDraggedCardPosition = ({ delta, active }: DragEndEvent) => {
  if (!delta.x && !delta.y) return;

  setCards(
    cards.map((card) => {
      if (card.id === active.id) {
        return {
          ...card,
          coordinates: {
            x: card.coordinates.x + delta.x,
            y: card.coordinates.y + delta.y,
          },
        };
      }
      return card;
    })
  );
};
```

Nous ajoutons une `div` pour représenter la toile, un `DndContext` (de DndKit), et rendons un `Draggable` pour chaque carte. Nous connectons notre nouvelle fonction avec l'événement `onDragEnd` de `DndContext` afin que l'état `card` soit mis à jour après une opération de glisser-déposer réussie.

```tsx
<div className="canvas">
  <DndContext onDragEnd={updateDraggedCardPosition}>
    {cards.map((card) => (
      <Draggable card={card} key={card.id} />
    ))}
  </DndContext>
</div>
```

[Canvas.tsx sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-1/blob/main/src/Canvas.tsx)

### **Draggable.tsx**

Le composant `Draggable` s'intègre avec DndKit et utilise le style CSS (`position`, `top` et `left`) pour se positionner correctement sur la toile.

`useDraggable` provient de DndKit, et nous passons aveuglément les `attributes`, `listeners` et `setNodeRef` qu'il retourne à notre `div`, ce qui lui permet de répondre aux événements `onClick` et similaires.

Nous utilisons également le `transform` de DndKit pour appliquer le CSS afin de rendre la carte à une position modifiée lorsqu'un glisser est en cours. Un peu confusément, le nom de la propriété CSS est également appelé `transform`.

```tsx
export const Draggable = ({ card }: { card: Card }) => {
  // hook up to DndKit
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: card.id,
  });

  return (
    <div
      className="card"
      style={{
        // position card on canvas
        position: "absolute",
        top: `${card.coordinates.y}px`,
        left: `${card.coordinates.x}px`,
        // temporary change to this position when dragging
        ...(transform
          ? {
              transform: `translate3d(${transform.x}px, ${transform.y}px, 0px)`,
            }
          : {}),
      }}
      ref={setNodeRef}
      {...listeners}
      {...attributes}
    >
      {card.text}
    </div>
  );
};
```

[Draggable.tsx sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-1/blob/main/src/Draggable.tsx)

### **App.css**

Enfin, nous pouvons ajouter un peu de style CSS pour que tout ait l'air vaguement acceptable. Ce n'est pas strictement nécessaire, mais cela a l'air beaucoup mieux, même avec mes compétences limitées en design.

[App.css sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-1/blob/main/src/App.css)

## **Étape 2 – Comment ajouter de nouvelles cartes à la toile**

Dans cette étape, nous allons créer un nouveau composant `Addable`, pour représenter les cartes qui ne sont pas actuellement sur la toile, mais qui peuvent être glissées dessus.

Nous allons mettre à jour `App` pour ajouter une `div` "tray" pour contenir ces nouvelles cartes `Addable`. Nous allons également ajouter *un autre* DndContext (ce nouveau `DndContext` gérera le glisser-déposer du plateau à la toile, et le `DndContext` existant dans `Canvas` gère le glisser des cartes sur la toile), et nous connecter à ses événements. Cela nous permettra de mettre à jour l'état lorsque les cartes `Addable` sont glissées / déposées sur la toile.

Nous allons mettre à jour `Canvas` pour en faire une cible de dépôt DndKit, afin que les cartes `Addable` puissent être déposées dessus.

[Code de l'étape 2 sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-2)

Voici les fonctionnalités que nous allons ajouter dans cette section, et il y a aussi une [démonstration en direct](https://ceddlyburge.github.io/react-figma-miro-canvas-part-1/) que vous pouvez essayer vous-même :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/part-2.gif align="left")

### **App.tsx**

Le composant `App` a maintenant besoin d'une `div` "tray" pour contenir les cartes `Addable`.

Il a également besoin d'*un autre* DndContext (ce nouveau `DndContext` gérera le glisser-déposer du plateau à la toile, et le `DndContext` existant dans `Canvas` gère le glisser des cartes sur la toile). Il doit se connecter à ses événements afin que nous puissions mettre à jour l'état lorsque les cartes `Addable` sont glissées / déposées sur la toile.

Nous ajoutons une liste de cartes à afficher sur le plateau :

```tsx
const trayCards = [
  // les coordonnées ne sont pas utilisées pour les cartes du plateau, nous pourrions créer un nouveau type sans elles
  { id: "World", coordinates: { x: 0, y: 0 }, text: "World" },
];
```

Nous ajoutons une fonction pour calculer la position sur la toile à la fin d'une opération de glisser-déposer. Cela doit connaître la position initiale de la carte, la distance de glisser / delta, et la position en haut à gauche de la toile. Ces détails sont tous fournis par l'événement `DragEndEvent` de DndKit.

```tsx
const calculateCanvasPosition = (
  initialRect: ClientRect,
  over: Over,
  delta: Translate
): Coordinates => ({
  x: initialRect.left + delta.x - (over?.rect?.left ?? 0),
  y: initialRect.top + delta.y - (over?.rect?.top ?? 0),
});
```

Nous ajoutons un état pour stocker la carte du plateau en cours de glisser, ainsi qu'une fonction pour mettre à jour l'état `cards` après un glisser / dépôt depuis le plateau. L'événement `DragEndEvent` provient de DndKit et inclut l'élément `active` en cours de glisser, nous pouvons donc l'utiliser pour créer une nouvelle `card` et l'ajouter au tableau `cards`. Nous effectuons également quelques vérifications pour nous assurer que la "toile" est la cible de dépôt et que nous avons toutes les données nécessaires.

```tsx
const [draggedTrayCardId, setDraggedTrayCardId] = useState<UniqueIdentifier | null>(null);

const addDraggedTrayCardToCanvas = ({ over, active, delta }: DragEndEvent) => {
  setDraggedTrayCardId(null);

  if (over?.id !== "canvas") return;
  if (!active.rect.current.initial) return;

  setCards([
    ...cards,
    {
      id: active.id,
      coordinates: calculateCanvasPosition(
        active.rect.current.initial,
        over,
        delta
      ),
      text: active.id.toString(),
    },
  ]);
};
```

Nous ajoutons le nouveau `DndContext` supplémentaire, une `div` pour représenter le plateau, et un `DragOverlay`.

Le composant `DragOverlay` provient de DndKit, et nous rendons la carte du plateau en cours de glisser à l'intérieur. Il fait le travail difficile de montrer la carte du plateau pendant qu'elle est glissée. Il est très pratique à utiliser avec le glisser-déposer, mais moins pratique lorsque l'on glisse simplement, ce qui explique pourquoi nous n'en avons pas utilisé un plus tôt lorsque nous glissions des cartes sur la toile.

```tsx
<DndContext
  onDragStart={({ active }) => setDraggedTrayCardId(active.id)} 
  onDragEnd={addDraggedTrayCardToCanvas} 
>
  <div className="tray">
    {trayCards.map((trayCard) => {
      // cette ligne supprime la carte du plateau si elle est sur la toile
      if (cards.find((card) => card.id === trayCard.id)) return null;

      return <Addable card={trayCard} key={trayCard.id} />;
    })}
  </div>
  <Canvas cards={cards} setCards={setCards} />
  <DragOverlay>
    {/* cela fonctionne parce que l'id de la carte est le même que le texte dans cet exemple, donc nous pouvons simplement rendre l'id à l'intérieur d'une div. Dans des cas plus complexes, vous auriez un composant pour rendre la carte, et l'utiliser ici. */}
    <div className="trayOverlayCard">{draggedTrayCardId}</div>
  </DragOverlay>
</DndContext>
```

[App.tsx sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-2/blob/main/src/App.tsx)

### **Addable.tsx**

Le composant `Addable` s'intègre avec DndKit et est utilisé pour représenter les cartes qui ne sont pas actuellement sur la toile, mais qui peuvent être glissées dessus.

Nous connectons le composant avec DndKit et rendons le texte de la carte dans une `div`. `useDraggable` provient de DndKit, et nous passons aveuglément les `attributes`, `listeners` et `setNodeRef` qu'il retourne à notre `div`. Cela lui permet de répondre aux événements `onClick` et similaires.

```tsx
export const Addable = ({
   card
} : {
  card: Card;
}) => {
  const { attributes, listeners, setNodeRef } = useDraggable({
    card.id,
  });

  return (
    <div 
      className="trayCard"
      ref={setNodeRef}
      {...listeners}
      {...attributes}>
      {card.text}
    </div>
  );
};
```

[Addable.tsx sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-2/blob/main/src/Addable.tsx)

### **Canvas.tsx**

`Canvas` doit maintenant s'intégrer avec DndKit pour en faire une cible de dépôt, afin que les cartes `Addable` puissent être déposées dessus.

Nous connectons la toile en tant que cible de dépôt avec DndKit. `useDroppable` provient de DndKit, et nous passons simplement la référence à notre `div`. Cela permet à DndKit de l'identifier et d'obtenir son `id` lorsqu'elle est survolée.

```tsx
const { setNodeRef } = useDroppable({ id: "canvas" });
```

```tsx
<div
  className="canvas"
  ref={setNodeRef}
  ...
>
  ...
</div>
```

[Canvas.tsx sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-2/blob/main/src/Canvas.tsx)

## **Étape 3 - Comment faire défiler et zoomer sur la toile**

Dans cette dernière étape, nous allons installer d3-zoom, le connecter à la toile, puis mettre à jour certains calculs et styles afin que tout apparaisse au bon endroit.

Nous allons mettre à jour `App`, pour stocker le `transform` (le défilement et le zoom de la toile) de d3-zoom, et mettre à jour le style du `DragOverlay` et `calculateCanvasPosition` pour tenir compte du `transform`.

Nous allons mettre à jour `Canvas` pour l'intégrer avec d3-zoom et utiliser le style CSS pour tenir compte du `transform`.

Nous allons mettre à jour `Draggable`, en utilisant le style CSS pour tenir compte du `transform`, à la fois lorsqu'il est stationnaire et pendant qu'il est glissé.

d3-zoom gère les événements de souris et de pointeur pour le défilement et le zoom automatiquement, donc nous n'avons pas besoin d'ajouter de code pour cela (mais il est facile de le faire si vous voulez ajouter un bouton "Zoom In" ou similaire).

[Code de l'étape 3 sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-3)

Voici ce que nous allons construire dans cette section, et il y a aussi une [démonstration en direct](https://ceddlyburge.github.io/react-figma-miro-canvas-part-3/) que vous pouvez essayer vous-même :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/part-3-1.gif align="left")

Avant de continuer, assurez-vous d'avoir installé d3-zoom :

```bash
npm install d3-zoom
npm install --save-dev @types/d3-zoom
```

### **App.tsx**

`App` doit maintenant stocker le `transform` (le défilement et le zoom de la toile) de d3-zoom et mettre à jour le style du `DragOverlay` et `calculateCanvasPosition` pour tenir compte du `transform`.

Nous stockons le `transform` actuel de d3-zoom. Cela représente à la fois le défilement (`transform.x` et `transform.y`) et le zoom (`transform.k`).

```tsx
const [transform, setTransform] = useState(zoomIdentity);
```

Nous ajoutons du CSS au `DragOverlay`, afin que les cartes glissées depuis le plateau soient de la même taille que sur la toile.

```tsx
style={{
  transformOrigin: "top left",
  transform: `scale(${transform.k})`,
}}
```

Nous mettons à jour la fonction calculateCanvasPosition car elle doit maintenant tenir compte du zoom de la toile (`transform.k`) ainsi que de la position en haut à gauche.

```tsx
const calculateCanvasPosition = (
  initialRect: ClientRect,
  over: Over,
  delta: Translate,
  transform: ZoomTransform
): Coordinates => ({
  x: (initialRect.left + delta.x - (over?.rect?.left ?? 0) - transform.x) / transform.k,
  y: (initialRect.top + delta.y - (over?.rect?.top ?? 0) - transform.y) / transform.k,
});
```

[App.tsx sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-3/blob/main/src/App.tsx)

### **Canvas.tsx**

`Canvas` doit maintenant s'intégrer avec d3-zoom et utiliser le style CSS pour tenir compte du `transform` de d3-zoom.

Nous ajoutons des props pour `transform` et `setTransform` (nous les passons depuis App.tsx).

```tsx
type Props = {
  cards: Card[];
  setCards: (cards: Card[]) => void;
  transform: ZoomTransform;
  setTransform(transform: ZoomTransform): void;
}
```

Nous connectons d3-zoom. DndKit et d3-zoom ont tous deux besoin d'une référence à l'élément, nous créons donc `canvasRef` et `updateAndForwardRef`, ce qui permet aux deux de référencer le même `HTMLDivElement`.

d3-zoom est une bibliothèque JavaScript, plutôt qu'un composant React, c'est pourquoi nous devons utiliser le code légèrement ésotérique ci-dessous, tel que `useMemo` et `useLayoutEffect` (bien que vous verrez les deux dans presque n'importe quelle base de code React de taille raisonnable).

```tsx
const canvasRef = useRef<HTMLDivElement | null>(null);

const updateAndForwardRef = (div: HTMLDivElement) => {
  canvasRef.current = div;
  setNodeRef(div);
};

// créer l'objet zoom d3, et utiliser useMemo pour le conserver pour les rerenders
const zoomBehavior = useMemo(() => zoom<HTMLDivElement, unknown>(), []);

// mettre à jour le transform lorsque d3 zoom notifie d'un changement.
const updateTransform = useCallback(
  ({ transform }: { transform: ZoomTransform }) => {
    setTransform(transform);
  },
  [setTransform]
);

useLayoutEffect(() => {
  if (!canvasRef.current) return;

  // obtenir les notifications de changement de transform de d3 zoom
  zoomBehavior.on("zoom", updateTransform);

  // attacher d3 zoom à l'élément div de la toile, qui gérera
  // les événements de molette de souris, de geste et de glisser automatiquement pour le défilement / zoom
  select<HTMLDivElement, unknown>(canvasRef.current).call(zoomBehavior);
  },
  [zoomBehavior, canvasRef, updateTransform]
 );
```

Nous ajoutons un wrapper / fenêtre autour de la toile. La div de la toile va maintenant défiler et zoomer (donc elle va beaucoup bouger à l'écran), nous l'enveloppons donc dans une autre div avec une position et une taille fixes et masquons tout débordement, afin que nous ayons une "fenêtre" montrant la partie pertinente de la toile.

Nous ajoutons également des styles CSS à la toile pour tenir compte du défilement et du zoom, utilisons la nouvelle fonction `updateAndForwardRef` et déplaçons la `ref` de la toile à la fenêtre de la toile.

```tsx
<div ref={updateAndForwardRef} className="canvasWindow">
  <div
    className="canvas"
    style={{
      // appliquer le transform de d3
      transformOrigin: "top left",
      transform: `translate3d(${transform.x}px, ${transform.y}px, ${transform.k}px)`,
      position: "relative",
      height: "300px",
    }}
  >
    ...
  </div>
</div>
```

[Canvas.tsx sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-3/blob/main/src/Canvas.tsx)

### **Draggable.tsx**

`Draggable` a maintenant besoin de différents styles CSS pour tenir compte du `transform` de d3-zoom, à la fois lorsqu'il est stationnaire et pendant qu'il est glissé.

Nous ajoutons une prop pour le transform de d3-zoom, que nous appelons `canvasTransform`, car nous utilisons déjà une variable `transform` de DndKit.

```tsx
type Props = {
  card: Card;
  canvasTransform: ZoomTransform;
}
```

Nous mettons à jour le CSS pour tenir compte du défilement et du zoom de la toile. Nous devons gérer deux cas, à la fois lorsqu'il est actuellement en cours de glisser, et lorsqu'il ne l'est pas.

```tsx
style={{
  position: "absolute",
  top: `${card.coordinates.y * canvasTransform.k}px`,
  left: `${card.coordinates.x * canvasTransform.k}px`,
  transformOrigin: "top left",
  ...(transform
    ? {
        // changement temporaire de cette position lors du glisser
        transform: `translate3d(${transform.x}px, ${transform.y}px, 0px) scale(${canvasTransform.k})`,
      }
    : {
        // zoom au zoom de la toile
        transform: `scale(${canvasTransform.k})`,
      }),
}}
```

Nous empêchons également l'événement `onPointerDown` de remonter à la toile, sinon il serait géré par d3-zoom et interprété comme une demande de commencer à glisser, ce qui entraîne le glisser de la toile et de la carte en même temps (un effet intéressant mais indésirable !)

```tsx
onPointerDown={(e) => {
  listeners?.onPointerDown?.(e);
  e.preventDefault();
}}
```

[Draggable.tsx sur GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-part-3/blob/main/src/Draggable.tsx)

## **Conclusion**

Il y a une certaine complexité dans les divers calculs de position / transformation, mais ce n'est pas trop fou, et il n'y a que deux dépendances à installer.

Il n'y a que quatre composants (`App`, `Canvas`, `Draggable` et `Addable`), et seulement environ 250 lignes de code pour tous, ce qui semble être une quantité très modeste pour toutes les fonctionnalités.

Cette démonstration est très simple, mais elle contient beaucoup de fonctionnalités de toile virtuelle, et il est facile de l'utiliser comme base et de construire quelque chose de plus élaboré par-dessus.