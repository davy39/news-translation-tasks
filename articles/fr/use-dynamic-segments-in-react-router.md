---
title: Comment implémenter des segments dynamiques avec useParams dans React Router
subtitle: ''
author: Alex Anie
co_authors: []
series: null
date: '2024-01-31T22:34:08.000Z'
originalURL: https://freecodecamp.org/news/use-dynamic-segments-in-react-router
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Dynamic-Segment-in-react-router-800x418.png
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: Comment implémenter des segments dynamiques avec useParams dans React Router
seo_desc: 'On a traditional website, when a user clicks on a URL, the browser makes
  a full-page request from the server and directs the user to a new page. This is
  referred to as static routing.

  This is very useful if you just need to navigate the user to a new...'
---

Sur un site web traditionnel, lorsqu'un utilisateur clique sur une URL, le navigateur envoie une requête complète de la page au serveur et dirige l'utilisateur vers une nouvelle page. Cela est appelé routage statique.

Cela est très utile si vous avez simplement besoin de naviguer vers une nouvelle page. Mais avec le développement des applications web, il est de plus en plus nécessaire que les pages soient rendues côté client ou chargées dynamiquement.

Cela implique la mise à jour de parties spécifiques de l'URL appelées segments, ainsi que le rendu de nouveau contenu ou la mise à jour du contenu sur la même page sans envoyer de requête au serveur ou recharger toute la page.

Cela est très courant et utile dans les applications web modernes. Cela permet le rendu côté client, améliore la navigation sur le site et permet des transitions et animations fluides (puisque le navigateur n'a pas besoin de recharger la page à partir de serveurs externes).

Cela peut globalement améliorer les performances du site et offrir une bonne expérience utilisateur.

Dans ce tutoriel, vous apprendrez à propos des segments dynamiques dans React Router.

Nous aborderons ce qu'est le routage dynamique et en quoi il diffère du routage statique. Nous couvrirons également comment utiliser *useParams* pour activer les segments dynamiques, et comment définir votre chemin lors de la récupération de données depuis une API.

Enfin, nous construirons un nouveau projet qui rend dynamiquement du nouveau contenu sur la même page lorsque l'utilisateur clique sur la barre latérale.

À la fin de ce guide, vous devriez être capable d'implémenter des segments dynamiques par vous-même dans votre application React.

## Table des matières
- [Prérequis](#heading-prerequisites)
- [Configuration du projet](#heading-installation)
    - [Installer React](#heading-install-react)
    - [Installer React Router](#heading-install-react-router)
    - [Installer Feather Icon](#heading-install-feather-icon)
    - [Installer Tailwind CSS](#heading-install-tailwind-css)
- [Routage côté client](#heading-client-side-routing)
- [Segments dynamiques](#heading-dynamic-segments)
- [Routage imbriqué](#heading-nested-routing)
- [Projet : Construire une galerie d'art](#heading-project-build-an-art-gallery)
    - [Aperçu du projet](#heading-project-overview)
    - [Structure des dossiers](#heading-folder-structure)
    - [Comment configurer la page d'accueil](#heading-how-to-set-up-the-home-page)
    - [Comment créer et styliser la barre de navigation](#heading-how-to-create-and-style-the-navbar)
    - [Comment créer la barre latérale](#heading-how-to-create-the-asidebar)
    - [Comment créer le composant de contenu](#heading-how-to-create-the-content-component)
- [Résumé](#heading-summary)


## Prérequis

Pour suivre ce tutoriel, vous aurez besoin d'une connaissance de base des éléments suivants :

- React
- React-Router
- Tailwind CSS (optionnel)

## Configuration du projet

Pour commencer, créez un dossier appelé `dynamic-segment` et ouvrez-le dans VS Code (ou votre éditeur de code préféré) :

![Capture d'écran de VS Code](https://www.freecodecamp.org/news/content/images/2024/01/Untitled.png)

Ensuite, cliquez sur `Ctrl + ` (accent grave) pour lancer le terminal comme indiqué ci-dessus. Cela nous permettra d'installer les packages npm que nous utiliserons dans ce projet.

## Installations

Maintenant que notre projet est configuré, installons les packages `npm` dont nous avons besoin pour faire fonctionner notre projet.

### Installer [React](https://react.dev/)

React est une bibliothèque JavaScript pour construire des composants réutilisables et interactifs. Pour l'installer, copiez et collez la commande fournie par [vite.js](https://vitejs.dev/) ci-dessous.

```bash
npm create vite@latest
```

Ensuite, suivez simplement le guide d'installation pour terminer le processus. Une fois l'installation terminée, le dossier node_modules devrait être présent dans votre dossier de projet.

### Installer [React Router](https://reactrouter.com/en/main)

C'est une bibliothèque de routage React pour créer des applications de routage côté client. Pour l'installer, copiez et collez la commande ci-dessous et appuyez sur entrée.

```bash
npm i react-router-dom
```

### Installer [Feather Icon](https://feathericons.dev/)

Feather icon est une petite mais belle collection d'icônes open-source de 24 x 24 sur une grille. Elle est conçue pour ajouter des icônes plates aux applications web.

Pour l'installer, collez la commande ci-dessous et appuyez sur entrée.

```bash
npm i react-feather
```

### Installer [Tailwind CSS](https://tailwindcss.com/)

Tailwind est un framework CSS utilitaire-first pour construire des designs de sites web beaux et compacts. Pour l'installer, exécutez la commande sur le terminal ci-dessous.

```bash
npm install -D tailwindcss postcss autoprefixer
```

Cela créera un fichier `tailwind.config.js`. Ensuite, générez vos fichiers `postcss.config.js` avec la commande ci-dessous :

```bash
npx tailwindcss init -p
```

Ensuite, configurez vos chemins de modèle et ajoutez les chemins vers tous vos fichiers de modèle dans votre fichier `tailwind.config.js`. Ensuite, cliquez sur `ctrl + s` pour sauvegarder.

```jsx
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

Ensuite, supprimez tous les styles CSS dans le fichier `./src/index.css` et ajoutez les directives Tailwind `@tailwind` pour chacune des couches de Tailwind.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Ensuite, supprimez le dossier `assets`, les fichiers `App.css` et `App.jsx` du dossier `/src`. Une fois que vous avez fait cela, configurez les fichiers `main.jsx` comme composant de route comme indiqué ci-dessous :

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css';

import {
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
  Route
} from 'react-router-dom';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route path='/' element={<p className='text-blue-700'>Bonjour, le monde</p>}></Route>
    </Route>
  )
)

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
```

Ensuite, exécutez la commande ci-dessous dans le terminal pour lancer votre application :

```jsx
npm run dev
```

Votre application devrait ressembler à ceci dans votre navigateur :

![Bonjour, le monde dans React](https://www.freecodecamp.org/news/content/images/2024/01/Untitled-1.png)

## Routage côté client

Dans React Router, la navigation est relative entre l'attribut `path` et la propriété `to`. Lorsque l'utilisateur clique en utilisant le composant `<Link>` (balise `<a>`), il navigue vers le `path` spécifié dans le composant de route et rend le composant lorsqu'il correspond.

Ce type de navigation est appelé routage côté client car nous ne rendons pas les pages depuis le serveur, mais plutôt en naviguant d'un composant à un autre dans l'application.

L'exemple ci-dessous explique comment fonctionne le routage côté client :

```jsx
⚡️ //main.jsx

import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css';
nt
import 
{
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
  Route
} from 'react-router-dom';
import Book from './book';
import Bookshop from './bookshop';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
     👉 <Route path='/' element={<Book />}></Route>
     👉 <Route path='bookshop' element={<Bookshop />}></Route>
    </Route>
  )
)

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
```

Dans l'exemple de code ci-dessus, nous avons importé deux composants, `Book` et `Bookshop`, et les avons liés via la balise `<a>` et le composant `Route` sur le composant `./src/main.jsx`.

```jsx
⚡️ //book.jsx

export default function Book() {
return (
    <>
        <main className="px-4">
            <ul>
                <ol>77 Façons d'atteindre plus de clients Par : <i>Ubuy</i></ol>
                <ol>Authenticité Par : <i>Emanuel Rose</i> </ol>
                <ol> Changez votre façon de penser, changez votre vie Par : <i>Brian Tracy</i></ol>

            👉 <a href="bookshop" className="text-blue-600 inline-block px-4 underline">voir la librairie</a>
                {/* <a href="publisher/itemId" className="text-blue-600 underline">Éditeur</a> */}
            </ul>
        </main>
    </>
)
}
```

L'attribut `href` accepte le composant `bookshop` comme chemin relatif. Donc, cliquer sur le lien devrait vous naviguer vers le composant `bookshop`.

```jsx
⚡️ //bookshop.jsx

export default function Bookshop() {
  return (
    <div className="px-4">
    <h1>liste des librairies</h1>
    <ul>
        <li>Librairie & Papeterie</li>
        <li>Livres de Simon</li>
        <li>Maison du Livre Dynamique</li>
    </ul>

  👉 <a href="/" className="text-blue-600 inline-block px-4 underline">Noms des Livres</a>
</div>
  )
}
```

L'attribut `href="/"` dans le composant bookshop spécifie la route d'index et devrait vous ramener aux composants d'accueil.

Votre application devrait ressembler à ceci dans votre navigateur – cliquez pour naviguer vers le composant bookshop.

![Routage côté client dans React](https://www.freecodecamp.org/news/content/images/2024/01/Browser_output.gif)

À partir de la sortie du navigateur ci-dessus, vous remarquerez comment l'URL est mise à jour depuis la barre d'adresse et un nouveau composant est rendu.

Ce type de routage est appelé routage côté client et ne met à jour le chemin de l'URL qu'une seule fois avec la nouvelle route.

Dans la section suivante, j'expliquerai comment vous pouvez mettre à jour un segment particulier et rendre le contenu dynamiquement.

## Segments dynamiques

Un segment dynamique, comme son nom l'indique, est un moyen de rendre un nouveau composant (UI) en mettant à jour un segment particulier dans l'URL appelé params. Vous utilisez le hook [useParams](https://reactrouter.com/en/main/hooks/use-params) de `react-router-dom` pour faire cela.

Cela est très utile dans les situations où le contenu doit être rendu dynamiquement à partir d'un composant particulier ou d'une API tierce.

En continuant depuis où nous nous sommes arrêtés dans le code, allez au composant `./src/main.jsx`. Modifiez la Route et ajoutez `:itemId` au chemin comme indiqué ci-dessous :

```jsx
⚡️ //main.jsx

<Route>
      <Route path='/' element={<Book />}></Route>
      <Route path='bookshop' element={<Bookshop />} />
 👉  <Route path='publisher/:itemId' element={<Publisher />} />
    </Route>
```

Notez que le `:` dans le segment d'URL `:itemId` signifie Segment Dynamique.

Ensuite, créez un nouveau composant `./src/publisher.jsx` et ajoutez le code ci-dessous :

```jsx
⚡️ //publisher.jsx

import { useParams } from "react-router-dom"

export default function Publisher() {
    const { itemId } = useParams();

return (
    <>
    {
        itemId ? (
            <div>
                <h1>Sociétés d'édition de livres</h1>
                <ul>
                    <ol>Penguin Random House</ol>
                    <ol>Scholastic</ol>
                    <ol>LPI Media</ol>
                </ul>
            </div>
        ) : (
            <p>L'élément de la page n'est pas présent</p>
        )
    }
    </>
)
}
```

Parlons de ce que fait ce code :

- `const { itemId } = useParams()` : ici, nous appliquons la *destructuration* pour obtenir les params de l'URL dans la barre d'adresse. Avec cela, nous pouvons rendre le contenu de retour.
- `itemId?():` ici, nous rendons conditionnellement une liste de sociétés de librairies lorsqu'un lien cliqué correspond aux params.

Ensuite, dans le composant `./src/book`, incluez le `publisher/itemId` comme indiqué dans la balise `<a>` ci-dessous :

```jsx
⚡️ //book.jsx

export default function Book() {
return (
    <>
        <main className="px-4">
            <ul>
                <ol>77 Façons d'atteindre plus de clients Par : <i>Ubuy</i></ol>
                <ol>Authenticité Par : <i>Emanuel Rose</i> </ol>
                <ol> Changez votre façon de penser, changez votre vie Par : <i>Brian Tracy</i></ol>

                <a href="bookshop" className="text-blue-600 inline-block px-4 underline">voir la librairie</a>
            👉  <a href="publisher/itemId" className="text-blue-600 underline">Éditeur</a>
            </ul>
        </main>
    </>
)
}
```

Votre application devrait ressembler à ceci dans votre navigateur :

![Segments dynamiques dans React](https://www.freecodecamp.org/news/content/images/2024/01/Dynamic_segment_one.gif)

Remarquez la mise à jour dans l'URL de la barre d'adresse du navigateur.

Regardons un autre exemple.

Dans une application réelle, les segments dynamiques sont principalement utilisés pour rendre le contenu dynamiquement lorsque le segment `:itemId` correspond à l'`id` des API retournées.

Voyons comment cela fonctionne. Tout d'abord, nous devons décider d'où nous allons récupérer nos données. Dans ce cas, créez un objet JavaScript externe `./scr/books.js` et copiez et collez le code ci-dessous :

```jsx
⚡️ //books.js

export default [
    {   id: "1",
        title: "Le Grand Gatsby",
        author: "F. Scott Fitzgerald",
        year: "1925",
        description: "Le Grand Gatsby est un roman de 1925 écrit par l'auteur américain F. Scott Fitzgerald. Situé à l'ère du jazz sur Long Island, près de New York, le roman décrit les interactions du narrateur à la première personne, Nick Carraway, avec le mystérieux millionnaire Jay Gatsby et l'obsession de Gatsby de se réunir avec son ancien amour, Daisy Buchanan."
    },

    {   id: "2",
        title: "Orgueil et Préjugés",
        author: "Jane Austen",
        year: "1813",
        description: "Orgueil et Préjugés est le deuxième roman de l'auteure anglaise Jane Austen, publié en 1813. Roman de mœurs, il suit le développement du personnage d'Elizabeth Bennet, la protagoniste du livre"
    },

    {   id: "3",
        title: "Ne tirez pas sur l'oiseau moqueur",
        author: "Harper Lee",
        year: "1960",
        description: "Ne tirez pas sur l'oiseau moqueur est un roman de l'auteure américaine Harper Lee. Il a été publié en juin 1960 et est devenu instantanément un succès. Aux États-Unis"
    },

    {   id:"4",
        title: "Bien-aimée",
        author: "Toni Morrison",
        year: "1987",
        description: "Bien-aimée est un roman de 1987 écrit par la romancière américaine Toni Morrison. Situé dans la période suivant la guerre civile américaine, le roman raconte l'histoire d'une famille dysfonctionnelle d'anciens esclaves dont la maison de Cincinnati est hantée par un esprit malveillant"
    }
]
```

Ensuite, créez un nouveau composant appelé `./src/FavBooks.jsx` et écrivez le code ci-dessous :

```jsx
⚡️ //FavBooks.js

import { useParams } from 'react-router-dom';
import book from './book';

export default function FavBooks() {
  const {bookId} =  useParams() 

👉 const newFavBook = book.find((book) => book.id === bookId)
  
  if(!newFavBook){
    return <p>{`Cette page ne contient pas de livres préférés`}</p>
  }
  return (
    <>
      <main>
          {newFavBook && (
            <>
              <main>
                <p>{`Titre: ${newFavBook.title}`}</p>
                <p>{`Par: ${newFavBook.author}`}</p>
                <p>{`Année: ${newFavBook.year}`}</p>
                <p>{`Description: ${newFavBook.description}`}</p>
              </main>
            </>
          )}
      </main>
    </>
  )
}
```

Ensuite, allez dans le composant `./src/book.jsx` et mettez à jour le code comme suit :

```jsx
import { Link } from 'react-router-dom';
import books from './book.js';

export default function Books() {
  
  return (
    <>
      <div className='m-4'>
        <p className="text-3xl">{`Liste de mes livres préférés`}</p>
      </div>

      <div className='m-4'> 
        {
          books && books.map((book)=> (
            <>
            <ul>
              <li>
                <Link to={`newbooks/${book.id}`} className='text-blue-600 underline'>{book.title}</Link>
              </li>
            </ul>
          </>
          )) 
        }
      </div>
    </>
  )
}
```

Ensuite, configurez le `path` vers le segment dynamique sur le composant de route :

```jsx
import Book from '../src/books';
import Bookshop from './bookshop';
import Publisher from './publisher';
👉 import FavBooks from './FavBooks';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route path='/' element={<Book />}></Route>
	      <Route path='bookshop' element={<Bookshop />} />
		    <Route path='publisher/:itemId' element={<Publisher />} />
     👉 <Route path='newbooks/:bookId' element={<FavBooks />} />
    </Route>
  )
)
```

Votre application devrait ressembler à ceci dans votre navigateur :

![Segment dynamique depuis l'API dans React](https://www.freecodecamp.org/news/content/images/2024/01/Dynamic_segment_from_api.gif)

À partir de la sortie du navigateur, les paramètres de l'URL sont mis à jour avec le segment de chemin et les valeurs d'ID de l'objet books.js.

Essayez de cliquer sur chacun des titres et remarquez comment l'ID de l'objet books.js est présent dans l'URL.

Lorsque l'utilisateur clique sur le lien, il rend une nouvelle UI sur une nouvelle page. Mais il y a des cas où vous pourriez vouloir rendre le contenu de l'API sur la même page sous forme d'éléments de liste, afin que le contenu n'ait pas à s'ouvrir sur une nouvelle page. Pour ce faire, nous devons implémenter le routage imbriqué.

## Routage imbriqué

Le routage imbriqué permet d'imbriquer des routes pour rendre de nouveaux composants sur la même page pour une navigation facile et une interactivité rapide de l'élément. Les routes imbriquées font fonctionner les éléments listés comme un onglet. Dès qu'un onglet est cliqué, le contenu correspondant à l'onglet s'affiche.

Maintenant, voyons comment convertir notre petite application en une route imbriquée.

Pour aller au composant `./src/main` et créer une route imbriquée comme suit :

```jsx
const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>

      <Route path='/' element={<Book />} >
   👉  <Route path='newbooks/:bookId' element={<FavBooks />} />
      </Route>

      <Route path='bookshop' element={<Bookshop />} />
      <Route path='publisher/:itemId' element={<Publisher />}>
    </Route>
    </Route>
  )
)
```

Essentiellement, nous imbriquons le composant `FavBook` dans le composant `Book` en tant qu'enfant direct, afin que le contenu s'affiche en dessous.

Ensuite, créez une balise div et rendez un composant outlet. Cela indique à react-router où rendre la nouvelle route imbriquée.

```jsx
return (
    <>
      <div className='m-4'>
        <p className="text-3xl">{`Liste de mes livres préférés`}</p>
      </div>

    👉 <section className='flex'>
        <div className='m-4'> 
          {
            books && books.map((book)=> (
              <>
              <ul>
                <li>
                  <Link to={`newbooks/${book.id}`} className='text-blue-600 underline'>{book.title}</Link>
                </li>
              </ul>
            </>
            )) 
          }
        </div>
        <div className='w-[70%]'>
       👉  <Outlet />
        </div>
      </section>
    </>
  )
```

Notez que pour rendre le composant `FavBook` imbriqué côte à côte, à la fois l'outlet et la balise de liste de livres sont imbriqués dans une balise section, et un style de display flex est appliqué.

Votre code devrait ressembler à ceci dans votre navigateur :

![Routage imbriqué dans React](https://www.freecodecamp.org/news/content/images/2024/01/rendered_outlet.gif)

À partir de la sortie du navigateur, vous pouvez voir que chaque élément listé fonctionne comme un onglet, et cliquer dessus rend le contenu de l'API.

Vous avez appris comment créer un segment dynamique. Dans la section suivante, nous construirons un projet pour aider à consolider ce que nous avons appris encore plus.

## Projet : Construire une galerie d'art

Dans ce projet, nous allons construire une application de galerie d'art qui contient une liste de sculptures et d'œuvres d'art de différents pays. Cela vous aidera à solidifier les concepts que vous avez précédemment appris.

Nous allons implémenter les fonctionnalités suivantes :

- Routage côté client
- Liens actifs
- Segments dynamiques
- Routes imbriquées

Voici un aperçu rapide de ce à quoi le projet ressemblera.

### Aperçu du projet

Voici un aperçu complet de notre projet après achèvement. Vous pouvez télécharger le code source sur 👉 [GitHub](https://github.com/alex-anie/Arts-Culture-dynamic-segment-example) ici.

![Projet : Construire une galerie d'art dans React.js](https://www.freecodecamp.org/news/content/images/2024/01/cotent_component-1.gif)

### Structure des dossiers

Voici à quoi devrait ressembler la structure des dossiers du projet :

```html
📂src
		📂apis
			├── data.js
		📂components
			├── AsideBar.jsx
			├── Content.jsx
			├── Navbar.jsx
		📂pages
			├── home.jsx
	├── index.css
	├── main.jsx
├── index.html
```

### Comment configurer la page d'accueil

Pour configurer la page d'accueil, créez un composant home `./src/pages/home.jsx` et ajoutez le code ci-dessous :

```jsx
├── home.jsx

export default function Home() {
return (
    <>
        <main className="">
            <section>
                <p className="text-orange-600">Bonjour le monde</p>
            </section>
        </main>
    </>
)
}
```

Ensuite, allez dans le composant `main.jsx`. Si vous n'en avez pas encore, créez-le en tant que `./src/main.jsx`. puis configurez la route comme suit :

```jsx
├── main.jsx

import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css';

import {
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
  Route
} from 'react-router-dom';

import Home from './pages/home';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route  path='/' element={<Home />}>
      
    </Route>
  )
)

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
```

Ensuite, tapez `npm run dev` pour lancer votre application.

Votre application devrait ressembler à ceci dans votre navigateur :

![Bonjour, le monde dans React](https://www.freecodecamp.org/news/content/images/2024/01/Untitled-2.png)

### Comment créer et styliser la barre de navigation

Maintenant que nous avons les composants d'accueil et de route configurés, créons le composant de barre de navigation, qui est le composant supérieur de notre application.

Créez un composant `./src/components/navbar.jsx` et ajoutez le code ci-dessous :

```jsx
├── navbar.jsx

import { Activity, Search } from "react-feather";

export default function Navbar() {
  return (
   <>
    <main className="">
        <header>
            <nav className="flex justify-between bg-slate-200 rounded-3xl py-2">
                {/* logo */}
                <div className="">
                    <Activity className="inline-block ml-10 mr-2 text-orange-500" />
                    <p className="inline-block text-xl">{`Arts & Culture`}</p>
                </div>

                {/* Navlinks */}
                <div className="bg-white rounded-3xl py-1 px-2 mr-5">
                    <Search className="inline-block mr-1 text-slate-500"/>
                    <input type="search" id="site-search" name="q" placeholder="Rechercher n'importe quoi" className="bg-transparent outline-none text-slate-800"/>
                </div>
            </nav>
        </header>
    </main>
   </>
  )
}
```

Dans le code ci-dessus, la barre de navigation est divisée entre le logo et la barre de recherche.

- **Le logo** : nous importons les *icônes d'activité* en tant que composant depuis les icônes de plume et appliquons quelques classes CSS Tailwind pour le styliser. L'icône est définie sur `inline-block` afin que nous puissions appliquer de l'espace. Nous appliquons `ml-10` et `mr-2`, qui est une marge gauche de `2.5rem` et droite `0.5rem` avec une couleur orange (`text-orange-500`).
- **La recherche** : pour la barre de recherche, nous l'avons également importée depuis les icônes de plume en tant que composant et appliqué le style suivant : `inline-block mr-1 text-slate-500`. Si vous avez du mal à comprendre les classes CSS Tailwind, vous pouvez en lire plus à ce sujet dans la documentation [ici](https://tailwindcss.com/).

Pour positionner le logo et la barre de recherche côte à côte, nous définissons l'en-tête parent sur display flex et justify-content de space-between pour appliquer de l'espace entre le logo et la barre de recherche.

Ensuite, ajoutez la barre de navigation à la route comme suit :

```jsx
├── main.jsx

import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'

import {
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
  Route
} from "react-router-dom"

👉  import Navbar from './components/Navbar'
		import Home from './pages/home'

const router = createBrowserRouter(
  createRoutesFromElements(
   <Route  path='/' element={<Home />}>
    👉   <Route path='/' element={<Navbar />} /> 
    </Route>
  )
)

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
```

Dans le code ci-dessus, le composant Navbar est imbriqué dans le composant Home. Cela signifie que nous devons utiliser un composant Outlet pour rendre le composant Navbar.

Ensuite, allez dans le composant `./src/page/home`, importez et remplacez le `<p>` par le composant Outlet comme indiqué ci-dessous :

```jsx
├── home.jsx

👉 import { Outlet } from "react-router-dom";

export default function Home() {
return (
    <>
        <main className="">
            <section>
           👉 <Outlet />
            </section>
        </main>
    </>
)
}
```

Votre application devrait ressembler à ceci dans votre navigateur :

![Composant Navbar dans React](https://www.freecodecamp.org/news/content/images/2024/01/Untitled-3.png)

### Comment créer la barre latérale

La `AsideBar` est l'un des composants les plus importants de notre application. C'est ici que les noms des cultures seront affichés. Ce composant fonctionne comme un onglet, et lorsqu'un utilisateur clique dessus, il affiche plus de détails sur la culture qui a été cliquée.

Créez un nouveau composant `./src/components/AsideBar.jsx` et écrivez le code ci-dessous :

```jsx
├── AsideBar.jsx

import { NavLink } from "react-router-dom"
import data from "../apis/data"

export default function AsideBar() {

    const activeStyle = ({isActive}) =>  {
            return {
                backgroundColor : isActive ? "rgb(154 52 18)" : "",
                color : isActive ? "rgb(255 247 237)" : "",
            }
        }

return (
    <>
        <main className="w-[100%] mt-[2em]">
            <section className="w-[100%]">
                <aside className="w-[fit-content] bg-slate-200 rounded-xl">
                    {
                        data.map((data)=>(
                            <ul key={data.id}>
                                <li className="">
                                    <NavLink className="w-[100%] py-3 px-2 inline-block text-slate-800 hover:bg-orange-200 transition-all whitespace-nowrap border-y-4 " to={`content/${data.id}`} style={activeStyle}>
                                        {data.type}
                                    </NavLink>
                                </li>
                            </ul>
                        ))
                    }
                </aside>
            </section>
        </main>
    </>
)
}
```

Dans l'exemple de code ci-dessus, notre code est divisé en deux sections : les `data` et le composant `NavLink`.

- **Les données** : nous avons importé les données depuis `./src/apis/data.js` et nous mappons chaque tableau d'objets et retournons le `data.type` comme noms de la `AsideBar`.
- **Le NavLink** : les données retournées depuis `data.js` sont rendues directement sur le composant `NavLink`. Le composant `NavLink` a deux props spécifiées, les props `style` et `to`. La prop `style` reçoit l'objet `activeStyle` qui indique quel style doit être appliqué à `NavLink` lorsqu'il est actif. La prop `to` `to={`content/${data.id}`}` nous passons le `data.id` comme segment pour correspondre avec le `path` des composants de contenu (*plus sur cela dans la section suivante*). Cela permet au contenu d'être rendu dynamiquement lorsque le `NavLink` est cliqué.

Ensuite, allez dans le composant home et rendez la `AsideBar` comme indiqué ci-dessous :

```jsx
├── home.jsx

 	 import { Outlet } from "react-router-dom";
👉 import AsideBar from "../components/AsideBar";

export default function Home() {
return (
    <>
      👉  <main className="w-[80%] mt-[2em] mx-auto">
            <section>
                <Outlet />
            </section>
            <section>
                <aside>
                 👉 <AsideBar />
                </aside>
            </section>
        </main>
    </>
)
}
```

Votre application devrait ressembler à ceci dans votre navigateur :

![composant aside dans react](https://www.freecodecamp.org/news/content/images/2024/01/aside_component.gif)

En interagissant avec l'`Asidebar`, vous avez peut-être remarqué que la page se casse chaque fois que vous cliquez sur les liens. Cela est dû au fait que le composant de contenu n'est pas encore défini. Alors créons-le.

### Comment créer le composant de contenu

Le composant de contenu rend le contenu qui est lié à un lien particulier qui a été cliqué.

Créez un nouveau composant appelé `./src/components/Content.jsx` et ajoutez le code ci-dessous :

```jsx
├── Content.jsx

import { Link, useParams } from "react-router-dom";
import data from "../apis/data.js";
import { WifiOff } from "react-feather";

export default function Content() {
    const {contentId} = useParams()

    const newData = data.find((data)=> data.id.toString() === contentId)

    if(!contentId){
        return (
            <main className="translate-x-44 translate-y-44">
                <div className="">
                    <WifiOff className="text-slate-400 text-center translate-x-48"/>
                    <p className="text-slate-400">{`Le contenu ne peut pas être accessible ! cliquez sur la navigation de gauche pour recharger`}</p>
                </div>
            </main>
        )
    }

return (
    <>
        <main className="w-[80%] mx-auto mt-8"> 
            <section >
                {
                    newData && (
                        <>  
                            {/* Image Over */}
                            <aside className="h-[6em] w-[100%]">
                                <div className="h-[100%]  w-[100%]">
                                    <img src={newData.imgHeaders} alt="" className="h-[100%]  w-[100%] object-cover rounded-xl"/>
                                </div>
                            </aside>

                            {/* Details */}
                           <section className="flex gap-6">
                           <aside className="w-[50%]">
                                <div>
                                    <p className="bg-orange-500 w-[fit-content] rounded-xl mt-4 py-1 px-2 font-bold">{newData.catagories}</p>
                                    <h1 className="font-light text-4xl my-7">{newData.type}</h1>
                                    <p className="font-bold mb-4 text-2xl">{newData.region}</p>
                                </div>
                                <div>
                                    <p className="font-light">{newData.history}</p>
                                </div>

                                <div className="mt-4">
                                    <span>{`En savoir plus sur`}</span>
                                    <Link to={newData.britannicaLink} target="_blank" className="text-orange-500 py-2 px-2 rounded-md inline mt-4 hover:underline hover:text-black">britannica</Link>
                                </div>
                            </aside>

                            {/* Image Cover */}
                            <aside className="w-[50%]">
                                <div>
                                    <img src={newData.imgCover} alt="" className="rounded-3xl mt-10"/>
                                </div>
                            </aside>
                            </section>
                        
                        </>
                    )
                }
            </section>
        </main>
    </>
  )
}
```

Le code ci-dessus fait ce qui suit :

- **useParams** : nous utilisons le hook [useParams()](https://reactrouter.com/en/main/hooks/use-params) pour retourner les paires clé-valeur du segment dynamique `content/:contentId` spécifié sur la route.
- **newData** : en utilisant la méthode de tableau [find()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find), le premier élément du tableau d'objets est retourné si la condition est vraie, sinon il retourne `undefined`.
- **if(!contentId)** : ici, nous vérifions si le `contentId` ne correspond pas ou n'est pas encore rendu – alors l'élément fourni dans la fonction doit s'exécuter. Cela est très utile pour vérifier les erreurs et dans les situations où le contenu n'est pas disponible.
- **newData &&** : ici, nous parcourons l'objet de données retourné et rendons le contenu de l'API dès que le contenu est chargé. Chaque propriété d'objet est analysée dans un élément à rendre en tant que contenu.

Ensuite, allez dans le composant home et rendez le composant de contenu comme indiqué ci-dessous.

```jsx
├── home.jsx

		import { Outlet } from "react-router-dom";
		import AsideBar from "../components/AsideBar";
👉 import Content from "../components/Content";

export default function Home() {
return (
    <>
        <main className="w-[80%] mt-[2em] mx-auto">
            <section>
                <Outlet />
            </section>
            
            <section className="flex">
                <aside>
                    <AsideBar />
                </aside>

                <aside>
              👉 <Content />
                </aside>
            </section>
        </main>
    </>
)
}
```

Ensuite, configurez la route vers un segment dynamique :

```jsx
├── home.jsx

	 import Home from './pages/home';
	 import Navbar from './components/navbar';
👉 import Content from './components/Content';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route  path='/' element={<Home />}>
       <Route path='/' element={<Navbar />}> 
       👉 <Route path='content/:contentId' element={<Content />} />
      </Route>
    </Route>
  )
)

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
```

Votre application devrait ressembler à ceci dans votre navigateur :

![composant de contenu dans react.js](https://www.freecodecamp.org/news/content/images/2024/01/cotent_component-1-1.gif)

En cliquant sur la `Asidebar`, le contenu de l'API sera chargé et rendu sur la même page que la `Asidebar`.

## Résumé

Dans ce tutoriel, nous avons appris les segments dynamiques dans React Router. Nous avons parlé de ce qu'est le routeur dynamique et de la manière dont il diffère du routage statique. Vous avez également appris à utiliser le hook `useParams` pour activer les segments dynamiques, ainsi que la manière de définir votre chemin lors de la récupération de données depuis une API.

Ensuite, nous avons construit un nouveau projet qui a rendu dynamiquement un nouveau contenu sur la même page lorsque l'utilisateur a cliqué sur la barre latérale.

Vous pouvez prendre ce projet plus loin et le rendre vôtre en implémentant plus de fonctionnalités.