---
title: Comment optimiser les performances d'une application Next.js avec le Lazy Loading
date: '2024-07-19T22:31:12.000Z'
author: Tapas Adhikary
authorURL: https://www.freecodecamp.org/news/author/atapas/
originalURL: https://freecodecamp.org/news/next-js-performance-optimization
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/lazyloading-next.js.png
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: web performance
  slug: web-performance
seo_desc: "People don't like using slow applications. And the initial load time matters\
  \ a lot for web applications and websites. \nAn application that takes more than\
  \ 3 seconds to load is considered slow and may cause users to leave the application\
  \ or website.\nN..."
---


Les gens n'aiment pas utiliser des applications lentes. Et le temps de chargement initial est crucial pour les applications web et les sites internet.

<!-- more -->

Une application qui met plus de 3 secondes à charger est considérée comme lente et peut inciter les utilisateurs à quitter l'application ou le site.

`Next.js` est un framework basé sur React que vous pouvez utiliser pour bâtir des applications web et des sites plus rapides, performants et scalables. Avec l'inclusion des [React Server Components][1] dans la version de l'App Router de Next.js, les développeurs disposent d'un nouveau modèle mental pour "penser en composants serveur". Cela résout les problèmes de SEO, aide à créer des composants React avec une `zero bundle size`, et le résultat final est un chargement plus rapide des composants de l'interface utilisateur (UI).

Mais votre application ne se résume pas toujours aux composants serveur. Vous pouvez également avoir besoin d'utiliser des composants client. De plus, vous pourriez vouloir les charger soit lors du chargement initial de l'application, soit à la demande (par exemple, au clic sur un bouton).

Charger un composant client sur le navigateur implique de télécharger le code du composant, de télécharger toutes les bibliothèques et autres composants que vous avez importés dans ce composant client, ainsi que quelques éléments supplémentaires que React gère pour vous afin de s'assurer que vos composants fonctionnent.

Selon la connexion internet de l'utilisateur et d'autres facteurs réseau, le chargement complet du composant client peut prendre un certain temps, ce qui peut empêcher vos utilisateurs d'utiliser l'application plus rapidement.

C'est là que les techniques de `Lazy Loading` (chargement différé) s'avèrent utiles. Elles peuvent vous éviter un chargement monolithique de vos composants client sur le navigateur.

Dans cet article, nous allons aborder quelques techniques de lazy loading dans Next.js pour l'optimisation du chargement des composants client. Nous parlerons également de quelques cas particuliers que vous devriez savoir gérer.

Si vous préférez apprendre via du contenu vidéo, cet article est également disponible sous forme de tutoriel vidéo ici : 🙂

<iframe width="560" height="315" src="https://www.youtube.com/embed/gq9bBZru78Y" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" loading="lazy"></iframe>

Avant de commencer, voici quelques précisions :

-   Nous allons écrire pas mal de code pour construire une application afin de démontrer les techniques de lazy loading. Vous pouvez trouver tout le code source dans ce dépôt GitHub : [https://github.com/tapascript/nextjs-lazy-load][2]. Mais je vous suggère fortement d'écrire le code vous-même au fur et à mesure et de n'utiliser le dépôt que comme référence.
-   Vous pouvez également accéder à l'application déployée publiquement [sur Netlify ici][3].

C'est parti 🚀. Ah oui, si vous aimez le dessin animé Tom & Jerry, vous allez encore plus apprécier ceci !

## **Table des matières**

-   [Qu'est-ce que le Lazy Loading ?][4]
-   [Techniques de Lazy Loading dans Next.js][5]
-   [Lazy Loading avec dynamic import et next/dynamic][6]
-   [Lazy Loading avec React.lazy() et Suspense][7]
-   [Comment charger en Lazy Loading les composants exportés nommés][8]
-   [Lazy Loading de vos Server Components][9]
-   [Devrions-nous utiliser le Lazy Loading pour tous les Client Components dans Next.js ?][10]
-   [Et après ?][11]

## Qu'est-ce que le Lazy Loading ?

Dans le développement d'applications web modernes, nous ne codons pas toute la logique dans un seul fichier JavaScript/TypeScript, ni tous les styles dans un fichier CSS gigantesque. Au lieu de cela, nous les divisons au niveau du code source et créons des modules logiques, de la logique métier, des composants de présentation et des fichiers liés au style. Cela nous aide à mieux organiser notre code.

Ensuite, nous utilisons ce qu'on appelle un bundler qui intervient lors de la phase de build du processus de développement. Il crée des bundles pour nos scripts et nos styles. Certains des bundlers les plus célèbres sont Webpack, Rollup et Parcel, entre autres.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-43.png) _Un bundler créant des bundles à partir du code source_

Maintenant que nous avons les bundles, si nous essayons de les charger tous ensemble sur le navigateur, nous rencontrerons des lenteurs. C'est parce que le bundle complet doit être chargé dans le navigateur pour que l'interface utilisateur soit fonctionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-44.png) _Le chargement d'un bundle énorme entraîne une mauvaise expérience de chargement_

Ainsi, au lieu d'attendre que l'énorme bundle soit chargé dans le navigateur, les bibliothèques de développement web modernes et les systèmes d'outillage nous permettent de charger le bundle par morceaux (chunks).

Nous pouvons vouloir charger certains chunks immédiatement, car les utilisateurs peuvent en avoir besoin dès le chargement de l'application. En même temps, nous pouvons vouloir attendre pour charger certaines parties d'une page web jusqu'à ce qu'elles soient nécessaires.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-45.png) _Découpage en chunks et chargement de ce qui est nécessaire_

Ce mécanisme consistant à attendre pour charger une partie des pages ou de l'application, et à ne les charger que lorsqu'elles sont absolument nécessaires, est appelé `Lazy Loading`. Le concept de lazy loading n'est pas spécifique à React ou Next.js. C'est une technique d'optimisation des performances que vous pouvez implémenter avec diverses bibliothèques et frameworks.

## Techniques de Lazy Loading dans Next.js

Les techniques de lazy loading dans Next.js sont utilisées pour réduire la quantité de JavaScript nécessaire pour une route. Cela permet d'accélérer les performances de chargement initial de l'application. Nous pouvons différer le chargement des composants client et des bibliothèques importées jusqu'à ce qu'ils soient nécessaires.

Il existe deux façons d'implémenter les techniques de lazy loading dans Next.js :

-   En utilisant les imports dynamiques à l'aide du package `next/dynamic`.
-   En utilisant une combinaison de `React.lazy()` et `Suspense`.

Comprenons chacune de ces techniques avec des exemples de code.

## Lazy Loading avec `dynamic import` et `next/dynamic`

`next/dynamic` est une combinaison de React.lazy() et Suspense de ReactJS. Utiliser un import dynamique avec le package next/dynamic est l'approche privilégiée pour réaliser le lazy loading dans Next.js.

Pour le démontrer, créons d'abord une application Next.js en utilisant la commande suivante :

```
npx create-next-app@latest
```

Vous pouvez lancer l'application localement avec la commande suivante :

```
## Avec npm
npm run dev

## Avec yarn
yarn dev

## Ou utilisez pnpm, bun, selon votre choix !
```

Maintenant, créez un dossier appelé `components` sous le répertoire `app/`. Nous créerons tous nos composants sous ce dossier. Ensuite, créez un dossier appelé `tom` sous `app/components/`. Enfin, créez un composant React appelé `tom.jsx` sous le répertoire `app/components/tom/` avec le code suivant :

```
// tom.jsx

const LazyTom = () => {
  return (
    <div className="flex flex-col">
      <h1 className="text-3xl my-2">The Lazy Tom</h1>
      <p className="text-xl my-1">
        Tom, nommé &quot;Jasper&quot; in his debut appearance, is a gray and white
        domestic shorthair cat 🐈. &quot;Tom&quot; is a generic name for a male cat. He is
        usually but not always, portrayed as living a comfortable, or even
        pampered life. Tom is no match for Jerry&apos;s wits.
      </p>
      <p className="text-xl my-1">
        Although cats typically chase mice to eat them, it is quite rare for Tom
        to actually try to eat Jerry. He tries to hurt or compete with him just
        to taunt Jerry, even as revenge, or to obtain a reward from a human,
        including his owner(s)/master(s), for catching Jerry, or for generally
        doing his job well as a house cat. By the final &quot;fade-out&quot; of each
        cartoon, Jerry usually gets the best of Tom.
      </p>
    </div>
  );
};

export default LazyTom;
```

Pour expliquer le code ci-dessus :

-   Nous avons créé un composant ReactJS appelé `LazyTom`.
-   C'est un simple composant de présentation qui contient un titre et quelques paragraphes parlant du chat, Tom, du célèbre dessin animé `Tom & Jerry`.
-   À la fin, nous avons utilisé un export `default` du composant pour l'importer ailleurs.

Maintenant, créez un autre fichier appelé `tom-story.jsx` sous le répertoire `app/components/tom/` avec le code suivant :

```
// tom-story.jsx

"use client";

import { useState } from "react";
import dynamic from "next/dynamic";

const LazyTom = dynamic(() => import("./tom"), {
    loading: () => <h1>Loading Tom&apos;s Story...</h1>,
});

function TomStory() {
    const [shown, setShown] = useState(false);

    return (
        <div className="flex flex-col m-8 w-[300px]">
            <h2 className="text-xl my-1">Demonstrating <strong>dynamic</strong></h2>
            <button
                className="bg-blue-600 text-white rounded p-1"
                onClick={() => setShown(!shown)}
            >
                Load 🐈 Tom&apos;s Story
            </button>

            {shown && <LazyTom />}
        </div>
    );
}

export default TomStory;
```

La magie principale du lazy loading avec `dynamic` se produit dans le code ci-dessus :

-   Nous avons créé un composant client appelé `TomStory` en utilisant la directive `"use client"`.
-   D'abord, nous avons importé le hook `useState` pour gérer un état de bascule (toggle), et la fonction `dynamic` de `next/dynamic` pour le lazy loading du composant créé précédemment.
-   La fonction `dynamic` prend une fonction en argument qui retourne le composant importé. Vous pouvez également configurer un message de chargement personnalisé en fournissant un objet de configuration optionnel comme argument à la fonction dynamic.
-   La fonction `dynamic()` retourne l'instance du composant chargé paresseusement – c'est-à-dire `LazyTom` (le nom peut être n'importe lequel). Mais ce composant n'est pas encore chargé.
-   Dans le JSX, nous avons un bouton de bascule qui affiche et masque le composant `LazyTom`. Notez que le composant sera chargé en lazy loading dans le navigateur de l'utilisateur dès la première instance d'un clic sur le bouton. Après cela, si vous le masquez et l'affichez à nouveau, le composant `LazyTom` ne sera pas rechargé à moins que nous ne rafraîchissions brutalement le navigateur ou que nous ne vidions le cache du navigateur.
-   Enfin, nous avons exporté par défaut le composant `TomStory`.

Nous devons maintenant le tester. Pour ce faire, ouvrez le fichier `page.js` dans le répertoire `app/` et remplacez le contenu par le code suivant :

```
import TomStory from "./components/tom/tom-story";

export default function Home() {
  return (
    <div className="flex flex-wrap justify-center ">
      <TomStory />
    </div>
  );
}
```

C'est un simple composant ReactJS qui importe le composant `TomStory` et l'utilise dans son JSX. Maintenant, ouvrez votre fenêtre de navigateur. Ouvrez les DevTools du navigateur et allez dans l'onglet `Network` (Réseau). Assurez-vous que le filtre `All` est sélectionné.

Accédez maintenant à l'application sur votre navigateur via `http://localhost:3000`. Vous devriez voir le bouton pour charger l'histoire de Tom. De plus, un certain nombre de ressources seront listées dans l'onglet `Network`. Ce sont les ressources requises pour le chargement initial de l'application qui ont été téléchargées sur votre navigateur.

Le composant `LazyTom` du fichier `tom.jsx` n'a pas encore été téléchargé. C'est parce que nous n'avons pas encore cliqué sur le bouton `Load Tom's Story`.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-9.21.10-AM.png) _Le bouton pour charger l'histoire de Tom en lazy loading_

Maintenant, cliquez sur le bouton. Vous devriez voir un message de chargement pendant un instant, puis le composant sera chargé avec l'histoire de Tom. Vous pouvez maintenant voir le composant `tom.jsx` listé dans l'onglet `Network` ainsi que le composant rendu sur la page avec l'histoire de Tom.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-9.27.55-AM.png) _Maintenant l'histoire de Tom est chargée en lazy loading_

Maintenant que vous avez vu comment la fonction `dynamic` de `next/dynamic` nous aide à charger un composant paresseusement, commençons par l'autre technique utilisant `React.lazy()` et `Suspense`.

## Lazy Loading avec `React.lazy()` et `Suspense`

Pour démontrer cette technique, commençons par l'histoire de Jerry, mon personnage préféré de Tom & Jerry.

D'abord, nous allons créer un dossier appelé `jerry` sous le répertoire `app/components/`. Ensuite, créez un fichier appelé `jerry.jsx` sous `app/components/jerry/` avec le code suivant :

```
// jerry.jsx

const LazyJerry = () => {
  return (
    <div className="flex flex-col justify-center">
      <h1 className="text-3xl my-2">The Lazy Jerry</h1>
      <p className="text-xl my-1">
        Jerry 🐀, whose name is not explicitly mentioned in his debut appearance,
        is a small, brown house mouse who always lives in close proximity to
        Tom. Despite being very energetic, determined and much larger, Tom is no
        match for Jerry&apos;s wits. Jerry possesses surprising strength for his
        size, approximately the equivalent of Tom&apos;s, lifting items such as
        anvils with relative ease and withstanding considerable impacts.
      </p>
      <p className="text-xl my-1">
        Although cats typically chase mice to eat them, it is quite rare for Tom
        to actually try to eat Jerry. He tries to hurt or compete with him just
        to taunt Jerry, even as revenge, or to obtain a reward from a human,
        including his owner(s)/master(s), for catching Jerry, or for generally
        doing his job well as a house cat. By the final &quot;fade-out&quot; of each
        cartoon, Jerry usually gets the best of Tom.
      </p>
    </div>
  );
};

export default LazyJerry;
```

Le contenu de `jerry.jsx` est structurellement similaire à `tom.jsx`. Ici, nous avons posté l'histoire de Jerry au lieu de celle de Tom, et exporté le composant par défaut.

Comme la dernière fois, créons un fichier `jerry-story.jsx` pour présenter le lazy loading de l'histoire de Jerry. Créez le fichier sous le répertoire `app/components/jerry/` avec le code suivant :

```
// jerry-story.jsx

"use client";

import React, { useState, Suspense } from "react";

const LazyJerry = React.lazy(() => import('./jerry'));

function JerryStory() {
    const [shown, setShown] = useState(false);

    return (
        <div className="flex flex-col m-8 w-[300px]">
            <h2 className="text-xl my-1"> Demonstrating <strong>React.lazy()</strong></h2>
            <button
                className="bg-pink-600 text-white rounded p-1"
                onClick={() => setShown(!shown)}
            >
                Load 🐀 Jerry&apos;s Story
            </button>

            {shown && <Suspense fallback={<h1>Loading Jerry&apos;s Story</h1>}>
                <LazyJerry />
            </Suspense>}
        </div>
    );
}

export default JerryStory;
```

Ici aussi, nous avons un composant client, et nous utiliserons la méthode `lazy()` et `Suspense` de React, nous les avons donc importés. Comme la fonction `dynamic()` dans la technique précédente, la fonction `lazy()` prend également une fonction en argument qui retourne le composant importé paresseusement. Nous avons également fourni le chemin relatif vers le composant que nous essayons de charger.

Notez qu'avec `dynamic()`, nous avions la possibilité de personnaliser le message de chargement au sein même de la fonction. Avec `lazy()`, nous ferons cela via la propriété `fallback` de `Suspense`.

Suspense utilise un fallback (solution de repli) pendant que vous attendez que les données se chargent. Si vous souhaitez comprendre en profondeur Suspense et les Error Boundaries de ReactJS, vous pouvez [consulter ce tutoriel vidéo][12].

Ici, comme notre composant `LazyJerry` se charge paresseusement, nous avons fourni un fallback pour afficher un message de chargement jusqu'à ce que le code du composant soit téléchargé avec succès dans le navigateur et rendu.

```
{shown && 
    <Suspense fallback={<h1>Loading Jerry&apos;s Story</h1>}>
                <LazyJerry />
    </Suspense>
}
```

De plus, comme vous pouvez le voir, nous chargeons le composant au premier clic sur le bouton. Ici aussi, le composant ne sera pas rechargé à chaque clic sur le bouton, sauf si nous rafraîchissons le navigateur ou vidons le cache.

Testons cela maintenant en l'important dans le fichier `page.js` et en ajoutant le composant dans son JSX.

```
// page.js

import TomStory from "./components/tom/tom-story";
import JerryStory from "./components/jerry/jerry-story"; 

export default function Home() {
  return (
    <div className="flex flex-wrap justify-center ">
      <TomStory />
      <JerryStory />
    </div>
  );
}
```

Maintenant, vous verrez un autre composant apparaître sur l'interface utilisateur avec un bouton pour charger l'histoire de Jerry. À ce stade, vous ne verrez pas le composant jerry.jsx chargé dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-9.33.36-AM.png) _Le bouton pour charger l'histoire de Jerry en lazy loading_

Maintenant, cliquez sur le bouton. Vous verrez que le composant est chargé, et vous pouvez le voir dans la liste de l'onglet Network. Vous devriez pouvoir lire l'histoire de Jerry rendue dans le cadre du composant chargé paresseusement.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-9.37.30-AM.png) _L'histoire de Jerry est chargée en lazy loading_

## Comment charger en Lazy Loading les composants exportés nommés

Jusqu'à présent, avec les deux techniques, nous avons importé un composant qui était exporté avec un `default export` puis chargé en lazy loading. En JavaScript (et donc en React), vous pouvez exporter et importer des modules de deux manières différentes :

-   Avec le mot-clé `default`. Dans ce cas, le module exporté peut être importé sous n'importe quel nom. Vous utiliseriez cela si vous vouliez exporter une seule fonctionnalité d'un module.
-   Sans le mot-clé `default`, c'est ce qu'on appelle un `named export` (export nommé). Dans ce cas, vous devez conserver le même nom de module pour l'export et l'import. Vous devez également entourer le nom du module d'accolades ({...}) lors de l'importation. Vous utiliseriez cela si vous vouliez exporter plusieurs fonctionnalités d'un module.

Si vous voulez approfondir les modules JavaScript et leur fonctionnement, je vous suggère de suivre [ce cours intensif][13] publié sur la chaîne YouTube de freeCodeCamp.

Pour démontrer le lazy loading d'un composant en `named export`, créons un autre composant React de présentation simple. Cette fois, nous utiliserons le chien colérique mais mignon nommé `Spike` du dessin animé Tom & Jerry.

Créez un dossier appelé `spike` sous le répertoire `app/components/`. Maintenant, créez un fichier appelé `spike.jsx` sous le répertoire `app/components/spike/` avec le code suivant :

```
// spike.jsx

export const LazySpike = () => {
  return (
    <div className="flex flex-col">
      <h1 className="text-3xl my-2">The Lazy Spike</h1>
      <p className="text-xl my-1">
        In his attempts to catch Jerry, Tom often has to deal with Spike 🦮, known
        as &quot;Killer&quot; and &quot;Butch&quot; in some shorts, an angry, vicious but easily
        duped bulldog who tries to attack Tom for bothering him or his son Tyke
        while trying to get Jerry. Originally, Spike was unnamed and mute, aside
        from howls and biting noises as well as attacking indiscriminately, not
        caring whether it was Tom or Jerry though usually attacking Tom.
      </p>
      <p className="text-xl my-1">
      In
        later cartoons, Spike spoke often, using a voice and expressions,
        performed by Billy Bletcher and later Daws Butler, modeled after
        comedian Jimmy Durante. Spike&apos;s coat has altered throughout the years
        between gray and creamy tan. The addition of Spike&apos;s son Tyke in the
        late 1940s led to both a slight softening of Spike&apos;s character and a
        short-lived spin-off theatrical series called Spike and Tyke.
      </p>
    </div>
  );
};
```

Encore une fois, ce composant est structurellement identique aux composants `tom.jsx` et `jerry.jsx` que nous avons vus auparavant, mais avec deux différences majeures :

1.  Ici, nous avons exporté le composant sans le mot-clé default, c'est donc un `named export`.
2.  Nous parlons du chien, Spike.

Maintenant, nous devons gérer le lazy loading d'un composant exporté par nom, et cela va être un peu différent du composant exporté par défaut.

Créez un fichier appelé `spike-story.jsx` sous le répertoire `app/components/spike/` avec le code suivant :

```
// spike-story.jsx

"use client";

import { useState } from "react";
import dynamic from "next/dynamic";

const LazySpike = dynamic(() => import("./spike").then((mod) => mod.LazySpike), {
    loading: () => <h1>Loading Spike&apos;s Story...</h1>,
});

function SpikeStory() {
    const [shown, setShown] = useState(false);

    return (
        <div className="flex flex-col m-8 w-[300px]">
            <h2 className="text-xl my-1">Demonstrating <strong>Named Export</strong></h2>
            <button
                className="bg-slate-600 text-white rounded p-1"
                onClick={() => setShown(!shown)}
            >
                Load 🦮 Spike&apos;s Story
            </button>

            {shown && <LazySpike />}
        </div>
    );
}

export default SpikeStory;
```

Comme pour `tom-story`, nous utilisons l'import dynamique avec next/dynamic. Mais zoomons sur le bloc suivant du code ci-dessus :

```
const LazySpike = dynamic(() => import("./spike").then((mod) => mod.LazySpike), {
    loading: () => <h1>Loading Spike&apos;s Story...</h1>,
});
```

Les changements que vous remarquerez ici sont que nous résolvons explicitement la promesse de la fonction `import("./spike")` en utilisant le gestionnaire `.then()`. Nous récupérons d'abord le module, puis nous choisissons le composant exporté par son nom réel – c'est-à-dire `LazySpike` dans ce cas. Le reste reste identique à ce que nous avons fait dans `tom-story`.

Maintenant, pour tester, importez à nouveau le composant dans le fichier `page.js`, et utilisez-le dans le JSX comme les deux fois précédentes.

```
// page.js

import TomStory from "./components/tom/tom-story";
import JerryStory from "./components/jerry/jerry-story";
import SpikeStory from "./components/spike/spike-story"; 

export default function Home() {
  return (
    <div className="flex flex-wrap justify-center ">
      <TomStory />
      <JerryStory />
      <SpikeStory />
    </div>
  );
}
```

Et voilà – vous devriez voir le nouveau composant rendu sur le navigateur avec un bouton pour charger l'histoire de Spike depuis le fichier `spike.jsx` qui n'est pas encore chargé.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-9.59.55-AM.png) _Le bouton pour charger l'histoire de Spike en lazy loading_

Cliquer sur le bouton chargera le fichier dans le navigateur et rendra le composant pour vous montrer l'histoire de Spike.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-10.02.01-AM.png) _L'histoire de Spike est chargée en lazy loading_

Ci-dessous, vous pouvez voir les trois composants démontrant trois techniques et cas d'utilisation différents côte à côte. Vous pouvez les tester ensemble. L'image ci-dessous montre le lazy loading de deux composants en parallèle alors qu'un autre composant était déjà chargé.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-10.14.21-AM.png) _Chargement paresseux de plusieurs composants en parallèle_

Voici un autre cas où les trois composants ont été chargés en lazy loading, à la demande, avec les clics sur les boutons respectifs.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-17-at-10.05.35-AM-1.png) _Toutes les histoires chargées en lazy loading_

## Lazy Loading de vos Server Components

Nous avons parlé des techniques de lazy loading pour les composants client. Pouvons-nous utiliser les mêmes pour les composants serveur ? Eh bien, vous le pouvez, mais vous n'avez pas à le faire, car les composants serveur sont déjà `code split` et l'aspect chargement est déjà géré par Next.js. Vous n'obtiendrez aucune erreur si vous essayez de le faire, mais ce serait inutile.

Dans le cas où vous importez dynamiquement un composant serveur qui a un ou plusieurs composants client comme enfants, ces composants client seront chargés en lazy loading. Mais il n'y aura aucun impact sur le composant serveur (parent) lui-même.

Voici un exemple de composant serveur qui a deux composants client comme enfants :

```
// server-comp.jsx

import ComponentA from "./a-client-comp";
import ComponentB from "./b-client-comp";

import React from 'react'

const AServerComp = () => {
  return (
    <div className="flex flex-col m-8 w-[300px]">
      <ComponentA />
      <ComponentB />
    </div>
  )
}

export default AServerComp
```

Maintenant, nous importons dynamiquement le composant serveur dans le fichier `page.js` et l'utilisons dans son JSX. Les composants client enfants du composant serveur importé dynamiquement seront chargés en lazy loading, mais pas le composant serveur lui-même.

```
// page.js

import dynamic from "next/dynamic";

import TomStory from "./components/tom/tom-story";
import JerryStory from "./components/jerry/jerry-story";
import SpikeStory from "./components/spike/spike-story";

const AServerComp = dynamic(() => import('./components/server-comps/server-comp'), {
  loading: () => <h1>Loading Through Server Component...</h1>,
})


export default function Home() {
  return (
    <div className="flex flex-wrap justify-center ">
      <TomStory />
      <JerryStory />
      <SpikeStory />

      <AServerComp />
    </div>
  );
}
```

## Devrions-nous utiliser le Lazy Loading pour tous les Client Components dans Next.js ?

Je me suis posé cette question quand j'ai commencé à apprendre le lazy loading. Maintenant que j'ai acquis plus d'expérience avec cette technique, voici mon point de vue :

Vous n'avez pas besoin de charger tous les composants client en lazy loading. L'optimisation est excellente, mais la sur-optimisation peut avoir des effets néfastes. Vous devez identifier où ces optimisations sont nécessaires.

-   Avez-vous des composants client vraiment volumineux ?
-   Mettez-vous inutilement trop de choses dans un seul composant alors que vous devriez le diviser et le refactoriser ?
-   Importez-vous des bibliothèques lourdes dans vos composants client ?
-   Avez-vous opté pour le tree-shaking ?
-   Pouvez-vous identifier les composants client volumineux par route et est-il acceptable de ne pas charger certains ou tous ces composants lors du chargement initial de la page pour cette route ?

Comme vous le voyez, ce sont des questions pertinentes à se poser avant de se lancer dans l'optimisation. Une fois que vous avez les réponses et que vous décidez que vous avez besoin du lazy loading, vous pouvez alors implémenter les techniques apprises dans cet article.

## Et après ?

C'est tout pour le moment. Avez-vous apprécié la lecture de cet article et avez-vous appris quelque chose de nouveau ? Si c'est le cas, j'aimerais savoir si le contenu vous a été utile. Mes réseaux sociaux sont indiqués ci-dessous.

Ensuite, si vous souhaitez apprendre `Next.js` et son écosystème comme `Next-Auth(V5)` avec à la fois des concepts fondamentaux et des projets, j'ai une excellente nouvelle pour vous : vous pouvez [consulter cette playlist sur ma chaîne YouTube][14] avec plus de 20 tutoriels vidéo et plus de 11 heures de contenu captivant à ce jour, gratuitement. J'espère qu'ils vous plairont également.

Restons connectés.

-   Abonnez-vous à ma [chaîne YouTube][15].
-   [Suivez-moi sur X (Twitter)][16] ou [LinkedIn][17] si vous ne voulez pas manquer la dose quotidienne de conseils de montée en compétences.
-   Découvrez et suivez mon travail Open Source sur [GitHub][18].
-   Je publie régulièrement des articles pertinents sur mon [Blog GreenRoots][19], vous pourriez les trouver utiles aussi.

À bientôt pour mon prochain article. D'ici là, prenez soin de vous et continuez d'apprendre.

---

![Tapas Adhikary](https://cdn.hashnode.com/res/hashnode/image/upload/v1645464332466/IynS2q6H6.jpeg)

Développeur Demand-Stack. J'enseigne sur YouTube youtube.com/tapasadhikary comment booster votre carrière tech. Passionné d'Open Source, écrivain.

---

Si vous avez lu jusqu'ici, remerciez l'auteur pour lui montrer que vous appréciez son travail. Dites Merci.

Apprenez à coder gratuitement. Le programme open source de freeCodeCamp a aidé plus de 40 000 personnes à obtenir des emplois de développeurs. [Commencer][20]

[1]: https://www.freecodecamp.org/news/how-to-use-react-server-components/
[2]: https://github.com/tapascript/nextjs-lazy-load
[3]: https://nextjs-lazy-load.netlify.app/
[4]: #heading-qu-est-ce-que-le-lazy-loading
[5]: #heading-techniques-de-lazy-loading-dans-next-js
[6]: #heading-lazy-loading-avec-dynamic-import-et-next-dynamic
[7]: #heading-lazy-loading-avec-react-lazy-et-suspense
[8]: #heading-comment-charger-en-lazy-loading-les-composants-exportes-nommes
[9]: #heading-lazy-loading-de-vos-server-components
[10]: #heading-devrions-nous-utiliser-le-lazy-loading-pour-tous-les-client-components-dans-next-js
[11]: #heading-et-apres
[12]: https://www.youtube.com/watch?v=OpHbSHp8PcI
[13]: https://www.youtube.com/watch?v=KeBxopnhizw
[14]: https://www.youtube.com/watch?v=VSB2h7mVhPg&list=PLIJrr73KDmRwz_7QUvQ9Az82aDM9I8L_8
[15]: https://www.youtube.com/tapasadhikary?sub_confirmation=1
[16]: https://twitter.com/tapasadhikary
[17]: https://www.linkedin.com/in/tapasadhikary/
[18]: https://github.com/atapas
[19]: https://blog.greenroots.info/
[20]: https://www.freecodecamp.org/learn/