---
title: TypeScript dans React – Comment gérer l'état avec Firebase Cloud Firestore
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-19T17:04:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-state-in-react-apps-with-firebase-cloud-firestore
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-quintin-gellar-313782.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Firebase
  slug: firebase
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
- name: TypeScript
  slug: typescript
seo_title: TypeScript dans React – Comment gérer l'état avec Firebase Cloud Firestore
seo_desc: "By Olasunkanmi Balogun\nState management is essential in today's world\
  \ of web development. If you do it well, it helps you create apps that are reliable\
  \ and effective. \nFirebase is a Backend-as-a-Service platform that has gained popularity\
  \ along with ..."
---

Par Olasunkanmi Balogun

La gestion de l'état est essentielle dans le monde actuel du développement web. Si vous le faites bien, cela vous aide à créer des applications fiables et efficaces. 

[Firebase](https://firebase.google.com/) est une plateforme Backend-as-a-Service qui a gagné en popularité avec l'émergence de l'architecture serverless et des technologies cloud. Et [Cloud Firestore](https://firebase.google.com/docs/firestore) est une base de données NoSQL scalable et flexible que Firebase propose dans le cadre de ses services. 

En combinant ces deux éléments, vous pouvez stocker et synchroniser des données pour vos applications. Cela aide à la gestion de l'état.

Cet article vous guidera à travers la mise en œuvre d'une gestion d'état efficace pour ce [Frontend Mentor Todo App Challenge](https://www.frontendmentor.io/challenges/todo-app-Su1_KokOW) dans un environnement TypeScript, en utilisant Firebase Cloud Firestore. 

Le défi consiste à effectuer les opérations CRUD (Create, Read, Update, Delete) suivantes :

- Ajouter de nouvelles tâches à la liste
- Marquer les tâches comme complétées
- Supprimer les tâches de la liste
- Filtrer par toutes/actives/complétées tâches
- Effacer toutes les tâches complétées

Ce défi est un excellent cas d'utilisation pour montrer les fonctionnalités de Cloud Firestore en raison des procédures mentionnées ci-dessus. Vous aurez une bonne compréhension de l'utilisation de Firebase Cloud Firestore pour créer des applications dynamiques et scalables à la fin de l'article. Lorsque vous êtes prêt, plongeons-nous dedans.

Juste une note : dans cet article, nous nous concentrerons uniquement sur la mise en œuvre de la fonctionnalité CRUD pour le défi. Nous n'aborderons aucun aspect du style.

### Voici ce que nous allons couvrir :

1. [Comment configurer le projet](#heading-installation)
2. [Comment créer la structure de votre liste de tâches](#heading-creation-structure-liste-taches)
3. [Comment ajouter de nouvelles tâches à la liste](#heading-ajout-nouvelles-taches)
4. [Comment peupler les tâches de la base de données vers l'interface utilisateur](#heading-peupler-taches-interface)
5. [Comment marquer les tâches comme complétées](#heading-marquer-taches-completees)
6. [Comment supprimer les tâches de la liste](#heading-supprimer-taches-liste)
7. [Comment filtrer par toutes, actives ou complétées tâches](#heading-filtrer-taches)
8. [Comment effacer toutes les tâches complétées](#heading-effacer-taches-completees)
9. [Comment afficher le nombre de tâches non complétées](#heading-afficher-taches-non-completees)
10. [Conclusion](#heading-conclusion)

## Prérequis

1. Vous avez des connaissances en TypeScript et JavaScript, en particulier les types de données et les méthodes.
2. Vous êtes familier avec la bibliothèque React.
3. Vous avez des connaissances de base sur l'API Context.
4. Vous savez comment créer un projet Firebase et configurer Firebase.

Des connaissances préalables de Firebase Firestore ne sont pas nécessaires, mais c'est un plus.

## Comment configurer le projet

### Configurer votre projet React TypeScript

Vous allez commencer par créer une nouvelle application React avec [Vite](https://vitejs.dev)

Pour créer un projet en utilisant Vite, entrez dans le dossier où vous hébergez tous vos projets – dans mon cas, c'est un dossier `Repos` dans mon dossier `desktop`. 

Avec Vite, vous pouvez directement spécifier le nom du projet et le modèle que vous souhaitez utiliser avec une seule commande. C'est aussi simple que cela :

```npm!
npm create vite@latest todolist-app -- --template react-ts
```

Après avoir tapé la commande ci-dessus dans votre terminal, vous obtiendrez une invite qui ressemble à ceci : 

![Invite à taper oui](https://i.imgur.com/2rd9CzK.png)

Vous avez votre projet après avoir fourni la réponse appropriée 🎉 :

![Projet terminé](https://i.imgur.com/MJKMmLp.png)

Maintenant, allez dans le dossier du projet que vous venez de créer avec cette commande : 

```cmd!
cd todolist-app
```

Pour installer les dépendances, exécutez :

```npm!
npm install
```

Puis démarrez votre serveur de développement : 

```npm!
npm run dev
```

Votre serveur de développement devrait fonctionner sur le `port 5173` de votre serveur local, s'il n'est pas utilisé.

![Serveur de développement démarré sur le port 5173](https://i.imgur.com/1eayCtl.png)

### Configurer Firebase dans votre projet

Il est maintenant temps d'installer Firebase dans votre environnement de développement avec cette commande :

```npm!
npm install firebase
```

Vous devez d'abord [créer un projet Firebase](https://firebase.google.com/docs/web/setup) et une [base de données Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart) afin d'utiliser Cloud Firestore pour lire et écrire des données.

Créez un dossier nommé `components`, et à l'intérieur du dossier, créez un nouveau fichier appelé `firebaseConfig.ts`. Copiez votre configuration Firebase dedans et initialisez Cloud Firestore comme vu [ici](https://firebase.google.com/docs/firestore/quickstart#initialize).

Si vous avez des difficultés à configurer cela, n'hésitez pas à me contacter.

### Configurer l'API Context

À l'intérieur de votre dossier `components`, créez un nouveau fichier appelé `Context.tsx`. Le code ci-dessous configure une `API Context` dans React pour gérer l'état que nous utiliserons tout au long du projet. Ne vous inquiétez pas si vous ne comprenez pas le code à ce moment-là – je l'expliquerai étape par étape plus tard dans cette section.

```tsx!
// Context.tsx

import React, { useContext, useState } from "react";

type ValueProp = {
    userId: string;
    setUserId: React.Dispatch<React.SetStateAction<string>>;
}

type ContextProp = {
    children: React.ReactNode
} 

export const AppContext = React.createContext({} as ValueProp); //créer l'API context

//corps de la fonction
export default function Context({ children }: ContextProp) {

const [ userId, setUserId ] = useState<string>('');

    return (
        <AppContext.Provider value={{userId, setUserId}}>
            {children}
         </AppContext.Provider>
    )
}

export const useGlobalContext = ():ValueProp => {
    return useContext(AppContext);
}
```

Le type `ValueProp` spécifie la forme de la valeur qui sera stockée dans le `context`, qui dans ce cas inclut le `userId` qui est de type `string` et `setUserId` de type `React.Dispatch`.

Les props qui seront fournies au composant `Context` sont spécifiées par le type `ContextProp`. La prop `children` est de type `React.ReactNode`, ce qui indique que tout composant React valide peut être passé en tant qu'enfant au composant `Context` car c'est un `ReactNode`.

Ensuite, nous créons un nouveau `Context` et l'assignons à la variable `AppContext`. `{}` est un objet vide qui sert de valeur initiale pour le contexte. 

L'[assertion de type](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) `as ValueProp` indique à TypeScript que cet objet vide se conforme au type `ValueProp`. Cela est nécessaire car TypeScript ne peut pas déduire le type d'un objet vide, nous devons donc lui dire explicitement que l'objet que nous créons se conforme au type que nous avons défini – c'est-à-dire, `ValueProp`.

La fonction `Context` est le composant fournisseur qui enveloppe les composants `children` et leur passe les valeurs `userId` et `setUserId` via la prop `value`, fournie par le composant `AppContext.Provider`.

La fonction `useGlobalContext` est un hook personnalisé qui simplifie l'accès à la valeur `userId` depuis n'importe quel composant de l'application. Elle utilise le hook `useContext` pour récupérer l'objet `AppContext` et retourner les propriétés `userId` et `setUserId` de l'objet `value` du contexte.

Notez que nous avons ajouté la variable `userId` comme paramètre requis dans le but de rendre la liste de tâches plus personnalisée pour chaque utilisateur. Elle est généralement obtenue lors du processus d'authentification, que nous n'aborderons pas dans cet article. 

Si vous êtes nouveau dans l'authentification Firebase, vous pouvez consulter ce [tutoriel](https://firebase.google.com/docs/auth) pour plus d'informations.

Maintenant que nous avons une bonne compréhension du code, rendons la valeur `Context` accessible dans tout notre projet. 

Pour y parvenir, allez dans le composant `main.tsx` et enveloppez le `Context` autour du composant `App` comme montré ci-dessous :

```tsx!
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import Context from './components/Context'


ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Context>  // enveloppez-le ici
    <App />
    </Context>
  </React.StrictMode>,
)

```

Avec votre configuration complète, il est temps de passer à la création de la structure de votre liste de tâches.

## Comment créer la structure de votre liste de tâches

Nettoyez le code de base dans votre fichier `App.tsx` et copiez la structure suivante :

```tsx!
import { useState } from "react"

export default function App() {

  const [ title, setTitle ] = useState<string>('')

  return (

     <div style={{
       display: 'flex',
       justifyContent: "center",
       alignContent:"center"
     }}>

    <div style={{
      width:'300px' }}>

      <p>Application de liste de tâches</p>

      <form style={{
        marginTop: '5px'}}>
      <input value={task} 
      onChange={(e) => setTitle(e.target.value)}/>
      </form>
      <div style={{
        marginTop: '10px'
      }}>
      <div style={{
         display:'flex',
         justifyContent: 'space-between',
         marginTop:'10px'
         
      }}>
      <label>
         <input type="checkbox"/>          
             Terminer le tutoriel de la liste de tâches         
        </label>
        <button>Supprimer</button>
      </div> 
      </div>
      {/* pied de page */}

       <footer style={{
         marginTop: '10px'
       }}>  
         <div style={{
          display: 'flex',
          justifyContent:'space-between',
          }}>
          <button>Toutes</button>  
          <button>Actives</button>  
          <button>Complétées</button>  
         </div>
         
         <div style={{
          display: 'flex',
          justifyContent:'space-between',
          marginTop: '10px'
          }}>
         <p>0 éléments restants</p>
         <button>
          Effacer les complétées
          </button>  
          </div>
      </footer>

    </div>
     </div>
  )
}

export default App
```

J'ai ajouté un style de base à la structure pour la rendre présentable 😁. Votre interface utilisateur devrait ressembler à ceci :
![Produit final du tutoriel de la liste de tâches](https://www.freecodecamp.org/news/content/images/2023/04/Todo-list-tutorial-final-product.png)

Un élément de formulaire contient un champ `input` qui contient la valeur du titre de la tâche et le gestionnaire d'événements `onChange` qui met à jour l'état du titre lorsque l'utilisateur tape. Nous utilisons cela pour ajouter de nouvelles tâches à la liste lorsque l'utilisateur soumet le formulaire.  

L'élément `div` en dessous contient une tâche factice avec une `label` qui inclut une entrée `checkbox` pour indiquer si la tâche est complète ou non et une balise `p` pour supprimer les tâches. Soyez conscient qu'une liste dynamique de tâches de notre base de données Firestore sera ensuite contenue dans cette balise `div`.

Nous utilisons deux balises `div` pour implémenter le pied de page. La première contient trois éléments `button` qui ont été stylisés pour montrer les options de filtre côte à côte. La seconde contient des éléments `p` et `button` qui montrent les tâches restantes non terminées et effacent les tâches complétées, respectivement.

Maintenant que nous avons notre structure en place, mettons-nous au travail ! 😀

## Comment ajouter de nouvelles tâches à la liste

Il est utile d'être quelque peu familier avec le modèle de données Cloud Firestore avant de commencer à ajouter des tâches à notre liste. Jetons un rapide coup d'œil au modèle de données Cloud Firestore pour mieux comprendre comment les données sont stockées dans la base de données.

Cloud Firestore organise les données en `collections` et `documents`. Un `document` est l'unité de base de stockage dans Firestore et est représenté par un ensemble de paires clé-valeur. 

En plus des `collections` et des `documents`, Firestore permet également les `sous-collections`, qui sont des `collections` imbriquées dans un `document`. 

Pour plus d'informations sur le modèle de données de Firestore, consultez la [documentation officielle](https://firebase.google.com/docs/firestore/data-model).

Maintenant que vous avez une compréhension de base du modèle de données, passons à la création d'une liste de tâches.

Tout d'abord, mettez à jour votre fichier `App.tsx` comme vu ci-dessous. Si vous ne comprenez pas le code tout de suite, ne vous inquiétez pas – je vais tout expliquer plus tard :

```tsx!

import { useState } from "react"
import { useGlobalContext } from "./components/Context";
import { collection, addDoc } from "firebase/firestore";
import { db } from "./components/firebaseConfig";

export default function App() {

  const [ title, setTitle ] = useState<string>('')
  const { userId } = useGlobalContext()

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        if(title !== '') {
            try {
      await addDoc(collection(db, 'users', userId, 'tasks'), {
                     title,
                     completed: false,
                 })
                setTitle('')
                console.log('Tâche ajoutée avec succès')
            }
            catch(e) {
                console.log('Échec')
            }
          }
    }

  return (
     <div style={{
       display: 'flex',
       justifyContent: "center",
       alignContent:"center",
     }}>

    <div style={{
      width:'300px' }}>

      <p>Application de liste de tâches</p>

      <form 
      onSubmit={handleSubmit}
      style={{
        marginTop: '5px'}}>
      <input 
      value={title} onChange={(e) => setTitle(e.target.value)}/>
      </form>
      // reste de la structure
     </div>
     </div>
  )
}

```

Nous avons importé `useGlobalContext` du composant `Context.tsx` pour obtenir le `userId` de notre magasin. Nous avons également importé les fonctions `collection` et `addDoc` du package `firestore` pour créer une `collection` dans notre base de données et ajouter un document à la `collection`, respectivement. 

Ensuite, nous avons importé `db`, que nous utiliserons pour initialiser Cloud Firestore, depuis notre fichier `firebaseConfig` pour nous aider à obtenir une référence à la base de données distante.

Lorsque l'utilisateur soumet une nouvelle tâche, la fonction `handleSubmit` est appelée. Cette fonction empêche la soumission par défaut du formulaire. 

Si `title` n'est pas une chaîne vide, la fonction crée un nouveau `document` dans la `collection` de tâches de l'utilisateur actuel dans la base de données Firestore avec les propriétés `title` et `completed`. La propriété `title` est définie sur l'état `title` avec la syntaxe `object literal shorthand`, et la propriété `completed` est initialement définie sur `false`. Ensuite, elle efface le champ de saisie `title`. 

Si l'opération échoue, un message est enregistré dans la console. L'ensemble de l'opération est enfermé dans un bloc try et catch, ce qui aide à personnaliser les messages d'erreur.

Passons à l'étape suivante et récupérons nos données de la base de données pour peupler l'interface utilisateur.

## Comment peupler les tâches de la base de données vers l'interface utilisateur

Dans votre fichier `App.tsx`, incluez le code ci-dessous. Je l'expliquerai après.


```tsx!
import { useState, useEffect } from "react"
import { collection, addDoc, onSnapshot } from "firebase/firestore"; 

type Task = {
  title: string,
  completed: boolean,
  id:string,  
}[];       //définir le type de tâche

export default function App() {

  const [ tasks, setTasks ] = useState<Task>([])
  const docRef = collection(db,`users/${userId}/tasks`);

  useEffect(() => {
    if(userId !== '') {
       // onSnapshot pour obtenir les mises à jour des données en temps réel
       const unsubscribe = onSnapshot(docRef, (querySnapshot) => {
       const tasks = querySnapshot.docs.map((doc) => {
        const data = doc.data();
// retourner des données compatibles avec les types de données spécifiés dans la variable tasks c'est-à-dire title, completed et id
       return { 
         title: data.title,
         completed: data.completed,
         id: doc.id,
            }
          }); 
         setTasks(tasks)              
       });
         return () => {
         unsubscribe();
       };
        }
      }, [userId]);
    
    return (
    //input
    
    <div style={{
        marginTop: '10px'}}>
        {   
          tasks.length > 0 && (
             tasks.map(task => {
             const { id, title, completed } = task;
             return (               
               <div id={id} style={{
                  display:'flex',
                  justifyContent: 'space-between',
                  marginTop:'10px'
               }}>
               <label style={{               
               }}>
               <input type="checkbox"
                 checked={completed} />          
                 {
                  completed ? 
                  <s>{title}</s> 
                  : <span>{title}</span>
                }          
               </label>
               <button>Supprimer</button>
               </div>
             )}))}
        </div>
  // reste du code ici
    )

```

Nous avons importé le hook `useEffect` et la méthode [`onSnapshot`](https://firebase.google.com/docs/firestore/query-data/listen) pour récupérer des données de notre base de données Firestore et pour nous abonner aux mises à jour de notre `collection`, respectivement. 

Nous avons également défini un type appelé `Task` qui est un tableau d'objets avec les propriétés `title`, `completed` et `id`. Cela définira la forme de l'état `tasks`. 

Pour obtenir des données de la base de données, nous devons d'abord obtenir sa [référence](https://firebase.google.com/docs/firestore/data-model#references) dans la base de données. Par référence, j'entends l'emplacement du `document` dans la base de données. Cet emplacement est référencé dans la variable `docRef`.

Dans le hook `useEffect`, nous utilisons la méthode `onSnapshot` pour nous abonner aux mises à jour de la `collection` `docRef`. Chaque fois que la collection est mise à jour, l'objet `querySnapshot` contiendra les dernières données. Nous parcourons ensuite chaque document dans le `querySnapshot` et retournons un objet avec les propriétés `title`, `completed` et `id`. Nous définissons ce tableau d'objets comme le nouvel état de `tasks` en utilisant la fonction `setTasks`.

Le hook `useEffect` prend un tableau de dépendances qui contient `userId`. Cela garantit que le hook `useEffect` n'est appelé que lorsque le `userId` change.

Nous parcourons ensuite le tableau `tasks` et peuplons l'interface utilisateur avec une liste d'éléments à faire :
![Ajouter des tâches et peupler l'interface utilisateur](https://www.freecodecamp.org/news/content/images/2023/04/Add-to-dos---populating-the-UI.gif)

Lorsque une tâche est complétée, la case à cocher est `cochée` et le titre est barré. Passons à l'implémentation de cette fonctionnalité.

## Comment marquer les tâches comme complétées
 
Lorsque l'utilisateur coche ou décoche la `case à cocher`, nous voulons mettre à jour le statut de complétion de la tâche correspondante dans Firestore. Votre `App.tsx` devrait inclure le code suivant :

```tsx!
import { collection, addDoc, onSnapshot, updateDoc, doc } from "firebase/firestore"; 

export default function App() {

 const handleComplete = async (id: string, completed: boolean): Promise<void> => {
    await updateDoc(doc(db, `users/${userId}/tasks/${id}`), {
        completed: !completed
    })}
    
  return (
    <div style={{
        marginTop: '10px'}}>
        {   
          tasks.length > 0 && (
             tasks.map(task => {
             const { id, title, completed } = task;
             return (               
               <div id={id} style={{
                  display:'flex',
                  justifyContent: 'space-between',
                  marginTop: '10px'
               }}>
               <label style={{               
               }}>
               <input type="checkbox"
                 checked={completed}
                 onChange={() => handleComplete(id, completed)}/>   // inclure un gestionnaire onChange 
                 {
                  completed ? 
                  <s className='completed'>{title}</s> 
                  : <span>{title}</span>
                }          
               </label>
               <button>Supprimer</button>
               </div>
             )}))}
        </div>
    )
}
```

Dans ce code, nous avons défini une fonction appelée `handleComplete` qui prend l'`id` et le statut `completed` d'une tâche. Cette fonction est asynchrone et retourne une promesse, mais comme elle ne retourne rien explicitement, la promesse se résout en void. C'est pourquoi nous avons `Promise<void>` comme type de retour. 

Dans la fonction, nous avons utilisé la fonction `updateDoc` de Firebase pour mettre à jour le statut `completed` d'une tâche dans Firestore. Nous avons ensuite passé la référence du document à `updateDoc` en appelant la fonction `doc` avec l'objet `db` et le chemin vers le document de la tâche dans Firestore.

Maintenant, lorsque la case à cocher est cliquée, les utilisateurs peuvent mettre à jour l'état de la tâche - qu'elle soit complétée ou non :
![Marquer une tâche comme complétée](https://www.freecodecamp.org/news/content/images/2023/04/Mark-to-do.gif)

## Comment supprimer les tâches de la liste

Comme vous le verrez ci-dessous, nous allons utiliser la fonction `deleteDoc` de Firebase pour supprimer une tâche de la base de données. Mettez à jour votre fichier `App.tsx` avec le fragment de code suivant : 

```tsx!
import { collection, addDoc, onSnapshot, updateDoc, doc, 
deleteDoc} from "firebase/firestore";

export default function App() {

const handleDelete = async (id: string): Promise<void> => {
      await deleteDoc(doc(db, `users/${userId}/tasks/${id}`));
   }
  return (
    <div style={{
        marginTop: '10px'}}>
        {   
          tasks.length > 0 && (
             tasks.map(task => {
             const { id, title, completed } = task;
             return (               
               <div id={id} style={{
                  display:'flex',
                  justifyContent: 'space-between',
                  marginTop: '10px'
               }}>
               <label style={{               
               }}>
               <input type="checkbox"
                 checked={completed}
                 onChange={() => handleComplete(id, completed)}/>
                 {
                  completed ? 
                  <s className='completed'>{title}</s> 
                  : <span>{title}</span>
                }          
               </label>
               <button
               onClick={() => handleDelete(id)}>
               Supprimer</button>
               </div>
             )}))}
        </div>
        //reste de votre structure
    )
}
```

Nous avons implémenté une fonction appelée `handleDelete` qui prend un `id` de type `string`. Dans la fonction, nous appelons la fonction `deleteDoc` et passons un objet `doc` qui référence la tâche spécifique que nous voulons supprimer. 

Après cela, l'élément `button` appelle la fonction `handleDelete` avec l'`id` de la tâche que nous voulons supprimer lorsqu'il est cliqué.

Voici à quoi devrait ressembler cette fonctionnalité :
![supprimer une tâche](https://www.freecodecamp.org/news/content/images/2023/04/delete-todo.gif)

Maintenant que vous comprenez cette fonctionnalité, passons au filtrage de nos données de base de données selon que l'utilisateur souhaite recevoir toutes les données, actives ou complétées.

## Comment filtrer par toutes, actives ou complétées tâches

Pour implémenter la fonctionnalité de filtre, incluez le code suivant dans votre `App.tsx` :

```tsx!

import { collection, addDoc, onSnapshot, updateDoc, doc, deleteDoc, query, where, getDocs } from "firebase/firestore"; //importer query, where, getDocs

export default function App() {

const handleFilter = async (val: boolean): Promise<void> => {
    const q = query(docRef, where("completed", "==", val)) //obtenir la collection en fonction de si completed est vrai ou non
    const querySnapshot = await getDocs(q)
     const tasks = querySnapshot.docs.map((doc) => {
        const data = doc.data();
        return {  //retourner des données compatibles avec les types de données spécifiés dans la variable tasks 
            title: data.title,
            completed: data.completed,
            id: doc.id,
              }
           }); 
     setTasks(tasks);
          }

    const handleFetchAll = async (): Promise<void> => {    
        const querySnapshot = await getDocs(docRef);
        const tasks = querySnapshot.docs.map((doc) => {
          const data = doc.data();
          return {  //retourner des données compatibles avec les types de données spécifiés dans la variable tasks 
              title: data.title,
              completed: data.completed,
              id: doc.id,
                }
             }); 
            setTasks(tasks); 
          }

  return (

      {/* pied de page */}

   
       <footer style={{
        marginTop: '10px'
        }}>  
         <div style={{
          display: 'flex',
          justifyContent:'space-between'
          }}>
          <button onClick={handleFetchAll}>Toutes</button>  
          <button onClick={() => handleFilter(false) }>Actives</button>  
          <button onClick={() => handleFilter(true)}>Complétées</button>  
         </div>
         
         <div style={{
          display: 'flex',
          justifyContent:'space-between',
          marginTop: '10px'
          }}>
         <p>0 éléments restants</p>
         <button onClick={handleClearCompleted}>
          Effacer les complétées
          </button>  
          </div>
      </footer>

    </div>
     </div>
  )}

```

Tout d'abord, nous importons quelques fonctions supplémentaires de la bibliothèque `firestore` : `query`, `where` et `getDocs`.

Nous avons ensuite défini deux fonctions : `handleFilter` et `handleFetchAll`, que nous utilisons pour filtrer et récupérer les tâches, respectivement, en fonction de leur statut de complétion.

La fonction `handleFilter` reçoit une valeur `boolean` `val` qui représente le statut de complétion de la tâche que nous voulons filtrer. 

Nous créons une nouvelle requête en utilisant la fonction [`query`](https://firebase.google.com/docs/firestore/query-data/queries), en passant `docRef` (qui représente la référence de la collection) et `where` pour spécifier les critères de filtre. Ici, nous recherchons des tâches où le champ completed est égal à la valeur de `val`.

Nous utilisons ensuite `getDocs` pour exécuter la requête et obtenir un objet `querySnapshot`. Nous parcourons le tableau `docs` dans `querySnapshot`, extrayons les champs de données dont nous avons besoin (`title`, `completed` et `id`) et retournons un `object` avec ces propriétés. Après cela, nous mettons à jour l'état `tasks` avec les résultats filtrés.

Dans `handleFetchAll`, nous utilisons également `getDocs` pour obtenir tous les documents dans la collection `docRef`. Nous parcourons le tableau docs dans `querySnapshot`, extrayons les champs de données dont nous avons besoin (`title`, `completed` et `id`) et retournons un `object` avec ces propriétés. Ensuite, nous mettons à jour l'état `tasks` avec les résultats récupérés.

Selon la fonctionnalité, nous passons ensuite les fonctions aux balises `p` correspondantes dans l'élément `footer`.

Voir la démonstration ci-dessous :
![Illustration du filtre de tâches](https://www.freecodecamp.org/news/content/images/2023/04/Filter-todo-1.gif)


## Comment effacer toutes les tâches complétées

Les utilisateurs doivent être autorisés à supprimer toute tâche terminée de leur liste de tâches. Cette fonctionnalité est implémentée en parcourant la liste des tâches et en supprimant toute tâche dont le statut de complétion est défini sur vrai avec la fonction `deleteDoc`. Incluez le code ci-dessous pour voir une illustration concrète :

```tsx!
// imports

export default function App() {

   const handleClearCompleted = async ():Promise<void> => {
     const q = await getDocs(query(docRef, where("completed", "==", true))); //obtenir le document afin que nous puissions le parcourir
       q.forEach( async (doc) => { //parcourir
          await deleteDoc(doc.ref);
          })
      }
    return (
       //pied de page
    
       <footer style={{
        marginTop: '10px'
        }}>  
         <div style={{
          display: 'flex',
          justifyContent:'space-between'
          }}>
          <button onClick={handleFetchAll}>Toutes</button>  
          <button onClick={() => handleFilter(false) }>Actives</button>  
          <button onClick={() => handleFilter(true)}>Complétées</button>  
         </div>
         
         <div style={{
          display: 'flex',
          justifyContent:'space-between',
          marginTop: '10px'
          }}>
         <p>0 éléments restants</p>
         <button onClick={handleClearCompleted}>
          Effacer les complétées
          </button>  
          </div>
      </footer>
    )
}

```

Nous avons utilisé la méthode `getDocs` pour récupérer tous les `documents` de la base de données qui ont un champ completed égal à `true`. Nous faisons cela en passant `where` comme paramètre à la méthode query. Le `where` spécifie que nous voulons uniquement les documents où le champ completed est égal à `true`. 

Nous utilisons ensuite la méthode `forEach` pour parcourir tous les `documents` qui ont été retournés par la `query` et supprimer chacun d'eux.

Enfin, la fonction `handleClearCompleted` est appelée lorsque le bouton "Effacer les complétées" est cliqué dans le `footer`.

La fonctionnalité d'effacement des tâches complétées fonctionne maintenant comme montré ci-dessous :
![Illustration de l'effacement des tâches](https://www.freecodecamp.org/news/content/images/2023/04/Clear-todo.gif)

## Comment afficher le nombre de tâches non complétées 

Dans la dernière étape du développement de notre application, nous allons ajouter une fonctionnalité pour afficher le nombre en temps réel de tâches non complétées lorsque l'utilisateur crée ou supprime des données de la base de données. 

Pour implémenter cela, nous allons utiliser les hooks `useState` et `useEffect` pour gérer l'état du compteur et récupérer les données, respectivement, chaque fois que `docRef` change. 

Pour y parvenir, nous allons également utiliser les méthodes `onSnapshot`, `query` et `where` de notre bibliothèque Firestore. Vous pouvez voir une illustration ci-dessous :

```tsx!
 export default function App() {
 
  const [ completedTasksCount, setCompletedTasksCount ] = useState(0);
 
   useEffect(() => {
         const unsubscribe = onSnapshot(query(docRef, where('completed', '==', false)), (q) => {
           setCompletedTasksCount(q.docs.length);
         });
         return unsubscribe;
   }, [docRef]);
   
  return (
    //pied de page    
       <footer style={{
        marginTop: '10px'
        }}>  
         <div style={{
          display: 'flex',
          justifyContent:'space-between'
          }}>
          <button onClick={handleFetchAll}>Toutes</button>  
          <button onClick={() => handleFilter(false) }>Actives</button>  
          <button onClick={() => handleFilter(true)}>Complétées</button>  
         </div>
         
         <div style={{
          display: 'flex',
          justifyContent:'space-between',
          marginTop: '10px'
          }}>
         <p>{completedTasksCount} éléments restants</p>
         <button onClick={handleClearCompleted}>
          Effacer les complétées
          </button>  
          </div>
      </footer>
  )
 }

```
Tout d'abord, nous initialisons la variable d'état `completedTasksCount` avec une valeur par défaut de `0`.

Ensuite, nous utilisons le hook `useEffect` pour configurer un écouteur de snapshot qui écoute les changements dans la collection des tâches complétées. 

Chaque fois qu'il y a un changement dans la `collection`, la fonction de rappel `onSnapshot` est appelée, et nous mettons à jour l'état `completedTasksCount` avec la longueur du tableau `docs` retourné par l'objet `querySnapshot`. Cela signifie que l'état `completedTasksCount` reflétera toujours le nombre actuel de tâches complétées dans la collection.

Enfin, nous avons passé la variable `completedTasksCount` à la balise `p` dans le `footer`. Une démonstration de cette fonctionnalité peut être vue ci-dessous :
![Afficher les tâches](https://www.freecodecamp.org/news/content/images/2023/04/Display-todo.gif)


Et voilà ! Nous avons terminé la construction de notre application Todo. Félicitations !

## Conclusion

Dans cet article, nous avons exploré diverses fonctionnalités de Cloud Firestore dans une application React pour créer une liste de tâches en temps réel. 

Nous avons commencé par configurer React dans un environnement TypeScript, Firebase et l'API Context pour gérer l'état. Nous avons ensuite approfondi la mise en œuvre des opérations CRUD (create, read, update, delete) en utilisant Firestore et des écouteurs en temps réel. Ceux-ci nous ont permis d'ajouter de nouvelles tâches, de les marquer comme complétées et de les supprimer de la liste. 

Nous avons également implémenté une fonctionnalité de filtre, permettant aux utilisateurs de filtrer leurs tâches par toutes, actives ou complétées. Enfin, nous avons exploré comment effacer toutes les tâches complétées de la liste. 

Si vous souhaitez examiner de plus près le code utilisé dans ce tutoriel, vous pouvez consulter le dépôt Github [ici](https://github.com/SiR-PENt/todolist-app-tutorial) et ma solution officielle au défi avec style [ici](https://github.com/SiR-PENt/todo-list-CRUD-app-with-Firebase).

À présent, vous devriez avoir une bonne compréhension de l'intégration de Firebase dans une application React et de la construction d'une liste de tâches en temps réel complète avec celle-ci. 

Avec les connaissances que vous avez acquises, vous pouvez appliquer ces principes pour développer des applications plus complexes avec Firebase et React, en tirant parti de sa vaste gamme de services tels que le stockage cloud et les fonctions cloud. La documentation exhaustive de Firebase en fait un outil puissant pour construire des applications web complexes en un rien de temps. Bon codage !