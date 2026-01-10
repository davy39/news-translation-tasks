---
title: 'Le didacticiel JavaScript + Firestore pour 2020 : Apprendre par l''exemple'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2020-07-16T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-firestore-tutorial-for-2020-learn-by-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/The-Firestore-Tutorial-2020.png
tags:
- name: cheatsheet
  slug: cheatsheet
- name: database
  slug: database
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
- name: NoSQL
  slug: nosql
- name: Tutorial
  slug: tutorial
seo_title: 'Le didacticiel JavaScript + Firestore pour 2020 : Apprendre par l''exemple'
seo_desc: Cloud Firestore is a blazing-fast, serverless NoSQL database, perfect for
  powering web and mobile apps of any size. Grab the complete guide to learning Firestore,
  created to show you how to use Firestore as the engine for your own amazing projects
  fr...
---

Cloud Firestore est une base de données NoSQL ultra-rapide et sans serveur, parfaite pour alimenter des applications web et mobiles de toute taille. [Obtenez le guide complet pour apprendre Firestore](https://reedbarger.com/resources/javascript-firestore-2020/), créé pour vous montrer comment utiliser Firestore comme moteur pour vos propres projets incroyables, de bout en bout.

## Table des matières

Démarrage avec Firestore

* Qu'est-ce que Firestore ? Pourquoi l'utiliser ?
* Installation de Firestore dans un projet JavaScript
* Documents et collections Firestore
* Gestion de notre base de données avec la console Firebase

Récupération de données avec Firestore

* Obtention de données d'une collection avec .get()
* Abonnement à une collection avec .onSnapshot()
* Différence entre .get() et .onSnapshot()
* Désabonnement d'une collection
* Obtention de documents individuels

Modification de données avec Firestore

* Ajout d'un document à une collection avec .add()
* Ajout d'un document à une collection avec .set()
* Mise à jour de données existantes
* Suppression de données

Modèles essentiels

* Travail avec des sous-collections
* Méthodes utiles pour les champs Firestore
* Requêtes avec .where()
* Tri et limitation des données

[Note : vous pouvez télécharger une version PDF de ce didacticiel pour le lire hors ligne.](https://reedbarger.com/resources/javascript-firestore-2020/)

### Qu'est-ce que Firestore ? Pourquoi l'utiliser ?

Firestore est une base de données très flexible et facile à utiliser pour le développement mobile, web et serveur. Si vous êtes familier avec la base de données en temps réel de Firebase, Firestore présente de nombreuses similitudes, mais avec une API différente (arguablement plus déclarative).

Voici quelques-unes des fonctionnalités que Firestore apporte :

#### ⚡ Obtenez facilement des données en temps réel

Comme la base de données en temps réel de Firebase, Firestore fournit des méthodes utiles telles que .onSnapshot() qui facilitent l'écoute des mises à jour de vos données en temps réel. Cela fait de Firestore un choix idéal pour les projets qui accordent une prime à l'affichage et à l'utilisation des données les plus récentes (applications de chat, par exemple).

#### Flexibilité en tant que base de données NoSQL

Firestore est une option très flexible pour un backend car c'est une base de données NoSQL. NoSQL signifie que les données ne sont pas stockées dans des tables et des colonnes comme le serait une base de données SQL standard. Elle est structurée comme un magasin clé-valeur, comme si c'était un grand objet JavaScript. 

En d'autres termes, il n'y a pas de schéma ou de besoin de décrire les données que notre base de données stockera. Tant que nous fournissons des clés et des valeurs valides, Firestore les stockera. 

#### ⇕ Facilement scalable

Un grand avantage de choisir Firestore pour votre base de données est l'infrastructure très puissante sur laquelle elle repose, ce qui vous permet de mettre à l'échelle votre application très facilement. Verticalement et horizontalement. Peu importe que vous ayez des centaines ou des millions d'utilisateurs. Les serveurs de Google seront capables de gérer toute charge que vous leur imposez.

En bref, Firestore est une excellente option pour les applications, petites et grandes. Pour les petites applications, elle est puissante car nous pouvons faire beaucoup sans beaucoup de configuration et créer des projets très rapidement avec elles. Firestore est bien adaptée aux grands projets grâce à sa scalabilité.

### Installation de Firestore dans un projet JavaScript

> Nous allons utiliser le SDK Firestore pour JavaScript. Tout au long de ce guide, nous couvrirons comment utiliser Firestore dans le contexte d'un projet JavaScript. Malgré cela, les concepts que nous couvrirons ici sont facilement transférables à l'une des bibliothèques clientes Firestore disponibles. 

Pour commencer avec Firestore, nous allons nous rendre dans la console Firebase. Vous pouvez y accéder en allant sur [firebase.google.com](https://firebase.com). Vous aurez besoin d'un compte Google pour vous connecter. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/firebase.png)

Une fois connectés, nous créerons un nouveau projet et lui donnerons un nom. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/create-a-project.png)

Une fois notre projet créé, nous le sélectionnerons. Après cela, sur le tableau de bord de notre projet, nous sélectionnerons le bouton de code. 

Cela nous donnera le code dont nous avons besoin pour intégrer Firestore avec notre projet JavaScript. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/firebase-integration.gif)

Habituellement, si vous configurez cela dans une application JavaScript quelconque, vous voudrez mettre cela dans un fichier dédié appelé firebase.js. Si vous utilisez une bibliothèque JavaScript qui a un fichier package.json, vous voudrez installer la dépendance Firebase avec npm ou yarn.

```bash
// avec npm
npm i firebase

// avec yarn
yarn add firebase
```

Firestore peut être utilisé soit sur le client, soit sur le serveur. Si vous utilisez Firestore avec Node, vous devrez utiliser la syntaxe CommonJS avec require. Sinon, si vous utilisez JavaScript côté client, vous importerez firebase en utilisant les modules ES.

```js
// avec la syntaxe Commonjs (si vous utilisez Node)
const firebase = require("firebase/app");
require("firebase/firestore");

// avec les modules ES (si vous utilisez JS côté client, comme React)
import firebase from 'firebase/app';
import 'firebase/firestore';

var firebaseConfig = {
  apiKey: "AIzaSyDpLmM79mUqbMDBexFtOQOkSl0glxCW_ds",
  authDomain: "lfasdfkjkjlkjl.firebaseapp.com",
  databaseURL: "https://lfasdlkjkjlkjl.firebaseio.com",
  projectId: "lfasdlkjkjlkjl",
  storageBucket: "lfasdlkjkjlkjl.appspot.com",
  messagingSenderId: "616270824980",
  appId: "1:616270824990:web:40c8b177c6b9729cb5110f",
};
// Initialiser Firebase
firebase.initializeApp(firebaseConfig);
```

### Collections et documents Firestore

Il y a deux termes clés qui sont essentiels pour comprendre comment travailler avec Firestore : **documents** et **collections**. 

Les documents sont des morceaux individuels de données dans notre base de données. Vous pouvez considérer les documents comme des objets JavaScript simples. Ils consistent en des paires clé-valeur, que nous appelons **champs**. Les valeurs de ces champs peuvent être des chaînes de caractères, des nombres, des booléens, des objets, des tableaux, et même des données binaires.

```js
document -> { clé: valeur } 
```

Les ensembles de ces documents sont appelés collections. Les collections sont très similaires à des tableaux d'objets. Dans une collection, chaque document est lié à un identifiant donné (id). 

```js
collection -> [{ id: doc }, { id: doc }]
```

### Gestion de notre base de données avec la console Firestore

Avant de pouvoir commencer à travailler avec notre base de données, nous devons la créer.

Dans notre console Firebase, allez dans l'onglet 'Database' et créez votre base de données Firestore. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/firestore.png)

Une fois que vous avez fait cela, nous commencerons en mode test et activerons toutes les lectures et écritures dans notre base de données. En d'autres termes, nous aurons un accès ouvert pour obtenir et modifier les données dans notre base de données. Si nous ajoutions l'authentification Firebase, nous pourrions restreindre l'accès uniquement aux utilisateurs authentifiés. 

Après cela, nous serons redirigés vers notre base de données elle-même, où nous pourrons commencer à créer des collections et des documents. La racine de notre base de données sera une série de collections, alors créons notre première collection. 

Nous pouvons sélectionner 'Start collection' et lui donner un id. Chaque collection aura un id ou un nom. Pour notre projet, nous allons suivre les livres préférés de nos utilisateurs. Nous donnerons à notre première collection l'id 'books'. 

![Image](https://www.freecodecamp.org/news/content/images/2021/09/collection-id.png)

Ensuite, nous ajouterons notre premier document avec notre collection nouvellement créée 'books'. 

Chaque document aura également un id, le liant à la collection dans laquelle il existe. 

Dans la plupart des cas, nous allons utiliser une option pour lui donner un ID généré automatiquement. Nous pouvons donc cliquer sur le bouton 'auto id' pour ce faire, après quoi nous devons fournir un champ, lui donner un type, ainsi qu'une valeur. 

Pour notre premier livre, nous créerons un champ 'title' de type 'string', avec la valeur 'The Great Gatsby', et nous cliquerons sur enregistrer. 

Après cela, nous devrions voir notre premier élément dans notre base de données.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/first-item.png)

### Obtention de données d'une collection avec .get()

Pour accéder à Firestore et utiliser toutes les méthodes qu'il fournit, nous utilisons `firebase.firestore()`. Cette méthode doit être exécutée chaque fois que nous voulons interagir avec notre base de données Firestore. 

Je recommande de créer une variable dédiée pour stocker une seule référence à Firestore. Cela permet de réduire la quantité de code que vous écrivez dans votre application. 

```js
const db = firebase.firestore();

```

> Dans ce guide, cependant, je vais continuer à utiliser la méthode firestore chaque fois pour être aussi clair que possible.

Pour référencer une collection, nous utilisons la méthode `.collection()` et fournissons l'id d'une collection comme argument. Pour obtenir une référence à la collection de livres que nous avons créée, il suffit de passer la chaîne 'books'.

```js
const booksRef = firebase.firestore().collection('books');
```

Pour obtenir toutes les données des documents d'une collection, nous pouvons enchaîner la méthode `.get()`. 

`.get()` retourne une promesse, ce qui signifie que nous pouvons la résoudre soit en utilisant un rappel `.then()`, soit nous pouvons utiliser la syntaxe async-await si nous exécutons notre code dans une fonction asynchrone. 

Une fois notre promesse résolue d'une manière ou d'une autre, nous obtenons ce qu'on appelle un **snapshot**. 

Pour une requête de collection, ce snapshot va consister en un certain nombre de documents individuels. Nous pouvons y accéder en disant `snapshot.docs`. 

À partir de chaque document, nous pouvons obtenir l'id comme une propriété séparée, et le reste des données en utilisant la méthode `.data()`. 

Voici à quoi ressemble notre requête complète :

```js
const booksRef = firebase
  .firestore()
  .collection("books");

booksRef
  .get()
  .then((snapshot) => {
    const data = snapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));
    console.log("Toutes les données dans la collection 'books'", data); 
    // [ { id: 'glMeZvPpTN1Ah31sKcnj', title: 'The Great Gatsby' } ]
  });
```

### Abonnement à une collection avec .onSnapshot()

La méthode `.get()` retourne simplement toutes les données de notre collection. 

Pour tirer parti de certaines des capacités en temps réel de Firestore, nous pouvons nous abonner à une collection, ce qui nous donne la valeur actuelle des documents de cette collection, chaque fois qu'ils sont mis à jour. 

Au lieu d'utiliser la méthode `.get()`, qui est pour une requête unique, nous utilisons la méthode `.onSnapshot()`. 

```js
firebase
  .firestore()
  .collection("books")
  .onSnapshot((snapshot) => {
    const data = snapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));
    console.log("Toutes les données dans la collection 'books'", data);
  });
```

Dans le code ci-dessus, nous utilisons ce qu'on appelle le chaînage de méthodes au lieu de créer une variable séparée pour référencer la collection.

Ce qui est puissant avec l'utilisation de firestore, c'est que nous pouvons enchaîner un tas de méthodes les unes après les autres, ce qui rend le code plus déclaratif et lisible.

Dans le rappel de onSnapshot, nous obtenons un accès direct au snapshot de notre collection, maintenant et chaque fois qu'il est mis à jour à l'avenir. Essayez de mettre à jour manuellement notre document et vous verrez que `.onSnapshot()` écoute tout changement dans cette collection.

### Différence entre .get() et .onSnapshot()

La différence entre les méthodes get et snapshot est que get retourne une promesse, qui doit être résolue, et seulement alors nous obtenons les données du snapshot.

`.onSnapshot`, cependant, utilise une fonction de rappel synchrone, qui nous donne un accès direct au snapshot. 

Il est important de garder cela à l'esprit lorsqu'il s'agit de ces différentes méthodes--nous devons savoir lesquelles d'entre elles retournent une promesse et lesquelles sont synchrones. 

### Désabonnement d'une collection avec unsubscribe()

Notez également que `.onSnapshot()` retourne une fonction que nous pouvons utiliser pour nous désabonner et arrêter d'écouter une collection donnée. 

Cela est important dans les cas où l'utilisateur, par exemple, quitte une page donnée où nous affichons les données d'une collection. Voici un exemple, en utilisant la bibliothèque React où nous appelons unsubscribe dans le hook useEffect. 

Lorsque nous le faisons, cela garantira que lorsque notre composant est démonté (n'est plus affiché dans le contexte de notre application), nous n'écoutons plus les données de la collection que nous utilisons dans ce composant.

```js
function App() {
  const [books, setBooks] = React.useState([]);

  React.useEffect(() => {
	const unsubscribe = firebase
      .firestore()
      .collection("books")
      .onSnapshot((snapshot) => {
        const data = snapshot.docs.map((doc) => ({
          id: doc.id,
          ...doc.data(),
        }));
		setBooks(data);
      });
  }, []);
  
  return books.map(book => <BookList key={book.id} book={book} />)
}
```

### Obtention de documents individuels avec .doc()

En ce qui concerne l'obtention d'un document dans une collection, le processus est le même que pour obtenir une collection entière : nous devons d'abord créer une référence à ce document, puis utiliser la méthode get pour le récupérer.

Après cela, cependant, nous utilisons la méthode `.doc()` enchaînée à la méthode de collection. Afin de créer une référence, nous devons récupérer cet id de la base de données s'il a été généré automatiquement. Après cela, nous pouvons enchaîner `.get()` et résoudre la promesse. 

```js
const bookRef = firebase
  .firestore()
  .collection("books")
  .doc("glMeZvPpTN1Ah31sKcnj");

bookRef.get().then((doc) => {
  if (!doc.exists) return;
  console.log("Données du document :", doc.data());
  // Données du document : { title: 'The Great Gatsby' }
});
```

Remarquez la condition `if (!doc.exists) return;` dans le code ci-dessus.

Une fois que nous avons récupéré le document, il est essentiel de vérifier s'il existe. 

Si nous ne le faisons pas, il y aura une erreur lors de la récupération des données de notre document. La façon de vérifier et de voir si notre document existe est de dire, si `doc.exists`, qui retourne une valeur vraie ou fausse. 

Si cette expression retourne false, nous voulons retourner de la fonction ou peut-être lancer une erreur. Si `doc.exists` est vrai, nous pouvons obtenir les données de `doc.data`.

### Ajout d'un document à une collection avec .add()

Ensuite, passons à la modification des données. La façon la plus simple d'ajouter un nouveau document à une collection est avec la méthode `.add()`. 

Tout ce que vous avez à faire est de sélectionner une référence de collection (avec `.collection()`) et d'enchaîner `.add()`. 

En revenant à notre définition des documents comme étant des objets JavaScript, nous devons passer un objet à la méthode `.add()` et spécifier tous les champs que nous voulons voir sur le document. 

Disons que nous voulons ajouter un autre livre, 'Of Mice and Men' :

```js
firebase
  .firestore()
  .collection("books")
  .add({
    title: "Of Mice and Men",
  })
  .then((ref) => {
    console.log("Document ajouté avec l'ID : ", ref.id);
    // Document ajouté avec l'ID :  ZzhIgLqELaoE3eSsOazu
  });
```

La méthode `.add` retourne une promesse et à partir de cette promesse résolue, nous obtenons une référence au document créé, qui nous donne des informations telles que l'id créé. 

La méthode `.add()` génère automatiquement un id pour nous. Notez que nous ne pouvons pas utiliser cette référence directement pour obtenir des données. Nous pouvons cependant passer la référence à la méthode doc pour créer une autre requête.

### Ajout d'un document à une collection avec .set()

Une autre façon d'ajouter un document à une collection est avec la méthode `.set()`. 

La différence entre set et add réside dans le besoin de spécifier notre propre id lors de l'ajout des données. 

Cela nécessite d'enchaîner la méthode `.doc()` avec l'id que vous souhaitez utiliser. De plus, notez que lorsque la promesse est résolue à partir de `.set()`, nous n'obtenons pas de référence au document créé :

```js
firebase
  .firestore()
  .collection("books")
  .doc("another book")
  .set({
    title: "War and Peace",
  })
  .then(() => {
    console.log("Document créé");
  });
```

De plus, lorsque nous utilisons `.set()` avec un document existant, il écrasera, par défaut, ce document. 

Si nous voulons fusionner un ancien document avec un nouveau document au lieu de l'écraser, nous devons passer un argument supplémentaire à `.set()` et fournir la propriété `merge` définie sur true.

```js
// utiliser .set() pour fusionner les données avec le document existant, ne pas écraser

const bookRef = firebase
  .firestore()
  .collection("books")
  .doc("another book");

bookRef
  .set({
    author: "Lev Nikolaevich Tolstoy"
  }, { merge: true })
  .then(() => {
    console.log("Document fusionné");
    
    bookRef
      .get()
      .then(doc => {
      console.log("Document fusionné : ", doc.data());
      // Document fusionné :  { title: 'War and Peace', author: 'Lev Nikolaevich Tolstoy' }
    });
  });
```

### Mise à jour de données existantes avec .update()

En ce qui concerne la mise à jour des données, nous utilisons la méthode update, comme `.add()` et `.set()` elle retourne une promesse.

Ce qui est utile avec `.update()`, c'est que, contrairement à `.set()`, elle n'écrasera pas l'ensemble du document. De plus, comme `.set()`, nous devons référencer un document individuel. 

Lorsque vous utilisez `.update()`, il est important d'utiliser une gestion des erreurs, telle que le rappel `.catch()` au cas où le document n'existe pas. 

```js
const bookRef = firebase.firestore().collection("books").doc("another book");

bookRef
  .update({
    year: 1869,
  })
  .then(() => {
    console.log("Document mis à jour"); // Document mis à jour
  })
  .catch((error) => {
    console.error("Erreur lors de la mise à jour du document", error);
  });	
```

### Suppression de données avec .delete()

Nous pouvons supprimer une collection de documents donnée en la référençant par son id et en exécutant la méthode `.delete()`, c'est aussi simple que cela. Elle retourne également une promesse.

Voici un exemple de base de suppression d'un livre avec l'id "another book" :

```js
firebase
  .firestore()
  .collection("books")
  .doc("another book")
  .delete()
  .then(() => console.log("Document supprimé")) // Document supprimé
  .catch((error) => console.error("Erreur lors de la suppression du document", error));
```

> Notez que la documentation officielle de Firestore ne recommande pas de supprimer des collections entières, seulement des documents individuels.

### Travail avec des sous-collections

Disons que nous avons fait une erreur dans la création de notre application, et au lieu d'ajouter simplement des livres, nous voulons également les connecter aux utilisateurs qui les ont créés. 

La façon dont nous voulons restructurer les données est de créer une collection appelée 'users' à la racine de notre base de données, et de faire de 'books' une sous-collection de 'users'. Cela permettra aux utilisateurs d'avoir leurs propres collections de livres. Comment mettre cela en place ? 

Les références à la sous-collection 'books' devraient ressembler à ceci : 

```js
const userBooksRef = firebase
  .firestore()
  .collection('users')
  .doc('user-id')
  .collection('books');
```

Notez également que nous pouvons écrire tout cela dans un seul appel `.collection()` en utilisant des barres obliques. 

Le code ci-dessus est équivalent au suivant, où la référence de collection doit avoir un nombre impair de segments. Sinon, Firestore lancera une erreur. 

```js
const userBooksRef = firebase
  .firestore()
  .collection('users/user-id/books');
```

Pour créer la sous-collection elle-même, avec un document (un autre roman de Steinbeck, 'East of Eden'), exécutez ce qui suit. 

```js
firebase.firestore().collection("users/user-1/books").add({
  title: "East of Eden",
});
```

Ensuite, l'obtention de cette sous-collection nouvellement créée ressemblerait à ce qui suit en fonction de l'ID de l'utilisateur.

```js
firebase
  .firestore()
  .collection("users/user-1/books")
  .get()
  .then((snapshot) => {
    const data = snapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));
    console.log(data); 
    // [ { id: 'UO07aqpw13xvlMAfAvTF', title: 'East of Eden' } ]
  });
```

### Méthodes utiles pour les champs Firestore

Il existe des outils utiles que nous pouvons obtenir de Firestore qui nous permettent de travailler avec les valeurs de nos champs un peu plus facilement. 

Par exemple, nous pouvons générer un horodatage chaque fois qu'un document donné est créé ou mis à jour avec l'aide suivante de la propriété `FieldValue`. 

Nous pouvons bien sûr créer nos propres valeurs de date en utilisant JavaScript, mais l'utilisation d'un horodatage serveur nous permet de savoir exactement quand les données sont modifiées ou créées depuis Firestore lui-même. 

```js
firebase
  .firestore()
  .collection("users")
  .doc("user-2")
  .set({
    created: firebase.firestore.FieldValue.serverTimestamp(),
  })
  .then(() => {
    console.log("Utilisateur ajouté"); // Utilisateur ajouté
  });
```

De plus, disons que nous avons un champ sur un document qui suit un certain nombre, disons le nombre de livres qu'un utilisateur a créés. Chaque fois qu'un utilisateur crée un nouveau livre, nous voulons incrémenter cela de un. 

Une façon facile de faire cela, au lieu d'avoir à faire une requête `.get()` en premier, est d'utiliser un autre helper de valeur de champ appelé `.increment()` :

```js
const userRef = firebase.firestore().collection("users").doc("user-2");

userRef
  .set({
    count: firebase.firestore.FieldValue.increment(1),
  })
  .then(() => {
    console.log("Utilisateur mis à jour");

    userRef.get().then((doc) => {
      console.log("Données de l'utilisateur mises à jour : ", doc.data());
    });
  });
 
```

### Requêtes avec .where()

Et si nous voulons obtenir des données de nos collections en fonction de certaines conditions ? Par exemple, disons que nous voulons obtenir tous les utilisateurs qui ont soumis un ou plusieurs livres ?

Nous pouvons écrire une telle requête avec l'aide de la méthode `.where()`. Tout d'abord, nous référençons une collection, puis nous enchaînons `.where()`. 

La méthode where prend trois arguments--d'abord, le champ que nous recherchons sur une opération, un opérateur, puis la valeur sur laquelle nous voulons filtrer notre collection. 

Nous pouvons utiliser l'un des opérateurs suivants et les champs que nous utilisons peuvent être des valeurs primitives ainsi que des tableaux.

`<`, `<=`, `==`, `>`, `>=`, `array-contains`, `in`, ou `array-contains-any`

Pour récupérer tous les utilisateurs qui ont soumis plus d'un livre, nous pouvons utiliser la requête suivante. 

Après `.where()` nous devons enchaîner `.get()`. Une fois notre promesse résolue, nous obtenons ce qu'on appelle un **querySnapshot**. 

Tout comme l'obtention d'une collection, nous pouvons itérer sur le querySnapshot avec `.map()` pour obtenir l'id et les données (champs) de chaque document :

```js
firebase
  .firestore()
  .collection("users")
  .where("count", ">=", 1)
  .get()
  .then((querySnapshot) => {
    const data = querySnapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));
    console.log("Utilisateurs avec > 1 livre : ", data);
    // Utilisateurs avec > 1 livre :  [ { id: 'user-1', count: 1 } ]
  });
```

> Notez que vous pouvez enchaîner plusieurs méthodes `.where()` pour créer des requêtes composées.

### Limitation et tri des requêtes

Une autre méthode pour interroger efficacement nos collections est de les limiter. Disons que nous voulons limiter une requête donnée à un certain nombre de documents. 

Si nous voulons retourner seulement quelques éléments de notre requête, nous devons simplement ajouter la méthode `.limit()`, après une référence donnée. 

Si nous voulions faire cela à travers notre requête pour récupérer les utilisateurs qui ont soumis au moins un livre, cela ressemblerait à ce qui suit. 

```js
const usersRef = firebase
  .firestore()
  .collection("users")
  .where("count", ">=", 1);

  usersRef.limit(3)
```

Une autre fonctionnalité puissante est de trier nos données interrogées selon les champs de document en utilisant `.orderBy()`. 

Si nous voulons trier nos utilisateurs créés par quand ils ont été faits pour la première fois, nous pouvons utiliser la méthode `orderBy` avec le champ 'created' comme premier argument. Pour le deuxième argument, nous spécifions s'il doit être dans l'ordre ascendant ou descendant. 

Pour obtenir tous les utilisateurs triés par quand ils ont été créés du plus récent au plus ancien, nous pouvons exécuter la requête suivante :

```js
const usersRef = firebase
  .firestore()
  .collection("users")
  .where("count", ">=", 1);

  usersRef.orderBy("created", "desc").limit(3);
```

Nous pouvons enchaîner `.orderBy()` avec `.limit()`. Pour que cela fonctionne correctement, `.limit()` doit être appelé en dernier et non avant `.orderBy()`.

## Vous voulez votre propre copie ? 

Si vous souhaitez avoir ce guide pour référence future, [téléchargez un aide-mémoire de ce tutoriel entier ici](https://reedbarger.com/resources/javascript-firestore-2020/). 

%[https://reedbarger.com/resources/javascript-firestore-2020/]

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*