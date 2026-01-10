---
title: Comment créer une application Todo basée sur la voix en utilisant React, Firebase
  et Alan AI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-16T15:32:00.000Z'
originalURL: https://freecodecamp.org/news/build-a-voice-based-weather-application-using-react-and-alan-ai
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/How-to-Build-a-Weather-Application-using-React--36-.png
tags:
- name: Apps
  slug: apps-tag
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Firebase
  slug: firebase
- name: React
  slug: react
seo_title: Comment créer une application Todo basée sur la voix en utilisant React,
  Firebase et Alan AI
seo_desc: 'By Nishant Kumar

  React Todo applications are generally very basic – in fact, they''re a great exercise
  if you''re a React beginner and want to work on building up your skills.

  But have you ever built a Todo application where a user can add todos using ...'
---

Par Nishant Kumar

Les applications Todo React sont généralement très basiques – en fait, elles constituent un excellent exercice si vous êtes débutant avec React et que vous souhaitez développer vos compétences.

Mais avez-vous déjà créé une application Todo où un utilisateur peut ajouter des todos en utilisant des commandes vocales ? Cela la rend un peu plus complexe et excitante.

C'est donc ce que nous allons faire dans ce tutoriel. Et pour construire cette application Todo basée sur la voix, nous allons utiliser trois outils principaux :

1. React – pour l'interface utilisateur.
2. Firebase – pour la base de données.
3. Alan AI – pour implémenter les commandes vocales.

Alors, commençons.

## Comment créer l'interface utilisateur de l'application Todo en utilisant React

Créons d'abord notre application React. Tapez simplement la commande suivante :

```
npx create-react-app react-todo-alan-firebase
```

Elle initialisera et créera notre application React comme ceci. Ensuite, nous naviguerons dans ce dossier et démarrerons l'application en utilisant npm start.

Maintenant, créons un dossier appelé components. Il contiendra notre composant principal, appelé Todo.js. Créez également le fichier Todo.js.

```
import React from 'react'

export default function Todo() {
    return (
        <div>
            
        </div>
    )
}

```

Donnez à l'application un en-tête (ou un nom), quelque chose comme Application Todo basée sur la voix, ou tout ce que vous choisissez.

```
import React from 'react'

export default function Todo() {
    return (
        <div>
            <h2>Application Todo basée sur la voix</h2>
        </div>
    )
}

```

Ensuite, importez ce composant dans votre fichier App.js.

```
import './App.css';
import Todo from './components/Todo';

function App() {
  return (
    <div>
      <Todo />
    </div>
  );
}

export default App;

```

Vous verrez l'en-tête sur l'écran de sortie.

Faisons en sorte que l'en-tête apparaisse au centre. Donc, donnez à la balise `h2` un nom de classe header dans le composant Todo.js.

```
import React from 'react'

export default function Todo() {
    return (
        <div>
            <h2 className="header">Application Todo basée sur la voix</h2>
        </div>
    )
}

```

Puis, nous ajouterons un peu de style dans le fichier App.css pour que l'en-tête soit centré.

```
.header{
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-215217.png)

Vous verrez la sortie ci-dessus sur l'écran, avec l'en-tête centré.

Maintenant, créons une carte qui contiendra nos éléments todo.

```
import React from 'react'

export default function Todo() {
    return (
        <div className="todo-main">
            <h2 className="header">Application Todo basée sur la voix</h2>

            <div className="todo-card">

            </div>
        </div>
    )
}

```

Créez une div et faites en sorte que le `className` soit `todo-card`. Vous verrez que la div parent principale a le `className` de `todo-main`. C'est parce que nous avons besoin de tout au centre.

```
.todo-main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.header {
  text-align: center;
}

.todo-card {
  border: 1px dashed #1f133d;
  height: 50vh;
  width: 50vh;
  border-radius: 20px;
}

```

Et ajoutez les styles ci-dessus à App.css. Cela ressemblera à ceci maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-220125.png)

Ajoutons maintenant les listes.

```
import React from 'react'

export default function Todo() {
    return (
        <div className="todo-main">
            <h2 className="header">Application Todo basée sur la voix</h2>

            <div className="todo-card">
                <div className="todo-list">
                    <h3>
                        Laver les vêtements
                    </h3>
                </div>
                <div className="todo-list">
                    <h3>
                        Cuisiner le dîner
                    </h3>
                </div>
                <div className="todo-list">
                    <h3>
                        Coder un logiciel
                    </h3>
                </div>
            </div>
        </div>
    )
}

```

J'ai donc créé une div, et elle contient les éléments dans les balises `h3`. Ces textes sont statiques pour l'instant, mais nous allons bientôt créer des textes dynamiques aussi, provenant de la base de données Firebase.

Et voici nos styles mis à jour :

```
.todo-main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.header {
  text-align: center;
}

.todo-card {
  border: 1px dashed #1f133d;
  height: 50vh;
  width: 50vh;
  border-radius: 20px;
}

.todo-list{
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-220710.png)

Voici donc la sortie maintenant, avec trois éléments sur notre liste.

Maintenant, ajoutons une icône de fermeture, qui supprimera chaque élément après que nous ayons terminé avec lui.

Et pour ajouter des icônes, nous avons besoin d'un package d'icônes. Donc, installons React Icons avec cette commande :

```
npm install react-icons --save
```

Après l'installation, choisissez n'importe quel package d'icônes dans la barre latérale de gauche.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-220805.png)

J'utilise Feather Icons, donc je vais l'importer.

Tout d'abord, importons ce package en utilisant cette commande :

```
import { FiX } from "react-icons/fi";
```

Ensuite, appelez-le après la balise h3.

```
import React from 'react'
import { FiX } from "react-icons/fi";
export default function Todo() {
    return (
        <div className="todo-main">
            <h2 className="header">Application Todo basée sur la voix</h2>

            <div className="todo-card">
                <div className="todo-list">
                    <h3>
                        Laver les vêtements
                    </h3>
                    <FiX />
                </div>
                <div className="todo-list">
                    <h3>
                        Cuisiner le dîner
                    </h3>
                    <FiX />
                </div>
                <div className="todo-list">
                    <h3>
                        Coder un logiciel
                    </h3>
                    <FiX />
                </div>
            </div>
        </div>
    )
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-221145.png)

Ci-dessus, voici à quoi ressemble notre application maintenant. Mais nous voulons que l'icône de fermeture et l'élément todo soient sur la même ligne.

Donnez à l'icône un nom de classe `close-icon`.

```
 <FiX className="close-icon" />
```

Et dans App.css, ajoutez les styles suivants :

```
.todo-list {
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-icon {
  margin-left: 10px;
}

```

Notre composant Todo.js aura le code final suivant jusqu'à ce point :

```
import React from 'react'
import { FiX } from "react-icons/fi";
export default function Todo() {
    return (
        <div className="todo-main">
            <h2 className="header">Application Todo basée sur la voix</h2>

            <div className="todo-card">
                <div className="todo-list">
                    <h3>
                        Laver les vêtements
                    </h3>
                    <FiX className="close-icon" />
                </div>
                <div className="todo-list">
                    <h3>
                        Cuisiner le dîner
                    </h3>
                    <FiX className="close-icon" />
                </div>
                <div className="todo-list">
                    <h3>
                        Coder un logiciel
                    </h3>
                    <FiX className="close-icon" />
                </div>
            </div>
        </div>
    )
}

```

Et notre App.css ressemble à ceci :

```
.todo-main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.header {
  text-align: center;
}

.todo-card {
  border: 1px dashed #1f133d;
  height: 50vh;
  width: 50vh;
  border-radius: 20px;
}

.todo-list {
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-icon {
  margin-left: 10px;
}

```

Maintenant, voici à quoi ressemblera notre interface utilisateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-221826.png)

## Comment ajouter Alan AI à notre projet React

Rendez-vous sur [https://alan.app/](https://alan.app/) et créez votre compte.

Après vous être connecté, vous pouvez créer un projet. Il suffit de cliquer sur le bouton plus.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-222106.png)

Mais avant de pouvoir l'utiliser, nous devons d'abord installer le package Alan AI. Donc, rendez-vous sur [https://alan.app/docs/client-api/web/react](https://alan.app/docs/client-api/web/react) pour la documentation React.

Installez Alan AI en utilisant la commande suivante :

```
npm install @alan-ai/alan-sdk-web --save
```

Maintenant, importons Alan dans notre fichier principal App.js.

```
import alanBtn from "@alan-ai/alan-sdk-web";
```

Ensuite, nous devons créer un Hook useEffect. Il démarrera notre service Alan chaque fois que notre composant est monté ou chargé.

```
useEffect(() => {
    alanBtn({
        key: 'YOUR_KEY_FROM_ALAN_STUDIO_HERE',
        onCommand: (commandData) => {
            if (commandData.command === 'go:back') {
                // Call the client code that will react to the received command
            }
        }
    });
}, []);
```

Ce `alanBtn` nécessite une clé que nous devons obtenir. Donc, dans le projet que vous avez créé dans Alan, vous devriez voir un bouton "Integrations" dans la barre supérieure. Cliquez sur ce bouton.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-222645.png)

Et là, vous obtiendrez votre clé.

Collez cette clé dans votre `alanBtn` dans votre application React, comme ceci :

```
import './App.css';
import Todo from './components/Todo';
import alanBtn from "@alan-ai/alan-sdk-web";
import { useEffect } from 'react'
function App() {
  useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {

      }
    });
  }, []);
  return (
    <div>
      <Todo />
    </div>
  );
}

export default App;

```

Maintenant, vérifiez la sortie, et vous verrez un bouton microphone.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-222913.png)

Maintenant, nous devons créer une Intention dans notre application Alan. Elle commencera par la commande Add, comme add Washing Clothes, add Write Some Code, et ainsi de suite. Donc, écrivons le code pour cela :

```
intent('Add $(item* (.*))', (p) => {
    if(p.item.value){
        p.play({ command: 'todoApp', data: p.item.value });
        p.play(`${p.item.value} added`);
    }
    else{
        p.play(`Cannot add Empty Item`);
    }
})
```

Il nous renverra également l'élément, que nous pouvons voir dans notre application React. Ici, nous avons également une vérification qui nous empêche d'ajouter un élément vide. Si nous essayons, il répondra avec "Cannot add Empty Item".

Maintenant, nous voulons recevoir l'élément parlé dans notre application React.

```
import './App.css';
import Todo from './components/Todo';
import alanBtn from "@alan-ai/alan-sdk-web";
import { useEffect } from 'react'
function App() {
  useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {
        console.log(commandData)
      }
    });
  }, []);
  return (
    <div>
      <Todo />
    </div>
  );
}

export default App;

```

Il suffit de faire un console.log de commandData, et vous obtiendrez le résultat suivant. N'oubliez pas de cliquer sur le bouton microphone et de dire quelque chose. Vous verrez ce que vous avez dit dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-223428.png)

Très bien, notre Alan AI est maintenant prêt.

## Comment utiliser Firebase pour envoyer des données à la base de données Firestore.

Nous allons maintenant envoyer ces données à Firebase.

Mais d'abord, nous devons l'installer. Rendez-vous sur [https://firebase.google.com/](https://firebase.google.com/) et créez un projet là-bas également.

Pour installer Firebase, tapez simplement `npm install firebase`.

Ensuite, créez une application dans le projet, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-223909.png)

Cela nous donnera des données de configuration. Créez simplement un fichier dans le dossier src, nommez-le `firebase-config.js`, et ajoutez ces données de configuration.

```
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCP8qL8z9BorGF3NZJsGb4vSaWHYyCVfc8",
    authDomain: "todo-firebase-alan.firebaseapp.com",
    projectId: "todo-firebase-alan",
    storageBucket: "todo-firebase-alan.appspot.com",
    messagingSenderId: "892581913000",
    appId: "1:892581913000:web:dbe08ac753c3adaab87d9d"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
```

N'oubliez pas d'exporter la const app.

Ensuite, nous devons également accéder à Firestore. Donc, importons-le ici dans notre fichier firebase-config.js.

```
import { getFirestore } from 'firebase/firestore'
```

```
export const database = getFirestore(app);
```

Et exportez-le également en bas.

```
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore'

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCP8qL8z9BorGF3NZJsGb4vSaWHYyCVfc8",
    authDomain: "todo-firebase-alan.firebaseapp.com",
    projectId: "todo-firebase-alan",
    storageBucket: "todo-firebase-alan.appspot.com",
    messagingSenderId: "892581913000",
    appId: "1:892581913000:web:dbe08ac753c3adaab87d9d"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const database = getFirestore(app);
```

C'est tout le code de firebase-config.

Maintenant, dans App.js, nous devons importer cette application et cette base de données.

```
import { app, database } from './firebase-config';
```

Ensuite, nous devons créer une connexion à notre Firebase Firestore. Pour cela, nous avons besoin de la propriété collection de Firebase Firestore. Nous allons également importer addDoc que nous utiliserons pour ajouter des données à Firestore.

```
import { collection, addDoc } from 'firebase/firestore';
```

Maintenant, créons la connexion à notre base de données.

Créez une variable, et mettez-y la base de données que nous avons importée du fichier firebase-config ainsi que le nom que nous voulons donner à notre collection. Puisque nous voulons que la collection soit todo-list, nous pouvons ajouter ce qui suit :

```
const databaseRef = collection(database, 'todo-list');
```

Pour ajouter des données, nous avons besoin de cette propriété addDoc.

La propriété addDoc prendra deux paramètres. Le premier est la connexion que nous avons créée, databaseRef. Le second est les données que nous voulons ajouter, sous forme d'objet.

Mettez addDoc dans le Hook useEffect comme ceci :

```
useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {
        addDoc(databaseRef, { item: commandData.data })
      }
    });
  }, []);
```

Actuellement, notre Firestore est vide.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-225805.png)

Maintenant, essayons cela. Dites quelque chose dans le microphone en commençant par la commande add, et cela sera visible dans Firebase Firestore.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-225922.png)

Vous voyez, ce que nous avons dit est maintenant ajouté dans Firebase.

Maintenant, essayons de lire et d'afficher ces données.

Passez `databaseRef` au composant Todo en tant que prop.

```
<Todo databaseRef={databaseRef}/>
```

Et recevez-le dans le composant Todo.

```
export default function Todo({databaseRef})
```

Créez un Hook useEffect dans le composant Todo.js, et à l'intérieur du Hook useEffect, créez la fonction `getData`.

```
useEffect(() => {
        const getData = async () => {
            
        }
        getData()
    }, [])
```

Nous utiliserons la propriété getDocs pour lire les données de Firebase Firestore. Et nous avons également besoin de cette connexion databaseRef, que nous avons passée en tant que prop précédemment.

```
let data = await getDocs(databaseRef);
```

```
const getData = async () => {
  let data = await getDocs(databaseRef);
  console.log(data.docs.map((item) => ({ ...item.data(), id: item.id })));
}
```

Nous mappons les données entrantes pour les rendre plus lisibles. Nous ajoutons également l'id unique de l'élément que l'application utilisera pour supprimer cet élément plus tard.

Vérifions notre console maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-231500.png)

Vous voyez, nous les obtenons.

Maintenant, stockons ces données dans un état pour les afficher dans l'application React.

Importez le Hook useState, puis créez un état de tableau comme ceci :

```
 const [todoList, setTodoList] = useState([]);
```

Et définissez les données en utilisant la fonction `setTodoList` :

```
setTodoList(data.docs.map((item) => ({ ...item.data(), id: item.id })));
```

Maintenant, mappons le tableau todoList.

```
<div className="todo-main">
            <h2 className="header">Application Todo basée sur la voix</h2>

            <div className="todo-card">
                {todoList.map((todo) => {
                    return (
                        <div className="todo-list">
                            <h3>
                                {todo.item}
                            </h3>
                            <FiX className="close-icon" />
                        </div>
                    )
                })}
            </div>
        </div>
```

Nous verrons nos données dans notre interface utilisateur React et cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-231945.png)

Maintenant, mettons à jour cela pour que chaque Todo commence par une majuscule.

Donnez à h3 le `className` de `todo-items`.

```
<h3 className="todo-item">
 {todo.item}
</h3>
```

Et dans App.css, ajoutez ce style :

```
.todo-item{
  text-transform: capitalize;
}
```

Et vous verrez que chaque Todo est maintenant en majuscule.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-232149.png)

Maintenant, si nous ajoutons quelque chose par commande vocale, notre liste dans React devrait se mettre à jour. Donc, configurons notre useEffect pour qu'il s'exécute chaque fois que nous disons quelque chose dans l'application.

Dans le fichier App.js, créez un état. Ce sera un booléen, avec l'état initial false.

```
const [update, setUpdate] = useState(false)
```

Cet état passera à true lorsque nous dirons quelque chose, ou lorsque le useEffect dans App.js s'exécutera.

```
useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {
        addDoc(databaseRef, { item: commandData.data })
        .then(() => {
          setUpdate(true);
        })
      }
    });
  }, []);
```

Ensuite, nous passerons l'état update et la fonction pour mettre à jour l'état dans Todo.js.

```
<Todo databaseRef={databaseRef} update={update} setUpdate={setUpdate}/>
```

Et recevez ces deux dans le composant Todo.

```
export default function Todo({ databaseRef, update, setUpdate })
```

Ensuite, dans le useEffect de Todo.js, une fois qu'il a récupéré nos données de Firebase Firestore, définissez update sur false en utilisant la fonction setUpdate. Ensuite, mettez l'état update dans le tableau de dépendances.

```
useEffect(() => {
        const getData = async () => {
            let data = await getDocs(databaseRef);
            setTodoList(data.docs.map((item) => ({ ...item.data(), id: item.id })));
        }
        getData()
        setUpdate(false)
    }, [update])
```

Cela peut être un peu confus, mais laissez-moi expliquer.

Lorsque nous parlons, l'état update passe de false à true. Ensuite, lorsque la récupération des données de Firestore est terminée, il passe de true à false. De cette façon, l'état change constamment. Ainsi, le useEffect est mis à jour chaque fois que l'état update change.

Essayons cela maintenant. Dites quelque chose et la liste sera mise à jour dynamiquement.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-233617.png)

Maintenant, ajoutons la fonction de suppression pour supprimer des éléments de Firebase Firestore et de notre application React.

Créez une fonction appelée `deleteItems`.

```
const deleteItems = () => {
        
}
```

Et liez cette fonction à l'icône `close` comme ceci :

```
<FiX className="close-icon" onClick={() => deleteItems()}/>
```

Lorsque nous cliquons sur une icône de fermeture particulière, nous devons passer l'id de cet élément à la fonction, qui sera utilisé pour supprimer cet élément.

```
<FiX className="close-icon" onClick={() => deleteItems(todo.id)}/>
```

Et dans la fonction, recevez-le.

Essayons de faire un console.log de notre id :

```
const deleteItems = (id) => {
  console.log(id)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-15-234631.png)

Nous obtiendrons cet id particulier dans la console.

Maintenant, avant de supprimer un élément todo, nous devons spécifier quel todo supprimer. Donc, nous allons créer une référence en utilisant cet id. Nous allons utiliser la propriété doc de Firestore.

Donc, importez d'abord doc de Firestore avec cette commande :

```
import { getDocs, doc } from 'firebase/firestore';
```

Ensuite, dans la fonction deleteItems, ajoutez le code suivant :

```
const data = doc(database, 'todo-list', id)
```

Ce doc prend trois paramètres – la base de données, le nom de la collection et l'id. Nous avons les trois.

La base de données a été importée de firebase-config. Le todo-list est le nom de la collection Firestore. Et l'id que nous avons obtenu du clic sur le bouton de fermeture.

Pour supprimer un élément, nous avons besoin d'une autre propriété appelée deleteDoc de Firestore.

```
import { getDocs, doc, deleteDoc } from 'firebase/firestore';
```

Ensuite, ajoutez simplement ce qui suit :

```
const deleteItems = (id) => {
   const data = doc(database, 'todo-list', id);
   deleteDoc(data)
}
```

Essayez maintenant – cliquez sur l'icône de fermeture, puis vérifiez Firestore. Cet élément sera supprimé.

Mais nous avons le même problème que nous avions lors des actions d'ajout et de lecture : l'application React ne se met pas à jour après avoir supprimé un élément.

Donc, la première chose à faire est de déplacer la fonction getData hors du Hook useEffect. Ne vous inquiétez pas, cela fonctionnera toujours.

```
const getData = async () => {
   let data = await getDocs(databaseRef);
   setTodoList(data.docs.map((item) => ({ ...item.data(), id: item.id })));
}

useEffect(() => {   
   getData()
   setUpdate(false)
}, [update])
```

Et dans la fonction deleteDoc, nous devons appeler à nouveau la fonction getData, pour récupérer les données mises à jour après que l'utilisateur a supprimé un élément.

```
const deleteItems = (id) => {
    const data = doc(database, 'todo-list', id);
    deleteDoc(data)
    .then(() => {
       getData()
    })
}
```

Voici tout le code de Todo.js :

```
import React, { useEffect, useState } from 'react'
import { FiX } from "react-icons/fi";
import { database } from '../firebase-config';
import { getDocs, doc, deleteDoc } from 'firebase/firestore';
export default function Todo({ databaseRef, update, setUpdate }) {
    const [todoList, setTodoList] = useState([]);
    const getData = async () => {
        let data = await getDocs(databaseRef);
        setTodoList(data.docs.map((item) => ({ ...item.data(), id: item.id })));
    }
    useEffect(() => {
        getData()
        setUpdate(false)
    }, [update])

    const deleteItems = (id) => {
        const data = doc(database, 'todo-list', id);
        deleteDoc(data)
            .then(() => {
                getData()
            })
    }

    return (
        <div className="todo-main">
            <h2 className="header">Application Todo basée sur la voix</h2>

            <div className="todo-card">
                {todoList.map((todo) => {
                    return (
                        <div className="todo-list">
                            <h3 className="todo-item">
                                {todo.item}
                            </h3>
                            <FiX className="close-icon" onClick={() => deleteItems(todo.id)} />
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

```

Et le code App.js également :

```
import './App.css';
import Todo from './components/Todo';
import alanBtn from "@alan-ai/alan-sdk-web";
import { useEffect, useState } from 'react';
import { app, database } from './firebase-config';
import { addDoc, collection } from '@firebase/firestore';
function App() {
  const databaseRef = collection(database, 'todo-list');
  const [update, setUpdate] = useState(false)
  useEffect(() => {
    alanBtn({
      key: '86e866fbe49666abd385ee5c9f9cbf5c2e956eca572e1d8b807a3e2338fdd0dc/stage',
      onCommand: (commandData) => {
        addDoc(databaseRef, { item: commandData.data })
          .then(() => {
            setUpdate(true);
          })
      }
    });
  }, []);
  return (
    <div>
      <Todo databaseRef={databaseRef} update={update} setUpdate={setUpdate} />
    </div>
  );
}

export default App;

```

Maintenant, nous pouvons ajouter des éléments en utilisant des commandes vocales, et ils seront stockés dans notre base de données Firebase. Ils s'afficheront également dans notre application React.

Il reste une dernière chose à faire. Dans notre fichier App.css, nous devons définir la hauteur de la carte sur auto, pour éviter que le texte ne déborde.

```
.todo-card {
  border: 1px dashed #1f133d;
  height: auto;
  width: 50vh;
  border-radius: 20px;
}
```

Et ceci est juste un design d'interface utilisateur simple. Vous pouvez utiliser vos propres designs si vous le souhaitez. Allez-y, construisez cette application géniale.

Merci d'avoir lu !

Vous pouvez consulter ma vidéo sur le même sujet à l'adresse [Let's build a Voice-Based Todo Application using React, Firebase, and Alan AI](https://youtu.be/BzHbI2AAXGs), qui se trouve sur ma chaîne YouTube.

> Bon apprentissage.