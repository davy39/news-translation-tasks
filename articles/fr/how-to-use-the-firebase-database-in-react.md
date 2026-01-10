---
title: Comment utiliser Cloud Firestore dans une application React
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-10-24T15:08:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-firebase-database-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/lautaro-andreani-xkBaqlcqeb4-unsplash.jpg
tags:
- name: database
  slug: database
- name: Firebase
  slug: firebase
- name: React
  slug: react
seo_title: Comment utiliser Cloud Firestore dans une application React
seo_desc: "Firebase provides some great services like NoSQL databases, authentication,\
  \ cloud storage, and much more.\nIn this tutorial, we will learn how to use your\
  \ React application to read and add data to your Firebase database. \nTo demonstrate\
  \ this, we will ..."
---

Firebase fournit certains services excellents comme des bases de données NoSQL, l'authentification, le stockage cloud, et bien plus encore.

Dans ce tutoriel, nous allons apprendre comment utiliser votre application React pour lire et ajouter des données à votre base de données Firebase.

Pour démontrer cela, nous allons apprendre comment construire une application Todo en utilisant React et Cloud Firestore (Firebase9 web SDK). Avant de commencer à construire, comprenons les outils que nous allons utiliser pour ce tutoriel.

## Qu'est-ce que Cloud Firestore ?

Contrairement à certaines bases de données qui stockent les données dans des tables (bases de données SQL), Cloud Firestore est une base de données non tabulaire qui stocke les données dans des collections.

Selon la [documentation](https://firebase.google.com/docs/firestore),

> "Cloud Firestore est une base de données flexible et évolutive pour le développement mobile, web et serveur. Cloud Firestore ne nécessite pas de créer explicitement des collections ou des documents. Cloud Firestore stocke les données dans des documents, qui sont stockés dans des collections."

Puisque nous ne nous concentrerons pas sur la partie design dans ce tutoriel, je fournirai le style CSS. Allons-y et configurons notre base de données.

## Comment configurer votre Cloud Firestore

Avant de configurer Cloud Firestore, vous devrez vous connecter à votre console Firebase. Voici comment faire.

### Se connecter à Firebase

Allez sur [Firebase Console](https://console.firebase.google.com/) et connectez-vous avec votre compte Google. Si vous n'avez pas encore de compte, inscrivez-vous avec votre compte Google et suivez les invites pour créer un nouveau projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/1-1.png)
_console firebase_

Choisissez un nom approprié pour votre projet et cliquez sur **continuer**. Pour ce tutoriel, nous nommerons notre projet **Todo-app**.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/2-2.png)
_configuration de firebase_

Votre écran suivant est une invite pour activer **Google Analytics**. Vous pouvez choisir de le désactiver. Nous n'aurons pas besoin de Google Analytics pour ce tutoriel, donc je vais le désactiver.

Félicitations, vous avez réussi à configurer votre Cloud Firestore. Votre écran suivant sera le tableau de bord de la console Firebase.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/3-2.png)
_tableau de bord firebase_

## Comment configurer une application React pour Firebase

Nous allons créer une nouvelle application React en utilisant **npx**. Nous allons créer une nouvelle application React avec **firebase-react-app** comme nom de l'application et aussi comme nom du répertoire. En utilisant la ligne de commande, entrez le code suivant pour créer une nouvelle application React :

```
$ npx create-react-app firebase-react-app
```

Pour démarrer votre application React, utilisez les commandes suivantes. Cela ouvre votre application React dans Visual Studio Code, navigue dans votre nouveau répertoire, et enfin exécute votre application React.

```
$ code .
$ cd firebase-storage
$ npm run start
```

Il y a un tas de fichiers de démarrage et de code dont nous n'aurons pas besoin pour ce tutoriel. Nous allons supprimer les fichiers **App.test.js**, **index.css**, et **logo.svg**. Nous allons également supprimer le code de démarrage dans les fichiers **App.css** et **App.js**.

## Aperçu de la console Firebase

Le tableau de bord Firebase a une **barre latérale** et une vue **principale**. La barre latérale a été catégorisée en différents produits que Firebase offre. En plus de notre domaine d'intérêt, Cloud Firestore, Firebase a beaucoup de produits avec des services excellents pour l'authentification, le stockage, les bases de données, et plus encore.

Pour commencer à utiliser les services Cloud Firestore, naviguez vers votre tableau de bord Firebase, cliquez sur le menu déroulant **Build**, et sélectionnez **Firestore Database**.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot--193-.png)
_Tableau de bord Firebase montrant la vue cloud firestore_

Sélectionnez l'option pour **créer une base de données** et définissez les règles de sécurité pour démarrer en **mode test**. Sélectionnez l'emplacement Firestore par défaut et cliquez pour **activer votre base de données**.

Continuez à configurer votre Firebase en ajoutant le SDK web Firebase à notre application React. Pour ce faire, cliquez sur l'icône web sur votre écran de vue d'ensemble du projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/3-3.png)
_Cliquez sur l'icône web_

Votre prochaine invite vous demandera d'ajouter Firebase à votre application web. Vous devrez choisir un **surnom** pour votre application. Nous utiliserons **Todo-app** comme surnom pour notre application.

Nous n'aurons pas besoin de l'hébergement Firebase. Vous pouvez donc laisser la case pour l'hébergement Firebase non cochée. Ensuite, cliquez sur **register app**.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/4-1.png)
_Écran Firebase pour enregistrer votre application web_

Votre prochaine invite vous demandera d'installer le dernier SDK de Firebase en utilisant [npm](https://www.npmjs.com/) et fournira également la configuration de votre application web.

```
$ npm install firebase
```

Cliquez sur **Continue to Console**. Vous êtes à moitié chemin d'ajouter Firebase à votre application React.

La configuration de votre application web sera affichée avec vos clés API uniques et quelques autres informations utiles.

Créez un fichier nommé **firebase.js** dans le répertoire **src** et collez votre configuration Firebase dans le fichier **firebase.js**. Nous allons également importer le SDK Cloud Firestore dans notre application React. Voici à quoi votre **firebase.js** devrait ressembler :

```js
 // Importez les fonctions dont vous avez besoin depuis les SDK dont vous avez besoin
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
// TODO: Ajoutez des SDK pour les produits Firebase que vous souhaitez utiliser
// https://firebase.google.com/docs/web/setup#available-libraries
// Configuration Firebase de votre application web
const firebaseConfig = {
  apiKey: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  projectId: "XXXXXXXXXXXXXXXXX",
  storageBucket: "XXXXXXXXXXXXXXXXXXXXXXXX",

  messagingSenderId: "XXXXXXXXXXXXXXX",
  appId: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
};
// Initialisez Firebase

const app = initializeApp(firebaseConfig);
// Exportez la base de données firestore
// Elle sera importée dans votre application react chaque fois que cela sera nécessaire
export const db = getFirestore(app);
```

Félicitations à nouveau. Vous avez réussi à initialiser Firebase et Cloud Firestore, et à les exporter afin de pouvoir les utiliser dans votre application React.

## Comment créer notre application

Pour écrire un code plus propre, nous allons créer un dossier **components** à l'intérieur de notre répertoire **src**. Nous allons ensuite créer un fichier **Todo.js** à l'intérieur de notre dossier **components**. Ce nouveau fichier sera importé dans le fichier **App.js** afin d'être rendu.

Le fichier **Todo.js** contiendra le code suivant :

```js
import React, { useState } from 'react';
import "../App.css";
 
const Todo = () => {
    const [todo, setTodo] = useState("")
   
    const addTodo = (e) => {
        e.preventDefault();        
    }
 
    return (
        <section className="todo-container">
            <div className="todo">
                <h1 className="header">
                    Todo-App
                </h1>
   
                <div>
   
                    <div>
                        <input
                            type="text"
                            placeholder="Qu'avez-vous à faire aujourd'hui ?"
                            onChange={(e)=>setTodo(e.target.value)}
                        />
                    </div>
   
                    <div className="btn-container">
                        <button
                            type="submit"
                            className="btn"
                            onClick={addTodo}
                        >
                            Soumettre
                        </button>
                    </div>
   
                </div>
   
                <div className="todo-content">
                    ...
                </div>
            </div>
        </section>
    )
}
 
export default Todo
```

### Explication du code :

Le fichier **Todo.js** contient une balise d'entrée (pour prendre l'entrée de l'utilisateur), un bouton avec une fonction **onClick** (que nous utiliserons pour poster des données à notre Firestore), et une fonction **onChange** qui gère les états.

Nous n'irons pas en profondeur dans la gestion de l'entrée du formulaire. Le code ci-dessus montre comment le faire avec le hook **useState**.

Chaque fois que le bouton est cliqué, la valeur de l'entrée, qui sera gérée par les hooks useState, sera ajoutée à Cloud Firestore.

Comme je l'ai mentionné ci-dessus, ce n'est pas un tutoriel CSS. Voici donc le code pour le style CSS que vous pouvez copier et coller :

```css
*{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
.todo-container {
    display: flex;
    justify-content: center;
    align-items: center;    
}
 
.todo {
    width: 70%;
    margin: 3rem auto 0 auto;    
}
 
.header {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}
 
input {
    padding: 10px 3px;
    width: 100%;
}
 
.btn-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 1rem;
}
 
.btn {
    padding: 10px 1rem;
    background: #334;
    color: white;
    border-radius: 5px;
    cursor: pointer;
}
 
.todo-content {
    margin-top: 2rem;
}
```

## Comment ajouter des données à Cloud Firestore

Vous pouvez ajouter des données obtenues à partir de l'entrée à Cloud Firestore en utilisant le code suivant :

```js
import { collection, addDoc } from "firebase/firestore";
import {db} from '../firebase';
   
    const addTodo = async (e) => {
        e.preventDefault();  
       
        try {
            const docRef = await addDoc(collection(db, "todos"), {
              todo: todo,    
            });
            console.log("Document écrit avec l'ID : ", docRef.id);
          } catch (e) {
            console.error("Erreur lors de l'ajout du document : ", e);
          }
    }

```

### Explication du code :

Dans Cloud Firestore, les données sont stockées dans des collections. Pour ajouter des données à Firestore, importez les fonctions **Collection** et **addDoc**. Nous importons également la **db** initialisée dans le fichier **firebase.js**.

Lorsque le bouton est cliqué, Cloud Firestore crée une collection (que nous avons nommée **todos**) et ajoute des données en tant que document à la collection **todos**.

Félicitations si vous suivez toujours. Vous avez réussi à ajouter vos données à Firebase.

## Comment lire les données

Vous pouvez toujours vérifier votre tableau de bord de la console Firebase pour voir toutes les données que vous avez ajoutées.

Pour récupérer les données ajoutées à votre Firestore, nous utiliserons la méthode **get** de Firebase pour lire tous les documents ajoutés à une collection. Vous pouvez ajouter des données lues à Cloud Firestore en utilisant le code suivant :

```js
import { collection, getDocs } from "firebase/firestore";
import {db} from '../firebase';
Import { useState } from 'react';
 
   const [todos, setTodos] = useState([]);
 
    const fetchPost = async () => {
       
        await getDocs(collection(db, "todos"))
            .then((querySnapshot)=>{               
                const newData = querySnapshot.docs
                    .map((doc) => ({...doc.data(), id:doc.id }));
                setTodos(newData);                
                console.log(todos, newData);
            })
       
    }
   
    useEffect(()=>{
        fetchPost();
    }, [])
```

### Explication du code :

Nous avons importé les fonctions **collection** et **getDocs** de Firebase. Nous avons utilisé la fonction **getDocs** pour obtenir des données à partir de la collection que nous avons initialement créée. Nous avons utilisé le hook **useEffect** pour récupérer les données après chaque nouveau rendu. Nous avons utilisé le hook **useState** pour gérer les données obtenues de Firestore. Nous avons mappé chaque document dans la collection **Todos** et ajouté chaque valeur au tableau **setTodos**.

Le tableau **todo** contient maintenant toutes les données que nous avons ajoutées à Firestore. Nous pouvons lire chaque entrée todo que nous avons ajoutée à la base de données Firestore en utilisant le code suivant :

```js
<div className="todo-content">
    {
        todos?.map((todo,i)=>(
            <p key={i}>
                {todo.todo}
            </p>
        ))
    }
</div>
```

Si vous suivez toujours jusqu'à ce point, félicitations. Vous avez réussi à ajouter et à lire des données à partir de Cloud Firestore en utilisant React.js. Voici le code complet de notre fichier Todo.js :

```todo.js
import "../App.css";
import React, { useState, useEffect } from 'react';
import { collection, addDoc, getDocs } from "firebase/firestore";
 
 
const Todo = () => {
    const [todo, setTodo] = useState("");
    const [todos, setTodos] = useState([]);
 
    const addTodo = async (e) => {
        e.preventDefault();  
       
        try {
            const docRef = await addDoc(collection(db, "todos"), {
              todo: todo,    
            });
            console.log("Document écrit avec l'ID : ", docRef.id);
          } catch (e) {
            console.error("Erreur lors de l'ajout du document : ", e);
          }
    }
 
    const fetchPost = async () => {
       
        await getDocs(collection(db, "todos"))
            .then((querySnapshot)=>{              
                const newData = querySnapshot.docs
                    .map((doc) => ({...doc.data(), id:doc.id }));
                setTodos(newData);                
                console.log(todos, newData);
            })
       
    }
   
    useEffect(()=>{
        fetchPost();
    }, [])
 
 
    return (
        <section className="todo-container">
            <div className="todo">
                <h1 className="header">
                    Todo-App
                </h1>
   
                <div>
   
                    <div>
                        <input
                            type="text"
                            placeholder="Qu'avez-vous à faire aujourd'hui ?"
                            onChange={(e)=>setTodo(e.target.value)}
                        />
                    </div>
   
                    <div className="btn-container">
                        <button
                            type="submit"
                            className="btn"
                            onClick={addTodo}
                        >
                            Soumettre
                        </button>
                    </div>
   
                </div>
   
                <div className="todo-content">
                    {
                        todos?.map((todo,i)=>(
                            <p key={i}>
                                {todo.todo}
                            </p>
                        ))
                    }
                </div>
            </div>
        </section>
    )
}
 
export default Todo
```

## Conclusion

Si vous avez suivi les instructions jusqu'à ce point, vous devriez être en mesure de travailler avec Cloud Firestore dans votre application React.

Cloud Firestore fait plus que simplement ajouter et récupérer des données. Vous pouvez consulter la [documentation](https://firebase.google.com/docs/firestore/quickstart) pour en apprendre davantage.

J'espère que vous avez appris beaucoup de choses à travers ce tutoriel. Bon codage !