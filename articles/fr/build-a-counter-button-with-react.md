---
title: Comment créer un bouton compteur avec React, TailwindCSS et TypeScript
subtitle: ''
author: Devin Lane
co_authors: []
series: null
date: '2024-07-10T14:41:14.000Z'
originalURL: https://freecodecamp.org/news/build-a-counter-button-with-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Build-a-counter-button-with-React-6-.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
- name: tailwind
  slug: tailwind
- name: TypeScript
  slug: typescript
seo_title: Comment créer un bouton compteur avec React, TailwindCSS et TypeScript
seo_desc: "How can you keep track of the number of times a user clicks a button? How\
  \ are the hearts on Instagram or the likes on Facebook counted? \nIn this tutorial,\
  \ we will build a button that tracks the number of times a button has been clicked.\
  \ Along the way..."
---

Comment pouvez-vous suivre le nombre de fois qu'un utilisateur clique sur un bouton ? Comment les cœurs sur Instagram ou les likes sur Facebook sont-ils comptés ? 

Dans ce tutoriel, nous allons construire un bouton qui suit le nombre de fois qu'un bouton a été cliqué. En chemin, vous apprendrez certains concepts fondamentaux de React tels que les composants, le JSX, le passage de props entre composants et la gestion de l'état avec les hooks. Vous recevrez également de brèves introductions à Tailwind et TypeScript.

Ce tutoriel s'appuie sur des exemples et des concepts décrits dans la section "Learn" de la documentation React, que vous pouvez trouver [ici](https://react.dev/learn).

### Prérequis

* Une familiarité de base avec JavaScript, comme la manipulation de variables, de fonctions, de tableaux et d'objets.
* Une familiarité de base avec CSS et HTML.
* Une familiarité de base avec la ligne de commande.
* [Node](https://nodejs.org/en) installé.
* Un éditeur de code de votre choix (j'utiliserai [Visual Studio Code](https://code.visualstudio.com/) ici)

## Table des matières

1. [Comment créer le bouton compteur](#heading-chapter-1-comment-creer-le-bouton-compteur)
2. [Comment refactoriser le projet](#heading-chapter-2-comment-refactoriser-le-projet)
3. [Deux composants avec un état indépendant et partagé](#heading-chapter-3-deux-composants-avec-un-etat-independant-et-partage)
4. [Comment ajouter les deux paires de boutons à notre site](#heading-chapter-4-comment-ajouter-les-deux-paires-de-boutons-a-notre-site)
5. [Comment déployer le site sur Netlify](#heading-chapter-5-comment-deployer-le-site-sur-netlify)

## Chapitre 1 : Comment créer le bouton compteur

### Qu'est-ce que React ?

Avant de plonger, définissons React. [React](https://react.dev/) est une bibliothèque JavaScript pour créer des interfaces utilisateur à partir de morceaux appelés _composants_. Les composants sont des fonctions JavaScript qui peuvent recevoir et afficher des données de manière interactive pour vos utilisateurs.

### Configuration du projet

Nous allons utiliser [Next.js](https://nextjs.org/) pour notre configuration React locale.

Dans le répertoire où vous souhaitez stocker ce projet, ouvrez votre terminal et exécutez la commande suivante :

```zsh
npx create-next-app@latest
```

Nommez votre projet comme vous le souhaitez, et répondez aux commandes comme suit :

```zsh
What is your project named? react-counter-button
Would you like to use TypeScript? Yes
Would you like to use ESLint? Yes
Would you like to use Tailwind CSS? Yes
Would you like to use `src/` directory? No
Would you like to use App Router? (recommended) Yes
Would you like to customize the default import alias (@/*)? No
```

Maintenant, entrons dans notre répertoire de projet avec `cd` :

```zsh
cd react-counter-button
```

Et lancez le projet dans Visual Studio Code :

```zsh
code .
```

Note : si vous n'avez pas la commande `code` dans votre PATH, vous pouvez appuyer sur ⇧⌘P (Ctrl+Shift+P sur Windows/Linux) et taper 'Shell Command: Install 'code' command in PATH'. Alternativement, vous pouvez faire glisser le dossier sur l'icône de Visual Studio Code dans MacOS. Ou, dans Visual Studio Code, vous pouvez sélectionner Fichier -> Ouvrir, et trouver "react-counter-button", ou le nom de votre projet.

Dans votre terminal, exécutez :

```zsh
npm run dev
```

Ouvrez votre navigateur sur `localhost:3000` et vous devriez voir la page suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-14-at-7.10.35-PM.png)
_Boilerplate de Next.js_

Le projet est maintenant opérationnel. De retour dans notre éditeur de code, nous pouvons commencer le travail.

### Supprimer le boilerplate

Dans `app/page.tsx`, supprimons la majeure partie du code boilerplate à l'exception des deux balises `main`. Ajoutons ensuite un titre pour notre projet dans une balise `h1` entre les balises `main`. Notre code devrait ressembler à ceci :

```js
export default function Home() {
    return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">
            <h1>React Counter Button</h1>
        </main>
    );
}
```

Voici ce que nous devrions maintenant voir :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-16-at-8.22.30-PM.png)
_État initial de notre projet_

### Écrire notre premier composant

Créons notre premier composant. Un composant React est une fonction qui renvoie du balisage. En dessous et en dehors de la portée de notre fonction `Home`, écrivons ce qui suit :

```js
function Button() {
    return <button>I have been clicked X times</button>;
}
```

Ici, nous avons une fonction `Button` qui renvoie du balisage en JSX. Le JSX ressemble beaucoup au HTML, mais il peut afficher du contenu dynamique et possède des règles plus strictes que le HTML. Vous pouvez en apprendre davantage sur le JSX dans la documentation React [ici](https://react.dev/learn/writing-markup-with-jsx).

La fonction `Button` doit commencer par une majuscule pour être reconnue comme un composant React valide. Cela le distingue d'une balise HTML, qui est en minuscules.

Vous remarquerez que nous ne voyons toujours aucun changement sur notre page web – nous devons rendre ce composant pour le voir à l'écran.

Nous pouvons utiliser notre composant `Button` comme s'il s'agissait d'une balise HTML que nous avons créée. Si nous nichons le composant `Button` à l'intérieur du composant `Home`, nous devrions le voir à l'écran :

```js
export default function Home() {
    return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">
            <h1>React Counter Button</h1>
            <Button />
        </main>
    );
}

function Button() {
    return <button>I have been clicked X times</button>;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-at-6.37.57-PM.png)
_Rendu du composant `Button` (avec un CSS loin d'être idéal)_

### Styliser notre premier composant avec Tailwind

Vous remarquerez que le bouton est en bas de l'écran. C'est parce que les styles sur `main` incluent `justify-between` dans la direction `flex-col`. Si nous supprimons `justify-between`, nous devrions voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-at-6.36.57-PM.png)
_Amélioration du CSS de l'état initial de notre application_

Vous pouvez en savoir plus sur l'alignement des éléments dans un flexbox sur MDN [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Aligning_Items_in_a_Flex_Container).

Vous remarquerez également que le bouton n'a pas de style. C'est parce que [Tailwind](https://tailwindcss.com/) supprime le style par défaut des boutons dans le cadre de ses styles "preflight". Si vous êtes curieux de voir d'où viennent ces styles, vous pouvez ouvrir `node_modules/tailwindcss/src/css/preflight.css` et consulter la ligne ~193 (permalink sur GitHub [ici](https://github.com/tailwindlabs/tailwindcss/blob/332347ed834a3078547923ccfddc1c22035011b6/packages/tailwindcss/preflight.css#L182)) :

```css
/*
1. Corriger l'incapacité à styliser les types cliquables dans iOS et Safari.
2. Supprimer les styles de bouton par défaut.
*/

button,
[type='button'],
[type='reset'],
[type='submit'] {
  -webkit-appearance: button; /* 1 */
  background-color: transparent; /* 2 */
  background-image: none; /* 2 */
}
```

Nous n'allons pas modifier les styles à l'intérieur de `node_modules` – nous allons plutôt ajouter notre propre style au composant Button. L'un des avantages de Tailwind est que notre CSS est co-localisé avec notre JavaScript, ce qui facilite les modifications rapides de style par rapport à l'ouverture d'un fichier de feuille de style séparé.

Apportons les modifications suivantes :

```js
export default function Home() {
    return (
        <main className="flex min-h-screen flex-col items-center p-24 gap-4">
            <h1>React Counter Button</h1>
            <Button />
        </main>
    );
}

function Button() {
    return (
        <button className="bg-blue-500 hover:bg-blue-700 rounded text-white font-bold px-4 py-2">
            I have been clicked X times
        </button>
    );
}
```

Nous avons ajouté des styles à notre bouton, et nous avons également ajouté un `gap-4` à notre flexbox parent `main` pour créer un espace entre le `h1` et le `button`. (Vous pouvez en savoir plus sur la propriété CSS "gap" sur MDN [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/gap).) Nous devrions maintenant voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-at-6.49.22-PM.png)
_Visualisation de notre composant `Button` stylisé_

### Attendez, mais qu'est-ce que Tailwind ?

Maintenant que nous avons stylisé notre composant bouton et espacé les éléments, réfléchissons à ce qu'est Tailwind et à ce qu'il nous a apporté. [Tailwind](https://tailwindcss.com/) est un Framework CSS qui fournit un ensemble de classes "utilitaires" que nous pouvons utiliser pour styliser chaque élément.

Mais qu'est-ce qu'une classe utilitaire ? Vous verrez que pour styliser notre bouton, nous avons ajouté des classes telles que `bg-blue-500` – qui correspond à la propriété CSS `background-color` réglée sur bleu, et `rounded` – qui correspond à `border-radius: 0.25rem`.

Chaque classe est définie selon son _utilité_ : changer la couleur d'arrière-plan, le rayon de bordure, et ainsi de suite. En ajoutant ces classes utilitaires à nos éléments, nous arrivons aux styles souhaités.

Tailwind se distingue d'autres frameworks, comme Bootstrap, qui fournissent des classes prédéfinies pour des éléments tels que les boutons. Avec Bootstrap, nous ajouterions une classe `btn` pour obtenir un bouton stylisé. Et bien sûr, avec du CSS standard, nous ajouterions probablement une classe personnalisée (peut-être appelée `button`) à notre élément et créerions des règles CSS dans une feuille de style séparée.

Revenons à notre projet : jusqu'à présent, nous avons configuré un projet React avec Next.js, créé notre premier composant React et stylisé notre bouton avec Tailwind. Comment introduire la fonctionnalité de compteur ?

### Comment ajouter de l'état

Pour afficher le nombre de fois qu'un bouton a été cliqué, nous devons utiliser un gestionnaire d'événements et nous avons besoin d'un moyen de gérer l'_état_.

L'[état](https://react.dev/learn/state-a-components-memory) est une mémoire spécifique au composant. Dans notre exemple, c'est ainsi que le bouton se souviendra du nombre de fois qu'il a été cliqué. En utilisant une fonction spéciale React appelée "[hook](https://react.dev/reference/react/hooks)", nous déclenchons un nouveau rendu et conservons les données entre les rendus – le hook `[useState](https://react.dev/reference/react/useState)` est fourni par React à cet effet.

En haut de notre fichier `page.tsx`, importons `useState` :

`import { useState } from "react"`

et à l'intérieur de notre composant `Button`, ajoutons ce qui suit :

```js
function Button() {
  const [count, setCount] = useState(0)
    return (
        <button className="bg-blue-500 hover:bg-blue-700 rounded py-2 px-4 text-white font-bold">
            I have been clicked X times
        </button>
    );
}
```

Analysons ce que nous avons ici :

* Nous utilisons l'[affectation par décomposition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) pour obtenir la valeur de `count` et la fonction `setCount` à partir de `useState`. La convention est de nommer ces deux valeurs `quelqueChose` et `setQuelqueChose`, bien que nous puissions les nommer n'importe comment.
* L'argument passé à `useState` est la valeur initiale de notre variable d'état. Ici, nous l'avons réglée sur 0.
* `count` est notre état actuel.
* `setCount` est la fonction qui met à jour notre état et déclenche un nouveau rendu.

Cependant, si vous cliquez sur enregistrer, vous verrez l'erreur suivante dans votre terminal et dans votre navigateur :

```zsh
You're importing a component that needs useState. It only works in a Client Component but none of its parents are marked with "use client", so they're Server Components by default.
Learn more: https://nextjs.org/docs/getting-started/react-essentials

   ╭─[/[...your project path]/src/app/page.tsx:1:1]
 1 │ import { useState } from "react";
   ·          ────────
 2 │ 
 3 │ export default function Home() {
 4 │     return (
   ╰────

Maybe one of these should be marked as a client entry with "use client":
  ./src/app/page.tsx
```

Cela est dû à l'utilisation par Next.js des [React Server Components](https://www.joshwcomeau.com/react/server-components/), sur lesquels vous pouvez en apprendre davantage [ici](https://nextjs.org/docs/app/building-your-application/rendering). Les React Server Components sont un vaste sujet, mais l'essentiel est que, par défaut, les composants sont des Server Components dans Next.js et `useState` ne fonctionne que dans un Client Component. Si nous écrivons la directive `"use client"` en haut de notre fichier `page.tsx`, nous résolvons l'erreur.

### Comment évaluer du JavaScript dans du JSX

Si nous cliquons sur le bouton, nous ne voyons toujours pas les chiffres se mettre à jour. C'est parce que nous avons besoin d'un moyen d'[interpoler](https://react.dev/learn/javascript-in-jsx-with-curly-braces) (ou évaluer) du JavaScript à l'intérieur de notre balisage JSX. Entrent en scène les accolades : `{}`.

Nous pouvons utiliser des accolades pour "s'échapper" vers le JavaScript à partir du balisage JSX. De cette façon, nous pouvons évaluer des expressions JavaScript (comme l'ajout à un compteur) et afficher dynamiquement des données dans nos composants. Voici ce que nous allons faire :

```js
function MyButton() {
    const [count, setCount] = useState(0);
    return (
        <button className="bg-blue-500 hover:bg-blue-700 rounded py-2 px-4 text-white font-bold">
            I have been clicked {count} times
        </button>
    );
}
```

Nous avons ajouté `{count}` pour évaluer la valeur de `count` provenant de `useState` à l'intérieur de notre bouton. Nous devrions voir ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-26-at-4.46.56-PM.png)
_Affichage des données en JSX avec des accolades {}_

Nous voyons un 0 – cela provient de la variable `count` que nous avons décomposée de notre hook `useState`, que nous avons initialement réglée sur 0. Nous avons réussi à interpoler le JavaScript dans notre balisage JSX !

### Gestion des événements

Vous remarquerez que si nous cliquons sur le bouton, il ne se passe toujours rien. Comment faire pour que le nombre s'incrémente lorsque nous cliquons dessus ?

Pour cela, nous allons utiliser une [fonction gestionnaire d'événements](https://react.dev/learn/responding-to-events#adding-event-handlers) ainsi que la fonction de modification (que nous avons nommée `setCount`) que nous obtenons de `useState` :

```js
function MyButton() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }
    return (
        <button className="bg-blue-500 hover:bg-blue-700 rounded py-2 px-4 text-white font-bold">
            I have been clicked {count} times
        </button>
    );
}
```

Ce que nous avons fait ici est d'ajouter une fonction `handleClick` pour mettre à jour l'état de la variable `count`. La convention est de nommer les fonctions gestionnaires d'événements `handle` suivi du nom de votre événement (par exemple, `handleClick`). 

`[setCount](https://react.dev/reference/react/useState#setstate)` est une fonction `set` spéciale renvoyée par `useState` qui mettra à jour l'état de la variable `count` avec la valeur que nous passons en argument. Par exemple, nous pourrions appeler `setCount(2)`, et cela mettrait à jour `count` à 2. `setCount(7)` le mettrait à 7, et ainsi de suite.

Nous appelons `setCount(count + 1)`, ce qui s'évalue en `setCount(0 + 1)`, car la valeur initiale de `count` est 0. Lors du clic suivant, `count` vaudra 1, donc nous appellerons `setCount(1 + 1)`, et le clic suivant appellera `setCount(2 + 1)` et ainsi de suite.

Cela nous permet de mettre à jour le compteur à chaque clic. Mais, si vous cliquez, vous remarquerez que _toujours_ rien ne se passe – pourquoi ? Prenez peut-être un moment pour essayer de comprendre par vous-même avant de continuer la lecture afin de mieux ancrer le concept.

### Comment passer un gestionnaire d'événements comme prop à votre JSX

En regardant notre code, il n'y a pas de relation entre l'utilisateur qui clique sur le bouton et la fonction `handleClick`. Nous devons passer le gestionnaire d'événements `handleClick` à la propriété `onClick` sur le bouton ! Ajoutons cela ici :

```js
function MyButton() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }
    return (
        <button
            onClick={handleClick}
            className="bg-blue-500 hover:bg-blue-700 rounded py-2 px-4 text-white font-bold"
        >
            I have been clicked {count} times
        </button>
    );
}
```

Remarquez que nous n'avons pas écrit `onClick={handleClick()}`. Nous n'appelons pas la fonction nous-mêmes ici – nous la transmettons. C'est une distinction importante, car React appelle la fonction pour nous lorsque l'utilisateur clique sur le bouton, au lieu qu'elle ne se déclenche immédiatement.

Vous pouvez en savoir plus sur le passage de props aux composants dans la documentation React [ici](https://react.dev/learn/passing-props-to-a-component).

### Notre projet fonctionnel

Essayez maintenant, le bouton fonctionne !

Vous avez maintenant un bouton qui met à jour son compteur lorsque vous cliquez dessus. Cela montre l'utilisation de l'interpolation de JavaScript dans JSX à l'aide d'accolades, la création de votre propre composant et son imbrication dans d'autres composants, l'utilisation de l'état et des hooks dans React, ainsi que le travail avec Next.js et Tailwind. Félicitations ! ✨

![Image](https://www.freecodecamp.org/news/content/images/2024/06/react-counter-button.gif)
_Notre projet fonctionnel_

C'est le bon moment pour _committer_ nos changements avec Git. Vous pouvez fermer le processus du terminal actuel en appuyant sur `ctrl + c`, puis tapez `git add .`, suivi de `git commit -m "counter button"` ou d'un autre message significatif.

## Chapitre 2 : Comment refactoriser le projet

### Déplacer notre composant vers un autre fichier

Dans l'état actuel de notre projet, tout le code se trouve dans `app/page.tsx`. Et si nous voulions ajouter un autre composant, ou plusieurs ? Avec le temps, notre fichier `page.tsx` deviendrait volumineux et difficile à lire.

Au lieu de cela, nous pouvons diviser nos composants dans leurs propres fichiers pour faciliter la lisibilité ainsi que la modularité (réutilisation du composant à plusieurs endroits différents).

Commençons par créer un dossier `components` à la racine de notre projet pour stocker nos composants. À l'intérieur de `components`, créez un fichier appelé `button.tsx`. Ensuite, dans `app/page.tsx`, coupez (copier puis supprimer) l'intégralité du composant fonctionnel `Button` et collez-le dans `components/button.tsx`.

`components/button.tsx` devrait ressembler à ceci :

```js
function Button() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }
    return (
        <button
            onClick={handleClick}
            className="bg-blue-500 hover:bg-blue-700 rounded text-white font-bold px-4 py-2"
        >
            I have been clicked {count} times
        </button>
    );
}
```

### Corriger l'erreur d'importation de `useState`

Vous remarquerez probablement dans votre éditeur de code que `useState(0)` est souligné par des lignes rouges. Dans Visual Studio Code, si vous passez la souris dessus, vous verrez une erreur qui dit :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-07-at-6.10.44-PM.png)
_Erreur : cannot find name 'useState'_

Pourquoi ? Nous utilisons `useState` mais nous n'avons pas importé le module depuis React. L'ajout de `import { useState } from "react";` en haut de notre fichier `button.tsx` corrigera cette erreur.

Si vous regardez le début de la fonction, vous verrez que `Button()` est souligné par des lignes blanches dans Visual Studio Code. Passer la souris dessus affichera cette erreur. Réfléchissez à la raison pour laquelle cela pourrait être le cas – nous y reviendrons plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-07-at-6.13.45-PM.png)
_Erreur : 'Button' is declared but its value is never read_

### Importation et exportation de composants

Retournons dans `app/page.tsx`. Vous verrez deux erreurs ici : une sur `import { useState } from "react";` et une autre sur `<Button />`.

Abordons d'abord l'erreur `useState`. Nous utilisions `useState` à l'intérieur de notre composant `Button`, mais maintenant que nous avons déplacé ce composant dans son propre fichier, nous n'en avons plus besoin ici. Le supprimer résoudra notre erreur. Vous pouvez utiliser `cmd (ctrl sur Windows) + shift + k` pour supprimer toute la ligne dans Visual Studio Code.

Si vous avez enregistré votre `app/page.tsx`, vous verrez cette erreur dans la console :

```zsh
 ⨯ app/page.tsx (7:14) @ Button
 ⨯ ReferenceError: Button is not defined
    at Home (./app/page.tsx:19:89)
digest: "2129895745"
   5 |         <main className="flex min-h-screen flex-col items-center p-24 gap-4">
   6 |             <h1>React Counter Button</h1>
>  7 |             <Button />
     |              ^
   8 |         </main>
   9 |     );
  10 | }
 GET / 500 in 87ms
```

Pourquoi `Button` ne serait-il pas défini ? Le problème est que dans notre fichier `app/page.tsx`, nous n'avons aucun moyen d'accéder au composant `Button` situé dans `components/button.tsx`. Nous résolvons cela en exportant et en important le module approprié.

Dans `components/button.tsx`, au début de notre déclaration de fonction, ajoutons les mots-clés `export default`. Le fichier ressemblera maintenant à ceci :

```js
import { useState } from "react";

export default function Button() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }
    return (
        <button
            onClick={handleClick}
            className="bg-blue-500 hover:bg-blue-700 rounded text-white font-bold px-4 py-2"
        >
            I have been clicked {count} times
        </button>
    );
}
```

Vous remarquerez que notre erreur précédente `'Button' is declared but its value is never read` a disparu, car maintenant la valeur est lue comme une exportation par défaut.

Mais qu'avons-nous fait ici ? Qu'est-ce qu'une exportation, ou une exportation par défaut ? L'[exportation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) et l'importation nous permettent de modulariser les composants JavaScript dans leurs propres sections et de les utiliser dans d'autres.

Il en existe deux types : les exportations _par défaut_ (default) et les exportations _nommées_ (named). Chaque fichier peut avoir plusieurs exportations _nommées_ mais seulement une seule exportation _par défaut_. Vous pouvez en savoir plus sur l'importation et l'exportation de composants dans la documentation React [ici](https://react.dev/learn/importing-and-exporting-components).

Maintenant que nous avons exporté le composant de `components/button.tsx`, nous devons l'importer dans `app/page.tsx`. Visual Studio Code peut aider avec les suggestions "[intellisense](https://code.visualstudio.com/docs/editor/intellisense)" : en haut de votre fichier, si vous commencez à taper "Button", il suggérera l'importation correcte avec le bon chemin de fichier :

`import Button from "@/components/button";`

Dans Next.js, nous pouvons utiliser cette syntaxe `@/` pour référencer la racine du projet. C'est une commodité ajoutée au cas où notre importation se trouverait à plusieurs couches de fichiers de profondeur. Vous pouvez lire les exemples de la syntaxe `@/` dans la documentation de Next.js [ici](https://nextjs.org/docs/app/building-your-application/configuring/absolute-imports-and-module-aliases).

Vous verrez que nos erreurs ont disparu et que le projet fonctionne toujours ! Nous n'avons ajouté aucune nouvelle fonctionnalité, mais nous avons réussi à refactoriser notre code pour le rendre plus modulaire, lisible et maintenable.

Suivons ici les mêmes étapes pour committer nos changements, en ajoutant un message tel que `refactor: move button to its own file`.

## Chapitre 3 : Deux composants avec un état indépendant et partagé

### Deux composants avec un état indépendant

Et si nous voulions avoir deux boutons capables de compter indépendamment l'un de l'autre ? Cela illustrera la beauté de React, et l'implémentation basée sur les composants sera plus simple que de reconstruire entièrement le bouton à partir de zéro.

Dans `app/page.tsx`, nous pouvons simplement ajouter un autre `<Button />`. Vous pouvez placer votre curseur sur `<Button />` et appuyer sur `option + shift + ↓` pour créer un autre `<Button />` :

```js
"use client";

import Button from "@/components/button";

export default function Home() {
    return (
        <main className="flex min-h-screen flex-col items-center p-24 gap-4">
            <h1>React Counter Button</h1>
            <Button />
            <Button />
        </main>
    );
}
```

Vous devriez maintenant voir deux compteurs de boutons avec leur propre état indépendant :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-07-at-6.40.47-PM.png)
_Deux boutons avec un état indépendant_

La conception basée sur les composants avec React facilite la réutilisation de parties de votre application. Une victoire facile.

### Deux composants avec un état partagé

Et si nous voulions que les boutons partagent leur état et se mettent à jour ensemble ? Vous remarquerez que lorsque nous cliquons sur chaque bouton, ils s'incrémentent séparément.

Pour que les boutons partagent leur état, nous devrons déplacer leur état de chaque composant individuel "vers le haut" vers leur composant parent commun (dans ce cas, la fonction `Home` dans `app/page.tsx`). Vous entendrez également parler de cela sous le nom de "[remontée de l'état (lifting state up)](https://react.dev/learn#sharing-data-between-components)".

Coupez la logique de comptage de `components/button.tsx` et collez-la dans `app/page.tsx` à l'intérieur du corps de la fonction `Home`. Nous aurons également besoin de notre importation `useState` en haut du fichier :

```js
"use client";

import { useState } from "react";

import Button from "@/components/button";

export default function Home() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }
    return (
        <main className="flex min-h-screen flex-col items-center p-24 gap-4">
            <h1>React Counter Button</h1>
            <Button />
            <Button />
        </main>
    );
}
```

### Passer des props à un composant

Maintenant que nous avons notre état dans le composant parent de chaque bouton (`Home`), nous pouvons transmettre cet état via des _[props](https://react.dev/learn/passing-props-to-a-component)_ au composant `Button`. Nous voudrons transmettre à la fois le gestionnaire d'événements `handleClick` ainsi que la variable `count` que nous souhaitons afficher :

```js
"use client";

import { useState } from "react";

import Button from "@/components/button";

export default function Home() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }
    return (
        <main className="flex min-h-screen flex-col items-center p-24 gap-4">
            <h1>React Counter Button</h1>
            <Button count={count} onClick={handleClick} />
            <Button count={count} onClick={handleClick} />
        </main>
    );
}
```

Le `count` de `useState` est passé à la prop `count`, et la fonction `handleClick` est passée à la prop `onClick`, toutes deux sur le composant `Button`. En JSX, nous pouvons définir nos propres props (qui peuvent vous rappeler les attributs HTML) afin de pouvoir passer des données d'un composant à un autre.

Vous pourriez voir des erreurs liées à TypeScript à ce stade – nous y reviendrons plus tard.

### Lire les props dans votre composant enfant

Maintenant que nous avons passé les données en tant que props à notre composant, nous devons ajuster notre composant `Button` pour _lire_ les props de son composant parent. Dans `components/button.tsx` :

```js
export default function Button({ count, onClick }) {
    return (
        <button
            onClick={onClick}
            className="bg-blue-500 hover:bg-blue-700 rounded text-white font-bold px-4 py-2"
        >
            I have been clicked {count} times
        </button>
    );
}
```

Les composants fonctionnels React acceptent un seul objet `props` comme argument. Ici, nous décomposons les props que nous voulons passer dans notre composant `Button`. En d'autres termes, nous prenons `count` et `onClick` directement de l'objet `props`, comme argument de `Button`.

Si vous enregistrez votre fichier, vous verrez que cela fonctionne maintenant : vous avez deux boutons avec un état partagé :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screen-Recording-2024-06-14-at-12.07.37-PM.gif)
_Deux boutons avec un état partagé_

Mais pourquoi avons-nous passé `onClick` et non `handleClick` au composant `Button` ? N'est-ce pas `handleClick` que nous voulons exécuter lorsque nous cliquons sur le bouton ?

Dans le composant `Home` dans `app/page.tsx`, nous définissons `handleClick` et le passons en tant que prop au composant `Button`. Dans le corps du composant `Button` dans `components/button.tsx`, nous lisons la _prop_ `onClick`, pas le gestionnaire d'événements `handleClick` lui-même. Ainsi, lorsque le composant `Button` se déclenche, il appelle la prop `onClick`, qui se trouve "plus haut" dans l'arbre des composants à l'intérieur de `Home`, où elle appelle ensuite `handleClick`, met à jour le compteur, puis renvoie cet état aux deux composants `Button`.

### Petit cours accéléré de TypeScript

Si vous vérifiez `components/button.tsx`, vous verrez les erreurs suivantes pour les props `count` et `onClick` que vous lisez dans `Button` :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-14-at-2.49.55-PM.png)
_Binding element 'count' implicitly has an 'any' type._

(Vous pouvez obtenir ces erreurs TypeScript avec coloration syntaxique avec l'extension Visual Studio Code [ici](https://marketplace.visualstudio.com/items?itemName=yoavbls.pretty-ts-errors)).

Que signifient ces erreurs et qu'est-ce que TypeScript ? TypeScript est un sur-ensemble de JavaScript qui ajoute des _types_ à JavaScript. Ceux-ci peuvent aider à garantir que notre programme fonctionne comme nous le prévoyons. Des exemples de types sont `number`, `boolean` et `string`. Cette erreur nous indique que nous n'avons pas défini de type pour les props `count` ou `onClick`.

Ainsi, quel sera le type de `count` ? Si nous considérons le résultat de count, les réponses pourraient être `1`, `2`, `3`, et ainsi de suite. Ce sont tous des nombres, nous allons donc assigner le type `number` à `count`.

La prop `onClick` est une fonction qui ne prend aucun argument et ne renvoie aucune valeur – nous l'utilisons pour son effet secondaire de mise à jour de `setCount`. Nous lui assignons donc le type `() => void`.

Nous créons une _[interface](https://www.typescriptlang.org/docs/handbook/interfaces.html)_ où nous définissons les types pour nos `ButtonProps`, puis lisons cette interface dans notre composant :

```js
interface ButtonProps {
    count: number;
    onClick: () => void;
}

export default function Button({ count, onClick }: ButtonProps) {
    return (
        <button
            onClick={onClick}
            className="bg-blue-500 hover:bg-blue-700 rounded text-white font-bold px-4 py-2"
        >
            I have been clicked {count} times
        </button>
    );
}
```

Les erreurs ont disparu et voilà : une petite introduction à TypeScript !

Effectuons ici un autre Commit avec un message tel que `buttons with shared state`.

## Chapitre 4 : Comment ajouter les deux paires de boutons à notre site

Présentons à la fois nos boutons avec état partagé et indépendant, et déployons l'application.

Renommons notre `button.tsx` en `button-shared-state.tsx`. Renommons également la fonction, l'interface, l'importation dans `app/page.tsx`, ainsi que le composant dans `app/page.tsx`. Et passons-les à des exportations _nommées_ en utilisant une expression de fonction avec `const` au lieu d'une déclaration de fonction :

```js
interface ButtonSharedStateProps {
    count: number;
    onClick: () => void;
}

export const ButtonSharedState = ({
    count,
    onClick,
}: ButtonSharedStateProps) => {
    return (
        <button
            onClick={onClick}
            className="bg-blue-500 hover:bg-blue-700 rounded text-white font-bold px-4 py-2"
        >
            I have been clicked {count} times
        </button>
    );
};
```

```js
"use client";

import { useState } from "react";

import { ButtonSharedState } from "@/components/button-shared-state";

export default function Home() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }
    return (
        <main className="flex min-h-screen flex-col items-center p-24 gap-4">
            <h1>React Counter Button</h1>
            <ButtonSharedState count={count} onClick={handleClick} />
            <ButtonSharedState count={count} onClick={handleClick} />
        </main>
    );
}
```

Créons maintenant un fichier `components/button-independent-state.tsx` :

```js
"use client";
import { useState } from "react";

export const ButtonIndependentState = () => {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }

    return (
        <button
            className="bg-blue-500 hover:bg-blue-700 rounded text-white font-bold py-2 px-4"
            onClick={handleClick}
        >
            I have been clicked {count} times
        </button>
    );
};
```

Ce que nous avons fait ici est similaire à notre logique au début de ce guide : nous avons situé l'état à l'intérieur du composant bouton lui-même, de sorte que chaque implémentation du composant bouton crée et suit son propre état indépendant.

Importons `ButtonIndependentState` dans `app/page.tsx` :

```js
"use client";

import { useState } from "react";

import { ButtonSharedState } from "@/components/button-shared-state";
import { ButtonIndependentState } from "@/components/button-independent-state";

export default function Home() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }
    return (
        <main className="flex min-h-screen flex-col items-center p-24 gap-4">
            <h1 className="text-3xl font-bold">React Counter Buttons</h1>
            <h2 className="text-xl">Buttons with shared state</h2>
            <ButtonSharedState count={count} onClick={handleClick} />
            <ButtonSharedState count={count} onClick={handleClick} />
            <h2 className="text-xl">Buttons with independent state</h2>
            <ButtonIndependentState />
            <ButtonIndependentState />
        </main>
    );
}
```

Nous avons maintenant présenté un ensemble de boutons ayant un état indépendant, ainsi que des boutons ayant un état partagé. Nous avons ajouté un peu de CSS pour rendre les choses plus agréables visuellement.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screen-Recording-2024-06-21-at-12.25.22-PM.gif)
_Notre projet terminé_

Ajoutons ici un autre Commit avec un message tel que `buttons with both shared and independent state`.

## Chapitre 5 : Comment déployer le site sur Netlify

### Publier sur GitHub

Déployons notre application dans le monde pour la montrer. Nous allons pousser notre code sur GitHub, puis le déployer sur Netlify.

La première étape consiste à pousser notre code sur GitHub. Si vous n'avez pas de compte GitHub, créez-en un d'abord. Dans Visual Studio Code, vous pouvez pousser vers GitHub à partir de la palette de commandes : ouvrez la palette de commandes en appuyant sur `⇧⌘P`, puis tapez `publish to GitHub`, et sélectionnez `publish to public GitHub repository`.

Ouvrez votre compte GitHub et vérifiez que le projet a été téléchargé avec succès.

### Déployer sur Netlify

Une fois que vous avez téléchargé votre projet sur GitHub, vous pouvez maintenant le déployer sur Netlify. Ouvrez le [site web de Netlify](https://www.netlify.com/) et connectez-vous (ou créez un compte si vous n'en avez pas).

Cliquez sur `add new site`, puis sur `import an existing project`. Lorsqu'on vous demande `Let’s deploy your project with…`, sélectionnez `GitHub`.

Sélectionnez le nom de votre dépôt dans la liste, puis donnez un nom au site sous `site name`. Vous pouvez laisser le reste des paramètres par défaut, puis cliquer sur `deploy [your site name]`.

Si le projet est construit avec succès, vous aurez un lien en direct de votre travail !

## Réflexions finales et prochaines étapes

Dans ce projet, vous avez appris des concepts fondamentaux de React tels que la création d'un composant fonctionnel, l'importation et l'exportation de modules, l'interpolation de JavaScript dans JSX à l'aide d'accolades, le travail avec l'état et l'utilisation des hooks React.

Vous avez également vu une introduction à l'utilisation des techniques CSS basées sur les utilitaires avec Tailwind CSS, et vous avez reçu une petite introduction à l'ajout de types à votre JavaScript avec TypeScript. Enfin, vous avez appris comment déployer votre projet sur Netlify via GitHub.

Où pouvez-vous aller à partir d'ici ? Une idée pour étendre le projet pourrait être de créer un "ticker" : un compteur qui pourrait être incrémenté et décrémenté (vous auriez un bouton qui augmente le nombre du compteur, et un qui le diminue).

Dans l'optique de l'apprentissage, une méthode efficace pour solidifier les concepts que vous avez appris ici serait de recommencer un projet totalement à zéro, et de voir si vous pouvez construire tout ce qui se trouve dans ce tutoriel sans le consulter. Au fur et à mesure que vous aurez besoin de vérifier, vous identifierez les concepts qui bénéficieraient d'une étude et d'une pratique plus approfondies.

Si vous souhaitez rester en contact, vous pouvez :

* Me suivre sur [Twitter](https://twitter.com/DevinCLane)
* Me suivre sur [LinkedIn](https://www.linkedin.com/in/devinlane/)

N'hésitez pas à publier ce que vous avez réalisé ainsi que vos questions ou commentaires.

Bon code ! 💡