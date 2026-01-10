---
title: Tutoriel GraphQL – Comment interroger l'API Rick and Morty
subtitle: ''
author: Velda Kiara
co_authors: []
series: null
date: '2023-05-30T18:07:33.000Z'
originalURL: https://freecodecamp.org/news/graphql-queries-for-everyone
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/cover-image--1-.png
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
seo_title: Tutoriel GraphQL – Comment interroger l'API Rick and Morty
seo_desc: "I enjoy fictional books about greek gods, demigods, the oracle, and prophecies.\
  \ \nI am a huge fan of Rick Riordan's books. I recently came across Apollo's Trials,\
  \ based on the greek god Apollo. \nWhen I hear any mention of Apollo, my mind goes\
  \ to the g..."
---

J'apprécie les livres de fiction sur les dieux grecs, les demi-dieux, l'oracle et les prophéties. 

Je suis un grand fan des livres de Rick Riordan. J'ai récemment découvert Apollo's Trials, basé sur le dieu grec Apollon. 

Quand j'entends parler d'Apollon, mon esprit va vers le dieu grec qui était le dieu de pratiquement tout – y compris, mais sans s'y limiter, la musique, la poésie, l'art, la prophétie, la vérité, le tir à l'arc, la peste, la guérison, le soleil et la lumière.

[Apollo client](https://www.apollo%5BGraphQL%5D(https://graphql.org/).com/tutorials/), tout comme le dieu Apollon, peut faire beaucoup de choses. Par exemple, il vous permet de récupérer et de gérer des données depuis une API [GraphQL](https://graphql.org/) dans votre application côté client. Il est également simple, flexible et compatible avec toute source de données.

Dans cet article, nous allons utiliser le client Apollo pour récupérer des données depuis l'[API Rick and Morty](https://rickandmortyapi.com/%5BGraphQL%5D(https://graphql.org/)), nommée d'après la série télévisée animée du même nom. Nous allons écrire une [requête GraphQL](https://www.freecodecamp.org/news/5-ways-to-fetch-data-React-GraphQL/) pour récupérer les données dont nous avons besoin. Les données seront ensuite affichées en utilisant React.

Avant de commencer le projet, passons en revue les cas d'utilisation de GraphQL et comment il diffère des API REST.

## Quels sont les cas d'utilisation de GraphQL ?

GraphQL est utilisé pour construire des applications qui nécessitent une synchronisation de données en temps réel, comme les applications de chat. Il permet aux développeurs de récupérer les données nécessaires, réduisant ainsi le transfert de données sur le réseau et améliorant les performances de l'application.

Les microservices gèrent des fonctionnalités ou des caractéristiques spécifiques de l'application, ce qui pose un défi aux développeurs de travailler avec plusieurs API individuellement. 

GraphQL permet aux développeurs de créer une seule API qui agit comme une passerelle vers de nombreux microservices. Il améliore également les performances puisque une seule requête récupère divers microservices en une seule demande.

GraphQL fournit un schéma auto-documenté, ce qui facilite la compréhension du modèle de données et des relations entre les données par les développeurs. Il simplifie également le processus de création, de test et de maintenance de l'API, réduisant ainsi le temps et les coûts.

Enfin, GraphQL offre des capacités de versionnement pour permettre l'évolution du schéma de l'API sans casser les clients existants. Le versionnement est possible puisque les clients spécifient les données exactes dont ils ont besoin, ce qui facilite l'ajout de nouveaux champs et la suppression de ceux qui sont obsolètes sans affecter les clients existants.

## Quelles sont les différences entre GraphQL et les API REST ?

Avec GraphQL, le client envoie une requête avec les données dont il a besoin, et le serveur répond avec ces données uniquement. En revanche, avec les [API REST](https://www.freecodecamp.org/news/build-consume-and-document-a-rest-api/), le client envoie une requête à un endpoint, et le serveur répond avec toutes les données/réponses liées à cet endpoint.

Les API REST sont basées sur les ressources, où les endpoints représentent des données qui peuvent être accédées, créées, mises à jour ou supprimées. En revanche, GraphQL est basé sur les graphes, où chaque nœud représente une relation entre des objets.

Les API REST retournent des données au format JSON (JavaScript Object Notation) ou XML (Extensible Markup Language). En même temps, GraphQL permet au client de spécifier les données dont il a besoin et répond avec un objet JSON correspondant à la requête.

GraphQL fournit un versionnement pour permettre l'évolution de l'API sans perturber les clients existants, tandis que les API REST créent de nouveaux endpoints pour chaque version.

Dans certains cas, les API REST peuvent souffrir de sur-récupération ou de sous-récupération, où le serveur peut envoyer trop ou trop peu de données. GraphQL résout ce problème en permettant aux clients de demander les données dont ils ont besoin, réduisant ainsi la quantité de données transférées sur un réseau.

## Installation du projet

Maintenant que vous êtes familiarisé avec ce que vous pouvez faire avec GraphQL, commençons à construire le projet.

### Prérequis

* Connaissances de base sur [React](https://react.dev/)
* Comprendre le fonctionnement des [APIs](https://www.freecodecamp.org/news/how-apis-work/) et des [CSS (Cascading Style Sheets)](https://www.freecodecamp.org/news/learn-css-in-this-free-6-hour-video-course/)

### Installation des dépendances

Créez une nouvelle application React nommée "rickandmorty".

```js
 npm init [React](https://react.dev/)-app rickandmorty 

```

ou

```js
npx create-[React](https://react.dev/)-app rickandmorty 

```

Installez Apollo Client et GraphQL. Le code ci-dessous installe deux dépendances :

1. @apollo/client contient tout ce dont vous avez besoin, comme un cache en mémoire, une gestion d'état locale, une gestion des erreurs et une couche de vue basée sur React.
2. GraphQL fournit la logique pour analyser les requêtes.

```js
npm install @apollo/client [GraphQL](https://graphql.org/)

```

### Configuration de l'API Rick & Morty et d'Apollo Client

Une fois le projet configuré, nous devons commencer à l'utiliser dans nos fichiers. Ensuite, naviguez vers votre fichier `index.js` en utilisant la commande `cd`, et ajoutez le code suivant :

```js
import [React](https://react.dev/)DOM from '[React](https://react.dev/)-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client';

const client = new ApolloClient({
  uri: 'https://rickandmortyapi.com/[GraphQL](https://graphql.org/)',
  cache: new InMemoryCache(),
});

const root = [React](https://react.dev/)DOM.createRoot(document.getElementById('root'));
root.render(
  <ApolloProvider client={client}>
  <App />
</ApolloProvider>,
);

```

Le code ci-dessus crée une instance du client Apollo avec l'URL (Uniform Resource Locator) de l'endpoint GraphQL de l'API Rick and Morty. 

Le composant App est enveloppé avec le composant fournisseur Apollo pour passer le client à tous les composants enfants.

### Implémentation de la requête

Maintenant, créez un fichier appelé `characters.js` à l'intérieur du dossier `src`. Le fichier contiendra la requête et toute autre fonction que vous souhaitez ajouter.

À l'intérieur du fichier, ajoutez le code suivant :

```js
import { gql } from '@apollo/client';

export const GET_CHARACTERS = gql`
query Characters{
    characters{
      results {
        name
        species
        status
        type
        gender
        origin{name}
        location {name}
        image
      },
    },
  }
`;

```

Dans le code ci-dessus, nous importons `gql` depuis `@apollo/client` pour définir notre requête.

Nous créons et exportons la variable `GET_CHARACTERS` sous forme de chaîne avec des lettres majuscules. La capitalisation est considérée comme une bonne pratique lors de la définition des requêtes en GraphQL. Il est également considéré comme une bonne pratique d'envelopper les chaînes avec un littéral de modèle.

Les objets en JavaScript sont des collections ou des conteneurs remplis de paires clé-valeur. Une paire clé-valeur est appelée une propriété.

La requête, dans notre cas, recherche les personnages de Rick and Morty. Elle retourne un objet avec la propriété `results`, qui est un tableau d'objets de personnages. 

Chaque personnage a des propriétés comme le nom, l'espèce, le statut, le type, le genre et l'image - vous pouvez choisir ce que vous voulez récupérer 😉. 

Les autres propriétés, origin et location, sont des objets avec une propriété name pour l'origine et l'emplacement de chaque personnage.

#### Définition de la fonction Character

Dans le fichier `character.js`, ajoutez le code suivant sous la requête `GET_CHARACTERS` après l'avoir modifiée comme indiqué ci-dessous :

```js
import { useQuery, gql } from '@apollo/client';
import { useState } from "[React](https://react.dev/)";
import  { RandomCharacter } from './randomcharacters';
import './App.css';

export const GET_CHARACTERS = gql`
query Characters($name: String){
    characters ( filter: {name: $name}){
      results {
        name
        species
        status
        type
        gender
        origin{name}
        location {name}
        image
      },
    },
  }
`;

export function CharacterList() {
  const [searchTerm, setSearchTerm] = useState("");
  const {loading, error, data }   = useQuery(GET_CHARACTERS, {variables: {name: searchTerm}});
  const handleChange = (event) => {
    setSearchTerm(event.target.value);
  };
  return (
    <div>
      <input type="text" name="search" placeholder="Rechercher des personnages de Rick and Morty..." value={searchTerm} onChange={handleChange} className="search-input"  /> 
      {loading && (
            <div className="loader-container">
              <div className="loader"></div>
            </div>
       )}
      {error && <p> erreur </p> }
      {data?.characters.results.length === 0 && (<>   <RandomCharacter/> </>)}
      {data && data.characters.results.map((character) => (
        <div className="card" key={character.name} style={{ backgroundImage: `url(${character.image})`,backgroundRepeat: 'no-repeat'}}> 
          <div className="info"> 
          <h2 className="h3"> {character.name}</h2>
          <p> Statut: {character.status}</p>
          <p> Espèce: {character.species} </p>
          <p> Type: {character.type}</p>
          <p> Genre: {character.gender}</p>
          <p> Origine: {character.origin.name}</p>
          <p> Emplacement: {character.location.name}</p>
        </div>
        </div> 
      ))}
    </div> 
  );
}

```

La fonction `export function CharacterList()` crée une fonction qui est également exportée et peut être utilisée par d'autres parties du code. 

La variable `searchTerm` initialise l'état de recherche à une chaîne vide et crée une fonction `setSearchTerm` pour mettre à jour la valeur. 

Le hook `useQuery` de la bibliothèque `@apollo/client` récupère les données de l'API. 

La requête passe `GET_CHARACTERS` et une variable nommée `searchTerm` qui est une variable pour contenir les noms des personnages recherchés. 

La variable `handleChange` définit la valeur de `searchTerm` à la valeur actuelle du champ de saisie. Le champ `input` est la barre de recherche que l'utilisateur utilisera pour rechercher les noms des personnages qu'il souhaite voir. L'état est géré par `handleChange`.

Nous devons également tenir compte des problèmes de chargement du site, ainsi que des bugs qui peuvent survenir. 

`loading` est rendu dynamiquement avec un spinner si le chargement est défini sur `True`. Un message d'erreur est affiché si l'erreur est définie sur `True`. 

Lorsque l'utilisateur recherche un personnage qui n'existe pas, nous voulons présenter un message et un autre personnage dont il peut trouver plus d'informations – c'est là que `RandomCharacter` intervient. Nous le définirons plus tard. Pour l'instant, laissons-le tel quel.

Une fois que nous avons récupéré les données, nous mappons le tableau `data.characters.results` à la carte de chaque personnage. 

Nous voulons également changer l'arrière-plan des cartes pour représenter le personnage dont les informations sont affichées. La propriété `backgroundImage` dans `style` gère le changement dynamique des images. Le reste des éléments est affiché sous forme de texte sur la carte.

### Comment afficher les données

Maintenant que nous avons une fonction qui fonctionne, nous devons voir ce qui est affiché dans le navigateur, et si nous pouvons faire des requêtes et obtenir les données dont nous avons besoin. 

Dans votre fichier `App.js`, ajoutez le code suivant :

```
function App() {
  return (
    <div>
    <h1 style={{ textAlign: 'center' }} >Personnages de Rick and Morty</h1>
    <CharacterList />
  </div>
      );
    }

```

Le composant `<CharacterList />` affiche les informations sur les personnages que nous obtenons de l'API.

### Comment randomiser les personnages

Rappelons que nous avons appelé le composant `RandomCharacter` mais que nous ne l'avons pas encore défini. 

Créez un fichier appelé `randomcharacters.js` dans `src` et ajoutez le code suivant :

```
import { useQuery } from "@apollo/client";
import { gql } from '@apollo/client';
import { useState } from "[React](https://react.dev/)";
import './App.css';

export const GET_SINGLE_CHARACTER = gql`
query Character($id: ID!){
    character   (id: $id) {
        name
        species
        status
        type
        gender
        origin{name}
        location {name}
        image
      },
    },
`;

export const RandomCharacter = () => {
    const [randomNumber, setRandomNumber] = useState(Math.floor(Math.random() * 200));
    const { loading, error, data } = useQuery(GET_SINGLE_CHARACTER, {variables: {id: randomNumber } });
    

  return (
    <div>
       <p className="intro" >
         Désolé, nous n'avons pas trouvé ce personnage 😞  
         <br/>
         <br/>
         Et si vous essayiez celui-ci à la place ? 😉 </p>

      {/* {loading && <p>loading...</p>} */}
      {loading && (
            <div className="loader-container">
              <div className="loader"></div>
            </div>
       )}
      {error && <p> erreur </p> }
      {data && (<> 
        <div className="card" key={data.character.name} style={{ backgroundImage: `url(${data.character.image})`,backgroundRepeat: 'no-repeat'}}> 
        <div className="info"> 
          <h2 className="h3">{data.character.name}</h2>
          <p>Statut: {data.character.status}</p>
          <p>Espèce: {data.character.species}</p>
          <p>Type: {data.character.type}</p>
          <p>Genre: {data.character.gender}</p>
          <p>Origine: {data.character.origin.name}</p>
          <p>Emplacement: {data.character.location.name}</p>
        </div>
        </div>
      </>
      )}
    </div>
  );
};

```

Nous allons reproduire la requête que nous avons créée dans le fichier `characters.js`, et la renommer en `GET_SINGLE_CHARACTER`. Au lieu de chercher des noms, nous allons chercher des `ID`. 

Nous cherchons des `ID` parce qu'ils sont uniques, et nous voulons randomiser les personnages qui seront sélectionnés une fois qu'un utilisateur ne trouve pas le personnage qu'il cherche.

`randomNumber` initialise l'état à la fonction `Math.floor` qui génère un nombre aléatoire entre 0 et 199 inclus, en utilisant la méthode `Math.random()` et en le multipliant par 200. 

La fonction `Math.floor` arrondit le résultat de l'expression à l'entier le plus proche. Chaque fois que `randomNumber` doit être mis à jour, la fonction `setRandomNumber` prend une nouvelle valeur comme argument et met à jour l'état.

Nous avons un message pour alerter l'utilisateur que le personnage qu'il cherche n'est pas trouvé, mais qu'il peut consulter un nouveau personnage. 

Le spinner de chargement est également implémenté dans ce composant, et les erreurs sont là au cas où des problèmes surviennent. Les images et les cartes sont similaires au format `characters.js` puisque nous voulons une cohérence dans l'apparence de tout.

### Comment styliser l'affichage

Nous allons utiliser CSS pour styliser l'apparence des cartes, ainsi que la barre de recherche et la page générale.

Ayant défini les fonctions et les composants, nous allons ajouter des attributs `className` à ce qui doit être stylisé.

Ajoutez le code suivant :

```js
@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,700);
body{
  background: navajowhite;
  font-family: Roboto, veranda;
  padding-bottom: 4em;
}
.card{
  position: relative;
  width: 22em;
  height: 30em;
  background-size: 22em 30em;
  box-shadow: 3px 3px 20px rgba(0,0,0,0.5);
  margin: auto;
  overflow: hidden;
  margin-bottom: 2em;
}
.card *{
  position: relative;
  z-index: 2;
}
.card:hover .info{
  bottom: -3em;
  opacity: 1;
  padding: 2px 1px;
  background-color: navajowhite;
}
.info{
  font-family: 'Droid Serif', serif;
  font-size: 1.2em;
  color: black;
 
  line-height: 1.1em;
  padding: 0 2em;
  position: relative;
  bottom: -4em;
  opacity: 0;
  background: transparent;
  transition: opacity 0.3s, bottom 0.3s;
  text-align: center;
}
/* search  bar*/
input[type="text"] {
  border: none;
  border-radius: 10px;
  background-color: #f2f2f2;
  padding: 10px;
  width: 500px;
  margin: 0 auto;
  display: block;
  font-size: 16px;
  font-family: 'Roboto', sans-serif;
  box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
  margin-bottom: 2em;
}

input[type="text"]::placeholder {
  color: #999;
  font-style: italic;
}
/* no result */
.intro{
/* width: 10px; */
text-align: center;
margin: 0 auto;
color:black;
font-family: 'Droid Serif', serif;
font-size: 23px;
font-style: italic;
line-height: 20px;
padding-bottom: 15px;
}
/* spinner */
.loader-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}

.loader {
  border: 8px solid #f3f3f3; 
  border-top: 8px solid black;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}


```

Points à noter :

* La classe `.card` représente l'apparence de la carte.
* La classe `.info` représente le texte du corps pour les personnages, comme l'espèce.
* La classe `.intro` représente le texte qui apparaît si le personnage n'est pas trouvé.
* La classe `.loader` représente le spinner qui s'affiche avant que les résultats ne soient affichés.

Votre site web devrait maintenant ressembler à [celui-ci](https://graphymorty.netlify.app/).

## Conclusion

Dans cet article, vous avez appris comment utiliser les requêtes GraphQL avec React, gérer l'état en utilisant le hook useState et styliser les différents composants de l'application web.

Que votre clavier soit rapide, vos bugs peu nombreux et votre compteur de plaisir à son maximum pendant que vous codez !