---
title: Comment créer une application To-Do avec la stack MERN
subtitle: ''
author: Casmir Onyekani
co_authors: []
series: null
date: '2025-03-04T18:58:44.318Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-mern-stack-to-do-app
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741102112733/3aa43545-c095-4a47-8787-130b470f6ce1.png
tags:
- name: MERN Stack
  slug: mern
- name: MongoDB
  slug: mongodb
- name: todoapp
  slug: todoapp
seo_title: Comment créer une application To-Do avec la stack MERN
seo_desc: This guide will walk you through building a full-stack MERN To-Do application.
  It covers setting up the environment, writing code to demonstrate core CRUD (Create,
  Read, Update, Delete) operations, and connecting the application to MongoDB Atlas,
  a f...
---

Ce guide vous expliquera comment créer une application To-Do full-stack MERN. Il couvre la configuration de l'environnement, l'écriture de code pour démontrer les opérations CRUD (Create, Read, Update, Delete) et la connexion de l'application à MongoDB Atlas, une base de données cloud gratuite.

Avant de plonger dans cet article, je vous recommande d'avoir une compréhension de base de HTML, CSS et JavaScript, ainsi que quelques connaissances des frameworks et bibliothèques frontend et backend.

Mon objectif principal sera la fonctionnalité, vous permettant de personnaliser le design comme vous le souhaitez. Les commandes que j'utiliserai ici sont adaptées pour Windows, donc si vous utilisez Linux, macOS ou Ubuntu, vous devrez peut-être les ajuster en conséquence.

À la fin de ce guide, vous aurez une application To-Do entièrement fonctionnelle en cours d'exécution sur votre système.

## Table des matières

* [Introduction à la stack MERN](#heading-introduction-a-la-stack-mern)
    
* [Comment configurer votre environnement de développement](#heading-comment-configurer-votre-environnement-de-developpement)
    
    * [Installer Node.js et npm - Node Package Manager](#heading-installer-nodejs-et-npm-node-package-manager)
        
* [Comment configurer un nouveau projet MERN](#heading-comment-configurer-un-nouveau-projet-mern)
    
    * [Configuration du Frontend](#heading-configuration-du-frontend)
        
    * [Créer l'interface utilisateur de l'application To-Do](#heading-creer-linterface-utilisateur-de-lapplication-to-do)
        
    * [Afficher vos tâches dans l'interface utilisateur](#heading-afficher-vos-taches-dans-linterface-utilisateur)
        
    * [Donner à votre application un style personnalisé](#heading-donner-a-votre-application-un-style-personnalise)
        
    * [Configuration du Backend](#heading-configuration-du-backend)
        
    * [Configurer MongoDB Atlas](#heading-configurer-mongodb-atlas)
        
    * [Exécuter l'application](#heading-executer-lapplication)
        
* [Conclusion](#heading-conclusion)
    

## Introduction à la stack MERN

La stack MERN est une pile JavaScript populaire pour construire des applications web modernes. Elle se compose de :

* **MongoDB** : Une base de données NoSQL pour stocker des données.
    
* **Express.js** : Un framework backend pour construire des APIs.
    
* **React (bibliothèque UI) + Vite (outil de build) + TypeScript (JavaScript typé)** : Une pile frontend moderne pour construire des interfaces utilisateur scalables et maintenables.
    
* **Node.js** : Un environnement d'exécution pour exécuter JavaScript sur le serveur.
    

## Comment configurer votre environnement de développement

### Installer Node.js et npm (Node Package Manager)

Au lieu d'installer Node.js et npm dans votre dossier de projet, je vous conseille de les installer dans le répertoire racine de votre système afin de pouvoir les utiliser dans n'importe quel projet, pas seulement celui-ci.

Tout d'abord, téléchargez et installez Node.js (qui inclut npm) depuis le [site officiel](https://nodejs.org/en) si vous ne l'avez pas déjà.

Après l'installation, ouvrez votre ligne de commande (j'utilise Git Bash) et vérifiez l'installation en exécutant les commandes suivantes :

```bash
node -v
npm -v
```

Vous devriez voir les versions installées de Node.js et npm si l'installation s'est bien passée.

## Comment configurer un nouveau projet MERN

Créez un dossier de projet et ouvrez votre éditeur de code en exécutant ces commandes :

```bash
mkdir mern-todo-app
cd mern-todo-app
code .
```

La commande `code .` ouvre automatiquement VS Code. Si ce n'est pas le cas, ouvrez VS Code manuellement et naviguez jusqu'à votre dossier `mern-todo-app`.

### Configuration du Frontend

#### Configurer Vite avec React et TypeScript

Assurez-vous d'être dans le répertoire racine de votre projet (`mern-todo-app`), puis exécutez la commande suivante :

```bash
npm create vite@latest frontend --template react-ts
```

Cette commande créera un frontend React basé sur TypeScript dans le dossier `frontend` à l'intérieur de votre répertoire `mern-todo-app`.

#### Installer Axios pour faire des requêtes API

Axios est une bibliothèque JavaScript populaire utilisée pour faire des requêtes HTTP depuis le frontend vers une API backend. Elle simplifie l'envoi de requêtes GET, POST, PUT et DELETE et la gestion des réponses.

Pour installer Axios, exécutez la commande suivante :

```bash
cd frontend
npm install axios
```

### Créer l'interface utilisateur de l'application To-Do

À l'intérieur du dossier `src`, créez un fichier `App.tsx` s'il n'existe pas déjà, et ajoutez le code ci-dessous. C'est beaucoup, mais ne vous inquiétez pas, je vais le décomposer bit par bit ensuite :

`frontend/src/App.tsx`:

```javascript
// BLOCK 1: Importing Dependencies
import React, { useState, useEffect } from "react";
import axios from "axios";
import TodoList from "./components/TodoList.tsx";
import "./App.css";

// BLOCK 2: Defining Task Interface
interface Task {
  _id: string;
  title: string;
  completed: boolean;
}

// BLOCK 3: Setting Up State Variables
const App: React.FC = () => {
  // State for tasks, new task text, and editing controls
  const [tasks, setTasks] = useState<Task[]>([]);
  const [task, setTask] = useState<string>("");
  const [editingTaskId, setEditingTaskId] = useState<string | null>(null);
  const [editingTitle, setEditingTitle] = useState<string>("");

  // BLOCK 4: Fetch tasks from the backend on component mount
  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const response = await axios.get<Task[]>(`http://localhost:5000/api/tasks`);
        console.log("Fetched tasks:", response.data); // Debugging log
        setTasks(response.data);
      } catch (error) {
        console.error("Error fetching tasks:", error);
      }
    };
    fetchTasks();
  }, []);

  // BLOCK 5: Adding a Task
  const addTask = async () => {
    if (!task) return;

    try {
      console.log("Adding task:", task); // Debugging log
      const response = await axios.post<Task>(
        `http://localhost:5000/api/tasks`,
        { title: task },
        { headers: { "Content-Type": "application/json" } }
      );
      console.log("Task added response:", response.data);
      setTasks([...tasks, response.data]);
      setTask("");
    } catch (error) {
      console.error("Error adding task:", error);
    }
  };

  // BLOCK 6: Delete a task
  const deleteTask = async (id: string) => {
    try {
      await axios.delete(`http://localhost:5000/api/tasks/${id}`);
      setTasks(tasks.filter((t) => t._id !== id));
    } catch (error) {
      console.error("Error deleting task:", error);
    }
  };

  // BLOCK 7: Updating a Task
  const updateTask = async (id: string, updatedTask: Partial<Task>) => {
    try {
      const response = await axios.put(
        `http://localhost:5000/api/tasks/${id}`,
        updatedTask,
        { headers: { "Content-Type": "application/json" } }
      );

      setTasks(
        tasks.map((task) =>
          task._id === id ? { ...task, ...response.data } : task
        )
      );
      setEditingTaskId(null);
      setEditingTitle("");
    } catch (error) {
      console.error("Error updating task:", error);
    }
  };

  // BLOCK 8: Handling Edits
  const startEditing = (id: string) => {
    setEditingTaskId(id);
  };

  // Handle title change during editing
  const handleEditChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEditingTitle(e.target.value);
  };

  // BLOCK 9: Render the app
  return (
    <div className="App">
      <h1>Todo App</h1>
      <div>
        <input
          type="text"
          value={task}
          onChange={(e) => setTask(e.target.value)}
        />
        <button onClick={addTask}>Add Task</button>
      </div>
      <TodoList
        tasks={tasks}
        deleteTask={deleteTask}
        updateTask={updateTask}
        editingTitle={editingTitle}
        setEditingTitle={setEditingTitle}
        editingTaskId={editingTaskId}
        setEditingTaskId={setEditingTaskId}
        startEditing={startEditing}
        handleEditChange={handleEditChange}
      />
    </div>
  );
};

// BLOCK 10: Exporting the Component
export default App;
```

Voici une décomposition bloc par bloc du code ci-dessus :

**BLOCK 1 :** Importation des dépendances

* `React, { useState, useEffect }` : Gère l'état du composant et les effets secondaires.
    
* `axios` : Gère les requêtes API.
    
* `TodoList.tsx` : Un composant enfant pour afficher et gérer les tâches.
    
* `App.css` : Style l'application.
    

**BLOCK 2 :** Définition de l'interface de la tâche

* Définit la structure d'une tâche (`_id`, `title`, `completed`).
    

**BLOCK 3 :** Configuration des variables d'état

* `tasks` : Stocke la liste des tâches.
    
* `task` : Contient l'entrée pour les nouvelles tâches.
    
* `editingTaskId` : Suivi de la tâche en cours d'édition.
    
* `editingTitle` : Stocke le titre mis à jour pendant l'édition.
    

**BLOCK 4 :** Récupération des tâches depuis le backend (`useEffect`)

* S'exécute une fois lorsque l'application se charge.
    
* Appelle l'API (`GET /api/tasks`) pour obtenir les tâches et met à jour `tasks`.
    
* Gestion des erreurs : Affiche un message d'erreur si la requête de récupération échoue.
    

**BLOCK 5 :** Ajout d'une tâche

* Envoie une requête `POST` pour ajouter une nouvelle tâche.
    
* Met à jour `tasks` avec la nouvelle tâche.
    
* Gestion des erreurs : Affiche un message d'erreur si la requête d'ajout de tâche échoue.
    

**BLOCK 6 :** Suppression d'une tâche

* Envoie une requête `DELETE` pour supprimer une tâche.
    
* Met à jour `tasks` en filtrant la tâche supprimée.
    
* Gestion des erreurs : Affiche un message d'erreur si la requête de suppression de tâche échoue.
    

**BLOCK 7 :** Mise à jour d'une tâche

* Envoie une requête `PUT` pour mettre à jour le titre d'une tâche.
    
* Met à jour `tasks` avec le nouveau titre.
    
* Gestion des erreurs : Affiche un message d'erreur si la requête de mise à jour échoue.
    

**BLOCK 8 :** Gestion des éditions

* `startEditing(id)` : Met une tâche en mode édition.
    
* `handleEditChange(e)` : Met à jour l'entrée d'édition.
    

**BLOCK 9 :** Rendu de l'interface utilisateur

* Affiche un champ de saisie et un bouton pour ajouter des tâches.
    
* Passe les données des tâches et les fonctions (`deleteTask`, `updateTask`, etc.) à `TodoList.tsx`.
    

**BLOCK 10 :** Exportation du composant

* `export default App;` : Rend `App` utilisable dans d'autres fichiers.
    

### Afficher vos tâches dans l'interface utilisateur

À l'intérieur du dossier `src`, créez un nouveau dossier nommé `components`. Ensuite, ajoutez un fichier `TodoList.tsx` à l'intérieur avec le code ci-dessous.

`src/components/TodoList.tsx`:

```javascript
// BLOCK 1: Importing Dependencies
import React from "react";

// BLOCK 2: Defining Interfaces
interface Task {
  _id: string; // Unique ID for the task
  title: string; // Task name
  completed: boolean; // True if done, False if not
}

interface TodoListProps {
  tasks: Task[];
  deleteTask: (id: string) => void;
  updateTask: (id: string, updatedTask: Partial<Task>) => void;
  editingTitle: string;
  setEditingTitle: (title: string) => void;
  editingTaskId: string | null;
  setEditingTaskId: (id: string | null) => void;
  startEditing: (id: string) => void;
  handleEditChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

// BLOCK 3: Declares the TodoList Component
const TodoList: React.FC<TodoListProps> = ({
  tasks,
  deleteTask,
  updateTask,
  editingTitle,
  setEditingTitle,
  editingTaskId,
  setEditingTaskId,
  startEditing,
  handleEditChange,
}) => {

  // BLOCK 4: Rendering the Task List and handling task actions
  return (
    <ul>
      {tasks.map((task) => (
        <li key={task._id}>
          <input
            type="checkbox"
            checked={task.completed}
            onChange={() => updateTask(task._id, { completed: !task.completed })}
          />
          {editingTaskId === task._id ? (
            <>
              <input type="text" value={editingTitle} onChange={handleEditChange} />
              <button
                onClick={() => {
                  updateTask(task._id, { title: editingTitle });
                  setEditingTaskId(null);
                }}
              >
                Save
              </button>
            </>
          ) : (
            <>
              <span style={{ textDecoration: task.completed ? "line-through" : "none" }}>
                {task.title}
              </span>
              
              <div>
                <button onClick={() => deleteTask(task._id)}>Delete</button>
                <button
                  onClick={() => {
                    startEditing(task._id);
                    setEditingTitle(task.title);
                  }}
                >
                  Edit
                </button>
              </div>
            </>
          )}
        </li>
      ))}
    </ul>
  );
};

// BLOCK 5: Exporting the Component
export default TodoList;
```

Voici une décomposition bloc par bloc du code ci-dessus :

**BLOCK 1 :** Importation des dépendances

* React : Permet la création de composants fonctionnels.
    

**BLOCK 2 :** Définition des interfaces

* Interface Task : Définit les propriétés `_id`, `title` et `completed`.
    
* Interface TodoListProps : Définit les props passées au composant `TodoList`.
    

**BLOCK 3 :** Déclaration du composant `TodoList`

* Définit un composant fonctionnel React (`TodoList`) en utilisant TypeScript (`React.FC<TodoListProps>`).
    
* Extrait les props listées de `TodoListProps` et prépare le composant pour le rendu.
    

**BLOCK 4 :** Rendu de la liste des tâches et gestion des actions sur les tâches

* Parcourt `tasks` pour afficher chaque tâche à l'intérieur d'un `<ul>`.
    
* La case à cocher bascule le statut `completed` en utilisant `updateTask()`.
    
* Rendu conditionnel :
    
    * Si une tâche est en cours d'édition, un champ de saisie apparaît pour l'édition.
        
    * Sinon, le titre de la tâche est affiché avec un barré si elle est terminée.
        
* Bouton Save : Met à jour le titre de la tâche en utilisant `updateTask()`, puis quitte le mode édition.
    
* Bouton Delete : Appelle `deleteTask()` pour supprimer une tâche.
    
* Bouton Edit : Active le mode édition, définissant `editingTaskId` et `editingTitle`.
    

**BLOCK 5 :** Exportation du composant

* Rend `TodoList` disponible pour une utilisation dans d'autres composants.
    

### Donner à votre application un style personnalisé

À l'intérieur de votre dossier `src`, créez `App.css` s'il n'existe pas et remplacez le contenu par le style souhaité. Donnons une touche finale au frontend.

`src/App.css`:

```css
/* Center the app in the middle of the screen */
html, body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f4f4f4; /* Light gray background */
  width: 100%;
  overflow-x: hidden; /* Prevent horizontal scrolling */
}

/* Style the main app container */
.App {
  text-align: center;
  background: white;
  padding: 20px;
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Light shadow effect */
  width: 90%; /* Make it flexible */
  max-width: 350px; /* Prevent exceeding max size */
  box-sizing: border-box;
}

/* Add spacing below the title */
h1 {
  margin-bottom: 20px;
  font-size: 24px;
  color: #333;
}

/* Style input fields */
input {
  width: 100%; /* Full width */
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  box-sizing: border-box;
}

/* Style buttons */
button {
  width: 100%; /* Make buttons full width */
  padding: 10px;
  margin-top: 5px;
  border: none;
  background-color: #007bff; /* Blue background */
  color: white;
  cursor: pointer;
  border-radius: 5px;
  font-size: 14px;
  transition: background-color 0.3s ease-in-out;
}

/* Change button color when hovered */
button:hover {
  background-color: #0056b3;
}

/* Remove default list styles */
ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

/* Style list items */
li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fff;
  padding: 10px;
  margin: 5px 0;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
  width: 100%;
  box-sizing: border-box;
}

/* Allow task text to take available space */
span {
  flex: 1;
  font-size: 16px;
  color: #333;
}

/* Style completed tasks */
span.completed {
  text-decoration: line-through;
  color: #888;
}

/* Adjust the width of input fields inside the list */
input[type="text"] {
  width: 70%;
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

/* Style the checkbox */
input[type="checkbox"] {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: #007bff; /* Blue checkbox to match buttons */
  margin-right: 10px;
}

/* Styling for editing mode */
.editing-container {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
}

/* Responsive styling for smaller screens */
@media (max-width: 400px) {
  .App {
    width: 95%;
    padding: 15px;
    max-width: none; /* Remove fixed width restriction */
  }

  li {
    flex-direction: column;
    align-items: flex-start;
  }

  input {
    width: 100%;
  }

  button {
    width: 100%;
    padding: 10px;
  }
}
```

Voici ce que fait ce code CSS :

Tout d'abord, il centre l'application (`html, body`) :

* Utilise `flexbox` pour centrer l'application verticalement et horizontalement.
    
* Définit `height: 100vh` pour une hauteur pleine écran.
    
* Empêche le défilement horizontal avec `overflow-x: hidden`.
    

Ensuite, il style le conteneur principal de l'application (`.App`) :

* Ajoute un fond blanc avec des coins arrondis et une ombre.
    
* Assure la réactivité avec `width: 90%` et `max-width: 350px`.
    

Ensuite, nous gérons la typographie et la mise en page :

* Définit `Arial, sans-serif` comme police.
    
* Ajoute un espacement sous le titre (`h1`).
    
* Assure que le texte de la tâche prend l'espace disponible avec `span { flex: 1; }`.
    

Ensuite, nous traitons le style des champs de saisie et des boutons :

* Les champs de saisie sont en pleine largeur, stylisés avec un remplissage, des bordures et des coins arrondis.
    
* Les boutons sont bleus, en pleine largeur, avec des effets de survol (`background-color: #0056b3`).
    

Et puis le style de la liste des tâches (`ul, li, span.completed`) :

* Supprime les styles de liste par défaut.
    
* Chaque tâche (`li`) a un fond blanc, un remplissage, des coins arrondis et une ombre.
    
* Les tâches terminées sont stylisées avec un `line-through` et une couleur de texte atténuée.
    

Ensuite, nous traitons le style des cases à cocher et du mode édition :

* Cases à cocher stylisées en bleu (`accent-color: #007bff`).
    
* Ajoute un `editing-container` avec `display: flex;` pour le mode édition.
    

Et enfin, nous rendons le design réactif (`@media (max-width: 400px)`) :

* Ajuste la largeur et le remplissage de `.App` pour les petits écrans.
    
* Empile les éléments de la liste (`li`) verticalement au lieu de côte à côte.
    

### Configuration du Backend

Dans votre terminal VS Code, assurez-vous d'être dans le répertoire racine de votre projet (à l'intérieur de `mern-todo-app`) puis créez un dossier appelé `backend`. Naviguez vers le dossier `backend` et initialisez `Node.js` :

```bash
mkdir backend
cd backend
npm init -y
```

#### Installer les dépendances

Toujours à l'intérieur de votre dossier `backend`, exécutez cette commande :

```bash
npm install express mongoose dotenv cors
```

Dans cette commande,

* `express` est un framework web rapide et minimal pour Node.js utilisé pour créer des applications côté serveur et des APIs.
    
* `mongoose` est une bibliothèque de modélisation de données objet (ODM) pour MongoDB, simplifiant les interactions avec la base de données.
    
* `dotenv` charge les variables d'environnement depuis un fichier `.env`, gardant les données sensibles sécurisées.
    
* `cors` active le partage des ressources entre origines (CORS), permettant aux applications frontend de communiquer avec le backend à travers différents domaines.
    

#### Créer un fichier server.js

À l'intérieur de votre dossier `backend`, créez un fichier nommé `server.js` et entrez le code suivant :

`backend/server.js`:

```javascript
// BLOCK 1: Importing Dependencies
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const dotenv = require("dotenv");

// BLOCK 2: Configuring the Express App
dotenv.config();

const app = express();

// BLOCK 3: Setting Up Middleware
app.use(cors());
app.use(express.json());

// BLOCK 4: Connecting to MongoDB
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI);
    console.log("MongoDB Connected");
  } catch (err) {
    console.error("MongoDB Connection Failed:", err);
    process.exit(1); // Exit process with failure
  }
};

// Call the database connection function
connectDB();

// BLOCK 5: Defining Routes
const tasksRoutes = require("./routes/tasks");
app.use("/api/tasks", tasksRoutes);

// BLOCK 6: Starting the Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

Voici une décomposition bloc par bloc du code ci-dessus :

**BLOCK 1 :** Importation des dépendances

* express : Crée le serveur.
    
* mongoose : Se connecte à MongoDB.
    
* cors : Active les requêtes cross-origin.
    
* dotenv : Charge les variables d'environnement.
    

**BLOCK 2 :** Configuration de l'application Express

* Charge les variables d'environnement en utilisant `dotenv.config()`.
    
* Initialise `express()` pour créer une instance d'application.
    

**BLOCK 3 :** Configuration du middleware

* cors() : Permet l'accès à l'API depuis différentes origines.
    
* express.json() : Analyse les requêtes JSON entrantes.
    

**BLOCK 4 :** Connexion à MongoDB

* Définit `connectDB()` pour se connecter à MongoDB en utilisant `MONGO_URI`.
    
* Journalise le succès ou l'échec et quitte en cas d'erreur.
    

**BLOCK 5 :** Définition des routes

* Importe `tasksRoutes` depuis `./routes/tasks`.
    
* Utilise `/api/tasks` comme route de base pour les opérations sur les tâches.
    

**BLOCK 6 :** Démarrage du serveur

* Définit `PORT` depuis `.env` ou utilise par défaut `5000`.
    
* Démarre le serveur et journalise le port en cours d'exécution.
    

#### Définir le modèle de tâche

Dans votre dossier `backend`, créez un dossier `model`. À l'intérieur de `model`, créez un fichier nommé `Task.js` et ajoutez le code suivant :

`backend/model/Task.js`:

```javascript
// BLOCK 1: Importing Mongoose
const mongoose = require("mongoose");

// BLOCK 2: Defining Task Schema
const TaskSchema = new mongoose.Schema({
    title: { type: String, required: true },
    completed: { type: Boolean, default: false },
});

// BLOCK 3: Creating and Exporting the Model
module.exports = mongoose.model("Task", TaskSchema);
```

Voici une décomposition bloc par bloc du code ci-dessus :

**BLOCK 1 :** Importation de Mongoose

* `mongoose` : Utilisé pour définir le schéma et interagir avec MongoDB.
    

**BLOCK 2 :** Définition du schéma de la tâche

* `title` : Un champ de type chaîne requis pour le titre de la tâche.
    
* `completed` : Un champ booléen indiquant l'état de la tâche (par défaut : `false`).
    

**BLOCK 3 :** Création et exportation du modèle

* Crée un modèle Mongoose nommé `"Task"` basé sur `TaskSchema`.
    
* Exporte le modèle pour une utilisation dans d'autres parties de l'application.
    

#### Définir les routes

Dans votre dossier `backend`, créez un dossier `routes`. À l'intérieur de `routes`, créez un fichier nommé `tasks.js` et ajoutez le code suivant :

`backend/routes/tasks.js`:

```javascript
// BOCK 1: Import dependencies
const express = require("express");
const Task = require("../models/Task");

const router = express.Router();

// BLOCK 2: GET all tasks
router.get("/", async (req, res) => {
  try {
    const tasks = await Task.find();
    res.json(tasks);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// BLOCK 3: POST a new task
router.post("/", async (req, res) => {
  const { title } = req.body;
  console.log("Received title:", title); // Debugging log

  if (!title) {
    return res.status(400).json({ error: "Task title is required" });
  }

  try {
    const newTask = new Task({ title });
    await newTask.save();
    res.status(201).json(newTask);
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: err.message });
  }
});

// BLOCK 4: DELETE a task
router.delete("/:id", async (req, res) => {
  try {
    const { id } = req.params;
    await Task.findByIdAndDelete(id);
    res.json({ message: "Task deleted" });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// BLOCK 5: UPDATE a task
router.put("/:id", async (req, res) => {
  try {
    const { id } = req.params;
  
    const updatedTask = await Task.findByIdAndUpdate(
      id,
      req.body,
      { new: true } // Return the updated task
    );
    res.json(updatedTask);
  } catch (error) {
    res.status(500).json({ error: "Error updating task" });
  }
});

// BLOCK 6: Export the router
module.exports = router;
```

Voici une décomposition bloc par bloc du code ci-dessus :

**BLOCK 1 :** Importation des dépendances

* express : Gère le routage.
    
* Task : Importe le modèle Task.
    
* express.Router() : Crée un routeur pour les routes liées aux tâches.
    

**BLOCK 2 :** GET toutes les tâches

* Récupère toutes les tâches de la base de données.
    
* Envoie les tâches en tant que réponse JSON.
    
* Gère les erreurs avec un statut 500.
    

**BLOCK 3 :** POST une nouvelle tâche

* Extrait `title` du corps de la requête.
    
* Journalise le titre reçu pour le débogage.
    
* Valide le titre (retourne 400 s'il est manquant).
    
* Enregistre la tâche dans la base de données et la retourne.
    

**BLOCK 4 :** DELETE une tâche

* Extrait `id` des paramètres de la requête.
    
* Supprime la tâche de la base de données.
    
* Retourne un message de succès.
    

**BLOCK 5 :** UPDATE une tâche

* Extrait `id` des paramètres de la requête.
    
* Met à jour la tâche en utilisant les données du corps de la requête.
    
* Retourne la tâche mise à jour.
    

**BLOCK 6 :** Exportation du routeur

* Exporte `router` pour une utilisation dans d'autres parties de l'application.
    

Ce routeur Express.js gère les opérations CRUD pour un modèle `Task` en utilisant MongoDB. Il définit des routes pour obtenir toutes les tâches, ajouter une nouvelle tâche, supprimer une tâche par ID et mettre à jour le titre d'une tâche par ID. La gestion des erreurs garantit des réponses appropriées pour les données manquantes ou les problèmes de serveur.

#### Créer un fichier .env

Dans votre dossier backend, créez un fichier `.env` et ajoutez ce qui suit :

`backend/.env`:

```javascript
MONGO_URI=your_mongodb_atlas_uri
```

### Configurer MongoDB Atlas

MongoDB Atlas est un service MongoDB basé sur le cloud. Nous utiliserons le niveau gratuit pour ce projet.

Pour commencer, allez sur [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database) et créez un compte ou connectez-vous.

Suivez les étapes pour créer un cluster gratuit. Une fois le cluster créé, cliquez sur Connect et suivez les instructions pour :

* Ajouter votre adresse IP à la liste blanche pour permettre l'accès à MongoDB en utilisant votre variable d'environnement.
    
* Créer un utilisateur de base de données.
    
* Obtenir la chaîne de connexion.
    

Remplacez `your_mongodb_atlas_uri` dans le fichier `.env` par votre chaîne de connexion MongoDB Atlas.

Si vous n'êtes toujours pas à l'aise avec la configuration de MongoDB Atlas, lisez ceci : [Tutoriel MongoDB Atlas - Comment commencer](https://www.freecodecamp.org/news/get-started-with-mongodb-atlas/).

### Exécuter l'application

Pour exécuter l'application avec succès en utilisant `npm run dev`, vous devez installer une dépendance qui démarrera à la fois le frontend et le backend simultanément. Vous pouvez le faire en utilisant [concurrently](https://www.npmjs.com/package/concurrently).

Installez concurrently :

Ouvrez votre terminal, naviguez jusqu'au répertoire racine de votre projet (`mern-todo-app`), et exécutez :

```bash
npm install concurrently
```

#### Configurer `package.json` :

Après avoir installé concurrently, assurez-vous d'avoir un fichier `package.json` dans le répertoire racine de votre projet. S'il n'existe pas, créez-en un et ajoutez le code suivant :

`mern-todo-app/package.json`:

```json
{
    "name": "mern-todo-app",
    "version": "1.0.0",
    "private": true,
    "scripts": {
        "start": "cd backend && npm start",
        "client": "cd frontend && npm run dev",
        "dev": "concurrently \"npm run start\" \"npm run client\""
    },
    "dependencies": {
        "concurrently": "^8.2.2"
    }
}
```

Ce fichier `package.json` configure l'application en définissant :

* Les métadonnées du projet (`name, version, private flag`).
    
* Les scripts (`start`, `client`, et `dev`) pour démarrer le backend, exécuter le frontend, et exécuter les deux simultanément.
    
* Les dépendances, y compris `concurrently`, qui permet d'exécuter plusieurs scripts en parallèle.
    
* Le projet est défini comme privé pour éviter une publication accidentelle.
    

#### Démarrer l'application

Assurez-vous que tout est configuré et sauvegardé, puis exécutez la commande suivante depuis la racine du projet :

```bash
npm run dev
```

Si l'application démarre avec succès, vous devriez voir des messages comme :

```nginx
Server running on port 5000
MongoDB Connected
```

#### Voir l'application

Ouvrez votre navigateur et accédez à :

* Frontend (interface de l'application To-Do) : **http://localhost:5173**
    
* Backend (tâches stockées dans la base de données) : **http://localhost:5000/api/tasks**
    

Testez la fonctionnalité en ajoutant, modifiant, sauvegardant, supprimant des tâches et en cochant les tâches terminées pour vous assurer que tout fonctionne correctement.

## Conclusion

Félicitations ! Vous avez réussi à créer une application To-Do MERN. Vous pouvez l'améliorer davantage en ajoutant des fonctionnalités telles que le suivi du temps et de la date, et en la déployant sur une plateforme cloud.

N'hésitez pas à copier le code ou à cloner le [dépôt GitHub](https://github.com/nuelcas/mern-todo-app.git) pour ajouter plus de fonctionnalités et personnaliser le style selon vos préférences. Si vous avez trouvé ce guide utile, envisagez de le partager et de [me contacter](https://www.linkedin.com/in/casmir-onyekani/) !

Pour plus de ressources d'apprentissage :

* [Documentation React.js](https://react.dev/)
    
* [Documentation TypeScript](https://www.typescriptlang.org/)
    
* [Documentation Vite](https://vite.dev/)
    
* [Documentation MongoDB](https://www.mongodb.com/docs/)
    
* [Documentation Node.js](https://nodejs.org/docs/latest/api/)