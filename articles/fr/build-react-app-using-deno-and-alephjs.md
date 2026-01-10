---
title: Comment construire des applications React avec Deno en utilisant la bibliothèque
  AlephJS
subtitle: ''
author: Akash Joshi
co_authors: []
series: null
date: '2021-03-12T18:08:00.000Z'
originalURL: https://freecodecamp.org/news/build-react-app-using-deno-and-alephjs
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Kapture-2021-03-11-at-11.33.15-4.gif
tags:
- name: Deno
  slug: deno
- name: React
  slug: react
seo_title: Comment construire des applications React avec Deno en utilisant la bibliothèque
  AlephJS
seo_desc: 'If you''re a front end developer who''s just getting started with Deno,
  you might be wondering – can you build something as complex as a NextJS or create-react-app
  (CRA) application using Deno?

  I was recently thinking the same thing. I wanted to try De...'
---

Si vous êtes un développeur front-end qui commence tout juste avec Deno, vous vous demandez peut-être – pouvez-vous construire quelque chose d'aussi complexe qu'une application NextJS ou create-react-app (CRA) en utilisant Deno ?

Je me posais récemment la même question. Je voulais essayer Deno en raison de sa capacité de partage qui résulte de la possibilité d'exécuter une application directement à partir d'une URL. Le compilateur Deno supporte l'exécution de fichiers JavaScript et TypeScript à partir d'une URL et il supporte également les imports à partir d'une URL, ce qui entraîne une portabilité extrême.

J'ai cherché à voir s'il existait des solutions en ligne, mais je n'ai trouvé que [cet article](https://dev.to/adriantwarog/react-deno-server-side-rendering-with-deno-ssr-4438), qui construisait une application React avec rendu côté serveur (SSR) en utilisant des techniques complexes. Ce n'était pas simple, comme commencer avec NextJS ou CRA.

Ainsi, à travers mes recherches en ligne, je suis arrivé à [AlephJS](https://alephjs.org/), qui possède l'une des animations de page d'accueil les plus cool jamais vues.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Kapture-2021-03-11-at-11.33.15-3.gif align="left")

Aleph est un framework React sans configuration, basé sur TypeScript, tout comme NextJS. Le seul inconvénient est qu'Aleph est encore très beaucoup en version alpha.

Alors, pour obtenir une véritable expérience React similaire à Next à l'intérieur de Deno, commençons avec AlephJS. Il possède de nombreuses conventions similaires à Next, telles que :

* Un répertoire `/pages` pour créer des routes URL

* Support direct des fichiers `.js, .jsx, .ts, .tsx` dans les pages

* Un répertoire `/public` pour servir des actifs statiques comme des fichiers vidéo, audio ou image

* Un dossier `/pages/api` pour servir des fichiers JavaScript ou TypeScript en tant qu'API sans serveur.

Si vous souhaitez regarder une vidéo sur la façon de faire cela pour compléter votre lecture, consultez-la ici :

%[https://www.youtube.com/watch?v=SDTedmFhnQc] 

## Comment commencer avec AlephJS

Pour pouvoir utiliser AlephJS, vous devez avoir Deno installé sur votre machine. Vous pouvez voir comment installer et commencer avec Deno dans mon [article précédent ici](https://www.freecodecamp.org/news/build-a-url-shortener-in-deno/).

Pour commencer avec Aleph, vous devez d'abord installer l'interface de ligne de commande (CLI) Aleph en exécutant cette commande :

```bash
deno install -A -f -n aleph https://deno.land/x/aleph@v0.3.0-alpha.1/cli.ts
```

Après l'installation, vous pouvez exécuter `aleph -h` pour vérifier si l'installation s'est déroulée correctement.

En raison de la portabilité de Deno, vous pouvez remplacer `aleph` par `deno run -A https://deno.land/x/aleph@v0.3.0-alpha.1/cli.ts start $app_URI` pour toute commande et il sera capable d'exécuter le programme Aleph sans avoir le CLI installé localement.

Pour créer une application de démarrage, exécutez :

```bash
aleph init hello
cd hello
```

Et démarrez l'application en mode développement en utilisant `aleph dev` pour démarrer un serveur sur le port `8080`.

Pour démarrer l'application en mode production, vous devez d'abord `build` l'application puis exécuter l'application construite. Vous pouvez faire cela à travers ces commandes :

```bash
aleph build # build your app
aleph start # runs built app
```

Après avoir initialisé votre application Aleph, vous constaterez que le composant racine est défini dans `pages/index.tsx`. C'est un composant React normal. Vous pouvez expérimenter avec pour voir comment Aleph fonctionne.

Vous pouvez ajouter plus de routes à votre application en créant plus de fichiers `.jsx` ou `.tsx` à l'intérieur du dossier `pages`. Vous pouvez en lire plus sur le routage dans Aleph [ici](https://alephjs.org/docs/basic-features/routing).

## Comment importer des bibliothèques dans Deno

J'ai écrit précédemment sur Deno sur [freeCodeCamp](https://www.freecodecamp.org/news/build-a-url-shortener-in-deno/) où j'ai démontré quelques bases de Deno, y compris les imports d'URL. Puisque Aleph est un framework Deno, toutes les imports se font de la manière "Deno".

Il existe deux types de bibliothèques que vous pouvez importer dans une application Deno.

1. Importer des bibliothèques natives Deno : Ces bibliothèques ont été soit construites pour Deno, soit portées depuis npm pour supporter l'utilisation de Deno.

2. Importer depuis NPM : si vous avez travaillé avec JS récemment, vous connaissez probablement npm. Si ce n'est pas le cas, npm (la société derrière le gestionnaire de paquets node) est le dépôt standard pour toutes les bibliothèques JavaScript. Heureusement, Deno a un support limité pour les bibliothèques npm. En utilisant des outils comme [esm.sh](http://esm.sh) ou skypack.dev, les utilisateurs peuvent importer des bibliothèques npm dans Deno.

### 1. Comment importer des bibliothèques natives Deno

Vous pouvez importer des bibliothèques natives Deno dans votre application en important directement leurs URL. Vous pouvez trouver une liste de bibliothèques Deno ici : [deno.land/x](http://deno.land/x)

Pour tester cela, importons cette [bibliothèque standard de formatage de date Deno](https://deno.land/std@0.88.0/datetime), et appelons une fonction de formatage de date dans une page React. Créez un fichier `date-import.tsx` dans le dossier `pages` de votre application. À l'intérieur du fichier, écrivez le code suivant :

```jsx
// react est une importation obligatoire dans Aleph
import React from "react";

// importer la fonction format depuis son URL
import { format } from "https://deno.land/std@0.88.0/datetime/mod.ts";

// capitaliser le nom de la fonction pour qu'elle soit reconnue comme un composant React
export default function DateImport() {
	// Ici, l'appel direct de la fonction format fonctionne comme prévu.
  return <section>Bonjour à tous ! Aujourd'hui nous sommes le : {format(new Date(), "dd-MM-yyyy")}</section>;
}
```

Pour voir le résultat de ce fichier, allez sur [localhost:8080/date-import](http://localhost:8080/date-import), ou son équivalent pour votre serveur. Vous devriez voir la page affichant la date d'aujourd'hui.

### 2. Comment importer des bibliothèques depuis NPM

Pour importer une bibliothèque npm, vous pouvez également importer directement depuis une URL – mais dans ce cas, il y a un léger changement. Puisque nous avons parlé de [esm.sh](http://esm.sh) et skypack.dev, essayons de les utiliser en action. Dans ce cas, essayons d'utiliser la bibliothèque [dayjs](https://www.npmjs.com/package/dayjs) dans notre projet.

> Note : Toutes les bibliothèques npm ne fonctionnent pas correctement dans Deno car elles peuvent dépendre de fonctions spécifiques à Node.

Pour importer une bibliothèque dans [esm.sh](http://esm.sh), vous ajoutez le nom du package de la bibliothèque à l'URL. Dans ce cas, pour importer dayjs, nous importerions [`https://esm.sh/dayjs`](https://esm.sh/dayjs). Cela fonctionne également pour tous les fichiers CSS que vous pourriez vouloir importer depuis une bibliothèque.

Maintenant, créons un fichier dans `pages` appelé `dayjs-import.tsx`. Ainsi, le code dans notre page ressemblera à ceci :

```jsx
// react est une importation obligatoire dans Aleph
import React from "react";

// importer la bibliothèque npm dayjs en utilisant esm.sh
import dayjs from "https://esm.sh/dayjs";

// capitaliser le nom de la fonction pour qu'elle soit reconnue comme un composant React
export default function DateImport() {
	// appeler la fonction dayjs directement pour afficher la date d'aujourd'hui
  return <section>Bonjour à tous ! Aujourd'hui nous sommes le : {dayjs().format("DD-MM-YYYY")}</section>;
}
```

Pour voir le résultat de ce fichier, allez sur [localhost:8080/dayjs-import](http://localhost:8080/dayjs-import), ou son équivalent pour votre serveur. Vous devriez voir la page affichant la date du jour.

Il y a une chose importante avant de continuer, cependant – comment gérez-vous les **imports React** comme l'import de `useState`, `useEffect`, et ainsi de suite ? Heureusement, les développeurs d'Aleph ont déjà écrit un exemple pour nous.

Allez dans `./lib/useCounter.ts` et vous trouverez le code pour le hook personnalisé qui est utilisé pour le compteur dans la page d'accueil.

Puisque je veux me concentrer sur Aleph et React eux-mêmes dans cet article, pour découvrir toutes les différentes façons dont vous pouvez importer un fichier CSS dans Aleph, visitez [cette page de la documentation officielle](https://alephjs.org/docs/basic-features/built-in-css-support).

## Comment construire une application d'exemple avec Deno et AlephJS

Maintenant, plongeons dans le vif du sujet et essayons de construire une application React dans Aleph nous-mêmes. Nous allons construire "Is It Down ?", une application d'exemple que j'avais réalisée en utilisant une API existante de vérification de site web. Cette application nous permettra de vérifier si un site web est actuellement en ligne ou hors ligne.

Voici le lien CodeSandbox : [https://codesandbox.io/s/awesome-firefly-5dofg](https://codesandbox.io/s/awesome-firefly-5dofg)

%[https://codesandbox.io/embed/awesome-firefly-5dofg?fontsize=14&hidenavigation=1&theme=dark&view=preview] 

La construction de cette application vous montrera comment utiliser le hook State, le hook Effect, et comment faire des appels API dans Aleph.

Créez un nouveau fichier appelé `web-checker.tsx` dans votre dossier `pages`. Commençons par ajouter simplement les éléments d'interface utilisateur en premier. Nous allons afficher un élément `h1` avec le titre, un élément `h2` liant à l'API, et un élément de formulaire pour prendre l'entrée de l'utilisateur. Il s'agit d'une page non interactive qui affiche simplement les éléments.

```jsx
import React from "react";

export default function App() {
	return (
    <div style={{ fontFamily: "sans-serif", textAlign: "center" }}>
      <h1>Est-ce en panne ?</h1>
      <h2>
        Allez{" "}
        <a
          href="https://rapidapi.com/jakash1997/api/website-data-gathering-and-update-tracking"
          target="_blank"
        >
          ici
        </a>{" "}
        pour obtenir une clé API
      </h2>

      <form
        onSubmit={(e) => {
          e.preventDefault();
        }}
      >
        <input
          type="text"
        />
        <button type="submit">Soumettre</button>
      </form>
    </div>
  );
}
```

Ensuite, pour capturer l'état du champ de saisie, et également pour capturer la réponse de l'appel API que nous devrons faire, introduisons l'état.

```jsx
// importer useState depuis react
import React, { useState } from "react";

export default function App() {
  // définir les deux variables d'état
  const [siteURL, setUrl] = useState("");
  const [response, setResponse] = useState(undefined);
...
```

Maintenant, nous allons utiliser cet état à l'intérieur de notre élément d'entrée afin qu'il puisse réagir à celui-ci.

```jsx
...
<input
  value={siteURL}
  onChange={(e) => setUrl(e.target.value)}
  type="text"
/>
...
```

Nous allons également ajouter du code pour afficher une réponse lorsqu'elle est retournée par la réponse de l'API :

```jsx
...
	</form>
	
	<br />
	
	<code>{JSON.stringify(response, null, 2)}</code>
</div>
...
```

Maintenant, pour commencer à intégrer l'API, essayons de former correctement la requête. Dans ce cas, l'API est un simple appel `GET`, donc nous devons seulement passer un paramètre et une clé API.

Tout d'abord, allez ici et générez une clé API : [https://rapidapi.com/jakash1997/api/website-data-gathering-and-update-tracking](https://rapidapi.com/jakash1997/api/website-data-gathering-and-update-tracking). Trouvez la clé API comme vous le voyez dans la capture d'écran ci-dessous, et gardez-la quelque part en sécurité :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot_2021-03-08_at_3.47.01_PM.png align="left")

Ensuite, créons une fonction séparée `submitData` qui générera les données de requête nécessaires. Nous allons utiliser la bibliothèque `axios` pour effectuer notre appel `GET`, donc nous allons former son objet d'options.

```jsx
...
const [response, setResponse] = useState(undefined);

const submitData = (siteURL) => {
  setResponse("Chargement...");
  const options = {
		// passage de siteURL ici par notation d'objet raccourcie
    params: { siteURL },

		// passage des en-têtes requis ici
    headers: {
      "x-rapidapi-key": "VOTRE_CLE_API",
      "x-rapidapi-host":
        "website-data-gathering-and-update-tracking.p.rapidapi.com",
    },
  };

	// imprimer les options ici
	console.log("options", options);
};

return (
...
```

Et nous ajoutons cela à la fonction `onSubmit` dans notre formulaire.

```jsx
onSubmit={(e) => {
  e.preventDefault();
  submitData(siteURL);
}}
```

Maintenant, chaque fois que vous appuyez sur le bouton Soumettre, vous verrez les `options` que nous avons générées dans la console. Si vous voyez l'objet `options` dans la console, vous êtes sur la bonne voie jusqu'à présent !

Ensuite, nous avons l'étape simple d'importer la bibliothèque `axios` en utilisant [`http://esm.sh`](http://esm.sh) et de l'utiliser pour faire un appel API.

Importez `axios` après l'import `react` comme ceci :

```jsx
import React, { useState } from "react";
import axios from "https://esm.sh/axios";

...
```

Et utilisez-le dans la fonction `submitData` comme suit :

```jsx
...
	axios
    .get(
      "https://website-data-gathering-and-update-tracking.p.rapidapi.com/sitecheck",
      options
    )
    .then(function (response) {
      setResponse(response.data);
      console.log(response.data);
    })
    .catch(function (error) {
      console.error(error);
    });
};
...
```

Et c'est tout ! Essayez de soumettre le formulaire à nouveau, et cette fois vous verrez le résultat à la fois à l'écran et dans la console.

## Conclusion

Maintenant, vous connaissez les bases d'Aleph. C'est un outil vraiment intéressant qui vous permet de mélanger vos connaissances existantes en React avec la nature orientée vers l'avenir et la sécurité de [deno.land](http://deno.land).

Si vous avez aimé ce tutoriel, vous pouvez me suivre sur Twitter [@thewritingdev](http://twitter.com/thewritingdev).