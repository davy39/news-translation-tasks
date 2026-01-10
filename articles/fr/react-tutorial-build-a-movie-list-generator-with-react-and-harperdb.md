---
title: Tutoriel React – Construire un générateur de liste de films avec React et HarperDB
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-30T19:07:30.000Z'
originalURL: https://freecodecamp.org/news/react-tutorial-build-a-movie-list-generator-with-react-and-harperdb
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/HarperDBMovieCover.png
tags:
- name: database
  slug: database
- name: React
  slug: react
- name: Web Applications
  slug: web-applications
seo_title: Tutoriel React – Construire un générateur de liste de films avec React
  et HarperDB
seo_desc: 'In this tutorial, we are going to be building a simple movie generator
  which automatically generates a new movie every 40 seconds. It will also contain
  a button called “Generate New Movie” to display another movie on demand.

  This app will display a m...'
---

Dans ce tutoriel, nous allons construire un générateur de films simple qui génère automatiquement un nouveau film toutes les 40 secondes. Il contiendra également un bouton appelé « Générer un nouveau film » pour afficher un autre film à la demande.

Cette application affichera un film avec son titre, sa date de sortie, sa note de fans, sa durée, une courte description, les acteurs principaux, le nom des réalisateurs et enfin un bouton qui mène à la page IMDb du film.

Vous pouvez accéder au code complet de ce projet depuis son dépôt [Github](https://github.com/KingsleyUbah/harperdb-movie-generator).

## Comment allons-nous construire cela ?

Comme pour la plupart des autres applications web, cette application se composera d'un front-end et d'un back-end.

Le front-end est la partie que l'utilisateur voit et avec laquelle il interagit. Dans notre application, notre front-end sera composé de l'image de couverture du film, de ses informations et d'un bouton qui mènera à la page IMDb du film.

Le back-end est l'endroit d'où proviendront nos données de films – comme le titre du film, la description, les acteurs, l'image, etc.

L'application va générer automatiquement un nouveau film aléatoire toutes les 40 secondes.

Nous allons construire le front-end de notre application en utilisant React. React est une bibliothèque JavaScript front-end utilisée pour construire des composants d'interface utilisateur réutilisables tels que des boutons, des menus de navigation, des images, des cartes, etc.

Nous allons également styliser nos composants en utilisant du CSS pur.

### Comment nous allons construire le back-end

Le back-end d'un site web contient généralement une base de données, qui est un programme que vous utilisez pour stocker et gérer des données. La base de données doit également être accessible via une API afin que notre front-end puisse accéder aux données et les afficher à l'utilisateur.

Pour y parvenir, nous allons utiliser un outil intéressant et amusant appelé **HarperDB**.

### **Qu'est-ce que HarperDB ?**

HarperDB est un logiciel de base de données et de gestion de données incroyablement rapide – il a même été prouvé qu'il est 37 fois plus rapide que MongoDB.

La vitesse d'une base de données fait référence à la rapidité avec laquelle elle peut lire et écrire des données dans ses enregistrements ainsi que faire des calculs sur ces données.

HarperDB est également incroyablement flexible. Il vous permet de faire ce qui suit :

* Faire des requêtes à un seul endpoint

* Utiliser à la fois SQL et NoSQL pour interroger votre base de données

* Télécharger des données en JSON et avec des requêtes SQL.

Si vous travaillez avec beaucoup de données, vous pouvez tout importer en une seule étape dans un fichier CSV. Plutôt pratique !

Vous n'avez pas à définir les types de données pour vos données, car HarperDB le fait dynamiquement pour vous. Sans parler de leur interface simple pour gérer votre instance cloud sans aucun tracas.

Comme je l'ai dit, très flexible.

## Prérequis pour ce tutoriel

Pour construire cette application, je vais supposer que vous avez quelques connaissances de base des langages et outils suivants :

**Npm ou tout autre gestionnaire de paquets** : Nous en aurons besoin pour installer React et un hook React HarperDB appelé [use-harperdb](https://www.npmjs.com/package/use-harperdb) dans votre projet.

NPM signifie Node Package Manager. C'est un outil qui connecte votre projet local au registre npm, où des millions de paquets de code publics, tels que React et `useharperdb`, sont hébergés. Il vous aide également à gérer ce code, une fois qu'il est installé.

Assurez-vous d'avoir une version de Node d'au moins 12.xx installée sur votre machine. Vous pouvez vérifier votre version de node avec cette commande : `node -v`

**SQL** : Dans ce projet, nous n'allons utiliser qu'une ou deux requêtes de base, donc ne vous inquiétez pas si vous ne connaissez pas beaucoup SQL.

SQL signifie Structured Query Language. C'est un langage populaire utilisé pour interroger les bases de données relationnelles. Nous l'utiliserons dans notre hook pour interroger notre instance cloud HarperDB pour des données.

**React** : Notre interface utilisateur sera construite avec React. Si vous connaissez JavaScript, alors apprendre React est relativement facile.

**Un compte HarperDB** : Si vous n'avez pas de compte HarperDB, vous devrez en [créer un](https://studio.harperdb.io/sign-up). Ne vous inquiétez pas, c'est complètement gratuit. Je vais vous montrer comment créer un compte ci-dessous.

**Et enfin, CSS** : nous utiliserons un peu de CSS pour styliser nos éléments.

## Que sont les hooks React ?

Dans le passé, pour travailler avec des données dans un composant React, vous deviez définir le composant comme un composant de classe. Cela a changé lorsque React a introduit les hooks.

Simplement, les hooks sont des fonctions qui vous permettent de travailler avec des données dans un composant React non-classe (c'est-à-dire, fonctionnel).

Grâce à cela, vous n'avez pas à définir un composant de classe React juste pour gérer les données d'état à l'intérieur.

Le hook `use-harperdb` vous permet de connecter votre application à votre instance de base de données cloud pour obtenir des données. Pensez-y comme un pont entre votre application React (front-end) et la base de données HarperDB (back-end).

## Comment configurer la base de données

HarperDB est une base de données flexible, comme je l'ai mentionné précédemment. Elle vous permet d'utiliser ses services soit en configurant votre propre serveur local HarperDB, soit en utilisant l'architecture serverless.

Dans ce projet, nous allons utiliser l'architecture serverless. Cela signifie que nous n'implémenterons pas de serveur (c'est-à-dire, le back-end) sur notre machine locale. Au lieu de cela, nous allons exploiter l'infrastructure cloud de HarperDB pour gérer nos données de films et les rendre disponibles pour notre application.

### Configurer l'instance cloud HarperDB

Tout d'abord, je vais supposer que vous avez créé votre compte gratuit comme je l'ai demandé précédemment. Si vous ne l'avez pas fait, allez-y et [inscrivez-vous](https://studio.harperdb.io/sign-up).

![Image](https://www.freecodecamp.org/news/content/images/2021/08/HarperDB-Start-for-free-1.png align="left")

*Inscription à HarperDB*

Vous serez invité à fournir votre nom, un e-mail valide et un nom de sous-domaine pour votre instance cloud. Avec cela, HarperDB créera un nom de sous-domaine pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Studio-HarperDB--password-1.png align="left")

*Assurez-vous de choisir un mot de passe fort*

Ensuite, nous allons créer une instance cloud :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Studio-HarperDB---instance-info-2.png align="left")

*Remplissez vos détails*

Ici, vous serez invité à ajouter un nom d'instance. Ne vous inquiétez pas, vous pouvez le nommer comme vous voulez, mais il est préférable de le rendre descriptif.

Pour créer votre URL d'instance, que vous aurez besoin dans votre application lors de l'interrogation des données, HarperDB combinera votre nom d'instance avec votre nom de sous-domaine. Vous serez également invité à définir les informations d'identification de votre instance (nom d'utilisateur et mot de passe).

Ensuite, nous sélectionnons les spécifications de l'instance. Pour les besoins de ce tutoriel, nous allons opter pour les plans gratuits. De plus, vous devrez choisir une région pour votre instance.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Studio-HarperDB----more-instance-1.png align="left")

*Choix des plans gratuits*

Cliquez sur « Confirmer les détails de l'instance » et vous serez redirigé vers une page contenant toutes les informations de votre instance. Maintenant, copiez l'URL de votre instance, votre nom d'utilisateur et votre mot de passe et sauvegardez-les quelque part car vous en aurez besoin plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Studio-HarperDB---confirm-instance-1.png align="left")

*Sauvegardez votre URL, nom d'utilisateur et mot de passe*

Lorsque vous avez terminé, cliquez sur le bouton « Ajouter une instance ». Vous serez redirigé vers une page qui montre la carte de votre instance. Votre instance aura besoin de quelques minutes pour se configurer initialement avant que vous puissiez l'utiliser, mais nous pouvons faire quelques choses en attendant.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Studio-HarperDB---creating-instance-2.png align="left")

*Configuration en cours*

## Comment configurer l'application React

Pendant que notre instance cloud est encore en cours de configuration, nous pouvons en profiter pour configurer le répertoire du projet pour notre application.

Tout d'abord, nous initialisons notre projet en exécutant la commande suivante sur n'importe quel terminal de commande :

```js
npx create-react-app harperdb-movies-generator
```

Cette commande créera un dossier appelé harperdb-movies-app ainsi que l'installation de toutes les dépendances dont nous avons besoin pour notre projet. Cela inclut React et ReactDOM, donc nous n'avons pas à le faire manuellement.

Ensuite, nous allons exécuter la commande pour intégrer le hook use-harperdb dans notre projet. Ce hook nous aidera à nous connecter à notre instance cloud. Pour l'installer, nous exécutons la commande suivante sur notre ligne de commande :

```js
npm install use-harperdb
```

**C'est tout pour la configuration !**

### Comment intégrer HarperDB à votre application React

Maintenant que le hook use-harperdb est installé, nous devons faire une chose de plus pour pouvoir accéder aux données de votre base de données et effectuer des opérations CRUD dessus : nous devons connecter votre application à votre instance cloud. Nous allons faire cela avec le HarperDBProvider.

Avant de nous lancer dans cela, nous devons faire quelque chose d'abord. Lors de la construction d'une application CRUD, il n'est pas bon de exposer des informations d'identification privées telles que nos clés API à d'autres personnes, surtout si nous avons l'intention de pousser le code vers un dépôt public comme GitHub.

Pour protéger toute information d'identification sensible, nous devons les stocker en tant que variables d'environnement. Ce n'est qu'un fichier où nous stockons des informations d'identification sensibles telles que nos mots de passe, clés API, et dans notre cas actuel, les informations d'identification de notre instance cloud (URL, nom d'utilisateur et mot de passe).

Créez un fichier `.env` à la racine de votre répertoire. Vous créez ce fichier dans votre éditeur de code, faites un clic droit sur le répertoire racine (harperdb-movie-generator) et sélectionnez l'option « créer un nouveau fichier ».

Nommez ce fichier `.env` et appuyez sur Entrée. Cela créera un fichier .env à l'intérieur de harperdb-movie-generator. Après cela, définissez les variables suivantes :

```c
REACT_APP_DB_URL=**
REACT_APP_USER=**
REACT_APP_PASSWORD=**
```

Assurez-vous d'utiliser le même format et de fournir les détails corrects concernant votre propre instance cloud à la place des doubles astérisques. Remplissez l'URL de votre instance, votre nom d'utilisateur et votre mot de passe, que je vous ai demandé de sauvegarder quelque part.

React lira toutes les variables d'environnement qui utilisent le préfixe REACT\_APP, puis transmettra dynamiquement la valeur là où c'est nécessaire.

Avec le fichier .env créé, notre prochaine action sera d'envelopper toute notre application React à l'intérieur du HarperDBProvider importé.

HarperDBProvider garantira que notre application dispose du contexte de la base de données HarperDB.

Pour envelopper notre application React à l'intérieur du fournisseur, nous allons nous rendre dans index.js à l'intérieur de notre projet, importer le fournisseur et transmettre en toute sécurité ces variables d'environnement dans le fournisseur. Cela lui permet de savoir à quelle instance connecter notre front-end :

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { HarperDBProvider } from 'use-harperdb';


ReactDOM.render(
  <React.StrictMode>
    <HarperDBProvider
    url={process.env.REACT_APP_DB_URL}
    user={process.env.REACT_APP_USER}
    password={process.env.REACT_APP_PASSWORD}
    >
      <App />
    </HarperDBProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
```

## Comment peupler notre base de données avec des données

Si vous vous souvenez, nous avons laissé l'instance cloud alors qu'elle était encore en cours de configuration. À présent, nous devrions avoir notre instance prête et prête à servir des données. Dans ce cas, vous verrez le statut OK sur votre instance :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Studio-HarperDB--okay-2.png align="left")

*Instance maintenant configurée*

Votre instance cloud devrait être prête à fonctionner avec votre front-end connecté à votre instance également. Cependant, le front-end sera inutile s'il n'a pas de données (c'est-à-dire des films) à afficher à l'utilisateur.

Nous devons donc d'abord peupler notre base de données avec des données.

Mais avant cela, nous devons créer un schéma pour nos données de films. Vous pouvez considérer un schéma comme une collection de tables dans notre base de données. J'appelle simplement mon propre schéma "collection" :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Studio-HarperDB---collection-1.png align="left")

*Création de notre schéma et d'une table à l'intérieur*

Ensuite, nous allons créer notre table. J'ai appelé la mienne "movie". Une table consistera en des enregistrements de films individuels.

Chaque enregistrement de film doit avoir un hash\_attribiute. Un hash\_attribute est simplement une colonne avec des clés uniques qui identifie cette ligne de données particulière et la distingue de la ligne suivante. Nous utilisons simplement la colonne "id" comme notre hash\_attribute.

Puisque nous créons une application avec plus d'un film, notre table consistera en plus d'une ligne de films (c'est-à-dire des enregistrements de données). De plus, puisque chaque film a de nombreuses propriétés telles que le titre, l'année, la date de sortie, etc., il aura plus d'un champ d'information.

Vous pouvez télécharger les films un par un avec un seul objet JSON ou télécharger une collection complète de films avec un tableau d'objets JSON.

HarperDB vous permet de télécharger des données de trois manières principales :

1. En effectuant des requêtes SQL ou NoSQL pour créer des données sur notre base de données.

2. En définissant un seul objet JSON (pour un seul enregistrement) et un tableau de données JSON (pour plusieurs enregistrements)

3. En important et en chargeant des données avec un fichier CSV

Pour télécharger les données d'un seul film, nous créons un objet JSON qui contient toutes les informations du film. Voici un exemple des données JSON :

```js
{
  cover: 'https://res.cloudinary.com/ubahthebuilder/image/upload/v1627129180/avengers_endgame_ilqzqj.png',
  date: 2017,
  description: 'Après les événements dévastateurs d\'Avengers : Infinity War (2018), l\'univers est en ruines. Avec l\'aide des alliés restants, les Avengers se rassemblent une fois de plus afin d\'inverser les actions de Thanos et de rétablir l\'équilibre dans l\'univers.',
  directors: [
    'Anthony Russo',
    'Joe Russo'
  ],
  genres: [
    'Action',
    'Aventure',
    'Drame'
  ],
  hours: 3,
  id: 1,
  minutes: 1,
  rating: 8.4,
  stars: [
    'Robert Downey',
    'Chris Evans',
    'Mark Ruffalo'
  ],
  title: 'Avengers: End Game',
  website: 'https://www.imdb.com/title/tt4154796/',
  writers: [
    'Christopher Markus',
    'Stephen McFeely'
  ]
}
```

Accédez à la table des films à l'intérieur de la collection et cliquez sur le signe + dans le coin supérieur droit de la page, qui est mis en évidence dans l'image suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/addmovie.png align="left")

*Ajout d'un nouvel enregistrement de film dans notre table*

Copiez l'objet JSON précédemment défini et collez-le dans l'espace prévu, en remplaçant tout ce qui s'y trouve pour des raisons de formatage. Cliquez sur le bouton vert pour enregistrer les informations dans la table des films.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/adddata.png align="left")

*Coller l'objet JSON*

Une fois le téléchargement terminé, notre table devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Studio-HarperDB-FULL-TABLE-1.png align="left")

*Huit films à l'intérieur de notre table*

Notez que vous pouvez utiliser les données du dépôt [GitHub](https://github.com/KingsleyUbah/harperdb-movie-generator/blob/master/data/movies.json) de ce projet pour insérer plusieurs enregistrements de films à la fois.

## Comment construire notre interface utilisateur et interroger la base de données

Maintenant que les données sont prêtes, nous devons les afficher sur notre front-end pour que l'utilisateur puisse les voir et interagir avec elles.

Tout d'abord, nous devons modifier notre fichier app.js :

```js
import React from 'react';
import './App.css';
import Movie from './components/Movie';

function App() {
  return (
    <div className="App">
      <div className="main-container">
        <header>
          <h1 className="heading">Liste de films</h1>
          <h3> Un générateur de films simple construit avec React et HarperDB</h3>
        </header>
        <div>
          <Movie />
        </div>
      </div>
    </div>
  );
}

export default App;
```

Ce sera le composant de niveau supérieur dans notre projet.

Ensuite, nous allons importer les bibliothèques React et React DOM ainsi que la feuille de style App.css pour toute notre application.

Ensuite, dans le fichier App.css, nous définissons notre composant d'application qui retourne les éléments Header ainsi que le composant Movie.

Voici le style pour toute notre application :

```css
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap');

/* Styles de base */

body {
  font-family: "lato", sans-serif;
  color: white;
  background-color: #082032;
}

a {
  color: black;
  font-family: "roboto", sans-serif;
  font-size: 50px;
  text-decoration: none;
  display: inline-block;
}

h1 {
  text-align: center;
  font-family: "roboto", sans-serif;
  font-size: 60px;
  font-weight: 80px;
}

h3 {
  text-align: center;
}

p {
  font-weight: 400px;
}

span {
  color: #FFF338;
}

ul {
  list-style-type: none;
  display: flex;
  margin-left: 339px;
}

li {
  outline-color: #2C394B;
  outline-style: inset;
  outline-width: 2px;
  outline-offset: 5px;
  margin: 11px;
  padding: 0px, 20px;
}

img {
  height: 500px;
  width: 100%;
}

/* Classes */

.movie-cover {
  max-width: 800px;
  width: 800px;
  background-color: #2C394B;
  margin: 0 auto;
  border-radius: 10px;
}

.circle {
    background-color: transparent;
    margin-right: 37px;
    text-align: center;
    margin-top: 50px;
    border:3px solid #FFF338;
    height:90px;
    border-radius:50%;
    -moz-border-radius:50%;
    -webkit-border-radius:50%;
    width:90px;
}

.ratings {
  font-size: 30px;
  margin-top: 12px;
}

.big-half , .small-half {
  font-family: "roboto", sans-serif;
  font-style: oblique;
  color: white;
}

.small-half {
  color: #DAD0C2;
  font-size: 19px;
}

.visit-movie-button {
  margin: 30px, 20px;
  padding: 10px, 30px;
  position: relative;
  top: 50px;
  left: 120px;
  font-size: 20px;
  outline-style: solid;
  color: #FFF338;
  outline-color: #FFF338;
  outline-offset: 10px;
}

.generate-movie-button {
background-color: #FFF338;
padding: 0.5em 1.2em;
font-size: 20px;
text-decoration: none;
position: relative;
top: 50px;
left: 250px;
text-transform: uppercase;
}

.action-buttons {
  width: inherit;
}

.title {
  font-size: 50px;
  padding-top: 40px;
  padding-left: 30px;
  margin-bottom: 0;
}

.top-information {
  display: flex;
  justify-content: space-between;
}

.supporting-info {
  padding-left: 30px;
  font-weight: bold;
  margin-bottom: 20px;
}

.lower-information {
  font-family: "roboto", sans-serif;
  width: 800px;
  max-width: 800px;
  margin-left: 380px;
}
```

Une fois de plus, vous pouvez accéder au code complet de ce projet depuis son dépôt [Github](https://github.com/KingsleyUbah/harperdb-movie-generator).

### Comment ajouter le composant Movie

Nous devons maintenant ajouter notre composant Movie. Nous allons commencer par créer un nouveau dossier sous le répertoire 'src' nommé `component`. Nous devons ensuite créer un nouveau fichier à l'intérieur de ce nouveau fichier nommé 'movie.js'. C'est ici que les choses intéressantes commencent à se produire.

En plus des bibliothèques React et ReactDOM, nous allons également importer le hook (fonction) use-harperdb.

Nous allons exécuter la fonction use-harperdb, en passant un objet comme argument. À l'intérieur de l'objet, nous devons fournir au moins une propriété de requête. Cette propriété détermine le type d'opération que nous voulons effectuer sur notre base de données.

```js
import React from 'react';
import { useHarperDB } from 'use-harperdb';

function Movie() {
let [data, loading, error, refresh] = useHarperDB({
    query: {
      operation: 'sql',
      sql: `select * from collection.movie where id = ${Math.floor(Math.random() * 8) + 1}`
    },
    interval: 40000 // 40 Secondes
  }
  )
  
  // CODE CONTINUES
```

La première propriété, qui est la propriété operation, spécifie comment vous voulez interroger les données. Dans notre exemple, nous allons le faire avec une commande SQL.

La deuxième propriété dans la requête est la propriété SQL. C'est ici que nous écrivons nos requêtes SQL pour toute opération CRUD que nous voulons effectuer. Dans notre cas, nous voulons simplement sélectionner tous les champs d'un film sélectionné aléatoirement entre 1-8, à partir de la base de données, que nous avons désigné par la clause SQL suivante :

```c
select * from collection.movie where id = ${Math.floor(Math.random() * 8) + 1}`
```

Après la requête, une autre propriété optionnelle que nous pouvons définir est la propriété interval. Avec cette propriété, vous pouvez spécifier combien de temps vous voulez que votre application attende avant de générer automatiquement une nouvelle requête à la base de données.

L'exécution de la fonction `useHarperDB` avec ces paramètres correctement passés nous retournera un tableau contenant certaines choses importantes. Voici quatre éléments importants que nous obtiendrons de `useHarperdDB` :

* `loading` : Il s'agit d'un booléen qui spécifie si la base de données traite encore les données ou non. Ainsi, vous pouvez éventuellement afficher un indicateur de chargement.

* `error` : Cela indique si une erreur a été rencontrée lors de l'interrogation de la base de données.

* `refresh` : En supposant que vous ne définissez pas de propriété d'intervalle, vous pouvez appeler cette fonction chaque fois que vous voulez récupérer de nouvelles données.

* `data` : La chose principale. Si tout se passe bien, HarperDB retournera nos données à cette variable.

## Comment afficher les données dans notre front-end

Avec nos données maintenant retournées avec succès de la base de données, il est temps de les passer dans notre modèle React :

```js
if(loading) {
    return <div> Chargement... </div>
  }

if(data) {
      return (
<>
<div className="movie-cover">
  <div className="top-information">
    <h2 className="title">{data[0].title}</h2>
    <div className="circle">
      <div className="ratings">
        <span className="big-half">{data[0].rating}</span>/<span className="small-half">10</span>
      </div>
    </div>
  </div>

  <div className="supporting-info">
    <span className="year">{data[0].date}</span> -
    <span className="time">{data[0].hours}h:{data[0].minutes}m</span>
  </div>
  <div className="image">
    <img src={data[0].cover} alt="Image du film" />
  </div>
</div>

<div className="genres">
  <ul className="movie-genres">
    {data[0].genres.map((genre, index) => {
    return (
    <li key={index}><span className="movie-genre-item">{genre}</span></li>
  )
    })}
  </ul>
</div>

<div className="lower-information">
  <p>{data[0].description}</p>

  <hr />
  <p> Avec : {data[0].stars.map((star, index) => {
    return (
    <span key={index}>{star} - </span>
    )
    })}
  </p>
  <hr />
  <p> Écrivains :
    {data[0].writers.map((writer, index) => {
      return (
    <span key={index} className="writer">{writer} - </span>
    )
    })}
  </p>
  <hr />
  <p>Réalisateurs :
    {data[0].directors.map((director, index) => {
      return (
    <span key={index} className="director">{director} - </span>
    )
    })}
  </p>
  <hr />
  <div className="action-buttons">
    <a href={data[0].website} className="visit-movie-button">Visiter le film</a>
    <a href="" className="generate-movie-button" onClick={refresh}>GÉNÉRER UN NOUVEAU FILM</a>
  </div>
</div>
</>
)
} else {
    return (
      <div>Désolé, aucune donnée
        {error}
      </div>
  )
}

}
```

Si vous êtes familier avec React, cela ne devrait pas vous être étranger. Mais je vais quand même expliquer ce que nous avons fait ici :

* Comme je l'ai mentionné, la fonction `useHarperDB` retournera nos données. Si vous interrogez pour obtenir tous les films, elle retournera un tableau de films. Puisque nous avons interrogé pour un seul film, elle retournera un objet contenant les données d'un seul film.

* Ensuite, nous devons vérifier si les données ont été retournées. Si aucune donnée n'est disponible, nous affichons un simple div affichant un message "Désolé, aucune donnée".

* Puisque nous avons reçu des données, nous les avons passées dans notre modèle. Nous extrayons chaque champ de l'objet et le passons dans le modèle correct.

Lorsque nous avons terminé, nous exécutons la commande suivante sur la ligne de commande :

```c
npm start
```

Cela devrait démarrer notre serveur de développement à l'adresse [https://localhost:3000](https://localhost:3000). Si tout se passe bien, nous devrions voir notre application en direct sur le navigateur avec des données de films sympas !

![Image](https://www.freecodecamp.org/news/content/images/2021/08/MovieListCover.png align="left")

*À quoi notre application devrait ressembler*

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Generate-new-movie.png align="left")

**C'est tout pour notre application !**

## Comment déployer l'application sur GitHub Pages

Bienvenue dans la dernière section du tutoriel. Nous allons déployer notre nouvelle application sur GitHub Pages pour que le monde puisse la voir.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Github-pages-1.png align="left")

*Déployer sur GitHub Pages*

Si vous avez un autre fournisseur d'hébergement, vous êtes absolument libre de déployer votre application là-bas. Si vous n'en avez pas, ou si vous voulez quelque chose de gratuit, alors GitHub Pages est idéal.

Tout d'abord, vous devez avoir un compte GitHub. Si vous n'en avez pas, vous pouvez en créer un pour vous-même [ici](https://github.com/join).

De plus, vous devez avoir le logiciel de contrôle de version Git installé sur votre machine locale. C'est quelque chose que tout développeur de logiciels devrait déjà avoir. Cependant, si vous ne l'avez pas, vous pouvez l'installer à partir d'[ici](https://git-scm.com/downloads).

La première chose à faire est de créer un nouveau dépôt pour votre projet sur votre compte GitHub :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Create-a-New-Repository-1.png align="left")

*Création d'un nouveau dépôt GitHub*

![Image](https://www.freecodecamp.org/news/content/images/2021/08/repo-1.png align="left")

Ensuite, retournez au terminal et exécutez la commande suivante :

```c
npm install gh-pages --save-dev
```

Cela enregistrera GitHub Pages dans votre projet en tant que dépendance de développement.

Lorsque cela est fait, allez dans le dossier de votre projet et ouvrez le fichier package.json. Vous devriez trouver gh-page installé en toute sécurité sous la dépendance de développement :

```c
"devDependencies": {
    "gh-pages": "^3.2.3"
  }
```

Ensuite, nous allons faire les trois choses suivantes :

1. Accédez à votre répertoire de projet (harperdb-movie-generator) et sélectionnez le fichier package.json. En haut de votre package json, vous ajouterez les données suivantes (remplacez le modèle par le vôtre) :

```c
"homepage":  https://{Votre nom d'utilisateur GitHub ici}.github.io/{Nom de votre projet}.git
```

Pour trouver votre nom d'utilisateur GitHub et le nom de votre dépôt, accédez au dépôt nouvellement créé sur GitHub. En haut, vous pouvez trouver votre nom d'utilisateur GitHub et le nom du projet à côté. Copiez les deux et remplissez le modèle mentionné ci-dessus – assurez-vous d'ajouter .git à la fin du nom de votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/project-name-and-username.png align="left")

*Informations GitHub pour votre package.json*

L'essence d'ajouter le champ "homepage" est de spécifier l'URL où notre application sera finalement hébergée. Assurez-vous de mettre une virgule à la fin, afin que votre package json soit analysé correctement.

2. Accédez au champ "scripts" dans le même fichier et passez les données suivantes en veillant à maintenir une indentation correcte :

```c
"predeploy": "npm run build",
"deploy": "gh-pages -d build"
```

C'est ce que vous exécuterez lorsque vous serez prêt à déployer sur GitHub Pages.

3. Enfin, vous allez initialiser Git dans votre projet. Pour ce faire, accédez simplement à votre répertoire de projet sur la ligne de commande et exécutez la commande suivante :

```c
cd projects/harperbd-movie-generator

git init
```

Maintenant, tout est prêt !

La seule chose qui reste à faire est de déployer votre application sur GitHub Pages. Pour ce faire, exécutez la commande suivante :

```c
npm run deploy
```

Et voilà ! Votre application sera immédiatement déployée sur GitHub Pages.

## Comment voir votre application en direct

Votre application est maintenant en ligne à ce stade, mais vous devez voir à quoi elle ressemble. Vous devez donc obtenir son URL.

Accédez à votre profil GitHub et cliquez sur l'onglet dépôt. Sélectionnez votre dépôt nouvellement créé, allez sur la page des paramètres et faites défiler un peu. Vous trouverez la section GitHub Pages. Cliquez sur "vérifiez-le ici !"

![Image](https://www.freecodecamp.org/news/content/images/2021/08/GIT1.png align="left")

Dans la page suivante, dans Source, basculez la branche sur "gh-pages" et le chemin du fichier sur "root". Dans quelques minutes, votre application sera prête. Copiez l'URL de la page et collez-la dans une nouvelle fenêtre de navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/git2.png align="left")

*Projet maintenant en ligne à l'URL fournie*

Et voici, vous verrez votre projet en direct.

## Conclusion

Nous avons construit ce projet avec React et HarperDB. HarperDB est un excellent choix pour la gestion de vos données et les opérations back-end.

Non seulement il est flexible, mais aussi très facile à intégrer, comme nous l'avons vu dans ce tutoriel.

Vous ne devriez pas vous arrêter ici. Vous pouvez améliorer vos compétences en construisant d'autres projets sympas avec cette même pile. Grâce au plan gratuit de HarperDB, vous n'avez rien à payer.

Vous pouvez récupérer le code de ce projet depuis son [dépôt GitHub](https://github.com/KingsleyUbah/harperdb-movie-generator).

Vous souhaitez me contacter pour des suggestions ? Vous pouvez me trouver sur [Twitter](https://twitter.com/ubahthebuilder)

C'est tout. Merci d'avoir suivi et passez une excellente semaine.