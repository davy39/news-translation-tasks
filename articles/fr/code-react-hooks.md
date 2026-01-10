---
title: Comment créer votre premier Hook React de A à Z
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-02T14:58:22.000Z'
originalURL: https://freecodecamp.org/news/code-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/how-to-create-your-first-react-hook.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment créer votre premier Hook React de A à Z
seo_desc: 'You can use custom React hooks to solve many different real-world problems
  in your React projects.

  As a result, learning how to make React hooks is a necessary skill in becoming a
  top-notch React developer.

  In this article, let''s take a look at how t...'
---

Vous pouvez utiliser des hooks React personnalisés pour résoudre de nombreux problèmes réels différents dans vos projets React.

Par conséquent, apprendre à créer des hooks React est une compétence nécessaire pour devenir un développeur React de premier ordre.

Dans cet article, voyons comment créer notre propre hook React personnalisé de A à Z qui permet aux utilisateurs de copier des extraits de code ou tout autre texte dans notre application.

## Quelle fonctionnalité voulons-nous ajouter ?

Sur mon site web, reedbarger.com, je permets aux utilisateurs de copier du code depuis mes articles à l'aide d'un package appelé `react-copy-to-clipboard`.

Un utilisateur survole simplement l'extrait, clique sur le bouton de presse-papiers, et le code est ajouté au presse-papiers de son ordinateur. Cela leur permet de coller et d'utiliser le code, où qu'ils le souhaitent.

![copy-gif.gif](https://dev-to-uploads.s3.amazonaws.com/i/fnmmit9fvxb4lejz3dcm.gif)

## Comment recréer react-copy-to-clipboard

Au lieu d'utiliser une bibliothèque tierce, cependant, je voulais recréer cette fonctionnalité avec mon propre hook React personnalisé.

Comme pour chaque hook React personnalisé que je crée, je le place dans un dossier dédié, généralement appelé `utils` ou `lib`, spécifiquement pour les fonctions que je peux réutiliser dans mon application.

Nous placerons ce hook dans un fichier appelé `useCopyToClipboard.js` et je créerai une fonction du même nom. Assurez-vous également d'importer React en haut du fichier.

Il existe diverses façons de copier du texte dans le presse-papiers de l'utilisateur. Cependant, je préfère utiliser une bibliothèque pour cela, ce qui rend le processus plus fiable, appelée `copy-to-clipboard`.

Elle exporte une fonction, que nous appellerons `copy`.

```jsx
// utils/useCopyToClipboard.js
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard() {}

```

Ensuite, nous créerons une fonction qui sera utilisée pour copier tout texte que l'on souhaite ajouter au presse-papiers de l'utilisateur. Nous appellerons cette fonction `handleCopy`.

## Comment créer la fonction handleCopy

Dans la fonction, nous devons d'abord nous assurer qu'elle n'accepte que les données de type chaîne ou nombre.

Nous allons mettre en place un if-else, qui s'assurera que le type est soit une chaîne soit un nombre. Sinon, nous enregistrerons une erreur dans la console indiquant à l'utilisateur qu'il ne peut pas copier d'autres types.

```jsx
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard() {
  const [isCopied, setCopied] = React.useState(false);

  function handleCopy(text) {
    if (typeof text === "string" || typeof text == "number") {
      // copy
    } else {
      // don't copy
      console.error(
        `Cannot copy typeof ${typeof text} to clipboard, must be a string or number.`
      );
    }
  }
}

```

Ensuite, nous voudrons prendre le texte et le convertir en chaîne, que nous passerons à la fonction `copy`. À partir de là, nous voulons retourner la fonction de gestion de la copie depuis le hook où nous le souhaitons dans notre application. Généralement, la fonction `handleCopy` sera connectée à un `onClick` d'un bouton.

```jsx
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard() {
  function handleCopy(text) {
    if (typeof text === "string" || typeof text == "number") {
      copy(text.toString());
    } else {
      console.error(
        `Cannot copy typeof ${typeof text} to clipboard, must be a string or number.`
      );
    }
  }

  return handleCopy;
}

```

De plus, nous voulons un état qui représente si le texte a été copié ou non. Pour cela, nous appellerons `useState` en haut de notre hook et créerons une nouvelle variable d'état `isCopied`, où le setter sera appelé `setCopy`.

Initialement, cette valeur sera false. Si le texte est copié avec succès, nous définirons `copy` sur true. Sinon, nous le définirons sur false.

Enfin, nous retournerons `isCopied` depuis le hook dans un tableau avec `handleCopy`.

```jsx
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard(resetInterval = null) {
  const [isCopied, setCopied] = React.useState(false);

  function handleCopy(text) {
    if (typeof text === "string" || typeof text == "number") {
      copy(text.toString());
      setCopied(true);
    } else {
      setCopied(false);
      console.error(
        `Cannot copy typeof ${typeof text} to clipboard, must be a string or number.`
      );
    }
  }

  return [isCopied, handleCopy];
}

```

## Comment utiliser useCopyToClipboard

Nous pouvons maintenant utiliser `useCopyToClipboard` dans n'importe quel composant que nous souhaitons.

Dans mon cas, je l'utiliserai avec un composant de bouton de copie, qui reçoit le code pour notre extrait de code.

Pour que cela fonctionne, tout ce que nous devons faire est d'ajouter un onClick au bouton. Et dans le retour d'une fonction appelée handleCopy avec le code demandé en tant que texte. Et une fois qu'il est copié, c'est vrai. Nous pouvons montrer une icône différente indiquant qu'une copie a réussi.

```jsx
import React from "react";
import ClipboardIcon from "../svg/ClipboardIcon";
import SuccessIcon from "../svg/SuccessIcon";
import useCopyToClipboard from "../utils/useCopyToClipboard";

function CopyButton({ code }) {
  const [isCopied, handleCopy] = useCopyToClipboard();

  return (
    <button onClick={() => handleCopy(code)}>
      {isCopied ? <SuccessIcon /> : <ClipboardIcon />}
    </button>
  );
}

```

## Comment ajouter un intervalle de réinitialisation

Il y a une amélioration que nous pouvons apporter à notre code. Tel que nous avons actuellement écrit notre hook, `isCopied` sera toujours vrai, ce qui signifie que nous verrons toujours l'icône de succès :

![success-gif.gif](https://dev-to-uploads.s3.amazonaws.com/i/pgpdz9f5xp7nr4twovsn.gif)

Si nous voulons réinitialiser notre état après quelques secondes, nous pouvons passer un intervalle de temps à useCopyToClipboard. Ajoutons cette fonctionnalité.

Dans notre hook, nous pouvons créer un paramètre appelé `resetInterval`, dont la valeur par défaut est `null`, ce qui garantira que l'état ne sera pas réinitialisé si aucun argument n'est passé.

Nous ajouterons ensuite `useEffect` pour dire que si le texte est copié et que nous avons un intervalle de réinitialisation, nous réinitialiserons `isCopied` à false après cet intervalle en utilisant un `setTimeout`.

De plus, nous devons effacer ce timeout si notre composant dans lequel le hook est utilisé est démonté (ce qui signifie que notre état n'est plus là pour être mis à jour).

```jsx
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard(resetInterval = null) {
  const [isCopied, setCopied] = React.useState(false);

  const handleCopy = React.useCallback((text) => {
    if (typeof text === "string" || typeof text == "number") {
      copy(text.toString());
      setCopied(true);
    } else {
      setCopied(false);
      console.error(
        `Cannot copy typeof ${typeof text} to clipboard, must be a string or number.`
      );
    }
  }, []);

  React.useEffect(() => {
    let timeout;
    if (isCopied && resetInterval) {
      timeout = setTimeout(() => setCopied(false), resetInterval);
    }
    return () => {
      clearTimeout(timeout);
    };
  }, [isCopied, resetInterval]);

  return [isCopied, handleCopy];
}

```

Enfin, la dernière amélioration que nous pouvons apporter est d'envelopper `handleCopy` dans le hook `useCallback` afin de nous assurer qu'il ne sera pas recréé à chaque fois qu'il y a un rerender.

## Résultat final

Et avec cela, nous avons notre hook final, qui permet à l'état d'être réinitialisé après un intervalle de temps donné. Si nous en passons un, nous devrions voir un résultat comme celui que nous avons ci-dessous :

```jsx
import React from "react";
import ClipboardIcon from "../svg/ClipboardIcon";
import SuccessIcon from "../svg/SuccessIcon";
import useCopyToClipboard from "../utils/useCopyToClipboard";

function CopyButton({ code }) {
  // isCopied est réinitialisé après un timeout de 3 secondes
  const [isCopied, handleCopy] = useCopyToClipboard(3000);

  return (
    <button onClick={() => handleCopy(code)}>
      {isCopied ? <SuccessIcon /> : <ClipboardIcon />}
    </button>
  );
}

```

![final-result.gif](https://dev-to-uploads.s3.amazonaws.com/i/kul32jsgeevk92j2j5ll.gif)

J'espère que vous avez appris quelques choses à travers ce processus de création de notre hook, et que vous l'utiliserez dans vos propres projets personnels pour copier n'importe quel texte que vous aimez dans le presse-papiers.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir quand j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*