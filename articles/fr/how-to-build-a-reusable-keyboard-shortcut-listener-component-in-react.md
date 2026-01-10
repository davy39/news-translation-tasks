---
title: Comment créer un composant réutilisable d'écouteur de raccourcis clavier dans
  React
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2024-12-16T18:11:42.188Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-reusable-keyboard-shortcut-listener-component-in-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733895763796/17684457-fb85-48d4-b049-ddbaf0b5281e.png
tags:
- name: React
  slug: reactjs
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
seo_title: Comment créer un composant réutilisable d'écouteur de raccourcis clavier
  dans React
seo_desc: Learn to build a reusable keyboard shortcut listener in React with Tailwind
  CSS and Framer Motion for efficient, accessible web apps
---

Si vous êtes comme moi et que vous adorez les raccourcis, vous savez à quel point il est satisfaisant d'appuyer sur quelques touches et de voir la magie opérer. Que ce soit le classique Ctrl+C – Ctrl+V que les développeurs utilisent pour "emprunter du code" 😉 depuis des LLMs et des pages de code, ou les raccourcis personnalisés que nous configurons dans nos outils préférés, les raccourcis clavier font gagner du temps et nous donnent l'impression d'être des magiciens de l'informatique.

Eh bien, ne craignez rien ! J'ai décrypté le code pour créer des composants qui déclenchent et répondent aux raccourcis clavier. Dans cet article, je vais vous apprendre à les créer avec React, Tailwind CSS et Framer Motion.

## Table des matières

Voici tout ce que nous allons couvrir :

* [Prérequis](#heading-prerequisites)
    
* [Qu'est-ce qu'un composant d'écouteur de raccourcis clavier (KSL) ?](#heading-quest-ce-quun-composant-decouteur-de-raccourcis-clavier-ksl)
    
* [Comment construire le composant KSL](#heading-comment-construire-le-composant-ksl)
    
* [Comment créer le composant de révélation](#heading-comment-creer-le-composant-de-revelation)
    
* [Comment déclencher le composant via un raccourci clavier](#heading-comment-declencher-le-composant-via-un-raccourci-clavier)
    
* [Comment animer la visibilité du composant](#heading-comment-animer-la-visibilite-du-composant)
    
* [Comment optimiser votre composant KSL](#heading-comment-optimiser-votre-composant-ksl)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

* Les bases de HTML, CSS et Tailwind CSS
    
* Les bases de JavaScript, React et des hooks React.
    

## Qu'est-ce qu'un composant d'écouteur de raccourcis clavier (KSL) ?

Un **composant d'écouteur de raccourcis clavier (KSLC)** est un composant qui écoute des combinaisons de touches spécifiques et déclenche des actions dans votre application. Il est conçu pour faire en sorte que votre application réponde aux raccourcis clavier, permettant une expérience utilisateur plus fluide et plus efficace.

### Pourquoi est-ce important ?

* **Accessibilité** : Le composant KSL facilite l'utilisation de l'application pour les personnes qui utilisent un clavier, la rendant plus inclusive et facile à utiliser.
    
* **Expérience plus rapide** : Les raccourcis sont rapides et efficaces, permettant aux utilisateurs d'accomplir des tâches en moins de temps. Plus besoin de chercher la souris, il suffit d'appuyer sur une touche (ou deux) et hop, l'action se produit !
    
* **Réutilisabilité** : Une fois que vous avez configuré votre KSL, il peut gérer différents raccourcis dans votre application, ce qui facilite son ajout sans avoir à réécrire la même logique.
    
* **Code plus propre** : Au lieu de disperser les écouteurs d'événements clavier partout, le composant KSL garde les choses bien organisées en centralisant la logique. Votre code reste propre, organisé et plus facile à maintenir.
    

## Comment construire le composant KSL

J'ai préparé un dépôt GitHub avec des [fichiers de démarrage](https://github.com/Daiveedjay/KSL-Component/tree/starter) pour accélérer les choses. Clonez simplement ce dépôt et installez les dépendances.

Pour ce projet, nous utilisons la page d'accueil de Tailwind comme muse et créons la fonctionnalité KSL. Après avoir installé et exécuté la commande de construction, voici à quoi votre page devrait ressembler :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733861510569/fd94572d-e973-4637-ab65-9dd5e944065f.png align="center")

## Comment créer le composant de révélation

Le composant de révélation est le composant que nous voulons afficher lorsque nous utilisons le raccourci.

Pour commencer, créez un fichier appelé `search-box.tsx` et collez ce code :

```javascript
export default function SearchBox() {
  return (
    <div className="fixed top-0 left-0 w-full h-full backdrop-blur-sm bg-slate-900/50 ">
      {" "}
      <div className=" p-[15vh] text-[#939AA7] h-full">
        <div className="max-w-xl mx-auto divide-y divide-[#939AA7] bg-[#1e293b] rounded-md">
          <div className="relative flex justify-between px-4 py-2 text-sm ">
            <div className="flex items-center w-full gap-2 text-white">
              <BiSearch size={20} />
              <input
                type="text"
                className="w-full h-full p-2 bg-transparent focus-within:outline-none"
                placeholder="Rechercher dans la documentation"
              />
            </div>
            <div className="absolute -translate-y-1/2 right-4 top-1/2 ">
              <kbd className="p-1 text-xs rounded-[4px] bg-[#475569] font-sans font-semibold text-slate-400">
                <abbr title="Escape" className="no-underline ">
                  Esc{" "}
                </abbr>{" "}
              </kbd>
            </div>
          </div>
          <div className="flex items-center justify-center p-10 text-center ">
            <h2 className="text-xl">
              Combien de coups de langue faut-il pour atteindre le centre d'une sucette Tootsie ?
            </h2>
          </div>
        </div>
      </div>
    </div>
  );
}
```

D'accord, alors que se passe-t-il dans ce code ?

1. **Calque principal (**`<div className="fixed top-0 left-0 ...">`)
    
    * Il s'agit du calque plein écran qui assombrit l'arrière-plan.
        
    * Le `backdrop-blur-sm` ajoute un flou subtil à l'arrière-plan, et `bg-slate-900/50` lui donne un calque sombre semi-transparent.
        
2. **Conteneur de la boîte de recherche (**`<div className="p-[15vh] ...">`)
    
    * Le contenu est centré à l'aide de la marge intérieure et des utilitaires flex.
        
    * Le `max-w-xl` garantit que la boîte de recherche reste dans une largeur raisonnable pour une bonne lisibilité.
        

Ensuite, dans votre `App.tsx`, créez un état qui affiche dynamiquement ce composant :

```javascript
const [isOpen, setIsOpen] = useState<boolean>(false);
```

* `useState` : Ce hook initialise `isOpen` à `false`, ce qui signifie que la boîte de recherche est masquée par défaut.
    
* Lorsque `isOpen` est défini sur `true`, le composant `SearchBox` sera rendu à l'écran.
    

Et rendez le composant de recherche :

```javascript
  {isOpen && <SearchBox />}
```

Pour afficher le composant de recherche, ajoutez une fonction de basculement au bouton d'entrée :

```javascript
<button
  type="button"
  className="items-center hidden h-12 px-4 space-x-3 text-left rounded-lg shadow-sm sm:flex w-72 ring-slate-900/10 focus:outline-none hover:ring-2 hover:ring-sky-500 focus:ring-2 focus:ring-sky-500 bg-slate-800 ring-0 text-slate-300 highlight-white/5 hover:bg-slate-700"
  onClick={() => setIsOpen(true)}>
  <BiSearch size={20} />
  <span className="flex-auto">Recherche rapide...</span>
   <kbd className="font-sans font-semibold text-slate-500">
   <abbr title="Control" className="no-underline text-slate-500">
    Ctrl{" "}
    </abbr>{" "}
    K
   </kbd>
</button>
```

L'événement `onClick` définit `isOpen` sur `true`, affichant ainsi la `SearchBox`.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733861855356/87adf797-9378-4f2f-bae4-d1b45f6122d2.gif align="center")

Mais comme vous l'avez vu, cela a été déclenché par une action de clic, et non par une action de raccourci clavier. Faisons cela ensuite.

## Comment déclencher le composant via un raccourci clavier

Pour faire en sorte que le composant de révélation s'ouvre et se ferme à l'aide d'un raccourci clavier, nous allons utiliser un hook `useEffect` pour écouter des combinaisons de touches spécifiques et mettre à jour l'état du composant en conséquence.

### Étape 1 : Écouter les événements clavier

Ajoutez un hook `useEffect` dans votre fichier `App.tsx` pour écouter les pressions de touches :

```javascript
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.ctrlKey && event.key === Key.K) {
        event.preventDefault(); // Empêcher le comportement par défaut du navigateur
       
      }    };

    window.addEventListener("keydown", handleKeyDown);
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);
```

Que se passe-t-il dans ce code ?

1. **Configuration de l'effet (**`useEffect`)
    
    * `useEffect` garantit que l'écouteur d'événements pour les pressions de touches est ajouté lorsque le composant est monté et nettoyé lorsque le composant est démonté, évitant ainsi les fuites de mémoire.
        
2. **Combinaison de touches (**`event.ctrlKey && event.key === "k"`)
    
    * Le `event.ctrlKey` vérifie si la touche **Contrôle** est enfoncée.
        
    * Le `event.key === "k"` garantit que nous écoutons spécifiquement la touche "K". Ensemble, cela vérifie si la combinaison **Ctrl + K** est enfoncée.
        
3. **Empêcher le comportement par défaut (**`event.preventDefault()`)
    
    * Certains navigateurs peuvent avoir des comportements par défaut liés aux combinaisons de touches comme **Ctrl + K** (par exemple, mettre le focus sur la barre d'adresse du navigateur). L'appel de `preventDefault` arrête ce comportement.
        
4. **Nettoyage de l'événement (**`return () => ...`)
    
    * La fonction de nettoyage supprime l'écouteur d'événements pour éviter que des écouteurs dupliqués ne soient ajoutés si le composant est rendu à nouveau.
        

### Étape 2 : Basculer la visibilité du composant

Ensuite, mettez à jour la fonction `handleKeyDown` pour basculer la visibilité de la `SearchBox` lorsque le raccourci est pressé :

```javascript
useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      // Écouter Ctrl + K
      if (event.ctrlKey && event.key === Key.K) {
        event.preventDefault(); // Empêcher le comportement par défaut du navigateur
        setIsOpen((prev) => !prev); // Basculer la boîte de recherche
      } else if (event.key === Key.Escape) {
        setIsOpen(false); // Fermer la boîte de recherche
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);
```

Que se passe-t-il dans ce code ?

1. **Basculer l'état** (`setIsOpen((prev) => !prev)`)
    
    * Lorsque **Ctrl + K** est pressé, le `setIsOpen` bascule la visibilité de la `SearchBox`.
        
    * L'argument `prev` représente l'état précédent. L'utilisation de `!prev` inverse sa valeur :
        
        * `true` (ouvert) devient `false` (fermé).
            
        * `false` (fermé) devient `true` (ouvert).
            
2. **Fermer avec la touche Échap** (`event.key === "Escape"`)
    
    * Lorsque la touche **Échap** est pressée, `setIsOpen(false)` définit explicitement l'état sur `false`, fermant ainsi la `SearchBox`.
        

Cela donne le résultat suivant :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733861983226/9c6ff7ef-a067-42c9-b6c7-afd35955731e.gif align="center")

## Comment animer la visibilité du composant

Pour l'instant, notre composant fonctionne, mais il manque un peu de style, n'est-ce pas ? Changeons cela.

### Étape 1 : Créer le composant de superposition

Nous allons commencer par créer un **composant de superposition**, qui agit comme l'arrière-plan sombre et flou pour la boîte de recherche. Voici la version de base :

```javascript
import { ReactNode } from "react";

export default function OverlayWrapper({ children }: { children: ReactNode }) {
  return (
    <div
      className="fixed top-0 left-0 w-full h-full backdrop-blur-sm bg-slate-900/50 ">
      {children}
    </div>
  );
}
```

### Étape 2 : Ajouter des animations à la superposition

Maintenant, faisons en sorte que la superposition s'estompe avec Framer Motion. Mettez à jour le composant `OverlayWrapper` comme ceci :

```javascript
import { motion } from "framer-motion";
import { ReactNode } from "react";

export default function OverlayWrapper({ children }: { children: ReactNode }) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed top-0 left-0 w-full h-full backdrop-blur-sm bg-slate-900/50 ">
      {children}
    </motion.div>
  );
}
```

##### Principales propriétés d'animation :

* `initial` : Définit l'état de départ lorsque le composant est monté (totalement transparent).
    
* `animate` : Définit l'état vers lequel animer (totalement opaque).
    
* `exit` : Spécifie l'animation lorsque le composant est démonté (fondu au noir).
    

### Étape 3 : Animer la boîte de recherche

Ensuite, ajoutons du mouvement à la boîte de recherche elle-même. Nous allons la faire glisser et apparaître lorsqu'elle apparaît et glisser hors de l'écran lorsqu'elle disparaît.

```javascript
import { motion } from "framer-motion";
import { BiSearch } from "react-icons/bi";
import OverlayWrapper from "./overlay";

export default function SearchBox() {
  return (
    <OverlayWrapper>
      <motion.div
        initial={{ y: "-10%", opacity: 0 }}
        animate={{ y: "0%", opacity: 1 }}
        exit={{ y: "-5%", opacity: 0 }}
        className=" p-[15vh] text-[#939AA7] h-full">
        <div
          className="max-w-xl mx-auto divide-y divide-[#939AA7] bg-[#1e293b] rounded-md"
        >
          <div className="relative flex justify-between px-4 py-2 text-sm ">
            <div className="flex items-center w-full gap-2 text-white">
              <BiSearch size={20} />
              <input
                type="text"
                className="w-full h-full p-2 bg-transparent focus-within:outline-none"
                placeholder="Rechercher dans la documentation"
              />
            </div>
            <div className="absolute -translate-y-1/2 right-4 top-1/2 ">
              <kbd className="p-1 text-xs rounded-[4px] bg-[#475569] font-sans font-semibold text-slate-400">
                <abbr title="Escape" className="no-underline ">
                  Esc{" "}
                </abbr>{" "}
              </kbd>
            </div>
          </div>
          <div className="flex items-center justify-center p-10 text-center ">
            <h2 className="text-xl">
              Combien de coups de langue faut-il pour atteindre le centre d'une sucette Tootsie ?
            </h2>
          </div>
        </div>
      </motion.div>
    </OverlayWrapper>
  );
}
```

### Étape 4 : Activer le suivi des animations avec `AnimatePresence`

Enfin, enveloppez votre logique de rendu conditionnel dans le composant `AnimatePresence` fourni par **Framer Motion**. Cela garantit que Framer Motion suit lorsque les éléments entrent et sortent du DOM.

```javascript
<AnimatePresence>{isOpen && <SearchBox />}</AnimatePresence>
```

Cela permet à Framer Motion de suivre lorsqu'un élément entre et sort du DOM. Avec cela, nous obtenons le résultat suivant :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733862299745/e4c9858c-d10a-4817-bf41-697fa103d096.gif align="center")

Ah, c'est bien mieux !

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733862351332/a1888e83-8df6-45cc-80c4-db1e2e8e7025.gif align="center")

## Comment optimiser votre composant KSL

Si vous pensiez que nous avions terminé, pas si vite... Nous avons encore un peu de travail à faire.

Nous devons optimiser pour l'accessibilité. Nous devons ajouter un moyen pour les utilisateurs de fermer le composant de recherche avec une souris, car l'accessibilité est très importante.

Pour ce faire, commencez par créer un hook appelé `useClickOutside`. Ce hook utilise un élément de référence pour savoir quand un utilisateur clique en dehors de l'élément cible (boîte de recherche), ce qui est un comportement très populaire pour fermer les modales et les KSLC.

```javascript

import { useEffect } from "react";

type ClickOutsideHandler = (event: Event) => void;

export const useClickOutside = (
  ref: React.RefObject<HTMLElement>,
  handler: ClickOutsideHandler
) => {
  useEffect(() => {
    const listener = (event: Event) => {
      // Ne rien faire si l'on clique sur l'élément ou ses descendants
      if (!ref.current || ref.current.contains(event.target as Node)) return;

      handler(event);
    };

    document.addEventListener("mousedown", listener);
    document.addEventListener("touchstart", listener);

    return () => {
      document.removeEventListener("mousedown", listener);
      document.removeEventListener("touchstart", listener);
    };
  }, [ref, handler]);
};
```

Pour utiliser ce hook, passez la fonction responsable de l'ouverture et de la fermeture du composant de recherche :

```javascript
<AnimatePresence> {isOpen && <SearchBox close={setIsOpen} />} </AnimatePresence>
```

Ensuite, recevez la fonction dans la recherche avec son type de prop approprié :

```javascript
export default function SearchBox({
  close,
}: {
  close: React.Dispatch<React.SetStateAction<boolean>>;
}) {
```

Après cela, créez une référence (ref) à l'élément que vous souhaitez suivre et marquez cet élément :

```javascript
import { motion } from "framer-motion";
import { useRef } from "react";
import { BiSearch } from "react-icons/bi";
import { useClickOutside } from "../hooks/useClickOutside";
import OverlayWrapper from "./overlay";

export default function SearchBox({
  close,
}: {
  close: React.Dispatch<React.SetStateAction<boolean>>;
}) {
  const searchboxRef = useRef<HTMLDivElement>(null);
  return (
    <OverlayWrapper>
      <motion.div
        initial={{ y: "-10%", opacity: 0 }}
        animate={{ y: "0%", opacity: 1 }}
        exit={{ y: "-5%", opacity: 0 }}
        className=" p-[15vh] text-[#939AA7] h-full">
        <div
          className="max-w-xl mx-auto divide-y divide-[#939AA7] bg-[#1e293b] rounded-md"
          ref={searchboxRef}>
          <div className="relative flex justify-between px-4 py-2 text-sm ">
            <div className="flex items-center w-full gap-2 text-white">
              <BiSearch size={20} />
              <input
                type="text"
                className="w-full h-full p-2 bg-transparent focus-within:outline-none"
                placeholder="Rechercher dans la documentation"
              />
            </div>
            <div className="absolute -translate-y-1/2 right-4 top-1/2 ">
              <kbd className="p-1 text-xs rounded-[4px] bg-[#475569] font-sans font-semibold text-slate-400">
                <abbr title="Escape" className="no-underline ">
                  Esc{" "}
                </abbr>{" "}
              </kbd>
            </div>
          </div>
          <div className="flex items-center justify-center p-10 text-center ">
            <h2 className="text-xl">
              Combien de coups de langue faut-il pour atteindre le centre d'une sucette Tootsie ?
            </h2>
          </div>
        </div>
      </motion.div>
    </OverlayWrapper>
  );
}
```

Ensuite, passez cette référence et la fonction à appeler lorsqu'un clic en dehors de cet élément est détecté.

```javascript
useClickOutside(searchboxRef, () => close(false));
```

En le testant maintenant, nous obtenons le résultat suivant :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733862607091/5c77d8e0-6ba8-4c04-8d7d-c0d0d8f7c408.gif align="center")

Nous pouvons également optimiser un peu plus le code. Comme nous l'avons fait avec la fonctionnalité d'accessibilité, nous pouvons rendre notre écouteur de détection de raccourcis beaucoup plus propre et efficace avec les étapes suivantes.

Tout d'abord, créez un fichier de hook `useKeyBindings` pour gérer les combinaisons de touches pressées.

Ensuite, définissez le hook et l'interface. Le hook acceptera un tableau de liaisons, où chaque liaison se compose de :

* Un tableau `keys`, qui spécifie la combinaison de touches (par exemple, ["Control", "k"])
    
* Une fonction de rappel, qui est appelée lorsque les touches correspondantes sont pressées.
    

```javascript
import { useEffect } from "react";

// Définir la structure d'une liaison de touches
interface KeyBinding {
  keys: string[]; // Tableau de touches (par exemple, ["Control", "k"])
  callback: () => void; // Fonction à exécuter lorsque les touches sont pressées
}

export const useKeyBindings = (bindings: KeyBinding[]) => {
 
};
```

Ensuite, créez la fonction `handleKeyDown`. À l'intérieur du hook, définissez une fonction qui écoutera les événements clavier. Cette fonction vérifiera si les touches pressées correspondent à une combinaison de touches définie.

Nous allons normaliser les touches en minuscules afin que la comparaison soit insensible à la casse et suivre les touches pressées en vérifiant `ctrlKey`, `shiftKey`, `altKey`, `metaKey` et la touche pressée (par exemple, "k" pour Ctrl + K).

```javascript
const handleKeyDown = (event: KeyboardEvent) => {
  // Suivre les touches qui sont pressées
  const pressedKeys = new Set<string>();

  // Vérifier les touches modificatrices (Ctrl, Shift, Alt, Meta)
  if (event.ctrlKey) pressedKeys.add("control");
  if (event.shiftKey) pressedKeys.add("shift");
  if (event.altKey) pressedKeys.add("alt");
  if (event.metaKey) pressedKeys.add("meta");

  // Ajouter la touche qui a été pressée (par exemple, "k" pour Ctrl + K)
  if (event.key) pressedKeys.add(event.key.toLowerCase());
};
```

Ensuite, nous allons comparer les touches pressées avec le tableau de touches de nos liaisons pour vérifier si elles correspondent. Si elles correspondent, nous allons appeler la fonction de rappel associée. Nous veillons également à ce que le nombre de touches pressées corresponde au nombre de touches définies dans la liaison.

```javascript
// Parcourir chaque liaison de touches
bindings.forEach(({ keys, callback }) => {
  // Normaliser les touches en minuscules pour la comparaison
  const normalizedKeys = keys.map((key) => key.toLowerCase());

  // Vérifier si les touches pressées correspondent à la liaison de touches
  const isMatch =
    pressedKeys.size === normalizedKeys.length &&
    normalizedKeys.every((key) => pressedKeys.has(key));

  // Si les touches correspondent, appeler le rappel
  if (isMatch) {
    event.preventDefault(); // Empêcher le comportement par défaut du navigateur
    callback(); // Exécuter la fonction de rappel
  }
});
```

Enfin, configurez les écouteurs d'événements sur l'objet window pour écouter les événements keydown. Ces écouteurs déclencheront la fonction `handleKeyDown` chaque fois qu'une touche est pressée. Assurez-vous d'ajouter le nettoyage des écouteurs d'événements lorsque le composant est démonté.

```javascript
useEffect(() => {
  // Ajouter des écouteurs d'événements pour keydown
  window.addEventListener("keydown", handleKeyDown);

  // Nettoyer les écouteurs d'événements lorsque le composant est démonté
  return () => {
    window.removeEventListener("keydown", handleKeyDown);
  };
}, [bindings]);
```

Le hook `useKeyBindings` complet maintenant assemblé ressemble à ceci :

```javascript
import { useEffect } from "react";

interface KeyBinding {
  keys: string[]; // Une combinaison de touches pour déclencher le rappel (par exemple, ["Control", "k"])
  callback: () => void; // La fonction à exécuter lorsque les touches sont pressées
}

export function useKeyBindings(bindings: KeyBinding[]) {
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      bindings.forEach(({ keys, callback }) => {
        const normalizedKeys = keys.map((key) => key.toLowerCase());
        const pressedKeys = new Set<string>();

        // Suivre les touches modificatrices explicitement
        if (event.ctrlKey) pressedKeys.add("control");
        if (event.shiftKey) pressedKeys.add("shift");
        if (event.altKey) pressedKeys.add("alt");
        if (event.metaKey) pressedKeys.add("meta");

        // Ajouter la touche réelle pressée
        if (event.key) pressedKeys.add(event.key.toLowerCase());

        // Correspondance exacte : les touches pressées doivent correspondre aux touches définies
        const isExactMatch =
          pressedKeys.size === normalizedKeys.length &&
          normalizedKeys.every((key) => pressedKeys.has(key));

        if (isExactMatch) {
          event.preventDefault(); // Empêcher le comportement par défaut
          callback(); // Exécuter le rappel
        }
      });
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [bindings]);
}
```

Voici comment vous pouvez utiliser ce hook dans votre `App` :

```javascript
import { useKeyBindings } from "./hooks/useKeyBindings";

export default function App() {
  const [isOpen, setIsOpen] = useState<boolean>(false);

  useKeyBindings([
    {
      keys: ["Control", "k"], // Écouter "Ctrl + K"
      callback: () => setIsOpen((prev) => !prev), // Basculer la boîte de recherche
    },
    {
      keys: ["Escape"], // Écouter "Escape"
      callback: () => setIsOpen(false), // Fermer la boîte de recherche
    },
  ]);
```

Ce qui donne le résultat suivant :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733863013736/620e7362-33fa-45d3-b2e0-4c8afc873cfd.gif align="center")

Avec cette approche, vous pouvez même ajouter plusieurs raccourcis pour déclencher la visibilité du composant de recherche.

```javascript
useKeyBindings([
    {
      keys: ["Control", "k"], // Écouter "Ctrl + K"
      callback: () => setIsOpen((prev) => !prev), // Basculer la boîte de recherche
    },
    {
      keys: ["Control", "d"], // Écouter "Ctrl + D"
      callback: () => setIsOpen((prev) => !prev), // Basculer la boîte de recherche
    },
    {
      keys: ["Escape"], // Écouter "Escape"
      callback: () => setIsOpen(false), // Fermer la boîte de recherche
    },
  ]);
```

Voici les liens vers toutes les ressources dont vous pourriez avoir besoin pour cet article :

* [Fichiers de démarrage](https://github.com/Daiveedjay/KSL-Component/tree/starter)
    
* [Version finale](https://github.com/Daiveedjay/KSL-Component/tree/main)
    

## Conclusion

J'espère que cet article a été comme un raccourci bien synchronisé, vous menant directement au cœur de la création de composants de raccourcis clavier réutilisables. Avec chaque pression de touche et animation, vous pouvez maintenant transformer des expériences web ordinaires en expériences extraordinaires.

J'espère que vos raccourcis vous aideront à créer des applications qui cliquent avec vos utilisateurs. Après tout, les meilleurs voyages commencent souvent avec la bonne combinaison.

### Vous aimez mes articles ?

N'hésitez pas à [m'offrir un café ici](https://www.buymeacoffee.com/JajaDavid), pour garder mon cerveau en marche et fournir plus d'articles comme celui-ci.

![coffee-tom](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdVWaSayW-ZONciTLakWFfSKvOKoaQR3MTpyGmLR77hl58lDorTCRNfOZfP-dMf-2WcIwfSWZE_psVHr-4qU1CIy28hsLj755zJdEcsLp3blw6l1Wtu4EUxTZ8mSF--dCk6mEQRWg?key=ypBQIzv1TD8iWEKblpAC4CZM align="left")

### Informations de contact

Vous souhaitez me contacter ou me connecter ? N'hésitez pas à me contacter sur les plateformes suivantes :

* Twitter / X : [@jajadavid8](https://twitter.com/JajaDavid8)
    
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
    
* Email : [Jajadavidjid@gmail.com](http://Jajadavidjid@gmail.com)