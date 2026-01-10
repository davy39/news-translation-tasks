---
title: 'Comment utiliser le Compound Components Pattern dans React : de la Prop Soup
  aux interfaces flexibles'
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2025-10-09T01:21:18.239Z'
originalURL: https://freecodecamp.org/news/compound-components-pattern-in-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759972853846/49e605c8-be15-44a4-9fc6-283be0cc0e4c.png
tags:
- name: React
  slug: reactjs
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: 'Comment utiliser le Compound Components Pattern dans React : de la Prop
  Soup aux interfaces flexibles'
seo_desc: Have you ever opened React project source code and wondered why things are
  so messy? Have you ever tried adding a feature to a React component created by someone
  else and felt that you needed to rewrite it? Have you felt nightmarish in tackling
  state...
---

Avez-vous déjà ouvert le code source d'un projet React en vous demandant pourquoi les choses étaient si désordonnées ? Avez-vous déjà essayé d'ajouter une fonctionnalité à un composant React créé par quelqu'un d'autre en ayant l'impression de devoir tout réécrire ? Avez-vous vécu des cauchemars en gérant l'état et les props d'un composant et de ses enfants ?

Si vous avez crié « Oui ! » à ce qui précède, vous n'êtes pas seul. C'est un sentiment partagé par de nombreux développeurs React à travers le monde. Mais React lui-même n'est pas responsable de ces problèmes. Ces situations surviennent à cause de « code smells » tels que :

* Des props transmises sur six niveaux de profondeur (Prop drilling).
    
* Un composant unique et boursouflé qui fait tout.
    
* Une logique dupliquée entre différents composants.
    
* Un rendu (et re-rendu) négligent causant des problèmes de performance.
    

Un `Code Smell` ne signifie pas un code cassé. C'est plutôt une indication que le code peut fonctionner maintenant, mais qu'il est difficile à maintenir, à réutiliser, à faire évoluer, et beaucoup plus difficile à déboguer.

Et c'est exactement là que nous devons utiliser les `Design Patterns`. Ce sont des solutions éprouvées aux divers problèmes de code smell que les développeurs rencontrent depuis des décennies. Lorsque vous savez bien les utiliser, vous obtenez une base de code propre et maintenable, facile à améliorer, à déboguer et à faire évoluer.

Aujourd'hui, nous allons plonger dans l'un des patterns de conception les plus importants de React, appelé le `Compound Components Pattern`. Ce pattern évite aux développeurs React de passer une longue liste de props et aide à construire des composants d'interface utilisateur composables.

Ceci sera un tutoriel complet et pratique. Préparez votre éditeur de code préféré et commençons. Cet article est également disponible sous forme de tutoriel vidéo dans le cadre de l'initiative [15 Days of React Design Patterns](https://www.youtube.com/playlist?list=PLIJrr73KDmRyQVT__uFZvaVfWPdfyMFHC). N'hésitez pas à y jeter un œil.

%[https://www.youtube.com/watch?v=LglWulOqh6k] 

## Table des matières

1. [Configuration du code React 19](#heading-configuration-du-code-react-19)
    
2. [Un composant Modal désordonné](#heading-un-composant-modal-desordonne)
    
3. [Les problèmes de ce composant Modal désordonné](#heading-les-problemes-de-ce-composant-modal-desordonne)
    
4. [Le Compound Components Pattern](#heading-le-compound-components-pattern)
    
5. [Comment construire un composant Modal en utilisant le Compound Components Pattern](#heading-comment-construire-un-composant-modal-en-utilisant-le-compound-components-pattern)
    
    * [Pourquoi n'avons-nous pas créé de fichiers séparés pour les sous-composants ?](#heading-pourquoi-navons-nous-pas-cree-de-fichiers-separes-pour-les-sous-composants)
        
    * [Comment utiliser le composant Modal](#heading-comment-utiliser-le-composant-modal)
        
    * [Comment construire un composant Accordéon en utilisant le Compound Components Pattern](#heading-comment-construire-un-composant-accordeon-en-utilisant-le-compound-components-pattern)
        
    * [Ajouter l'Accordéon à la Modal](#heading-ajouter-laccordeon-a-la-modal)
        
6. [Les cas d'utilisation](#heading-les-cas-dutilisation)
    
7. [Les pièges et anti-patterns](#heading-les-pieges-et-anti-patterns)
    
8. [15 jours de React Design Patterns](#heading-15-jours-de-react-patterns)
    
9. [Avant de terminer...](#heading-avant-de-terminer)
    

## Configuration du code React 19

La meilleure façon de comprendre comment appliquer un design pattern est de refactoriser un code désordonné contenant des code smells pour l'améliorer vers un code plus propre. Créons donc un environnement de codage afin de pouvoir d'abord y placer notre code désordonné, puis appliquer le design pattern.

Note : vous pouvez trouver tout le code source utilisé dans ce tutoriel sur le [GitHub de tapaScript](https://github.com/tapascript/15-days-of-react-design-patterns/tree/main/day-03/compound-components-patterns). N'hésitez pas à le suivre en parallèle.

Assurez-vous également d'avoir Node.js installé (de préférence v18+). Vous pouvez vérifier cela en tapant cette commande dans votre terminal :

```bash
node -v
```

Si vous obtenez une sortie avec la version de Node.js installée, vous êtes prêt. Sinon, téléchargez et installez Node.js depuis [ici](https://nodejs.org/en/download).

Maintenant, exécutez cette commande dans votre terminal pour créer un projet React 19 :

```bash
npx degit atapas/code-in-react-19#main compound-components-pattern
```

Cela créera un dossier appelé `compound-components-pattern` contenant les fichiers du projet React basés sur Vite. Maintenant, changez de répertoire avec cette commande :

```bash
cd compound-components-pattern
```

Ensuite, installez les dépendances :

```bash
npm install ## Ou yarn install, ou pnpm install, etc.
```

Maintenant, vous pouvez importer le dossier du projet dans votre éditeur de code préféré (j'utilise VS Code).

![Code Scaffolding](https://cdn.hashnode.com/res/hashnode/image/upload/v1759478983493/692ac0f9-4780-4d60-bc72-55f27b9a6074.png align="center")

Enfin, pour démarrer le projet localement, utilisez la commande suivante :

```bash
npm run dev ## Ou yarn dev, ou pnpm dev
```

Le projet devrait maintenant fonctionner localement et être accessible sur l'URL par défaut, [`http://localhost:5173`](http://localhost:5173). Vous pouvez accéder à l'URL dans votre navigateur. Nous sommes maintenant prêts à coder.

## Un composant Modal désordonné

Commençons par créer un composant Modal. Créez un répertoire appelé `messy` sous le répertoire `src/`. Ensuite, créez un fichier appelé `Modal.jsx` sous `src/messy/` avec l'extrait de code suivant :

```javascript
function Modal({ title, body, primaryAction, secondaryAction }) {
    return (
        <div className="modal-backdrop">
            <div className="modal-container">
                <h2 className="modal-header">{title}</h2>
                <p className="modal-body">{body}</p>
                <div className="modal-footer">
                    {secondaryAction}
                    {primaryAction}
                </div>
            </div>
        </div>
    );
}

export default Modal;
```

Il s'agit d'une implémentation React simple d'un composant modal qui accepte un titre, un corps et quelques actions comme props pour les afficher sous forme de modal.

* Le `title` : Le titre de l'en-tête de la modal.
    
* Le `body` : Le contenu de la modal.
    
* Le `primaryAction` : Un bouton d'action comme supprimer, créer, enregistrer, etc., à placer dans la section pied de page.
    
* Le `secondaryAction` : Un bouton d'action comme annuler, fermer, etc., à placer dans la section pied de page.
    

Ensuite, ouvrez le fichier `App.jsx` et remplacez le code existant par l'extrait suivant :

```javascript
import Modal from "./messy/Modal";

import "./App.css";

function App() {
    return (
        <div className="flex flex-col items-center">
            <Modal
                title="Supprimer le compte"
                body="Êtes-vous sûr de vouloir supprimer votre compte ?"
                primaryAction={<button>Supprimer</button>}
                secondaryAction={<button>Annuler</button>} />
        </div>
    );
}

export default App;
```

Ici, nous avons importé le composant `Modal` et l'avons utilisé en passant les valeurs de ses props. Allez dans l'onglet du navigateur et accédez à l'URL de l'application. Vous devriez voir la modal apparaître comme ceci :

![messy modal without style](https://cdn.hashnode.com/res/hashnode/image/upload/v1759409687600/825901e9-5b38-49a7-8d7d-74a0867f6a01.png align="center")

Comme elle ne ressemble pas à une modal traditionnelle avec un arrière-plan, corrigeons cela avec du CSS. Ouvrez `App.css`, collez les styles CSS suivants et enregistrez :

```css
.modal-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}
.modal-container {
    background: white;
    border-radius: 8px;
    padding: 1rem;
    width: 400px;
    position: relative;
}
.modal-header {
    font-weight: bold;
    margin-bottom: 1rem;
}
.modal-footer {
    display: flex;
    justify-content: flex-end;
    gap: 0.5rem;
    margin-top: 1rem;
}
.modal-close {
    position: absolute;
    top: 8px;
    right: 8px;
    background: none;
    border: none;
    font-size: 1.2rem;
}
```

Super ! Vous avez maintenant une boîte de dialogue modale élégante demandant confirmation pour supprimer votre compte.

![Messy Modal with style](https://cdn.hashnode.com/res/hashnode/image/upload/v1759409736382/ceaaa23e-26d3-4d7d-93ed-ae83aa69b421.png align="center")

## Les problèmes de ce composant Modal désordonné

Question pour vous : quels problèmes pensez-vous que cette implémentation de modal pourrait avoir ?

Voici les réponses :

1. `Manque de flexibilité` : La modal a une structure rigide qui dicte exactement ce qu'elle affiche. Et si vous voulez une modal sans titre ? Ou une modal avec une mise en page personnalisée ? Ou plus de deux boutons d'action ? Vous devez écrire une logique supplémentaire et passer des props additionnelles chaque fois que vous voulez améliorer la modal pour un autre cas d'utilisation. Ces changements dans le composant entraîneront des problèmes de maintenance et augmenteront le code smell.
    
2. `Responsabilités mixtes` : La modal essaie de faire plusieurs choses. Elle gère à la fois la mise en page et le contenu. Cela viole le principe de séparation des préoccupations que nous apprenons d'autres patterns, comme le [Container-Presenter Pattern](https://www.youtube.com/watch?v=1UHbhikwg-s).
    
3. `Réutilisabilité difficile` : La modal manque de réutilisabilité à cause de sa rigidité. Actuellement, si vous voulez une modal avec ceci :
    
    ```javascript
    <h2>Quelque chose ne va pas !</h2>
    <img src="warning.png" />
    <p>Une erreur est survenue. Veuillez consulter les logs pour plus de détails.</p>
    ```
    
    Vous ne pouvez pas réutiliser ce composant, et vous finirez par en créer un nouveau.
    
4. `Faible scalabilité` : Le composant modal n'est pas scalable. Imaginez, par exemple, que vous créiez une bibliothèque de composants et que vous finissiez par créer plusieurs instances de modal comme ConfirmationModal, InfoModal, FormModal, ImageModal, etc. Ce serait un énorme frein à la scalabilité de cette bibliothèque de devoir créer et maintenir chaque nouvelle version de la modal.
    
5. `Difficile à tester` : Cette implémentation de modal est difficile à tester en raison de son couplage étroit avec les props.
    

Avec ces problèmes en tête, accueillons le compound components pattern et voyons comment il peut nous aider à les résoudre.

## Le Compound Components Pattern

Le `Compound Components Pattern` dans React est un design pattern où un composant parent travaille avec ses composants enfants pour partager un état et un comportement implicites. Au lieu de passer une longue liste de props, le parent gère l'état et expose des composants enfants flexibles (&lt;Modal.Header&gt;, &lt;Modal.Body&gt;, &lt;Modal.Footer&gt;, etc.) afin que les utilisateurs puissent composer l'interface naturellement, tout comme avec des éléments HTML natifs.

![Compound Components Pattern Diagram](https://cdn.hashnode.com/res/hashnode/image/upload/v1759409949714/8144535d-c0f3-4ae7-bd8d-ab93fe7bf6c2.png align="center")

Pensez au Compound Composition Pattern comme à des briques LEGO.

* Le composant parent est comme la plaque de base LEGO.
    
* Les composants enfants sont les briques LEGO (porte, fenêtre, toit, etc.).
    
* Vous ne passez pas de props à la plaque de base en disant : *« ajoute une porte ici, ajoute une fenêtre là »*. Au lieu de cela, vous placez simplement les pièces où vous le souhaitez.
    
* La plaque de base (parent) fournit toujours les règles et la structure (tenons, alignement, stabilité), mais vous avez la flexibilité d'assembler votre modèle comme bon vous semble.
    

Compris ? C'est là toute la puissance des compound components. C'est une composition flexible avec un état/comportement partagé en dessous.

Refactorisons maintenant notre composant modal désordonné en appliquant le compound components pattern.

## Comment construire un composant Modal en utilisant le Compound Components Pattern

Créez un dossier appelé `with-pattern` sous le dossier `src/`. Nous y organiserons et maintiendrons le composant modal, et plus tard, un composant accordéon.

Ensuite, créez un dossier appelé `modal` sous `src/with-pattern`. Enfin, créez un fichier appelé `Modal.jsx` avec l'extrait de code suivant :

```javascript
// Emplacement du fichier : src/with-pattern/modal/Modal.jsx

const Modal = ({ children, isOpen, onClose }) => {
    if(!isOpen) return null;
    return (
        <div className="modal-backdrop">
            <div className="modal-container">
                {children}
                <button className="modal-close" onClick={onClose}>
                    ✖
                </button>
            </div>

        </div>
    );
};

function ModalHeader({ children }) {
    return <div className="modal-header">{children}</div>;
}

function ModalBody({ children }) {
    return <div className="modal-body">{children}</div>;
}

function ModalFooter({ children }) {
    return <div className="modal-footer">{children}</div>;
}

Modal.Header = ModalHeader;
Modal.Body = ModalBody;
Modal.Footer = ModalFooter;

export default Modal;
```

Laissez-moi vous expliquer :

* Tout d'abord, concentrez-vous sur le composant Modal ci-dessus. Il ne prend plus title, body, etc., comme props. À la place, il accepte `children`, une prop spéciale dans React pour passer n'importe quel élément HTML, groupe de HTML, JSX, ou même un composant React. Cela apporte une flexibilité telle que nous ne sommes plus limités à une structure particulière pour la Modal.
    
* Le JSX du composant Modal affiche simplement la prop `children` telle quelle, donnant tout le pouvoir au consommateur du composant Modal pour passer n'importe quelle structure. Le composant Modal utilise le style de l'arrière-plan et du conteneur pour dicter l'aspect de base d'une modal.
    
* Le JSX de la Modal possède également un bouton pour fermer la modal en cliquant sur un x. Pour ouvrir et fermer la modal, nous avons passé deux props supplémentaires, `isOpen` et `onClose`. Vous pouvez imaginer que `isOpen` est une valeur d'état que le consommateur utilise pour ouvrir la modal, et `onClose` est une fonction qui définit `isOpen` à false pour la fermer.
    
* Ensuite, nous avons défini trois autres composants, `ModalHeader`, `ModalBody` et `ModalFooter`, qui sont tout aussi flexibles pour accepter n'importe quelle structure HTML légitime ou composant React via la prop `children`. Vous pouvez maintenant passer n'importe quoi à afficher dans l'en-tête de la modal. Il en va de même pour le corps et le pied de page.
    
* Ensuite, nous ajoutons l'en-tête, le corps et le pied de page comme sous-composants du composant `Modal`.
    
    ```javascript
    Modal.Header = ModalHeader;
    Modal.Body = ModalBody;
    Modal.Footer = ModalFooter;
    ```
    
* Enfin, nous avons exporté le composant `Modal`.
    

### Pourquoi n'avons-nous pas créé de fichiers séparés pour les sous-composants ?

Cette question est tout à fait naturelle. En général, nous suivons la pratique standard d'un composant par fichier source (.jsx/.tsx). Ici, nous semblons enfreindre cette règle... est-ce le cas ? Pas vraiment.

Les règles d'or sont :

* Les sous-composants (ModalHeader, ModalBody et ModalFooter) n'ont de sens que dans le contexte de la Modal. Ils n'ont pas (ou n'ont pas besoin) d'existence au-delà de la modal.
    
* Ce sont de petits composants utilitaires que vous ne prévoyez pas de réutiliser ailleurs.
    
* Les garder ensemble facilite la découverte et protège contre une mauvaise utilisation potentielle dont nous discuterons plus tard dans la section sur les pièges.
    

### Comment utiliser le composant Modal

C'est réglé. Apprenons maintenant à utiliser ce composant Modal et voyons comment il apporte flexibilité, réutilisabilité, scalabilité et testabilité.

Ouvrez le fichier `App.jsx` et remplacez son contenu par l'extrait suivant :

```javascript
import { useState } from "react";
// import Modal from "./messy/Modal";
import Modal from "./with-pattern/modal/Modal";

import "./App.css";

function App() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="flex flex-col items-center">

      <button onClick={() => setIsOpen(true)}>Ouvrir la Modal</button>

      <Modal isOpen={isOpen} onClose={() => setIsOpen(false)}>

        <Modal.Header>
          <h2>Bienvenue !</h2>
        </Modal.Header>

        <Modal.Body>
          <p>
              Ceci est une modal construite avec le Compound Component
              pattern.
          </p>
        </Modal.Body>

        <Modal.Footer>
          <button>Aide !</button>
          <button onClick={() => setIsOpen(false)}>Fermer</button>
          <button onClick={() => alert("Action effectuée !")}>Agir</button>
        </Modal.Footer>

      </Modal>

    </div>
  );
}

export default App;
```

Regardez comment nous avons passé un ensemble de JSX à l'intérieur de &lt;Modal&gt;...&lt;/Modal&gt; en tant qu'enfants. C'est très puissant. Nous passons les sous-composants header, body et footer dans l'ordre où nous voulons qu'ils apparaissent.

Ensuite, si nous regardons les composants &lt;ModalHeader&gt;, &lt;ModalBody&gt; ou &lt;ModalFooter&gt;, nous pouvons à nouveau leur passer n'importe quoi comme enfants. Par exemple, le &lt;ModalFooter /&gt; peut maintenant prendre trois boutons (ou n'importe quoi d'autre) selon les besoins.

Nous pouvons composer les composants comme des blocs Lego pour construire le type de Modal que nous souhaitons. Vous n'avez plus besoin de composants différents pour représenter différents types de modals. Ce composant unique peut répondre à tous vos besoins sans introduire de drame de « prop soup ».

Nous avons un bouton pour ouvrir la modal, et le composant App.jsx gère un état appelé `isOpen` pour gérer l'ouverture et la fermeture.

Vous devriez pouvoir voir ces changements maintenant dans le navigateur. Cliquez sur le bouton d'ouverture de la modal.

![Open Modal Button](https://cdn.hashnode.com/res/hashnode/image/upload/v1759410185904/b7adbab0-9d24-4245-92ad-84766817af12.png align="center")

La boîte de dialogue modale s'ouvre avec tout le contenu que nous lui avons passé.

![Modal With Pattern](https://cdn.hashnode.com/res/hashnode/image/upload/v1759410275413/9bff6791-3cf8-45eb-aea8-a85e9a95777d.png align="center")

C'est un grand pas vers l'obtention d'un code propre que d'utiliser le design pattern compound components. Maintenant que vous êtes familier avec les bases, faisons rapidement une autre implémentation classique de ce pattern en construisant un composant Accordéon.

## Comment construire un composant Accordéon en utilisant le Compound Components Pattern

Un composant accordéon est un tableau d'éléments d'accordéon. C'est une combinaison d'un en-tête et d'un corps qui affiche et masque le contenu lorsque les utilisateurs cliquent sur l'en-tête.

Créez un dossier appelé `accordion` sous le dossier `src/with-pattern`. Maintenant, créez un fichier appelé `Accordion.jsx` à l'intérieur de `src/with-pattern/accordion` avec l'extrait de code suivant :

```javascript
import { useState } from "react";

function Accordion({ children }) {
  return <div className="accordion">{children}</div>;
}

function AccordionItem({ title, children }) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="accordion-item">
      <button className="accordion-title" onClick={() => setIsOpen(!isOpen)}>
        {title}
      </button>
      {isOpen && <div className="accordion-content">{children}</div>}
    </div>
  );
}

// Attacher les sous-composants
Accordion.Item = AccordionItem;

export default Accordion;
```

Ici,

* Nous avons suivi le même pattern que pour la modal précédemment. Nous avons un composant `Accordion` qui prend une prop spéciale appelée `children`, permettant à l'Accordéon d'accepter n'importe quel composant HTML/JSX/React et de l'afficher.
    
* Ensuite, nous avons défini `AccordionItem`. Il prend deux props : le titre pour créer l'en-tête, et la prop spéciale `children` pour former le contenu de l'accordéon de manière flexible.
    
* L'en-tête est formé à l'aide du bouton piloté par un état appelé `isOpen` pour afficher/masquer la zone de contenu.
    
* La zone de contenu d'un `AccordionItem` peut être n'importe quoi : un paragraphe, un tableau, une image ou même un JSX les combinant.
    
* Enfin, nous avons ajouté AccordionItem comme sous-composant du composant Accordion.
    

Pour améliorer l'apparence de l'accordéon, ajoutons quelques styles. Ouvrez le fichier `App.css` et ajoutez ces styles à la fin du fichier :

```css
.accordion-item {
    margin-bottom: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
}
.accordion-title {
    width: 100%;
    text-align: left;
    padding: 0.5rem;
    font-weight: bold;
    cursor: pointer;
    background: #f9f9f9;
    border: none;
}
.accordion-content {
    padding: 0.5rem;
    background: #fff;
}
```

Super, utilisons maintenant le composant Accordéon. Créez un nouveau fichier appelé `AccordionDemo.jsx` sous le dossier `src/with-pattern/accordion` avec l'extrait de code suivant :

```javascript
import Accordion from "./Accordion";

export default function AccordionDemo() {
  return (
    <Accordion>
      <Accordion.Item title="Qu'est-ce que le Compound Component Pattern ?">
        C'est un pattern React qui permet aux composants parents et enfants de travailler
        ensemble de manière transparente tout en offrant aux développeurs une composition flexible.
      </Accordion.Item>

      <Accordion.Item title="Pourquoi l'utiliser ?">
        Il facilite la construction et l'utilisation de bibliothèques d'UI comme les modals, les onglets, les accordéons, les menus, etc.
      </Accordion.Item>

      <Accordion.Item title="Pièges ?">
        Une utilisation excessive peut entraîner des structures profondément imbriquées ou rendre les choses plus difficiles
        à déboguer si elles ne sont pas bien documentées.
      </Accordion.Item>
    </Accordion>
  );
}
```

Voyez comment le composant `Accordion` peut accepter un ensemble de composants AccordionItem. Vous pouvez également créer un tableau de composants `AccordionItem` et les passer dynamiquement au composant Accordion.

Chacun des composants AccordionItem accepte la prop title, et nous avons passé le texte en tant qu'enfants. Si nécessaire, vous pouvez passer n'importe quel autre JSX valide en tant qu'enfant. C'est incroyable !

### Ajouter l'Accordéon à la Modal

Maintenant, portons l'utilisation de ce pattern au niveau supérieur. Que diriez-vous d'utiliser `AccordionDemo` à l'intérieur du composant `Modal` ? Pouvons-nous le faire sans modifier le composant Modal ?

Oh que oui ! Rappelez-vous, le composant Modal accepte n'importe quel JSX comme enfant, tout comme le composant ModalBody. Nous pouvons donc simplement importer le composant AccordionDemo dans le fichier App.jsx et l'utiliser à l'intérieur de &lt;Modal.Body&gt;...&lt;/Modal.Body&gt; comme indiqué ci-dessous :

```javascript
import { useState } from "react";
// import Modal from "./messy/Modal";
import Modal from "./with-pattern/modal/Modal";

import AccordionDemo from "./with-pattern/accordion/AccordionDemo";

import "./App.css";

function App() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="flex flex-col items-center">

      <button onClick={() => setIsOpen(true)}>Ouvrir la Modal</button>

      <Modal isOpen={isOpen} onClose={() => setIsOpen(false)}>

        <Modal.Header>
          <h2>Bienvenue !</h2>
        </Modal.Header>

        <Modal.Body>
          <p>
              Ceci est une modal construite avec le Compound Component
              pattern.
          </p>
          <AccordionDemo />
        </Modal.Body>

        <Modal.Footer>
          <button>Aide !</button>
          <button onClick={() => setIsOpen(false)}>Fermer</button>
          <button onClick={() => alert("Action effectuée !")}>Agir</button>
        </Modal.Footer>
      </Modal>

    </div>
  );
}

export default App;
```

Maintenant, si vous lancez l'application avec ces changements, vous devriez voir l'accordéon apparaître à l'intérieur de la modal. Vous pourrez également afficher/masquer le contenu de l'accordéon et ouvrir/fermer la modal. Cela signifie que leurs états individuels sont intacts comme prévu.

![Accordion](https://cdn.hashnode.com/res/hashnode/image/upload/v1759410454778/69fdcb6a-77a0-42e1-b060-fa2666543c94.png align="center")

## Les cas d'utilisation

Jusqu'à présent, nous avons vu quelques utilisations importantes du pattern Compound Components avec la modal et l'accordéon. De même, vous pouvez utiliser ce pattern pour construire des composants réutilisables tels que :

* Des tableaux (Table.Head, Table.Body, Table.Row).
    
* Tout composant où la mise en page et l'imbrication comptent.
    

De plus, si vous écrivez votre propre bibliothèque de composants ou système de conception, ce pattern est indispensable. Si vous avez besoin d'inspiration, regardez ShadCN, Material UI ou Radix UI. Ils l'utilisent tous.

## Les pièges et anti-patterns

Comme vous le savez, un grand pouvoir implique de grandes responsabilités. Et avec les patterns viennent les pièges et les anti-patterns dont vous devrez être conscient. Lorsque vous utilisez le compound components pattern, assurez-vous de :

* Ne pas attacher de sous-composants au hasard. Ils doivent appartenir au parent sémantiquement.
    
* Éviter de ré-exporter les sous-composants séparément. Ce serait un désastre si quelqu'un utilisait ModalFooter sans Modal. Et si ModalFooter changeait demain dans le contexte de la Modal, alors que les autres consommateurs n'en ont pas besoin ou n'en sont pas conscients ?
    
* Ne pas tenter de tout transformer en compound components pattern. La règle d'or est de ne l'utiliser que lorsque la structure des enfants compte et que vous voulez qu'elle reste flexible.
    

## 15 jours de React Design Patterns

J'ai d'excellentes nouvelles pour vous ! Après l'initiative *40 days of JavaScript*, j'ai maintenant lancé une toute nouvelle initiative appelée [15 Days of React Design Patterns](https://www.youtube.com/playlist?list=PLIJrr73KDmRyQVT__uFZvaVfWPdfyMFHC).

Si vous avez aimé apprendre de cet article, je suis sûr que vous adorerez cette série présentant les 15 patterns de conception React les plus importants. Allez-y et rejoignez-nous.

[![15 Days of React Design Patterns](https://cdn.hashnode.com/res/hashnode/image/upload/v1759482303884/694491a4-2fd9-4515-b595-eafc925d2a18.png align="center")](https://www.youtube.com/playlist?list=PLIJrr73KDmRyQVT__uFZvaVfWPdfyMFHC)

## **Avant de terminer...**

C'est tout ! J'espère que vous avez trouvé cet article instructif.

Restons connectés :

* Abonnez-vous à ma [chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1).
    
* Abonnez-vous à ma newsletter bimensuelle, [The Commit Log](https://tapascript.substack.com/subscribe?utm_medium=fcc).
    
* Suivez-moi sur [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer les conseils quotidiens de montée en compétences.
    
* Rejoignez mon [serveur Discord](https://discord.gg/zHHXx4vc2H), et apprenons ensemble.
    

À bientôt pour mon prochain article. D'ici là, prenez soin de vous et continuez à apprendre.