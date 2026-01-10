---
title: Comment créer un composant modal réutilisable dans React
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2024-09-24T13:17:14.478Z'
originalURL: https://freecodecamp.org/news/create-react-reusable-modal-component
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727021808508/312a7af2-5049-4093-9f58-5ef277986598.png
tags:
- name: React
  slug: reactjs
seo_title: Comment créer un composant modal réutilisable dans React
seo_desc: 'When using React, we strive to create reusable components as much as we
  can to limit the number of components and repetition. This keeps your code “DRY”.

  DRY is a concept you may have come across—it means “Don’t Repeat Yourself”. DRY
  is a coding prin...'
---

En utilisant React, nous nous efforçons de créer des composants réutilisables autant que possible afin de limiter le nombre de composants et la répétition. Cela permet de garder votre code « DRY ».

DRY est un concept que vous avez peut-être rencontré — cela signifie « Don’t Repeat Yourself » (Ne vous répétez pas). DRY est un principe de codage qui vous encourage à minimiser la duplication de code en utilisant des abstractions comme des fonctions ou des modules.

C'est important car cela réduit la redondance, facilite la maintenance du code, améliore la lisibilité et diminue le risque d'erreurs lors des mises à jour.

## Que couvrira cet article ?

Dans cet article, vous apprendrez :

* Comment construire une modale en utilisant React et CSS.
    
* Comment s'assurer que la modale peut être réutilisée dans plusieurs scénarios, contenus et styles.
    
* Comment intégrer l'état et les fonctions de rappel (callback) dans la modale.
    

## Table des matières

* [Que couvrira cet article ?](#heading-que-couvrira-cet-article)
    
* [Le composant modal de base](#heading-le-composant-modal-de-base)
    
* [L'interface des Props](#heading-linterface-des-props)
    
* [Le balisage](#heading-le-balisage)
    
* [React useEffect](#heading-react-useeffect)
    
* [Quand utilisons-nous useEffect ?](#heading-quand-utilisons-nous-useeffect)
    
* [Comment utiliser la modale réutilisable](#heading-comment-utiliser-la-modale-reutilisable)
    
* [Améliorations supplémentaires](#heading-ameliorations-supplementaires)
    
* [Conclusion](#heading-conclusion)
    

## Le composant modal de base

Dans cette section, nous utiliserons React pour construire une bibliothèque de composants. Il existe plusieurs modèles que vous pouvez suivre pour ce faire, mais l'un de mes préférés est le modèle « atomic design ».

```typescript
import React, {useEffect} from 'react';
import './Modal.css'

interface Props {
    open: boolean;
    cancelFn?: () => void;
    primaryFn?: () => void;
    closeIcon?: string;
    content?: React.ReactNode;
    titleContent?: React.ReactNode;
    className?: string;
}

export const Modal: React.FC<Props> = (props) => {
    const {open, cancelFn, primaryFn, closeIcon, titleContent, content} = props;

    // useEffect simple pour capturer la touche Échap afin de fermer la modale 
    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if (e.key === 'Escape' && open) {
                if (cancelFn) {
                    cancelFn();
                }
            }
        };

        document.addEventListener('keydown', handleKeyDown);
        return () => document.removeEventListener('keydown', handleKeyDown);
    }, [open, cancelFn]);


    if (!open) return null;

    return (
        <div className="modalBackground">
            <div className="modalContainer">
                {titleContent && (<div className="title">
                        {titleContent}
                        <div className="titleCloseBtn">
                            <button onClick={cancelFn}>{closeIcon ?? 'X'}</button>
                        </div>
                    </div>
                )}

                <div className="body">
                    {content}
                </div>

                <div className="footer">
                    {secondaryFn && (
                        <button onClick={secondaryFn} id="cancelBtn">
                            Annuler
                        </button>
                    )}
                    {primaryFn && (
                        <button onClick={primaryFn}>Continuer</button>
                    )}
                </div>
            </div>
        </div>

    );
};
```

```scss

.modalBackground {
    width: 100vw;
    height: 100vh;
    background-color: rgb(33, 33, 33, 0.9);
    position: fixed;
    display: flex;
    justify-content: center;
    align-items: center;
}

.modalContainer {
    display: flex;
    flex-direction: column;
    border-radius: 20px;
    background-color: white;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;

}

.modalContainer .title {
    display: flex;
    flex-direction: row;
    text-align: center;
    align-items: center;
    justify-content: space-between;
    padding: 8px;
    border-top-right-radius: 20px;
    border-top-left-radius: 20px;
    background-color: #FFE936;
}

.titleCloseBtn {
    display: flex;
    justify-content: flex-end;
}

.titleCloseBtn button {
    font-size: 0.3rem;
}

.titleCloseBtn button {
    background-color: transparent;
    border: none;
    font-size: 25px;
    cursor: pointer;
}

.modalContainer .body {
    flex: 1;
    padding: 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 1rem;
    text-align: center;
}

.modalContainer .footer {
    display: flex;
    justify-content: center;
    align-items: center;
}

.modalContainer .footer button {
    width: 150px;
    height: 45px;
    margin: 10px;
    border: none;
    background-color: cornflowerblue;
    color: white;
    border-radius: 8px;
    font-size: 20px;
    cursor: pointer;
}

#cancelBtn {
    background-color: crimson;
}
```

Le code ci-dessus est le composant modal de base. Analysons-le.

## L'interface des Props

```typescript
interface Props {
    open: boolean;
    cancelFn?: () => void;
    primaryFn?: () => void;
    closeIcon?: string | React.ReactNode;
    content?: React.ReactNode;
    titleContent?: React.ReactNode;
}
```

Dans cette interface (que nous transmettons au composant `Modal`), nous avons :

* `open` : Une valeur booléenne qui indique si la modale doit être affichée ou non. Un moyen courant d'activer ou de désactiver la modale.
    
* `cancelFn` : Un paramètre optionnel (indiqué par `?`) qui fournit une fonction de rappel pour le moment où le bouton secondaire est pressé. Par exemple, la fonctionnalité « annuler » pour fermer la modale ou annuler une action.
    
* `primaryFn` : Un paramètre optionnel qui fournit une fonction de rappel pour le moment où le bouton principal est pressé. Par exemple, une fonctionnalité « ok », « confirmer » ou « soumettre ».
    
* `closeIcon` : Un paramètre optionnel qui fournit une icône à utiliser comme bouton de fermeture en haut à droite de la modale. Par exemple, vous pourriez utiliser un cercle avec un X dedans, ou une autre forme de bouton.
    
* `content` : Un paramètre optionnel qui fournit le contenu interne de la modale. Cela pourrait être aussi simple qu'une balise `<p/>` ou un élément `<form/>` complet.
    
* `titleContent` : Un paramètre optionnel qui fournit le contenu à placer dans la section titre de la modale. Cela peut aller du texte à une image de logo, tout ce que vous voulez.
    

## Le balisage

Le balisage est assez simple, il y a des `divs` pour chaque section (titre, contenu et actions) ainsi qu'une logique de rendu conditionnel.

À savoir :

```typescript
{titleContent && (
    <div className="title">
        {titleContent}
        <div className="titleCloseBtn">
            <button onClick={secondaryFn}>{closeIcon ?? 'X'}</button>
         </div>
    </div>
)}
```

Nous avons utilisé la syntaxe d'évaluation court-circuit pour vérifier si la propriété `titleContent` est définie par le développeur. Si c'est le cas, le titre de la modale est rendu ; sinon, la section du titre est omise.

Cette approche permet une configuration flexible de la modale, vous permettant d'inclure ou d'exclure facilement des sections comme le titre, le contenu ou les actions.

Par exemple, une modale de confirmation n'aura peut-être besoin que d'un titre comme « Êtes-vous sûr ? » et de boutons d'action comme « Oui » ou « Non », sans aucun contenu supplémentaire.

## React useEffect

Si vous n'êtes pas familier avec `useEffect` et que vous prévoyez d'utiliser React davantage, je vous recommande vivement d'en lire plus [ici](https://react.dev/reference/react/useEffect), car c'est l'un des piliers de l'écosystème de React.

En substance, `useEffect` est comme un assistant qui s'assure que vous faites les choses au bon moment dans votre application.

## Quand utilisons-nous `useEffect` ?

1. Quand vous voulez que quelque chose se produise juste après que votre application soit prête :
    
    * Exemple : Lorsque l'application s'ouvre et que vous souhaitez récupérer des données sur Internet (comme charger des recettes pour votre dîner).
        
2. Quand une variable d'état ou une prop d'entrée change, et que vous voulez faire quelque chose après ce changement.
    
3. Quand votre application se ferme ou se nettoie.
    

Dans notre application React, nous avons créé un Hook `useEffect` qui s'exécute après le chargement de notre composant modal. Le `useEffect` attachera simplement un gestionnaire d'événements `keydown` au `document` (la page/DOM), qui écoutera toutes les touches pressées sur l'écran, puis vérifiera s'il s'agit de la touche `Échap` (ESC).

S'il s'agit de la touche `Échap`, il appellera la fonction `secondaryFn` transmise à la modale. Dans notre cas, c'est la fonction qui ferme la modale. L'instruction `return` supprime le gestionnaire d'événements lors du démontage (lorsque `modalOpen` est `false`).

## Comment utiliser la modale réutilisable

```typescript
import './App.css'
import {useState} from "react";
import {Modal} from "./components/molecules/Modal";

function App() {

    const [modalOpen, setModalOpen] = useState(false);

    return (
        <div className="App">
            <h1>Hé, cliquez sur le bouton pour ouvrir la modale.</h1>
            <button className="openModalBtn" onClick={() => setModalOpen(true)}>
                Ouvrir
            </button>

            <Modal 
                open={modalOpen}
                titleContent={<h1> Fermer </h1>}
                secondaryFn={() => setModalOpen(false)}
                content={
                   <>
                     <h2>Ceci est une modale</h2>
                     <p>Vous pouvez la fermer en appuyant sur la touche Échap, en cliquant sur fermer ou en cliquant à l'extérieur de la modale.</p>
                  </>

               }
           />
        </div>
    );
}

export default App
```

### Analyse

Dans le code ci-dessus, nous avons un composant bouton qui déclenche l'affichage de la modale. Cela se fait en mettant à jour la variable `useState` `modalOpen`. Régler cela sur `true` fera apparaître le composant `Modal`.

Plus bas dans le code, nous avons implémenté le composant `Modal` et transmis les propriétés pertinentes : un titre, un contenu de corps et un bouton secondaire (nous n'avons pas transmis de fonction principale). Cela rend la modale suivante :

![Image: implemented information modal](https://cdn.hashnode.com/res/hashnode/image/upload/v1726519310027/a88f68a8-7bed-49cf-bbd2-ad4b2f5dea05.png align="center")

En utilisant le même composant, nous pouvons également varier et construire une modale de confirmation comme ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1726519756233/e9c2bf7f-0ea1-4656-859e-2a9b90a4418d.png align="center")

Remplaçant l'implémentation de la modale précédente par :

```typescript
<Modal
    open={modalOpen}
    titleContent={<h1> Êtes-vous sûr ? </h1>}
    cancelFn={() => setModalOpen(false)}
    primaryFn={() => {
        alert(" Vous avez tout supprimé ");
        setModalOpen(false);
    }}
    content={
        <>
            <h4>Voulez-vous vraiment tout supprimer ?</h4>
        </>
    }
/>
```

Et voilà, vous avez un composant `Modal` avec des possibilités et des configurations infinies, selon le contenu que vous passez à chaque zone de la modale.

## Améliorations supplémentaires

Il existe quelques améliorations supplémentaires.

### Remplacement des boutons Annuler et Principal

Au lieu de passer les propriétés `cancelFn` et `primaryFn`, vous pouvez passer un composant complet contenant les boutons, ou tout autre composant de pied de page.

Le code mis à jour devrait ressembler à ceci :

```typescript
import React, { useEffect } from 'react';
import './Modal.css';

interface Props {
    open: boolean;
    escFn: () => void;
    closeIcon?: string;
    content?: React.ReactNode;
    titleContent?: React.ReactNode;
    className?: string;
    actions?: React.ReactNode; // Ceci sera utilisé pour passer des boutons ou d'autres actions en tant qu'enfants
}

export const Modal: React.FC<Props> = (props) => {
    const { open, closeIcon, titleContent, content, actions } = props;

    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if (e.key === 'Escape' && open) {
               
            }
        };
        document.addEventListener('keydown', handleKeyDown);
        return () => document.removeEventListener('keydown', handleKeyDown);
    }, [open]);

    if (!open) return null;

    return (
        <div className="modalBackground">
            <div className="modalContainer">
                {titleContent && (
                    <div className="title">
                        {titleContent}
                        <div className="titleCloseBtn">
                            <button>{closeIcon ?? 'X'}</button>
                        </div>
                    </div>
                )}

                <div className="body">
                    {content}
                </div>

                <div className="footer">
                    {actions && actions}
                </div>
            </div>
        </div>
    );
};
```

**Utilisation :**

```typescript
const handleCancel = () => {
    setIsOpen(false);
};

const handleContinue = () => {
    console.log('Action continuer');
};

 <Modal
    open={isOpen}
    titleContent={<h2>Confirmer l'action</h2>}
    content={<p>Êtes-vous sûr de vouloir continuer ?</p>}
    closeIcon="X"
    actions={
        <div className="custom-actions">
           <button onClick={handleCancel}>Annuler</button>
           <button onClick={handleContinue}>Continuer</button>
        </div>
    }
/>
```

Ici, nous passons maintenant les boutons en tant que propriété. Vous pouvez également concevoir la modale pour passer le contenu en tant que composant enfant, mais cela peut devenir confus, car les développeurs pourraient voir cela au premier coup d'œil comme le passage du contenu de la modale, plutôt que de simples éléments de pied de page.

Il y a des avantages et des inconvénients à procéder de cette façon :

**Avantages :**

* **Plus de flexibilité** : Permet de passer toutes sortes d'éléments à la section pied de page. Par exemple, plusieurs boutons CTA (Call To Action), des liens ou tout ce que vous voulez, avec un style personnalisé.
    
* **Séparation des préoccupations :** La modale n'est plus responsable que du rendu du conteneur (mise en page, titre, contenu, etc.). La logique des actions (boutons) à afficher et de leurs comportements est gérée par le composant parent qui rend la modale, ce qui rend le composant modal plus propre et plus réutilisable.
    
* **Réutilisabilité améliorée :** Vous pouvez passer n'importe quel JSX pour les actions, ce qui le rend utilisable pour une variété de cas (par exemple, une modale avec des boutons de soumission de formulaire ou des options multiples). Cette approche est utile lorsque vous avez des modales qui nécessitent différents ensembles de boutons ou d'interactions dépendant d'une autre logique au sein du composant parent/modal. La logique peut être gérée par une fonction de construction, ou au sein d'un autre composant wrapper qui héberge les boutons.
    

**Inconvénients :**

* **Plus de responsabilité sur le composant parent :** Vous devez maintenant gérer les boutons dans chaque instance où vous utilisez `Modal`. Cela peut entraîner une répétition de la logique des boutons (comme `handleCancel` et `handleContinue`) à différents endroits si vous n'y prenez pas garde.
    
* **Utilisation légèrement plus complexe :** L'approche précédente vous permettait de passer `cancelFn` et `primaryFn` directement (optionnellement), ce qui pourrait être plus simple pour la majorité des cas d'utilisation simples. Passer les actions en tant qu'enfants peut nécessiter plus de configuration.
    
* **Mise en page des actions incohérente :** Si vous ne faites pas attention à votre code, vous pourriez vous retrouver avec des placements de boutons ou des styles incohérents entre différentes instances de la modale. Cela peut être géré en s'assurant de toujours passer un balisage ou des styles cohérents lors du passage des actions en tant qu'enfants, mais encore une fois, cela peut devenir difficile à gérer.
    

## Conclusion

Construire un composant modal réutilisable dans React offre une grande flexibilité et une réutilisabilité à travers votre application. Vous pouvez facilement adapter la modale à divers scénarios, qu'il s'agisse d'une simple modale de confirmation ou d'une modale de soumission de formulaire plus complexe.

Cependant, il est essentiel de trouver un équilibre entre flexibilité et simplicité — trop de complexité pourrait surcharger les composants parents avec des répétitions inutiles.

Dans l'ensemble, cette approche garde votre code DRY, améliore la maintenabilité et vous permet de créer des composants UI évolutifs. En appliquant ces pratiques et améliorations, vous pouvez construire des modales hautement adaptables qui répondent à des exigences diverses, améliorant à la fois l'expérience du développeur et la qualité du produit final.

Comme toujours, n'hésitez pas à me suivre ou à me contacter sur [Twitter/X](https://x.com/grantdotdev).