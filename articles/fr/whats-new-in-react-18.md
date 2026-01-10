---
title: Quoi de neuf dans React 18 Alpha ? Concurrence, Regroupement, l'API Transition
  et plus encore
subtitle: ''
author: Akash Joshi
co_authors: []
series: null
date: '2021-07-09T18:42:26.000Z'
originalURL: https://freecodecamp.org/news/whats-new-in-react-18
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/SUSPENSE-BATCHING-TRANSITION.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Quoi de neuf dans React 18 Alpha ? Concurrence, Regroupement, l'API Transition
  et plus encore
seo_desc: 'Hey everyone! In this article, I''m going to show you what''s new in the
  latest of version of React – React 18 alpha – in under 8 minutes.

  First, you might be wondering whether the latest set of changes will break anything
  with your current setup, or w...'
---

Salut à tous ! Dans cet article, je vais vous montrer ce qui est nouveau dans la dernière version de React – React 18 alpha – en moins de 8 minutes.

Tout d'abord, vous vous demandez peut-être si le dernier ensemble de changements va casser quelque chose avec votre configuration actuelle, ou si vous devrez apprendre de nouveaux concepts complètement sans rapport.

Eh bien, ne vous inquiétez pas – vous pouvez continuer avec votre travail actuel ou continuer à apprendre votre cours React actuel tel quel, car React 18 ne casse rien.

Si vous voulez regarder une vidéo pour compléter votre lecture, consultez-la ici :

%[https://www.youtube.com/watch?v=IOeqma3YcGs]

Pour ceux d'entre vous qui veulent vraiment apprendre ce qui se passe, voici le détail.

Juste une petite note : React 18 est toujours en alpha et n'est pas encore sorti. Donc voici ce à quoi vous pouvez vous attendre lorsqu'il sera publié.

## Qu'est-ce que la Concurrence dans React ?

Le thème majeur de cette version est la **concurrence**. Pour commencer, regardons ce qu'est la concurrence.

La concurrence est la capacité d'exécuter plusieurs tâches simultanément. Prenons l'exemple d'une application React standard, où une animation est en cours de lecture dans un composant, et en même temps un utilisateur peut cliquer ou taper dans d'autres composants React.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f5a65bda-b76b-466f-abe3-3d8fbb232655/firefox_PJSGkv5qWX.png](https://www.freecodecamp.org/news/content/images/2021/07/firefox_juLm49pOIQ.png align="left")

Ici, tandis que l'utilisateur tape et clique sur des boutons, une animation est également rendue dans le contexte de React.

React doit gérer tous les appels de fonctions, les appels de hooks et les rappels d'événements, dont plusieurs peuvent même se produire en même temps. Si React passe tout son temps à rendre les images d'animation, l'utilisateur aura l'impression que l'application est "bloquée", car elle ne réagira pas à ses entrées.

Maintenant, React, fonctionnant sur un processus à thread unique, doit combiner, réorganiser et prioriser ces événements et fonctions afin de pouvoir offrir aux utilisateurs une expérience optimale et performante.

Pour ce faire, React utilise un "dispatcher" en interne qui est responsable de la priorisation et de l'invocation de ces rappels.

Avant React 18, l'utilisateur n'avait aucun moyen de contrôler l'ordre d'invocation de ces fonctions. Mais maintenant, React donne un certain contrôle de cette boucle d'événements à l'utilisateur via l'API Transition.

Vous pouvez en lire plus à ce sujet dans cet article de Dan Abramov : [Une explication simple de la concurrence](https://github.com/reactwg/react-18/discussions/46#discussioncomment-846786).

## L'API Transition

Les développeurs de React ont exposé quelques API qui permettent aux utilisateurs de React d'avoir un certain contrôle sur la concurrence.

L'une de ces API est `startTransition`, qui permet aux développeurs d'indiquer à React quelles actions peuvent bloquer le thread et causer des retards à l'écran.

Typiquement, ces actions sont celles pour lesquelles vous auriez précédemment utilisé le debounce, comme les appels réseau via une API de recherche, ou les processus gourmands en rendu comme la recherche dans un tableau de 1000 chaînes.

Les mises à jour enveloppées dans `startTransition` sont marquées comme non urgentes et sont interrompues si des mises à jour plus urgentes comme des clics ou des presses de touches arrivent.

Si une transition est interrompue par l'utilisateur (par exemple, en tapant plusieurs lettres dans un champ de recherche), React jettera le travail de rendu obsolète qui n'était pas terminé et ne rendra que la dernière mise à jour.

### Exemple d'API Transition

Pour comprendre cela plus en détail, considérons un composant avec un champ de recherche. Supposons qu'il a 2 fonctions pour contrôler l'état :

```jsx
// Mettre à jour la valeur de l'entrée
setInputValue(input)

// Mettre à jour la valeur recherchée et les résultats de la recherche
setSearchQuery(input);
```

`setInputValue` est responsable de la mise à jour du champ d'entrée, tandis que `setSearchQuery` est responsable de l'exécution de la recherche basée sur la valeur d'entrée actuelle. Maintenant, si ces appels de fonctions se produisaient de manière synchrone chaque fois que l'utilisateur commence à taper, l'une des deux choses suivantes se produirait :

1. Plusieurs appels de recherche seraient effectués, ce qui retarderait ou ralentirait d'autres appels réseau.

2. Ou, plus probablement, l'opération de recherche s'avérerait très lourde et bloquerait l'écran à chaque frappe.

Une façon de résoudre ce problème aurait été d'utiliser le debounce, qui aurait espacé les appels réseau ou les opérations de recherche. Mais le problème avec le debounce est que nous devons souvent ajuster et optimiser le minuteur de debounce.

Dans ce cas, nous pouvons envelopper setSearchQuery dans `startTransition`, permettant à React de le traiter comme non urgent et de le retarder tant que l'utilisateur tape.

```jsx
import { startTransition } from 'react';

// Urgent : Montrer ce qui a été tapé
setInputValue(input);

// Marquer les mises à jour d'état à l'intérieur comme transitions
startTransition(() => {
  // Transition : Montrer les résultats
  setSearchQuery(input);
});
```

Les transitions vous permettent de garder la plupart des interactions réactives même si elles entraînent des changements significatifs dans l'UI. Elles vous permettent également d'éviter de perdre du temps à rendre du contenu qui n'est plus pertinent.

React fournit également un nouveau hook appelé `useTransition`, afin que vous puissiez afficher un chargeur pendant que la transition est en attente. Cela aide à indiquer à l'utilisateur que l'application traite son entrée et affichera les résultats sous peu.

```jsx
import { useTransition } from 'react';

const [isPending, startTransition] = useTransition();

const callback = () => {
  // Urgent : Montrer ce qui a été tapé
  setInputValue(input);

  // Marquer les mises à jour d'état à l'intérieur comme transitions
  startTransition(() => {
    // Transition : Montrer les résultats
    setSearchQuery(input);
  });
}

{isPending && <Spinner />}
```

En règle générale, vous pouvez utiliser l'API de transition partout où des appels réseau ou des processus bloquant le rendu sont présents.

Vous pouvez en lire plus sur l'API dans cet article, [Une explication de startTransition](https://github.com/reactwg/react-18/discussions/41) par Ricky de l'équipe principale de React.

### Démos de l'API Transition

Utilisez `useTransition` et Suspense dans une application : [https://codesandbox.io/s/sad-banach-tcnim?file=/src/App.js:664-676](https://codesandbox.io/s/sad-banach-tcnim?file=/src/App.js:664-676)

Démo de `startTransition` avec un algorithme de rendu complexe : [https://react-fractals-git-react-18-swizec.vercel.app/](https://react-fractals-git-react-18-swizec.vercel.app/)

## Le Regroupement dans React

Ensuite, nous avons le regroupement. Le regroupement est quelque chose que le développeur n'a généralement pas à gérer, mais il est bon de savoir ce qui se passe en coulisses.

Chaque fois que vous utilisez setState pour changer une variable à l'intérieur d'une fonction, au lieu de faire un rendu à chaque setState, React collecte tous les setStates et les exécute ensemble. Cela s'appelle le regroupement.

```jsx
function App() {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  function handleClick() {
    setCount(c => c + 1); // Ne re-rend pas encore
    setFlag(f => !f); // Ne re-rend pas encore
    // React ne re-rendra qu'une seule fois à la fin (c'est le regroupement !)
  }

  return (
    <div>
      <button onClick={handleClick}>Suivant</button>
      <h1 style={{ color: flag ? "blue" : "black" }}>{count}</h1>
    </div>
  );
}
```

C'est génial pour la performance car cela évite les re-rendus inutiles. Cela empêche également votre composant de rendre des états "à moitié terminés" où seule une variable d'état a été mise à jour, ce qui peut causer des bugs d'UI et des glitches dans votre code.

Cependant, React n'était pas toujours cohérent quant au moment où il effectuait le regroupement. Cela était dû au fait que React n'utilisait le regroupement que *pendant* les événements du navigateur (comme un clic), mais ici nous mettons à jour l'état *après* que l'événement a déjà été traité (dans un rappel de fetch) :

```jsx
function App() {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  function handleClick() {
    fetchSomething().then(() => {
      // React 17 et les versions antérieures ne regroupent PAS ces mises à jour car
      // elles s'exécutent *après* l'événement dans un rappel, et non *pendant* celui-ci
      setCount(c => c + 1); // Provoque un re-rendu
      setFlag(f => !f); // Provoque un re-rendu
    });
  }

  return (
    <div>
      <button onClick={handleClick}>Suivant</button>
      <h1 style={{ color: flag ? "blue" : "black" }}>{count}</h1>
    </div>
  );
}
```

À partir de React 18 avec `[createRoot](<https://github.com/reactwg/react-18/discussions/5>)`, toutes les mises à jour d'état seront automatiquement regroupées, peu importe d'où elles proviennent.

Cela signifie que les mises à jour à l'intérieur des timeouts, des promesses, des gestionnaires d'événements natifs ou de tout autre événement seront regroupées de la même manière que les mises à jour à l'intérieur des événements React. Cela entraînera moins de travail de rendu par React, et donc de meilleures performances dans les applications.

Vous pouvez en lire plus sur le regroupement ici dans [Une explication du Regroupement](https://github.com/reactwg/react-18/discussions/21) par Dan Abramov.

### Démos du Regroupement

Avant React 18 : [https://codesandbox.io/s/hopeful-fire-ge4t2?file=/src/App.tsx](https://codesandbox.io/s/hopeful-fire-ge4t2?file=/src/App.tsx)

Après React 18 : [https://codesandbox.io/s/morning-sun-lgz88?file=/src/index.js](https://codesandbox.io/s/morning-sun-lgz88?file=/src/index.js)

## L'API Suspense

React 18 inclut de nombreux changements pour améliorer les performances de React dans un contexte de [Rendu Côté Serveur](https://www.freecodecamp.org/news/server-side-rendering-your-react-app-in-three-simple-steps-7a82b95db82e/). Le rendu côté serveur est un moyen de rendre les données JS en HTML sur le serveur pour économiser du calcul sur le frontend. Cela entraîne un chargement initial de la page plus rapide dans la plupart des cas.

React effectue le rendu côté serveur en 4 étapes séquentielles :

* Sur le serveur, les données sont récupérées pour chaque composant.

* Sur le serveur, l'ensemble de l'application est rendu en HTML et envoyé au client.

* Sur le client, le code JavaScript de l'ensemble de l'application est récupéré.

* Sur le client, le JavaScript connecte React au HTML généré par le serveur, ce qui est connu sous le nom d'Hydratation.

React 18 introduit l'API `Suspense`, qui vous permet de diviser votre application en **unités indépendantes plus petites**, qui passeront par ces étapes indépendamment et ne bloqueront pas le reste de l'application. En conséquence, les utilisateurs de votre application verront le contenu plus tôt et pourront commencer à interagir avec lui beaucoup plus rapidement.

### Comment fonctionne l'API Suspense ?

#### Streaming HTML

Avec le SSR d'aujourd'hui, le rendu HTML et l'hydratation sont "tout ou rien". Le client doit récupérer et hydrater toute l'application en une seule fois.

Mais React 18 vous offre une nouvelle possibilité. Vous pouvez envelopper une partie de la page avec `<Suspense>`.

```jsx
<Suspense fallback={<Spinner />}> 
  {children}
</Suspense>
```

En enveloppant le composant dans `<Suspense>`, nous disons à React qu'il n'a pas besoin d'attendre les commentaires pour commencer à streamer le HTML pour le reste de la page. Au lieu de cela, React enverra le placeholder (un spinner) à la place.

Lorsque les données pour les commentaires sont prêtes sur le serveur, React enverra du HTML supplémentaire dans le même flux, ainsi qu'une balise `<script>` inline minimale pour placer ce HTML au "bon endroit".

#### Hydratation Sélective

Avant React 18, l'hydratation ne pouvait pas commencer si le code JavaScript complet de l'application n'avait pas été chargé. Pour les applications plus grandes, ce processus peut prendre un certain temps.

Mais dans React 18, `<Suspense>` vous permet d'hydrater l'application avant que les composants enfants n'aient été chargés.

En enveloppant les composants dans `<Suspense>`, vous pouvez dire à React qu'ils ne doivent pas bloquer le reste de la page de streamer – et même l'hydratation. Cela signifie que vous n'avez plus à attendre que tout le code soit chargé pour commencer l'hydratation. React peut hydrater les parties au fur et à mesure qu'elles sont chargées.

Ces 2 fonctionnalités de `Suspense` et plusieurs autres changements introduits dans React 18 accélèrent considérablement le chargement initial des pages.

Vous pouvez en lire plus dans cet article [Une explication de Suspense SSR](https://github.com/reactwg/react-18/discussions/37) et les changements associés par Dan Abramov.

### Démo de Suspense

[https://codesandbox.io/s/recursing-mclaren-1ireo?file=/src/index.js:458-466](https://codesandbox.io/s/recursing-mclaren-1ireo?file=/src/index.js:458-466)

## Résumé

Pour résumer, les fonctionnalités que React 18 apporte sont :

* Contrôle de la concurrence avec l'API Transition,

* Regroupement automatique des appels de fonctions et des événements pour améliorer les performances dans l'application, et

* Chargement de pages beaucoup plus rapide pour le SSR avec Suspense.

Bien que ce ne soit pas un grand écart par rapport à la version précédente de React, tous ces changements font de React un précurseur pour tous les frameworks existants.

Merci d'avoir lu cela ! Vous pouvez consulter mes précédents articles et tutoriels sur React ici sur freeCodeCamp. Vous pouvez également me suivre sur Twitter [@thewritingdev](https://twitter.com/thewritingdev), où je poste quotidiennement du contenu sur React et le développement web.