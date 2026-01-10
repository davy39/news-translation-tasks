---
title: Comment utiliser les URLs pour la gestion d'état dans React
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2023-10-06T17:50:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-urls-for-state-management-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Article-Cover.png
tags:
- name: React
  slug: react
- name: routing
  slug: routing
- name: 'State Management '
  slug: state-management
- name: url
  slug: url
seo_title: Comment utiliser les URLs pour la gestion d'état dans React
seo_desc: 'For years, URLs have been synonymous with web navigation. But the tide
  is turning, especially with the emergence of single-page applications. In the React
  universe, URLs are stepping up to play a pivotal role in state management.

  This article will gu...'
---

Pendant des années, les URLs ont été synonymes de navigation web. Mais les choses changent, surtout avec l'émergence des applications monopages. Dans l'univers React, les URLs jouent un rôle pivot dans la gestion d'état.

Cet article vous guidera à travers le parcours transformateur des URLs en tant que gestionnaires d'état dans le contexte des applications React.

### Prérequis

* Fondamentaux de HTML et CSS
* Fondamentaux de JavaScript ES6
* Fondamentaux de React, React Router et React Hooks.

## L'évolution de la gestion d'état dans React

Faisons un voyage dans le passé :

* **setState** : Dans les premiers jours de React, beaucoup s'appuyaient sur l'état des composants, surtout dans les [composants de classe](https://react.dev/reference/react/Component#defining-a-class-component). C'était simple pour gérer les données spécifiques aux composants. Mais ce n'était pas idéal pour les applications plus grandes.
* **Redux & MobX** : À mesure que les applications devenaient plus complexes, des outils comme [Redux](https://redux.js.org/) et [MobX](https://mobx.js.org/README.html) ont émergé. Ils ont centralisé la gestion des données, rendant plus facile la manipulation des données à l'échelle de l'application.
* **Context API & Hooks** : L'[API de contexte](https://react.dev/reference/react/useContext) de React, combinée à l'avènement des hooks, a apporté une manière plus native de gérer l'état global sans ajouter de bibliothèques supplémentaires.

## Gérer l'état avec les URLs

Au premier abord, utiliser une URL pour gérer l'état peut sembler inhabituel. Mais en explorant davantage, vous découvrirez plusieurs avantages clairs :

* **Sauvegardez votre place** : En gardant l'état dans l'URL, votre page web se souvient de votre place. Ainsi, si vous marquez une page, elle aura la même apparence lorsque vous y reviendrez plus tard.
* **Partage facile** : Si vous regardez quelque chose de spécifique sur une page, comme un produit ou un graphique, vous pouvez partager l'URL. Toute personne qui clique dessus verra exactement ce que vous voyez, rendant la collaboration un jeu d'enfant.
* **Dépannage facilité** : Les développeurs peuvent trouver et corriger les problèmes plus rapidement car l'URL montre l'état de l'application. Ils peuvent voir les problèmes simplement en cliquant sur le lien partagé.

En résumé, l'utilisation des URLs de cette manière aide à garder votre place, à partager des vues spécifiques et rend la résolution de problèmes plus fluide pour les développeurs.

## Comment implémenter la gestion d'état basée sur les URLs

Considérant la taille de cette section, voici tout ce que vous allez apprendre.

1. Comment configurer l'environnement
2. Nettoyer l'encombrement
3. Analyse du projet
4. Installer les dépendances nécessaires
5. Comment récupérer les données et concevoir l'interface utilisateur
6. Comment stocker l'état dans l'URL
7. Comment lire l'état stocké dans l'URL
8. Comment personnaliser la page produit

### Comment configurer l'environnement

Ouvrez votre terminal intégré ou le terminal de votre éditeur de code (de préférence) et exécutez la commande suivante :

```bash
npm create vite@latest
```

Cette commande utilise [Vite](https://vitejs.dev/guide/) (un outil léger utilisé pour construire des applications web rapides et optimisées) pour échafauder un environnement d'application web. Naviguez vers le bas en utilisant les touches fléchées et sélectionnez React.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/02-Selecting-React.png)
_Sélection de React depuis la configuration Vite_

Ensuite, sélectionnez votre combinaison de langage préférée – j'utiliserai du JS simple.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/03-Selecting-JS.png)
_Sélection du langage dans React_

Ensuite, déplacez-vous dans votre dossier React en utilisant la commande cd "nom-du-projet" et exécutez `npm install` pour installer toutes les dépendances du projet.

Enfin, démarrez le serveur de développement en exécutant `npm run dev` et allez à l'URL respective ([http://localhost:5173/](http://localhost:5173/)).

![Image](https://www.freecodecamp.org/news/content/images/2023/10/04-dev-server-running.png)
_Serveur de développement en cours d'exécution_

### Nettoyer l'encombrement

Assurez-vous de vider le contenu de tous les fichiers CSS et supprimez le fichier `App.css` car vous n'aurez besoin que d'un seul fichier de style. Ensuite, videz le contenu du composant `App` et remplacez-le par un contenu JSX basique.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/05-clutter-cleared.png)
_Encombrement nettoyé dans l'environnement de développement_

Cela retourne une page claire sur votre serveur local qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/06-clear-server-page.png)
_Page du serveur claire_

### Analyse du projet

Le projet implique de récupérer des données depuis une API et de persister ces données globalement via l'URL pour qu'elles soient accessibles à travers de nombreux composants/pages.

Un exemple concret est lorsque vous êtes sur votre site de commerce électronique préféré, vous pouvez voir ce gadget cool et vouloir le partager avec votre ami.

Vous partagez généralement le lien depuis le navigateur vers les messages directs de votre ami sur les réseaux sociaux, qu'il peut utiliser pour voir le même produit sans aucun problème en ouvrant le lien que vous lui avez envoyé.

Voici un aperçu du projet que nous allons construire : 😉

![Image](https://www.freecodecamp.org/news/content/images/2023/10/1-sneaky-peek.gif)
_Aperçu du projet complet_

Intrigué ? 🌚 Plongeons alors.

### Installer les dépendances nécessaires

Avant de mettre quoi que ce soit sur la page, vous devez d'abord configurer complètement votre environnement de développement avec les dépendances nécessaires.

* [json-server](https://www.npmjs.com/package/json-server) : Ce package héberge vos données sur un serveur local, vous permettant de les récupérer comme une API externe.
* [react-router](https://www.npmjs.com/package/react-router) : Ce package permet à React de créer des SPAs qui permettent de naviguer sans rafraîchir la page.

```bash
npm i json-server react-router-dom
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/08-installing-dependencies-1.png)
_Installation des dépendances_

* Ensuite, téléchargez les données JSON depuis ce [GitHub(json-data)](https://github.com/Daiveedjay/URL-State-Management/tree/main/data), et les assets depuis ce [GitHub(assets-data)](https://github.com/Daiveedjay/URL-State-Management/tree/main/public/assets).

Maintenant, créez un dossier data dans votre répertoire de projet racine et placez le fichier JSON à l'intérieur. Ensuite, créez un dossier assets dans votre répertoire public et placez toutes les images dans ce dossier assets.

Votre structure de dossier actuelle devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/07-folder-structure-after-downloading-files.png)
_Structure de dossier après le téléchargement des fichiers_

Ensuite, modifiez votre fichier package.json en ajoutant un script qui démarre le json-server

```json
"server": "json-server --watch data/products.json --port 9000 "
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/09-adding-a-server-script.png)
_Ajout d'un script de serveur à package.json_

Après cela, ouvrez votre terminal et démarrez le serveur avec `npm run server` :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/10-starting-data-server.png)
_Démarrage du serveur de données_

Avec cela, votre serveur est en cours d'exécution et le contenu de votre fichier JSON peut être accessible via l'URL fournie.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/11-data-on-browser.png)
_Données dans le navigateur_

Ps : Si vous souhaitez visualiser les fichiers JSON dans le navigateur comme je le fais, téléchargez l'extension de navigateur – [JSON Viewer](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh).

### Comment récupérer les données et concevoir l'interface utilisateur

Commencez par créer un composant HomePage et importer-le dans le composant App. Ce composant contiendra toutes les données de la première page que vous avez vue précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/12-importing-the-homepage.png)
_Importation de la page d'accueil_

Dans le composant `HomePage`, utilisez un hook `useEffect` pour récupérer toutes les données de votre API locale.

```js
import { useEffect } from "react";

export default function HomePage() {
  useEffect(function () {
    async function fetchData() {

      try{
      const res = await fetch("http://localhost:9000/products");
      const clothesData = await res.json();
      console.log(clothesData);   
      }
      catch (error) {  console.log(error);}
      }
    fetchData();
  }, []);

  return (
    <main className="homepage">
      <h1>Page d'accueil de ma page produit fictive</h1>
    </main>
  );
}

```

Pour l'instant, vous pouvez déjà voir les données récupérées dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/13-evidence-of-fetching-data.png)
_Preuves de la récupération des données_

Ensuite, stockez vos données dans un état en utilisant le hook `useState` et remplissez votre interface avec ces données.

```js
import { useEffect, useState } from "react";

export default function HomePage() {
  const [products, setProducts] = useState([]);

  useEffect(function () {
    async function fetchData() {
      try {
        const res = await fetch("http://localhost:9000/products");
        const clothesData = await res.json();
        console.log(clothesData);
        // Le stockage se fait ici
        setProducts(clothesData);
      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, []);

  return (
    <main className="homepage">
      <h1>Page d'accueil de ma page produit fictive</h1>
      <div className="products__list">
        {products.map((product) => (
          <div
            key={product.id}
                      className="product__item"
          >
            <img loading="lazy" src={product.imageUrl} alt="" />
            <h2>{product.itemName}</h2>
          </div>
        ))}
      </div>
    </main>
  );
}
```

Tous les styles nécessaires dans ce projet se trouvent dans ce [fichier CSS](https://github.com/Daiveedjay/URL-State-Management/blob/main/src/index.css). Alternativement, vous pouvez coller ces styles dans votre index.css, ce qui donne le même résultat.

```css
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&display=swap");

*,
::before,
::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html {
  font-size: 62.5%;
}
body {
  font-family: "Nunito", sans-serif;
}

h1 {
  text-align: center;
  font-weight: 700;
  font-size: 3rem;

  & span {
    cursor: pointer;
    margin-right: 3rem;
  }
}

a,
h3 {
  text-decoration: none;
  color: #a04000;
}

img {
  width: 100%;
  display: block;
  transition: all ease-in 0.3s;
}

.homepage {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 1rem;
  flex-direction: column;
  gap: 3rem;

  & > * {
    width: 100%;
  }
}

.products__list {
  column-count: 1;
  column-gap: 2rem;
  padding: 2rem;

  & > * {
    break-inside: avoid;
    margin-bottom: 2rem;
  }

  & .product__item {
    border-radius: 1rem;
    overflow: hidden;
    display: block;
    position: relative;
    transition: all ease-in 0.3s;

    & h2 {
      background: #fff;
      bottom: 5px;
      left: 5px;
      padding: 0.5rem 1rem;
      border-radius: 5px;
      z-index: 2;
      position: absolute;
      transition: all ease-in 0.3s;
    }

    &:hover img {
      scale: 1.1;
    }

    &:hover h2 {
      transform: translate(10px, -10px);
    }
  }
}

.single__product {
  display: flex;
  flex-direction: column;
  padding: 2rem;
  gap: 4rem;
  border-radius: 1rem;
  overflow: hidden;

  & section {
    display: flex;
    justify-content: center;
    flex-direction: column;

    & figure {
      border-radius: 1rem;
      overflow: hidden;

      & .product__img {
        width: 100%;
      }
    }

    & aside {
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 1.5rem;

      & > h2 {
        font-size: 2.5rem;
      }
      & > h3 {
        font-size: 1.6rem;
      }
      & span {
        background: rgba(160, 64, 0, 0.5);
        padding-inline: 1rem;
        align-self: flex-start;
      }
    }
  }
}

/* Petits appareils (tablettes en portrait et grands téléphones, 600px et plus) */
@media only screen and (min-width: 600px) {
  .products__list {
    column-count: 2;
  }

  .single__product {
    & section {
      flex-direction: row;

      & .product__img {
        max-width: 300px;
      }
    }
  }
}

/* Appareils moyens (tablettes en paysage, 768px et plus) */
@media only screen and (min-width: 768px) {
  .homepage {
    padding: 2rem 4rem;
  }
  .products__list {
    column-count: 3;
  }
}
```

Pour l'instant, votre page d'accueil devrait déjà ressembler à la version de démonstration.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/14-page-with-styings-applied.png)
_Page d'accueil avec les styles ajoutés_

### Comment stocker l'état dans l'URL

Afin de gérer et de partager l'état à travers plusieurs pages en utilisant l'URL, vous devez d'abord définir des routes en utilisant le package react-router.

Commencez par créer une route pour la page d'accueil :

```js
import { BrowserRouter, Route, Routes } from "react-router-dom";

import HomePage from "./HomePage";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<HomePage />} />
      </Routes>
    </BrowserRouter>
  );
}
```

* Le composant **BrowserRouter** enveloppe votre application entière ou la partie de votre application où vous souhaitez utiliser le routage.
* Le composant **Routes** enveloppe tous vos composants **Route** et est responsable du rendu de la première route qui correspond à l'emplacement actuel.
* Le composant **Route** représente une seule route dans votre application.

Ensuite, créez un composant `ProductItem` responsable de l'affichage d'un seul élément et sa route équivalente.

```js
import { BrowserRouter, Route, Routes } from "react-router-dom";

import HomePage from "./Homepage";
import ProductItem from "./ProductItem";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<HomePage />} />
         <Route path="product" element={<ProductItem />} />
      </Routes>
    </BrowserRouter>
  );
}

```

Pour voir le composant `ProductItem`, rendez-vous sur votre `HomePage` et enveloppez chaque produit individuel avec un élément `Link` pointant vers la page produit avec leur ID unique.

```js
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function HomePage() {
  const [products, setProducts] = useState([]);

  useEffect(function () {
    async function fetchData() {
      const res = await fetch("http://localhost:9000/products");

      const clothesData = await res.json();
      console.log(clothesData);
      setProducts(clothesData);
    }
    fetchData();
  }, []);

  return (
    <main className="homepage">
      <h1>Page d'accueil de ma page produit fictive</h1>
      <div className="products__list">
        {products.map((product) => (
          <Link
            key={product.id}
           // Aller à la page produit
           to={`/product?id=${product.id}`}
            className="product__item"
          >
            <img loading="lazy" src={product.imageUrl} alt="" />
            <h2>{product.itemName}</h2>
          </Link>
        ))}
      </div>
    </main>
  );
}
```

En cliquant sur un produit, vous êtes maintenant redirigé vers la page produit et voyez le composant `ProductItem`.

En observant de plus près, vous pouvez remarquer que l'id de chaque élément est ajouté à l'URL via sa propriété id (par exemple : product?id=12345678). Cela implique que vous avez réussi à stocker l'état de l'id dans l'URL.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/02-confirming-id-state-shared.gif)

### Comment lire l'état stocké dans l'URL

Afin d'afficher les données pour chaque produit, vous devez lire l'état stocké dans l'URL.

Pour implémenter cela, commencez par créer un nouveau hook personnalisé (cela aide pour la réutilisabilité). Dans votre hook personnalisé, importez le hook `useSearchParams`.

```js
import { useSearchParams } from "react-router-dom";

export function useURLID() {
  const [searchParams] = useSearchParams();
}
```

Le hook `useSearchParams` vous permet d'interagir avec les paramètres de requête de l'URL (la partie de l'URL qui vient après le ? comme vous l'avez vu dans votre URL précédemment).

Afin de récupérer les valeurs de l'URL, utilisez la méthode `get` et passez le nom de la valeur que vous souhaitez récupérer, dans ce cas, l'`id`.

```js
import { useSearchParams } from "react-router-dom";

export function useURLID() {
  const [searchParams] = useSearchParams();
  const id = searchParams.get("id");
  return { id };
}
```

Pour tester votre hook, importez-le dans la page `ProductItem` et extrayez les valeurs.

```js
import { useURLID } from "./useURLID";

export default function ProductItem() {
  const { id } = useURLID();
  return <div>Product Item {id}</div>;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/2-confirming-id-state-shared.gif)

Et voilà ! Votre état d'id est maintenant global et peut être utilisé par n'importe quel composant de votre application. Bravo !

### Comment personnaliser la page produit

Afin de réaliser pleinement ce qui a été montré dans la démonstration, effectuez une autre récupération basée sur l'id pour obtenir les données de ce produit.

Commencez par créer des états pour stocker les données et tenir compte du chargement des données.

```js
const [singleProduct, setSingleProduct] = useState({});
const [loading, setLoading] = useState(false);
```

Ensuite, utilisez un hook `useEffect` pour récupérer et stocker les données basées sur l'id unique du produit.

```js
  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      try {
        const res = await fetch(`http://localhost:9000/products/${id}`);

        const data = await res.json();

        setSingleProduct(data);
      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [id]);
```

Ensuite, utilisez les données reçues pour remplir l'interface.

```js
import { useEffect, useState } from "react";
import { useURLID } from "./useURLID";


export default function ProductItem() {
  const { id } = useURLID();
  const [singleProduct, setSingleProduct] = useState({});
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      try {
        const res = await fetch(`http://localhost:8000/products/${id}`);

        const data = await res.json();

        setSingleProduct(data);
      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [id]);



  // Si chargement, afficher la div de chargement
  if (loading) return <div>Chargement...</div>;

  // Si pas de chargement, afficher les détails du produit
  return (
    <div className="single__product">
      <h1>
               <span>
          {singleProduct.itemName} Page id: {id}
        </span>
      </h1>
      <section>
        <figure className="product__img-container">
          <img
            className="product__img"
            src={singleProduct.imageUrl}
            alt="Image"
          />
        </figure>
        <aside>
          <h2>{singleProduct.itemName}</h2>
          <h3>{singleProduct.notes}</h3>
          <h4>
            Catégorie: <span>{singleProduct.type}</span>
          </h4>
          <p>
            Largeur: <strong>{singleProduct?.size?.width}</strong>
          </p>
          <p>
            Longueur: <strong>{singleProduct?.size?.length}</strong>
          </p>
        </aside>
      </section>
    </div>
  );
}
```

Enfin, prévoyez une navigation facile en fournissant un bouton de retour pour aller à la page d'accueil. Vous pouvez faire cela en utilisant le hook `useNavigate` dans react-router. Ce hook fournit une fonction qui vous permet de naviguer de manière programmatique vers d'autres parties de votre application.

Il suffit d'importer le hook `useNavigate`, et de l'initialiser avec une variable comme ceci :

```js
import { useNavigate } from "react-router-dom";
const navigate = useNavigate();
```

Ensuite, appelez cette fonction avec un gestionnaire d'événements, et passez la route de la page d'accueil.

```js
import { useEffect, useState } from "react";
import { useURLID } from "./useURLID";
import { useNavigate } from "react-router-dom";

export default function ProductItem() {
  const { id } = useURLID();
  const [singleProduct, setSingleProduct] = useState({});
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      try {
        const res = await fetch(`http://localhost:9000/products/${id}`);

        const data = await res.json();

        setSingleProduct(data);
      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [id]);

  const navigate = useNavigate();

  // Si chargement, afficher la div de chargement
  if (loading) return <div>Chargement...</div>;

  // Si pas de chargement, afficher les détails du produit
  return (
    <div className="single__product">
      <h1>
       // Naviguer vers la page d'accueil
        <span onClick={() => navigate("/")}>🔙 </span>
        <span>
          {singleProduct.itemName} Page id: {id}
        </span>
      </h1>
      <section>
        <figure className="product__img-container">
          <img
            className="product__img"
            src={singleProduct.imageUrl}
            alt="Image"
          />
        </figure>
        <aside>
          <h2>{singleProduct.itemName}</h2>
          <h3>{singleProduct.notes}</h3>
          <h4>
            Catégorie: <span>{singleProduct.type}</span>
          </h4>
          <p>
            Largeur: <strong>{singleProduct?.size?.width}</strong>
          </p>
          <p>
            Longueur: <strong>{singleProduct?.size?.length}</strong>
          </p>
        </aside>
      </section>
    </div>
  );
}
```

Tester votre résultat final donne maintenant ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/final-take-1.gif)
_Prise finale montrant toutes les fonctionnalités_

## Exemples concrets

* **Plateformes de commerce électronique** : Pensez à des sites comme Amazon. Ils utilisent des URLs pour vous permettre de partager des recherches de produits spécifiques ou des paramètres. Grâce à cela, les gens peuvent facilement partager leurs articles préférés ou leurs listes de courses avec des amis.
* **Outils de données** : Des outils comme [Tableau](https://www.tableau.com/) sauvegardent vos vues personnalisées dans l'URL. Cela signifie que les équipes peuvent partager des images de données spécifiques entre elles, rendant les discussions, les présentations et les décisions plus rapides et plus claires.

### Informations supplémentaires

Je voudrais souligner quelques points dans l'article qui n'ont pas été mis en évidence.

* Le CSS utilisé contient [l'imbrication CSS native](https://developer.chrome.com/articles/css-nesting/) qui n'est pas entièrement supportée par tous les navigateurs, donc si vous remarquez des irrégularités dans l'interface utilisateur, cela peut provenir du navigateur que vous utilisez. N'hésitez pas à passer à un navigateur comme Google Chrome pour un meilleur support ou vérifiez la compatibilité du navigateur avec un outil comme [CanIUse](https://caniuse.com/) et ajoutez des polyfills à votre code.
* Si cet article a abordé des choses qui étaient un peu compliquées pour vous (comment fonctionne le routage), n'hésitez pas à consulter cet article sur les [Animations de routage](https://www.freecodecamp.org/news/improve-user-experience-in-react-by-animating-routes-using-framer-motion/) pour une meilleure compréhension.
* Si vous êtes intéressé par le code complet, voici le dépôt, [GitHub](https://github.com/Daiveedjay/URL-State-Management), et la version live est ici. [Démo](https://free-code-camp-url-state-manangement.netlify.app/)
* En tant que fonctionnalité ajoutée, j'ai rendu le code entièrement réactif pour toute personne intéressée à créer des grilles en maçonnerie pour des projets futurs, santé !🍷

## Conclusion

La gestion d'état dans React a évolué, avec l'état basé sur les URLs émergent comme une solution remarquable. Cette méthode non seulement simplifie la gestion d'état, mais favorise également la collaboration et la transparence entre les utilisateurs et les développeurs.

Alors, la prochaine fois que vous serez en ligne et penserez à partager des données via une URL, rappelez-vous que vous avez les outils pour implémenter cette fonctionnalité vous-même 😉. C'est une incitation pour les développeurs à explorer le potentiel inexploité des URLs dans la gestion d'état.

### Informations de contact

Vous voulez me contacter ou me connecter ? N'hésitez pas à me contacter sur les plateformes suivantes :

* Twitter / X : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : [Jajadavidjid@gmail.com](mailto:Jajadavidjid@gmail.com)