---
title: Comment récupérer des données d'API dans React en utilisant Axios
subtitle: ''
author: Oluwadamisi Samuel
co_authors: []
series: null
date: '2025-07-01T20:33:34.211Z'
originalURL: https://freecodecamp.org/news/how-to-fetch-api-data-in-react-using-axios
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751385483454/7e7949aa-4bcd-4f58-9725-36df67b866a5.png
tags:
- name: React
  slug: reactjs
- name: APIs
  slug: apis
- name: Frontend Development
  slug: frontend-development
- name: axios in react
  slug: axios-in-react
seo_title: Comment récupérer des données d'API dans React en utilisant Axios
seo_desc: Learning how to fetch data from APIs is a must-have skill for any developer.
  Whether you're building a simple portfolio site or working on real-world applications,
  you'll often need to connect to external data sources. Being comfortable with API
  call...
---

Apprendre à récupérer des données à partir d'API est une compétence indispensable pour tout développeur. Que vous construisiez un simple site portfolio ou que vous travailliez sur des applications réelles, vous aurez souvent besoin de vous connecter à des sources de données externes. Être à l'aise avec les appels API montre que vous êtes prêt à contribuer à des projets réels et à bien travailler en équipe.

Ce tutoriel pour débutants est conçu pour les développeurs juniors et toute personne nouvelle dans React. Vous apprendrez à récupérer des données à partir d'une API, puis à les stocker et à les afficher dans votre application React. Aucune connaissance avancée requise – nous allons décomposer tout cela étape par étape, afin que vous puissiez suivre et gagner en confiance au fur et à mesure.

Nous allons utiliser React, Vite, Axios et Tailwind CSS pour construire une application simple qui récupère et affiche des données à partir d'une API publique. Tout d'abord, nous allons récupérer des données en utilisant la méthode fetch intégrée. Ensuite, nous allons la refactoriser en utilisant Axios, une bibliothèque populaire qui simplifie les requêtes HTTP.

## Prérequis

Pour suivre cet article, vous devez :

* Être familier avec les concepts de base de React comme les composants et useState

* Savoir ce qu'est une API et qu'elle retourne des données (généralement en JSON)

* Avoir une certaine expérience avec les promesses JavaScript et la méthode .then(). (Si vous avez déjà vu ou utilisé .then(), c'est suffisant – nous allons nous appuyer sur cela).

* Être à l'aise avec l'utilisation de map() pour rendre des listes à partir de tableaux (les données que nous obtenons de l'API)

* Être capable d'exécuter un projet React en utilisant des outils comme Vite ou Create React App

## Table des matières

1. [Qu'est-ce qu'une API et pourquoi en avons-nous besoin ?](#heading-questce-quune-api-et-pourquoi-en-avons-nous-besoin)

2. [Types d'API que vous rencontrerez](#heading-types-dapi-que-vous-rencontrerez)

3. [Outils que nous utiliserons](#heading-outils-que-nous-utiliserons)

4. [Comment récupérer des données avec React](#heading-comment-recuperer-des-donnees-avec-react)

* [Comment récupérer des données avec fetch()](#heading-comment-recuperer-des-donnees-avec-fetch)

* [Refactoriser avec Axios](#heading-refactoriser-avec-axios)

5. [Comment gérer les états de chargement et d'erreur](#heading-comment-gerer-les-etats-de-chargement-et-derreur)

* [Qu'est-ce qu'un état de chargement ?](#heading-questce-quun-etat-de-chargement)

* [Qu'est-ce qu'un état d'erreur ?](#heading-questce-quun-etat-derreur)

6. [Comment garder vos clés API en sécurité](#heading-comment-garder-vos-cles-api-en-securite)

* [Pourquoi c'est important :](#heading-pourquoi-cest-important)

7. [API publiques amusantes pour s'entraîner](#heading-api-publiques-amusantes-pour-sentrainer)

8. [Conclusion](#heading-conclusion)

## Qu'est-ce qu'une API et pourquoi en avons-nous besoin ?

Une API, ou Interface de Programmation d'Applications, est un moyen pour différents systèmes de communiquer. Pensez à cela comme à un serveur dans un restaurant. Vous dites au serveur ce que vous voulez dans le menu (la requête), il prend cette commande à la cuisine (le serveur), puis ramène votre nourriture à la table (la réponse).

En développement web, les API permettent à votre application frontend de communiquer avec un service backend. La plupart du temps, cette communication se fait par le biais de requêtes HTTP. Vous faites une requête à une URL spécifique (appelée endpoint), et vous obtenez une réponse, généralement au format JSON (JavaScript Object Notation). JSON est léger, facile à lire et fonctionne bien avec JavaScript.

Voici un exemple de requête GET de base :

```javascript
GET https://jsonplaceholder.typicode.com/users
```

Cette requête GET demande au serveur une liste d'utilisateurs. La réponse ressemblera à quelque chose comme ceci :

```javascript
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "JohnDOe@email.com",
  },
  {
    "id": 2,
    "name": "Jane Doe",
    "email": "JaneDoe@email.com",
  },
   //...plus d'utilisateurs
]
```

Votre application React peut récupérer ce JSON, le stocker dans l'état et l'afficher dans le navigateur. C'est le cycle de base de l'API que vous verrez encore et encore dans les applications réelles :

* Faire la requête

* Attendre la réponse

* Analyser le JSON

* Utiliser les données dans votre UI

Comprendre les API et JSON est essentiel. Vous les utiliserez pour récupérer des profils d'utilisateurs, soumettre des formulaires, mettre à jour des tableaux de bord, rechercher des bases de données, et bien plus encore.

## Types d'API que vous rencontrerez

Toutes les API ne sont pas identiques. Comprendre les types d'API que vous rencontrerez vous aidera à savoir quels outils ou étapes vous devrez utiliser pour travailler avec elles.

### 1. API publiques (aucune clé requise)

Ce sont des API en accès libre que tout le monde peut utiliser. Elles ne nécessitent pas d'authentification ni de clé API. Elles sont idéales pour les tests, l'apprentissage et la construction d'applications de démonstration.

Exemple :

`GET https://jsonplaceholder.typicode.com/users`

### 2. API publiques (avec clé API)

Certaines API sont publiques, mais nécessitent tout de même une clé API. Cela aide le fournisseur à suivre l'utilisation et à prévenir les abus. Vous devrez généralement vous inscrire pour obtenir une clé gratuite.

Exemple :

`GET https://newsapi.org/v2/top-headlines?country=us&apiKey=VOTRE_CLE_API`

* `https://newsapi.org/v2/top-headlines` – l'endpoint API réel

* `country=us` – un paramètre de requête spécifiant que vous voulez les "titres US"

* `apiKey=VOTRE_CLE_API` – il s'agit de votre clé API personnelle que vous obtenez après vous être inscrit sur [newsapi.org](http://newsapi.org)

**Pour utiliser ces API, vous devrez :**

* Vous inscrire sur le site du fournisseur

* Stocker votre clé (en toute sécurité) dans votre application (nous explorerons cela plus tard)

* La passer en tant que paramètre de requête ou en-tête

### 3. API privées

Celles-ci sont généralement utilisées en interne dans les entreprises. Elles nécessitent souvent des formes d'authentification plus avancées, comme des jetons OAuth ou des cookies de session. Vous ne les utiliserez généralement pas sauf si vous travaillez sur le backend ou dans le cadre d'un projet d'équipe.

### 4. Utilisation de jetons Bearer pour l'authentification API

Lors de la manipulation d'API modernes, il est courant de rencontrer des API qui nécessitent une authentification utilisant un jeton Bearer au lieu d'une simple clé API dans l'URL. La seule différence ici est que vous passez un objet qui contient le jeton Bearer au lieu de simplement la variable de la clé API (par exemple, l'API The Movie Database (TMDB)).

Cette approche est plus sécurisée car elle garde le jeton hors de l'URL et de l'historique du navigateur. Elle s'aligne également sur les normes d'authentification basées sur les jetons comme OAuth 2.0.

**Note :** Lorsque vous travaillez avec des API tierces, vérifiez toujours la documentation pour voir comment l'authentification doit être gérée. Les méthodes d'authentification varient – certaines API nécessitent de passer la clé dans l'URL, d'autres l'attendent dans les en-têtes.

## Outils que nous utiliserons

* **React :** notre bibliothèque UI JavaScript de choix

* **Tailwind CSS :** Pour un style rapide

* **fetch :** Méthode native du navigateur pour faire des requêtes HTTP

* **Axios :** Bibliothèque optionnelle qui rend les requêtes plus pratiques

Apprendre à utiliser ces outils et méthodes facilitera l'adaptation à différentes méthodes et environnements de production.

## Comment récupérer des données avec React

Maintenant, vous devez comprendre la structure de base et les outils dont vous avez besoin pour récupérer des données avec React et stocker ces données pour les utiliser dans vos composants. Pour cela correctement, vous devrez comprendre quelques outils et concepts de base :

* **Hook useState :** Vous permet de créer et de gérer l'état local à l'intérieur de votre composant. Vous l'utiliserez pour contenir les données que vous récupérez, et suivre des choses comme si vous êtes toujours en train de charger ou s'il y a eu une erreur.

* **Hook useEffect :** Vous permet d'effectuer des opérations qui doivent s'exécuter après le rendu du composant, comme la récupération de données, l'abonnement à des événements, ou la mise à jour du DOM.

* **Requêtes HTTP :** C'est ainsi que vous communiquez avec les API. Vous pouvez utiliser la méthode fetch() native du navigateur ou des outils tiers comme Axios.

Un flux de base de récupération de données ressemble à ceci :

* Configurer l'état pour contenir vos données lorsqu'elles arrivent

* Utiliser le hook useEffect() pour faire l'appel API

* Gérer les états de chargement et d'erreur

* Stocker et afficher les données une fois qu'elles arrivent

Maintenant que vous avez les bases, passons en revue deux façons de récupérer des données : d'abord en utilisant fetch(), puis en utilisant Axios.

### Comment récupérer des données avec fetch()

La méthode fetch() est une fonctionnalité native du navigateur qui vous permet d'envoyer des requêtes HTTP directement depuis le frontend. Elle est utile pour faire des appels API de base sans aucune bibliothèque supplémentaire.

Pour utiliser fetch() dans React, vous suivrez généralement ce modèle :

* Utilisez le hook useEffect() pour vous assurer que l'appel fetch ne s'exécute qu'une seule fois lorsque le composant est monté.

* Appelez fetch('url') pour envoyer la requête HTTP GET.

* Utilisez .json() pour analyser la réponse JSON.

* Stockez la réponse dans l'état en utilisant useState().

**Voyons un exemple :**

Importez les hooks nécessaires et faites l'appel fetch à l'intérieur de useEffect.js :

```javascript
import { useEffect, useState } from 'react';

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(res => res.json())
      .then(data => setUsers(data));
   // res.json() convertit la réponse brute en JSON.
   // setUsers(data) met à jour l'état React avec ce JSON et le stocke dans l'état afin que vous puissiez y accéder.

  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Liste des utilisateurs (en utilisant fetch)</h1>
      <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {users.map(user => (
          <li key={user.id} className="bg-white shadow p-4 rounded-xl">
            <h2 className="text-lg font-semibold">{user.name}</h2>
            <p className="text-sm text-gray-600">{user.email}</p>
            <p className="text-sm text-gray-600">{user.company.name}</p>
          </li>
        ))}
      </ul>
    </div>
//Passer à travers les données stockées dans l'état et afficher le contenu
// dans une liste et accéder aux propriétés des données(user.name)
  );
}

export default App;
```

### Refactoriser avec Axios

Axios est une bibliothèque tierce qui rend les requêtes HTTP plus faciles et plus fiables. Bien que fetch() soit intégré au navigateur, Axios simplifie plusieurs choses, comme l'analyse JSON automatique et la gestion des erreurs plus propre.

#### Pourquoi utiliser Axios plutôt que fetch :

* Axios convertit automatiquement la réponse en JSON – vous n'avez pas besoin d'appeler .json() manuellement.

* Il a un support intégré pour les interceptors de requêtes et de réponses.

* Il facilite l'envoi d'en-têtes, la gestion des erreurs et le travail avec des requêtes non-GET (POST, DELETE, etc.).

**Tout d'abord, installez Axios dans votre projet via le terminal :**

`npm install axios`

Importez les hooks nécessaires et Axios et faites l'appel API à l'intérieur de useEffect.

```javascript
import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('https://jsonplaceholder.typicode.com/users')
      .then(response => setUsers(response.data);
      // response.data contient le JSON analysé de l'API.
      // setUsers(data) met à jour l'état React avec ce JSON et le stocke dans l'état afin que vous puissiez y accéder.
  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Liste des utilisateurs (en utilisant Axios)
      </h1>
      <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {users.map(user => (
          <li key={user.id} className="bg-white shadow p-4 rounded-xl">
            <h2 className="text-lg font-semibold">{user.name}</h2>
            <p className="text-sm text-gray-600">{user.email}</p>
            <p className="text-sm text-gray-600">{user.company.name}</p>
          </li>
        ))}
      </ul>
    </div>
//Passer à travers les données stockées dans l'état et afficher le contenu
// dans une liste et accéder aux propriétés des données(user.name)
  );
}

export default App;
```

## Comment gérer les états de chargement et d'erreur

Lorsque vous travaillez avec la récupération de données dans React, tout ne se passe pas toujours parfaitement. Parfois, les données mettent du temps à arriver et d'autres fois la requête échoue. Les états de chargement et d'erreur sont utiles car ils vous donnent des retours et rendent l'expérience à la fois conviviale et adaptée aux développeurs.

### Qu'est-ce qu'un état de chargement ?

Un état de chargement est utilisé pour montrer que des données sont en cours de récupération. Sans cela, les utilisateurs pourraient ne pas savoir ce qui se passe et penser que la requête n'a pas abouti ou que l'application ne fonctionne pas. Vous utilisez généralement un booléen pour suivre cela.

### Qu'est-ce qu'un état d'erreur ?

Un état d'erreur vous indique qu'un problème est survenu – peut-être que l'API est hors service, ou que l'URL était incorrecte. Capturer et afficher ces erreurs vous aide à déboguer plus rapidement et donne aux utilisateurs un retour clair.

#### Extrait de code :

Voici comment vous pourriez ajouter la gestion du chargement et des erreurs à une requête fetch() de base :

```javascript
const [users, setUsers] = useState([]);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);

useEffect(() => {
  fetch('https://jsonplaceholder.typicode.com/users')
    .then(res => {
      if (!res.ok) throw new Error('La réponse du réseau n\'est pas correcte');
      return res.json();
    })
    .then(data => {
      setUsers(data);
      setLoading(false);
    })
    .catch(err => {
      setError(err.message);
      setLoading(false);
    });
}, []);

if (loading) return <p>Chargement...</p>;
if (error) return <p>Erreur : {error}</p>;
```

Cela vous donne une expérience utilisateur plus fluide et rend votre application plus fiable.

## Comment garder vos clés API en sécurité

Si vous utilisez une API qui nécessite une clé, il est crucial de garder cette clé sécurisée. Ne codez jamais vos clés API directement dans vos composants React ou ne les poussez pas dans des dépôts publics. Au lieu de cela, stockez-les dans un fichier .env à la racine de votre projet (le même répertoire que votre fichier package.json). Dans votre fichier .env, faites ceci :

`VITE_API_KEY=votre_clé_réelle_ici`

Pour y accéder dans votre application, utilisez :

`const apiKey = import.meta.env.VITE_API_KEY;`

Vous pouvez ensuite utiliser cette clé dans vos requêtes API. Voici comment vous l'incluriez dans l'exemple Axios :

```javascript
axios.get(`https://api.example.com/data?apikey=${apiKey}`)
  .then(response => {
    setUsers(response.data);
    setLoading(false);
  })
  .catch(error => {
    setError(error.message);
    setLoading(false);
  });
```

**Note :** Dans Vite, toutes les variables d'environnement doivent commencer par VITE_ pour être accessibles dans le navigateur. Assurez-vous d'ajouter .env à votre fichier .gitignore afin qu'il ne soit pas poussé vers GitHub.

Cacher votre clé aide à prévenir l'exposition de celle-ci au public, surtout si votre projet est partagé sur GitHub ou déployé en ligne.

### Pourquoi c'est important :

* Les clés exposées peuvent être abusées, entraînant des dépassements ou des bannissements par le fournisseur d'API

* Vous pourriez perdre l'accès ou accumuler des frais selon le service

* Dans les applications sécurisées, les clés exposées peuvent être une faille de sécurité majeure

Traitez toujours vos clés comme des mots de passe. Si une clé est exposée, révoquez-la et générez-en une nouvelle depuis le tableau de bord de votre fournisseur d'API.

## API publiques amusantes pour s'entraîner

Voici quelques API gratuites et amusantes que vous pouvez utiliser pour construire des projets d'entraînement :

**1. JSONPlaceholder :** Fausses données pour les tests : utilisateurs, posts, commentaires, todos. Aucune clé requise.

**2. The Dog API :** Obtenez des images aléatoires, des informations sur les races et recherchez par race. Nécessite une clé API gratuite.

**3. The Cat API :** Comme The Dog API, mais pour les chats. Idéal pour les applications riches en images. Clé API gratuite.

**4. PokeAPI :** Récupérez des données détaillées sur les Pokémon. Idéal pour les cartes, les filtres de recherche ou les jeux. Aucune clé requise.

**5. TMDB API :** Obtenez des données sur les films, les émissions tendances, les détails des distributions, les affiches, et plus encore. Nécessite une clé API gratuite de TMDB (vous pouvez cloner des sites de streaming populaires avec cela).

**6. REST Countries API :** Récupérez les noms des pays, les capitales, les régions, les drapeaux et les populations. Aucune clé API requise.

**7. Bored API :** Obtenez des suggestions d'activités aléatoires pour quand vous êtes ennuyé. Aucune clé requise.

**8. JokeAPI :** Récupérez des blagues par catégorie ou type (safe for work, programmation, humour noir). Aucune clé nécessaire.

**9. Rick and Morty API :** Explorez les personnages, les lieux et les épisodes. Parfait pour les fans. Aucune clé requise.

**10. NASA APIs :** Explorez les images, les données astronomiques et les faits spatiaux. Nécessite une clé API gratuite de la NASA.

Amusez-vous avec différents formats de données, ajoutez des filtres ou des recherches, et combinez plusieurs API en un seul projet. C'est une excellente pratique pour le développement d'applications réelles.

## Conclusion

Ce que vous venez de construire est la base de nombreuses applications réelles. La capacité à récupérer, gérer et afficher des données à partir d'API est essentielle en développement web.

À partir de là, vous pouvez étendre cette application pour :

* Ajouter une fonctionnalité de recherche ou de filtrage

* Paginator les résultats

* Afficher les détails sur une page séparée

Au fur et à mesure que vous continuez à grandir en tant que développeur, les modèles que vous avez pratiqués ici réapparaîtront encore et encore. Les maîtriser maintenant vous prépare au succès plus tard.