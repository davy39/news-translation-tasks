---
title: Comment utiliser des composants UI non stylisés – Guide pour les développeurs
  Front-End
subtitle: ''
author: 'Chinenye Anikwenze '
co_authors: []
series: null
date: '2023-08-29T15:56:00.000Z'
originalURL: https://freecodecamp.org/news/unstyled-ui-components-for-front-end-developers
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/article
seo_title: Comment utiliser des composants UI non stylisés – Guide pour les développeurs
  Front-End
---

unstyled-ui-components-2.png
étiquettes:
- nom: Accessibilité
  slug: accessibilite
- nom: Développement Front-end
  slug: developpement-front-end
- nom: Conception UI
  slug: conception-ui
- nom: Interface Utilisateur
  slug: interface-utilisateur
- nom: Développement Web
  slug: developpement-web
seo_title: null
seo_desc: "Imaginez cette situation : vous travaillez sur un projet sensible au temps, et vous devez implémenter certains composants UI spécifiques qui respectent les meilleures pratiques d'accessibilité. \nVous connaissez peut-être certaines bibliothèques remplies d'éléments UI préconçus, chacun avec leur propre style. Mais voici le problème – vous n'avez peut-être besoin que d'une poignée de ces composants. Alors pourquoi alourdir votre application ? En réalité, une partie significative des styles regroupés pourrait rester inutilisée. \nNe vous inquiétez pas – c'est là que les composants UI **non stylisés** entrent en jeu."
---

Imaginez cette situation : vous travaillez sur un projet sensible au temps, et vous devez implémenter certains composants UI spécifiques qui respectent les meilleures pratiques d'accessibilité. 

Vous connaissez peut-être certaines bibliothèques remplies d'éléments UI préconçus, chacun avec leur propre style. Mais voici le problème – vous n'avez peut-être besoin que d'une poignée de ces composants. Alors pourquoi alourdir votre application ? En réalité, une partie significative des styles regroupés pourrait rester inutilisée. 

Ne vous inquiétez pas – c'est là que les composants UI **non stylisés** entrent en jeu.

## Qu'est-ce que les composants UI non stylisés ?

Les composants UI non stylisés sont des blocs de construction UI accessibles sans styles prédéfinis. Cela vous donne une autorité sans égale sur la présentation visuelle et le comportement de ces interfaces. 

Le terme « **non stylisé** » ne signifie pas un manque de design – plutôt, il fait référence à une page blanche qui vous permet d'infuser votre créativité et votre marque sans les limitations qui accompagnent les éléments UI traditionnels. 

Cela vous permet d'adapter les composants aux besoins distincts de votre application, tout en priorisant l'esthétique et l'accessibilité.

## Avantages des composants UI non stylisés

Explorons les caractéristiques clés qui distinguent les composants non stylisés et découvrons pourquoi ils pourraient être indispensables pour vos projets à venir.

### Contrôle sur l'apparence visuelle et la fonctionnalité :

Les bibliothèques UI conventionnelles ont des styles prédéfinis qui pourraient ne pas correspondre à votre design ou à votre esthétique. 

Prenons cet exemple : vous travaillez sur une plateforme de commerce électronique qui nécessite un catalogue de produits. Avec des composants UI non stylisés, vous pouvez ajuster l'apparence de chaque carte de produit, les effets de survol et les interactions pour refléter l'identité de votre marque. 

Cette liberté s'étend aux couleurs, à la typographie et aux choix de mise en page, résultant en une expérience cohérente et captivante unique à votre application.

### Réduction des surcharges et amélioration des performances :

Souvent, dans les projets personnels, nous n'avons besoin que de quelques composants parmi des bibliothèques étendues. Mais l'incorporation de ces bibliothèques peut introduire des styles et des éléments inutiles qui ralentissent les choses. 

Les composants non stylisés résolvent ce problème en vous permettant d'inclure uniquement ce dont vous avez besoin. Cela accélère votre application, la rendant plus légère et plus efficace, sans dépendances inutiles.

### Flexibilité pour la personnalisation

Les composants non stylisés vous permettent de créer des éléments parfaitement adaptés aux exigences de votre projet. Cela couvre leur apparence, leurs mouvements et leurs réactions aux interactions des utilisateurs. 

Que vous construisiez un simple formulaire ou une fonctionnalité interactive complexe, les composants non stylisés vous donnent la liberté de façonner chaque détail pour qu'il corresponde à votre design et à votre objectif, en harmonie avec le style global de votre application.

### Accessibilité et convivialité

Créer des interfaces accessibles qui respectent les principes de [conception WAI-ARIA](https://www.w3.org/WAI/standards-guidelines/aria/) est important pour les développeurs. Les composants UI non stylisés, souvent conçus avec l'accessibilité en tête, offrent une utilité améliorée pour un spectre plus large d'utilisateurs. Cette abstraction élimine l'implémentation manuelle.

### Développement prêt pour l'avenir

La technologie évolue, tout comme les tendances de design et les attentes des utilisateurs. Les composants non stylisés garantissent que vous êtes prêt pour ce qui vous attend. Les intégrer vous permet d'adapter l'apparence et la sensation de votre application à mesure que les tendances changent, sans être limité par des styles obsolètes.

### Architecture modulaire et évolutive

Les composants non stylisés ressemblent à des blocs de construction qui s'intègrent parfaitement dans votre projet. Cela simplifie votre code et le rend plus facile à gérer. Cela vous permet également de réutiliser ces blocs dans différentes sections de l'application, économisant du temps tout en préservant la cohérence à mesure que votre projet s'étend.

## Exploration des composants UI non stylisés populaires 

Pour vous donner plus de contexte sur le fonctionnement des composants non stylisés, nous allons maintenant comparer les composants modaux de cinq bibliothèques courantes de composants UI non stylisés. 

Pour la plupart de ces composants, les composants Dialog facilitent la création de boîtes modales interactives et visuellement attrayantes pour des actions comme l'édition de profil, la confirmation de décisions ou l'affichage d'informations supplémentaires sans naviguer loin du contenu principal. 

Je vais également décrire les fonctionnalités globales de ces bibliothèques de composants afin que vous puissiez les intégrer dans vos futurs projets.

Explorons maintenant une sélection des bibliothèques de composants UI non stylisés les plus notables et examinons leurs composants de dialogue.

### Radix UI

Le composant Dialog de Radix UI, que vous pouvez trouver dans le package `@radix-ui/react-dialog`, est un outil polyvalent qui vous aide à créer des fenêtres contextuelles dans vos applications React. Il vous permet d'interagir avec certaines zones de votre programme sans quitter l'écran actuel.

Vous pouvez créer de nombreux types de fenêtres contextuelles, y compris celles qui arrêtent le flux (modales) et celles qui ne le font pas (non modales). 

Pour concevoir des dialogues complets, vous disposez de nombreux éléments de construction, notamment `Trigger`, `Portal`, `Overlay`, `Content`, `Title`, `Description` et `Close`. Vous pouvez le styliser pour qu'il corresponde à votre design. Il respecte également les exigences d'accessibilité afin que tout le monde puisse l'utiliser.

Lorsque vous appuyez sur la touche `Escape` ou cliquez sur le bouton `fermer`, le dialogue se ferme. Pour les utilisateurs de lecteurs d'écran, des composants spéciaux tels que `Title` et `Description` sont disponibles.

La documentation est extensive et fournit des exemples pour plusieurs scénarios et elle fonctionne bien avec l'écosystème React.

#### Exemple de code de Radix :

Pour commencer avec Radix, vous pouvez exécuter cette commande dans votre terminal :

`npm install @radix-ui/react-popover@latest -E`  
  
Pour utiliser le composant de dialogue, vous pouvez importer les composants comme suit :

```
import React from 'react';
import * as Dialog from '@radix-ui/react-dialog';

const DialogComponent = () => (
  <Dialog.Root>
    <Dialog.Trigger asChild>
      <button>Ouvrir le profil</button>
    </Dialog.Trigger>
    <Dialog.Portal>
      <Dialog.Overlay className="DialogOverlay" />
      <Dialog.Content className="DialogContent">
        <Dialog.Title className="DialogTitle">Modifier le profil</Dialog.Title>
        <Dialog.Description className="DialogDescription">
          Apportez des modifications à votre profil ici. Cliquez sur enregistrer lorsque vous avez terminé.
        </Dialog.Description>
        <fieldset>
          <label className="Label" htmlFor="name">
            Nom
          </label>
          <input className="Input" id="name" defaultValue="Chinenye A" />
        </fieldset>
        <fieldset className="Fieldset">
          <label className="Label" htmlFor="username">
            Nom d'utilisateur
          </label>
          <input className="Input" id="username" defaultValue="@chinenye" />
        </fieldset>
        <div style={{ display: 'flex', marginTop: 25, justifyContent: 'flex-end' }}>
          <Dialog.Close asChild>
            <button className="Button green">Enregistrer les modifications</button>
          </Dialog.Close>
        </div>
        <Dialog.Close asChild>
          <button className="IconButton" aria-label="Fermer">
         Bouton
          </button>
        </Dialog.Close>
      </Dialog.Content>
    </Dialog.Portal>
  </Dialog.Root>
);

export default DialogComponent;
```

Voici à quoi cela ressemble :

![L'image montre une fenêtre modale contextuelle avec un formulaire. La modale est une carte placée au centre de l'écran](https://www.freecodecamp.org/news/content/images/2023/08/radix-modal.jpg)
_Écran modal du composant de dialogue de Radix UI_

Pour en savoir plus sur Radix et ses autres composants, [vous pouvez consulter leur documentation ici](https://www.radix-ui.com/primitives/docs/components/dialog).

### Composant UI de shadcn

Les composants UI de shadcn, basés sur Radix UI et Tailwind CSS, offrent une expérience utilisateur fluide et intégrée. 

shadcn est efficace et léger car vous pouvez installer uniquement les composants dont vous avez besoin. Il prend en charge deux types de fenêtres contextuelles : 

1. Celles qui nécessitent une réponse avant de se fermer `Alert Dialog`  
2. Celles qui ne le font pas (ce qui est utile pour afficher des messages)

Le composant UI de shadcn est polyvalent car vous pouvez superposer du contenu sur l'écran principal ou une autre fenêtre contextuelle. Il est simple à utiliser pour les utilisateurs de clavier et de lecteurs d'écran également.

Pour rendre vos fenêtres contextuelles plus attrayantes visuellement, vous pouvez appliquer des effets comme le fondu, le glissement ou le zoom. Vous pouvez combiner cela avec des menus tels que les Menus Contextuels ou les Menus Déroulants (également partie des composants Shadcn) pour augmenter la fonctionnalité.

Les composants pour le dialogue sont divisés en sections comme `DialogTrigger`, `DialogContent`, `DialogHeader`, entre autres pour une implémentation plus simple.

#### Exemple de code de shadcn :

Pour commencer, vous pouvez installer le composant de dialogue shadcn en exécutant   
`npx shadcn-ui@latest add dialog`.  
  
Pour utiliser le composant dans vos projets, vous pouvez les importer comme ceci :

```
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"

<Dialog>
  <DialogTrigger>Ouvrir</DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Êtes-vous absolument sûr ?</DialogTitle>
      <DialogDescription>
        Cette action ne peut pas être annulée. Cela supprimera définitivement votre compte
        et supprimera vos données de nos serveurs.
      </DialogDescription>
    </DialogHeader>
  </DialogContent>
</Dialog>


```

Et voici le résultat du code ci-dessus :

![Cet écran montre une modale ](https://www.freecodecamp.org/news/content/images/2023/08/screencapture-ui-shadcn-docs-components-dialog-2023-08-26-07_47_54.png)
_Affichage du dialogue Shadcn_

[Vous pouvez lire leur documentation pour d'autres cas d'utilisation](https://ui.shadcn.com/docs/components/dialog).

### Bibliothèque Headless UI :

La bibliothèque Headless UI offre une approche entièrement gérée et flexible pour construire des fenêtres modales. Vous pouvez l'utiliser dans les applications React et Vue. 

La bibliothèque vous permet de personnaliser les fenêtres contextuelles pour qu'elles correspondent à l'apparence et à la sensation de votre programme. Elle dispose également de fonctionnalités d'accessibilité intégrées, la rendant utilisable par les utilisateurs de clavier et de lecteurs d'écran.

Pour adapter l'apparence de votre application, vous pouvez styliser les composants `Dialog` et `Dialog.Panel` avec `className` ou `style props`. Le `Dialog.Panel` peut avoir une superposition ou un arrière-plan qui peut être animé individuellement pour attirer l'attention. Il vous permet d'utiliser CSS pour construire des dialogues défilables.

La bibliothèque offre des transitions fluides lors de l'ouverture et de la fermeture des fenêtres contextuelles, ce qui améliore l'expérience visuelle.

#### Exemple de code de Headless UI :

Pour commencer avec cette bibliothèque, vous pouvez exécuter cette commande pour l'installer :  
`npm install @headlessui/react`.  
  
Vous pouvez utiliser les composants de dialogue comme illustré ci-dessous :

```
import { Dialog, Transition } from '@headlessui/react'
import { Fragment, useState } from 'react'

export default function MyModal() {
  let [isOpen, setIsOpen] = useState(true)

  function closeModal() {
    setIsOpen(false)
  }

  function openModal() {
    setIsOpen(true)
  }

  return (
    <>
      <div className="fixed inset-0 flex items-center justify-center">
        <button
          type="button"
          onClick={openModal}
          className="rounded-md bg-black bg-opacity-20 px-4 py-2 text-sm font-medium text-white hover:bg-opacity-30 focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
        >
          Ouvrir le dialogue
        </button>
      </div>

      <Transition appear show={isOpen} as={Fragment}>
        <Dialog as="div" className="relative z-10" onClose={closeModal}>
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black bg-opacity-25" />
          </Transition.Child>

          <div className="fixed inset-0 overflow-y-auto">
            <div className="flex min-h-full items-center justify-center p-4 text-center">
              <Transition.Child
                as={Fragment}
                enter="ease-out duration-300"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-200"
                leaveFrom="opacity-100 scale-100"
                leaveTo="opacity-0 scale-95"
              >
                <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all">
                  <Dialog.Title
                    as="h3"
                    className="text-lg font-medium leading-6 text-gray-900"
                  >
                    Paiement réussi
                  </Dialog.Title>
                  <div className="mt-2">
                    <p className="text-sm text-gray-500">
                      Votre paiement a été soumis avec succès. Nous vous avons envoyé
                      un email avec tous les détails de votre commande.
                    </p>
                  </div>

                  <div className="mt-4">
                    <button
                      type="button"
                      className="inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                      onClick={closeModal}
                    >
                      Compris, merci !
                    </button>
                  </div>
                </Dialog.Panel>
              </Transition.Child>
            </div>
          </div>
        </Dialog>
      </Transition>
    </>
  )
}

```

Voici à quoi cela ressemble :

![Une modale positionnée au centre avec un dégradé bleu et violet en superposition pour montrer comment fonctionnent les composants headless ui](https://www.freecodecamp.org/news/content/images/2023/08/screencapture-headlessui-react-dialog-2023-08-27-16_28_15.png)
_Exemple de modale faite avec Headless UI_

  
Pour plus de détails sur ce composant, [vous pouvez consulter leur documentation](https://headlessui.com/react/dialog).

### PrimeReact UI

PrimeReact UI dispose d'un composant `Dialog` flexible qui vous permet d'afficher du contenu dans des fenêtres de superposition.

Les temps d'apparition et de disparition du dialogue peuvent être modifiés. Il inclut des outils comme le redimensionnement et le glisser-déposer également.

Il insère automatiquement une barre de défilement pour une navigation facile si le matériel est trop long. En fonction de différentes largeurs d'écran, vous pouvez ajuster la largeur du dialogue. Le paramètre `position` vous permet de placer le dialogue dans différents coins de l'écran.

Il est compatible avec les lecteurs d'écran et la navigation au clavier car il a été créé en tenant compte de l'accessibilité. Les touches du clavier permettent aux utilisateurs de parcourir le dialogue. Il respecte les meilleures pratiques d'intégration et fonctionne bien avec d'autres bibliothèques.

#### Exemple de code de PrimeReact UI :

Pour commencer, exécutez cette commande dans votre terminal : 

`npm install primereact`

Voici un extrait de code du composant de dialogue :

```
import React, { useState } from "react";
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';

export default function BasicDemo() {
    const [visible, setVisible] = useState(false);

    return (
        <div className="card flex justify-content-center">
            <Button label="Afficher" icon="pi pi-external-link" onClick={() => setVisible(true)} />
            <Dialog header="En-tête" visible={visible} style={{ width: '50vw' }} onHide={() => setVisible(false)}>
                <p className="m-0">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                </p>
            </Dialog>
        </div>
    )
}
                
```

Voici à quoi cela ressemble :

![Ce composant de dialogue de primereact est positionné à droite de l'écran et a une superposition grise](https://www.freecodecamp.org/news/content/images/2023/08/screencapture-primereact-org-dialog-2023-08-26-08_09_58.png)
_Position du composant de dialogue au centre-droit de l'écran_

Pour plus d'informations sur la bibliothèque, [visitez leur documentation ici](https://primereact.org/dialog/).

### Composant Dialog de Reach UI :

Le composant Dialog de Reach UI est une excellente option pour concevoir des fenêtres contextuelles conviviales et accessibles.

Il offre un contrôle précis et est simple à utiliser. Il fonctionne parfaitement sur une variété d'appareils. Il dispose de fonctionnalités d'accessibilité améliorant l'utilisabilité, et il est simple de créer des fenêtres contextuelles d'alerte.

Il prend également en charge le zoom par pincement et est compatible avec les iPads et les iPhones.

#### Exemple de code de Reach UI :

Pour commencer, vous pouvez exécuter cette commande dans votre terminal pour installer les composants : `npm install @reach/dialog`.

Pour utiliser les composants dans votre application, vous pouvez les importer comme ceci :

```
import { Dialog, DialogOverlay, DialogContent } from "@reach/dialog";
import "@reach/dialog/styles.css";

function Dialog() {
  const [showDialog, setShowDialog] = React.useState(false);
  const open = () => setShowDialog(true);
  const close = () => setShowDialog(false);

  return (
    <div>
      <button onClick={open}>Ouvrir le dialogue</button>

      <Dialog isOpen={showDialog} onDismiss={close}>
        <button className="close-button" onClick={close}>
          <VisuallyHidden>Fermer</VisuallyHidden>
          <span aria-hidden>7</span>
        </button>
        <p>Bonjour. Je suis un dialogue</p>
      </Dialog>
    </div>
  );
}
```

Voici à quoi ils ressemblent :

![Le composant de dialogue de reach ui est placé au centre de l'écran](https://www.freecodecamp.org/news/content/images/2023/08/screencapture-reach-tech-dialog-2023-08-26-08_37_03.png)
_Composant de dialogue de reach ui_

  
Pour en savoir plus sur cette bibliothèque et ses composants, [vous pouvez consulter leur documentation ici](https://reach.tech/dialog/).

## Conclusion

Cet article a mis en lumière plusieurs bibliothèques de composants non stylisés populaires, notamment Radix UI, le composant UI de shadcn, la bibliothèque Headless UI, PrimeReact UI et le composant Dialog de Reach UI. 

En résumé, l'utilisation de composants UI non stylisés vous permet de personnaliser vos composants selon vos besoins. Cela apporte également une efficacité de performance et une adaptabilité future. 

Ces composants offrent une surcharge réduite, car ils vous permettent d'utiliser uniquement les composants dont vous avez besoin. Cela se traduit par une application plus efficace. 

La flexibilité des composants non stylisés vous permet également de personnaliser les éléments pour des exigences de projet spécifiques, tout en priorisant l'accessibilité et la convivialité. L'intégration de composants UI non stylisés améliore votre capacité à créer des interfaces utilisateur accessibles, visuellement attrayantes et efficaces.