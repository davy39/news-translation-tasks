---
title: Guide TypeScript pour les développeurs React – Comment créer une application
  Todo sécurisée par les types
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-11T16:05:08.000Z'
originalURL: https://freecodecamp.org/news/typescript-tutorial-for-react-developers
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/TypeScript-Handbook-for-React-Developers-Cover.png
tags:
- name: handbook
  slug: handbook
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Guide TypeScript pour les développeurs React – Comment créer une application
  Todo sécurisée par les types
seo_desc: 'By Yazdun Fadali

  In today''s JavaScript landscape, TypeScript is gaining more and more popularity.
  And React developers are starting to use it more and more.

  If you''re a React developer looking to explore TypeScript or enhance your skills
  with it, thi...'
---

Par Yazdun Fadali

Dans le paysage JavaScript actuel, TypeScript gagne de plus en plus en popularité. Et les développeurs React commencent à l'utiliser de plus en plus.

Si vous êtes un développeur React cherchant à explorer TypeScript ou à améliorer vos compétences avec celui-ci, ce guide est fait pour vous. Je vais vous guider à travers l'utilisation de TypeScript dans une application React en construisant une classique application de liste de tâches.

Je vais couvrir tout ce que vous devez savoir pour commencer avec TypeScript en tant que développeur React. Vous apprendrez comment gérer l'état et les props avec un typage fort, comment créer des composants React avec TypeScript, comment utiliser TypeScript avec les React Hooks, et comment utiliser TypeScript avec l'API Context.

À la fin de ce tutoriel, vous aurez une solide compréhension de TypeScript et serez prêt à développer des applications React sécurisées par les types avec confiance. Alors, sans plus attendre, commençons !

## Voici ce que nous allons couvrir

* [Prérequis](#heading-prerequisites)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Mise en route](#heading-mise-en-route)
* [Comment configurer le composant de l'application Todo](#heading-comment-configurer-le-composant-de-lapplication-todo)
* [Comment créer un élément de formulaire simple dans React](#heading-comment-creer-un-element-de-formulaire-simple-dans-react)
* [Qu'est-ce qu'une erreur de type dans TypeScript et comment la corriger ?](#heading-questce-quune-erreur-de-type-dans-typescript-et-comment-la-corriger)
* [Quels sont les types génériques dans TypeScript ?](#heading-quels-sont-les-types-generiques-dans-typescript)
* [Comment gérer la soumission de formulaire avec TypeScript dans React](#heading-comment-gerer-la-soumission-de-formulaire-avec-typescript-dans-react)
* [Comment mettre automatiquement le focus sur un champ de saisie dans React](#heading-comment-mettre-automatiquement-le-focus-sur-un-champ-de-saisie-dans-react)
* [Qu'est-ce que `useRef` et comment l'utiliser avec TypeScript](#heading-questce-que-useref-et-comment-lutiliser-avec-typescript)
* [Comment créer des composants React sécurisés par les types avec TypeScript](#heading-comment-creer-des-composants-react-securises-par-les-types-avec-typescript)
* [Qu'est-ce que `forwardRef` dans React ?](#heading-questce-que-forwardref-dans-react)
* [Comment créer un élément todo lors de la soumission du formulaire ?](#heading-comment-creer-un-element-todo-lors-de-la-soumission-du-formulaire)
* [Qu'est-ce que le Context de React ?](#heading-questce-que-le-context-de-react)
* [Comment utiliser le Context de React avec TypeScript ?](#heading-comment-utiliser-le-context-de-react-avec-typescript)
* [Quelles sont les interfaces dans TypeScript ?](#heading-quelles-sont-les-interfaces-dans-typescript)
* [Comment utiliser les interfaces TypeScript avec le Context de React](#heading-comment-utiliser-les-interfaces-typescript-avec-le-context-de-react)
* [Comment créer un hook personnalisé pour consommer le Context de React](#heading-comment-creer-un-hook-personnalise-pour-consommer-le-context-de-react)
* [Comment définir une interface pour les éléments Todo](#heading-comment-definir-une-interface-pour-les-elements-todo)
* [Comment construire un composant React personnalisé pour afficher les éléments Todo](#heading-comment-construire-un-composant-react-personnalise-pour-afficher-les-elements-todo)
* [Comment implémenter les fonctionnalités : Éditer, Supprimer et Mettre à jour les éléments Todo](#heading-comment-implementer-les-fonctionnalites-editer-supprimer-et-mettre-a-jour-les-elements-todo)
* [Conclusion](#heading-conclusion)

## Prérequis

Aucune connaissance préalable de TypeScript n'est nécessaire pour commencer ce tutoriel, ce qui le rend complètement adapté aux débutants. Cependant, avoir une expérience avec React améliorera grandement votre compréhension et maximisera votre potentiel d'apprentissage tout au long de ce tutoriel.

Tout au long de ce tutoriel, vous utiliserez les outils suivants :

1. **React 18.2.0** : React est une bibliothèque JavaScript utilisée pour construire des interfaces utilisateur. Elle permet aux développeurs de créer des composants UI réutilisables et de mettre à jour efficacement l'UI en fonction des changements de données.
2. **TypeScript** : TypeScript est un sur-ensemble de JavaScript avec typage statique qui ajoute des annotations de type optionnelles. Il fournit des outils améliorés et aide à détecter les erreurs potentielles pendant le développement, rendant le code plus fiable et plus facile à maintenir.
3. **Vite** : Vite est un serveur de développement rapide et un outil de construction pour les applications web modernes. Il offre un démarrage instantané du serveur, le remplacement de modules à chaud et une sortie de construction optimisée, permettant des flux de travail de développement rapides et efficaces.
4. **Framer Motion** : Framer Motion est une bibliothèque d'animation populaire pour React. Elle fournit une interface facile à utiliser pour créer des animations et des transitions fluides et interactives dans les applications web, améliorant ainsi l'expérience utilisateur globale.

Dans la section suivante, vous obtiendrez un aperçu concis du projet que vous allez construire dans ce tutoriel.

## Que allons-nous construire ?

Nous allons construire une application classique de liste de tâches. Elle aura les fonctionnalités suivantes :

* Ajouter un élément de tâche.
* Modifier un élément de tâche.
* Supprimer un élément de tâche.
* Marquer un élément de tâche comme terminé ou non.
* Stocker les éléments de tâche dans le stockage local du navigateur.
* Afficher des messages d'erreur appropriés lorsque l'utilisateur essaie d'ajouter ou de modifier un élément de tâche avec un titre vide.

![Il s'agit d'une application de liste de tâches où les utilisateurs peuvent ajouter ou supprimer un élément, ils peuvent également modifier un élément existant ou les marquer comme terminés](https://www.freecodecamp.org/news/content/images/2023/06/ezgif-3-98866e5ad0.gif)
_Aperçu de l'application finale_

## Mise en route

Pour commencer avec ce tutoriel, j'ai déjà préparé pour vous un projet de base qui contient toutes les dépendances requises. Cela élimine le besoin de configurer votre projet à partir de zéro.

Clonez simplement le [modèle de base](https://github.com/Yazdun/react-ts-fcc-tutorial/tree/starter) depuis le dépôt GitHub, puis suivez le tutoriel. De cette façon, vous pouvez vous concentrer sur l'apprentissage et la mise en œuvre des concepts sans vous perdre dans les détails de configuration.

* Modèle de base : [Voir sur GitHub](https://github.com/Yazdun/react-ts-fcc-tutorial/tree/starter)
* Version finale : [Voir sur GitHub](https://github.com/Yazdun/react-ts-fcc-tutorial)

Une fois que vous avez configuré le modèle de base et l'avez exécuté avec succès sur votre machine locale, vous devriez pouvoir voir la page initiale. Cette page servira de point de départ pour notre voyage.

![Page simple affichant le texte "Todo App". cette page sert de point de départ de notre tutoriel](https://www.freecodecamp.org/news/content/images/2023/06/image-314.png)
_Modèle de base_

Maintenant, nous allons commencer à ajouter des fonctionnalités passionnantes à notre application. Plongeons-nous et commençons tout de suite !

## Comment configurer le composant de l'application Todo

Dans cette section, vous allez configurer le composant principal de votre application Todo et l'améliorer progressivement avec des fonctionnalités supplémentaires. Ouvrez `./src/App.tsx` et ajoutez le code suivant :

```tsx
//📂./src/App.tsx

import { TodoList, AddTodo } from './components'
import { Toaster } from 'react-hot-toast'

function App() {
  return (
    <div>
      <Toaster position="bottom-center" />
      <AddTodo />
      <TodoList />
    </div>
  )
}

export default App

```

Décomposons cela étape par étape :

* `<Toaster position="bottom-center" />` : Ce composant est responsable de l'affichage des notifications toast au centre inférieur de l'écran.
* `<AddTodo />` : Ce composant représentera un champ de saisie et un bouton pour ajouter de nouveaux éléments de tâche à l'application.
* `<TodoList />` : Ce composant affichera une liste des éléments de tâche existants.

Maintenant, ouvrez votre serveur local sur votre navigateur et vous pourrez voir la page suivante :

![Page web simple affichant deux composants React](https://www.freecodecamp.org/news/content/images/2023/06/image-315.png)
_Aperçu de App.tsx_

Ces deux composants jouent un rôle critique dans votre application. Dans la section suivante, vous allez construire la fonctionnalité pour ajouter un élément de tâche en utilisant le composant `<AddTodo />`. Plus précisément, vous apprendrez comment gérer les soumissions de formulaire avec TypeScript dans React.

## Comment créer un élément de formulaire simple dans React

Tout d'abord, vous devez créer un élément de formulaire pour créer un élément de tâche. Pour y parvenir dans votre application, vous devez créer un formulaire et gérer la soumission du formulaire efficacement. Dans cette section, vous allez explorer comment gérer la soumission de formulaire en utilisant TypeScript dans une application React.

Je veux juste vous donner un petit avertissement puisque vous allez rencontrer votre première erreur de type dans TypeScript ! Ajoutez le code suivant à `components/AddTodo.tsx` :

```tsx
//📂./src/components/AddTodo.tsx
// 26a0 fe0fTypeScript n'est pas content de ce code

import React, { useEffect, useRef, useState } from 'react'
import { toast } from 'react-hot-toast'
import { useTodo } from '../context'
import { Input } from './Input'

export const AddTodo = () => {
  const [input, setInput] = useState()

  return (
    <form>
      <div className="flex items-center w-full max-w-lg gap-2 p-5 m-auto">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          type="text"
          className="w-full px-5 py-2 bg-transparent border-2 outline-none border-zinc-600 rounded-xl placeholder:text-zinc-500 focus:border-white"
          placeholder="commencez à taper ..."
        />
        <button
          type="submit"
          className="px-5 py-2 text-sm font-normal text-blue-300 bg-blue-900 border-2 border-blue-900 active:scale-95 rounded-xl"
        >
          Soumettre
        </button>
      </div>
    </form>
  )
}

```

Vous avez créé un hook useState qui met à jour l'état avec la valeur de l'entrée à mesure qu'elle change. Cependant, TypeScript n'est pas content de ce code. Mais pourquoi TypeScript n'est-il pas content ?

### Qu'est-ce qu'une erreur de type dans TypeScript et comment la corriger

Les types dans TypeScript définissent le type de données que les variables peuvent contenir et permettent la détection d'erreurs et de bugs pendant le développement.

Une erreur de type dans TypeScript se produit lorsqu'une valeur est utilisée de manière incompatible avec son type attendu, ce qui peut entraîner des bugs ou un comportement inattendu dans le code.

Dans notre cas, TypeScript montre une erreur dans ce code car il ne peut pas déduire automatiquement le type de la variable d'état `input`. Pour corriger cela, vous devez fournir à TypeScript les informations de type de manière explicite. Dans ce cas, vous voulez que input soit de type string puisqu'il représente la valeur du champ de saisie.

Pour corriger cette erreur, vous avez deux options. La solution facile consiste à ajouter une valeur initiale au hook `useState` et TypeScript déduira automatiquement le type `input` comme une chaîne :

```tsx
 const [input, setInput] = useState('')

```

En ajoutant le code ci-dessus, vous pouvez remarquer que l'erreur disparaît et que TypeScript est satisfait. Mais toutes les erreurs ne peuvent pas être résolues aussi facilement dans TypeScript.

Considérons une situation où vous n'êtes pas certain du type de votre état et ne pouvez pas déterminer s'il doit être initialisé comme un nombre ou une chaîne. Cette incertitude nous conduit à la deuxième option, qui consiste à utiliser des types génériques.

### Quels sont les types génériques dans TypeScript ?

Les types génériques fournissent un moyen de gérer les situations où vous n'êtes pas sûr du type spécifique d'une valeur. Avec les types génériques, vous pouvez définir un espace réservé qui représente le type réel, ce qui vous permet de rendre votre code plus flexible et réutilisable :

```tsx
const [state, setState] = useState<string | number>('')

```

Le code ci-dessus initialise une variable d'état nommée "state" avec une valeur initiale de chaîne vide, mais il permet à l'état de contenir soit une chaîne, soit un nombre comme valeur.

Maintenant, introduisons un type générique dans votre application. Vous ne voulez pas que vos utilisateurs ajoutent un nombre comme todo – nous voulons qu'ils puissent uniquement ajouter une chaîne :

```tsx
//📂./src/components/AddTodo.tsx
// 2705TypeScript est content de ce code

import React, { useEffect, useRef, useState } from 'react'
import { toast } from 'react-hot-toast'
import { useTodo } from '../context'
import { Input } from './Input'

export const AddTodo = () => {
  const [input, setInput] = useState<string>('')

  return (
    <form>
      <div className="flex items-center w-full max-w-lg gap-2 p-5 m-auto">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          type="text"
          className="w-full px-5 py-2 bg-transparent border-2 outline-none border-zinc-600 rounded-xl placeholder:text-zinc-500 focus:border-white"
          placeholder="commencez à taper ..."
        />
        <button
          type="submit"
          className="px-5 py-2 text-sm font-normal text-blue-300 bg-blue-900 border-2 border-blue-900 active:scale-95 rounded-xl"
        >
          Soumettre
        </button>
      </div>
    </form>
  )
}

```

En spécifiant `<string>` après la fonction `useState`, nous nous assurons que la variable d'état `input` ne peut contenir que des valeurs de type string. Cela empêche les utilisateurs de saisir des nombres ou tout autre type de données incompatible comme des todos.

### Comment gérer la soumission de formulaire avec TypeScript dans React

Maintenant que vous avez réussi à stocker la valeur de l'entrée dans l'état, procédons à la gestion de la soumission du formulaire elle-même :

```tsx
//📂./src/components/AddTodo.tsx

import React, { useEffect, useRef, useState } from 'react'
import { toast } from 'react-hot-toast'
import { useTodo } from '../context'
import { Input } from './Input'

export const AddTodo = () => {
  const [input, setInput] = useState<string>('')

  const handleSubmission = (e: React.FormEvent) => {
    e.preventDefault()
    console.log('le formulaire a été soumis')
  }

  return (
    <form onSubmit={handleSubmission}>
      <div className="flex items-center w-full max-w-lg gap-2 p-5 m-auto">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          type="text"
          className="w-full px-5 py-2 bg-transparent border-2 outline-none border-zinc-600 rounded-xl placeholder:text-zinc-500 focus:border-white"
          placeholder="commencez à taper ..."
        />
        <button
          type="submit"
          className="px-5 py-2 text-sm font-normal text-blue-300 bg-blue-900 border-2 border-blue-900 active:scale-95 rounded-xl"
        >
          Soumettre
        </button>
      </div>
    </form>
  )
}


```

La fonction `handleSubmission` est appelée lorsque le formulaire est soumis. Décomposons cela étape par étape :

1. `(e: React.FormEvent)` est la déclaration de paramètre de la fonction. Elle spécifie que la fonction attend un objet événement de type `React.FormEvent` à passer comme argument. Le `React.FormEvent` est un type d'objet événement qui représente un événement se produisant sur un élément de formulaire, tel que la soumission du formulaire ou l'interaction avec les champs de formulaire.
2. `e.preventDefault()` est une méthode qui appartient à l'objet événement (`e`). Elle est appelée pour empêcher le comportement par défaut de la soumission du formulaire, qui est de rafraîchir la page. En appelant `preventDefault()`, nous remplaçons le comportement par défaut et empêchons la page de se rafraîchir.
3. `console.log('le formulaire a été soumis')` est une simple instruction qui enregistre un message dans la console du navigateur. Dans ce cas, elle enregistre le message "le formulaire a été soumis" lorsque l'événement de soumission du formulaire se produit.

Super ! Vous avez terminé les étapes nécessaires pour gérer la soumission du formulaire. Maintenant, passons à la section suivante où vous améliorerez la fonctionnalité de votre formulaire en apportant quelques modifications.

### Comment mettre automatiquement le focus sur un champ de saisie dans React

Pour améliorer l'expérience utilisateur, vous pouvez automatiquement mettre le focus sur le champ de saisie "ajouter une tâche" lorsque l'application est initialement chargée. Cela élimine le besoin pour les utilisateurs de cliquer manuellement sur le champ de saisie lors de l'ouverture de l'application.

Pour implémenter cette fonctionnalité, vous pouvez utiliser un hook React spécifique appelé `useRef`, qui vous permet d'incorporer cette fonctionnalité dans le champ de saisie.

#### Qu'est-ce que `useRef` et comment l'utiliser avec TypeScript

`useRef` est un hook spécial dans React qui crée une référence à un élément ou une valeur dans votre composant. Cette référence peut être utilisée pour accéder et manipuler l'élément référencé directement, sans provoquer de re-rendus. 

Vous l'utiliserez couramment pour accéder aux éléments du DOM, gérer le focus ou stocker des valeurs mutables entre les rendus des composants.

Ouvrez l'application `components/AddTodo.tsx` et ajoutez le code suivant :

```tsx
//📂./src/components/AddTodo.tsx

import React, { useEffect, useRef, useState } from 'react'
import { toast } from 'react-hot-toast'
import { useTodo } from '../context'
import { Input } from './Input'

export const AddTodo = () => {
  const [input, setInput] = useState<string>('')
  const inputRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus()
    }
  }, [])

  const handleSubmission = (e: React.FormEvent) => {
    e.preventDefault()
    console.log('le formulaire a été soumis')
  }

  return (
    <form onSubmit={handleSubmission}>
      <div className="flex items-center w-full max-w-lg gap-2 p-5 m-auto">
        <input
          ref={inputRef}
          value={input}
          onChange={e => setInput(e.target.value)}
          type="text"
          className="w-full px-5 py-2 bg-transparent border-2 outline-none border-zinc-600 rounded-xl placeholder:text-zinc-500 focus:border-white"
          placeholder="commencez à taper ..."
        />
        <button
          type="submit"
          className="px-5 py-2 text-sm font-normal text-blue-300 bg-blue-900 border-2 border-blue-900 active:scale-95 rounded-xl"
        >
          Soumettre
        </button>
      </div>
    </form>
  )
}

```

Ici, le hook `useRef` de React est utilisé avec TypeScript.

* La ligne `const inputRef = useRef<HTMLInputElement>(null)` déclare une variable de référence appelée `inputRef` en utilisant le hook useRef. Le paramètre de type `<HTMLInputElement>` spécifie que la référence est destinée à un élément d'entrée. La valeur initiale de la référence est définie sur `null`.
* Dans le hook useEffect, `inputRef.current` est vérifié pour voir s'il existe. Si c'est le cas, la méthode `focus()` est appelée sur celui-ci, ce qui signifie que le champ de saisie recevra le focus lorsque le composant sera monté.

Le hook `useRef` est paramétré avec le type `<HTMLInputElement>` pour s'assurer que la référence est compatible avec les éléments d'entrée.

En utilisant useRef et TypeScript ensemble, le code bénéficie de la vérification de type statique de TypeScript et de la capacité à interagir avec la référence DOM de l'élément d'entrée en utilisant useRef.

Bien que ce code fonctionne correctement, il serait bénéfique de réutiliser ce composant d'entrée dans d'autres parties de votre application. Par conséquent, créons un composant d'entrée réutilisable et explorons comment développer des composants React sécurisés par les types en implémentant cette entrée.

### Comment créer des composants React sécurisés par les types avec TypeScript

Dans cette section, vous allez créer un composant Input sécurisé par les types pour les cas d'utilisation futurs dans votre application. 

Pour créer ce composant Input personnalisé, vous devrez passer la référence que vous avez créée dans la section précédente en tant que prop à ce composant. 

Les refs sont passées en tant que props normales, et afin de passer des refs aux composants enfants, vous devez implémenter une fonction intégrée spéciale de React appelée forwardRef.

#### Qu'est-ce que `forwardRef` dans React ?

Dans React, la fonction `forwardRef` est une fonctionnalité qui vous permet de passer une ref d'un composant parent à un composant enfant. Les refs sont utilisées pour accéder et manipuler directement les éléments DOM sous-jacents.

En utilisant `forwardRef`, vous pouvez créer un composant personnalisé qui peut recevoir une ref et la transmettre à un élément spécifique au sein du composant.

Cela permet au composant parent d'interagir avec l'élément sous-jacent du composant enfant, comme mettre le focus sur un champ de saisie ou déclencher certaines actions.

En termes simples, `forwardRef` vous aide à connecter une ref entre les composants, vous permettant de contrôler ou d'accéder à l'élément interne du composant enfant si nécessaire.

Maintenant, créons un composant Input réutilisable. Ouvrez `components/Input.tsx` :

```tsx
// 📂./src/components/Input.tsx

import { InputHTMLAttributes, forwardRef } from 'react'
import cn from 'classnames'

export const Input = forwardRef<
  HTMLInputElement,
  InputHTMLAttributes<HTMLInputElement>
>(({ className, ...rest }, ref) => {
  return (
    <input
      {...rest}
      ref={ref}
      className={cn(
        'w-full px-5 py-2 bg-transparent border-2 outline-none border-zinc-600 rounded-xl placeholder:text-zinc-500 focus:border-white',
        className,
      )}
    />
  )
})
```

Décomposons ce composant étape par étape :

1. Le composant utilise la fonction `forwardRef` de React pour transmettre la ref à l'élément `<input>` sous-jacent. Cela permet aux composants parents d'accéder et de manipuler l'élément d'entrée directement.
2. `HTMLInputElement` spécifie le type de la ref qui sera transmise à l'élément `<input>` sous-jacent. Cela garantit que la ref est compatible avec le type attendu de l'élément d'entrée.
3. `InputHTMLAttributes<HTMLInputElement>` spécifie le type de l'objet props que le composant accepte. Cela inclut tous les attributs standard des éléments d'entrée HTML, tels que `value`, `placeholder`, `onChange`, et ainsi de suite.
4. Le composant déstructure la prop `className` de l'objet `rest` et reçoit également la `ref` en tant que paramètre.
5. À l'intérieur du composant, une expression JSX est utilisée pour rendre un élément `<input>`. L'opérateur de propagation (`{...rest}`) est utilisé pour passer toutes les props (sauf `className` et `ref`) reçues par le composant à l'élément `<input>`. Cela garantit que tous les attributs supplémentaires passés au composant `<Input>` seront appliqués à l'élément `<input>` sous-jacent.
6. La `ref` est assignée à l'élément `<input>` sous-jacent en utilisant l'attribut `ref`, permettant au composant parent de référencer l'élément d'entrée.
7. La `className` est construite en utilisant la fonction `cn` du module `classnames`. Cette fonction combine plusieurs noms de classes CSS en fonction des conditions fournies. Dans ce cas, elle combine les noms de classes par défaut de l'élément d'entrée avec la prop `className` passée au composant `<Input>`.

L'élément `<input>` final rendu aura les noms de classes combinés et héritera de toutes les autres props passées au composant `<Input>`.

Maintenant, mettons à jour le composant `<AddTodo />` pour utiliser le composant personnalisé `<Input />` au lieu de l'élément HTML d'entrée par défaut :

```tsx
//📂./src/components/AddTodo.tsx

import React, { useEffect, useRef, useState } from 'react'
import { toast } from 'react-hot-toast'
import { useTodo } from '../context/useTodo'
import { Input } from './Input'

export const AddTodo = () => {
  const [input, setInput] = useState<string>('')
  const inputRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus()
    }
  }, [])

  const handleSubmission = (e: React.FormEvent) => {
    e.preventDefault()
    console.log('le formulaire a été soumis')
  }

  return (
    <form onSubmit={handleSubmission}>
      <div className="flex items-center w-full max-w-lg gap-2 p-5 m-auto">
        <Input
          ref={inputRef}
          value={input}
          onChange={e => setInput(e.target.value)}
          type="text"
          className="w-full px-5 py-2 bg-transparent border-2 outline-none border-zinc-600 rounded-xl placeholder:text-zinc-500 focus:border-white"
          placeholder="commencez à taper ..."
        />
        <button
          type="submit"
          className="px-5 py-2 text-sm font-normal text-blue-300 bg-blue-900 border-2 border-blue-900 active:scale-95 rounded-xl"
        >
          Soumettre
        </button>
      </div>
    </form>
  )
}

```

Maintenant, vous pouvez utiliser ce composant personnalisé `<Input />` dans toute votre application. Dans la section suivante, vous allez créer la fonctionnalité pour ajouter un élément todo lors de la soumission du formulaire. 

### Comment créer un élément todo lors de la soumission du formulaire

Pour stocker chaque élément todo, vous pouvez utiliser un tableau qui contient la saisie de l'utilisateur. Essentiellement, nous avons besoin d'un tableau de chaînes pour stocker chaque todo :

```tsx
const [todos, setTodos] = useState<string[]>([])

```

`string[]` spécifie le type de données qui seront stockées dans la variable d'état `todos`. Dans ce cas, il s'agit d'un tableau de chaînes, ce qui signifie qu'il contiendra une liste d'éléments todo, où chaque élément est représenté par une chaîne.

Maintenant, ajoutons un élément au tableau `todos` lors de la soumission du formulaire :

```tsx
//📂./src/components/AddTodo.tsx

import React, { useEffect, useRef, useState } from 'react'
import { toast } from 'react-hot-toast'
import { useTodo } from '../context'
import { Input } from './Input'

export const AddTodo = () => {
  const [input, setInput] = useState<string>('')
  const [todos, setTodos] = useState<string[]>([])

  const handleSubmission = (e: React.FormEvent) => {
    e.preventDefault()
    if (input.trim() !== '') {
      setTodos([...todos, input])
      setInput('')
    }
  }

  return (
    <form onSubmit={handleSubmission}>
      <div className="flex items-center w-full max-w-lg gap-2 p-5 m-auto">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          type="text"
          className="w-full px-5 py-2 bg-transparent border-2 outline-none border-zinc-600 rounded-xl placeholder:text-zinc-500 focus:border-white"
          placeholder="commencez à taper ..."
        />
        <button
          type="submit"
          className="px-5 py-2 text-sm font-normal text-blue-300 bg-blue-900 border-2 border-blue-900 active:scale-95 rounded-xl"
        >
          Soumettre
        </button>
      </div>
    </form>
  )
}
```

La fonction `handleSubmission` vérifie si la valeur de `input` (la tâche saisie par l'utilisateur) n'est pas une chaîne vide après avoir supprimé les espaces de début et de fin en utilisant `input.trim() !== ''`.

Si elle n'est pas vide, elle ajoute la valeur de `input` au tableau `todos` existant en utilisant `setTodos([...todos, input])`. Cela crée un nouveau tableau avec tous les todos précédents et le nouveau todo ajouté à la fin. Elle réinitialise la valeur de `input` à une chaîne vide en utilisant `setInput('')` afin que le champ de saisie devienne vide et prêt pour la prochaine entrée de todo.

Maintenant, bien que vous ayez réussi à implémenter la fonctionnalité pour créer un élément todo, il ne peut pas encore être affiché à l'écran.

C'est parce que le composant `<AddTodo />` est responsable de l'ajout d'éléments todo, pas de leur affichage.

D'autre part, le composant `<TodoList />` est responsable de l'affichage de tous les éléments. Pour combler cet écart et partager les todos entre ces composants, vous pouvez tirer parti de la puissance du Context de React.

## Qu'est-ce que le Context de React ?

L'API React Context est une fonctionnalité de React qui permet de partager et d'accéder aux données par les composants sans les passer explicitement via les props. Elle fournit un moyen de créer un état global qui peut être accessible par n'importe quel composant dans l'application.

Imaginez que vous avez une structure d'arbre de composants, où certaines données doivent être accessibles par plusieurs composants à différents niveaux. Plutôt que de passer les données à travers plusieurs couches de composants, vous pouvez utiliser React Context pour créer un magasin central pour ces données.

Voici comment cela fonctionne :

1. **Créer un Context** : Tout d'abord, vous définissez un contexte en utilisant la fonction `createContext()`. Cela crée un objet de contexte qui contient les données partagées.
2. **Fournir le Context** : Vous enveloppez le composant parent ou une partie spécifique de votre application avec un `<Context.Provider>`. Ce composant fournisseur accepte une prop `value` où vous pouvez passer les données que vous souhaitez partager.
3. **Consommer le Context** : Pour accéder aux données partagées au sein d'un composant, vous utilisez le hook `useContext()` fourni par React. En passant le contexte créé comme argument à `useContext()`, vous pouvez accéder aux données partagées et les utiliser au sein de ce composant.
4. **Mettre à jour le Context** : Si vous devez mettre à jour les données partagées, vous pouvez le faire en modifiant la valeur dans le composant fournisseur. Ce changement se propagera automatiquement à tous les composants qui consomment le contexte.

L'API React Context simplifie le processus de partage de données entre les composants, éliminant le besoin de passer manuellement les props à travers plusieurs niveaux.

Dans votre situation, vous devez créer un Context pour partager les éléments todo entre plusieurs composants. Créons un Context pour voir comment ce mécanisme fonctionne en pratique.

### Comment utiliser le Context de React avec TypeScript

Dans cette section, vous apprendrez à créer un Context React pour isoler la logique de l'application et améliorer les capacités de gestion d'état de votre application.

Si vous ouvrez `context/TodoContext.tsx`, vous verrez le code suivant :

```tsx
// 📂./src/context/TodoContext.tsx

import React, { createContext } from 'react'
import { nanoid } from 'nanoid'
import { useLocalStorage } from 'usehooks-ts'

export const TodoContext = createContext<undefined>(undefined)

export const TodoProvider = (props: { children: React.ReactNode }) => {
  return (
    <TodoContext.Provider value={undefined}>
      {props.children}
    </TodoContext.Provider>
  )
}


```

Décomposons cela étape par étape :

* Le `TodoContext` est créé en utilisant la fonction `createContext` fournie par React. Il est initialisé avec une valeur indéfinie.
* De plus, un composant `TodoProvider` est défini. Il prend une prop `children`, qui représente les composants enfants qui seront enveloppés par ce fournisseur.
* À l'intérieur du composant `TodoProvider`, un composant `<TodoContext.Provider>` est rendu. Il enveloppe les `props.children`, ce qui permet aux composants enfants d'accéder au TodoContext.
* La valeur fournie au composant `<TodoContext.Provider>` est définie sur `undefined` pour l'instant.

Dans la section suivante, vous allez créer un Context plus complexe en apprenant quelque chose appelé une **Interface** dans TypeScript.

### Quelles sont les interfaces dans TypeScript ?

Dans TypeScript, les interfaces sont un moyen de définir la structure et la forme d'un objet. Elles vous permettent de spécifier les propriétés et leurs types qu'un objet doit avoir. Considérez une interface comme un plan ou un contrat qui décrit à quoi un objet doit ressembler.

Imaginez que vous construisez une maison. Avant de commencer la construction, vous auriez un plan qui décrit la conception et la disposition de la maison. De même, une interface dans TypeScript est comme un plan pour un objet.

Regardons un exemple simple d'une interface :

```ts
interface Person {
  name: string;
  age: number;
}
```

Dans cet exemple, nous définissons une interface appelée `Person` qui décrit la structure d'un objet personne. Elle spécifie qu'un objet personne doit avoir deux propriétés : `name`, qui doit être de type `string`, et `age`, qui doit être de type `number`.

Considérons votre Todo Context et les props que vous souhaitez passer à ses consommateurs. Dans ce cas, vous aurez besoin d'une interface qui définit les props requises, y compris un tableau de chaînes qui contient tous les éléments todo, ainsi qu'une fonction qui accepte une chaîne et l'ajoute à la liste des todos.

```tsx
interface TodoContextProps {
  todos: string[]
  addTodo: (text: string) => void
}
```

L'interface `TodoContextProps` spécifie la structure des propriétés attendues dans le TodoContext. Elle a deux propriétés :

1. `todos` : Un tableau de chaînes qui représente les éléments todo. Cette propriété contient tous les todos existants.
2. `addTodo` : Une fonction qui accepte un paramètre de type string (`text`) et a un type de retour `void`. Cette fonction est responsable de l'ajout d'un nouvel élément todo à la liste. Elle prend le nouvel élément todo comme entrée et effectue l'action nécessaire sans retourner de valeur.

### Comment utiliser les interfaces TypeScript avec le Context de React

Maintenant que vous avez une compréhension des avantages des interfaces TypeScript, il est temps d'améliorer votre Context en incorporant cette interface :

```tsx
// 📂./src/context/TodoContext.tsx

import React, { createContext, useState } from 'react'
import { nanoid } from 'nanoid'
import { useLocalStorage } from 'usehooks-ts'

interface TodoContextProps {
  todos: string[]
  addTodo: (text: string) => void
}
export const TodoContext = createContext<TodoContextProps | undefined>(
  undefined,
)

export const TodoProvider = (props: { children: React.ReactNode }) => {
  const [todos, setTodos] = useState<string[]>([])

  // ::: AJOUTER UN NOUVEAU TODO :::
  const addTodo = (text: string) => {
    setTodos([...todos, text])
  }

  const value: TodoContextProps = {
    todos,
    addTodo,
  }

  return (
    <TodoContext.Provider value={value}>{props.children}</TodoContext.Provider>
  )
}

```

Dans ce code mis à jour, il y a des changements significatifs par rapport à la version précédente. Ces changements introduisent TypeScript et modifient les composants TodoContext et TodoProvider :

1. Ici, `TodoContextProps` spécifie qu'il doit avoir deux propriétés : `todos`, qui est un tableau de chaînes représentant les éléments todo, et `addTodo`, une fonction qui prend un paramètre de chaîne et ne retourne rien (void).
2. Le `TodoContext` est maintenant créé avec `createContext` et initialisé avec un type `TodoContextProps | undefined`. Cela signifie que la valeur du contexte peut être de type `TodoContextProps` ou indéfinie.
3. Le composant `TodoProvider` initialise maintenant l'état `todos` en utilisant le hook `useState`. Il suit les éléments todo en utilisant un tableau de chaînes.
4. Une nouvelle fonction `addTodo` est introduite, qui prend un paramètre de texte de chaîne (`text`). Elle utilise la fonction `setTodos` pour mettre à jour l'état `todos` en ajoutant le nouvel élément todo à la fin du tableau existant.
5. Création de la valeur pour le contexte : La variable `value` est assignée à un objet de type `TodoContextProps`, contenant le tableau `todos` et la fonction `addTodo`.
6. Fourniture de la valeur du contexte : Le composant `<TodoContext.Provider>` enveloppe les `props.children`, et la prop `value` est définie sur `value`, qui fournit les `todos` et `addTodo` aux composants enfants.

En résumé, vous utilisez TypeScript pour définir une interface pour les TodoContextProps, ajoutez un nouveau todo en utilisant useState et une fonction personnalisée, et fournissez la valeur de contexte mise à jour aux composants enfants.

### Comment créer un hook personnalisé pour consommer le Context de React

Pour utiliser les valeurs fournies par le contexte, vous devez créer un hook personnalisé qui consomme ce contexte et fournit ses valeurs aux composants enfants. Ouvrez `context/useTodo.ts` et ajoutez le code suivant :

```tsx
// 📂./src/context/useTodo.ts

import { useContext } from 'react'
import { TodoContext } from './TodoContext'

export const useTodo = () => {
  const context = useContext(TodoContext)

  if (!context) {
    throw new Error('useTodo doit être utilisé dans un TodoProvider')
  }

  return context
}

```

Décomposons cela étape par étape :

1. Vous importez le hook `useContext` du module 'react' et le `TodoContext` du fichier `./TodoContext`.
2. À l'intérieur du hook, le hook `useContext` est appelé avec `TodoContext` comme argument. Cela se connecte au `TodoContext` et récupère sa valeur actuelle.
3. Si la valeur `context` est `undefined`, cela signifie que le hook `useTodo` est utilisé en dehors de la portée du `TodoProvider`. Dans de tels cas, une erreur est levée avec le message 'useTodo doit être utilisé dans un TodoProvider'.

Dans l'ensemble, ce code vous permet de créer un hook personnalisé nommé `useTodo` qui peut être utilisé dans vos composants.

En appelant ce hook, vous pouvez accéder au `TodoContext` et récupérer sa valeur, qui inclut les données et fonctions liées aux todos définies dans le `TodoProvider`.

Il garantit également que le hook `useTodo` est utilisé uniquement dans la portée du `TodoProvider` pour maintenir une utilisation correcte et prévenir toute erreur.

Ensuite, vous devrez envelopper toute votre application avec le composant TodoProvider. Cela garantit que les valeurs de contexte sont accessibles à ses composants enfants en utilisant le hook `useTodo` :

```tsx
// 📂 ./src/main.tsx

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <TodoProvider>
      <App />
    </TodoProvider>
  </React.StrictMode>,
)
```

`<TodoProvider>` enveloppe toute l'application et fournit le contexte nécessaire pour gérer les données liées aux todos.

Maintenant, intégrons le hook useTodo dans le composant `<AddTodo />` pour gérer efficacement les éléments todo via le contexte. De plus, implémentons des notifications toast pour fournir un retour en fonction des interactions de l'utilisateur :

```tsx
//📂./src/components/AddTodo.tsx

import React, { useEffect, useRef, useState } from 'react'
import { toast } from 'react-hot-toast'
import { useTodo } from '../context/useTodo'
import { Input } from './Input'

export const AddTodo = () => {
  const [input, setInput] = useState<string>('')
  const inputRef = useRef<HTMLInputElement>(null)
  const { addTodo } = useTodo()

  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus()
    }
  }, [])

  const handleSubmission = (e: React.FormEvent) => {
    e.preventDefault()
    if (input.trim() !== '') {
      addTodo(input)
      setInput('')
      toast.success('Todo ajouté avec succès !')
    } else {
      toast.error('Le champ Todo ne peut pas être vide !')
    }
  }

  return (
    <form onSubmit={handleSubmission}>
      <div className="flex items-center w-full max-w-lg gap-2 p-5 m-auto">
        <Input
          ref={inputRef}
          type="text"
          placeholder="commencez à taper ..."
          value={input}
          onChange={e => setInput(e.target.value)}
        />
        <button
          type="submit"
          className="px-5 py-2 text-sm font-normal text-blue-300 bg-blue-900 border-2 border-blue-900 active:scale-95 rounded-xl"
        >
          Soumettre
        </button>
      </div>
    </form>
  )
}

```

1. La ligne `const { addTodo } = useTodo()` utilise le hook `useTodo` pour récupérer la fonction `addTodo` du contexte todo. Cela nous permet d'ajouter de nouveaux éléments todo.
2. La ligne `toast.success('Todo ajouté avec succès !')` affiche une notification toast de succès indiquant que le todo a été ajouté avec succès.
3. La ligne `toast.error('Le champ Todo ne peut pas être vide !')` affiche une notification toast d'erreur si le champ todo est vide lors de la tentative de soumission.
4. Si la valeur de `input` (sans les espaces) n'est pas vide, la fonction `addTodo` est appelée avec la valeur de l'input, l'état de l'input est effacé, et une notification toast de succès est affichée.
5. Si la valeur de `input` est vide, une notification toast d'erreur est affichée indiquant que le champ todo ne peut pas être vide.

Ce code intègre le hook `useTodo` pour gérer les éléments todo via le contexte. Il capture la saisie de l'utilisateur, ajoute des todos, et affiche des notifications toast pour fournir un retour sur le succès ou l'échec de l'ajout d'un élément todo.

Maintenant, modifions également le composant `<TodoList />` et affichons les éléments todo à l'écran. Ouvrez `components/TodoList.tsx` et ajoutez le code suivant :

```tsx
//📂./src/components/TodoList.tsx

import { useTodo } from '../context/useTodo'
import { SiStarship } from 'react-icons/si'

export const TodoList = () => {
  const { todos } = useTodo()

  if (!todos.length) {
    return (
      <div className="max-w-lg px-5 m-auto">
        <h1 className="flex flex-col items-center gap-5 px-5 py-10 text-xl font-bold text-center rounded-xl bg-zinc-900">
          <SiStarship className="text-5xl" />
          Vous n'avez rien à faire !
        </h1>
      </div>
    )
  }

  return (
    <ul className="grid max-w-lg gap-2 px-5 m-auto">
      {todos.map(todo => (
        <li key={todo}>{todo}</li>
      ))}
    </ul>
  )
}

```

1. L'instruction d'importation `import { useTodo } from '../context/useTodo'` importe le hook `useTodo` du contexte personnalisé, ce qui nous permet d'accéder au tableau `todos`.
2. Si le tableau `todos` est vide (`!todos.length`), ce qui signifie qu'il n'y a pas de todos, un message est affiché indiquant qu'il n'y a rien à faire.
3. S'il y a des todos dans le tableau `todos`, une liste non ordonnée (`<ul>`) est rendue.
4. À l'intérieur de la `<ul>`, le tableau `todos` est itéré en utilisant la fonction `map`. Pour chaque élément todo, un élément de liste (`<li>`) est créé avec une `key` unique définie sur la valeur de l'élément todo.
5. L'élément todo lui-même est ensuite affiché à l'intérieur de l'élément de liste.

Ce composant récupère le tableau `todos` du contexte en utilisant le hook `useTodo`. S'il n'y a pas de todos, il affiche un message. S'il y a des todos, il rend une liste non ordonnée et la remplit avec des éléments de liste pour chaque élément todo.

![Ajout d'éléments todo et affichage des notifications toast](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-5-ff3ed7ffc5.gif)
_Ajout d'éléments todo et affichage des notifications toast_

Bon travail jusqu'à présent ! Vous avez maintenant une application todo fonctionnelle de base. Il est temps de passer à la vitesse supérieure et d'ajouter quelques fonctionnalités passionnantes pour améliorer encore davantage votre application.

## Comment définir une interface pour les éléments Todo

Dans cette section, vous allez construire sur le contexte existant de la section précédente et l'améliorer pour créer un élément todo plus complexe avec des fonctionnalités supplémentaires.

Chaque élément todo se compose de trois attributs :

* **id** : une chaîne unique qui sert d'identifiant pour l'élément
* **text** : une simple chaîne représentant le contenu de l'élément todo
* **status** : le statut de l'élément todo, qui peut être soit "undone" soit "completed"

Sur la base des informations ci-dessus, l'interface todo appropriée serait la suivante :

```ts
interface Todo {
  id: string
  text: string
  status: 'undone' | 'completed'
}
```

Pour implémenter l'interface Todo dans votre contexte, nous allons apporter les mises à jour et modifications nécessaires pour utiliser efficacement ce contexte amélioré :

```tsx
//📂./src/context/TodoContext.tsx

import React, { createContext, useState } from 'react'
import { nanoid } from 'nanoid'
import { useLocalStorage } from 'usehooks-ts'

interface TodoContextProps {
  todos: Todo[]
  addTodo: (text: string) => void
}

export interface Todo {
  id: string
  text: string
  status: 'undone' | 'completed'
}

export const TodoContext = createContext<TodoContextProps | undefined>(
  undefined,
)

export const TodoProvider = (props: { children: React.ReactNode }) => {
  const [todos, setTodos] = useState<Todo[]>([])

  // ::: AJOUTER UN NOUVEAU TODO :::
  const addTodo = (text: string) => {
    const newTodo: Todo = {
      id: nanoid(),
      text,
      status: 'undone',
    }

    setTodos([...todos, newTodo])
  }

  const value: TodoContextProps = {
    todos,
    addTodo,
  }

  return (
    <TodoContext.Provider value={value}>{props.children}</TodoContext.Provider>
  )
}

```

Voici une explication de ce qui a changé dans le contexte :

**Interface Todo :**

* L'interface Todo définit la structure d'un élément todo.
* Elle se compose de trois propriétés : id (une chaîne), text (une chaîne représentant le contenu de l'élément todo), et status (une chaîne qui peut avoir la valeur 'undone' ou 'completed').
* Cette interface aide à garantir que les éléments todo ont des propriétés et des types de données cohérents.

**useState<Todo[]> :**

* Le hook useState est utilisé pour gérer l'état dans un composant fonctionnel.
* Dans ce cas, `useState<Todo[]>` initialise une variable d'état appelée "todos" en tant que tableau d'éléments Todo.
* La variable d'état "todos" sera utilisée pour stocker et mettre à jour les éléments todo.

**Fonction `addTodo` et variable `newTodo` :**

* La fonction addTodo est une fonction de rappel qui prend un paramètre de texte (chaîne).
* À l'intérieur de la fonction addTodo, une variable newTodo est déclarée en tant qu'objet Todo.
* Le nouvel objet Todo est créé avec un id unique généré par la fonction nanoid(), le texte fourni, et un statut initial de 'undone'.
* La fonction setTodos de useState est appelée pour mettre à jour l'état todos en ajoutant le nouvel objet newTodo au tableau existant de todos.
* Cela permet d'ajouter de nouveaux éléments todo à la liste.

Maintenant, vous devez mettre à jour les composants `<TodoList />` pour refléter les modifications que vous avez apportées au contexte :

```tsx
//📂./src/components/TodoList.tsx

import { useTodo } from '../context/useTodo'
import { SiStarship } from 'react-icons/si'

export const TodoList = () => {
  const { todos } = useTodo()

  if (!todos.length) {
    return (
      <div className="max-w-lg px-5 m-auto">
        <h1 className="flex flex-col items-center gap-5 px-5 py-10 text-xl font-bold text-center rounded-xl bg-zinc-900">
          <SiStarship className="text-5xl" />
          Vous n'avez rien à faire !
        </h1>
      </div>
    )
  }

  return (
    <ul className="grid max-w-lg gap-2 px-5 m-auto">
      {todos.map(todo => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  )
}

```

Avec ce code mis à jour, l'id du todo est maintenant utilisé comme la prop key pour chaque élément todo rendu, et le texte du todo est utilisé pour afficher le contenu de chaque élément todo.

Maintenant, créons un composant React personnalisé pour afficher correctement chaque élément todo et introduisons des fonctionnalités supplémentaires comme l'édition, la suppression et la mise à jour des éléments todo individuels dans notre application.

## Comment construire un composant React personnalisé pour afficher les éléments Todo

Dans cette section, vous allez créer un composant React personnalisé qui gère l'affichage et la gestion de chaque élément todo individuel.

Ouvrez `components/TodoItem.tsx` et ajoutez le code suivant :

```tsx
//📂./src/components/TodoItem.tsx

export const TodoItem = (props: { todo: Todo }) => {
  const { todo } = props

  return (
    <motion.li
      layout
      className={cn(
        'p-5 rounded-xl bg-zinc-900',
        todo.status === 'completed' && 'bg-opacity-50 text-zinc-500',
      )}
    >
      <motion.span
        layout
        style={{
          textDecoration: todo.status === 'completed' ? 'line-through' : 'none',
        }}
      >
        {todo.text}
      </motion.span>
    </motion.li>
  )
}

```

`<TodoItem />` est responsable de l'affichage d'un élément todo individuel :

* Le composant prend une prop appelée `props`, qui est un objet contenant une propriété appelée `todo`. La propriété `todo` est de type `Todo`, représentant un seul élément todo.
* À l'intérieur du composant, la propriété `todo` est extraite de l'objet `props` en utilisant la déstructuration.
* Le composant `motion.li` est utilisé depuis Framer Motion pour fournir des animations. Il représente un élément de liste (`<li>`) et prend en charge les animations de disposition.
* L'attribut `className` utilise la fonction utilitaire `cn` (du module `classnames`) pour appliquer conditionnellement des classes CSS en fonction de `todo.status`. Si le todo est terminé, il ajoute des classes pour un arrière-plan semi-transparent et une couleur de texte.
* À l'intérieur de l'élément de liste, un composant `motion.span` est utilisé pour envelopper le texte du todo. Il prend également en charge les animations de disposition.
* Le style de l'élément span est défini en fonction de `todo.status`. Si le todo est terminé, une décoration de texte barré est appliquée.
* L'expression `{todo.text}` affiche le contenu textuel de l'élément todo.

TodoItem reçoit un élément todo en tant que prop et le rend avec des animations, un style et des classes CSS conditionnelles en fonction du statut du todo.

Maintenant, modifions le composant `<TodoList />` pour utiliser le composant `<TodoItem />` :

```tsx
//📂./src/components/TodoList.tsx

import { TodoItem } from './TodoItem'
import { useTodo } from '../context/useTodo'
import { SiStarship } from 'react-icons/si'
import { motion } from 'framer-motion'

export const TodoList = () => {
  const { todos } = useTodo()

  if (!todos.length) {
    return (
      <div className="max-w-lg px-5 m-auto">
        <h1 className="flex flex-col items-center gap-5 px-5 py-10 text-xl font-bold text-center rounded-xl bg-zinc-900">
          <SiStarship className="text-5xl" />
          Vous n'avez rien à faire !
        </h1>
      </div>
    )
  }

  return (
    <motion.ul className="grid max-w-lg gap-2 px-5 m-auto">
      {todos.map(todo => (
        <TodoItem todo={todo} key={todo.id} />
      ))}
    </motion.ul>
  )
}

```

Voici une explication de ce qui a changé dans le `<TodoList />` :  
  
**Importation de dépendances supplémentaires :**

* Le code importe maintenant le composant `motion` de la bibliothèque `framer-motion`. Cela permet d'avoir des animations dans le composant.

**Rendu du composant TodoItem :**

* Auparavant, les éléments todo étaient rendus en tant qu'éléments de liste (`<li>`) directement dans le composant TodoList.
* Dans la version mise à jour, le composant TodoItem est importé (`import { TodoItem } from './TodoItem'`) et utilisé pour rendre chaque élément todo.
* Le composant TodoItem reçoit la prop `todo`, qui représente un élément todo individuel.
* La prop `key` est également fournie à chaque composant TodoItem, garantissant un identifiant unique pour chaque élément todo rendu.

**Enveloppement de la liste avec le composant motion :**

* L'élément `<ul>` est maintenant enveloppé avec le composant `<motion.ul>` pour activer les animations en utilisant la bibliothèque `framer-motion`.
* Cela permet des transitions dynamiques et fluides lors de l'ajout, de la suppression ou de la mise à jour des éléments todo.

Dans l'ensemble, le composant TodoList mis à jour introduit des animations en utilisant le composant `motion` de `framer-motion` et remplace le rendu direct des éléments todo par le composant `<TodoItem />`.

Maintenant que vous avez réussi à créer le composant `<TodoItem />`, concentrons-nous sur l'implémentation des fonctionnalités nécessaires pour permettre l'édition, la suppression et la mise à jour de chaque élément todo en utilisant le Todo Context et le composant TodoItem.

## Comment implémenter les fonctionnalités : Éditer, Supprimer et Mettre à jour les éléments Todo

Dans cette section, vous allez améliorer votre application Todo en incorporant des fonctionnalités supplémentaires. 

Tout d'abord, vous allez implémenter la logique nécessaire dans le contexte todo pour gérer ces fonctionnalités. Ensuite, vous allez ajouter le JSX correspondant au composant `<TodoItem />` pour introduire l'interactivité et permettre aux utilisateurs d'interagir avec l'application.

Comme vous vous en souvenez, vous avez utilisé le contexte pour gérer l'ajout d'éléments todo à l'application, et vous allez suivre une approche similaire pour les fonctionnalités d'édition, de suppression et de mise à jour. 

La logique de ces actions sera encapsulée dans le contexte todo, et le hook useTodo sera utilisé pour exploiter cette logique dans le composant `<TodoItem />`. Vous allez également stocker les éléments todo dans le stockage local du navigateur pour vous assurer que les utilisateurs ne perdent pas leur progression lorsqu'ils quittent l'application.

Ouvrez `context/TodoContext.tsx` et ajoutez le code suivant :

```tsx
// 📂./src/context/TodoContext.tsx

import React, { createContext } from 'react'
import { nanoid } from 'nanoid'
import { useLocalStorage } from 'usehooks-ts'

interface TodoContextProps {
  todos: Todo[]
  addTodo: (text: string) => void
  deleteTodo: (id: string) => void
  editTodo: (id: string, text: string) => void
  updateTodoStatus: (id: string) => void
}

export interface Todo {
  id: string
  text: string
  status: 'undone' | 'completed'
}

export const TodoContext = createContext<TodoContextProps | undefined>(
  undefined,
)

export const TodoProvider = (props: { children: React.ReactNode }) => {
  const [todos, setTodos] = useLocalStorage<Todo[]>('todos', [])

  // ::: AJOUTER UN NOUVEAU TODO :::
  const addTodo = (text: string) => {
    const newTodo: Todo = {
      id: nanoid(),
      text,
      status: 'undone',
    }

    setTodos([...todos, newTodo])
  }

  // ::: SUPPRIMER UN TODO :::
  const deleteTodo = (id: string) => {
    setTodos(prevTodos => prevTodos.filter(todo => todo.id !== id))
  }

  // ::: MODIFIER UN TODO :::
  const editTodo = (id: string, text: string) => {
    setTodos(prevTodos => {
      return prevTodos.map(todo => {
        if (todo.id === id) {
          return { ...todo, text }
        }
        return todo
      })
    })
  }

  // ::: METTRE À JOUR LE STATUT DU TODO :::
  const updateTodoStatus = (id: string) => {
    setTodos(prevTodos => {
      return prevTodos.map(todo => {
        if (todo.id === id) {
          return {
            ...todo,
            status: todo.status === 'undone' ? 'completed' : 'undone',
          }
        }
        return todo
      })
    })
  }

  const value: TodoContextProps = {
    todos,
    addTodo,
    deleteTodo,
    editTodo,
    updateTodoStatus,
  }

  return (
    <TodoContext.Provider value={value}>{props.children}</TodoContext.Provider>
  )
}
```

Voici une explication de ce qui se passe :

**Définition de TodoContextProps :**

* TodoContextProps est une interface qui spécifie la structure de la valeur du TodoContext.
* Elle inclut des propriétés telles que todos (un tableau d'éléments Todo) et des fonctions pour ajouter, supprimer, modifier et mettre à jour le statut des éléments todo.

**Implémentation de `addTodo` :**

* La fonction addTodo prend un paramètre text, génère un ID unique en utilisant nanoid, et crée un nouvel objet todo avec le texte fourni et un statut initial de 'undone'.
* Elle utilise la fonction setTodos, fournie par useLocalStorage, pour mettre à jour l'état todos en ajoutant le newTodo au tableau existant de todos.

**Implémentation de `deleteTodo` :**

* La fonction deleteTodo prend un paramètre id et utilise la fonction setTodos pour filtrer l'élément todo avec l'id correspondant de l'état todos.

**Implémentation de `editTodo` :**

* La fonction editTodo prend un paramètre id et text.
* Elle utilise la fonction setTodos pour mapper l'état todos et mettre à jour le texte de l'élément todo avec l'id correspondant.

**Implémentation de `updateTodoStatus` :**

* La fonction updateTodoStatus prend un paramètre id.
* Elle utilise la fonction setTodos pour mapper l'état todos et basculer le statut de l'élément todo avec l'id correspondant entre 'undone' et 'completed'.

**Fourniture de la valeur et rendu des composants enfants :**

* L'objet value est créé avec le tableau todos et les fonctions définies.
* Il est passé en tant que prop value au composant TodoContext.Provider pour fournir les valeurs définies à ses composants enfants imbriqués.

En résumé, le `TodoContext` et le `TodoProvider` gèrent l'état et la logique liés à la gestion des éléments todo. Ils fournissent les fonctions et données nécessaires via le TodoContext pour être utilisés par les composants enfants, tels que `<TodoItem />`, pour effectuer des opérations comme l'ajout, la suppression, la modification et la mise à jour des éléments todo.

Maintenant, intégrons le JSX correspondant pour permettre aux utilisateurs d'interagir avec la logique que vous venez d'implémenter. Ouvrez `components/TodoItem.tsx` et ajoutez le code suivant :

```tsx
//📂./src/components/TodoItem.tsx

import { useEffect, useRef, useState } from 'react'
import { Todo } from '../context/TodoContext'
import { useTodo } from '../context/useTodo'
import { Input } from './Input'
import { BsCheck2Square } from 'react-icons/bs'
import { TbRefresh } from 'react-icons/tb'
import { FaRegEdit } from 'react-icons/fa'
import { RiDeleteBin7Line } from 'react-icons/ri'
import { toast } from 'react-hot-toast'
import cn from 'classnames'
import { motion } from 'framer-motion'

export const TodoItem = (props: { todo: Todo }) => {
  const { todo } = props

  const [editingTodoText, setEditingTodoText] = useState<string>('')
  const [editingTodoId, setEditingTodoId] = useState<string | null>(null)

  const { deleteTodo, editTodo, updateTodoStatus } = useTodo()

  const editInputRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (editingTodoId !== null && editInputRef.current) {
      editInputRef.current.focus()
    }
  }, [editingTodoId])

  const handleEdit = (todoId: string, todoText: string) => {
    setEditingTodoId(todoId)
    setEditingTodoText(todoText)

    if (editInputRef.current) {
      editInputRef.current.focus()
    }
  }

  const handleUpdate = (todoId: string) => {
    if (editingTodoText.trim() !== '') {
      editTodo(todoId, editingTodoText)
      setEditingTodoId(null)
      setEditingTodoText('')
      toast.success('Todo mis à jour avec succès !')
    } else {
      toast.error('Le champ Todo ne peut pas être vide !')
    }
  }

  const handleDelete = (todoId: string) => {
    deleteTodo(todoId)
    toast.success('Todo supprimé avec succès !')
  }

  const handleStatusUpdate = (todoId: string) => {
    updateTodoStatus(todoId)
    toast.success('Statut du Todo mis à jour avec succès !')
  }

  return (
    <motion.li
      layout
      key={todo.id}
      className={cn(
        'p-5 rounded-xl bg-zinc-900',
        todo.status === 'completed' && 'bg-opacity-50 text-zinc-500',
      )}
    >
      {editingTodoId === todo.id ? (
        <motion.div layout className="flex gap-2">
          <Input
            ref={editInputRef}
            type="text"
            value={editingTodoText}
            onChange={e => setEditingTodoText(e.target.value)}
          />
          <button
            className="px-5 py-2 text-sm font-normal text-orange-300 bg-orange-900 border-2 border-orange-900 active:scale-95 rounded-xl"
            onClick={() => handleUpdate(todo.id)}
          >
            Mettre à jour
          </button>
        </motion.div>
      ) : (
        <div className="flex flex-col gap-5">
          <motion.span
            layout
            style={{
              textDecoration:
                todo.status === 'completed' ? 'line-through' : 'none',
            }}
          >
            {todo.text}
          </motion.span>
          <div className="flex justify-between gap-5 text-white">
            <button onClick={() => handleStatusUpdate(todo.id)}>
              {todo.status === 'undone' ? (
                <span className="flex items-center gap-1">
                  <BsCheck2Square />
                  Marquer comme terminé
                </span>
              ) : (
                <span className="flex items-center gap-1">
                  <TbRefresh />
                  Marquer comme non terminé
                </span>
              )}
            </button>
            <div className="flex items-center gap-2">
              <button
                onClick={() => handleEdit(todo.id, todo.text)}
                className="flex items-center gap-1 "
              >
                <FaRegEdit />
                Modifier
              </button>
              <button
                onClick={() => handleDelete(todo.id)}
                className="flex items-center gap-1 text-red-500"
              >
                <RiDeleteBin7Line />
                Supprimer
              </button>
            </div>
          </div>
        </div>
      )}
    </motion.li>
  )
}
```

Concentrons-nous sur les fonctions `handleEdit`, `handleUpdate`, `handleDelete` et `handleStatusUpdate` et comment elles fonctionnent :

**Fonction `handleEdit` :**

Cette fonction est appelée lorsque l'utilisateur clique sur le bouton "Modifier". Elle prend `todoId` (identifiant unique de l'élément todo) et `todoText` (texte actuel de l'élément todo) comme paramètres. 

Elle définit l'état `editingTodoId` sur `todoId` et l'état `editingTodoText` sur `todoText`. De plus, si `editInputRef` (une référence au champ de saisie) existe, elle met le focus sur le champ de saisie en utilisant la méthode `focus`.

**Fonction `handleUpdate` :**

Cette fonction est appelée lorsque l'utilisateur clique sur le bouton "Mettre à jour" après avoir modifié un élément todo. Elle prend `todoId` comme paramètre. 

Elle vérifie d'abord si le `editingTodoText` (sans les espaces) n'est pas vide. Si ce n'est pas le cas, elle appelle la fonction `editTodo` du hook `useTodo`, en passant `todoId` et `editingTodoText` comme arguments. Elle réinitialise ensuite les états `editingTodoId` et `editingTodoText` à null et une chaîne vide, respectivement. 

Enfin, elle affiche un message toast de succès si la mise à jour a réussi ou un message toast d'erreur si le champ todo était vide.

**Fonction `handleDelete` :**

Cette fonction est appelée lorsque l'utilisateur clique sur le bouton "Supprimer". Elle prend `todoId` comme paramètre. Elle appelle la fonction `deleteTodo` du hook `useTodo`, en passant `todoId` comme argument. Elle affiche ensuite un message toast de succès indiquant que l'élément todo a été supprimé avec succès.

**Fonction `handleStatusUpdate` :** 

Cette fonction est appelée lorsque l'utilisateur clique sur le bouton "Marquer comme terminé" ou "Marquer comme non terminé". Elle prend `todoId` comme paramètre. 

Elle appelle la fonction `updateTodoStatus` du hook `useTodo`, en passant `todoId` comme argument. Elle affiche ensuite un message toast de succès indiquant que le statut de l'élément todo a été mis à jour avec succès.

Ces fonctions gèrent les interactions et les actions liées à la modification, la mise à jour, la suppression et la mise à jour du statut d'un élément todo dans le composant TodoItem.

Le JSX affiche le texte du todo avec l'option de modifier, supprimer et mettre à jour son statut. L'apparence et le comportement de l'élément todo sont déterminés par les valeurs de l'objet `todo` et les variables d'état du composant. 

Si le todo est en cours de modification, un champ de saisie et un bouton "Mettre à jour" sont affichés. Sinon, le texte du todo est affiché, et des boutons pour le marquer comme terminé ou non terminé, le modifier et le supprimer sont disponibles. 

Les fonctions `handleEdit`, `handleUpdate`, `handleDelete` et `handleStatusUpdate` sont utilisées comme gestionnaires d'événements pour ces boutons, permettant à l'utilisateur d'interagir avec et de modifier l'élément todo.

![Application todo finale, un utilisateur ajoute un élément, puis le modifie et le supprime afin d'afficher les fonctionnalités de l'application](https://www.freecodecamp.org/news/content/images/2023/07/ezgif-1-f7b9438717.gif)
_Résultat final_

Félicitations ! Vous avez réussi à créer une belle application Todo avec les fonctionnalités essentielles. 

Avec les connaissances acquises dans cet article, vous êtes maintenant bien équipé pour améliorer et personnaliser davantage l'application en fonction de vos besoins et préférences spécifiques.

## Conclusion 

Tout au long de cet article, nous avons couvert les bases du développement React avec TypeScript et appris à créer une application Todo entièrement fonctionnelle. 

Nous avons exploré des concepts tels que la gestion d'état, le contexte et les hooks, vous permettant d'ajouter, de modifier, de supprimer et de mettre à jour des éléments todo. 

Avec ces connaissances, vous êtes maintenant prêt à appliquer ces principes à vos projets futurs et à construire des applications sécurisées par les types avec React. Continuez à explorer et à expérimenter de nouvelles fonctionnalités pour faire passer votre application au niveau supérieur. 

Vous pouvez me suivre sur [Twitter](https://twitter.com/Yazdun) où je partage d'autres conseils utiles sur le développement web. Bon codage !