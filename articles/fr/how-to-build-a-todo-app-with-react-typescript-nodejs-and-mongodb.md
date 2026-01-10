---
title: Comment créer une application Todo avec React, TypeScript, NodeJS et MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-21T23:28:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-todo-app-with-react-typescript-nodejs-and-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/cover-1.png
tags:
- name: MongoDB
  slug: mongodb
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Comment créer une application Todo avec React, TypeScript, NodeJS et MongoDB
seo_desc: 'By Ibrahima Ndaw

  In this tutorial, we will be using TypeScript on both sides (server and client)
  to build a Todo App from scratch with React, NodeJS, Express, and MongoDB.

  So, let''s start by planning the API.


  API with NodeJS, Express, MongoDB and Ty...'
---

Par Ibrahima Ndaw

Dans ce tutoriel, nous utiliserons TypeScript des deux côtés (serveur et client) pour construire une application Todo à partir de zéro avec React, NodeJS, Express et MongoDB.

Commençons donc par planifier l'API.

* [API avec NodeJS, Express, MongoDB et TypeScript](#heading-api-avec-nodejs-express-mongodb-et-typescript)
* [Installation](#heading-installation)
* [Créer un type Todo](#heading-creer-un-type-todo)
* [Créer un modèle Todo](#heading-creer-un-modele-todo)
* [Créer des contrôleurs API](#heading-creer-des-controleurs-api)
* [Obtenir, ajouter, mettre à jour et supprimer des Todos](#heading-obtenir-ajouter-mettre-a-jour-et-supprimer-des-todos)
* [Créer des routes API](#heading-creer-des-routes-api)
* [Créer un serveur](#heading-creer-un-serveur)
* [Côté client avec React et TypeScript](#heading-cote-client-avec-react-et-typescript)
* [Installation](#heading-installation)
* [Créer un type Todo](#heading-creer-un-type-todo)
* [Récupérer des données de l'API](#heading-recuperer-des-donnees-de-l-api)
* [Créer les composants](#heading-creer-les-composants)
* [Formulaire d'ajout de Todo](#heading-formulaire-d-ajout-de-todo)
* [Afficher un Todo](#heading-afficher-un-todo)
* [Récupérer et afficher les données](#heading-recuperer-et-afficher-les-donnees)
* [Ressources](#heading-ressources)

_Commençons._

## API avec NodeJS, Express, MongoDB et TypeScript

### Installation

Si vous êtes nouveau dans ce domaine, vous pouvez commencer par [Un guide pratique de TypeScript](https://www.ibrahima-ndaw.com/blog/a-practical-guide-to-typescript/) ou [Comment construire une API à partir de zéro avec Node JS, Express et MongoDB](https://www.ibrahima-ndaw.com/blog/graphql-api-express-mongodb/) pour tirer le meilleur parti de ce tutoriel. Sinon, commençons.

Pour créer une nouvelle application NodeJS, vous devez exécuter cette commande dans le terminal :

```shell
  yarn init

```

Il vous posera quelques questions puis initialisera l'application. Vous pouvez sauter cette étape en ajoutant le drapeau `-y` à la commande.

Ensuite, structurez le projet comme suit :

```
├── dist
├── node_modules
├── src
   ├── app.ts
   ├── controllers
   |  └── todos
   |     └── index.ts
   ├── models
   |  └── todo.ts
   ├── routes
   |  └── index.ts
   └── types
      └── todo.ts
├── nodemon.json
├── package.json
├── tsconfig.json

```

Comme vous pouvez le voir, cette structure de fichiers est relativement simple. Le répertoire `dist` servira de dossier de sortie une fois le code compilé en JavaScript simple.

Nous avons également un fichier `app.ts` qui est le point d'entrée du serveur. Les contrôleurs, types et routes sont également dans leurs dossiers respectifs.

Maintenant, nous devons configurer le fichier `tsconfig.json` pour aider le compilateur selon nos préférences.

* tsconfig.json

```js
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "outDir": "dist/js",
    "rootDir": "src",
    "strict": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["src/types/*.ts", "node_modules", ".vscode"]
}

```

Ici, nous avons quatre propriétés principales à souligner :

`outDir` : indique au compilateur de mettre le code compilé dans le dossier `dist/js`.

`rootDir` : informe TypeScript de compiler chaque fichier `.ts` situé dans le dossier `src`.

`include` : indique au compilateur d'inclure les fichiers qui sont dans le répertoire `src` et sous-répertoire.

`exclude` : exclura les fichiers ou dossiers passés dans le tableau pendant la compilation.

Nous pouvons maintenant installer les dépendances pour activer TypeScript dans le projet. Car par défaut, cette application utilisera JavaScript.

Il existe deux façons d'utiliser TypeScript dans une application NodeJS. Soit localement dans le projet, soit globalement dans notre machine. Je vais opter pour cette dernière méthode par préférence personnelle, mais vous pouvez rester avec la méthode locale si vous le souhaitez.

Maintenant, exécutons la commande suivante dans le terminal pour installer TypeScript.

```shell
  yarn add typescript -g

```

Ce drapeau `g` permet d'installer TypeScript globalement et cela le rend accessible depuis n'importe quel endroit sur l'ordinateur.

Ensuite, ajoutons quelques dépendances afin d'utiliser Express et MongoDB.

```shell
  yarn add express cors mongoose

```

Nous devons également installer leurs types en tant que dépendances de développement pour aider le compilateur TypeScript à comprendre les packages.

```shell
  yarn add -D @types/node @types/express @types/mongoose @types/cors

```

Maintenant, TypeScript ne vous criera plus dessus - il utilisera ces types pour définir les bibliothèques que nous venons d'installer.

Nous devons également ajouter d'autres dépendances pour pouvoir compiler le code TypeScript et démarrer le serveur simultanément.

```shell
  yarn add -D concurrently nodemon

```

Avec cela en place, nous pouvons maintenant mettre à jour le fichier `package.json` avec les scripts nécessaires pour démarrer le serveur.

* package.json

```js
  "scripts": {
    "build": "tsc",
    "start": "concurrently \"tsc -w\" \"nodemon dist/js/app.js\""
  }

```

`concurrently` aidera à compiler le code TypeScript, à surveiller les changements et à démarrer le serveur simultanément. Cela dit, nous pouvons maintenant lancer le serveur - cependant, nous n'avons pas encore créé quelque chose de significatif à cet égard. Alors, corrigeons cela dans la section suivante.

### Créer un type Todo

* types/todo.ts

```ts
import { Document } from "mongoose"

export interface ITodo extends Document {
  name: string
  description: string
  status: boolean
}

```

Ici, nous avons une interface Todo qui étend le type `Document` fourni par `mongoose`. Nous l'utiliserons plus tard pour interagir avec MongoDB. Cela dit, nous pouvons maintenant définir à quoi doit ressembler un modèle Todo.

### Créer un modèle Todo

* models/todo.ts

```ts
import { ITodo } from "./../types/todo"
import { model, Schema } from "mongoose"

const todoSchema: Schema = new Schema(
  {
    name: {
      type: String,
      required: true,
    },

    description: {
      type: String,
      required: true,
    },

    status: {
      type: Boolean,
      required: true,
    },
  },
  { timestamps: true }
)

export default model<ITodo>("Todo", todoSchema)

```

Comme vous pouvez le voir ici, nous commençons par importer l'interface `ITodo` et quelques utilitaires de `mongoose`. Ces derniers aident à définir le schéma Todo et à passer `ITodo` comme type au `model` avant de l'exporter.

Avec cela, nous pouvons maintenant utiliser le modèle Todo dans d'autres fichiers pour interagir avec la base de données.

### Créer des contrôleurs API

#### Obtenir, ajouter, mettre à jour et supprimer des Todos

* controllers/todos/index.ts

```ts
import { Response, Request } from "express"
import { ITodo } from "./../../types/todo"
import Todo from "../../models/todo"

const getTodos = async (req: Request, res: Response): Promise<void> => {
  try {
    const todos: ITodo[] = await Todo.find()
    res.status(200).json({ todos })
  } catch (error) {
    throw error
  }
}

```

Ici, nous devons d'abord importer certains types de `express` car je veux typer les valeurs explicitement. Si vous le souhaitez, vous pouvez laisser TypeScript les inférer pour vous.

Ensuite, nous utilisons la fonction `getTodos()` pour récupérer les données. Elle reçoit un paramètre `req` et `res` et retourne une promesse.

Et avec l'aide du modèle `Todo` créé précédemment, nous pouvons maintenant obtenir les données de MongoDB et retourner une réponse avec le tableau des todos.

* controllers/todos/index.ts

```ts
const addTodo = async (req: Request, res: Response): Promise<void> => {
  try {
    const body = req.body as Pick<ITodo, "name" | "description" | "status">

    const todo: ITodo = new Todo({
      name: body.name,
      description: body.description,
      status: body.status,
    })

    const newTodo: ITodo = await todo.save()
    const allTodos: ITodo[] = await Todo.find()

    res
      .status(201)
      .json({ message: "Todo ajouté", todo: newTodo, todos: allTodos })
  } catch (error) {
    throw error
  }
}

```

Comme vous pouvez le voir, la fonction `addTodo()` reçoit l'objet body qui contient les données saisies par l'utilisateur.

Ensuite, j'utilise le transtypage pour éviter les fautes de frappe et restreindre la variable `body` pour qu'elle corresponde à `ITodo`, puis je crée un nouveau Todo basé sur le modèle.

Avec cela en place, nous pouvons maintenant sauvegarder le Todo dans la base de données et retourner une réponse qui contient le todo créé et le tableau des todos mis à jour.

* controllers/todos/index.ts

```ts
const updateTodo = async (req: Request, res: Response): Promise<void> => {
  try {
    const {
      params: { id },
      body,
    } = req
    const updateTodo: ITodo | null = await Todo.findByIdAndUpdate(
      { _id: id },
      body
    )
    const allTodos: ITodo[] = await Todo.find()
    res.status(200).json({
      message: "Todo mis à jour",
      todo: updateTodo,
      todos: allTodos,
    })
  } catch (error) {
    throw error
  }
}

```

Pour mettre à jour un todo, nous devons extraire l'id et le body de l'objet `req`, puis les passer à `findByIdAndUpdate()`. Cet utilitaire trouvera le Todo dans la base de données et le mettra à jour. Et une fois l'opération terminée, nous pouvons maintenant retourner les données mises à jour à l'utilisateur.

* controllers/todos/index.ts

```ts
const deleteTodo = async (req: Request, res: Response): Promise<void> => {
  try {
    const deletedTodo: ITodo | null = await Todo.findByIdAndRemove(
      req.params.id
    )
    const allTodos: ITodo[] = await Todo.find()
    res.status(200).json({
      message: "Todo supprimé",
      todo: deletedTodo,
      todos: allTodos,
    })
  } catch (error) {
    throw error
  }
}

export { getTodos, addTodo, updateTodo, deleteTodo }

```

La fonction `deleteTodo()` vous permet de supprimer un Todo de la base de données. Ici, nous extrayons l'id de req et le passons comme argument à `findByIdAndRemove()` pour accéder au Todo correspondant et le supprimer de la base de données.

Ensuite, nous exportons les fonctions pour pouvoir les utiliser dans d'autres fichiers. Cela dit, nous pouvons maintenant créer quelques routes pour l'API et utiliser ces méthodes pour gérer les requêtes.

### Créer des routes API

* routes/index.ts

```ts
import { Router } from "express"
import { getTodos, addTodo, updateTodo, deleteTodo } from "../controllers/todos"

const router: Router = Router()

router.get("/todos", getTodos)

router.post("/add-todo", addTodo)

router.put("/edit-todo/:id", updateTodo)

router.delete("/delete-todo/:id", deleteTodo)

export default router

```

Comme vous pouvez le voir ici, nous avons quatre routes pour obtenir, ajouter, mettre à jour et supprimer des todos de la base de données. Et puisque nous avons déjà créé les fonctions, la seule chose que nous devons faire est d'importer les méthodes et de les passer comme paramètres pour gérer les requêtes.

Jusqu'à présent, nous avons couvert beaucoup de choses. Mais nous n'avons toujours pas de serveur à démarrer. Alors, corrigeons cela dans la section suivante.

### Créer un serveur

Avant de créer le serveur, nous devons d'abord ajouter quelques variables d'environnement qui contiendront les informations d'identification de MongoDB dans le fichier `nodemon.json`.

* nodemon.json

```js
{
    "env": {
        "MONGO_USER": "votre-nom-d-utilisateur",
        "MONGO_PASSWORD": "votre-mot-de-passe",
        "MONGO_DB": "votre-nom-de-bd"
    }
}

```

Vous pouvez obtenir les informations d'identification en créant un nouveau cluster sur [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

* app.ts

```ts
import express, { Express } from "express"
import mongoose from "mongoose"
import cors from "cors"
import todoRoutes from "./routes"

const app: Express = express()

const PORT: string | number = process.env.PORT || 4000

app.use(cors())
app.use(todoRoutes)

const uri: string = `mongodb+srv://${process.env.MONGO_USER}:${process.env.MONGO_PASSWORD}@clustertodo.raz9g.mongodb.net/${process.env.MONGO_DB}?retryWrites=true&w=majority`
const options = { useNewUrlParser: true, useUnifiedTopology: true }
mongoose.set("useFindAndModify", false)

mongoose
  .connect(uri, options)
  .then(() =>
    app.listen(PORT, () =>
      console.log(`Serveur en cours d'exécution sur http://localhost:${PORT}`)
    )
  )
  .catch(error => {
    throw error
  })

```

Ici, nous commençons par importer la bibliothèque `express` qui nous permet d'accéder à la méthode `use()` qui aide à gérer les routes des Todos.

Ensuite, nous utilisons le package `mongoose` pour nous connecter à MongoDB en ajoutant à l'URL les informations d'identification contenues dans le fichier `nodemon.json`.

Cela dit, maintenant si nous nous connectons avec succès à MongoDB, le serveur démarrera. Si approprié, une erreur sera lancée.

Nous avons maintenant terminé la construction de l'API avec Node, Express, TypeScript et MongoDB. Commençons maintenant à construire l'application côté client avec React et TypeScript.

![excité](https://media.giphy.com/media/Is1O1TWV0LEJi/giphy.gif)

## Côté client avec React et TypeScript

### Installation

Pour créer une nouvelle application React, je vais utiliser create-react-app - vous pouvez utiliser d'autres méthodes si vous le souhaitez.

Alors, exécutons dans le terminal la commande suivante :

```shell
  npx create-react-app my-app --template typescript

```

Ensuite, installez la bibliothèque Axios pour pouvoir récupérer des données distantes.

```shell
  yarn add axios

```

Une fois l'installation terminée, structurons notre projet comme suit :

```
├── node_modules
├── public
├── src
|  ├── API.ts
|  ├── App.test.tsx
|  ├── App.tsx
|  ├── components
|  |  ├── AddTodo.tsx
|  |  └── TodoItem.tsx
|  ├── index.css
|  ├── index.tsx
|  ├── react-app-env.d.ts
|  ├── setupTests.ts
|  └── type.d.ts
├── tsconfig.json
├── package.json
└── yarn.lock

```

Ici, nous avons une structure de fichiers relativement simple. La chose principale à noter est que `src/type.d.ts` contiendra les types. Et puisque je vais les utiliser dans presque tous les fichiers, j'ai ajouté l'extension `.d.ts` pour rendre les types disponibles globalement. Et maintenant, nous n'avons plus besoin de les importer.

### Créer un type Todo

* src/type.d.ts

```ts
interface ITodo {
  _id: string
  name: string
  description: string
  status: boolean
  createdAt?: string
  updatedAt?: string
}

interface TodoProps {
  todo: ITodo
}

type ApiDataType = {
  message: string
  status: string
  todos: ITodo[]
  todo?: ITodo
}

```

Ici, l'interface `ITodo` doit refléter la forme des données de l'API. Et puisque nous n'avons pas `mongoose` ici, nous devons ajouter des propriétés supplémentaires pour correspondre au type défini sur l'API.

Ensuite, nous utilisons cette même interface pour `TodoProps` qui est l'annotation de type pour les props qui seront reçues par le composant responsable du rendu des données.

Nous avons maintenant défini nos types - commençons maintenant à récupérer les données de l'API.

### Récupérer des données de l'API

* src/API.ts

```ts
import axios, { AxiosResponse } from "axios"

const baseUrl: string = "http://localhost:4000"

export const getTodos = async (): Promise<AxiosResponse<ApiDataType>> => {
  try {
    const todos: AxiosResponse<ApiDataType> = await axios.get(
      baseUrl + "/todos"
    )
    return todos
  } catch (error) {
    throw new Error(error)
  }
}

```

Comme vous pouvez le voir, nous devons importer `axios` pour demander des données à l'API. Ensuite, nous utilisons la fonction `getTodos()` pour obtenir les données du serveur. Elle retournera une promesse de type `AxiosResponse` qui contient les Todos récupérés qui doivent correspondre au type `ApiDataType`.

* src/API.ts

```ts
export const addTodo = async (
  formData: ITodo
): Promise<AxiosResponse<ApiDataType>> => {
  try {
    const todo: Omit<ITodo, "_id"> = {
      name: formData.name,
      description: formData.description,
      status: false,
    }
    const saveTodo: AxiosResponse<ApiDataType> = await axios.post(
      baseUrl + "/add-todo",
      todo
    )
    return saveTodo
  } catch (error) {
    throw new Error(error)
  }
}

```

Cette fonction reçoit les données saisies par l'utilisateur comme argument et retourne une promesse. Ici, nous devons omettre la propriété `_id` car MongoDB la créera à la volée.

* src/API.ts

```ts
export const updateTodo = async (
  todo: ITodo
): Promise<AxiosResponse<ApiDataType>> => {
  try {
    const todoUpdate: Pick<ITodo, "status"> = {
      status: true,
    }
    const updatedTodo: AxiosResponse<ApiDataType> = await axios.put(
      `${baseUrl}/edit-todo/${todo._id}`,
      todoUpdate
    )
    return updatedTodo
  } catch (error) {
    throw new Error(error)
  }
}

```

Pour mettre à jour un Todo, nous devons passer les données mises à jour et l'`_id` de l'objet. Ici, nous devons changer le `status` du Todo, c'est pourquoi je ne sélectionne que la propriété dont nous avons besoin avant d'envoyer la requête au serveur.

* src/API.ts

```ts
export const deleteTodo = async (
  _id: string
): Promise<AxiosResponse<ApiDataType>> => {
  try {
    const deletedTodo: AxiosResponse<ApiDataType> = await axios.delete(
      `${baseUrl}/delete-todo/${_id}`
    )
    return deletedTodo
  } catch (error) {
    throw new Error(error)
  }
}

```

Ici, nous avons également une fonction qui reçoit en paramètre la propriété `_id` et retourne une promesse.

Avec cela en place, nous pouvons maintenant aller dans le dossier `components` et ajouter un code significatif à ses fichiers.

### Créer les composants

#### Formulaire d'ajout de Todo

* components/AddTodo.tsx

```js
import React from "react"

type Props = TodoProps & {
  updateTodo: (todo: ITodo) => void
  deleteTodo: (_id: string) => void
}

const Todo: React.FC<Props> = ({ todo, updateTodo, deleteTodo }) => {
  const checkTodo: string = todo.status ? `line-through` : ""
  return (
    <div className="Card">
      <div className="Card--text">
        <h1 className={checkTodo}>{todo.name}</h1>
        <span className={checkTodo}>{todo.description}</span>
      </div>
      <div className="Card--button">
        <button
          onClick={() => updateTodo(todo)}
          className={todo.status ? `hide-button` : "Card--button__done"}
        >
          Terminer
        </button>
        <button
          onClick={() => deleteTodo(todo._id)}
          className="Card--button__delete"
        >
          Supprimer
        </button>
      </div>
    </div>
  )
}

export default Todo

```

Comme vous pouvez le voir, ici nous avons un composant fonctionnel de type `React.FC` (FC signifie composant fonctionnel). Il reçoit en prop la méthode `saveTodo()` qui nous permet de sauvegarder les données dans la base de données.

Ensuite, nous avons un état `formData` qui doit correspondre au type `ITodo` pour satisfaire le compilateur. C'est pourquoi nous le passons au hook `useState`. Nous devons également ajouter un type alternatif (`{}`) car l'état initial sera un objet vide.

Et avec cela, nous pouvons maintenant avancer et afficher les données récupérées.

### **Afficher un Todo**

* components/TodoItem.tsx

```jsx
import React from "react"

type Props = TodoProps & {
  updateTodo: (todo: ITodo) => void
  deleteTodo: (_id: string) => void
}

const Todo: React.FC<Props> = ({ todo, updateTodo, deleteTodo }) => {
  const checkTodo: string = todo.status ? `line-through` : ""
  return (
    <div className="Card">
      <div className="Card--text">
        <h1 className={checkTodo}>{todo.name}</h1>
        <span className={checkTodo}>{todo.description}</span>
      </div>
      <div className="Card--button">
        <button
          onClick={() => updateTodo(todo)}
          className={todo.status ? `hide-button` : "Card--button__done"}
        >
          Terminer
        </button>
        <button
          onClick={() => deleteTodo(todo._id)}
          className="Card--button__delete"
        >
          Supprimer
        </button>
      </div>
    </div>
  )
}

export default Todo

```

Ici, nous devons étendre le type `TodoProps` et ajouter les fonctions `updateTodo` et `deleteTodo` pour gérer correctement les props reçues par le composant.

Maintenant, une fois l'objet Todo passé, nous pourrons l'afficher et ajouter les fonctions nécessaires pour mettre à jour ou supprimer un Todo.

Super ! Nous pouvons maintenant aller dans le fichier `App.tsx` et ajouter la dernière pièce du puzzle.

### Récupérer et afficher les données

* App.tsx

```jsx
import React, { useEffect, useState } from 'react'
import TodoItem from './components/TodoItem'
import AddTodo from './components/AddTodo'
import { getTodos, addTodo, updateTodo, deleteTodo } from './API'

const App: React.FC = () => {
  const [todos, setTodos] = useState<ITodo[]>([])

  useEffect(() => {
    fetchTodos()
  }, [])

  const fetchTodos = (): void => {
    getTodos()
    .then(({ data: { todos } }: ITodo[] | any) => setTodos(todos))
    .catch((err: Error) => console.log(err))
  }

```

Ici, nous devons d'abord importer les composants et les fonctions utilitaires contenues dans `API.ts`. Ensuite, nous passons à `useState` un tableau de type `ITodo` et l'initialisons avec un tableau vide.

La méthode `getTodos()` retourne une promesse - par conséquent, nous pouvons accéder à la fonction `then` et mettre à jour l'état avec les données récupérées ou lancer une erreur si elle se produit.

Avec cela en place, nous pouvons maintenant appeler la fonction `fetchTodos()` lorsque le composant est monté avec succès.

* App.tsx

```jsx
const handleSaveTodo = (e: React.FormEvent, formData: ITodo): void => {
  e.preventDefault()
  addTodo(formData)
    .then(({ status, data }) => {
      if (status !== 201) {
        throw new Error("Erreur ! Todo non sauvegardé")
      }
      setTodos(data.todos)
    })
    .catch(err => console.log(err))
}

```

Une fois le formulaire soumis, nous utilisons `addTodo()` pour envoyer la requête au serveur, puis si le Todo a été sauvegardé avec succès, nous mettons à jour les données, sinon une erreur sera lancée.

* App.tsx

```jsx
const handleUpdateTodo = (todo: ITodo): void => {
  updateTodo(todo)
    .then(({ status, data }) => {
      if (status !== 200) {
        throw new Error("Erreur ! Todo non mis à jour")
      }
      setTodos(data.todos)
    })
    .catch(err => console.log(err))
}

const handleDeleteTodo = (_id: string): void => {
  deleteTodo(_id)
    .then(({ status, data }) => {
      if (status !== 200) {
        throw new Error("Erreur ! Todo non supprimé")
      }
      setTodos(data.todos)
    })
    .catch(err => console.log(err))
}

```

Les fonctions pour mettre à jour ou supprimer un Todo sont assez similaires. Elles reçoivent toutes deux un paramètre, envoient la requête et reçoivent une réponse. Ensuite, elles vérifient si la requête a été réussie et la gèrent en conséquence.

* App.tsx

```jsx
  return (
    <main className='App'>
      <h1>Mes Todos</h1>
      <AddTodo saveTodo={handleSaveTodo} />
      {todos.map((todo: ITodo) => (
        <TodoItem
          key={todo._id}
          updateTodo={handleUpdateTodo}
          deleteTodo={handleDeleteTodo}
          todo={todo}
        />
      ))}
    </main>
  )
}

export default App

```

Ici, nous parcourons le tableau `todos` puis passons à `TodoItem` les données attendues.

Maintenant, si vous naviguez dans le dossier qui contient l'application côté serveur (et exécutez la commande suivante dans le terminal) :

```shell
yarn start

```

Et aussi sur l'application côté client :

```shell
yarn start

```

Vous devriez voir que notre application Todo fonctionne comme prévu.

![Image de l'application todo fonctionnelle](https://www.freecodecamp.org/news/content/images/2021/10/todo-image.png)

Super ! Avec cette dernière touche, nous avons maintenant terminé la construction d'une application Todo en utilisant TypeScript, React, NodeJs, Express et MongoDB.

Vous pouvez trouver le [Code Source ici](https://github.com/ibrahima92/fullstack-typescript-mern-todo).

Vous pouvez trouver d'autres excellents contenus comme celui-ci sur [mon blog](https://www.ibrahima-ndaw.com) ou me suivre [sur Twitter](https://twitter.com/ibrahima92_) pour être notifié.

Merci d'avoir lu.

## Ressources

[React TypeScript Cheatsheet](https://github.com/typescript-cheatsheets/react-typescript-cheatsheet)

[Advanced TypeScript Types cheatsheet (with examples)](https://www.ibrahima-ndaw.com/blog/advanced-typescript-cheat-sheet/)

[TypeScript Cheatsheets](https://github.com/typescript-cheatsheets)