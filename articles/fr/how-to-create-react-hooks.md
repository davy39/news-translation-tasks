---
title: 'Comment créer vos propres Hooks React : Un guide étape par étape'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-03-05T16:26:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/how-to-create-custom-react-hooks.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: 'Comment créer vos propres Hooks React : Un guide étape par étape'
seo_desc: "Custom React hooks are an essential tool that let you add special, unique\
  \ functionality to your React applications. \nIn many cases, if you want to add\
  \ a certain feature to your application, you can simply install a third-party library\
  \ that is made to..."
---

Les hooks React personnalisés sont un outil essentiel qui vous permet d'ajouter des fonctionnalités spéciales et uniques à vos applications React. 

Dans de nombreux cas, si vous souhaitez ajouter une certaine fonctionnalité à votre application, vous pouvez simplement installer une bibliothèque tierce conçue pour résoudre votre problème. Mais si une telle bibliothèque ou un tel hook n'existe pas, que faites-vous ?

En tant que développeur React, il est important d'apprendre le processus de création de hooks personnalisés pour résoudre des problèmes ou ajouter des fonctionnalités manquantes dans vos propres projets React.

Dans ce guide étape par étape, je vais vous montrer comment créer vos propres hooks React personnalisés en décomposant trois hooks que j'ai créés pour mes propres applications, ainsi que les problèmes qu'ils étaient censés résoudre.

## 1. Hook useCopyToClipboard

Dans une ancienne version de mon site web, [reedbarger.com](https://reedbarger.com), je permettais aux utilisateurs de copier du code depuis mes articles à l'aide d'un package appelé `react-copy-to-clipboard`.

Un utilisateur survole simplement le snippet, clique sur le bouton de presse-papiers, et le code est ajouté au presse-papiers de son ordinateur pour lui permettre de coller et d'utiliser le code, où il le souhaite.

![copy-gif.gif](https://dev-to-uploads.s3.amazonaws.com/i/fnmmit9fvxb4lejz3dcm.gif)

Au lieu d'utiliser une bibliothèque tierce, cependant, je voulais recréer cette fonctionnalité avec mon propre hook React personnalisé. Comme pour chaque hook React personnalisé que je crée, je le place dans un dossier dédié, généralement appelé `utils` ou `lib`, spécifiquement pour les fonctions que je peux réutiliser dans mon application.

Nous allons placer ce hook dans un fichier appelé useCopyToClipboard.js et je vais créer une fonction du même nom.

Il existe diverses façons de copier du texte dans le presse-papiers de l'utilisateur. Je préfère utiliser une bibliothèque pour cela, ce qui rend le processus plus fiable, appelée `copy-to-clipboard`.

Elle exporte une fonction, que nous appellerons `copy`.

```jsx
// utils/useCopyToClipboard.js
import React from "react";
import copy from "copy-to-clipboard";

export default function useCopyToClipboard() {}

```

Ensuite, nous allons créer une fonction qui sera utilisée pour copier tout texte souhaitant être ajouté au presse-papiers de l'utilisateur. Nous appellerons cette fonction `handleCopy`.

### Comment créer la fonction handleCopy

Dans la fonction, nous devons d'abord nous assurer qu'elle n'accepte que les données de type string ou number. Nous allons mettre en place une instruction `if-else`, qui vérifiera que le type est soit string soit number. Sinon, nous allons logger une erreur dans la console indiquant à l'utilisateur qu'il ne peut pas copier d'autres types.

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

Ensuite, nous prenons le texte et le convertissons en string, que nous passerons ensuite à la fonction `copy`. À partir de là, nous retournons la fonction `handleCopy` depuis le hook vers l'endroit où nous le souhaitons dans notre application. 

Généralement, la fonction `handleCopy` sera connectée à un `onClick` d'un bouton.

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

De plus, nous voulons un état qui représente si le texte a été copié ou non. Pour cela, nous allons appeler `useState` en haut de notre hook et créer une nouvelle variable d'état `isCopied`, où le setter sera appelé `setCopy`.

Initialement, cette valeur sera false. Si le texte est copié avec succès, nous allons définir `copy` sur true. Sinon, nous le définirons sur false.

Enfin, nous allons retourner `isCopied` depuis le hook dans un tableau avec `handleCopy`.

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

### Comment utiliser useCopyToClipboard

Nous pouvons maintenant utiliser `useCopyToClipboard` dans n'importe quel composant que nous souhaitons.

Dans mon cas, je vais l'utiliser avec un composant de bouton de copie qui reçoit le code pour notre extrait de code.

Pour que cela fonctionne, tout ce que nous avons à faire est d'ajouter un on click au bouton. Et dans le retour d'une fonction appelée handle copy avec le code demandé en tant que texte. Et une fois qu'il est copié, c'est vrai. Nous pouvons montrer une icône différente indiquant qu'une copie a réussi.

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

### Comment ajouter un intervalle de réinitialisation

Il y a une amélioration que nous pouvons apporter à notre code. Comme nous avons actuellement écrit notre hook, `isCopied` sera toujours vrai, ce qui signifie que nous verrons toujours l'icône de succès :

![success-gif.gif](https://dev-to-uploads.s3.amazonaws.com/i/pgpdz9f5xp7nr4twovsn.gif)

Si nous voulons réinitialiser notre état après quelques secondes, vous pouvez passer un intervalle de temps à `useCopyToClipboard`. Ajoutons cette fonctionnalité.

De retour dans notre hook, nous pouvons créer un paramètre appelé `resetInterval`, dont la valeur par défaut est `null`, ce qui garantira que l'état ne sera pas réinitialisé si aucun argument n'est passé.

Nous ajouterons ensuite `useEffect` pour dire que si le texte est copié et que nous avons un intervalle de réinitialisation, nous définirons `isCopied` à false après cet intervalle en utilisant un `setTimeout`.

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

Enfin, la dernière amélioration que nous pouvons apporter est d'envelopper `handleCopy` dans le hook `useCallback` afin de garantir qu'il ne sera pas recréé à chaque fois qu'il y a un rerender.

### Résultat final

Et avec cela, nous avons notre hook final qui permet à l'état d'être réinitialisé après un intervalle de temps donné. Si nous en passons un, nous devrions voir un résultat comme celui que nous avons ci-dessous.

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

## 2. Hook usePageBottom

Dans les applications React, il est parfois important de savoir quand votre utilisateur a fait défiler jusqu'au bas d'une page.

Dans les applications où vous avez un défilement infini, comme Instagram par exemple, une fois que l'utilisateur atteint le bas de la page, vous devez récupérer plus de publications.

![Défilement infini dans Instagram](https://dev-to-uploads.s3.amazonaws.com/i/4dav187wpkl46skhhjgh.gif)

Examinons comment créer un hook usePageBottom nous-mêmes pour des cas d'utilisation similaires comme la création d'un défilement infini.

Nous commencerons par créer un fichier séparé, usePageBottom.js, dans notre dossier utils et nous ajouterons une fonction (hook) avec le même nom :

```js
// utils/usePageBottom.js
import React from "react";

export default function usePageBottom() {}


```

Ensuite, nous devrons calculer quand notre utilisateur atteint le bas de la page. Nous pouvons déterminer cela avec des informations de la `window`. Pour y accéder, nous devons nous assurer que notre composant dans lequel le hook est appelé est monté, nous utiliserons donc le hook `useEffect` avec un tableau de dépendances vide.

```js
// utils/usePageBottom.js
import React from "react";

export default function usePageBottom() {
  React.useEffect(() => {}, []);
}


```

L'utilisateur aura fait défiler jusqu'au bas de la page lorsque la valeur `innerHeight` de la fenêtre plus la valeur `scrollTop` du document est égale à la valeur `offsetHeight`. Si ces deux valeurs sont égales, le résultat sera vrai, et l'utilisateur a fait défiler jusqu'au bas de la page :

```js
// utils/usePageBottom.js
import React from "react";

export default function usePageBottom() {
  React.useEffect(() => {
    window.innerHeight + document.documentElement.scrollTop === 
    document.documentElement.offsetHeight;
  }, []);
}


```

Nous allons stocker le résultat de cette expression dans une variable, `isBottom` et nous allons mettre à jour une variable d'état appelée `bottom`, que nous retournerons finalement depuis notre hook.

```js
// utils/usePageBottom.js
import React from "react";

export default function usePageBottom() {
  const [bottom, setBottom] = React.useState(false);

  React.useEffect(() => {
    const isBottom =
      window.innerHeight + document.documentElement.scrollTop ===
      document.documentElement.offsetHeight;
    setBottom(isButton);
  }, []);

  return bottom;
}


```

Notre code tel qu'il est, cependant, ne fonctionnera pas. Pourquoi ?

Le problème réside dans le fait que nous devons calculer `isBottom` chaque fois que l'utilisateur fait défiler. Par conséquent, nous devons écouter un événement de défilement avec `window.addEventListener`. Nous pouvons réévaluer cette expression en créant une fonction locale à appeler chaque fois que l'utilisateur fait défiler, appelée `handleScroll`.

```js
// utils/usePageBottom.js
import React from "react";

export default function usePageBottom() {
  const [bottom, setBottom] = React.useState(false);

  React.useEffect(() => {
    function handleScroll() {
      const isBottom =
        window.innerHeight + document.documentElement.scrollTop 
        === document.documentElement.offsetHeight;
      setBottom(isButton);
    }
    window.addEventListener("scroll", handleScroll);
  }, []);

  return bottom;
}


```

Enfin, puisque nous avons un écouteur d'événement qui met à jour l'état, nous devons gérer l'événement où notre utilisateur navigue loin de la page et notre composant est supprimé. Nous devons supprimer l'écouteur d'événement de défilement que nous avons ajouté, afin de ne pas tenter de mettre à jour une variable d'état qui n'existe plus.

Nous pouvons faire cela en retournant une fonction depuis `useEffect` avec `window.removeEventListener`, où nous passons une référence à la même fonction `handleScroll`. Et nous avons terminé.

```js
// utils/usePageBottom.js
import React from "react";

export default function usePageBottom() {
  const [bottom, setBottom] = React.useState(false);

  React.useEffect(() => {
    function handleScroll() {
      const isBottom =
        window.innerHeight + document.documentElement.scrollTop 
        === document.documentElement.offsetHeight;
      setBottom(isButton);
    }
    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return bottom;
}


```

Maintenant, nous pouvons simplement appeler ce code dans n'importe quelle fonction où nous voulons savoir si nous avons atteint le bas de la page ou non. 

Dans mon site Gatsby, j'ai un en-tête, et lorsque je réduis la taille de la page, je veux montrer moins de liens.

![redimensionnement de la fenêtre pour montrer l'en-tête](https://dev-to-uploads.s3.amazonaws.com/i/kxbnn3jmwjarkc8zrpbm.gif)

Pour ce faire, nous pourrions utiliser une requête média (CSS), ou nous pourrions utiliser un hook React personnalisé pour nous donner la taille actuelle de la page et masquer ou afficher les liens dans notre JSX.

Auparavant, j'utilisais un hook de la bibliothèque appelée `react-use`. Au lieu d'importer une bibliothèque tierce entière, j'ai décidé de créer mon propre hook qui fournirait les dimensions de la fenêtre, à la fois la largeur et la hauteur. J'ai appelé ce hook `useWindowSize`.

### Comment créer le hook

Tout d'abord, nous allons créer un nouveau fichier .js dans notre dossier utilitaires (utils), avec le même nom que le hook `useWindowSize`. J'importerai React (pour utiliser les hooks) tout en exportant le hook personnalisé.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {}


```

Maintenant, puisque j'utilise cela dans un site Gatsby, qui est rendu côté serveur, j'ai besoin d'obtenir la taille de la fenêtre. Mais nous n'avons peut-être pas accès à celle-ci car nous sommes sur le serveur. 

Pour vérifier et s'assurer que nous ne sommes pas sur le serveur, nous pouvons voir si le type de `window` n'est pas égal à la chaîne `undefined`.

Dans ce cas, nous pouvons retourner à une largeur et une hauteur par défaut pour un navigateur, disons, 1200 et 800 dans un objet :

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  if (typeof window !== "undefined") {
    return { width: 1200, height: 800 };
  }
}


```

### Comment obtenir la largeur et la hauteur de la fenêtre

Et en supposant que nous sommes sur le client et que nous pouvons obtenir la fenêtre, nous pouvons utiliser le hook `useEffect` pour effectuer un effet secondaire en interagissant avec `window`. Nous inclurons un tableau de dépendances vide pour nous assurer que la fonction d'effet est appelée uniquement une fois que le composant (dans lequel ce hook est appelé) est monté.

Pour connaître la largeur et la hauteur de la fenêtre, nous pouvons ajouter un écouteur d'événement et écouter l'événement `resize`. Et chaque fois que la taille du navigateur change, nous pouvons mettre à jour un morceau d'état (créé avec `useState`), que nous appellerons `windowSize`, et le setter pour le mettre à jour sera `setWindowSize`.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  if (typeof window !== "undefined") {
    return { width: 1200, height: 800 };
  }

  const [windowSize, setWindowSize] = React.useState();

  React.useEffect(() => {
    window.addEventListener("resize", () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    });
  }, []);
}


```

Lorsque la fenêtre est redimensionnée, le callback sera appelé et l'état `windowSize` sera mis à jour avec les dimensions actuelles de la fenêtre. Pour obtenir cela, nous définissons la largeur sur `window.innerWidth`, et la hauteur sur `window.innerHeight`.

### Comment ajouter la prise en charge du SSR

Cependant, le code tel que nous l'avons ici ne fonctionnera pas. Cela est dû à une règle clé des hooks : ils ne peuvent pas être appelés de manière conditionnelle. Par conséquent, nous ne pouvons pas avoir une condition au-dessus de notre hook `useState` ou `useEffect` avant qu'ils ne soient appelés.

Pour corriger cela, nous allons définir la valeur initiale de `useState` de manière conditionnelle. Nous allons créer une variable appelée `isSSR`, qui effectuera la même vérification pour voir si la fenêtre n'est pas égale à la chaîne `undefined`.

Et nous allons utiliser un ternaire pour définir la largeur et la hauteur en vérifiant d'abord si nous sommes sur le serveur. Si nous y sommes, nous utiliserons la valeur par défaut, et si ce n'est pas le cas, nous utiliserons `window.innerWidth` et `window.innerHeight`.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  // if (typeof window !== "undefined") {
  // return { width: 1200, height: 800 };
  // }
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  React.useEffect(() => {
    window.addEventListener("resize", () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    });
  }, []);
}


```

Ensuite, enfin, nous devons penser à quand nos composants sont démontés. Que devons-nous faire ? Nous devons supprimer notre écouteur de redimensionnement.

### Comment supprimer l'écouteur d'événement de redimensionnement

Vous pouvez le faire en retournant une fonction depuis useEffect. Nous allons supprimer l'écouteur avec `window.removeEventListener`.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  // if (typeof window !== "undefined") {
  // return { width: 1200, height: 800 };
  // }
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  React.useEffect(() => {
    window.addEventListener("resize", () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    });

    return () => {
      window.removeEventListener("resize", () => {
        setWindowSize({ width: window.innerWidth, height: window.innerHeight });
      });
    };
  }, []);
}


```

Mais nous avons besoin d'une référence à la même fonction, et non à deux fonctions différentes comme nous l'avons ici. Pour cela, nous allons créer une fonction de callback partagée pour les deux écouteurs appelée `changeWindowSize`.

Et enfin, à la fin du hook, nous allons retourner notre état `windowSize`. Et c'est tout.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  function changeWindowSize() {
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });
  }

  React.useEffect(() => {
    window.addEventListener("resize", changeWindowSize);

    return () => {
      window.removeEventListener("resize", changeWindowSize);
    };
  }, []);

  return windowSize;
}


```

### Résultat final

Pour utiliser le hook, nous devons simplement l'importer là où nous en avons besoin, l'appeler et utiliser la largeur où nous voulons masquer ou afficher certains éléments.

Dans mon cas, cela se situe à la marque des 500px. Là, je veux masquer tous les autres liens et n'afficher que le bouton Join Now, comme vous le voyez dans l'exemple ci-dessus :

```jsx
// components/StickyHeader.js

import React from "react";
import useWindowSize from "../utils/useWindowSize";

function StickyHeader() {
  const { width } = useWindowSize();

  return (
    <div>
      {/* visible uniquement lorsque la fenêtre est supérieure à 500px */}
      {width > 500 && (
        <>
          <div onClick={onTestimonialsClick} role="button">
            <span>Témoignages</span>
          </div>
          <div onClick={onPriceClick} role="button">
            <span>Prix</span>
          </div>
          <div>
            <span onClick={onQuestionClick} role="button">
              Question ?
            </span>
          </div>
        </>
      )}
      {/* visible à n'importe quelle taille de fenêtre */}
      <div>
        <span className="primary-button" onClick={onPriceClick} role="button">
          Rejoindre maintenant
        </span>
      </div>
    </div>
  );
}


```

Ce hook fonctionnera sur n'importe quelle application React rendue côté serveur, comme Gatsby et Next.js.

## 3. Hook useDeviceDetect

Je suis en train de construire une nouvelle page de destination pour un de mes cours, et j'ai rencontré une erreur très étrange sur les appareils mobiles. Sur les ordinateurs de bureau, les styles avaient l'air super.

Mais lorsque je l'ai regardé sur mobile, tout était décalé et cassé.

![Erreur de l'application React](https://dev-to-uploads.s3.amazonaws.com/i/n69a3h184fhniah3g1z8.gif)

J'ai remonté le problème jusqu'à une bibliothèque appelée `react-device-detect` que j'utilisais pour détecter si les utilisateurs avaient un appareil mobile ou non. Si c'était le cas, je supprimais l'en-tête.

```jsx
// templates/course.js
import React from "react";
import { isMobile } from "react-device-detect";

function Course() {
  return (
    <>
      <SEO />
      {!isMobile && <StickyHeader {...courseData} />}
      {/* plus de composants... */}
    </>
  );
}


```

Le problème était que cette bibliothèque ne prend pas en charge le rendu côté serveur, ce que Gatsby utilise par défaut. J'avais donc besoin de créer ma propre solution pour vérifier quand un utilisateur était sur un appareil mobile. Et pour cela, j'ai décidé de créer un hook personnalisé avec le nom `useDeviceDetect`.

### Comment j'ai créé le Hook

J'ai créé un fichier séparé pour ce hook dans mon dossier utils avec le même nom, useDeviceDetect.js. Puisque les hooks sont simplement des fonctions JavaScript partageables, qui utilisent les hooks React, j'ai créé une fonction appelée `useDeviceDetect` et importé React.

```jsx
// utils/useDeviceDetect.js
import React from "react";

export default function useDeviceDetect() {}


```

### Comment obtenir l'agent utilisateur depuis window

La manière dont nous pouvons nous assurer que nous pouvons obtenir des informations sur l'appareil de l'utilisateur est via la propriété userAgent (située sur la propriété navigator de window).

Et puisque l'interaction avec l'API window en tant qu'API / ressource externe serait classée comme un effet secondaire, nous devons obtenir l'accès à l'agent utilisateur dans le hook `useEffect`.

```jsx
// utils/useDeviceDetect.js
import React from "react";

export default function useDeviceDetect() {
  React.useEffect(() => {
    console.log(`L'appareil de l'utilisateur est : ${window.navigator.userAgent}`);
    // peut aussi s'écrire 'navigator.userAgent'
  }, []);
}


```

Une fois le composant monté, nous pouvons utiliser `typeof navigator` pour déterminer si nous sommes sur le client ou le serveur. Si nous sommes sur le serveur, nous n'aurons pas accès à la fenêtre. `typeof navigator` sera égal à la chaîne `undefined` puisqu'il n'est pas là. Sinon, si nous sommes sur le client, nous pourrons obtenir notre propriété userAgent.

Nous pouvons exprimer tout cela en utilisant un ternaire pour obtenir les données userAgent :

```jsx
// utils/useDeviceDetect.js
import React from "react";

export default function useDeviceDetect() {
  React.useEffect(() => {
    const userAgent =
      typeof navigator === "undefined" ? "" : navigator.userAgent;
  }, []);
}


```

### Comment vérifier si userAgent est un appareil mobile

`userAgent` est une valeur de chaîne qui sera définie sur l'un des noms d'appareils suivants si ils utilisent un appareil mobile :

Android, BlackBerry, iPhone, iPad, iPod, Opera Mini, IEMobile, ou WPDesktop.

Tout ce que nous avons à faire est de prendre la chaîne que nous obtenons et d'utiliser la méthode `.match()` avec une regex pour voir si elle correspond à l'une de ces chaînes. Nous allons la stocker dans une variable locale appelée `mobile`.

Nous allons stocker le résultat dans l'état avec le hook useState, auquel nous donnerons une valeur initiale de false. Pour cela, nous allons créer une variable d'état correspondante `isMobile`, et le setter sera `setMobile`.

```jsx
// utils/useDeviceDetect.js
import React from "react";

export default function useDeviceDetect() {
  const [isMobile, setMobile] = React.useState(false);

  React.useEffect(() => {
    const userAgent =
      typeof window.navigator === "undefined" ? "" : navigator.userAgent;
    const mobile = Boolean(
      userAgent.match(
        /Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i
      )
    );
    setMobile(mobile);
  }, []);
}


```

Une fois que nous obtenons la valeur `mobile`, nous allons la définir dans l'état. Ensuite, enfin, nous allons retourner un objet depuis le hook afin que nous puissions ajouter plus de valeurs à l'avenir si nous choisissons d'ajouter plus de fonctionnalités à ce hook.

Dans l'objet, nous allons ajouter `isMobile` en tant que propriété et valeur :

```jsx
// utils/useDeviceDetect.js
import React from "react";

export default function useDeviceDetect() {
  const [isMobile, setMobile] = React.useState(false);

  React.useEffect(() => {
    const userAgent =
      typeof window.navigator === "undefined" ? "" : navigator.userAgent;
    const mobile = Boolean(
      userAgent.match(
        /Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i
      )
    );
    setMobile(mobile);
  }, []);

  return { isMobile };
}


```

### Résultat final

De retour dans la page de destination, nous pouvons exécuter le hook et simplement obtenir cette propriété depuis l'objet déstructuré et l'utiliser là où nous en avons besoin.

```jsx
// templates/course.js
import React from "react";
import useDeviceDetect from "../utils/useDeviceDetect";

function Course() {
  const { isMobile } = useDeviceDetect();

  return (
    <>
      <SEO />
      {!isMobile && <StickyHeader {...courseData} />}
      {/* plus de composants... */}
    </>
  );
}


```

## Conclusion

Comme j'ai tenté de l'illustrer à travers chacun de ces exemples, les hooks React personnalisés peuvent nous donner les outils pour résoudre nos propres problèmes lorsque les bibliothèques tierces ne suffisent pas.

J'espère que ce guide vous a donné une meilleure idée de quand et comment créer vos propres hooks React. N'hésitez pas à utiliser l'un de ces hooks et le code ci-dessus dans vos propres projets et comme inspiration pour vos propres hooks React personnalisés.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais souhaité avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*