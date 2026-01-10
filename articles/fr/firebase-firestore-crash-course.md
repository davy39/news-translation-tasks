---
title: Firebase Cloud Firestore – Cours accéléré sur les bases de données
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2021-10-13T15:57:42.000Z'
originalURL: https://freecodecamp.org/news/firebase-firestore-crash-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/g943.png
tags:
- name: database
  slug: database
- name: Firebase
  slug: firebase
seo_title: Firebase Cloud Firestore – Cours accéléré sur les bases de données
seo_desc: "In this article, we will be learning about one of Firebase's build products\
  \ called Cloud Firestore. It lets you store, sync, and retrieve data in a document-based\
  \ database. \nWe'll learn how to set up our project for the web. Since this isn't\
  \ a design..."
---

Dans cet article, nous allons apprendre l'un des produits de Firebase appelé Cloud Firestore. Il vous permet de stocker, synchroniser et récupérer des données dans une base de données basée sur des documents. 

Nous apprendrons comment configurer notre projet pour le web. Comme ce n'est pas un tutoriel axé sur le design, nous utiliserons simplement un fichier HTML et JavaScript pour montrer comment vous pouvez ajouter (stocker), synchroniser et interroger des données. 

Cloud Firestore est utile car il sert de base de données backend qui est sécurisée et très scalable. Lorsque vous l'utilisez, vous n'avez pas à vous soucier d'écrire du code pour créer et gérer votre propre base de données. 

C'est aussi un excellent choix si vous êtes un développeur front-end, car il vous permet de créer des applications full stack. Commençons.

## Qu'est-ce que Cloud Firestore ?

Selon la [documentation Firebase](https://firebase.google.com/docs/firestore),

> "Cloud Firestore est une base de données flexible et scalable pour le développement mobile, web et serveur de Firebase et Google Cloud... ".

Firestore est une base de données NoSQL qui ne stocke pas les données dans des tables avec des lignes et des colonnes. Au lieu de cela, elle stocke les données dans des collections où chaque collection peut avoir divers documents sous elle où les données sont stockées.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/g1271-2.png)

Nous allons nous concentrer sur l'utilisation de Firestore pour stocker et récupérer des données pour le web. Vous pouvez trouver le code [ici](https://github.com/ihechikara/firebase-firestore). Chaque section a sa propre branche.

## Comment créer le projet localement

Nous travaillerons uniquement avec les fichiers HTML et JS, donc vous pouvez styliser votre page web comme vous le souhaitez. L'objectif principal ici sera d'ajouter et d'interagir avec les données stockées dans la base de données.

Voici le fichier HTML :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Firestore</title>
</head>
<body>
    
    <script src="app.js"></script>
</body>
</html>
```

Maintenant, vous devez simplement créer un fichier JavaScript. J'ai appelé le mien app.js comme vous pouvez le voir ci-dessus.

## Comment configurer le projet dans Firebase

Pour configurer votre projet, allez sur le [site web de Firebase](https://firebase.google.com/) et inscrivez-vous si vous n'avez pas déjà de compte (ou connectez-vous si vous en avez un).

Une fois connecté, cliquez sur "Go to console" (devrait être en haut à droite de la page) ou "Get Started" selon le cas.

Ensuite, cliquez sur "Add project" et donnez un nom à votre projet. Les étapes suivantes sont assez simples – continuez à cliquer sur suivant et attendez que votre projet soit créé.

## Comment installer et initialiser Firebase

Tout d'abord, si vous n'avez pas encore installé Firebase, exécutez la commande suivante dans le terminal de votre projet :

`npm install firebase`

Après l'installation, allez dans la section head de votre page HTML et incluez les scripts suivants :

```html
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-firestore.js"></script>
    <title>Firestore</title>
  </head>
```

Le premier script charge la bibliothèque de l'application Firebase tandis que le second nous permet d'utiliser les fonctionnalités de Firestore.

Ensuite, allez dans la console Firebase de votre projet et cliquez sur Firestore Database. Assurez-vous de commencer en mode Test afin de pouvoir faire des requêtes sans authentification puisque nous sommes en mode développement.

Assurez-vous de changer vos règles de sécurité lorsque le besoin se présente afin que votre projet soit accessible sur Internet. Après avoir créé la base de données, cliquez sur Project Overview dans la barre de navigation. Vous devriez voir une page comme celle montrée ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot--74--3.png)

Cliquez sur l'icône </> pour initialiser votre projet pour le web. Sur la page suivante, copiez l'apiKey, l'authDomain et le projectId. Nous allons initialiser le projet en utilisant la méthode Firestore Web version 8 comme montré ci-dessous :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-firestore.js"></script>
    <title>Firestore</title>
  </head>
  <body>
    <script>
      firebase.initializeApp({
        apiKey: "### FIREBASE API KEY ###",
        authDomain: "### FIREBASE AUTH DOMAIN ###",
        projectId: "### CLOUD FIRESTORE PROJECT ID ###",
      });

      const db = firebase.firestore();
    </script>
    <script src="app.js"></script>
  </body>
</html>
```

Assurez-vous de remplacer `### FIREBASE API KEY ###`, `### FIREBASE AUTH DOMAIN ###`, et `### CLOUD FIRESTORE PROJECT ID ###` par les valeurs correspondantes que vous avez copiées lors de l'initialisation de votre projet pour le web.

## Comment ajouter des données à Firestore

Vous pouvez ajouter manuellement des données à votre base de données en allant dans la console et en créant une nouvelle collection avec des documents qui peuvent avoir différents types de données. Mais ici, nous allons adopter une approche différente – ajouter des données à notre base de données depuis le front-end en utilisant des champs de saisie.

J'ai ajouté une div à mon code avec un champ de saisie et une zone de texte :

```html
<div class="content">
    <input type="text" id="username" placeholder="username">
    <textarea name="" id="about" placeholder="about"></textarea>
    <button id="btn">ADD</button>
</div>
```

Cela devrait suffire pour le balisage pour l'instant. Passons à un peu de JavaScript vanille. Nous devons créer des variables qui obtiendront les valeurs de nos entrées :

```javascript
const username = document.getElementById('username');
const about = document.getElementById('about');
const btn = document.getElementById('btn');
```

Ensuite, nous attachons un écouteur d'événement au bouton et écrivons le code pour ajouter des données à la base de données :

```javascript
btn.addEventListener('click', ()=>{
    db.collection('userInfo').add({
        username: username.value,
        bio: about.value
    });
    username.value = '';
    about.value = '';
})
```

**`db.collection('userInfo')`** recherche une collection appelée **`userInfo`** qui n'existe pas à ce stade. Elle sera créée automatiquement si elle n'existe pas déjà. L'id pour les documents est également généré automatiquement s'il n'est pas spécifié.

**`.add()`** prend les données dans les accolades et les ajoute à la collection, ce qui crée un nouveau document sous la collection `userInfo`. Les données dans les accolades viennent en paires nom et valeur.

J'ai ajouté quelques données à ma propre base de données. Vous pouvez jouer avec et en ajouter autant que vous le souhaitez. Après avoir appuyé sur le bouton d'ajout, allez dans votre console de base de données et actualisez. Vous devriez voir vos données dans la base de données comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot--78--1.png)

Vous pouvez trouver le code pour cela dans la [branche addData](https://github.com/ihechikara/firebase-firestore-tutorial/tree/addData).

## Comment obtenir des données

Maintenant, nous allons parcourir les données que nous avons stockées précédemment et les afficher sur le front-end.

Nous commençons par créer un élément **`ul`** dans notre fichier HTML qui servira de conteneur.

```html
<body>
    <div class="content">
      <ul id="lists">

      </ul>
    </div>
</body>
```

Nous créerons le reste dynamiquement en utilisant JavaScript :

```javascript
const lists = document.getElementById("lists");

db.collection("userInfo")
  .get()
  .then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
      let li = document.createElement("li");
      let username = document.createElement("h4");
      let bio = document.createElement("p");

      username.textContent = doc.data().username;
      bio.textContent = doc.data().bio;

      li.appendChild(username);
      li.appendChild(bio);

      lists.appendChild(li);
    });
  })
  .catch((error) => {
    console.log("Error getting documents: ", error);
  });
```

**`db.collection("userInfo").get()`** obtient la collection `userInfo`. Comme cela retourne une promesse, nous pouvons attacher une méthode **`.then()`** qui a une fonction de rappel avec un paramètre **`querySnapshot`**. Ce paramètre retourne l'état actuel de la base de données.

Nous avons ensuite parcouru l'état actuel en utilisant la méthode **`forEach()`**. Nous avons créé trois nouveaux éléments : **`li`, `h4`,** et `p` où la valeur du `h4` était le nom d'utilisateur stocké dans la base de données. Nous avons récupéré le nom d'utilisateur en utilisant **`data().username`** (même processus pour la bio).

Nous avons ensuite ajouté les éléments `h4` et `p` à l'élément `li`, et ajouté l'élément `li` à l'élément `ul` qui existe déjà dans le DOM.

Le code pour cette section peut être trouvé dans la [branche getData](https://github.com/ihechikara/firebase-firestore-tutorial/tree/getData).

## Comment effectuer des requêtes sur les données

Les requêtes vous permettent de filtrer les données que vous obtenez de votre base de données, et elles retournent des valeurs basées sur des conditions données. Un exemple serait de retourner des données uniquement pour un mot-clé spécifique. Voici un exemple :

```javascript
db.collection("userInfo").where('username', '==', 'Ihechikara')
  .get()
  .then((querySnapshot) => {
    querySnapshot.forEach(doc =>{
        console.log(doc.data())
    })
  })
  .catch((error) => {
    console.log("Error getting documents: ", error);
  });
```

La requête ici est la même que dans la section précédente sauf pour la méthode **`where()`**, qui prend trois paramètres : le nom d'utilisateur, une évaluation pour le nom d'utilisateur, et la valeur avec laquelle nous voulons évaluer le nom d'utilisateur.

Donc, c'est comme dire : "Allez dans la collection `userInfo`, dans les documents, retournez un utilisateur dont le nom d'utilisateur est égal à 'Ihechikara'".

Vous pouvez décider comment vous voulez afficher votre résultat sur le front-end. Dans l'exemple ci-dessus, nous avons enregistré le résultat dans la console.

Voici d'autres opérateurs de comparaison que vous pouvez utiliser pour l'évaluation des requêtes :

* < inférieur à
* <= inférieur ou égal à
* > supérieur à
* => supérieur ou égal à
* != différent de
* array-contains
* array-contains-any
* in
* not-in

Vous pouvez voir le code pour cette section dans la [branche queries](https://github.com/ihechikara/firebase-firestore-tutorial/tree/queries).

## Comment ordonner et limiter les données

Comme l'indique le titre, vous pouvez ordonner l'arrangement de vos données ou limiter la quantité de données à retourner.

### Comment ordonner les données

```javascript
db.collection("userInfo").orderBy('username')
  .get()
  .then((querySnapshot) => {
    querySnapshot.forEach(doc =>{
        console.log(doc.data())
    })
  })
  .catch((error) => {
    console.log("Error getting documents: ", error);
  });

```

Cela retourne les données de la base de données par ordre alphabétique basé sur les noms d'utilisateur. Vous pouvez également changer l'ordre pour qu'il soit décroissant en ajoutant un 'desc' après le nom d'utilisateur. C'est-à-dire :

```javascript
db.collection("userInfo").orderBy('username', 'desc')
  .get()
  .then((querySnapshot) => {
    querySnapshot.forEach(doc =>{
        console.log(doc.data())
    })
  })
  .catch((error) => {
    console.log("Error getting documents: ", error);
  });

```

Vous pouvez également enchaîner les méthodes. Vous pouvez combiner la méthode **`where()`** avec la méthode **`orderBy()`** pour filtrer les données retournées, comme ceci :

```javascript
db.collection("userInfo").where("bio", "==", "Web Developer")
  .orderBy('username')
  .get()
  .then((querySnapshot) => {
    querySnapshot.forEach(doc =>{
        console.log(doc.data())
    })
  })
  .catch((error) => {
    console.log("Error getting documents: ", error);
  });
```

Si cela génère une erreur disant que la requête a besoin d'un index, cliquez sur l'URL dans le message d'erreur pour créer un index dans votre console.

### Comment limiter les données

```javascript
db.collection("userInfo").limit(1)
  .get()
  .then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
      console.log(doc.data());
    });
  })
  .catch((error) => {
    console.log("Error getting documents: ", error);
  });
```

La méthode **`limit()`** prend un paramètre qui est le nombre de documents à retourner. Dans l'exemple ci-dessus, un seul est retourné.

Vous pouvez voir le code pour cette section dans la [branche order_and_limit](https://github.com/ihechikara/firebase-firestore-tutorial/tree/order_and_limit).

## Conclusion

Et c'est tout pour cet article. Si vous avez suivi jusqu'à ce point, vous devriez avoir assez de connaissances pour commencer à créer des applications web géniales en utilisant Firestore.

Cet article ne couvre pas tout ce qu'il y a à savoir sur Firestore, alors allez-y et consultez la [documentation](https://firebase.google.com/docs/firestore) pour en apprendre davantage.

Voici le [lien](https://github.com/ihechikara/firebase-firestore) vers le dépôt de l'article.

Vous pouvez me suivre sur Twitter [@ihechikara2](https://twitter.com/Ihechikara2). Merci pour votre temps.