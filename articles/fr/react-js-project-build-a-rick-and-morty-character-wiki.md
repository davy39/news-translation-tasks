---
title: Projet ReactJS – Construire un Wiki des Personnages de Rick et Morty
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-11-22T19:13:34.000Z'
originalURL: https://freecodecamp.org/news/react-js-project-build-a-rick-and-morty-character-wiki
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/FCC.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
- name: React
  slug: reactjs
seo_title: Projet ReactJS – Construire un Wiki des Personnages de Rick et Morty
seo_desc: 'Today we''re gonna practice our React JS skills by building a Rick and
  Morty Character Wiki.

  Here''s what we''ll build today:


  Here''s a [live demo of the project] 👇

  https://react-projects-psi.vercel.app/.

  And here''s the GitHub Repository.

  The topics we...'
---

Aujourd'hui, nous allons pratiquer nos compétences en **React JS** en construisant un Wiki des Personnages de Rick et Morty.

Voici ce que nous allons construire aujourd'hui :

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cufjzu9x8i7iuxmttzyf.png)

Voici une [démo en direct du projet] 👍
https://react-projects-psi.vercel.app/.

Et [voici le Dépôt GitHub](https://github.com/JoyShaheb/React-Projects/tree/main/Level-1/rick-morty-wiki).

Les sujets que nous allons couvrir lors de la construction de ce projet sont :

- React Hooks (useState, useEffect)
- Composants React
- Fetch API
- Bootstrap - pour le style
- Pagination
- Barre de recherche
- Filtrage des données
- Routage dynamique

## Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/35QCQnohLg8]

## Fonctionnalités du projet

Regardons une démo de toutes les fonctionnalités que nous allons construire au cours de cet article.

Ce projet est rempli de fonctionnalités cool afin que vous puissiez tirer le meilleur parti de ce tutoriel et devenir vraiment bon dans l'écriture de code ReactJS.

### Barre de recherche

Nous allons construire cette barre de recherche cool afin que nous puissions rechercher nos personnages préférés.

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/oamlwwlpdi12mxyo5fyo.gif)

### Pagination

Au total, il y a 800+ personnages. Afin d'afficher et de gérer tous ces personnages, nous allons mettre en place un système de pagination où chaque page affichera 20 personnages.

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h1xv509vqui8s326dr4u.gif)

### Filtres

Il y a beaucoup d'étiquettes présentes dans l'API. En les utilisant, nous pouvons filtrer nos données et rechercher exactement ce dont nous avons besoin. Voici la démo :

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nxcx8oqqmgw6nqns0gdz.gif)

### Routage

Nous allons implémenter ce composant pour changer nos pages et créer une barre de navigation. Nous allons utiliser la bibliothèque appelée `react-router-dom` pour cela.

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i5in52wka4jccwdrol9l.gif)

### Routage dynamique

En utilisant `react-router-dom`, nous allons également ajouter un routage dynamique afin que nous puissions en savoir plus sur un personnage lorsque nous cliquons dessus.

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wx9c3gld1hvnn7nz3sda.gif)

# Table des matières

- Installation
- Structure des dossiers
- Récupération des données
- Cartes des personnages
- Barre de recherche
- React-paginate
- Filtres
- React Router
- Épisodes
- Localisation
- Pages dynamiques

# Installation du projet

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dvqlz2dbwxw8hfw05s2w.png)

Avant de commencer le projet, suivez ces étapes pour le configurer :

- Créez un dossier nommé 'react-wiki'
- ouvrez ce dossier dans VS code
- ouvrez votre terminal et exécutez ces commandes une par une : 👍

```JS
npx create-react-app .

npm install bootstrap

npm install @popperjs/core --save

npm install sass

npm install react-router-dom

npm install react-paginate --save

npm start
```

Pour faciliter votre expérience de développement, téléchargez ces extensions VS code :

- ES7 React/Redux/GraphQL/React-Native snippets
- ESLint

# Structure des dossiers

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q4m7qo4j58o8fge72dgx.png)

Nous allons diviser notre projet entier en 5 composants :

- Carte
- Pagination
- Recherche
- Filtre
- Navbar

Créez un dossier nommé 'components' à l'intérieur de votre dossier 'src' et faites 5 dossiers comme ceci : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m58kt2r2cu7u5nfe7h9t.png)

Ensuite, créez ces fichiers selon les noms de nos composants. 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gziuy17t2zlub3m30nro.png)

### App.js

Quelques autres changements que vous devez faire :

- Supprimez tout du fichier `App.css`
- importez React hooks et Bootstrap en haut dans `App.js`

```JS
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap";
import React, { useState, useEffect } from "react";
```

Ensuite, importez tous vos modules depuis les composants :

```JS
import Search from "./components/Search/Search";
import Card from "./components/Card/Card";
import Pagination from "./components/Pagination/Pagination";
import Filter from "./components/Filter/Filter";
import Navbar from "./components/Navbar/Navbar";
```

À l'intérieur de la `déclaration de retour`, supprimez tout et ajoutez ce code : 👍

```JS
<div className="App">
  <h1 className="text-center mb-3">Personnages</h1>
  <div className="container">
  <div className="row">
    Le composant Filtre sera placé ici
    <div className="col-lg-8 col-12">
      <div className="row">
        Le composant Carte sera placé ici
      </div>
    </div>
  </div>
  </div>
</div>
```

### index.css

Ajoutez ces styles par défaut : 👍

```CSS
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400;500;700&display=swap');

body {
  margin: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.ubuntu {
  font-family: "Ubuntu" !important;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, "Courier New",
    monospace;
}
```

Voici le résultat jusqu'à présent :

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hiwhca06v6q4f6nvy6fs.png)

Félicitations ! Nous avons terminé le processus de configuration. Alors maintenant, commençons à coder.

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zaff3h3an5botfzfdjxa.png)

# Comment Récupérer les Données de l'API

Pour récupérer les données de notre API, nous allons utiliser [l'API des personnages de Rick et Morty](https://rickandmortyapi.com/). Nous devrons ajouter quelques éléments.

### App.js 👍

```JS
 let api = `https://rickandmortyapi.com/api/character/?page=1`
```

**Note :** n'utilisez pas de guillemets ou de guillemets doubles autour de l'URL, utilisez des backticks (`comme ceci`) à la place. ☝

Pour récupérer les données de cette API, nous allons utiliser notre hook `useEffects` comme ceci : 👍

```JS
  useEffect(() => { }, [api]);
```

Nous écrivons le hook `useEffect` et mettons l'observation sur `api`. Cela signifie que, au cas où la variable `api` change, nous voulons charger de nouvelles données. Continuons. 👍

```JS
useEffect(() => {
  (async function () {
    let data = await fetch(api).then((res) => res.json());
    console.log(data);
  })();
}, [api]);
```

Nous utilisons une fonction asynchrone pour récupérer nos données brutes et ensuite nous les convertissons au format JSON. Vérifions la console pour voir ce que nous avons jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pbtaztnmfa3e9t9hi8js.png)

Vous voulez le tester vous-même ? Changez le numéro de page en 2 à l'intérieur de l'API, et vous trouverez de nouvelles données dans votre console : 👍

```JS
let api = `https://rickandmortyapi.com/api/character/?page=1`
```

Au lieu de stocker les données dans la console, utilisons le Hook `useState`. Cela stockera les données dans une variable, et nous aurons une clé de fonction pour changer les données de la variable chaque fois que le hook useEffect récupère de nouvelles données. 👍

```JS
let [fetchedData, updateFetchedData] = useState([]);
let { info, results } = fetchedData;
```

De plus, nous déstructurons `info et results` de la variable `fetchedData` pour faciliter notre vie. 👋

La variable `fetchedData` stockera les données que nous avons obtenues de l'API. Nous utiliserons la fonction `updateFetchedData` pour changer les données chaque fois que nous le voulons.

Changeons notre hook useEffect : 👍

```JS
useEffect(() => {
  (async function () {
    let data = await fetch(api).then((res) => res.json());
    updateFetchedData(data);
  })();
}, [api]);
```

# Comment Créer les Cartes des Personnages

Commençons à construire nos cartes de personnages. 👍

Tout d'abord, importez le composant de carte en remplaçant le texte où il est écrit `Le composant Carte sera placé ici`. Ensuite, passez les données récupérées de notre composant `App.js` à notre `composant Carte` comme ceci : 👍

```JS
<Card results={results} />
```

### Card.js

Maintenant, déstructurez d'abord les données que nous avons obtenues de notre composant `App.js`. 👍

```JS
const Card = ({ results }) => {}
```

Ensuite, créez une variable nommée `display`. Cela contiendra toutes nos cartes. Avec cela, nous créerons une instruction `if` `else` pour vérifier si les données que nous avons obtenues de notre API sont vides ou non. 👍

```JS
const Card = ({ results }) => {
  let display;

  if (results) {}
  else{
    display = "Aucun personnage trouvé :/";
  }

  return <>{display}</>;
}
```

Maintenant, nous allons mapper nos `results` à notre composant de cartes de manière à ce qu'il crée des cartes pour nous automatiquement. Mais d'abord, nous devons déstructurer les données que nous avons obtenues de notre API. 👍

```JS
if (results) {
  display = results.map((x) => {
  let { id, image, name, status, location } = x;

    return (
      <div
        key={id}
        className="col-lg-4 col-md-6 col-sm-6 col-12 mb-4 position-relative text-dark"
      >
      </div>
  );
});
}
```

Créez un fichier nommé `Card.module.scss` et ajoutez ce code : 👍

```SCSS
$radius: 10px;
.card {
  border: 2px solid #0b5ed7;
  border-radius: $radius;
}
.content {
  padding: 10px;
}
.img {
  border-radius: $radius $radius 0 0;
}
.badge {
  top: 10px; right: 20px;
  font-size: 17px;
}
```

De plus, importez-le à l'intérieur du composant `Card.js` : 👍

```JS
import styles from "./Card.module.scss";
```

Maintenant, il est temps de créer notre modèle de carte et de mettre les données à leurs places respectives. 👍

```JS
<div
  className={`${styles.card} d-flex flex-column justify-content-center`}
>
  <img className={`${styles.img} img-fluid`} src={image} alt="" />
  <div className={`${styles.content}`}>
    <div className="fs-5 fw-bold mb-4">{name}</div>
    <div className="">
      <div className="fs-6 fw-normal">Dernier emplacement</div>
      <div className="fs-5">{location.name}</div>
    </div>
  </div>
</div>
```

Les résultats jusqu'à présent ressemblent à ceci : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/50oqyl113kg096fcj0wl.png)

À la toute fin, nous allons utiliser ce code 👍 pour informer les utilisateurs si le personnage est mort, vivant ou inconnu :

```JS
{
(() => {
  if (status === "Dead") {
    return (
      <div className={`${styles.badge} position-absolute badge bg-danger`}>
        {status}
      </div>
    );
  } else if (status === "Alive") {
    return (
      <div className={`${styles.badge} position-absolute badge bg-success`}>
        {status}
      </div>
    );
  } else {
    return (
      <div
        className={`${styles.badge} position-absolute badge bg-secondary`}
      >
        {status}
      </div>
    );
  }
})()}
```

Les résultats jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4hyl5uugz5h35dsve7wv.png)

# Comment Construire la Barre de Recherche

Voici une vidéo de démonstration de notre composant de barre de recherche : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/44tw3yyly0d3hiikhrpo.gif)

Maintenant, construisons notre barre de recherche de personnages. Mais d'abord, nous devons créer deux hooks `useState` pour contenir nos `mots-clés de recherche` et notre `numéro de page actuel`. 👍

### App.js

```JS
let [pageNumber, updatePageNumber] = useState(1);
let [search, setSearch] = useState("");
```

Ensuite, nous devons mettre à jour notre API avec des variables. Cela signifie que chaque fois que notre API change, notre hook useEffect récupérera de nouvelles données de notre base de données. 👍

```JS
let api = `https://rickandmortyapi.com/api/character/?page=${pageNumber}&name=${search}`;
```

Maintenant, nous allons importer notre composant de barre de recherche à l'intérieur de la déclaration de retour. Et avec cela, nous allons passer nos nouvelles variables d'état à l'intérieur de ce composant. 👍

```JS
  <h1 className="text-center mb-3">Personnages</h1>
  <Search setSearch={setSearch} updatePageNumber={updatePageNumber} />
```

Créez un fichier nommé `Search.module.scss` pour contenir les styles de ce module spécifique. Ensuite, faites ces ajustements : 👍

### Search.module.scss

```SCSS
.input {
  width: 40%; border-radius: 8px;
  border: 2px solid #0b5ed7;
  box-shadow: 1px 3px 9px rgba($color: #000000, $alpha: 0.25);
  padding: 10px 15px;
  &:focus { outline: none; }
}
.btn {
  box-shadow: 1px 3px 9px rgba($color: #000000, $alpha: 0.25);
}
@media (max-width: 576px) {
  .input { width: 80%; }
}
```

### Search.js

Tout d'abord, nous devons déstructurer nos props. Ensuite, nous créerons une fonction nommée `searchBtn` pour empêcher le comportement par défaut de notre application, comme ceci : 👍

```JS
import React from "react";
import styles from "./Search.module.scss";

const Search = ({ setSearch, updatePageNumber }) => {
  let searchBtn = (e) => {
    e.preventDefault();
  };
};
```

Ensuite, écrivons à l'intérieur de notre déclaration de retour. Tout d'abord, écrivons la balise de formulaire pour contenir nos balises d'entrée et de bouton. 👍

```JS
return (
  <form
    className={`${styles.search} d-flex flex-sm-row flex-column align-items-center justify-content-center gap-4 mb-5`}
  >
  </form>
);
```

Ensuite, nous créons les balises de bouton et d'entrée à l'intérieur de notre balise de formulaire. 👍

```JS
<input
  onChange={(e) => {
    updatePageNumber(1);
    setSearch(e.target.value);
  }}
  placeholder="Rechercher des personnages"
  className={styles.input}
  type="text"
/>
<button
  onClick={searchBtn}
  className={`${styles.btn} btn btn-primary fs-5`}
>
  Rechercher
</button>
```

Les résultats jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/44tw3yyly0d3hiikhrpo.gif)

# Comment Configurer la Pagination avec React-paginate

Voici une démo de notre composant React-paginate : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h1xv509vqui8s326dr4u.gif)

Nous allons utiliser [ce package pour paginer nos données](https://www.npmjs.com/package/react-paginate). Alors, importons-le tout en bas : 👍

### App.js

```JS
<Pagination
  info={info}
  pageNumber={pageNumber}
  updatePageNumber={updatePageNumber}
/>
```

### Pagination.js

Ici, nous allons déstructurer nos props, puis écrire quelques styles JSX : 👍

```JS
import React, { useState, useEffect } from "react";
import ReactPaginate from "react-paginate";

const Pagination = ({ pageNumber, info, updatePageNumber }) => {}
```

À l'intérieur de la déclaration de retour, nous écrivons les styles en JSX comme ceci : 👍

```JS
return (
<>
<style jsx>
{`
  a {
    color: white; text-decoration: none;
  }
  @media (max-width: 768px) {
    .pagination {font-size: 12px}

    .next,
    .prev {display: none}
  }
  @media (max-width: 768px) {
    .pagination {font-size: 14px}
  }
`}
</style>
</>
);
```

Maintenant, créez cette fonction pour gérer la fonction de changement de page : 👍

```JS
let pageChange = (data) => {
  updatePageNumber(data.selected + 1);
};
```

Afin de rendre notre composant de pagination réactif, nous devons écrire ce petit composant :

```JS
const [width, setWidth] = useState(window.innerWidth);
const updateDimensions = () => {
  setWidth(window.innerWidth);
};
useEffect(() => {
  window.addEventListener("resize", updateDimensions);
  return () => window.removeEventListener("resize", updateDimensions);
}, []);
```

Très bien tout le monde, excellent ! Maintenant, nous allons utiliser le package react-paginate. 

Tout d'abord, stylisons tout en utilisant les props intégrées de react-paginate pour styliser les éléments de base : 👍

```JS
<ReactPaginate
  className="pagination justify-content-center my-4 gap-4"
  nextLabel="Suivant"
  previousLabel="Préc"
  previousClassName="btn btn-primary fs-5 prev"
  nextClassName="btn btn-primary fs-5 next"
  activeClassName="active"
  pageClassName="page-item"
  pageLinkClassName="page-link"
/>
```

Voici le principal : nous allons ajouter les fonctionnalités à notre composant afin qu'il fonctionne correctement. 👍

```JS
<ReactPaginate
  forcePage={pageNumber === 1 ? 0 : pageNumber - 1}
  marginPagesDisplayed={width < 576 ? 1 : 2}
  pageRangeDisplayed={width < 576 ? 1 : 2}
  pageCount={info?.pages}
  onPageChange={pageChange}
  //.... autres props ici
/>
```

Les résultats jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h1xv509vqui8s326dr4u.gif)

# Comment Créer le Composant Filtres

Voici une démo de notre composant filtres : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nxcx8oqqmgw6nqns0gdz.gif)

La toute première chose que nous devons faire est de créer une structure de dossiers pour contenir tous les petits composants que nous allons utiliser. Créez ces composants à l'intérieur du dossier `Filter` : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1f1mna2c00acmoer45ce.png)

### App.js

Maintenant, créez ces hooks useState pour stocker notre statut, genre et espèce.

```JS
let [status, updateStatus] = useState("");
let [gender, updateGender] = useState("");
let [species, updateSpecies] = useState("");
```

De plus, nous devons modifier notre variable `api` selon nos variables de hook useState. 👍

```JS
  let api = `https://rickandmortyapi.com/api/character/?page=${pageNumber}&name=${search}&status=${status}&gender=${gender}&species=${species}`;
```

Maintenant, nous allons importer notre composant `filter` à l'intérieur de notre App où il est écrit `Le composant Filtre sera placé ici`. De plus, passez toutes ces props requises : 👍

```JS
<Filter
  pageNumber={pageNumber}
  status={status}
  updateStatus={updateStatus}
  updateGender={updateGender}
  updateSpecies={updateSpecies}
  updatePageNumber={updatePageNumber}
/>
```

### Filter.js

Apportons ces modifications à notre composant Filter afin que nous puissions obtenir les résultats souhaités. Tout d'abord, importez tous nos composants de catégorie comme ceci : 👍

```JS
import React from "react";
import Gender from "./category/Gender";
import Species from "./category/Species";
import Status from "./category/Status";
```

Ensuite, déstructurez les props passées et placez un `accordion` incluant un `bouton de réinitialisation` :

```JS
const Filter = ({
  pageNumber, updatePageNumber,
  updateStatus, updateGender,
  updateSpecies,
}) => {

return (
<div className="col-lg-3 col-12 mb-5">
  <div className="text-center fw-bold fs-4 mb-2">Filtres</div>
  <div
    style={{ cursor: "pointer" }} onClick={clear}
    className="text-primary text-decoration-underline text-center mb-3"
  > Réinitialiser les filtres </div>
  <div className="accordion" id="accordionExample">
    {/* Les composants de catégorie seront placés ici */}
  </div>
</div>
);
};

```

Créez cette fonction afin que nous puissions réinitialiser nos filtres et rafraîchir la page : 👍

```JS
let clear = () => {
  updateStatus("");
  updateGender("");
  updateSpecies("");
  updatePageNumber(1);
  window.location.reload(false);
};
```

Les résultats jusqu'à présent ressemblent à ceci : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jcnncgfpnjqkaow9201j.png)

### FilterBTN.js

Tout d'abord, créons ces boutons de filtre. Nous allons également déstructurer les props requises. 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dmas54wdnue9d7rfcreg.png)

```JS
const FilterBTN = ({ input, task, updatePageNumber, index, name }) => {
return (
<div>
  <style jsx>
    {`
      .x:checked + label {
        background-color: #0b5ed7;
        color: white }
      input[type="radio"] { display: none; }
    `}
  </style>
</div>
);
};
```

Maintenant, nous plaçons le composant d'entrée principal avec des étiquettes sous le `style jsx` : 👍

```JS
<div className="form-check">
  <input
    className="form-check-input x" type="radio"
    name={name} id={`${name}-${index}`}
  />
  <label
    onClick={(x) => {
      task(input); updatePageNumber(1);
    }}
    className="btn btn-outline-primary"
    for={`${name}-${index}`}
  > {input} </label>
</div>
```

### Status.js

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dmas54wdnue9d7rfcreg.png)

Écrivez ce code de départ à l'intérieur de Status.js :

```JS
import FilterBTN from "../FilterBTN";

const Status = ({ updateStatus, updatePageNumber }) => {
  let status = ["Alive", "Dead", "Unknown"];
  return (
    <div className="accordion-item">
      <h2 className="accordion-header" id="headingOne">
        <button
          className="accordion-button" type="button"
          data-bs-toggle="collapse" data-bs-target="#collapseOne"
          aria-expanded="true" aria-controls="collapseOne"
        > Statut </button>
      </h2>
    </div>
  );
};
```

Ensuite, créons les boutons de statut en mappant notre tableau de données. 👍

Sous la balise `h2` de fin, mettez ceci à l'intérieur 👍 qui nous aidera à mapper automatiquement les données et à créer nos boutons de statut :

```JS
<div
  id="collapseOne" className="accordion-collapse collapse show"
  aria-labelledby="headingOne" data-bs-parent="#accordionExample"
>
<div className="accordion-body d-flex flex-wrap gap-3">
  {status.map((item, index) => (
    <FilterBTN
      key={index}
      index={index}
      name="status"
      task={updateStatus}
      updatePageNumber={updatePageNumber}
      input={item}
    />
  ))}
</div>
</div>
```

#### temps de tester dans Filter.js

Écrivez ces lignes à l'intérieur de Filter.js pour vérifier si le composant fonctionne ou non : 👍

```JS
<Status
  updatePageNumber={updatePageNumber}
  updateStatus={updateStatus}
/>
```

Les résultats jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kxcq2s8q8ntfe6dh36vc.gif)

### Species.js

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mmvw4v4tqh6gx2lupoju.png)

Écrivez ces codes de départ à l'intérieur de Species.js :

```JS
import FilterBTN from "../FilterBTN";

const Species = ({ updateSpecies, updatePageNumber }) => {
return (
<div className="accordion-item ">
  <h2 className="accordion-header" id="headingTwo">
    <button
      className="accordion-button collapsed" type="button"
      data-bs-toggle="collapse" data-bs-target="#collapseTwo"
      aria-expanded="false" aria-controls="collapseTwo"
    > Espèce </button>
  </h2>
</div>
)}
```

Maintenant, créez un tableau pour contenir toutes nos données d'espèces possibles : 👍

```JS
  let species = [
    "Human", "Alien", "Humanoid",
    "Poopybutthole", "Mythological", "Unknown",
    "Animal", "Disease","Robot","Cronenberg","Planet",
  ];
```

Et ensuite, créons les boutons d'espèces en mappant nos données de tableau comme ceci : 👍

```JS
<div
    id="collapseTwo" className="accordion-collapse collapse"
    aria-labelledby="headingTwo"
    data-bs-parent="#accordionExample"
  >
  <div className="accordion-body d-flex flex-wrap gap-3">
    {species.map((item, index) => {
      return (
        <FilterBTN
          name="species" index={index} key={index}
          updatePageNumber={updatePageNumber}
          task={updateSpecies} input={item}
        />
      );
    })}
  </div>
</div>
```

#### temps de tester dans Filter.js

Écrivez ces lignes à l'intérieur de Filter.js pour vérifier si le composant fonctionne ou non : 👍

```JS
<Species
  updatePageNumber={updatePageNumber}
  updateSpecies={updateSpecies}
/>
```

Les résultats jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/aav8duudtdkwxznfayn0.gif)

### Gender.js

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/45yw5m81hr3utyydwfms.png)

Écrivez ce code de départ : 👍

```JS
import FilterBTN from "../FilterBTN";

const Gender = ({ updateGender, updatePageNumber }) => {
let genders = ["female", "male", "genderless", "unknown"];
return (
  <div className="accordion-item">
    <h2 className="accordion-header" id="headingThree">
      <button
        className="accordion-button collapsed" type="button"
        data-bs-toggle="collapse" data-bs-target="#collapseThree"
        aria-expanded="false" aria-controls="collapseThree"
      > Genre </button>
    </h2>
  </div>
);
};
```

Sous la balise `h2` finale, mettez ce code à l'intérieur 👍 qui nous aidera à mapper automatiquement les données et à créer nos boutons de genre :

```JS
<div id="collapseThree" className="accordion-collapse collapse"
  aria-labelledby="headingThree" data-bs-parent="#accordionExample"
>
<div className="accordion-body d-flex flex-wrap gap-3">
  {genders.map((items, index) => {
    return (
      <FilterBTN
        name="gender" index={index} key={index}
        updatePageNumber={updatePageNumber}
        task={updateGender} input={items}
      />
      );
    })}
  </div>
</div>
```

#### temps de tester dans Filter.js

Écrivez ces lignes à l'intérieur de Filter.js pour vérifier si le composant fonctionne ou non : 👍

```JS
<Gender
  updatePageNumber={updatePageNumber}
  updateGender={updateGender}
/>
```

Les résultats jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9aklsikf2brx5h7vxxsm.gif)

# Comment Configurer React Router

Voici une démo de notre composant de navigation : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i5in52wka4jccwdrol9l.gif)

Commençons à coder !

Tout d'abord, créez un dossier nommé `Pages` à l'intérieur du dossier `src`. Il contiendra 2 fichiers - `Episodes.js` et `Location.js`. Quelque chose comme ceci : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fd0k8mt8s1sq842axwsd.png)

### App.js

Importez votre nouveau composant de pages dans `App.js` : 👍

```JS
import Episodes from "./Pages/Episodes";
import Location from "./Pages/Location";
```

Afin de déclarer le Router et de définir tous les types de chemins de fichiers, nous devons importer `react-router-dom` dans `App.js` incluant ses composants principaux. 👍

```JS
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
```

Maintenant, créez un nouveau composant fonctionnel appelé `Home` à l'intérieur du fichier App.js. Ensuite, coupez tout du composant `App` et mettez-le à l'intérieur du composant `Home` : 👍

```JS
const Home = () => {
  // Tout ce que vous avez écrit jusqu'à présent
}
```

À l'intérieur de votre fonction de composant `App`, créez un nouveau composant `Router` et mettez-le à l'intérieur du composant `Navbar`. 👍

```JS
function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
      </div>
    </Router>
  );
}
```

Maintenant, nous devons définir toutes nos routes. Souvenez-vous, `Routes` est une collection de `Route`s. `Route` est le chemin de fichier réel.

Chaque route nécessite 2 choses : Le `path` où l'application mènera réellement et l'`element` qui sera chargé. 👍

```JS
<Routes>
  <Route path="/" element={<Home />} />

  <Route path="/episodes" element={<Episodes />} />

  <Route path="/location" element={<Location />} />
</Routes>
```

### Navbar.js

Jusqu'à présent, tout va bien ! Maintenant, faisons le composant de la barre de navigation. Tout d'abord, importez 2 composants de `react-router-dom`. Ensuite, écrivez cette classe parente bootstrap incluant le nom de la marque pour contenir notre composant de pages de la barre de navigation : 👍

```JS
import { NavLink, Link } from "react-router-dom";

const Navbar = () => {
return (
  <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
    <div className="container">
      <Link to="/" className="navbar-brand fs-3 ubuntu">
        Rick & Morty <span className="text-primary">WiKi</span>
      </Link>
      <style jsx>{`
        button[aria-expanded="false"] > .close {
          display: none;
        }
        button[aria-expanded="true"] > .open {
          display: none;
        }
      `}</style>
    </div>
  </nav>
);
};
```

Écrivez ce code pour générer notre menu hamburger réactif : 👍

```JS
<button
  className="navbar-toggler border-0"
  type="button"
  data-bs-toggle="collapse"
  data-bs-target="#navbarNavAltMarkup"
  aria-controls="navbarNavAltMarkup"
  aria-expanded="false"
  aria-label="Toggle navigation"
>
  <span class="fas fa-bars open text-dark"></span>
  <span class="fas fa-times close text-dark"></span>
</button>
```

Écrivez ce code pour générer nos liens de barre de navigation cliquables. Remarquez que nous utilisons le composant <NavLink> de 'react-router-dom' pour lier à l'URL du composant de notre page : 👍

```JS
<div
  className="collapse navbar-collapse justify-content-end"
  id="navbarNavAltMarkup"
> <div className="navbar-nav fs-5">
    <NavLink to="/" className="nav-link">
      Personnages
    </NavLink>
    <NavLink to="/episodes" className="nav-link">
      Épisodes
    </NavLink>
    <NavLink
      activeClassName="active" className="nav-link"
      to="/location" >Localisation</NavLink>
  </div>
</div>
```

### App.css

Écrivez également ces styles si vous voulez rendre la barre de navigation belle et permettre à vos utilisateurs de savoir exactement sur quelle page ils se trouvent actuellement : 👍

```CSS
.active {
  color: #0b5ed7 !important;
  font-weight: bold;
  border-bottom: 3px solid #0b5ed7;
}
```

Ensuite, à l'intérieur de `Navbar.js`, importez les styles comme ceci : 👍

```JS
import "../../App.css";
```

Le résultat jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i5in52wka4jccwdrol9l.gif)

# Épisodes

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kby93lasrq6di8md58sg.png)

Pour créer cette page, nous avons besoin de 2 composants : le premier est le `composant carte`, qui est déjà construit, et le second est le composant `Groupe d'entrée` à travers lequel nous pouvons changer notre numéro d'épisode.

### InputGroup.js

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d53jsa8tz1e2aab1dk9s.gif)

Nos groupes d'entrée ne seront disponibles que dans les composants `Épisodes` et `Localisation` afin que nous puissions changer le numéro d'épisode et la localisation pour rechercher des personnages. Commençons ! 👍

À l'intérieur du dossier `category` du dossier `Filter`, créez un nouveau fichier nommé `InputGroup.js` et écrivez ce code de départ incluant le système de déstructuration des props : 👍

```JS
const InputGroup = ({ name, changeID, total }) => {
return <div className="input-group mb-3">
  <select
  onChange={(e) => changeID(e.target.value)}
  className="form-select"
  id={name}
  ></select>
</div>
};
```

Ensuite, créons notre groupe d'entrée d'option. Écrivez ce code à l'intérieur de votre balise `select` : 👍

```JS
<option value="1">Choisir...</option>
{[...Array(total).keys()].map((x, index) => {
  return (
    <option value={x + 1}>
      {name} - {x + 1}
    </option>
  );
})}
```

### Episodes.js

À l'intérieur de ce fichier, importez ces composants : 👍

```JS
import React, { useEffect, useState } from "react";
import Card from "../components/Card/Card";
import InputGroup from "../components/Filter/category/InputGroup";
```

Maintenant, créez ces états afin que nous puissions contenir et changer des informations cruciales pour récupérer des données de notre `api` : 👍

```JS
const Episodes = () => {
  let [results, setResults] = React.useState([]);
  let [info, setInfo] = useState([]);
  let { air_date, episode, name } = info;
  let [id, setID] = useState(1);

let api = `https://rickandmortyapi.com/api/episode/${id}`;
}
```

Écrivez ce code pour récupérer des données de notre API : 👍

```JS
useEffect(() => {
  (async function () {
    let data = await fetch(api).then((res) => res.json());
    setInfo(data);

    let a = await Promise.all(
      data.characters.map((x) => {
        return fetch(x).then((res) => res.json());
      })
    );
    setResults(a);
  })();
}, [api]);
```

Maintenant, écrivons le code pour afficher les résultats sur notre écran. Tout d'abord, affichons le nom de l'épisode et la date de diffusion comme ceci : 👍

```JS
return (
<div className="container">
  <div className="row mb-3">
    <h1 className="text-center mb-3">
      Nom de l'épisode :{" "}
      <span className="text-primary">{name === "" ? "Inconnu" : name}</span>
    </h1>
    <h5 className="text-center">
      Date de diffusion: {air_date === "" ? "Inconnu" : air_date}
    </h5>
  </div>
</div>
);
```

Les résultats jusqu'à présent ressemblent à ceci : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8rq6yd767in8qi5eu3mt.png)

Maintenant, affichons les cartes des personnages et les groupes d'entrée : 👍

```JS
<div className="row">
  <div className="col-lg-3 col-12 mb-4">
    <h4 className="text-center mb-4">Choisir un épisode</h4>
    <InputGroup name="Épisode" changeID={setID} total={51} />
  </div>
  <div className="col-lg-8 col-12">
    <div className="row">
      <Card results={results} />
    </div>
  </div>
</div>
```

Les résultats jusqu'à présent : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kby93lasrq6di8md58sg.png)

# Localisation

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4yq78xas7xjcgzgnkp74.gif)

La création de ce composant est similaire à la création de la page `épisodes`. Tout d'abord, copiez tout de la page `épisodes` et apportez ces quelques modifications : 👍

```JS
  let [results, setResults] = useState([]);
  let [info, setInfo] = useState([]);
  let { dimension, type, name } = info;
  let [number, setNumber] = useState(1);

  let api = `https://rickandmortyapi.com/api/location/${number}`;
```

Maintenant, changez seulement un mot-clé dans le hook `useEffect`, de `characters` à `residents`, comme ceci : 👍

```JS
useEffect(() => {
      // Les autres codes sont ici
      data.residents.map((x) => {
      })
    // Les autres codes sont ici
}, [api]);
```

Dans la déclaration de retour, apportez ces modifications : 👍

```JS
return (
<h1 className="text-center mb-3">
  Localisation :
  <span className="text-primary">
    {name === "" ? "Inconnu" : name}
  </span>
</h1>
<h5 className="text-center">
  Dimension: {dimension === "" ? "Inconnu" : dimension}
</h5>
<h6 className="text-center">Type: {type === "" ? "Inconnu" : type}</h6>
);
```

Et enfin, apportez ces modifications pour notre composant `InputGroup` : 👍

```JS
<InputGroup name="Localisation" changeID={setNumber} total={126} />
```

Les résultats jusqu'à présent 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4yq78xas7xjcgzgnkp74.gif)

# Pages Dynamiques

C'est la dernière étape de notre projet. Notre objectif principal est d'en savoir plus sur un personnage spécifique lorsque nous cliquons sur la carte. Nous allons utiliser le système de module dynamique de `react-router-dom` – quelque chose comme ceci : 👍

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wx9c3gld1hvnn7nz3sda.gif)

### CardDetails.js

Pour accomplir nos objectifs, nous devons créer un composant séparé pour afficher plus de détails sur le personnage. Nous allons créer un nouveau fichier nommé `CardDetails.js` à l'intérieur du dossier `Card`.

Tout d'abord, importons les composants essentiels :

```JS
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
```

Ensuite, nous devons stocker notre `api` et utiliser quelques hooks `useState`. Nous allons utiliser le hook `useParams` pour obtenir l'id de l'URL : 👍

```JS
const CardDetails = () => {
let { id } = useParams();
let [fetchedData, updateFetchedData] = useState([]);
let { name, location, origin, gender, image, status, species } = fetchedData;

let api = `https://rickandmortyapi.com/api/character/${id}`;
}
```

Nous allons utiliser ce hook useEffect pour récupérer des données de notre API : 👍

```JS
useEffect(() => {
  (async function () {
    let data = await fetch(api).then((res) => res.json());
    updateFetchedData(data);
  })();
}, [api]);
```

Maintenant, écrivons ce code qui affichera le nom et l'image de notre personnage : 👍

```JS
return (
<div className="container d-flex justify-content-center mb-5">
  <div className="d-flex flex-column gap-3">
    <h1 className="text-center">{name}</h1>
    <img className="img-fluid" src={image} alt="" />
  </div>
</div>
)
```

Maintenant, écrivez ce code au cas où vous souhaitez afficher le statut actuel de chaque personnage : 👍

```JS
{(() => {
if (status === "Dead") {
  return <div className="badge bg-danger fs-5">{status}</div>;
} else if (status === "Alive") {
  return <div className=" badge bg-success fs-5">{status}</div>;
} else {
  return <div className="badge bg-secondary fs-5">{status}</div>;
}
})()}
```

Ensuite, écrivez ce code pour afficher toutes les informations sur le personnage : 👍

```JS
<div className="content">
  <div className="">
    <span className="fw-bold">Genre : </span>
    {gender}
  </div>
  <div className="">
    <span className="fw-bold">Localisation : </span>
    {location?.name}
  </div>
  <div className="">
    <span className="fw-bold">Origine : </span>
    {origin?.name}
  </div>
  <div className="">
    <span className="fw-bold">Espèce : </span>
    {species}
  </div>
</div>
```

### App.js

Ensuite, nous devons définir nos chemins afin que notre composant de routeur dynamique fonctionne correctement. Tout d'abord, importez puis ajoutez ce code : 👍

```JS
import CardDetails from "./components/Card/CardDetails";
// autres codes sont ici

<Routes>
  <Route path="/:id" element={<CardDetails />} />
  <Route path="/episodes/:id" element={<CardDetails />} />
  <Route path="/location/:id" element={<CardDetails />} />
</Routes>
```

Maintenant, faites défiler vers le bas à l'intérieur de votre App.js et faites cette petite modification 👍 afin qu'il fasse référence à la page d'accueil :

```JS
<Card page="/" results={results} />
```

### Card.js

Allez dans votre composant de carte et apportez ces modifications : 👍

- Tout d'abord, déstructurez les nouvelles props et importez `Link` de `react-router-dom`

```JS
import { Link } from "react-router-dom";

const Card = ({ page, results }) => {}
```

- Ensuite, enveloppez tout à l'intérieur de la déclaration de retour à l'intérieur d'une balise Link :

```JS
<Link
  style={{ textDecoration: "none" }}
  to={`${page}${id}`}
  key={id}
  className="col-lg-4 col-md-6 col-sm-6 col-12 mb-4 position-relative text-dark"
>
{/* Autres codes sont ici */}
</Link>
```

### Episodes.js

Dans ce fichier, ajustez simplement cette petite ligne : 👍

```JS
<Card page="/episodes/" results={results} />
```

### Location.js

Tout comme dans Episodes.js, ajustez simplement cette petite ligne : 👍

```JS
<Card page="/location/" results={results} />
```

Les résultats : ✨✨✨

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wx9c3gld1hvnn7nz3sda.gif)

# Conclusion

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6596mzy60z7yb2366ffa.png)

Félicitations pour avoir lu jusqu'à la fin ! Maintenant, vous pouvez facilement et efficacement utiliser React JS et Bootstrap pour gérer des projets. 
    
Vous avez également appris à récupérer des données d'une API et à mapper les résultats. Non seulement cela, mais vous avez également un projet à montrer à votre recruteur local.

Voici votre médaille pour avoir lu jusqu'à la fin ❤️

## Les suggestions et critiques sont grandement appréciées ❤️

![Texte Alternatif](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

- [LinkedIn/ JoyShaheb](https://www.linkedin.com/in/joyshaheb/)
- [YouTube / JoyShaheb](https://www.youtube.com/c/joyshaheb)
- [Twitter / JoyShaheb](https://twitter.com/JoyShaheb)
- [Instagram / JoyShaheb](https://www.instagram.com/joyshaheb/)