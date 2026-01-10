---
title: Comment optimiser une base de code React graphique — Optimiser le code d3-zoom
  et dnd-kit
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2025-10-16T12:36:57.964Z'
originalURL: https://freecodecamp.org/news/how-to-optimize-a-graphical-react-codebase
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760617553059/99fd830f-39a8-4067-9727-e9b35850168d.png
tags:
- name: React
  slug: reactjs
- name: optimization
  slug: optimization
- name: performance
  slug: performance
seo_title: Comment optimiser une base de code React graphique — Optimiser le code
  d3-zoom et dnd-kit
seo_desc: Miro and Figma are online collaborative canvas tools that became very popular
  during the pandemic. Instead of using sticky notes on a physical wall, you can add
  a virtual post—and an array of other things—to a virtual canvas. This lets teams
  collabor...
---

Miro et Figma sont des outils de canevas collaboratifs en ligne qui sont devenus très populaires pendant la pandémie. Au lieu d'utiliser des notes autocollantes sur un mur physique, vous pouvez ajouter un post-it virtuel — et une multitude d'autres éléments — sur un canevas virtuel. Cela permet aux équipes de collaborer virtuellement de manière familière par rapport au monde physique.

J'ai précédemment écrit un article montrant [comment créer un clone de Figma/Miro en React et TypeScript](https://www.freecodecamp.org/news/how-to-create-a-figma-miro-style-canvas-with-react-and-typescript/). Le [code de l'article](https://github.com/ceddlyburge/react-figma-miro-canvas-part-3) a été conçu pour être aussi simple que possible à comprendre, et dans cet article, nous allons l'optimiser. Le code utilisait [DndKit](https://dndkit.com/) pour le glisser-déposer, et [D3 Zoom](https://github.com/d3/d3-zoom) pour le panoramique et le zoom. Il y avait quatre composants (`App`, `Canvas`, `Draggable` et `Addable`), et environ 250 lignes de code. Vous n'avez pas besoin de lire l'article original pour comprendre celui-ci.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1759863968693/38c8784c-47c8-46e0-9f06-0567c0ebf668.gif align="center")

Les optimisations standards telles que `useCallback`, `memo`, et d'autres similaires l'ont rendu environ deux fois plus rapide lors du glissement, mais n'ont fait aucune différence pour le panoramique et le zoom. Des optimisations plus créatives/intensives l'ont rendu environ dix fois plus rapide dans la plupart des cas.

Vous pouvez voir le code optimisé sur [GitHub](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised) et il existe une [démo en direct sur GitHub pages](https://ceddlyburge.github.io/react-figma-miro-canvas-optimised/) pour tester la vitesse avec 100 000 cartes.

## Table des matières

* [Comment mesurer la performance dans les applications React](#heading-comment-mesurer-la-performance-dans-les-applications-react)
    
* [Comment étudier la performance](#heading-comment-etudier-la-performance)
    
* [Comment optimiser le panoramique et le zoom du canevas](#heading-comment-optimiser-le-panoramique-et-le-zoom-du-canevas)
    
* [Comment optimiser le glissement de cartes sur le canevas](#heading-comment-optimiser-le-glissement-de-cartes-sur-le-canevas)
    
* [Résultats](#heading-resultats)
    
* [Résumé](#heading-resume)
    

## Comment mesurer la performance dans les applications React

Il existe trois façons courantes de mesurer la performance dans les applications React :

* [Le profiler des React Dev Tools](https://chromewebstore.google.com/detail/react-developer-tools)
    
* [Le profiler des Chrome Dev Tools](https://developer.chrome.com/docs/devtools/performance/overview), en utilisant particulièrement les [pistes personnalisées (custom tracks)](https://www.debugbear.com/blog/favourite-devtools-features-in-2025#add-custom-tracks-to-performance-recordings)
    
* [Le composant Profiler](https://react.dev/reference/react/Profiler)
    

Ces outils sont tous excellents, mais aucun n'est tout à fait adapté dans ce cas précis. Dans la plupart des bases de code, le temps passé à exécuter le code JavaScript (à la fois notre code et celui du Framework React) est le problème principal. Cependant, une fois que tout votre code a été exécuté et que React a mis à jour le DOM, le navigateur a encore beaucoup de travail à faire :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1760025146277/7ae9ef2a-e248-491b-a07d-c674694d3fa9.png align="center")

Dans ce cas, ce temps de mise en page (layout) et de rendu du navigateur était significatif, et n'est pas pris en compte par le profilage React.

Vous pouvez utiliser des pistes personnalisées dans le profiler des outils de développement Chrome, mais c'est très fastidieux à utiliser.

Pour nous, l'[API performance](https://developer.mozilla.org/en-US/docs/Web/API/Performance) de JavaScript est la meilleure option, car elle donne des résultats plus proches de ceux ressentis par l'utilisateur et est relativement facile à utiliser.

Tout d'abord, nous effectuons un appel à [`performance.mark`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/mark) dans le gestionnaire d'événements qui démarre l'action, avec une chaîne de caractères pour décrire le point temporel. Par exemple, lors du démarrage d'une opération de zoom ou de panoramique :

```javascript
zoomBehavior.on("start", () => {
    performance.mark('zoomingOrPanningStart');
}
```

Ensuite, dans un hook `useEffect`, nous appelons à nouveau [`performance.mark`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/mark), et nous appelons [`performance.measure`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/measure) pour calculer le temps entre les deux points :

```javascript
useEffect(() => {
    performance.mark('zoomingOrPanningEnd');
    performance.measure('zoomingOrPanning', 'zoomingOrPanningStart', 'zoomingOrPanningEnd');
});
```

La [documentation React](https://react.dev/reference/react/useEffect) indique que `useEffect` s'exécute généralement après que le navigateur a dessiné l'écran mis à jour, ce qui est exactement ce que nous voulons.

Ce n'est pas parfait, et cela variera en fonction des spécifications de la machine et de ce que la machine fait d'autre à ce moment-là, mais c'était suffisant pour vérifier quelles optimisations fonctionnaient le mieux. Il est possible d'aller plus loin si nécessaire. Par exemple, en utilisant [Cypress pour automatiser et profiler des scénarios](https://filiphric.com/testing-frontend-performance-with-cypress), potentiellement en les exécutant plusieurs fois pour obtenir une bonne moyenne, ou en utilisant [Browserstack pour tester sur une variété d'appareils](https://www.browserstack.com/guide/performance-testing-with-cypress).

## Comment étudier la performance

L'essentiel de l'étude a consisté à utiliser le [profiler des React Dev Tools](https://chromewebstore.google.com/detail/react-developer-tools) pour enregistrer les profils des interactions utilisateur.

Les données de performance montrent combien de Commit il y a eu dans le profil, et combien de temps chacun a duré, ce qui est un excellent moyen de voir s'il y a trop de Commit.

Chaque Commit affiche un graphique en flammes (flame chart) montrant quels composants ont été rendus et pourquoi ils ont été re-rendus. Cela facilite grandement la recherche de moyens d'éviter le re-rendu et permet de vérifier que les stratégies de mémoïsation fonctionnent comme prévu. Cela comporte toutefois quelques bémols. Il est souvent indiqué ['Le composant parent a été rendu'](https://github.com/facebook/react/issues/19732), ce qui est un texte par défaut trompeur lorsqu'il ne comprend pas ce qui s'est passé (et est souvent dû à un changement dans un contexte parent). Il indique également des choses comme 'le hook 9 a changé', ce qui rend chronophage le fait de déterminer exactement quel hook a changé.

Le graphique en flammes montre également le temps que chaque composant a mis à s'afficher. Cela aide à cibler les composants problématiques sur lesquels nous devons nous concentrer.

## Comment optimiser le panoramique et le zoom du canevas

L'élément [Canvas](https://github.com/ceddlyburge/react-figma-miro-canvas-part-3/blob/main/src/Canvas.tsx) original utilisait la transformation CSS `translate3d(x, y, k)` pour effectuer le panoramique et le zoom du canevas. Cela fonctionne, mais cela ne met pas à l'échelle les éléments enfants. Ainsi, lorsque le zoom change, toutes les cartes sur le canevas doivent être re-rendues avec une nouvelle transformation CSS pour le nouveau niveau de zoom ([`scale(${canvasTransform.k})`](https://github.com/ceddlyburge/react-figma-miro-canvas-part-3/blob/97935f5b03ecff2f0732f6138e173a0c5e71a1ed/src/Draggable.tsx#L31)).

```javascript
 <div
    ...
    className="canvas"
    style={{
        transform: `translate3d(${transform.x}px, ${transform.y}px, ${transform.k}px)`,
        ...
    }}>
    ...
</div>
<div
    className="card"
    style={{
        ...
        transform: `scale(${canvasTransform.k})`,
    }}>
    ...
</div>
```

J'ai modifié cela pour utiliser `translateX(x) translateY(y) scale(k)`, ce qui produit le même effet, mais met à l'échelle les éléments enfants. De cette façon, lorsque le zoom change, aucune des cartes ne sera re-rendue (le `style` du composant `card` n'utilise plus `canvasTransform.k`).

```javascript
 <div
    ...
    className="canvas"
    style={{
        transform: `translateX(${transform.x}px) translateY(${transform.y}px) scale(${transform.k})`,
        ...
    }}>
    ...
</div>
<div
    className="card"
    ...
</div>
```

Le `Canvas` devait toujours se re-rendre chaque fois que le panoramique ou le zoom changeait, et il est possible d'empêcher cela avec `useRef` et en mettant à jour la transformation CSS par manipulation directe du DOM en JavaScript dans le gestionnaire d'événements [d3-zoom](https://d3js.org/d3-zoom). Cela n'apporte cependant pas d'amélioration significative de la performance et constitue un véritable hack, le compromis n'en vaut donc pas la peine.

Le zoom et le panoramique deviennent tous deux un peu plus lents lorsque le canevas est très dézoomé et qu'il y a (beaucoup) plus de cartes visibles à l'écran, simplement parce que le navigateur doit toutes les rendre. Cela reste exploitable avec 100 000 cartes. Il existe des solutions pour cela. Une option simple consiste à limiter l'étendue maximale du zoom. C'est un changement fonctionnel, donc potentiellement quelque chose qui ne répond pas aux exigences, mais c'est facile à faire dans d3-zoom en utilisant [`scaleExtent`](https://d3js.org/d3-zoom#zoom_scaleExtent) :

```javascript
zoom<HTMLDivElement>().scaleExtent([0.1, 100])
```

Une autre option consiste à créer un bitmap pour les niveaux de zoom très faibles et à le rendre comme un seul élément. Cela peut être difficile, mais cela signifie qu'il n'y aura aucun changement dans la fonctionnalité.

## Comment optimiser le glissement de cartes sur le canevas

### **Démarrer un glissement**

Le hook `useDraggable` de `DndContext` provoque des re-rendus lors du démarrage d'une opération de glissement.

Il est possible d'améliorer cela en modifiant le composant [`Draggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Draggable.tsx) pour qu'il ne contienne que ce hook (et les éléments qui l'utilisent) et en ayant un composant `DraggableInner` pour tout le reste (à l'intérieur d'un `memo`). Cela fonctionne bien pour réduire les re-rendus, dans la mesure où `DraggableInner` n'est presque jamais re-rendu, et améliore la vitesse de démarrage d'une opération de glissement. Cependant, c'était encore assez lent, et tout le temps était consommé sous le `DndContext`.

Une meilleure option consiste à créer un nouveau composant [`NonDraggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/NonDraggable.tsx), qui ressemble exactement au composant [`Draggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Draggable.tsx), mais ne se connecte pas à `DndContext`. Ces cartes sont affichées sur le canevas et possèdent un événement [`onMouseEnter`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/56d0c8256350ef3a0d8f50cc442305bd6c9d03c1/src/NonDraggable.tsx#L10) pour échanger le composant [`Draggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Draggable.tsx) avec la carte active, afin que le glissement continue de fonctionner.

```javascript
const onMouseEnter = useCallback(() => {
    setHoverCard(card);
}, []);
```

Cela fonctionne bien et améliore considérablement la vitesse lors du démarrage d'une opération de glissement, mais c'était encore assez lent avec un grand nombre de cartes. Presque rien n'était re-rendu, mais l'utilisation de `memo` a toujours un coût temporel, car il doit vérifier si les composants ont changé.

Pour corriger cela, nous créons un composant [`AllCards`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/AllCards.tsx), qui contient toutes les cartes du canevas sous forme de composants [`NonDraggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/NonDraggable.tsx). Comme il rend toujours toutes les cartes, il n'a presque jamais besoin d'être re-rendu, et il est utilisé avec `memo`. Ainsi, au lieu que chaque carte individuelle utilise un `memo` (avec le coût temporel associé), il n'y a plus qu'un seul composant utilisant un `memo`. Pour que le glissement fonctionne toujours, le composant [`Draggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Draggable.tsx) actif est rendu par-dessus, masquant le composant [`NonDraggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/NonDraggable.tsx) en dessous. Il y a également un composant [`Cover`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Cover.tsx) en dessous, de sorte que lorsque le composant [`Draggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Draggable.tsx) est déplacé, le composant [`NonDraggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/NonDraggable.tsx) en dessous reste caché.

Code original, où chaque carte est un composant [`Draggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Draggable.tsx) :

```javascript
<DndContext ...>
    {cards.map((card) => (
        <Draggable card={card} key={card.id} canvasTransform={transform} />
    ))}
</DndContext>
```

Code optimisé, où le composant [`AllCards`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/AllCards.tsx) rend toutes les cartes en tant que composants [`NonDraggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/NonDraggable.tsx), puis un composant [`Cover`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Cover.tsx) et un composant [`Draggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Draggable.tsx) pour la carte active.

```javascript
<AllCards cards={cards} setHoverCard={setHoverCard} />
<DndContext ...>
    <Cover card={hoverCard} />
    <Draggable card={hoverCard} canvasTransform={transform} />
</DndContext>
```

Cela fonctionne très bien. Avec un faible nombre de cartes, la vitesse est à peu près la même, mais avec un nombre élevé de cartes, c'est environ vingt fois plus rapide.

Il existe maintenant un nouveau problème de performance potentiel avec l'événement [`onMouseEnter`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/56d0c8256350ef3a0d8f50cc442305bd6c9d03c1/src/NonDraggable.tsx#L10) qui échange le composant [`Draggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/Draggable.tsx) pour la carte active, mais cela ne fait qu'ajouter deux composants au DOM, et c'est très rapide même avec un grand nombre de cartes.

### **Terminer un glissement**

Terminer une opération de glissement est difficile à optimiser, car la position d'une carte change, et cela nécessite un re-rendu, ce qui signifie que le composant [`AllCards`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/AllCards.tsx) doit également être re-rendu.

Vous pouvez voir le code original ci-dessous. Même en utilisant `memo` avec le composant Draggable, l'opération de fin de glissement prend toujours 2500 ms avec 100 000 cartes, principalement en raison de la complexité du composant `Draggable` et de son intégration avec DndKit.

```javascript
<DndContext ...>
    {cards.map((card) => (
        <Draggable card={card} key={card.id} canvasTransform={transform} />
    ))}
</DndContext>
```

Cependant, nous utilisons maintenant les composants [`NonDraggable`](https://github.com/ceddlyburge/react-figma-miro-canvas-optimised/blob/main/src/NonDraggable.tsx), qui se mémoïsent tous avec succès, et seule la carte glissée est re-rendue. Il y a toujours un coût temporel à l'utilisation du `memo`, et c'est la partie la plus lente de la solution, mais cela conduit à une augmentation de la vitesse à 500 ms avec 100 000 cartes.

```javascript
const NonDraggable = memo(...)

const AllCards = memo((cards, setHoverCard) => {
    <>
        {cards.map((card) => {
            <NonDraggable card={card} key={card.id} setHoverCard={setHoverCard} />);
        })}
    </>;
});
```

## **Résultats**

La version de base non optimisée commençait à devenir lente entre 1 000 et 5 000 cartes. Les optimisations standards ont amélioré cela jusqu'à environ 10 000 cartes, et l'optimisation plus poussée l'a porté à environ 100 000 cartes. Le compromis est que le code devient nettement plus complexe, ce qui le rend plus difficile à comprendre et à modifier, en particulier pour les personnes qui découvrent la base de code.

|  |  | **Pan (ms)** | **Zoom (ms)** | **Début glissement (ms)** | **Fin glissement (ms)** | **Survol carte (ms)** |
| --- | --- | --- | --- | --- | --- | --- |
| 1000 cartes | Base | 3 | 4 | 200 | 50 | \- |
|  | Optimisation de base | 2 | 3 | 200 | 30 | \- |
|  | Optimisation intensive | 10 | 10 | 7 | 15 | 2 |
| 5000 cartes | Base | 20 | 150 | 450 | 200 | \- |
|  | Optimisation de base | 20 | 150 | 200 | 80 | \- |
|  | Optimisation intensive | 10 | 10 | 25 | 40 | 2 |
| 10 000 cartes | Base | 50 | 300 | 900 | 400 | \- |
|  | Optimisation de base | 50 | 300 | 400 | 180 | \- |
|  | Optimisation intensive | 25 | 25 | 50 | 50 | 2 |
| 50 000 cartes | Base | 1000 | 1500 | 4000 | 1800 | \- |
|  | Optimisation de base | 1000 | 1500 | 1900 | 900 | \- |
|  | Optimisation intensive | 150 | 150 | 150 | 250 | 5 |
| 100 000 cartes | Base | \- | \- | \- | \- | \- |
|  | Optimisation de base | 3000 | 4500 | 5000 | 2500 | \- |
|  | Optimisation intensive | 150 | 250 | 300 | 500 | 15 |

## Résumé

Il est inhabituel d'afficher 100 000 éléments ou plus à l'écran dans une application React standard, mais dans une base de code hautement graphique, cela devient beaucoup plus probable.

Avec ces chiffres, le moteur de rendu du navigateur est susceptible de prendre un temps considérable. Il est donc préférable d'utiliser l'API performance pour mesurer la performance, au lieu des outils React habituels.

Les stratégies d'optimisation React standards fonctionnent et améliorent la situation, mais il est nécessaire d'aller plus loin, en trouvant des moyens d'éviter les rendus, et même d'éviter trop de comparaisons `memo`.