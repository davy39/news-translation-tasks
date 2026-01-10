---
title: Comment créer une application de garde-robe dynamique avec React Drag and Drop
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2025-05-05T14:55:53.567Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-dynamic-wardrobe-app-with-react-drag-and-drop
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746456835547/563ca5bd-27b0-421e-a0f3-a13f97388449.png
tags:
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de garde-robe dynamique avec React Drag and
  Drop
seo_desc: Have you ever found yourself stuck deciding what color outfit to wear? Maybe
  you’re mixing and matching different tops and bottoms, unsure if the colors go together.
  It’s a common dilemma – so common that many of us turn to friends or family for
  a se...
---

Vous êtes-vous déjà retrouvé bloqué en essayant de décider quelle tenue de couleur porter ? Peut-être mélangez-vous et associez-vous différents hauts et bas, sans être sûr que les couleurs s'accordent. C'est un dilemme courant – si courant que beaucoup d'entre nous demandent l'avis d'amis ou de la famille avant de sortir pour une réunion ou une sortie.

Mais que faire si vous êtes seul et devez prendre cette décision rapidement ? Imaginez avoir une application où vous pouvez faire glisser et déposer différentes couleurs de vêtements sur votre écran, visualisant instantanément votre tenue. Si cela a l'air bien, c'est toute la validation dont vous avez besoin – plus de doutes sur votre look.

Dans ce tutoriel, nous allons créer une application de garde-robe dynamique en utilisant React. Vous apprendrez à structurer des composants, à gérer les interactions de glisser-déposer et à concevoir une expérience utilisateur fluide. Commençons tout de suite !

## Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequisites)
    
* [Étapes pour créer une garde-robe dynamique avec React](#heading-steps-to-create-a-dynamic-wardrobe-using-react)
    
    * [Étape 1 : Configuration de votre projet](#heading-step-1-setting-up-your-project)
        
    * [Étape 2 : Configuration des états](#heading-step-2-setting-up-states)
        
    * [Étape 3 : Définition des options de couleur](#heading-step-3-defining-color-options)
        
    * [Étape 4 : Implémentation de la fonctionnalité de glisser-déposer](#heading-step-4-implementing-drag-and-drop-functionality)
        
    * [Étape 5 : Construction de l'interface utilisateur](#heading-step-5-building-the-user-interface)
        
    * [Étape 6 : Mise en place de l'ensemble](#heading-step-6-putting-it-all-together)
        
* [Conclusion](#heading-conclusion)
    

## **Prérequis**

Avant de commencer à coder, assurez-vous d'avoir :

* Des connaissances de base en React.
    
* Un éditeur de code de votre choix.
    

## Étapes pour créer une garde-robe dynamique avec React

Nous allons passer en revue comment construire ce projet étape par étape, afin qu'il soit facile à suivre. À la fin, vous comprendrez exactement comment fonctionne la fonctionnalité de glisser-déposer dans React.

### **Étape 1 : Configuration de votre projet**

Tout d'abord, vous devez configurer React et Tailwind CSS en utilisant Vite dans un projet. Si vous ne savez pas comment faire, consultez cet [article](https://www.freecodecamp.org/news/how-to-install-tailwindcss-in-react/) et suivez les étapes. Lorsque vous avez terminé, revenez ici et continuons à construire.

Si vous avez déjà un projet React avec Tailwind CSS que vous souhaitez utiliser, c'est très bien aussi.

### **Étape 2 : Configuration des états**

Nous allons commencer par configurer nos états. Si vous n'avez aucune idée de ce que sont les états, vous pouvez lire mon article sur les états [ici](https://www.freecodecamp.org/news/react-state-management/). Dans ce projet simple, nous n'aurons que deux états : un pour la couleur du haut sélectionnée (`selectedTop`) et l'autre pour la couleur du bas sélectionnée (`selectedBottom`). Nous allons définir la valeur initiale des deux états à **blanc** (avec le code hexadécimal #ffffff), comme montré ci-dessous :

```javascript
const [selectedTop, setSelectedTop] = useState("#ffffff");

const [selectedBottom, setSelectedBottom] = useState("#ffffff");
```

### **Étape 3 : Définition des options de couleur**

Ensuite, nous définissons un tableau d'options de couleur pour les tenues :

```javascript
const colorOptions = [

"#ff0000", // Rouge

"#0000ff", // Bleu

"#ffff00", // Jaune

"#00ff00", // Vert

"#ff00ff", // Rose

"#808080", // Gris

"#000000", // Noir

"#ffffff", // Blanc

];
```

Le tableau `colorOptions` fournit une palette vibrante de couleurs que les utilisateurs peuvent glisser sur les articles de vêtements.

### **Étape 4 : Implémentation de la fonctionnalité de glisser-déposer**

Maintenant, créons la fonctionnalité de glisser-déposer, qui est l'aspect central de ce projet. Nous aurons besoin de fonctions de gestion d'événements pour gérer certains événements lorsqu'ils sont déclenchés par des interactions spécifiques de l'utilisateur ou des événements du navigateur – dans ce cas, le glisser-déposer.

Voici les gestionnaires d'événements dont nous avons besoin pour implémenter la fonctionnalité de glisser-déposer :

1. `handleDragStart`
    

Cette fonction est déclenchée lorsque l'utilisateur commence à glisser un bloc de couleur depuis la palette de couleurs (généralement déclenché via `onDragStart` dans JSX).

```javascript
const handleDragStart = (e, color) => {

e.dataTransfer.setData("color", color);

};
```

Décomposons cela :

* `const handleDragStart = (e, color) => { ... }` : Cette fonction accepte deux paramètres – l'**objet d'événement de glisser (e)** et **color**, une valeur personnalisée représentant la couleur associée au bloc de couleur glissé.
    
* `e.dataTransfer.setData("color", color)` :
    
    * `dataTransfer` est une propriété de l'événement de glisser qui contient les données en cours de glisser.
        
    * `.setData("color", color)` stocke la valeur de la couleur sous la clé "color".
        

2. `handleDropOnTop`
    

Cette fonction est déclenchée lorsque le bloc de couleur est déposé sur la section "**haut**" de votre interface de tenue.

```javascript
const handleDropOnTop = (e) => {

e.preventDefault();

const color = e.dataTransfer.getData("color");

setSelectedTop(color);

};
```

Décomposons cela :

* `const handleDropOnTop = (e) => { 026 }` : Cette fonction prend un seul argument **e**, qui est l'objet d'événement représentant l'action de dépôt.
    
* `e.preventDefault()` : Par défaut, le navigateur n'autorisera pas le dépôt d'un élément à moins que vous ne empêchiez explicitement le comportement par défaut. Cela garantit que la cible de dépôt peut accepter l'élément glissé.
    
* `const color = e.daaTransfer.getData(01ccolor01d)` : récupère les données précédemment définies pendant l'opération de glisser à l'aide de `setData(01ccolor01d, color)` dans `handleDragStart`.
    
* `setSelectedTop(color)` : Les données `color` seront utilisées pour mettre à jour l'état `selectedTop` qui suit la couleur actuelle du haut sélectionné. Cela provoquera généralement le re-rendu de l'UI, montrant la couleur déposée sur la section "haut" de la tenue.
    

3. `handleDropOnBottom`
    

Cette fonction est déclenchée lorsque le bloc de couleur est déposé sur la section "**bas**" de votre interface de tenue.

```javascript
const handleDropOnBottom = (e) => {

e.preventDefault();

const color = e.dataTransfer.getData("color");

setSelectedBottom(color);

};
```

Décomposons cela :

* `const handleDropOnBottom = (e) => { ... }` : Cette fonction prend un seul argument **e**, qui est l'objet d'événement représentant l'action de dépôt.
    
* `e.preventDefault()` : Par défaut, le navigateur n'autorisera pas le dépôt d'un élément à moins que vous ne empêchiez explicitement le comportement par défaut. Cela garantit que la cible de dépôt peut accepter l'élément glissé.
    
* `const color = e.dataTransfer.getData("color")` : Récupère les données précédemment définies pendant l'opération de glisser à l'aide de `setData("color", color)` dans `handleDragStart`.
    
* `setSelectedBottom(color)` : Les données `color` seront utilisées pour mettre à jour l'état `selectedBottom` qui suit la couleur actuelle du haut sélectionné. Cela provoquera généralement le re-rendu de l'UI, montrant la couleur déposée sur la section "bas" de la tenue.
    

4. `allowDrop`
    

Cette fonction de gestion d'événements permet une cible de dépôt en empêchant le comportement par défaut du navigateur, qui sinon interdit le dépôt d'éléments.

```javascript
const allowDrop = (e) => {

e.preventDefault();

};
```

### **Étape 5 : Construction de l'interface utilisateur**

Ayant terminé la partie fonctionnelle de notre projet de garde-robe, nous voulons construire la partie visuelle que les utilisateurs peuvent voir et avec laquelle ils peuvent interagir.

L'interface utilisateur se composera de deux parties : une palette de couleurs à gauche et un aperçu de la tenue à droite. La section de la palette de couleurs comprendra 30 blocs de couleur tandis que la section d'aperçu de la tenue comprendra un haut et un bas, sur lesquels les couleurs sélectionnées peuvent être glissées et appliquées pour voir comment elles s'accordent.

Voici une représentation visuelle de l'interface utilisateur que nous construisons :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746193425525/449e4294-8917-470e-ad06-cf54d1809296.png align="center")

#### Création de la section de la palette de couleurs

Pour afficher toutes les couleurs fournies dans notre tableau `colorOptions`, nous devons d'abord parcourir le tableau composé de valeurs de couleur et rendre un `<div>` pour chaque couleur.

Chaque `<div>` :

* Agit comme un **bloc de couleur glissable** avec une largeur et une hauteur fixes.
    
* A une apparence semi-circulaire en utilisant les classes Tailwind CSS et le style en ligne pour appliquer la couleur de fond spécifique.
    
* Déclenche la fonction `handleDragStart` lorsque le glisser commence, en passant l'événement et la couleur sélectionnée.
    
* A une clé unique pour l'optimisation du rendu de React.
    
* Si la couleur est blanche (`#ffffff`), elle affiche conditionnellement le texte "**Blanc**" en gris clair pour la visibilité.
    

Cette configuration permet aux utilisateurs d'identifier visuellement et de glisser différentes options de couleur vers le haut ou le bas d'une tenue sur l'interface utilisateur.

```javascript
return (
  <div className="flex flex-col items-center p-6 bg-gray-100 rounded-lg min-h-screen">
    <h1 className="text-3xl font-extrabold mb-8 text-indigo-700">
      Garde-robe dynamique
    </h1>

    <div className="flex flex-col md:flex-row w-full gap-8">
      {/* Section de la palette de couleurs */}
      <div className="w-full md:w-1/3 bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4 text-center">
          Palette de couleurs
        </h2>
        <p className="mb-4 text-sm text-gray-600">
          Glissez les couleurs vers les pièces de la tenue
        </p>
        <div className="grid grid-cols-5 gap-2">
          {colorOptions.map((color) => (
            <div
              key={color}
              className="w-12 h-12 rounded-md shadow-sm cursor-move flex items-center justify-center"
              style={{ backgroundColor: color, border: "1px solid #ddd" }}
              draggable="true"
              onDragStart={(e) => handleDragStart(e, color)}
            >
              {color === "#ffffff" && (
                <span className="text-xs text-gray-400">Blanc</span>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  </div>
);
```

#### Création de l'aperçu de la tenue

Enfin, implémentons la section d'aperçu de la tenue, qui est la partie amusante. Il y a deux parties à l'affichage de la tenue : la section du haut et la section du bas. Regardons-les l'une après l'autre :

#### Section du haut

Cette section agit comme une **cible de dépôt pour la couleur du haut**. Elle se compose d'un div avec un SVG qui permet le remplissage de couleur.

```javascript
<div
  className="w-full flex items-center justify-center"
  onDrop={handleDropOnTop}
  onDragOver={allowDrop}
>
  {/* T-shirt */}
  <svg viewBox="0 0 24 24" width="180" height="140">
    <path
      d="M16 2H8L6 6v3h2v13h8V9h2V6l-2-4z"
      fill={selectedTop}
      stroke="#333"
      strokeWidth="0.2"
    />
  </svg>
</div>;
```

Dans cette section :

* `onDrop={handleDropOnTop}` : Définit la couleur du haut de la tenue, lorsqu'une couleur est déposée sur le div du haut.
    
* `allowDrop` est appelé via `onDragOver` pour activer le dépôt.
    
* Le SVG du T-shirt est dessiné et sa couleur de remplissage est contrôlée par `selectedTop`, qui se met à jour lorsqu'une nouvelle couleur est déposée.
    

#### Section du bas

Cette section agit comme une **cible de dépôt pour la couleur du bas**. Elle se compose d'un div avec un SVG qui permet le remplissage de couleur.

```javascript
<div
  className="w-full flex items-center justify-center -mt-8"
  onDrop={handleDropOnBottom}
  onDragOver={allowDrop}
>
  <svg viewBox="0 0 200 200" width="120" height="140">
    {/* Pantalon */}
    <path
      d="M60,20 L140,20 L150,180 L110,180 L100,100 L90,180 L50,180 L60,20 Z"
      fill={selectedBottom}
      stroke="#333"
      strokeWidth="2"
    />
    {/* Ceinture */}
    <rect x="60" y="18" width="80" height="5" fill="#444" />
    {/* Couture centrale */}
    <path d="M100,20 L100,100" stroke="#000" strokeWidth="1" />
  </svg>
</div>;
```

Dans cette section :

* `onDrop={handleDropOnBottom}` : Définit la couleur du bas de la tenue, lorsqu'une couleur est déposée sur le div du bas.
    
* `allowDrop` est appelé via `onDragOver` pour activer le dépôt.
    
* Le SVG du pantalon est dessiné et sa couleur de remplissage est contrôlée par `selectedBottom`, qui se met à jour lorsqu'une nouvelle couleur est déposée.
    
* Des détails supplémentaires comme une ceinture (rect) et une couture (path) ajoutent du réalisme.
    

Cela complète la section de l'interface utilisateur de notre projet.

### Étape 6 : Mise en place de l'ensemble

Maintenant que vous avez appris les aspects intégraux, voici le code complet qui vous donnera l'apparence et la fonctionnalité complètes :

```javascript
import { useState } from "react";

export default function App() {
  // État pour les couleurs sélectionnées
  const [selectedTop, setSelectedTop] = useState("#ffffff");
  const [selectedBottom, setSelectedBottom] = useState("#ffffff");

  // Options de couleur pour les vêtements
  const colorOptions = [
    "#ff0000", // Rouge
    "#0000ff", // Bleu
    "#ffff00", // Jaune
    "#00ff00", // Vert
    "#ff00ff", // Rose
    "#808080", // Gris
    "#000000", // Noir
    "#ffffff", // Blanc
    "#ffa500", // Orange
    "#800080", // Violet
    "#8B0000", // Rouge foncé
    "#006400", // Vert foncé
    "#00008B", // Bleu foncé
    "#4B0082", // Indigo
    "#228B22", // Vert forêt
    "#20B2AA", // Vert mer clair
    "#87CEEB", // Bleu ciel
    "#4682B4", // Bleu acier
    "#9932CC", // Orchidée foncée
    "#FF1493", // Rose foncé
    "#FF4500", // Rouge orangé
    "#FFD700", // Or
    "#F0E68C", // Kaki
    "#F5DEB3", // Blé
    "#D2B48C", // Tan
    "#A0522D", // Terre de Sienne
    "#8B4513", // Brun selle
    "#BC8F8F", // Brun rosé
    "#708090", // Gris ardoise
    "#2F4F4F", // Gris ardoise foncé
  ];

  // Gestionnaires de glisser-déposer
  const handleDragStart = (e, color) => {
    e.dataTransfer.setData("color", color);
  };

  const handleDropOnTop = (e) => {
    e.preventDefault();
    const color = e.dataTransfer.getData("color");
    setSelectedTop(color);
  };

  const handleDropOnBottom = (e) => {
    e.preventDefault();
    const color = e.dataTransfer.getData("color");
    setSelectedBottom(color);
  };

  const allowDrop = (e) => {
    e.preventDefault();
  };

  return (
    <div className="flex flex-col items-center p-6 bg-gray-100 rounded-lg min-h-screen">
      <h1 className="text-3xl font-extrabold mb-8 text-indigo-700">
        Garde-robe dynamique
      </h1>

      <div className="flex flex-col md:flex-row w-full gap-8">
        {/* Section de la palette de couleurs */}
        <div className="w-full md:w-1/3 bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4 text-center">
            Palette de couleurs
          </h2>
          <p className="mb-4 text-sm text-gray-600">
            Glissez les couleurs vers les pièces de la tenue
          </p>
          <div className="grid grid-cols-5 gap-2">
            {colorOptions.map((color) => (
              <div
                key={color}
                className="w-12 h-12 rounded-md shadow-sm cursor-move flex items-center justify-center"
                style={{ backgroundColor: color, border: "1px solid #ddd" }}
                draggable="true"
                onDragStart={(e) => handleDragStart(e, color)}
              >
                {color === "#ffffff" && (
                  <span className="text-xs text-gray-400">Blanc</span>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Section de visualisation de la tenue */}
        <div className="w-full md:w-2/3 bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4 text-center">
            Aperçu de la tenue
          </h2>
          <div className="flex flex-col items-center">
            <div className="relative w-64 h-64">
              {/* Conteneur de la tenue - meilleur positionnement */}
              <div className="relative w-full h-full flex flex-col items-center justify-center">
                {/* Section du haut - accepte le glisser-déposer */}
                <div
                  className="w-full flex items-center justify-center"
                  onDrop={handleDropOnTop}
                  onDragOver={allowDrop}
                >
                  {/* T-shirt */}
                  <svg viewBox="0 0 24 24" width="180" height="140">
                    <path
                      d="M16 2H8L6 6v3h2v13h8V9h2V6l-2-4z"
                      fill={selectedTop}
                      stroke="#333"
                      strokeWidth="0.2"
                    />
                  </svg>
                </div>
                <div
                  className="w-full flex items-center justify-center -mt-8"
                  onDrop={handleDropOnBottom}
                  onDragOver={allowDrop}
                >
                  <svg viewBox="0 0 200 200" width="120" height="140">
                    {/* Pantalon */}
                    <path
                      d="M60,20 L140,20 L150,180 L110,180 L100,100 L90,180 L50,180 L60,20 Z"
                      fill={selectedBottom}
                      stroke="#333"
                      strokeWidth="2"
                    />
                    {/* Ceinture */}
                    <rect x="60" y="18" width="80" height="5" fill="#444" />
                    {/* Couture centrale */}
                    <path d="M100,20 L100,100" stroke="#000" strokeWidth="1" />
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```

Voici notre garde-robe dynamique en pleine action :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746197218776/e840ecd6-665f-41b4-a590-02e91302cf26.gif align="center")

## **Conclusion**

Ce projet de garde-robe dynamique démontre la puissance de l'API de glisser-déposer de React combinée à la gestion d'état. Non seulement c'est un projet amusant à construire, mais il vous a également appris des concepts importants comme la gestion d'état dans les composants React, l'implémentation de la fonctionnalité de glisser-déposer, la création de mises en page réactives avec Tailwind CSS et l'utilisation de SVG pour des visuels interactifs.

Si vous avez aimé lire ce tutoriel, vous pouvez [M'offrir un café](https://buymeacoffee.com/timothyolanrewaju). Vous pouvez également me connecter sur [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750) pour plus de publications et d'articles liés à la programmation.

À la prochaine !