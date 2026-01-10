---
title: Comment utiliser React Router pour créer des applications monopage
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-07-18T14:42:16.000Z'
originalURL: https://freecodecamp.org/news/use-react-router-to-build-single-page-applications
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Using-React-Router-to-build-SPAs--Twitter-Post-.png
tags:
- name: react router
  slug: react-router
- name: ' Single Page Applications '
  slug: single-page-applications
seo_title: Comment utiliser React Router pour créer des applications monopage
seo_desc: 'Single Page Applications (SPAs) have revolutionized web development. They
  offer a more dynamic and fluid user experience compared to traditional multi-page
  applications.

  Traditional web apps require full-page reloads for almost every click the user m...'
---

Les applications monopage (SPA) ont révolutionné le développement web. Elles offrent une expérience utilisateur plus dynamique et fluide par rapport aux applications multipages traditionnelles.

Les applications web traditionnelles nécessitent un rechargement complet de la page pour presque chaque clic de l'utilisateur. Les SPA, en revanche, chargent une seule page HTML et mettent à jour le contenu de la page dynamiquement lorsque les utilisateurs interagissent avec l'application. Ce dynamisme imite le comportement des applications de bureau et entraîne des interactions plus réactives.

### Avant d'aller plus loin :

Pour suivre ce que je vais discuter dans cet article, vous devez avoir quelques connaissances de base sur React et sur la façon de configurer un projet React. Si vous les avez déjà, commençons.

## Qu'est-ce que React Router et React Router DOM ?

React Router est une bibliothèque puissante qui gère la navigation et le routage dans les applications React. React Router DOM est utilisé spécifiquement pour les applications web et possède quelques API spécifiques au DOM.

Alors que nous plongeons dans le monde de React Router DOM, nous explorerons ses concepts fondamentaux tout en démontrant leur mise en œuvre dans une application React. Notre objectif sera de construire un système de navigation simple avec des liens vers différents composants, illustrant comment configurer les routes, gérer la correspondance des routes et implémenter la navigation.

À la fin de cet article, vous aurez une compréhension solide de l'utilisation de React Router DOM pour créer des expériences de navigation dynamiques et fluides dans vos applications monopage.

## Comment installer React Router

Comme je l'ai expliqué ci-dessus, React-router-DOM est utilisé exclusivement pour intégrer des fonctionnalités de routage dans les applications web. Ainsi, pour l'utiliser dans votre application React, vous devez installer le package `react-router-dom` en exécutant cette commande dans le terminal de votre application React :

```react
npm install react-router-dom

```

Après l'avoir installé avec succès, vous pouvez maintenant commencer le routage dans votre projet React.

## Concepts de base dans React Router DOM

### BrowserRouter

BrowserRouter est un composant parent qui contient tous les composants de route. Toutes les routes que vous utilisez dans une application doivent être déclarées dans le `BrowserRouter`. Plus important encore, il stocke l'emplacement actuel dans la barre d'adresse du navigateur en utilisant des URL, ce qui est utile lors de la navigation.

Pour utiliser BrowserRouter, vous devez l'importer depuis `react-router-dom` dans votre fichier App.jsx.

```react
import { BrowserRouter } from "react-router-dom";

function App() {
  
  return (
    <BrowserRouter>
    
    </BrowserRouter>
  );
}

export default App;
```

Le `BrowserRouter` a un attribut `basename` utilisé pour définir l'URL de base pour toutes les routes dans une application. C'est important si votre application est hébergée dans un sous-répertoire d'un domaine.

```
<BrowserRouter basename="/boutique">

</BrowserRouter>
```

L'ajout de `/boutique` comme basename garantira que tous les chemins de route sont relatifs à `/boutique`.

### Routes

Ce composant est un remplacement direct de `switch` qui était utilisé dans les versions précédentes de React Router. Il agit également comme un parent et rend la première route enfant correspondante, ce qui garantit que le composant correct est affiché en fonction de l'URL actuelle.

Pour déclarer des routes, importez `routes` depuis `react-router-dom` et positionnez-le dans le composant `BrowserRouter`.

```react
import { BrowserRouter, Routes } from "react-router-dom";

function App() {
  
  return (
    <BrowserRouter>
    	<Routes>
        
        </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### Route

`Route` est un composant enfant qui se compose de deux attributs : **path** et **element**. Un **path** peut être n'importe quel nom de chemin spécifié tandis que l'attribut **element** est le composant qui doit être rendu. Une route rend un composant spécifique lorsque le chemin spécifié correspond à une URL.

Une application peut avoir autant de `route`s que nécessaire, et elles doivent toutes être déclarées à l'intérieur du composant `Routes`. En supposant que nous avons un composant `<Home\>` et `<Tarification\>`, nous devrons importer le composant `Route` et le positionner dans les `Routes`.

```react
import { BrowserRouter, Routes, Route } from "react-router-dom";

//TOUTES LES IMPORTATIONS DE COMPOSANTS VIENNENT ICI

function App() {
  
  return (
    <BrowserRouter>
    	<Routes>
        	<Route path="/" element={<Home/>}/>
            	<Route path="tarification" element={<Tarification/>}/>
        </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### Routes non déclarées

Il existe un moyen de gérer les routes qui n'existent pas dans votre application, comme une page d'erreur 404. Pour ce faire, créez un autre composant portant un message "Non trouvé" et ajoutez la `route`.

Définissez le nom du chemin sur `*` et passez le composant comme **element**.

```
import { BrowserRouter, Routes, Route } from "react-router-dom";

//TOUTES LES IMPORTATIONS DE COMPOSANTS VIENNENT ICI

function App() {
  
  return (
    <BrowserRouter>
    	<Routes>
        	<Route path="/" element={<Home/>}/>
            	<Route path="tarification" element={<Tarification/>}/>
                <Route path="*" element={<PageNonTrouvee/>}/>
        </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### Routes imbriquées

Dans certains cas, les routes peuvent avoir des enfants ou des sous-routes.

```
import { BrowserRouter, Routes, Route } from "react-router-dom";

//TOUTES LES IMPORTATIONS DE COMPOSANTS VIENNENT ICI

function App() {
  
  return (
    <BrowserRouter>
    	<Routes>
        	<Route path="/" element={<Home/>}/>
            	<Route path="tarification" element={<Tarification/>}/>
                <Route path="categories" element={<Categories/>}>
                	<Route path="homme" element={<Homme/>}/>
                    	<Route path="femme" element={<Femme/>}/>
                </Route>
                <Route path="*" element={<PageNonTrouvee/>}/>
        </Routes>
    </BrowserRouter>
  );
}

export default App;
```

Lors de la navigation vers les éléments imbriqués, l'URL dans le navigateur sera quelque chose comme `/categories/homme` et `/categories/femme`.

### Link

Cela agit comme un attribut `href` d'ancre. Il a un attribut **to** qui spécifie où le `Link` emmènera l'utilisateur après un clic. Habituellement, c'est le chemin vers la page d'un composant qui est passé à l'attribut **to**. 

Les liens sont généralement placés dans un composant Navbar, nous allons donc placer deux liens qui pointent vers les chemins des composants dans nos routes déjà déclarées.

```react
import { Link } from "react-router-dom";
export default function PageNav() {
  return (
  <>
        <Link to="/">Accueil</Link>
        <Link to="tarification">Tarification</Link>
  </>
  );
}

```

**NB :** Si vous pratiquez en lisant cet article, il est important de noter que le composant `PageNav` créé ici doit être situé dans votre **App.jsx** et spécifiquement juste après la balise d'ouverture `BrowserRouter` avant les Routes. Cela garantit que `PageNav` reste toujours en haut comme un menu de navigation malgré le routage à travers différents composants.

```
import { BrowserRouter, Routes, Route } from "react-router-dom";

//TOUTES LES IMPORTATIONS DE COMPOSANTS VIENNENT ICI

function App() {
  
  return (
    <BrowserRouter>
    	<PageNav/>
    	<Routes>
        	<Route path="/" element={<Home/>}/>
            	<Route path="tarification" element={<Tarification/>}/>
                <Route path="categories" element={<Categories/>}>
                	<Route path="homme" element={<Homme/>}/>
                    	<Route path="femme" element={<Femme/>}/>
                </Route>
                <Route path="*" element={<PageNonTrouvee/>}/>
        </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### NavLink

NavLink remplit la même fonction que `Link` et possède également un attribut **to**. Mais il est différent car il a un attribut de classe. Les attributs de classe sont `active`, `isPending` et `isTransitioning`. Cela le rend plus polyvalent que `Link` et vous pouvez l'utiliser pour ajouter conditionnellement des styles lors des interactions utilisateur.

```
import { NavLink } from "react-router-dom";
export default function PageNav() {
  return (
  	<>
        <NavLink to="/">Accueil</NavLink>
        <NavLink to="tarification">Tarification</NavLink>
    </>
  );
  }
```

### Outlet

Avoir des éléments enfants à l'intérieur d'un élément de route parent signifie qu'il y a une couche d'abstraction dans le rendu de l'interface utilisateur des routes enfants. C'est là que le composant `Outlet` entre en jeu. Vous l'ajoutez à la route parente – dans notre exemple, ce serait le composant `Categories`.

```react
import { NavLink, Outlet } from "react-router-dom";
export default function Categories() {
  return (
 <>
          <NavLink to="homme">
            Homme
          </NavLink>
          <NavLink to="femme">
            Femme
          </NavLink>
      <Outlet />
</>
  );
}
```

Cela permet le rendu de l'interface utilisateur des routes enfants dans la route imbriquée.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/nested-routes.PNG)
_Image montrant les routes imbriquées enfants dans la route Categories_

### Hook `useNavigate`

Ce hook retourne une fonction qui permet la navigation programmatique entre les routes.

Il existe plusieurs façons d'utiliser la fonction navigate dans votre application. Tout d'abord, nous devons importer le hook `useNavigate` et l'initialiser comme **navigate**.

```
import { useNavigate } from "react-router-dom";

export default function Homepage() {
  const navigate = useNavigate();

  return (
    <>
      <h1>Ceci est la page d'accueil</h1>
 
 
    </>
  );
}
```

Nous pouvons utiliser navigate de plusieurs façons dans notre application :

* En l'attachant à un bouton via la prop `onClick` avec le chemin souhaité à naviguer, passé à la fonction navigate.

```react
 <button onClick={() => navigate("/categories")}>Aller aux catégories</button>
```

* En l'utilisant avec un composant `Link`.

```react
<Link to={navigate("/categories")}>Aller aux catégories</Link>
```

* En utilisant un nombre au lieu du chemin du composant dans la fonction **navigate**. Le nombre doit spécifier le nombre de navigations en arrière dans la pile d'historique où vous souhaitez aller.

```react
<Link to={navigate(-1)}>Revenir d'un pas en arrière</Link>
```

### Hook `useParams`

Retourne un objet des `params` dynamiques obtenus à partir de l'URL actuelle correspondante au chemin de la Route. Les routes parentes transmettent tous les `params` à leurs routes enfants.

L'exemple ci-dessous montre un composant `OrderPage` qui sera rendu pour chaque `customer` avec leur `id` unique. Lorsque l'URL correspond à `/customer/123`, `:id` sera `123`.

```react
import { useParams } from "react-router-dom";

function App() {
  const {id} = useParams()
  return (
    <BrowserRouter>
    	<Routes>
        <Route path="customer">
        	<Route path=":id" element={<OrderPage/>}/>
           </Route>
        </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### Résultat final

À ce stade, nous avons entièrement implémenté React Router dans notre petit projet de navigation. Voici à quoi cela ressemble en plein flux :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Untitled-design.gif)

Pour plus d'informations détaillées et de concepts sur React Router, vous pouvez visiter le site de la [documentation officielle de React Router](https://reactrouter.com/).

## Conclusion

Dans cet article, nous avons exploré les concepts et la mise en œuvre du routage côté client (CSR) dans une application web React. React Router, grâce à sa bibliothèque centrée sur le web React-Router-DOM, permet le CSR, permettant aux applications de mettre à jour l'URL avec un clic sur un lien sans faire de demande au serveur pour un nouveau document.

Cette fonctionnalité améliore l'expérience utilisateur en fournissant une navigation plus rapide et une interaction plus fluide au sein de l'application. En tirant parti du CSR, les développeurs peuvent construire des applications monopage (SPA) plus efficaces et réactives, améliorant ainsi les performances et la satisfaction des utilisateurs.

Si vous avez aimé lire cet article, vous pouvez [m'offrir un café](https://buymeacoffee.com/timothyolanrewaju).

Vous voulez voir plus de contenu comme celui-ci ? Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750/).

À la prochaine !

Bon codage !