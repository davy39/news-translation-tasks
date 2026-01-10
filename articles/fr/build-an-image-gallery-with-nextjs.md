---
title: Comment créer une galerie d'images avec NextJS en utilisant l'API Pexels et
  Chakra UI
subtitle: ''
author: Ashutosh K Singh
co_authors: []
series: null
date: '2020-11-16T14:55:07.000Z'
originalURL: https://freecodecamp.org/news/build-an-image-gallery-with-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Screenshot_2020-11-12-NextJS-Image-Gallery-1.png
tags:
- name: image
  slug: image
- name: Next.js
  slug: nextjs
- name: projects
  slug: projects
seo_title: Comment créer une galerie d'images avec NextJS en utilisant l'API Pexels
  et Chakra UI
seo_desc: "In this article, we will build an Image Gallery with Next.js using the\
  \ Pexels API and Chakra UI v1, a modular and accessible component library. \nWe\
  \ will also use the Next.js Image component to optimize the images fetched from\
  \ the Pexels API.\nIf you w..."
---

Dans cet article, nous allons créer une galerie d'images avec [Next.js](https://nextjs.org/) en utilisant l'[API Pexels](https://www.pexels.com/api/) et [Chakra UI v1](https://chakra-ui.com/), une bibliothèque de composants modulaire et accessible. 

Nous utiliserons également le [composant Image de Next.js](https://nextjs.org/blog/next-10#built-in-image-component-and-automatic-image-optimization) pour optimiser les images récupérées depuis l'API Pexels.

Si vous souhaitez plonger directement dans le code, consultez le [dépôt GitHub ici](https://github.com/lelouchB/next-image-gallery).

Et voici un lien vers la version déployée : [https://next-image-gallery.vercel.app/](https://next-image-gallery.vercel.app/).

#### Quels concepts et sujets allons-nous couvrir dans cet article ?

* Comment installer et utiliser [Chakra UI v1](https://chakra-ui.com/) avec [Next.js](https://nextjs.org/)
* Comment récupérer des données dans Next.js depuis [une API](https://www.pexels.com/api/)
* Comment utiliser le [composant Image de Next.js](https://nextjs.org/docs/basic-features/image-optimization)
* Comment configurer les [routes dynamiques](https://nextjs.org/docs/routing/dynamic-routes) dans Next.js

## Table des matières

* [Prérequis](#heading-prerequis)
* [Comment configurer et installer Next.js](#heading-comment-configurer-et-installer-nextjs)
* [Comment générer la clé API Pexels](#heading-comment-generer-la-cle-api-pexels)
* [Comment ajouter un titre à la galerie](#heading-comment-ajouter-un-titre-a-la-galerie)
* [Comment récupérer des données depuis l'API Pexels](#heading-comment-recuperer-des-donnees-depuis-lapi-pexels)
* [Comment afficher des photos sur la page](#heading-comment-afficher-des-photos-sur-la-page)
* [Comment styliser les images avec Chakra UI](#heading-comment-styliser-les-images-avec-chakra-ui)
* [Comment ajouter une fonctionnalité de recherche à la galerie](#heading-comment-ajouter-une-fonctionnalite-de-recherche-a-la-galerie)
* [Comment ajouter des routes dynamiques aux images](#heading-comment-ajouter-des-routes-dynamiques-aux-images)
* [Conclusion](#heading-conclusion)

Maintenant, commençons.

## Prérequis

Avant de commencer, vous devriez avoir :

1. Des connaissances en [HTML, CSS et JavaScript](https://www.freecodecamp.org/learn/responsive-web-design/).
2. Des connaissances de base en [React](https://www.freecodecamp.org/learn/front-end-libraries/react/) et Next.js.
3. [Node](https://nodejs.org/en/) et NPM installés sur votre machine de développement locale.
4. Un éditeur de code de votre choix.
5. [React Dev Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) (optionnel)

Si vous avez l'impression que votre progression est entravée parce que vous ne connaissez pas assez ces sujets, consultez [https://www.freecodecamp.org/learn](https://www.freecodecamp.org/learn). Les modules géniaux disponibles vous mettront en route en un rien de temps.

## Comment configurer et installer Next.js

Nous allons utiliser [Create Next App](https://nextjs.org/docs/api-reference/create-next-app) pour initialiser rapidement un projet Next.js. Dans le répertoire racine de votre projet, exécutez les commandes suivantes dans le terminal.

```bash
npx create-next-app next-image-gallery
cd next-image-gallery
npm run dev
```

La dernière commande, `npm run dev`, démarrera le serveur de développement sur le port 3000 de votre système. 

Accédez à [http://localhost:3000](http://localhost:3000/) dans le navigateur. Voici à quoi ressemblera votre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-26.png)
_Bienvenue sur Next.js - http://localhost:3000_

Exécutez la commande suivante pour installer Chakra UI :

```bash
npm i @chakra-ui/react @emotion/react @emotion/styled framer-motion @chakra-ui/icons
```

L'étape suivante consiste à nettoyer le code d'exemple généré par `create-next-app` et à configurer le projet pour utiliser Chakra UI. 

1. Supprimez les dossiers `styles` et `pages/api`.
2. Mettez à jour votre fichier `pages/_app.js` comme ceci :

```jsx
// pages/_app.js
import { ChakraProvider } from "@chakra-ui/react";

function MyApp({ Component, pageProps }) {
  return (
    <ChakraProvider>
      <Component {...pageProps} />
    </ChakraProvider>
  );
}

export default MyApp;

```

3.  Modifiez `pages/index.js` comme ceci :

```jsx
// pages/index.js
import Head from "next/head";

export default function Home() {
  return (
    <div>
      <Head>
        <title> Galerie d'images NextJS</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
    </div>
  );
}

```

Retournez à [http://localhost:3000](http://localhost:3000/). Vous verrez que l'application est vide, mais le titre a changé pour `Galerie d'images NextJS`. 

Vous pouvez maintenant fermer le serveur de développement.

## Comment générer la clé API Pexels

Nous allons utiliser l'[API Pexels](https://www.pexels.com/api/) pour récupérer des images pour notre galerie. Vous devrez créer une clé API Pexels pour authentifier vos requêtes API. L'API elle-même est complètement gratuite à utiliser.

Vous pouvez effectuer jusqu'à 200 requêtes par heure et 20 000 requêtes par mois à l'API Pexels.

Rendez-vous sur [https://www.pexels.com/join-consumer/](https://www.pexels.com/join-consumer/) et créez un nouveau compte sur Pexels.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-28.png)
_Créer un nouveau compte_

Après avoir rempli vos détails, vous devrez également confirmer votre compte avant de demander une clé API. Vérifiez donc votre boîte de réception et confirmez votre compte Pexels.

Accédez à [https://www.pexels.com/api/new/](https://www.pexels.com/api/new/) et remplissez les détails pour une nouvelle clé API et cliquez sur **Demander une clé API**

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-31.png)
_Demander une clé API_

N'oubliez pas de suivre les [directives de l'API](https://www.pexels.com/api/documentation/#guidelines). Copiez maintenant la clé API affichée sur la page suivante.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-32.png)
_Clé API_

Dans le répertoire racine de votre projet, créez un nouveau fichier nommé `.env.local` pour stocker cette clé API en toute sécurité. Exécutez les commandes suivantes pour créer le fichier :

```bash
touch .env.local
```

À l'intérieur de ce fichier `.env.local`, créez une nouvelle variable d'environnement nommée `PEXELS_API_KEY` et collez la clé API là.

```env
NEXT_PUBLIC_PEXELS_API_KEY = ''
```

Next.js prend en charge le chargement des variables d'environnement depuis `.env.local` dans `process.env`.

Par défaut, toutes les variables d'environnement chargées via `.env.local` ne sont disponibles que dans l'environnement Node.js. Cela signifie qu'elles ne seront pas exposées au navigateur. L'utilisation du préfixe `NEXT_PUBLIC_` expose la variable d'environnement au navigateur.

Vous pouvez en lire plus à ce sujet [ici](https://nextjs.org/docs/basic-features/environment-variables).

## Comment ajouter un titre à la galerie

Dans cette section, nous allons ajouter un titre à notre galerie.

Importez et ajoutez le composant `Box` à `index.js` comme ceci :

```jsx
//pages/index.js
import Head from "next/head";
import { Box } from "@chakra-ui/react";
export default function Home() {
  return (
    <div>
      <Head>
        <title> Galerie d'images NextJS</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Box overflow="hidden" bg="purple.100" minH="100vh"></Box>
    </div>
  );
}

```

Accédez à [http://localhost:3000](http://localhost:3000/). Vous verrez que votre application a une couleur de fond violet clair.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-56.png)
_Page vide avec fond violet clair_

Voici ce que nous faisons :

* Dans Chakra UI, `bg` est la propriété raccourcie pour `background`. En passant `bg="purple.100"`, le fond de l'application change en violet clair. Le nombre après la couleur représente la nuance de la couleur où la plus claire est `50`, et la plus foncée est `900`. 
Voici une image des [docs Chakra UI](https://chakra-ui.com/docs/theming/theme#purple) pour mieux illustrer ce point.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-57.png)
_Nuances de violet_

* Définir `minH="100vh"` fait en sorte que l'application ait au moins 100% de la hauteur de l'élément parent. `minH` est la propriété raccourcie pour `min-height`.
* Pour se débarrasser des barres de défilement supplémentaires au cas où le contenu déborderait de l'élément parent, `overflow="hidden"` est passé.

Pour ajouter un titre, nous allons utiliser les composants `Text` et `Container` disponibles dans Chakra UI.

 Modifiez l'import `Box` dans `index.js` comme ceci :

```jsx
import { Box, Container, Text } from "@chakra-ui/react";

```

Maintenant, ajoutez le composant `Container` à l'intérieur du composant `Box`.

```jsx  
<Box overflow="hidden" bg="purple.100" minH="100vh">
  <Container></Container>
</Box>

```

Vous ne verrez aucun changement dans votre application, mais le composant `Container` a ajouté un peu de remplissage horizontal dans votre application, ce qui sera plus apparent après l'ajout du composant `Text`.

Ajoutez le code suivant à l'intérieur du composant `Container` :

```jsx
<Container>
  <Text
    color="pink.800"
    fontWeight="semibold"
    mb="1rem"
    textAlign="center"
    textDecoration="underline"
    fontSize={["4xl", "4xl", "5xl", "5xl"]}
  >
    Galerie d'images NextJS
  </Text>
</Container>
```

Décortiquons le code ci-dessus et discutons-en.

* `color` est utilisé pour définir la couleur du texte sur `pink.900`.
* `fontWeight` est utilisé pour définir l'épaisseur des caractères.
* `mb` est une propriété raccourcie pour `margin-bottom` et `1rem=16px`.
* `textAlign="center"` aligne le texte au centre.
* `textDecoration="underline"` ajoute une ligne sous le texte.
* `fontSize`, comme son nom l'indique, définit la taille du texte.

Voici à quoi ressemblera votre application :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-58.png)
_Titre - Galerie d'images NextJS_

```javascript
xs: "12px"
sm: "14px"
md: "16px"
lg: "18px"
xl: "20px"

```

Vous pourriez demander pourquoi il y a quatre valeurs de `fontSize` sous forme de tableau à l'intérieur des accolades ?

Les `{}` sont utilisés pour indiquer au parseur JSX d'interpréter l'expression à l'intérieur des `{}` comme du JavaScript. Ici, `{}` est utilisé pour passer un tableau pour la valeur de `fontSize`. Ce tableau est un raccourci pour les requêtes média dans Chakra UI.

Les valeurs sont passées dans un tableau pour rendre le texte réactif et changer la taille de la police en fonction des appareils, c'est-à-dire que le titre sera plus grand sur le bureau. 

Chaque index du tableau correspond à un point d'arrêt spécifique et à la valeur de la propriété. Cela signifie que `font-size` change en fonction du point d'arrêt. Vous pouvez en lire plus à ce sujet [ici](https://chakra-ui.com/docs/features/responsive-styles).

```javascript
const breakpoints = {
  sm: "30em",
  md: "48em",
  lg: "62em",
  xl: "80em",
}
```

Il suit l'approche "mobile-first", donc la première valeur est pour les petits appareils, et la dernière valeur est pour les appareils de bureau.

Le code ci-dessus générera du CSS comme ceci :

```css
.css-px6f4t {
 text-align:center;
 -webkit-text-decoration:underline;
 text-decoration:underline;
 font-size:2.25rem;
 color:#702459;
 font-weight:600;
 margin-bottom:1rem;
}
@media screen and (min-width:30em) {
 .css-px6f4t {
  font-size:2.25rem;
 }
}
@media screen and (min-width:48em) {
 .css-px6f4t {
  font-size:3rem;
 }
}
@media screen and (min-width:62em) {
 .css-px6f4t {
  font-size:3rem;
 }
}

```

Voici la différence côte à côte de la taille du titre telle que vue dans [Polypane](https://polypane.app/).

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-61.png)
_Polypane_

## Comment récupérer des données depuis l'API Pexels

Vous avez généré la clé API, alors écrivons le code pour récupérer les données de l'API. Nous allons créer un fichier séparé et définir les fonctions pour récupérer les données à l'intérieur.

Dans le répertoire racine de votre projet, créez un dossier nommé `lib`. À l'intérieur, créez un fichier nommé `api.js`.

Exécutez la commande suivante dans le terminal :

```bash
mkdir lib
cd lib
touch api.js
```

Voici l'URL de base de l'API Pexels pour les photos : [https://api.pexels.com/v1](https://api.pexels.com/v1/).

L'API Pexels a trois points de terminaison :

* `/curated` pour recevoir des photos en temps réel sélectionnées par l'équipe Pexels.
* `/search` pour rechercher des photos en fonction d'une requête.
* `/photos/:id` pour obtenir une seule photo à partir de son identifiant.

Nous utiliserons le point de terminaison `/curated` pour afficher les photos sélectionnées par l'équipe Pexels sur la page d'accueil de l'application.

Ajoutez le code suivant à `api.js` :

```javascript
const API_KEY = process.env.NEXT_PUBLIC_PEXELS_API_KEY;

export const getCuratedPhotos = async () => {
  const res = await fetch(
    `https://api.pexels.com/v1/curated?page=11&per_page=18`,
    {
      headers: {
        Authorization: API_KEY,
      },
    }
  );
  const responseJson = await res.json();
  return responseJson.photos;
};

```

Discutons du code ci-dessus :

* Nous commençons par créer une variable nommée `API_KEY` qui accède à la variable d'environnement `NEXT_PUBLIC_PEXELS_API_KEY` en utilisant `process.env.`
* Ensuite, nous créons une fonction asynchrone nommée `getCuratedPhotos()` qui utilise la méthode `fetch()` pour récupérer les données de l'API.
* Si vous regardez de plus près l'URL de récupération, vous remarquerez que nous avons ajouté `?page=11&per_page=18` après le point de terminaison `/curated`. Ce sont les paramètres optionnels que vous pouvez passer au point de terminaison `/curated` sous forme de [chaînes de requête](https://en.wikipedia.org/wiki/Query_string). Ici, `page=11` signifie envoyer la 11ème page, et `per_page=18` signifie envoyer 18 photos par page. 
* Vous pouvez également supprimer ces paramètres optionnels, auquel cas le point de terminaison de l'API vous enverra 15 images de la première page. Vous pouvez obtenir jusqu'à 80 photos en une seule requête.
* La clé API Pexels est passée dans le champ `Authorization` sous `headers`.
* `res.json()` analyse la réponse au format JSON. 
* `responseJson` contient des champs comme `page`, `per_page`, etc., qui ne sont pas utilisés par notre application. Seule la partie `photos` de la réponse est donc retournée, qui ressemble à ceci :

```javascript
[
  {
    id: 4905078,
    width: 7952,
    height: 5304,
    url: "https://www.pexels.com/photo/ocean-waves-under-blue-sky-4905078/",
    photographer: "Nick Bondarev",
    photographer_url: "https://www.pexels.com/@nick-bondarev",
    photographer_id: 2766954,
    src: {
      original:
        "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg",
      large2x:
        "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
      large:
        "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&h=650&w=940",
      medium:
        "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&h=350",
      small:
        "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&h=130",
      portrait:
        "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=1200&w=800",
      landscape:
        "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200",
      tiny:
        "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=200&w=280",
    },
    liked: false,
  },
];

```

Dans le champ `src`, nous avons plusieurs formats d'image différents à choisir. Dans ce tutoriel, nous utiliserons les images de type `portrait` sur notre page d'accueil. Vous êtes libre d'explorer d'autres formats également.

Au fur et à mesure que nous développons notre application, nous écrirons les fonctions pour rechercher une photo et obtenir une seule photo dans `api.js`. Pour l'instant, nous utiliserons cette fonction pour afficher une image sur notre page d'accueil ou page principale.

## Comment afficher des photos sur la page

Maintenant que nous avons créé la fonction pour récupérer les données, affichons-les sur notre page.

Tout d'abord, importez la fonction `getCuratedPhotos()` dans `index.js`.

```jsx
import Head from "next/head";
import { Box, Container, Text } from "@chakra-ui/react";
import {getCuratedPhotos} from "../lib/api"
 
```

Nous allons utiliser la fonction `getServerSideProps()` disponible dans Next.js et utiliser la fonction `getCuratedPhotos()` à l'intérieur pour récupérer les données de l'API Pexels et les injecter dans notre page. Vous pouvez en lire plus sur `getServerSideProps()` [ici](https://nextjs.org/docs/basic-features/data-fetching#getserversideprops-server-side-rendering).

Ajoutez le code suivant en bas de votre fichier `index.js` :

```jsx
export async function getServerSideProps() {
  const data = await getCuratedPhotos();
  return {
    props: {
      data,
    },
  };
}
```

La fonction asynchrone ci-dessus utilise `getCuratedPhotos()` pour récupérer les images de l'API Pexels et les stocke dans la variable `data`. Cette variable `data` est rendue disponible en tant que prop dans la propriété `props`.

Cette `data` est disponible en tant que prop, alors ajoutez-la en tant qu'argument dans la fonction du composant `Home`.

```jsx
export default function Home({data}) {
...
}
```

Redémarrez votre serveur de développement, et à l'intérieur de votre composant `Home`, `console.log` cette `data` :

```jsx
export default function Home({data}) {
  console.log(data)
  return (
 ...
 }

```

Rendez-vous sur [http://localhost:3000/](http://localhost:3000/) et ouvrez la console en appuyant sur `CTRL + Shift + J` dans Chrome ou `CTRL + Shift + K` dans Firefox.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-73.png)
_console.log(data)_

Supprimez le `console.log` et ajoutez le code suivant en haut de votre fichier `index.js` pour importer le hook `useState()` de `react`.

```jsx
import React, { useState } from "react";

```

Nous allons stocker les données de l'API Pexels à l'intérieur d'un état nommé `photos`. Ajoutez le code suivant avant l'instruction return :

```jsx
const [photos, setPhotos] = useState(data);
```

Pour afficher les images, parcourez le tableau `photos` et passez `src.original` dans l'attribut `src` de l'élément `img`. 

Ajoutez le code suivant après le composant `Container` :

```jsx
{
  photos.map((pic) => (
    <img src={pic.src.original} width="500" height="500" />
  ))
}

```

Votre application ressemblera maintenant à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-74.png)
_Affichage des images en utilisant l'élément img_

Outre le fait que les images ne sont pas correctement dimensionnées, il y a un autre problème avec l'utilisation de `<img>` pour afficher les images.

Rendez-vous sur [http://localhost:3000/](http://localhost:3000/) et ouvrez les **Outils de développement**, puis l'onglet **Réseau** (**Ctrl+ Shift + E** dans Firefox et **Ctrl + Shift + J** dans Chrome). Cela ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-75.png)
_Onglet Réseau_

Maintenant, rechargez votre page. Vous verrez que l'onglet **Réseau** vide est maintenant rempli de données.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-76.png)
_Requête unique_

Comme vous pouvez le voir dans l'image ci-dessus, le fichier demandé a une taille de plus de 11 Mo, et cela pour un seul fichier ou image. Les tailles peuvent varier de 10 à 100 Mo ou plus en fonction de la qualité de l'image.

Imaginez que vous avez 80 images sur la page d'accueil de votre application. Est-il judicieux de transférer environ 800 Mo de fichiers chaque fois que quelqu'un visite votre galerie ou votre site web ? **Non.**

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-77.png)
_Multiples requêtes_

C'est pourquoi aujourd'hui, la plupart des images sur le web sont servies au format [WebP](https://en.wikipedia.org/wiki/WebP). Ce format réduit considérablement la taille de l'image, et vous pouvez à peine détecter une différence visuelle. 

Nous devons donc changer le format de l'image en `webp`, mais la question est, comment ? Doit-on le faire manuellement ? Si oui, ne serait-ce pas chronophage et fastidieux ?

**Non, vous n'avez pas besoin de le faire manuellement.** 

[Next.js version 10](https://nextjs.org/blog/next-10) est livré avec un support intégré pour l'optimisation des images en utilisant le composant **Image**. Vous pouvez en lire plus sur cette mise à jour [ici](https://nextjs.org/blog/next-10#built-in-image-component-and-automatic-image-optimization).

Remplaçons donc l'élément `img` par le composant `Image` de Next.js. Tout d'abord, importez ce composant à l'intérieur de votre `index.js` comme ceci :

```jsx
import Image from "next/image";

```

Mais attendez, avant d'utiliser ce composant dans notre code, nous devons indiquer à Next.js que nos images proviennent d'une ressource externe, comme Pexels.

Arrêtez votre serveur de développement et créez un fichier `next.config.js` en exécutant la commande suivante :

```bash
touch next.config.js
```

Ajoutez le code suivant à `next.config.js` :

```javascript
module.exports = {
  images: {
    domains: ["images.pexels.com"],
  },
};

```

Et c'est tout. Il existe d'autres configurations comme `path`, `imageSizes`, `deviceSizes`, etc., que vous pouvez ajouter dans le champ `images`. Mais dans ce tutoriel, nous les laisserons par défaut. Vous pouvez en lire plus sur la configuration [ici](https://nextjs.org/docs/basic-features/image-optimization).

Remplacez `img` par le composant `Image` et passez les props, comme indiqué ci-dessous : 

```jsx
{
  photos.map((pic) => (
    <Image
      src={pic.src.portrait}
      height={600}
      width={400}
      alt={pic.url}
    />
  ))
}

```

Comme discuté ci-dessus, l'API Pexels fournit différents formats ou tailles de la même image, comme `portrait`, `landscape`, `tiny`, etc., sous le champ `src`. 

Ce tutoriel utilise les images `portrait` sur la page d'accueil, mais vous êtes libre d'explorer d'autres tailles. 

```javascript
src: {
    original: "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg",
    large2x: "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    large: "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&h=650&w=940",
    medium: "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&h=350",
    small: "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&h=130",
    portrait: "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=1200&w=800",
    landscape: "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200",
    tiny: "https://images.pexels.com/photos/4905078/pexels-photo-4905078.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=200&w=280",
  }

```

Comme vous pouvez le voir dans l'exemple de champ `src` ci-dessus, le format `portrait` de l'image a une largeur de **800** et une hauteur de **1200**. Mais il est trop grand pour être affiché sur la page web, alors nous allons le réduire en divisant par 2. Donc `600` et `400` sont passés pour la hauteur et la largeur du composant `Image`.

Redémarrez votre serveur de développement et rendez-vous sur [http://localhost:3000/](http://localhost:3000/). Vous verrez que l'application elle-même a exactement le même aspect. Mais cette fois, si vous ouvrez l'onglet **Réseau** et rechargez la page, vous verrez quelque chose de vraiment magique.

Vos images sont maintenant au format `webp`, et leurs tailles ont été réduites.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-121.png)
_Onglet Réseau_

Le composant Image de Next.js a également ajouté le [chargement paresseux](https://en.wikipedia.org/wiki/Lazy_loading) aux images. Voici un exemple pour expliquer comment et pourquoi vous devriez utiliser le chargement paresseux si vous n'êtes pas familier avec celui-ci.

Même si les images sont maintenant au format `webp`, est-il nécessaire de charger toutes les images chaque fois que quelqu'un visite votre site web ? Et si le visiteur vient et repart sans faire défiler, est-il judicieux de charger les images en bas de la page ?

Il n'est pas nécessaire de charger les images qu'un utilisateur ou un visiteur ne va pas voir dans la plupart des situations.

Et c'est là que le **chargement paresseux** vient sauver la journée. Il retarde les requêtes des images jusqu'à ce qu'elles soient nécessaires ou, dans cette situation, lorsque les images apparaissent à l'écran. Cela aide considérablement à réduire le poids initial de la page et augmente les performances du site web.

Si vous vous rendez sur [http://localhost:3000/](http://localhost:3000/) et faites défiler toutes les images, vous verrez que les images qui ne sont pas dans la fenêtre d'affichage ne sont pas chargées initialement. Mais à mesure que vous faites défiler vers le bas, elles sont transférées et chargées. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/ezgif.com-video-to-gif-1.gif)
_Chargement paresseux_

Par défaut, la prop `layout` du composant `Image` a la valeur `intrinsic`, ce qui signifie que l'image redimensionnera les dimensions pour les viewports plus petits mais maintiendra les dimensions originales pour les viewports plus grands.

Il existe de nombreuses props que vous pouvez passer au composant `Image` pour modifier davantage ce composant. Vous pouvez en lire plus à ce sujet [ici](https://nextjs.org/docs/api-reference/next/image).

## Comment styliser les images avec Chakra UI

Pour styliser les images, nous allons utiliser le composant `Wrap` de Chakra UI. 

[Wrap](https://chakra-ui.com/docs/layout/wrap) est un composant de mise en page qui ajoute un espace défini entre ses enfants ou images dans ce scénario. Il 'enveloppe' ses enfants automatiquement s'il n'y a pas assez d'espace pour adapter un enfant.

Importez `Wrap` et `WrapItem` depuis Chakra UI.

```jsx
import { Box, Container, Text, Wrap, WrapItem } from "@chakra-ui/react";

```

`WrapItem` englobe les enfants individuels tandis que `Wrap` englobe tous les composants `WrapItem`.

Modifiez l'expression pour afficher les images comme ceci :

```jsx
<Wrap px="1rem" spacing={4} justify="center">
  {photos.map((pic) => (
    <Image src={pic.src.portrait} height={600} width={400} alt={pic.url} />
  ))}
</Wrap>
```

Voici ce qui se passe dans le code ci-dessus :

* `px="1rem"` est la propriété raccourcie pour `padding-left` et `padding-right`. Cela ajoute un remplissage horizontal de 1 rem.
* `spacing={4}` applique un espacement entre chaque enfant. Cela sera visible une fois que chaque image est enveloppée avec `WrapItem`.
* `justify="center"` justifie les images au centre. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-80.png)
_Wrap_

Maintenant, enveloppez chaque image avec `WrapItem`. Ajoutez le code suivant à l'intérieur de l'expression JavaScript :

```jsx
<Wrap px="1rem" spacing={4} justify="center">
  {photos.map((pic) => (
    <WrapItem
      key={pic.id}
      boxShadow="base"
      rounded="20px"
      overflow="hidden"
      bg="white"
      lineHeight="0"
      _hover={{ boxShadow: "dark-lg" }}
    >
      <Image src={pic.src.portrait} height={600} width={400} alt={pic.url} />
    </WrapItem>
  ))}
</Wrap>

```

Discutons des props passées à `WrapItem` une par une :

* `key={pic.id}` donne à chaque image une clé unique afin que React puisse différencier les enfants ou les images.
* `boxShadow="base"` ajoute une ombre à `WrapItem`.
* `rounded="20px"` ajoute un `border-radius` de 20px.
* `overflow="hidden"` s'assure que l'image ne déborde pas de `WrapItem` et est vue arrondie. 
* `bg="white"` ajoute un fond blanc à `WrapItem`.
* `lineHeight="0"` définit la propriété `line-height` à zéro.
* `_hover={{ boxShadow: "dark-lg" }}` change le `boxShadow` lorsque vous survolez l'image. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/ezgif.com-video-to-gif-2-.gif)
_GIF_

Vous verrez que `spacing={4}` a également pris effet depuis que nous avons ajouté `WrapItem` aux images.  

## Comment ajouter une fonctionnalité de recherche à la galerie

L'étape suivante consiste à ajouter une fonctionnalité permettant aux utilisateurs de rechercher des images et de leur montrer ces images. Pour cela, nous allons utiliser le point de terminaison `/search` dans l'API Pexels.

Dans `lib/api.js`, créez une nouvelle fonction `getQueryPhotos()` pour rechercher des images en fonction de l'entrée de recherche de l'utilisateur.

```javascript
export const getQueryPhotos = async (query) => {
  const res = await fetch(`https://api.pexels.com/v1/search?query=${query}`, {
    headers: {
      Authorization: API_KEY,
    },
  });
  const responseJson = await res.json();
  return responseJson.photos;
};

```

La fonction ci-dessus `getQueryPhotos()` est similaire à `getCuratedPhotos` mais ici nous avons ajouté un paramètre `query` à la fonction et modifié le point de terminaison de l'API pour inclure cette `query`.

```javascript
`https://api.pexels.com/v1/search?query=${query}`
```

Importez la fonction `getQueryPhotos()` dans `index.js`.

```javascript
import { getCuratedPhotos, getQueryPhotos } from "../lib/api";

```

Maintenant, nous allons créer un formulaire pour prendre l'entrée de l'utilisateur et rechercher la même chose. 

Nous allons importer et utiliser `Input`, `IconButton`, `InputRightElement`, et `InputGroup` de Chakra UI pour créer ce formulaire.

Modifiez l'import de Chakra UI comme ceci et ajoutez un import pour `SearchIcon` :

```jsx
import {
  Box,
  Container,
  Text,
  Wrap,
  WrapItem,
  Input,
  IconButton,
  InputRightElement,
  InputGroup,
} from "@chakra-ui/react";
import { SearchIcon } from "@chakra-ui/icons";

```

Ajoutez le code suivant pour le formulaire d'entrée à l'intérieur du composant `Container` dans le fichier `index.js` :

```jsx
<InputGroup pb="1rem">
  <Input placeholder="Rechercher une pomme" variant="ghost" />

  <InputRightElement
    children={
      <IconButton
        aria-label="Rechercher"
        icon={<SearchIcon />}
        bg="pink.400"
        color="white"
      />
    }
  />
</InputGroup>

```

Voici ce que nous faisons.

* `InputGroup` est utilisé pour regrouper les composants `Input` et `InputRightElement`. Ici, `pb` est le raccourci pour `padding-bottom`.
* `Input` est le champ de saisie où les utilisateurs taperont leurs requêtes. Il a un placeholder "Rechercher une pomme".
* `InputRightElement` est utilisé pour ajouter un élément à droite du composant `Input`. Un [bouton d'icône](https://chakra-ui.com/docs/form/icon-button) avec l'icône de recherche est passé à la prop `children` de `InputRightElement`.
* `IconButton` est un composant dans Chakra UI qui est utile lorsque vous voulez une icône comme bouton. L'icône à rendre est passée à l'intérieur de la prop `icon`.

Voici à quoi ressemblera le champ de saisie.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-89.png)
_Champ de saisie_

Ce formulaire ne fait encore rien. Changeons cela. 

Définissez un nouvel état nommé `query` pour stocker les entrées d'un utilisateur :

```jsx
export default function Home({ data }) {
  const [photos, setPhotos] = useState(data);
  const [query, setQuery] = useState("");

...
}
```

Modifiez le composant `Input` pour créer une liaison bidirectionnelle entre le champ de saisie et l'état `query` en utilisant la méthode `value` et l'événement `onChange` :

```jsx
<Input
  placeholder="Rechercher une pomme"
  variant="ghost"
  value={query}
  onChange={(e) => setQuery(e.target.value)}
/>
```

Maintenant, créez une fonction nommée `handleSubmit()` pour gérer l'événement de clic de l'icône de recherche. Pour l'instant, nous allons simplement `console.log` la requête de saisie et effacer le champ ensuite.

```jsx
export default function Home({ data }) {
  const [photos, setPhotos] = useState(data);
  const [query, setQuery] = useState("");

  const handleSubmit = async (e) => {
    await e.preventDefault();
    await console.log(query);
    await setQuery("");
  };
  
...
}
```

Ajoutez cette fonction à l'événement `onClick` de `IconButton` :

```jsx
<InputRightElement
  children={
    <IconButton
      aria-label="Rechercher"
      icon={<SearchIcon />}
      onClick={handleSubmit}
      bg="pink.400"
      color="white"
    />
  }
/>

```

Rendez-vous sur [http://localhost:3000/](http://localhost:3000/) et tapez quelque chose dans le champ de saisie et cliquez sur le bouton de recherche.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-90.png)
_console.log(query)_

Mais ce formulaire manque encore quelque chose : si vous essayez de rechercher quelque chose en appuyant sur **Entrée** au lieu du bouton de recherche, il rechargera la page, et la requête ne sera pas enregistrée.

Pour corriger cela, enveloppez le `InputGroup` avec l'élément `form` et passez la fonction `handleSubmit` à l'événement `onSubmit` comme ceci :

```jsx
<form onSubmit={handleSubmit}>
  <InputGroup pb="1rem">
    <Input
      placeholder="Rechercher une pomme"
      variant="ghost"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
    />

    <InputRightElement
      children={
        <IconButton
          aria-label="Rechercher"
          icon={<SearchIcon />}
          onClick={handleSubmit}
          bg="pink.400"
          color="white"
        />
      }
    />
  </InputGroup>
</form>

```

Vous remarquerez que l'appui sur **Entrée** fonctionnera maintenant.

Maintenant, mettez à jour la fonction `handleSubmit` comme ceci pour récupérer les images en fonction de la requête de l'utilisateur :

```jsx
const handleSubmit = async (e) => {
  await e.preventDefault();
  const res = await getQueryPhotos(query);
  await setPhotos(res);
  await setQuery("");
}
```

La fonction ci-dessus passe la variable `query` à la fonction `getQueryPhotos()` et les données retournées par la fonction remplacent la valeur précédente dans la variable `photos` en utilisant `setPhotos(res)`.

Et c'est fait ! Vous pouvez maintenant rechercher des images dans votre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/ezgif.com-video-to-gif-2.gif)
_Recherche de pomme_

Il manque encore quelque chose. Qu'est-ce que c'est ?

Que se passe-t-il si l'utilisateur essaie de rechercher sans aucune requête, comme avec des **chaînes vides** ? Le code actuel essaiera toujours de faire une requête en utilisant `""` et nous rencontrerons l'erreur suivante.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-91.png)

Pour gérer ce problème, nous allons utiliser `Toast` de Chakra UI.

Importez `useToast` de Chakra UI :

```jsx
import {
  Box,
  Container,
  Text,
  Wrap,
  WrapItem,
  Input,
  IconButton,
  InputRightElement,
  InputGroup,
  useToast
} from "@chakra-ui/react";

```

Ajoutez le code suivant juste en dessous de l'endroit où vous avez défini les états pour initialiser Toast.

```jsx
export default function Home({ data }) {
  const [photos, setPhotos] = useState(data);
  const [query, setQuery] = useState("");
  const toast = useToast();

...
}
```

Modifiez la fonction `handleSubmit()` comme ceci :

```jsx
const handleSubmit = async (e) => {
  await e.preventDefault();
  if (query == "") {
    toast({
      title: "Erreur.",
      description: "Recherche vide",
      status: "error",
      duration: 9000,
      isClosable: true,
      position: "top",
    });
  } else {
    const res = await getQueryPhotos(query);
    await setPhotos(res);
    await setQuery("");
  }
};

```

Dans le code ci-dessus, nous vérifions si la `query` est vide ou non avec une simple instruction `if/else`. Et si elle est vide, alors nous affichons un toast d'erreur avec le texte `Recherche vide`.

Essayez d'appuyer sur **Entrée** sans taper quoi que ce soit dans le champ de saisie. Vous verrez un toast comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-92.png)
_Toast de recherche vide_

## Comment ajouter des routes dynamiques aux images

Nous allons créer une route dynamique pour chaque image afin que les utilisateurs puissent cliquer sur les images pour obtenir plus d'informations à leur sujet.

Next.js possède une fonctionnalité très intéressante où vous pouvez créer une route dynamique en ajoutant des crochets à une page (`[param]`), où `param` peut être des slugs d'URL, des URL conviviales, un ID, etc.

Ici, le `param` est `id`, puisque pour obtenir une photo spécifique de l'API Pexels, vous devez fournir son `id`. 

Exécutez les commandes suivantes dans le répertoire racine de votre projet pour créer `[id].js` dans le répertoire `photos` sous pages. 

```bash
mkdir pages/photos
cd pages/photos
touch [id].js
```

Importez `Link` de `next/link` dans `index.js`. `Link` aide aux transitions côté client entre les routes. Vous pouvez en lire plus sur `Link` [ici](https://nextjs.org/docs/api-reference/next/link).

```javascript
import Link from "next/link"

```

Ajoutez ce `Link` à chaque image comme ceci :

```jsx
<Link href={`/photos/${pic.id}`}>
  <a>
    <Image src={pic.src.portrait} height={600} width={400} alt={pic.url} />
  </a>
</Link>

```

Rendez-vous sur votre application et essayez de cliquer sur n'importe quelle image. Elle affichera une erreur puisque nous avons créé `photos/[id].js` mais n'avons pas ajouté de code à l'intérieur. 

Mais si vous regardez l'URL de cette page, elle sera quelque chose comme ceci :

```
http://localhost:3000/photos/2977079
```

Nous allons maintenant créer une troisième fonction nommée `getPhotoById()` dans `lib/api.js` pour obtenir une photo spécifique en fonction de son identifiant.

Ajoutez le code suivant à `api.js` :

```javascript
export const getPhotoById = async (id) => {
  const res = await fetch(`https://api.pexels.com/v1/photos/${id}`, {
    headers: {
      Authorization: API_KEY,
    },
  });
  const responseJson = await res.json();
  return responseJson;
};
```

Le code ci-dessus utilise le point de terminaison `/photos` pour obtenir une seule image de l'API Pexels. Vous remarquerez que contrairement à `getCuratedPhotos` et `getQueryPhotos`, `getPhotoById` retourne `responseJson` et non `responseJson.photos`.

Ajoutez le code suivant à `photos/[id].js` :

```jsx
import { getPhotoById } from "../../lib/api";
import {
  Box,
  Divider,
  Center,
  Text,
  Flex,
  Spacer,
  Button,
} from "@chakra-ui/react";
import Image from "next/image";
import Head from "next/head";
import Link from "next/link";
import { InfoIcon, AtSignIcon } from "@chakra-ui/icons";

export default function Photos() {
  
    return (
      <Box p="2rem" bg="gray.200" minH="100vh">
        <Head>
          <title>Image</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>
     
      </Box>
    )
  }


```

Nous avons ajouté une couleur de fond gris clair en utilisant la prop `bg` et le composant `Box`. Pour gagner du temps, nous avons importé tous les composants et icônes au préalable.

Créez une fonction `getServerSideProps()` dans `[id].js` pour récupérer les données de l'API Pexels.

```jsx
export async function getServerSideProps({ params }) {
  const pic = await getPhotoById(params.id);
  return {
    props: {
      pic,
    },
  };
}

```

Redémarrez votre serveur de développement.

Vous pourriez demander comment `getServerSideProps()` obtient l'`id` de l'image à partir de l'argument `params` ? 

Puisque cette page utilise une route dynamique, `params` contient les paramètres de route. Ici, le nom de la page est `[id].js`, donc `params` ressemblera à `{ id: ... }`. 

Vous pouvez essayer `console.log(params)` – cela ressemblera à quelque chose comme ceci.

```javascript
{ id: '4956064' }
```

Passez cette prop `pic` à la fonction du composant `Photos` en tant qu'argument.

```jsx
export default function Photos({ pic }) {
...
}

```

Ajoutez le code suivant au composant `Box` :

```jsx
<Box p="2rem" bg="gray.200" minH="100vh">
  <Head>
    <title> Image: {pic.id}</title>
    <link rel="icon" href="/favicon.ico" />
  </Head>

  <Flex px="1rem" justify="center" align="center">
    <Text
      letterSpacing="wide"
      textDecoration="underline"
      as="h2"
      fontWeight="semibold"
      fontSize="xl"
      as="a"
      target="_blank"
      href={pic.photographer_url}
    >
      <AtSignIcon />
      {pic.photographer}
    </Text>
    <Spacer />
    <Box as="a" target="_blank" href={pic.url}>
      <InfoIcon focusable="true" boxSize="2rem" color="red.500" />{" 