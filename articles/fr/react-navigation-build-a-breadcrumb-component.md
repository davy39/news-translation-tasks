---
title: React Navigation – Comment créer un composant Breadcrumb
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2024-03-25T22:33:05.000Z'
originalURL: https://freecodecamp.org/news/react-navigation-build-a-breadcrumb-component
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Breadcrumb-article-cover.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react-navigation
  slug: react-navigation
- name: routing
  slug: routing
- name: tailwind
  slug: tailwind
seo_title: React Navigation – Comment créer un composant Breadcrumb
seo_desc: 'I know what you''re thinking – but despite the article title and cover
  image, this article isn''t about bread or even pastries. Instead, it looks at a
  commonly used component in web applications for navigation called the breadcrumb
  component.

  Here, we''...'
---

Je sais ce que vous pensez – mais malgré le titre de l'article et l'image de couverture, cet article ne parle pas de pain ni même de pâtisseries. Au lieu de cela, il examine un composant couramment utilisé dans les applications web pour la navigation appelé le composant breadcrumb.

Ici, nous allons démystifier les chemins de breadcrumb dans les applications React. Nous allons disséquer leurs types, et vous apprendrez comment les intégrer de manière transparente dans vos projets web pour une meilleure navigation utilisateur.

## Prérequis

* Fondamentaux de CSS et TailwindCSS
* Fondamentaux de ES6 JavaScript et React 
* Fondamentaux du Routing et de la bibliothèque React Router (consultez cet [article sur le routing](https://www.freecodecamp.org/news/improve-user-experience-in-react-by-animating-routes-using-framer-motion/) si vous n'êtes pas familier).

## Ce que nous allons couvrir:

1. [Comprendre les Breadcrumbs](#heading-comprendre-les-breadcrumbs)
2. [Types de Navigation Breadcrumb](#heading-types-de-navigation-breadcrumb)
3. [Comment Construire le Composant Breadcrumb dans React](#heading-comment-construire-le-composant-breadcrumb-dans-react)
4. [Comment Créer la Structure du Composant Breadcrumb](#heading-comment-creer-la-structure-du-composant-breadcrumb)  
– [Breadcrumbs Basés sur l'Emplacement](#heading-breadcrumbs-bases-sur-lemplacement)  
– [Breadcrumbs Basés sur le Chemin](#heading-breadcrumbs-bases-sur-le-chemin)  
– [Breadcrumbs Basés sur les Attributs](#heading-breadcrumbs-bases-sur-les-attributs)
5. [Meilleures Pratiques pour les Breadcrumbs dans React](#heading-meilleures-pratiques-pour-les-breadcrumbs-dans-react)
6. [Conclusion](#heading-conclusion)

## Comprendre les Breadcrumbs

Avant de nous aventurer plus profondément dans les intrications des breadcrumbs, mettons la scène. Imaginez le conte classique de [Hansel et Gretel](https://en.wikipedia.org/wiki/Hansel_and_Gretel), où ils laissent une trace de miettes de pain pour retrouver leur chemin à travers la forêt dense.

Dans le domaine numérique, les breadcrumbs servent un but similaire, bien qu'avec une touche différente.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Hansel-And-Gretel-2.jpg)
_Hansel et Gretel_

Les breadcrumbs, dans le contexte de la navigation web, sont une série de liens hiérarchiques généralement affichés en haut d'une page web. Ces liens reflètent le chemin de l'utilisateur depuis la page d'accueil jusqu'à la page actuelle, lui permettant de retracer ses pas ou de naviguer vers des pages de niveau supérieur.

Ces aides à la navigation ont une histoire fascinante et un rôle crucial dans le guidage des utilisateurs à travers un espace numérique.

Un exemple typique de ce à quoi ressemble ce composant est montré ci-dessous:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Breadcrumb-example.png)
_Exemple de Breadcrumb: Page d'Accueil > Page des Produits > Page d'un Produit Unique (page actuelle)_

### Types de Navigation Breadcrumb

* **Breadcrumbs Basés sur l'Emplacement**: Comme des points de repère dans une forêt, les breadcrumbs basés sur l'emplacement montrent aux utilisateurs où ils se trouvent dans la hiérarchie du site web. Ils montrent la position de la page actuelle par rapport aux autres pages du site.
* **Breadcrumbs Basés sur le Chemin**: Comme retracer vos pas dans la forêt, les breadcrumbs basés sur le chemin affichent le parcours de l'utilisateur à travers le site web. Ils montrent la séquence des pages visitées, aidant les utilisateurs à comprendre comment ils sont arrivés à la page actuelle.
* **Breadcrumbs Basés sur les Attributs**: Ces breadcrumbs mettent en évidence des attributs ou caractéristiques spécifiques de la page actuelle. Ils offrent plus de contexte à la navigation de l'utilisateur, comme découvrir des caractéristiques uniques le long d'un sentier.

## Comment Construire le Composant Breadcrumb dans React

La première étape de cette section implique la création d'un environnement React. Avant de commencer, assurez-vous d'installer [Node.js](https://nodejs.org/en/download) sur votre ordinateur si ce n'est pas déjà fait.

### Comment Configurer un Environnement React

Après avoir installé Node.js, utilisez [Vite](https://vitejs.dev/guide/) (un outil de construction moderne pour les projets React) pour créer un nouveau projet React. Dans votre terminal local, exécutez la commande:

```bash
npm create vite@latest
```


Sélectionnez React comme framework et votre variante préférée.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Setting-up-a-react-environment-with-Vite.png)
_Configuration d'un environnement React avec Vite_

Pour installer les packages nécessaires, exécutez `npm install` et ouvrez-le dans votre IDE.

Enfin, effacez le code de base et démarrez votre serveur en utilisant la commande `npm run dev`.

Ce projet utilisera Tailwind pour le style. Pour le configurer, exécutez la commande suivante:

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Après cette commande, un fichier `tailwind.config.js` sera créé. Allez dans le fichier de configuration, supprimez son contenu, et collez ceci à la place:

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Ensuite, ouvrez votre fichier `index.css` et collez les configurations de style (de préférence en haut):

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Enfin, redémarrez votre serveur de développement pour avoir accès à Tailwind.

## Comment Créer la Structure du Composant Breadcrumb

Plutôt que de construire un seul composant breadcrumb, nous allons construire les trois types mentionnés ci-dessus afin que vous puissiez voir comment ils fonctionnent.

### Breadcrumbs Basés sur l'Emplacement

Ce type est le type de breadcrumb le plus basique qui implique de montrer toutes les routes facilement disponibles pour que l'utilisateur navigue.

Pour commencer, commencez par créer un fichier Breadcrumb et collez ces styles:

```jsx
import SlashImg from "./assets/slash.png";

export default function Breadcrumb() {
  return (
    <div className="bg-white ">
      <ul className=" flex border p-2 gap-6 text-xl text-[#2E4053] items-center">
        <li className=" cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md">
          Accueil
        </li>
        <img src={SlashImg} className="w-5 h-5 " alt="" />
        <li className=" cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md transition-all duration-300">
          Produits
        </li>
        <img src={SlashImg} className="w-5 h-5 " alt="" />
        <li className=" cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md transition-all duration-300">
          À propos
        </li>
        <img src={SlashImg} className="w-5 h-5 " alt="" />
        <li className=" cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md transition-all duration-300">
          FAQ
        </li>
      </ul>
    </div>
  );
}
```

Ensuite, importez ce fichier dans un composant `Home` que vous devez également créer:

```jsx
import Breadcrumb from "./Breadcrumb";

export default function Home() {
  return (
    <div className=" h-[100dvh] bg-gray-200">
      <div className="flex flex-col items-center gap-8 ">
        <h1 className=" text-4xl text-[#2E4053 ] mt-20">
          Mon Composant Breadcrumb 🍞
        </h1>
        <Breadcrumb />
      </div>
    </div>
  );
}
```

Pour l'instant, votre composant ressemble à ceci:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Breadcrumb-after-rendering-on-UI.png)
_Breadcrumb après rendu sur l'UI_

Pour effectuer des fonctionnalités de navigation avec ce composant, commencez par installer [React Router](https://www.npmjs.com/package/react-router-dom) (une bibliothèque largement utilisée pour gérer la navigation et le routage dans les applications React).

```bash
npm i react-router-dom
```

Ensuite, créez les routes dans votre composant App.

```jsx
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";

import About from "./About";
import FAQ from "./FAQ";
import Home from "./Home";
import Homepage from "./Homepage";
import Products from "./Products";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Navigate replace to="home" />} />
        <Route path="/" element={<Home />}>
          <Route path="home" element={<Homepage />} />
          <Route path="products" element={<Products />} />
          <Route path="about" element={<About />} />
          <Route path="faq" element={<FAQ />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
```

Le bloc de code ci-dessus est une configuration pour le routage côté client dans une application React utilisant React Router v6. Il configure un `BrowserRouter` pour gérer le routage dynamique et définit une série de composants Route dans Routes pour mapper les chemins d'URL aux composants React.

* `BrowserRouter` est une implémentation de routeur qui utilise l'API d'historique HTML5 pour garder l'UI synchronisée avec l'URL.
* `Navigate` redirige les utilisateurs vers une route spécifique. Dans ce cas, il redirige depuis la route d'index vers `/home`.
* Les composants `Route` définissent une correspondance entre un chemin et un composant. La propriété `element` spécifie ce qu'il faut rendre lorsque le chemin correspond à l'URL actuelle.
* La route `path="/" element={<Home />}` est une route imbriquée qui sert de mise en page pour ses routes enfants. Elle rend le composant Home lorsque l'URL est `/`. Imbriquée dans la route `Home` se trouvent les routes pour `home`, `products`, `about`, et `faq`, chacune rendant leurs composants respectifs lorsque leur chemin correspond à l'URL.

Ensuite, rendez-vous dans votre composant Breadcrumb et changez les éléments de liste en éléments `Link` (importés depuis React Router) pour aider au routage entre les routes.

```jsx
import { Link } from "react-router-dom";
import SlashImg from "./assets/slash.png";

export default function Breadcrumb() {
  return (
    <div className="bg-white ">
      <ul className=" flex border p-2 gap-6 text-xl text-[#2E4053] items-center">
        <Link
          to={"home"}
          className=" cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md">
          Accueil
        </Link>
        <img src={SlashImg} className="w-5 h-5 " alt="" />
        <Link
          to={"products"}
          className=" cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md transition-all duration-300">
          Produits
        </Link>
        <img src={SlashImg} className="w-5 h-5 " alt="" />
        <Link
          to={"about"}
          className=" cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md transition-all duration-300">
          À propos
        </Link>
        <img src={SlashImg} className="w-5 h-5 " alt="" />
        <Link
          to={"faq"}
          className=" cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md transition-all duration-300">
          FAQ
        </Link>
      </ul>
    </div>
  );
}
```

Ensuite, utilisez le composant `Outlet` fourni par React Router pour afficher le contenu de chaque route dans le composant `Home`.

```jsx
import Breadcrumb from "./Breadcrumb";
import { Outlet } from "react-router-dom";

export default function Home() {
  return (
    <div className=" h-[100dvh] bg-gray-200">
      <div className="flex flex-col items-center gap-8 ">
        <h1 className=" text-4xl text-[#2E4053 ] mt-20">
          Mon Composant Breadcrumb 🍞
        </h1>
        <Breadcrumb />
        <Outlet />
      </div>
    </div>
  );
}
```

Tester votre composant dans le navigateur donne maintenant le résultat suivant:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Routing-with-the-Breadcrumb-component.gif)
_Routage avec le composant Breadcrumb_

Avec cela, vos breadcrumbs basés sur l'emplacement sont fonctionnels, mais nous pouvons aller plus loin. Pour améliorer l'UX, nous pouvons ajouter une classe active à la route actuellement active, créant un indicateur visuel de l'endroit où l'utilisateur se trouve à tout moment.

Commencez par extraire l'emplacement actuel de l'utilisateur dans le composant Breadcrumb:

```jsx
  const location = useLocation();
```

Ensuite, utilisez la propriété pathname pour ajouter une classe active à chaque lien:

```jsx
import { Link, useLocation } from "react-router-dom";

import SlashImg from "./assets/slash.png";

export default function Breadcrumb() {
  const location = useLocation();
  console.log(location.pathname);

  return (
    <div className="bg-white ">
      <ul className=" flex border p-2 gap-6 text-xl text-[#2E4053] items-center">
        <Link
          to={"home"}
          className={`cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md ${
            location.pathname === "/home" && "bg-[#b572d6] text-white"
          }`}>
          Accueil
        </Link>
        <img src={SlashImg} className="w-5 h-5 " alt="" />
        <Link
          to={"products"}
          className={`cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md ${
            location.pathname === "/products" && "bg-[#b572d6] text-white"
          }`}>
          Produits
        </Link>
        <img src={SlashImg} className="w-5 h-5 " alt="" />
        <Link
          to={"about"}
          className={`cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md ${
            location.pathname === "/about" && "bg-[#b572d6] text-white"
          }`}>
          À propos
        </Link>
        <img src={SlashImg} className="w-5 h-5 " alt="" />
        <Link
          to={"faq"}
          className={`cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md ${
            location.pathname === "/faq" && "bg-[#b572d6] text-white"
          }`}>
          FAQ
        </Link>
      </ul>
    </div>
  );
}
```

Cela donne maintenant le résultat suivant:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Routing-with-the-Breadcrumb-component-after-adding-an-active-class.gif)
_Routage avec le composant Breadcrumb après avoir ajouté une classe active_

Délicieux! 🍩

### Breadcrumbs Basés sur le Chemin

Ce type de breadcrumb utilise le modèle de révélation progressive pour mieux guider les utilisateurs sur leur position en fonction de leurs actions.

Ici, nous allons créer deux routes et passer de la première à la troisième (Accueil à la page d'un produit unique).

Commencez par modifier un peu votre composant `Home`.

```jsx
export default function Home() {
  return (
    <div className=" h-[100dvh] bg-gray-200">
      <div className="flex flex-col items-center gap-8 ">
        <h1 className=" text-4xl text-[#2E4053 ] mt-20">
          Mon Composant Breadcrumb 🍞
        </h1>
        <Breadcrumb />
        <Outlet />

        <div className="flex gap-4 p-2 ">
          <Link to="products" className=" rounded-md p-2 bg-[#777] text-white">
            Produits
          </Link>
          <Link
            to="products/1"
            className=" rounded-md p-2 bg-[#777] text-white">
            Produit Unique
          </Link>
        </div>
      </div>
    </div>
  );
}
```

Les modifications incluent la création d'une page de produit unique vers laquelle nous allons router plus tard.

Ensuite, créez un chemin de route imbriqué pour la page dans le composant App:

```jsx
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";

import Home from "./Home";
import Homepage from "./Homepage";
import Products from "./Products";
import SingleProduct from "./SingleProduct";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Navigate replace to="home" />} />
        <Route path="/" element={<Home />}>
          <Route path="home" element={<Homepage />} />
          <Route path="products" element={<Products />}>
            <Route path=":productId" element={<SingleProduct />} />
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
```

Pour la page Produits déjà existante, ajoutez ces styles et modifications:

```jsx
import { Outlet } from "react-router-dom";

export default function Products() {
  return (
    <div className="bg-[#EDBB99] p-2 w-96 h-96 flex flex-col items-center">
      <h1>Page des Produits</h1>
      <Outlet />
    </div>
  );
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Page-after-creating-the-Single-Product-page-without-any-routing-1.png)
_Page après la création de la page Produit Unique sans aucun routage_

Enfin, modifiez votre composant breadcrumb pour afficher les routes lorsque vous routez vers elles depuis la page d'accueil.

```jsx
import { Link, useLocation } from "react-router-dom";

import RightArrowImg from "./assets/right-icon.png";

export default function Breadcrumb() {
  const location = useLocation();

  return (
    <div className="bg-white ">
      <ul className=" flex border p-2 gap-6 text-xl text-[#2E4053] items-center">
        <Link
          to={"home"}
          className={`cursor-pointer hover:bg-[#E8DAEF] hover:text-black p-4 rounded-md ${
            location.pathname === "/home" && "bg-[#b572d6] text-white"
          }`}>
          Accueil
        </Link>
        {location.pathname.includes("/products") && (
          <>
            <img src={RightArrowImg} className="w-5 h-5 " alt="" />
            <Link
              to={"products"}
              className={` hover:text-black cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md ${
                location.pathname.includes("/products") &&
                " bg-[#b572d6] text-white"
              } ${
                location.pathname.includes("/products/") &&
                " bg-[#E8DAEF] text-black"
              }`}>
              Produits
            </Link>
          </>
        )}
        {location.pathname.includes(`/products/`) && (
          <>
            <img src={RightArrowImg} className="w-5 h-5 " alt="" />
            <Link
              to={"products"}
              className={`hover:text-black  cursor-pointer hover:bg-[#E8DAEF] p-4 rounded-md ${
                location.pathname.includes("/products") &&
                "bg-[#b572d6] text-white"
              }`}>
              Produit Unique
            </Link>
          </>
        )}
      </ul>
    </div>
  );
}
```

Dans le code ci-dessus, nous affichons plus de breadcrumbs en fonction de la route dans laquelle nous nous trouvons et appliquons des styles pour refléter les changements de route.

Tester notre composant maintenant donne le résultat suivant:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Routing-with-the-Breadcrumb-component-after-adding-a-nested-route.gif)
_Routage avec le composant Breadcrumb après avoir ajouté une route imbriquée_

Super! 🍬

### Breadcrumbs Basés sur les Attributs

Les breadcrumbs basés sur les attributs se concentrent sur la mise en évidence d'attributs ou de caractéristiques spécifiques de la page actuelle, tels que les tags, les catégories, ou toute autre métadonnée pertinente.

Au lieu de simplement montrer le chemin de l'utilisateur à travers la hiérarchie du site web, ils fournissent un contexte supplémentaire qui peut aider à la navigation et à la compréhension. 

Un cas d'utilisation courant pour eux est sur les sites de commerce électronique où vous passez par plusieurs articles et filtrez à travers plusieurs propriétés de produits pour trouver votre produit souhaité.

Pour commencer, notre composant d'application va avoir une apparence radicalement différente sans aucun routage effectué.

```jsx
import Products from "./Products";

export default function App() {
  return (
    <div className=" h-[100dvh] bg-[#EDBB99]">
      <Products />
    </div>
  );
}

```

Ensuite, ajoutez ce JSX à votre composant `Products`:

```jsx
import Breadcrumb from "./Breadcrumb";

export default function Products() {
  const dogsArray = [
    {
      size: "S",
      color: "white",
      image: "/small-white-dog.jpg",
      name: "Gigi",
      age: 1,
    },
    {
      size: "M",
      color: "white",
      image: "/medium-white-dog.jpg",
      name: "Tom",
      age: 2,
    },
    {
      size: "L",
      color: "white",
      image: "/big-white-dog.jpg",
      name: "Jake",
      age: 3,
    },
    {
      size: "S",
      color: "black",
      image: "/small-black-dog.jpg",
      name: "Hill",
      age: 1,
    },
    {
      size: "M",
      color: "black",
      image: "/medium-black-dog.jpg",
      name: "Jack",
      age: 2,
    },
    {
      size: "L",
      color: "black",
      image: "/big-black-dog.jpg",
      name: "Jones",
      age: 3,
    },
    {
      size: "S",
      color: "brown",
      image: "/small-brown-dog.jpg",
      name: "Herbert",
      age: 1,
    },
    {
      size: "M",
      color: "brown",
      image: "/medium-brown-dog.jpg",
      name: "Coco",
      age: 2,
    },
    {
      size: "L",
      color: "brown",
      image: "/big-brown-dog.jpg",
      name: "Benny",
      age: 3,
    },
  ];


  return (
    <div className="flex flex-col items-center p-2">
      <h1 className="p-4">Page d'Adoption</h1>
      <Breadcrumb />
      <main>
        <div className="relative grid grid-cols-5 gap-6">
          {dogsArray.map((dog) => (
            <div key={dog.name}>
              <div className=" w-[225px] rounded-md overflow-hidden">
                <img className="w-full " src={dog.image} alt="" />
              </div>
              <div className="grid items-center grid-cols-2 gap-2 mt-2">
                <div className="flex items-center gap-2">
                  <span>Nom:</span>
                  <p className="text-center text-white bg-orange-900 border rounded-[4px] p-1.5 min-w-14">
                    {dog.name}
                  </p>
                </div>
                <div className="flex gap-2 ">
                  <span>Taille:</span>
                  <p className="text-center text-white min-w-14">{dog.size}</p>
                </div>
                <div className="flex gap-2 ">
                  <span>Couleur:</span>
                  <p className="text-center text-white capitalize min-w-14">
                    {dog.color}
                  </p>
                </div>
                <div className="flex gap-2 ">
                  <span>Âge:</span>
                  <p className="text-center text-white min-w-14">
                    {`${dog.age + " " + "an"}${dog.age > 1 ? "s" : ""}`}
                  </p>
                </div>
              </div>
            </div>
          ))}

          <div className="absolute bottom-0 left-0 p-1 translate-y-[110%]">
            <h2 className="mb-2">Filtrer par</h2>
            <div className="flex items-center mb-4">
              <h3 className="w-12">Taille:</h3>
              <div className="flex gap-2">
                <button
                  className={`p-2 text-center bg-white rounded-md min-w-14 `}>
                  Tous
                </button>
                <button
                  className={`p-2 text-center bg-white rounded-md min-w-14 `}>
                  S
                </button>
                <button
                  className={`p-2 text-center bg-white rounded-md min-w-14 `}>
                  M
                </button>
                <button
                  className={`p-2 text-center bg-white rounded-md min-w-14 `}>
                  L
                </button>
              </div>
            </div>
            <div className="flex items-center">
              <h3 className="w-12">Couleur:</h3>
              <div className="flex gap-2">
                <button
                  className={`p-2 text-center bg-white  rounded-md min-w-14 `}>
                  Tous
                </button>
                <button
                  className={`p-2 text-center bg-white  rounded-md min-w-14`}>
                  Blanc
                </button>
                <button
                  className={`p-2 text-center rounded-md bg-white min-w-14 `}>
                  Marron
                </button>
                <button
                  className={`p-2 text-center rounded-md bg-white  min-w-14 `}>
                  Noir
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
```

Ce JSX utilise des données fictives de chiens pour créer un modèle et le styliser avec Tailwind.

Pour l'instant, votre application devrait ressembler à ceci;

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Page-after-looping-over-the-dummy-dog-data.png)
_Page après avoir parcouru les données fictives de chiens_

Pour implémenter les breadcrumbs basés sur les attributs, commencez par créer deux états pour les attributs que vous souhaitez filtrer:

```jsx
const [sizeFilter, setSizeFilter] = useState(null);
const [colorFilter, setColorFilter] = useState(null);
```

Ensuite, créez une fonction pour filtrer en fonction de la valeur passée:

```jsx
  const filteredDogs = dogsArray.filter((dog) => {
    if (sizeFilter && dog.size !== sizeFilter) return false;

    if (colorFilter && dog.color !== colorFilter) return false;

    return true;
  });
```

Après cela, changez le tableau que vous avez utilisé pour créer le JSX en le tableau retourné par la fonction:

```jsx
 {filteredDogs.map((dog) => (
            <div key={dog.name}>
```

Enfin, utilisez la fonction de définition pour passer les valeurs par lesquelles vous souhaitez filtrer:

```jsx
<main>
        <div className="relative grid grid-cols-5 gap-6">
          {filteredDogs.map((dog) => (
            <div key={dog.name}>
              <div className=" w-[225px] rounded-md overflow-hidden">
                <img className="w-full " src={dog.image} alt="" />
              </div>
              <div className="grid items-center grid-cols-2 gap-2 mt-2">
                <div className="flex items-center gap-2">
                  <span>Nom:</span>
                  <p className="text-center text-white bg-orange-900 border rounded-[4px] p-1.5 min-w-14">
                    {dog.name}
                  </p>
                </div>
                <div className="flex gap-2 ">
                  <span>Taille:</span>
                  <p className="text-center text-white min-w-14">{dog.size}</p>
                </div>
                <div className="flex gap-2 ">
                  <span>Couleur:</span>
                  <p className="text-center text-white capitalize min-w-14">
                    {dog.color}
                  </p>
                </div>
                <div className="flex gap-2 ">
                  <span>Âge:</span>
                  <p className="text-center text-white min-w-14">
                    {`${dog.age + " " + "an"}${dog.age > 1 ? "s" : ""}`}
                  </p>
                </div>
              </div>
            </div>
          ))}

          <div className="absolute bottom-0 left-0 p-1 translate-y-[110%]">
            <h2 className="mb-2">Filtrer par</h2>
            <div className="flex items-center mb-4">
              <h3 className="w-12">Taille:</h3>
              <div className="flex gap-2">
                <button
                  // Réinitialiser l'état de la taille
                  onClick={() => setSizeFilter(null)}
                  className={`p-2 text-center bg-white rounded-md min-w-14 `}>
                  Tous
                </button>
                <button
                  // Définir le filtre sur petit
                  onClick={() => setSizeFilter("S")}
                  className={`p-2 text-center bg-white rounded-md min-w-14 `}>
                  S
                </button>
                <button
                  // Définir le filtre sur moyen
                  onClick={() => setSizeFilter("M")}
                  className={`p-2 text-center bg-white rounded-md min-w-14 `}>
                  M
                </button>
                <button
                  // Définir le filtre sur grand
                  onClick={() => setSizeFilter("L")}
                  className={`p-2 text-center bg-white rounded-md min-w-14 `}>
                  L
                </button>
              </div>
            </div>
            <div className="flex items-center">
              <h3 className="w-12">Couleur:</h3>
              <div className="flex gap-2">
                <button
                  // Réinitialiser l'état de la couleur
                  onClick={() => setColorFilter(null)}
                  className={`p-2 text-center bg-white  rounded-md min-w-14 `}>
                  Tous
                </button>
                <button
                  // Définir la couleur sur blanc
                  onClick={() => setColorFilter("white")}
                  className={`p-2 text-center bg-white  rounded-md min-w-14 `}>
                  Blanc
                </button>
                <button
                  // Définir la couleur sur marron
                  onClick={() => setColorFilter("brown")}
                  className={`p-2 text-center rounded-md bg-white min-w-14 `}>
                  Marron
                </button>

                <button
                  // Définir la couleur sur noir
                  onClick={() => setColorFilter("black")}
                  className={`p-2 text-center rounded-md bg-white  min-w-14 `}>
                  Noir
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
```

Tester votre composant maintenant donne le résultat suivant:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Filtering-by-properties.gif)
_Filtrage par propriétés fonctionnant_

Exquis!🍦

Pour ajouter notre fonctionnalité de breadcrumb, passez les props de filtre au composant comme ceci:

```jsx
<Breadcrumb sizeFilter={sizeFilter} colorFilter={colorFilter} />
```

Ensuite, utilisez ces props pour rendre les en-têtes:

```jsx
import RightArrowImg from "./assets/right-icon.png";

export default function Breadcrumb({ sizeFilter, colorFilter }) {
  return (
    <div className="mb-4 bg-gray-200 rounded-md ">
      <ul className="   flex items-center  text-xl text-[#2E4053] text-left">
        <li className={`cursor-pointer p-4 rounded-md `}>Tous</li>

        {sizeFilter && (
          <>
            <img src={RightArrowImg} className="w-5 h-5 " alt="" />
            <li className={`cursor-pointer p-4 rounded-md capitalize`}>
              {sizeFilter}
            </li>
          </>
        )}
        {colorFilter && (
          <>
            <img src={RightArrowImg} className="w-5 h-5 " alt="" />
            <li className={`cursor-pointer p-4 rounded-md capitalize`}>
              {colorFilter}
            </li>
          </>
        )}
      </ul>
    </div>
  );
}
```

Avant de voir le résultat final, ajoutons des indicateurs des props de filtre actuellement actives:

```jsx
<main>
        <div className="relative grid grid-cols-5 gap-6">
          {filteredDogs.map((dog) => (
            <div key={dog.name}>
              <div className=" w-[225px] rounded-md overflow-hidden">
                <img className="w-full " src={dog.image} alt="" />
              </div>
              <div className="grid items-center grid-cols-2 gap-2 mt-2">
                <div className="flex items-center gap-2">
                  <span>Nom:</span>
                  <p className="text-center text-white bg-orange-900 border rounded-[4px] p-1.5 min-w-14">
                    {dog.name}
                  </p>
                </div>
                <div className="flex gap-2 ">
                  <span>Taille:</span>
                  <p className="text-center text-white min-w-14">{dog.size}</p>
                </div>
                <div className="flex gap-2 ">
                  <span>Couleur:</span>
                  <p className="text-center text-white capitalize min-w-14">
                    {dog.color}
                  </p>
                </div>
                <div className="flex gap-2 ">
                  <span>Âge:</span>
                  <p className="text-center text-white min-w-14">
                    {`${dog.age + " " + "an"}${dog.age > 1 ? "s" : ""}`}
                  </p>
                </div>
              </div>
            </div>
          ))}

          <div className="absolute bottom-0 left-0 p-1 translate-y-[110%]">
            <h2 className="mb-2">Filtrer par</h2>
            <div className="flex items-center mb-4">
              <h3 className="w-12">Taille:</h3>
              <div className="flex gap-2">
                <button
                  onClick={() => setSizeFilter(null)}
                  className={`p-2 text-center  rounded-md min-w-14 ${
                    // Ajout dynamique de la couleur de fond
                    sizeFilter === null
                      ? "bg-orange-900 text-white"
                      : "bg-white text-black "
                  }`}>
                  Tous
                </button>
                <button
                  onClick={() => setSizeFilter("S")}
                  className={`p-2 text-center  rounded-md min-w-14 ${
                    // Ajout dynamique de la couleur de fond
                    sizeFilter === "S"
                      ? "bg-orange-900 text-white"
                      : "bg-white text-black "
                  }`}>
                  S
                </button>
                <button
                  onClick={() => setSizeFilter("M")}
                  className={`p-2 text-center  rounded-md min-w-14 ${
                    // Ajout dynamique de la couleur de fond
                    sizeFilter === "M"
                      ? "bg-orange-900 text-white"
                      : "bg-white text-black "
                  }`}>
                  M
                </button>
                <button
                  onClick={() => setSizeFilter("L")}
                  className={`p-2 text-center  rounded-md min-w-14 ${
                    // Ajout dynamique de la couleur de fond
                    sizeFilter === "L"
                      ? "bg-orange-900 text-white"
                      : "bg-white text-black "
                  }`}>
                  L
                </button>
              </div>
            </div>
            <div className="flex items-center">
              <h3 className="w-12">Couleur:</h3>
              <div className="flex gap-2">
                <button
                  onClick={() => setColorFilter(null)}
                  className={`p-2 text-center   rounded-md min-w-14 ${
                    // Ajout dynamique de la couleur de fond
                    colorFilter === null
                      ? "bg-orange-900 text-white"
                      : "bg-white text-black "
                  }`}>
                  Tous
                </button>
                <button
                  onClick={() => setColorFilter("white")}
                  className={`p-2 text-center   rounded-md min-w-14 ${
                    // Ajout dynamique de la couleur de fond
                    colorFilter === "white"
                      ? "bg-orange-900 text-white"
                      : "bg-white text-black "
                  }`}>
                  Blanc
                </button>
                <button
                  onClick={() => setColorFilter("brown")}
                  className={`p-2 text-center rounded-md   min-w-14 ${
                    // Ajout dynamique de la couleur de fond
                    colorFilter === "brown"
                      ? "bg-orange-900 text-white"
                      : " bg-white text-black "
                  }`}>
                  Marron
                </button>

                <button
                  onClick={() => setColorFilter("black")}
                  className={`p-2 text-center rounded-md    min-w-14 ${
                    // Ajout dynamique de la couleur de fond
                    colorFilter === "black"
                      ? "bg-orange-900 text-white"
                      : " bg-white text-black"
                  }`}>
                  Noir
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
```

Un test final sur votre composant donne maintenant ce résultat:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Filtering-by-properties-tested.gif)
_Filtrage par propriétés et affichage dans le breadcrumb_

Et voilà! Votre composant filtre parfaitement, et montre également un breadcrumb utile pour aider les utilisateurs à savoir quelles propriétés ils ont filtrées.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/bruce-almighty-jim-carrey.gif)
_Bruce Tout-Puissant Jim Carrey beau gif_

## Meilleures Pratiques pour les Breadcrumbs dans React

Lors de l'implémentation de breadcrumbs dans React, il est crucial de suivre certaines meilleures pratiques pour garantir une expérience utilisateur fluide. Voici quelques points clés à considérer:

1. **Cohérence avec le Routage React**: Les breadcrumbs doivent s'aligner avec la structure de routage de l'application. Vous pouvez le faire en implémentant des breadcrumbs dynamiques en utilisant une bonne bibliothèque de routage (React Router). En définissant des routes et en générant un tableau de breadcrumbs basé sur la route actuelle de l'utilisateur, vous pouvez vous assurer que le chemin de breadcrumb reflète le chemin de navigation de l'utilisateur.
2. **Largeur et Profondeur des Chemins de Breadcrumb**: Les chemins de breadcrumb doivent représenter l'emplacement de l'utilisateur au sein de l'application. Cela inclut l'utilisation d'un séparateur, tel qu'une barre oblique ("/"), pour distinguer les différentes parties du chemin de breadcrumb.
3. **Nom et Navigation**: Les breadcrumbs doivent être faciles à comprendre et à naviguer. Cela implique d'utiliser des noms clairs et descriptifs pour chaque breadcrumb et de s'assurer que chaque lien de breadcrumb est cliquable, menant l'utilisateur à la page appropriée.
4. **Assurer l'Accessibilité**: Les breadcrumbs doivent être accessibles à tous les utilisateurs. Cela peut être réalisé en utilisant l'attribut `aria-label` pour identifier le chemin de breadcrumb comme un repère de navigation. Cela facilite la localisation et la navigation du chemin de breadcrumb pour les utilisateurs utilisant des technologies d'assistance.
5. **Personnalisation et Facilité d'Utilisation**: Lorsque vous utilisez un composant pour créer des breadcrumbs, considérez ses options de personnalisation et sa facilité d'utilisation. Recherchez des composants qui fournissent des valeurs par défaut utiles et permettent une personnalisation facile des textes, des liens et des séparateurs.

En adhérant à ces meilleures pratiques, vous pouvez créer des breadcrumbs efficaces et conviviaux dans vos applications React. 

Voici les liens vers les dépôts sur GitHub:

* [Basé sur l'emplacement](https://github.com/Daiveedjay/React-breadcrumb-article-location-based)
* [Basé sur le chemin](https://github.com/Daiveedjay/React-breadcrumb-article-path-based)
* [Basé sur les attributs](https://github.com/Daiveedjay/React-breadcrumb-article-attribute-based)

## Conclusion

L'implémentation de breadcrumbs dans les applications React fournit non seulement une aide à la navigation, mais contribue également à une expérience utilisateur fluide et intuitive. Le respect des meilleures pratiques améliore l'utilisabilité et l'accessibilité des applications.

Tout comme l'arôme du pain fraîchement cuit incite les gens affamés à venir visiter la boulangerie, un chemin de breadcrumb bien structuré peut inciter les utilisateurs à explorer et naviguer dans une application avec facilité, améliorant ainsi la navigation et l'expérience utilisateur. Et c'est ainsi que le cookie s'émiette, laissant une trace de navigation délicieuse dans son sillage.

### Informations de Contact

Vous souhaitez me contacter ou me connecter? N'hésitez pas à me contacter sur les plateformes suivantes:

* Twitter / X: [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn: [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email: Jajadavidjid@gmail.com