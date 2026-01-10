---
title: How to Build a MERN Stack To-Do App
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
seo_title: null
seo_desc: This guide will walk you through building a full-stack MERN To-Do application.
  It covers setting up the environment, writing code to demonstrate core CRUD (Create,
  Read, Update, Delete) operations, and connecting the application to MongoDB Atlas,
  a f...
---

This guide will walk you through building a full-stack MERN To-Do application. It covers setting up the environment, writing code to demonstrate core CRUD (Create, Read, Update, Delete) operations, and connecting the application to MongoDB Atlas, a free cloud database.

Before diving into this article, I recommend that you have a foundational understanding of HTML, CSS, and JavaScript, as well as some knowledge of frontend and backend frameworks and libraries.

My primary focus will be on functionality, allowing you to customize the design as you see fit. The commands I’ll use here are tailored for Windows, so if you're using Linux, macOS, or Ubuntu, you may need to adjust them accordingly.

By the end of this guide, you'll have a fully functional To-Do app up and running on your system.

## Table of Contents

* [Introduction to the MERN Stack](#heading-introduction-to-the-mern-stack)
    
* [How to Set Up Your Development environment](#heading-how-to-set-up-your-development-environment)
    
    * [Install Node.js and npm - Node Package Manager](#heading-install-nodejs-and-npm-node-package-manager)
        
* [How to Set Up a New MERN Project](#heading-how-to-set-up-a-new-mern-project)
    
    * [Frontend Setup](#heading-frontend-setup)
        
    * [Build the To-Do App UI](#heading-build-the-to-do-app-ui)
        
    * [Displaying your tasks in the UI](#heading-displaying-your-tasks-in-the-ui)
        
    * [Give Your App Customized Styling](#heading-give-your-app-customized-styling)
        
    * [Backend Setup](#heading-backend-setup)
        
    * [Set Up MongoDB Atlas](#heading-set-up-mongodb-atlas)
        
    * [Run the Application](#heading-run-the-application)
        
* [Conclusion](#heading-conclusion)
    

## Introduction to the MERN Stack

The MERN stack is a popular JavaScript stack for building modern web applications. It consists of:

* **MongoDB**: A NoSQL database for storing data.
    
* **Express.js**: A backend framework for building APIs.
    
* **React (UI library) + Vite (build tool) + TypeScript (typed JavaScript)**: A modern frontend stack for building scalable and maintainable user interfaces.
    
* **Node.js**: A runtime environment for executing JavaScript on the server.
    

## How to Set Up Your Development environment

### Install Node.js and npm (Node Package Manager)

Instead of installing Node.js and npm in your project folder, I advise you to install them in your system's root directory so that you can use them in any project, not just this one.

First, download and install Node.js (which includes npm) from the [official website](https://nodejs.org/en) if you don’t have it already.

After installation, open your command line (I am using Git Bash) and verify the installation by running the following commands:

```bash
node -v
npm -v
```

You should see the installed versions of Node.js and npm if correctly installed.

## How to Set Up a New MERN Project

Create a project folder and open your code editor by running these commands:

```bash
mkdir mern-todo-app
cd mern-todo-app
code .
```

The command `code .` automatically opens VS Code. If it doesn’t, open VS Code manually and navigate to your `mern-todo-app` folder.

### Frontend Setup

#### Set Up Vite with React and TypeScript

Make sure you are in your project root directory (`mern-todo-app`), then run the following command:

```bash
npm create vite@latest frontend --template react-ts
```

This command will create a TypeScript-based React frontend inside the `frontend` folder within your `mern-todo-app` directory.

#### Install Axios for Making API Requests

Axios is a popular JavaScript library used to make HTTP requests from the frontend to a backend API. It simplifies sending GET, POST, PUT, and DELETE requests and handling responses.

To install Axios, run the following command:

```bash
cd frontend
npm install axios
```

### Build the To-Do App UI

Inside the `src` folder, create an `App.tsx` file if it doesn’t already exist, and add the below code. It’s a lot, but don’t worry – I’ll break it down bit by bit afterwards:

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

Here’s a block-by-block breakdown of the code above:

**BLOCK 1:** Importing dependencies

* `React, { useState, useEffect }`: Manages component state and side effects.
    
* `axios`: Handles API requests.
    
* `TodoList.tsx`: A child component to display and manage tasks.
    
* `App.css`: Styles the app.
    

**BLOCK 2:** Defining the task interface

* Defines the structure of a task (`_id`, `title`, `completed`).
    

**BLOCK 3:** Setting up state variables

* `tasks`: Stores the list of tasks.
    
* `task`: Holds input for new tasks.
    
* `editingTaskId`: Tracks the task being edited.
    
* `editingTitle`: Stores the updated title while editing.
    

**BLOCK 4:** Fetching tasks from the backend (`useEffect`)

* Runs once when the app loads.
    
* Calls the API (`GET /api/tasks`) to get tasks and updates `tasks`.
    
* Error handling\*\*:\*\* Logs an error message if the fetching request fails
    

**BLOCK 5:** Adding a task

* Sends a `POST` request to add a new task.
    
* Updates `tasks` with the new task.
    
* Error handling\*\*:\*\* Logs an error message if the adding task request fails
    

**BLOCK 6:** Deleting a task

* Sends a `DELETE` request to remove a task.
    
* Updates `tasks` by filtering out the deleted task.
    
* Error handling\*\*:\*\* Logs an error message if the deleting task request fails
    

**BLOCK 7:** Updating a task

* Sends a `PUT` request to update a task’s title.
    
* Updates `tasks` with the new title.
    
* Error handling\*\*:\*\* Logs an error message if the update request fails
    

**BLOCK 8:** Handling edits

* `startEditing(id)`: Sets a task into edit mode.
    
* `handleEditChange(e)`: Updates the editing input.
    

**BLOCK 9:** Rendering the UI

* Displays an input field and button to add tasks.
    
* Passes task data and functions (`deleteTask`, `updateTask`, etc.) to `TodoList.tsx`.
    

**BLOCK 10:** Exporting the component

* `export default App;`: Makes `App` usable in other files.
    

### Displaying your tasks in the UI

Inside the `src` folder, create a new folder named `components`. Then add a `TodoList.tsx` file inside it with the below code.

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

Here’s a block-by-block breakdown of the code above:

**BLOCK 1:** Importing dependencies

* React: Enables functional component creation.
    

**BLOCK 2:** Defining interfaces

* Task interface: Defines `_id`, `title`, and `completed` properties.
    
* TodoListProps interface: Defines props passed to the `TodoList` component
    

**BLOCK 3**: Declares the `TodoList` component

* Defines a functional React component (`TodoList`) using TypeScript (`React.FC<TodoListProps>`).
    
* Extracts the listed props from `TodoListProps` and prepares the component for rendering.
    

**BLOCK 4**: Rendering the Task List and handling task actions

* Maps through `tasks` to display each task inside a `<ul>`.
    
* Checkbox toggles `completed` status using `updateTask()`.
    
* Conditional rendering:
    
    * If a task is being edited, an input field appears for editing.
        
    * Otherwise, the task title is displayed with a strikethrough if completed
        
* Save button: Updates the task title using `updateTask()`, then exits edit mode.
    
* Delete button: Calls `deleteTask()` to remove a task.
    
* Edit button: Enables edit mode, setting `editingTaskId` and `editingTitle`.
    

**BLOCK 5**: Exporting the component

* Makes `TodoList` available for use in other components.
    

### Give Your App Customized Styling

Inside your `src` folder, create `App.css` if it doesn’t exist and replace the content with your desired styling. Let’s give the frontend a finishing touch.

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

Here’s what this CSS code does:

First, it centers the app (`html, body`):

* Uses `flexbox` to center the app vertically and horizontally.
    
* Sets `height: 100vh` for full-screen height.
    
* Prevents horizontal scrolling with `overflow-x: hidden`.
    

Then it styles the main app container (`.App`):

* Adds a white background with rounded corners and a shadow.
    
* Ensures responsiveness with `width: 90%` and `max-width: 350px`.
    

Next, we handle typography and layout:

* Sets `Arial, sans-serif` as the font.
    
* Adds spacing below the title (`h1`).
    
* Ensures task text takes available space with `span { flex: 1; }`.
    

Then we deal with input and button styling:

* Inputs are full-width, styled with padding, borders, and rounded corners.
    
* Buttons are blue, full-width, with hover effects (`background-color: #0056b3`).
    

And then task list styling **(**`ul, li, span.completed`):

* Removes default list styles.
    
* Each task (`li`) has a white background, padding, rounded corners, and a shadow.
    
* Completed tasks are styled with a `line-through` and faded text color.
    

Next, we handle checkbox and editing mode styling:

* Styled blue checkboxes (`accent-color: #007bff`).
    
* Adds an `editing-container` with `display: flex;` for edit mode.
    

And finally, we make the design responsive (`@media (max-width: 400px)`):

* Adjusts `.App` width and padding for small screens.
    
* Stacks list items (`li`) vertically instead of side-by-side.
    

### Backend Setup

In your VS Code terminal, make sure you are in your project root directory (inside `mern-todo-app`) and then create a folder called `backend`. Navigate to the `backend` folder and initialize `Node.js`:

```bash
mkdir backend
cd backend
npm init -y
```

#### Install Dependencies

Still inside your `backend` folder, run this command:

```bash
npm install express mongoose dotenv cors
```

In this command,

* `express` is a fast and minimal web framework for Node.js used to create server-side applications and APIs.
    
* `mongoose` is an Object Data Modeling (ODM) library for MongoDB, simplifying database interactions.
    
* `dotenv` loads environment variables from a `.env` file, keeping sensitive data secure.
    
* `cors` enables Cross-Origin Resource Sharing, allowing frontend applications to communicate with the backend across different domains.
    

#### Create a server.js File

Inside your `backend` folder, create a file named `server.js` and enter the following code:

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

Here’s a block-by-block breakdown of the code above:

**BLOCK 1**: Importing dependencies

* express\*\*:\*\* Creates the server.
    
* mongoose\*\*:\*\* Connects to MongoDB.
    
* cors\*\*:\*\* Enables cross-origin requests.
    
* dotenv\*\*:\*\* Loads environment variables.
    

**BLOCK 2**: Configuring the Express app

* Loads environment variables using `dotenv.config()`.
    
* Initializes `express()` to create an app instance.
    

**BLOCK 3**: Setting up middleware

* cors()**:** Allows API access from different origins.
    
* express.json()**:** Parses incoming JSON requests.
    

**BLOCK 4**: Connecting to MongoDB

* Defines `connectDB()` to connect to MongoDB using `MONGO_URI`.
    
* Logs success or failure and exits on error.
    

**BLOCK 5**: Defining routes

* Imports `tasksRoutes` from `./routes/tasks`.
    
* Uses `/api/tasks` as the base route for task operations.
    

**BLOCK 6**: Starting the server

* Sets `PORT` from `.env` or defaults to `5000`.
    
* Starts the server and logs the running port.
    

#### Define Task Model

In your `backend` folder, create a `model` folder. Inside `model`, create a file named `Task.js` and add the following code:

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

Here’s a block-by-block breakdown of the code above:

**BLOCK 1**: Importing Mongoose

* `mongoose`: Used to define the schema and interact with MongoDB.
    

**BLOCK 2**: Defining the task schema

* `title`: A required string field for the task title.
    
* `completed`: A boolean field indicating task status (default: `false`).
    

**BLOCK 3**: Creating and exporting the model

* Creates a Mongoose model named `"Task"` based on `TaskSchema`.
    
* Exports the model for use in other parts of the application
    

#### Define Routes

In your `backend` folder, create a `routes` folder. Inside `routes`, create a file named `tasks.js` and add the following code:

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

Here’s a block-by-block breakdown of the code above:

**BLOCK 1**: Import dependencies

* express: Handles routing.
    
* Task: Imports the Task model.
    
* express.Router(): Creates a router for task-related routes.
    

**BLOCK 2**: GET all tasks

* Fetches all tasks from the database.
    
* Sends the tasks as a JSON response.
    
* Handles errors with a 500 status.
    

**BLOCK 3**: POST a new task

* Extracts `title` from the request body.
    
* Logs the received title for debugging.
    
* Validates the title (returns 400 if missing).
    
* Saves the task to the database and returns it.
    

**BLOCK 4**: DELETE a task

* Extracts `id` from the request params.
    
* Deletes the task from the database.
    
* Returns a success message.
    

**BLOCK 5**: UPDATE a task

* Extracts `id` from the request params.
    
* Updates the task using request body data.
    
* Returns the updated task.
    

**BLOCK 6**: Export the router

* Exports `router` for use in other parts of the app.
    

This Express.js router handles CRUD operations for a `Task` model using MongoDB. It defines routes to get all tasks, add a new task, delete a task by ID, and update a task's title by ID. Error handling ensures proper responses for missing data or server issues.

#### Create a .env file

In your backend folder, create a `.env` file and add the following:

`backend/.env`:

```javascript
MONGO_URI=your_mongodb_atlas_uri
```

### Set Up MongoDB Atlas

MongoDB Atlas is a cloud-based MongoDB service. We'll use the free tier for this project.

To get started, go to [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database) and create an account or log in.

Follow the steps to create a free cluster. Once the cluster is created, click Connect and follow the instructions to:

* Whitelist your IP address to allow MongoDB access using your environment variable.
    
* Create a database user.
    
* Get the connection string.
    

Replace the `your_mongodb_atlas_uri` in `.env` file with your MongoDB Atlas connection string.

If you are still not comfortable with how to set up MongoDB atlas, read this: [MongoDB Atlas Tutorial – How to Get Started](https://www.freecodecamp.org/news/get-started-with-mongodb-atlas/).

### Run the Application

To run the application successfully using `npm run dev`, you need to install a dependency that will start both the frontend and backend simultaneously. You can do this using [concurrently](https://www.npmjs.com/package/concurrently)**.**

Install concurrently:

Open your terminal, navigate to your project root directory (`mern-todo-app`), and run:

```bash
npm install concurrently
```

#### Configure `package.json`:

After installing concurrently, ensure that you have a `package.json` file in your project root directory. If it doesn't exist, create one and add the following code:

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

This `package.json` file configures the application by defining:

* Project metadata (`name, version, private flag`).
    
* Scripts (`start`, `client`, and `dev`) to start the backend, run the frontend, and execute both simultaneously.
    
* Dependencies, including `concurrently`, which enables running multiple scripts in parallel.
    
* The project is set to private to prevent accidental publishing.
    

#### Start the Application

Ensure everything is set up and saved, then run the following command from the project root:

```bash
npm run dev
```

If the application starts successfully, you should see messages like:

```nginx
Server running on port 5000
MongoDB Connected
```

#### View the Application

Open your browser and navigate to:

* Frontend (To-Do app interface)**:** **http://localhost:5173**
    
* Backend (Stored tasks in the database)**:** **http://localhost:5000/api/tasks**
    

Test the functionality by adding, editing, saving, deleting tasks, and checking off completed tasks to ensure everything works properly.

## Conclusion

Congratulations! You have successfully built a MERN To-Do app. You can further enhance it by adding features such as time and date tracking, and deploying it to a cloud platform.

Feel free to copy the code or clone the [GitHub](https://github.com/nuelcas/mern-todo-app.git) repository to add more functionalities and customize the styling to your preference. If you found this guide helpful, please consider sharing it and [connecting](https://www.linkedin.com/in/casmir-onyekani/) with me!

For more learning resources:

* [React.js Docs](https://react.dev/)
    
* [TypeScript Docs](https://www.typescriptlang.org/)
    
* [Vite Docs](https://vite.dev/)
    
* [MongoDB Docs](https://www.mongodb.com/docs/)
    
* [Node.js Docs](https://nodejs.org/docs/latest/api/)
