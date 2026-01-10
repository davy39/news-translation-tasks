---
title: Comment utiliser JSON Server pour le développement front-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-08-21T13:54:28.000Z'
originalURL: https://freecodecamp.org/news/json-server-for-frontend-development
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Cover-image-for-my-json-server-article-on-freecodecamp.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: json
  slug: json
- name: React
  slug: reactjs
seo_title: Comment utiliser JSON Server pour le développement front-end
seo_desc: 'By Juliet Ofoegbu

  One of the most common responsibilities for front-end developers is handling the
  data in their front-end applications. You’ll need to be able to retrieve data from
  an API, manipulate it, and then render it on the screen in a modern ...'
---

Par Juliet Ofoegbu

L'une des responsabilités les plus courantes pour les développeurs front-end est la gestion des données dans leurs applications front-end. Vous devrez être capable de récupérer des données à partir d'une API, de les manipuler et de les afficher à l'écran dans une application web moderne pour les interactions utilisateur. 

Une communication efficace entre le front-end et le back-end est cruciale pour créer des applications fluides et réactives.

Imaginez maintenant un scénario où vous travaillez avec un développeur back-end sur un projet et vous attendez l'endpoint de l'API pour vous connecter à votre front-end. Il existe un excellent outil que les développeurs front-end peuvent utiliser pour créer une API fictive ou factice pendant la phase de développement. Cet outil s'appelle "JSON Server". 

Dans cet article, vous apprendrez à utiliser des serveurs JSON pour le stockage de données dans vos applications React. Vous en apprendrez davantage sur les fonctionnalités et les avantages, ainsi qu'une implémentation pratique dans un projet front-end. 

L'application permettra aux utilisateurs de voir une liste d'utilisateurs et leurs détails. Les données des utilisateurs seront créées à l'aide de JSON Server dans un fichier JSON dans l'application front-end.

## Qu'est-ce que JSON Server ?

JSON est l'acronyme de JavaScript Object Notation. JSON Server est un outil Node.js léger et facile à utiliser qui simule une API [RESTful](https://www.freecodecamp.org/news/what-is-rest-rest-api-definition-for-beginners/) en utilisant un fichier JSON comme source de données. Avec JSON Server, les développeurs front-end peuvent créer des API fictives sans avoir besoin d'écrire du code côté serveur complexe, ou lorsqu'une API back-end n'est pas encore prête. 

Cette API fictive envoie des requêtes à un endpoint qui sera fourni. Elle répond aux requêtes HTTP, ce qui la rend idéale pour le développement rapide pour les développeurs front-end. JSON Server permet également aux développeurs d'effectuer des opérations CRUD et de sauvegarder des données dans des fichiers JSON. JSON se présente sous forme de paires clé-valeur et est écrit dans ce format :

```json
{  
  "name": "Jane",   
  "age": 30,   
  "gender": "Female"
}
```

Les "name", "age" et "gender" sont appelés **propriétés** et les "Jane", "30" et "female" sont les **valeurs** de chacune des propriétés.

Le fichier de données JSON peut se présenter sous deux formats : le format tableau et le format objet avec des objets imbriqués.

**Format Tableau**

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "age": 25
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "age": 40
  }
]

```

**Format Objet avec Objets Imbriqués**

```json
{
  "users": {
    "1": {
      "name": "John Doe",
      "age": 25
    },
    "2": {
      "name": "Jane Smith",
      "age": 30
    }
  }
}
```

## Fonctionnalités de JSON Server

Voici quelques-unes des fonctionnalités de JSON Server :

* Il est facile et rapide à configurer. Il est également convivial pour les développeurs front-end et les développeurs back-end débutants.
* Il prend en charge les méthodes HTTP courantes comme les méthodes GET, POST, PUT et DELETE, tout comme un serveur d'API back-end réel le ferait.
* Avec JSON Server, vous pouvez effectuer des opérations de création, lecture, mise à jour et suppression (CRUD) sur les données pour construire une application interactive.
* JSON Server offre aux développeurs la possibilité de créer des routes personnalisées pour gérer des scénarios plus complexes.

## Avantages de l'utilisation de JSON Server

Voici quelques-uns des avantages de l'utilisation de JSON Server :

* JSON Server permet aux développeurs front-end de créer rapidement des prototypes d'API fonctionnels qui peuvent être testés et modifiés en attendant que le serveur back-end soit prêt.
* Les développeurs front-end peuvent utiliser JSON Server pour simuler différents scénarios et cas d'erreur lors des tests pour améliorer leur application.

## Comment configurer JSON Server dans une application

Vous aurez besoin de [Node.js](https://nodejs.org/en) et de [npm](https://www.npmjs.com/) installés sur votre système, car ils sont tous deux des prérequis pour cette configuration. 

Suivez ces étapes pour configurer et utiliser JSON Server dans votre application front-end :

### Étape #1 - Installer JSON Server

Pour installer JSON Server dans votre application, naviguez jusqu'à votre répertoire de projet dans votre terminal ou invite de commande et tapez cette commande : `npm install -g json-server`. 

Cela installera le serveur JSON globalement sur votre système. Si vous souhaitez l'installer localement pour un projet particulier, utilisez cette commande : `npm i json-server`.

### Étape #2 - Créer un fichier JSON

Créez un fichier JSON dans votre répertoire de projet qui servira de source de données. Ce fichier JSON doit avoir une extension de fichier `.json`. Que veux-je dire ? Supposons que vous souhaitiez que le nom de votre fichier JSON soit 'db', cela signifie que vous créerez un fichier appelé **db.json**.

### Étape #3 - Créer des données

Définissez vos données à l'intérieur du fichier JSON. Ces données JSON peuvent être un tableau d'objets ou un objet avec des objets imbriqués. Chaque objet représente une entité de données et doit avoir un identifiant unique.

### Étape #4 - Démarrer le serveur

Démarrez le serveur JSON en tapant cette commande dans votre terminal : `json-server --watch db.json`. Cela s'exécutera sur "https://localhost:3000" par défaut. Vous pouvez changer le port sur lequel il s'exécute en spécifiant un numéro de port différent lors du démarrage du serveur en utilisant le drapeau `--port`. 

Par exemple, si vous souhaitez que votre serveur s'exécute sur le port 8000 au lieu du port par défaut (3000), utilisez cette commande lors du démarrage du serveur : `json-server --watch db.json --port 8000`. Vous pouvez ensuite le visualiser dans votre navigateur sur le port 8000.

JSON Server générera automatiquement des endpoints RESTful basés sur les données que vous avez définies dans votre fichier JSON. 

Si vous avez un fichier JSON avec un tableau de "users", voici l'endpoint qui sera automatiquement généré par JSON Server :

* GET  /users - Cela récupère une liste de toutes les entités de ressources des utilisateurs.
* GET /users/:id - Cela récupère un utilisateur spécifique par son identifiant.
* POST /users - Cela crée un nouvel utilisateur.
* PUT /users/:id - Cela met à jour un utilisateur en fonction d'un identifiant spécifié.
* DELETE /users/:id - Cela supprime un utilisateur en fonction de l'identifiant spécifié.

Ce modèle facilite l'interaction avec l'API fictive de manière RESTful, tout comme on le ferait avec une véritable API back-end.

## Comment construire une application front-end simple en utilisant JSON Server

Pour mieux comprendre comment utiliser JSON Server dans un projet réel, examinons un exemple. Vous allez construire une application React.js simple qui affiche les données des utilisateurs à partir d'un fichier de données JSON en utilisant le serveur JSON sur le front-end. 

Prêt ? Commençons. Voici un aperçu rapide de l'application que vous allez construire à la fin de cet article.

![Page d'accueil de l'application de données utilisateur](https://www.freecodecamp.org/news/content/images/2023/08/json-2.png)
_Page d'accueil de l'application de données utilisateur_

Cette application n'aura que deux pages. La première page est affichée ci-dessus, et c'est une liste d'utilisateurs avec leurs noms et adresses e-mail. L'autre page contiendra plus de détails sur chaque utilisateur en fonction de l'identifiant de l'utilisateur lorsque le bouton **Voir les détails complets** est cliqué.

### Installation des dépendances

Créez une application React en utilisant CRA ou Vite (recommandé). J'ai utilisé le gestionnaire de paquets yarn pour créer mon application avec cette commande : `yarn create vite`. Choisissez un nom de projet et sélectionnez "React" comme framework et "Typescript" comme variante. Vous pouvez sélectionner JavaScript comme variante si vous le souhaitez. 

Une fois cela fait, naviguez jusqu'à votre projet et utilisez la commande `yarn` pour installer les dépendances. Après avoir installé avec succès les dépendances, exécutez votre serveur de développement avec cette commande : `yarn run dev`. Ouvrez votre navigateur, collez l'URL (http://127.0.0.1:5173/) et vous verrez votre application s'exécuter dans le navigateur.

Installez le serveur JSON dans votre application en utilisant cette commande : `npm install -g json-server` pour une installation globale, ou la commande `npm i json-server` pour une installation locale.

Le dernier paquet à installer est react-router pour permettre la navigation entre les pages en utilisant cette commande : `npm i react-router-dom`. 

### Structure des dossiers

Maintenant, vous voulez que votre application ait une structure de dossiers propre, alors suivez ces directives :

Tout d'abord, créez un dossier **data** dans le répertoire racine de votre projet. À l'intérieur de ce dossier de données, vous créerez un fichier JSON appelé **db.json**. C'est là que les données JSON seront définies. 

Ensuite, dans le répertoire **src**, créez un dossier **components**. Dans ce dossier, vous créerez 3 fichiers : **Home.tsx**, **UserDetails.tsx** et **UserList.tsx**. Ce sont les composants qui rendront la logique et l'interface utilisateur de l'application. 

Dans le répertoire **src**, créez un fichier nommé **useFetch.tsx**. Ce fichier contiendra le code pour l'implémentation de l'API. Le composant principal de votre application — le fichier **App.tsx** — est l'endroit où vous gérerez le routage des pages.

### Construction de l'application

Le premier composant que vous allez modifier est le fichier **App.tsx**. Collez les lignes de code suivantes dans le composant :

```js
import Home from './components/Home';
import UserDetails from './components/UserDetails';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/users/:id" element={<UserDetails />} />
      </Routes>
    </Router>
  )
}

export default App
```

Cela permet simplement de fournir des routes pour l'application. 

Allez dans votre fichier **db.json** et définissez vos données JSON à l'intérieur. Collez ces lignes de code dans le fichier JSON :

```json
{
  "users": [
    {
      "id": 1,
      "name": "Juliet Oma",
      "email": "julie@yahoo.com",
      "number": "08100000000"
    },
    {
      "id": 2,
      "name": "James Williams",
      "email": "jameswilly@gmail.com",
      "number": "08111111111"
    },
    {
      "id": 3,
      "name": "Ahmed Ali",
      "email": "ahmedali012@gmail.com",
      "number": "09022222222"
    },
    {
      "id": 4,
      "name": "Grace Funsho",
      "email": "gracefunsho@gmail.com",
      "number": "09033333333"
    }
  ]
}
```

Démarrez votre serveur JSON en utilisant cette commande : `json-server --watch db.json --port 8000`. Cette commande surveillera le fichier db.json et enveloppera l'endpoint de l'API s'exécutant sur le port 8000. Si vous vérifiez votre terminal, voici à quoi cela ressemblera :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/json-1.png)

Si vous copiez l'URL **Resources** (http://localhost:8000/users) fournie dans le terminal et que vous l'ouvrez dans votre navigateur, vous verrez des données JSON affichant toutes les données utilisateur que vous avez définies dans votre fichier **db.json**. 

![Image](https://www.freecodecamp.org/news/content/images/2023/08/json-3-1.png)
_Fichier JSON dans le navigateur_

Ensuite, vous devrez écrire du code pour implémenter l'API. Cela sera fait dans le fichier **useFetch.tsx**. Il s'agit essentiellement d'un hook React personnalisé que vous allez créer pour gérer la récupération asynchrone de données à partir d'une URL donnée.

```js
import { useState, useEffect } from 'react';

interface UseFetchResult {
    data: any | null;
    isPending: boolean;
    error: any | null;
}

const useFetch = (url: string): UseFetchResult => {
    const [data, setData] = useState<any | null>(null);
    const [isPending, setIsPending] = useState<boolean>(true);
    const [error, setError] = useState<any | null>(null);

    useEffect(() => {
        setTimeout(() => {
            fetch(url)
                .then(res => {
                    if (!res.ok) {
                        throw Error('Erreur lors de la récupération des données des utilisateurs');
                    }
                    return res.json();
                })
                .then(data => {
                    setData(data);
                    setIsPending(false);
                    setError(null);
                })
                .catch(err => {
                    setIsPending(false);
                    setError(err.message);
                });
        }, 1000);
    }, [url]);

    return { data, isPending, error };
}

export default useFetch;
```

Analysons le code ci-dessus.

Tout d'abord, vous devrez importer deux hooks. Les hooks `useState` et `useEffect` seront utilisés pour gérer les états et effectuer des effets secondaires dans le hook personnalisé.

Lors de la configuration de mon projet React, j'ai sélectionné Typescript comme variante, donc mon application utilise Typescript. Si vous avez fait de même, vous devrez déclarer une interface nommée `useFetchResult` qui spécifie la structure de l'objet de résultat que le hook `useFetch` retournera. Il contient trois propriétés : `data`, `isPending` et `error`.

La ligne de code `const useFetch = (url: string): UseFetchResult => { ... }` définit le hook personnalisé `useFetch`. Il prend un paramètre url de type string et retourne un objet qui respecte l'interface `UseFetchResult`.

Ensuite, vous devez initialiser trois variables en utilisant le hook `useState` : `data` pour stocker les données récupérées, `isPending` pour indiquer si la récupération des données est en cours, et `error` pour stocker toute erreur qui se produit pendant le processus de récupération. Chacun a une valeur initiale de `null`, `true` et `null` respectivement.

Le hook `useEffect` est utilisé pour effectuer la récupération des données lorsque l'URL change. Il s'exécute après le rendu initial et chaque fois que la dépendance de l'URL change. À l'intérieur de la fonction `useEffect`, un `setTimeOut` est défini pour simuler un délai de 1000 millisecondes (1 seconde) avant d'initier la récupération des données. 

La méthode `fetch` est utilisée pour faire une requête GET à l'URL spécifiée. La réponse est vérifiée en utilisant `res.ok`. Si la réponse n'est pas correcte, elle lance une erreur. La réponse est ensuite convertie en JSON en utilisant la méthode `res.json()` et stockée dans la variable de données. L'état `isPending` est défini sur `false` pour indiquer que la récupération des données est terminée, et l'état d'erreur est défini sur null pour effacer l'erreur précédente.

Si une erreur se produit pendant le processus de récupération des données, elle est capturée dans le bloc `.catch`. `isPending` est défini sur false, puis l'état `error` est mis à jour avec le message d'erreur.

Le hook personnalisé retourne un objet contenant les états `data`, `isPending` et `error`, permettant à d'autres composants d'accéder aux données récupérées et à leur état.

### Création de la liste des utilisateurs sous forme de tableau

Il s'agit essentiellement du composant qui affichera toutes les informations des utilisateurs dans un tableau. Dans votre fichier **UserList.tsx**, collez ces lignes de code :

```js
import React from 'react';
import { Link } from 'react-router-dom';

interface User {
    id: number;
    name: string;
    email: string;
    number: string;
}

interface UserListProps {
    users: User[];
    name: string;
}

const UserList: React.FC<UserListProps> = ({ users, name }) => {

    return (
        <>
            <section>
                    <section>
                        <h1>Liste des utilisateurs</h1>
                    </section>
                    <section>
                        <table>
                            <thead>
                                <tr>
                                    <th>Nom</th>
                                    <th>Email</th>
                                    <th>Détails</th>
                                </tr>
                            </thead>
                            <tbody>
                                {users.map((user) => (
                                    <tr key={user.id}>
                                        <td>
                                          <p>{user.name}</p>
                                        </td>

                                        <td>
                                            <p>{user.email}</p>
                                        </td>

                                        <td>
                                            <Link to={`/users/${user.id}`}>
                                                <button>
                                                    Voir les détails complets
                                                </button>
                                            </Link>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </section>
            </section>
        </>
    );
};

export default UserList;

```

Nous avons commencé par importer `Link` de la bibliothèque `react-router-dom`. 

La ligne de code suivante est l'interface `User`, une interface Typescript qui définit la structure d'un objet utilisateur qui a quatre propriétés, chaque propriété ayant un type de données spécifié.

Ensuite vient l'interface `UserListProps` qui définit la structure d'un objet qui a deux propriétés — `users` et `name`. `users` est un tableau d'objets qui correspond à l'interface `User`.

Ce composant prend un objet avec l'interface `userListProps` comme argument, déstructure `users` de celui-ci et l'utilise comme props dans le composant.

Ensuite, vous avez l'élément JSX pour afficher la liste des utilisateurs sous forme de tableau. Nous avons parcouru la liste en utilisant la méthode `map` pour rendre chaque utilisateur dans une ligne. 

Nous avons ensuite ajouté un bouton à chaque ligne qui déclenche la navigation vers une route spécifique (`/users/${user.id}`). Ces routes afficheront les informations détaillées de l'utilisateur dont l'`id` est fourni dans l'URL. 

Nous avons utilisé un littéral de modèle pour créer une URL dynamique qui inclut la valeur `user.id`.

Votre application prend progressivement forme.

### Affichage de la liste des utilisateurs dans le navigateur

Le prochain composant sur lequel vous allez travailler est le composant **Home.tsx**. C'est là que la liste des utilisateurs sera affichée à l'écran et c'est la page d'accueil de votre application. 

```js
import UserList from './UserList';
import useFetch from '../useFetch';

const Home = (): JSX.Element => {
    const { data: users, isPending, error } = useFetch('http://localhost:8000/users')

    return (
        <section>
            {error && <p>{error}</p>}
            {isPending && <p>Chargement des utilisateurs...</p>}
            {users && <UserList users={users} />}
        </section>
    );
};

export default Home;
```

Nous avons d'abord importé le composant `UserList` et le hook personnalisé `useFetch` depuis leur emplacement dans le répertoire du projet.

La ligne de code `const { data: users, isPending, error } = useFetch('http://localhost:8000/users')` appelle le hook personnalisé `useFetch` pour récupérer les données de l'URL spécifiée (http://localhost:8000/users). Le hook retourne un objet avec trois propriétés : `data` (les utilisateurs récupérés), `isPending` (statut de chargement) et `error` (message d'erreur).

Nous avons rendu l'interface utilisateur avec les éléments JSX. Si l'état `error` a une valeur, il rend un élément de paragraphe contenant le message d'erreur. Si l'état `isPending` est `true`, il rend un élément de paragraphe indiquant que les utilisateurs sont en cours de chargement. Si l'état `users` a des données (s'il n'est pas `null`), il rend le composant `UserList` et transmet les données `users` comme prop.

### Affichage des détails complets des utilisateurs

Nous voulons ajouter une fonctionnalité supplémentaire où vous pouvez voir plus de détails sur un utilisateur particulier sur une autre page en cliquant sur le bouton **Voir les détails complets** qui se trouve dans la même ligne que son nom. 

Pour cela, collez ces lignes de code dans le composant `UserDetails.tsx` :

```js
import { useParams } from 'react-router-dom';
import useFetch from '../useFetch';

const UserDetails = () => {
    const { id } = useParams();
    const { data: user, error, isPending } = useFetch("http://localhost:8000/users/" + id);

    return (
        <>
            <section>
                {isPending && <p>Chargement des détails de l'utilisateur...</p>}

                {error && <p>{error}</p>}

                {user && (
                    <>
                        <h1>Détails de l'utilisateur {user.id}</h1>
                        <h2>{user.name}</h2>
                        <p>{user.email}</p>
                        <p>{user.number}</p>
                    </>
                )}
            </section>
        </>
    );
};

export default UserDetails;

```

Dans le code ci-dessus, nous avons importé le hook `useParams` de la bibliothèque `react-router-dom`. Cela permet d'accéder aux paramètres de l'URL. Nous avons également importé le hook personnalisé `useFetch`.

La ligne de code `const { id } = useParams();` utilise le hook `useParams` pour extraire le paramètre `id` de l'URL. Cela est typiquement utilisé dans des routes comme `/users/:id`.

La ligne de code suivante appelle le hook personnalisé `useFetch` pour récupérer les données d'une URL spécifique d'un utilisateur en fonction du paramètre `id` extrait. Le hook retourne un objet avec les propriétés `data`, `error` et `isPending`.

Ensuite, viennent les éléments JSX pour rendre les détails des utilisateurs. `{isPending && <p>Chargement des détails de l'utilisateur...</p>}` rend un paragraphe indiquant que les détails de l'utilisateur sont en cours de chargement si `isPending` est `true`. 

`{error && <p>{error}</p>}` rendra un paragraphe affichant un message d'erreur, s'il y a une erreur. Tandis que `{user && (...)}` rendra certains détails de l'utilisateur comme `id`, `name`, `email` et `number`, si les données sont disponibles.

Lorsque vous retournez à votre navigateur, vous verrez une liste de données utilisateur dans un tableau. Chaque ligne d'utilisateur dans le tableau aura un bouton que vous pouvez cliquer pour ouvrir une page afin de voir les détails complets de cet utilisateur spécifique. 

Maintenant, cette application ne sera pas très belle car elle n'a pas été stylisée. Alors, allez-y et stylisez votre application en utilisant la technique de stylisation que vous souhaitez. Un aperçu rapide de mon application après le stylisme :

<iframe src="https://giphy.com/embed/XPVIQLbhPVlXWHSAyh" width="480" height="258" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/XPVIQLbhPVlXWHSAyh">via GIPHY</a></p>

Je sais que l'interface utilisateur n'est pas géniale, mais l'accent principal ici était la fonctionnalité. Remarquez comment j'ai ajouté une animation de chargement qui s'affiche lorsque la liste des utilisateurs et les détails sont en attente d'être récupérés ? Vous pouvez faire cela en utilisant une bibliothèque d'animation comme Framer motion ou en créant un composant de spinner. 

L'animation de chargement ou le spinner sera rendu pendant que les données sont en attente d'être récupérées au lieu d'un simple texte "Chargement....". Cela peut rendre votre application plus belle et vous aider avec l'engagement des utilisateurs.

Vous pouvez modifier les données des utilisateurs ou ajouter plus de détails à votre liste d'utilisateurs comme la description de l'emploi des utilisateurs, leur titre, etc. dans votre fichier **db.json** et vous verrez les changements reflétés dans la liste sur le navigateur. 

Cette application envoie une requête à l'endpoint de l'API fourni lorsque vous démarrez le serveur JSON et affiche la réponse sur le navigateur. C'est essentiellement comment fonctionne un serveur d'API back-end réel. Dans ce cas, nous avons pu atteindre notre fonctionnalité en utilisant JSON Server.

Il est important de savoir que cette API fictive JSON ne peut pas être utilisée en phase de production. Elle ne peut être utilisée qu'en phase de développement pour créer des données JSON fictives. Cela signifie que vous ne pouvez pas la déployer en production car le fichier de données JSON ne s'exécute que sur un port localhost.

## Conclusion

C'est tout pour cet article. Ici, vous avez appris à propos du serveur JSON et comment l'utiliser dans une application front-end React.js.

Vous pouvez également effectuer des opérations CRUD complètes avec ces données à partir de votre fichier JSON sur votre front-end. Dans cet article, je n'ai démontré que l'opération **Read**. Cette application peut être améliorée pour permettre aux gens de **Créer** des utilisateurs, **Mettre à jour** des utilisateurs et **Supprimer** des utilisateurs de la base de données JSON.

Si vous cherchez à apprendre comment implémenter une API tierce réelle dans votre application React, consultez [mon article précédent](https://www.freecodecamp.org/news/how-to-use-apis-in-web-development/).