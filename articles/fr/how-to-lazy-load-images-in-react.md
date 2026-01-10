---
title: Comment charger paresseusement des images dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-31T22:24:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-lazy-load-images-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/How-to-lazy-load-images-in-React-1.png
tags:
- name: React
  slug: react
- name: web performance
  slug: web-performance
seo_title: Comment charger paresseusement des images dans React
seo_desc: 'By Victor Eke

  Optimizing the assets you use on your websites – like lazy loading images – is one
  of the most effective ways to improve web performance.

  Doing this helps you make sure that your websites are fast, they have great SEO,
  and it helps enha...'
---

Par Victor Eke

Optimiser les ressources que vous utilisez sur vos sites web – comme le chargement paresseux des images – est l'une des méthodes les plus efficaces pour améliorer les performances web.

Cela vous aide à vous assurer que vos sites web sont rapides, qu'ils ont un excellent [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization), et cela contribue à améliorer l'expérience utilisateur.

Dans cet article, vous apprendrez comment charger paresseusement des images dans une application React. Nous parlerons des avantages de le faire, et comment l'implémenter dans votre code.

Mais avant de commencer, qu'est-ce que le chargement paresseux, et comment fonctionne-t-il ?

## Qu'est-ce que le Chargement Paresseux ?

> Le chargement paresseux est une stratégie qui retarde le chargement de certaines ressources (par exemple, des images) jusqu'à ce qu'elles soient nécessaires pour l'utilisateur en fonction de l'activité et du modèle de navigation de l'utilisateur. Typiquement, ces ressources ne sont chargées que lorsqu'elles sont défilées dans la vue. <a href="https://developer.mozilla.org/en-US/docs/Glossary/Lazy_load">(Source : MDN Docs)</a>

Vous pouvez voir un excellent exemple de cela sur [Unsplash](http://unsplash.com) lorsque nous faisons défiler la liste des images. Initialement, nous voyons un espace réservé d'image floue de faible qualité [LQIP](https://web.dev/image-component/), et lorsque nous faisons défiler dans la vue, l'image entière est complètement chargée sur la page.

![unsplash-lazy-load-image-illustration-](https://www.freecodecamp.org/news/content/images/2022/08/unsplash-lazy-load-image-illustration-.gif)

L'idée derrière ce processus est de reporter le chargement des images en dehors de la fenêtre d'affichage pour réduire l'utilisation de la bande passante, améliorer l'expérience utilisateur et accélérer le chargement de la page.

Le chargement paresseux d'une `image/iframe` aujourd'hui est aussi simple que d'ajouter l'attribut `loading="lazy"` à l'intérieur de l'élément img/iframe, comme ceci :

```html
<img src="image.jpg" alt="Image Alt" loading="lazy" />
<iframe src="iframe" loading="lazy"></iframe>
```

Et cela fonctionne sans aucune configuration supplémentaire.

Malheureusement, le chargement paresseux des images de cette manière n'est pas largement supporté dans tous les navigateurs selon [caniuse.com](https://caniuse.com/?search=lazyloading). De plus, pour des navigateurs comme Firefox, l'attribut `loading="lazy"` ne fonctionne pas dans un élément `iframe`. Dans ces cas, vous devrez l'utiliser/combiner avec d'autres bibliothèques ou outils.

## Commencer avec le Chargement Paresseux
Cet article utilisera une bibliothèque JavaScript appelée [React Lazy Load Image Component](https://www.npmjs.com/package/react-lazy-load-image-component).
Cette bibliothèque populaire fournit des capacités de rendu d'images et des effets que vous pouvez implémenter rapidement et facilement dans vos propres applications React.

Le code pour cette démonstration est disponible sur [GitHub ici](https://github.com/evavic44/react-lazyload).

### Étape 1 – Installer React Lazy Load Image Component
La première chose que nous devons faire est d'installer la bibliothèque de composants d'image de chargement paresseux React en utilisant NPM :

```js
// Yarn
$ yarn add react-lazy-load-image-component
ou
// NPM
$ npm i --save react-lazy-load-image-component
```

### Étape 2 – Importer le composant
Nous allons simplement importer notre image et le composant de chargement paresseux. Mais vous pouvez utiliser une URL externe si vous le souhaitez. Dans mon cas, je l'importe en tant que composant depuis le répertoire des images.

```js
import Image from "../images/bird.jpg";
import { LazyLoadImage } from "react-lazy-load-image-component";
```

### Étape 3 – Déclarer l'image
Pour commencer à l'utiliser, au lieu de déclarer vos images avec une balise `img`, remplacez cela par `LazyLoadImage` et déclarez l'image avec un attribut `src` comme vous le feriez normalement.

Voici à quoi cela ressemble en code :

```js
import React from "react";
import Image from "../images/bird.jpg";
import { LazyLoadImage } from "react-lazy-load-image-component";

export default function App() {
  return (
    <div>
      <LazyLoadImage src={Image}
        width={600} height={400}
        alt="Image Alt"
      />
     </div>
  );
}
```

De plus, nous avons explicitement défini la largeur et la hauteur de l'image. Cela aide à éviter des problèmes comme le [décalage cumulatif de mise en page (CLS)](https://web.dev/cls/).

Pour voir les effets du composant, ouvrez l'onglet réseau dans vos outils de développement en utilisant <kbd>Ctrl + Maj + J</kbd> sur Windows et Linux, et <kbd>Cmd + Opt + J</kbd> sur Mac. Ensuite, réglez la limitation à un réseau plus lent (3G), désactivez le cache et actualisez la page.

<br>

![network-tab](https://www.freecodecamp.org/news/content/images/2022/08/network-tab.png)

Voici le résultat :

<br>

![default](https://www.freecodecamp.org/news/content/images/2022/08/default.gif)

Par défaut, vous pouvez voir que l'image n'a pas été chargée à l'écran car elle n'est pas visible dans la fenêtre d'affichage. Une fois que nous commençons à faire défiler et que l'image est dans la vue, le chargement paresseux est désactivé, et nous pouvons maintenant voir l'image.

[Démonstration en direct](https://react-lazyload.vercel.app/default)

### Étape 4 – Ajouter une image de remplacement
Alternativement, nous pouvons prévisualiser une image de faible résolution d'abord tout en attendant que l'image principale se charge. Cela aide à remplir la zone de l'image pour que les utilisateurs sachent qu'une image est en cours de chargement. Nous appelons cette image de remplacement un espace réservé d'image de faible qualité (LQIP).

Faire cela non seulement a l'air bien, mais donne également à l'utilisateur une idée de ce à quoi ressemble l'image réelle.

Pour obtenir une taille d'image plus petite, j'aime utiliser [squoosh.app](https://squoosh.app/). Importez l'image et expérimentez avec la résolution et la qualité jusqu'à ce que vous soyez satisfait de la taille.

D'autres outils d'image que vous pouvez utiliser incluent :

- [Photoshop](https://www.adobe.com/products/photoshop.html)
- [Responsive Breakpoints](https://responsivebreakpoints.com)

<br>

![rasterized-image](https://www.freecodecamp.org/news/content/images/2022/08/rasterized.png)

Initialement, notre image était de `288KB`, mais nous l'avons compressée avec succès en une version basse résolution de `2.41KB`. Pour utiliser l'image de remplacement, ajoutez un attribut `PlaceholderSrc` à l'image avec la valeur de l'image.

```js
import Image from "../images/bird.jpg";
import PlaceholderImage from "../images/placeholder.jpg";

<LazyLoadImage src={Image}
    width={600} height={400}
    PlaceholderSrc={PlaceholderImage}
    alt="Image Alt"
/>
```

<br>

![React-lazyload-LQIP-](https://www.freecodecamp.org/news/content/images/2022/08/React-lazyload---LQIP-.gif)

Vous pouvez voir comment il a chargé l'image de remplacement initialement, et après avoir terminé le chargement, elle a été remplacée par l'image principale.

[Démonstration en direct](https://react-lazyload.vercel.app/placeholder)

### Étape 5 – Ajouter un flou à l'image
LazyLoadImage fournit également un plugin pour flouter une image initialement avant qu'elle ne se charge et supprime le flou après que l'image soit complètement chargée.

Combiner cela avec l'image de remplacement améliorera l'apparence globale et fournira une meilleure sortie.

Afin d'utiliser l'effet de flou, nous devons importer le fichier CSS qui le contrôle :

```js
import Image from "../images/bird.jpg";
import PlaceholderImage from "../images/placeholder.jpg";
import { LazyLoadImage } from 'react-lazy-load-image-component';
import 'react-lazy-load-image-component/src/effects/blur.css';

<LazyLoadImage src={Image}
    width={600} height={400}
    PlaceholderSrc={PlaceholderImage}
    effect="blur"
/>
```

<br>

![React-lazyload---Blur](https://www.freecodecamp.org/news/content/images/2022/08/React-lazyload---Blur.gif)


[Démonstration en direct](https://react-lazyload.vercel.app/blur)

## Pourquoi Devriez-Vous Charger Paresseusement Vos Images ?
Vous vous demandez peut-être pourquoi vous devriez vous donner la peine de charger paresseusement les images hors écran dans votre application web. Est-ce que cela en vaut la peine, et pourquoi devriez-vous vous soucier des points partagés dans cet article ?

Voici une liste de raisons :

### 1. Le Chargement Paresseux Économise des Données et de la Bande Passante
Puisque les images en dehors de la fenêtre d'affichage ne sont pas téléchargées immédiatement, le chargement paresseux économise l'utilisation supplémentaire de la bande passante. Cela est bon pour les performances, surtout pour les utilisateurs mobiles.

### 2. Le Chargement Paresseux Réduit le Coût d'un CDN
Les services de contenu multimédia comme [Cloudinary](https://cloudinary.com) ou [Imagekit](imagekit.io) offrent des plans payants pour le stockage multimédia. Le chargement paresseux des images garantit que seules les images demandées depuis le CDN sont chargées, réduisant ainsi les coûts du serveur.

### 3. Le Chargement Paresseux Améliore le SEO
La vitesse de la page est un facteur critique qui influence le SEO (et rend les moteurs de recherche plus susceptibles de recommander votre page). Parce que le temps de chargement de votre page est très faible, les moteurs de recherche aimeront votre site.

## Conclusion
Optimiser les images est une bonne compétence que je crois que chaque développeur web devrait cultiver. Cela crée une meilleure expérience pour les utilisateurs, surtout ceux sur des appareils mobiles.

Voici le [fichier de code pour cet article sur GitHub](https://github.com/Evavic44/react-lazyload).

C'est tout pour cet article. Si vous avez lu jusqu'à ce point, alors je suis sûr que vous aimerez mes autres contenus. Consultez [mon blog](https://eke.hashnode.dev) ou suivez-moi sur Twitter [@victorekea](https://twitter.com/victorekea) pour plus.

## Ressources
- [React Lazy Load Image Component](https://www.npmjs.com/package/react-lazy-load-image-component)
- [Démonstration](https://react-lazyload.vercel.app)