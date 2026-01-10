---
title: Use the FARM Stack to Develop Full Stack Apps
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2024-09-18T13:55:42.198Z'
originalURL: https://freecodecamp.org/news/use-the-farm-stack-to-develop-full-stack-apps
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726760870442/726967ee-7f01-432d-a73e-9f73f037f942.jpeg
tags:
- name: MongoDB
  slug: mongodb
- name: React
  slug: reactjs
- name: FastAPI
  slug: fastapi
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'The FARM stack is a modern web development stack that combines three powerful
  technologies: FastAPI, React, and MongoDB. This full-stack solution provides developers
  with a robust set of tools to build scalable, efficient, and high-performance web
  ap...'
---

The FARM stack is a modern web development stack that combines three powerful technologies: FastAPI, React, and MongoDB. This full-stack solution provides developers with a robust set of tools to build scalable, efficient, and high-performance web applications.

In this article, I'll be giving you an introduction to each of the key technologies, and then we'll build a project using the FARM stack and Docker so you can see how everything works together.

This article is based on a course I created [on the freeCodeCamp.org YouTube channel](https://www.youtube.com/watch?v=PWG7NlUDVaA). Watch it here:

%[https://www.youtube.com/watch?v=PWG7NlUDVaA] 

# Introduction to the FARM Stack

The FARM in FARM stack stands for:

* F: FastAPI (Backend)
    
* R: React (Frontend)
    
* M: MongoDB (Database)
    

The FARM stack is designed to leverage the strengths of each component, allowing developers to create feature-rich applications with a smooth development experience.

### Components of FARM Stack

1. **FastAPI:** FastAPI is a modern, high-performance Python web framework for building APIs. It's designed to be easy to use, fast to code, and ready for production environments. FastAPI is built on top of Starlette for the web parts and Pydantic for the data parts, making it a powerful choice for building robust backend services.
    
2. **React**: React is a popular JavaScript library for building user interfaces. Developed and maintained by Facebook, React allows developers to create reusable UI components that efficiently update and render as data changes. Its component-based architecture and virtual DOM make it an excellent choice for building dynamic and responsive frontend applications.
    
3. **MongoDB:** MongoDB is a document-oriented NoSQL database. It stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time. This flexibility makes MongoDB an ideal choice for applications that need to evolve quickly and handle diverse data types.
    

### Advantages of using FARM Stack

1. High Performance: FastAPI is one of the fastest Python frameworks available, while React's virtual DOM ensures efficient UI updates. MongoDB's document model allows for quick reads and writes.
    
2. Scalability: All components of the FARM stack are designed to scale. FastAPI can handle concurrent requests efficiently, React applications can manage complex UIs, and MongoDB can distribute data across multiple servers.
    
3. Community and Ecosystem: All three technologies have large, active communities and rich ecosystems of libraries and tools.
    
4. Flexibility: The FARM stack is flexible enough to accommodate various types of web applications, from simple CRUD apps to complex, data-intensive systems.
    

By combining these technologies, the FARM stack provides a comprehensive solution for building modern web applications. It allows developers to create fast, scalable backends with FastAPI, intuitive and responsive frontends with React, and flexible, efficient data storage with MongoDB. This stack is particularly well-suited for applications that require real-time updates, complex data models, and high performance.

# Project Overview: Todo Application

In the video course, I cover more about each individual technology in the FARM Stack. But in this article, we are going to jump right into a project to put everything together.

We will be creating a todo application to help us understand the FARM stack. Before we start creating the applicaiton, let’s discuss more about the features and software architecture.

### Features of the todo application

Our FARM stack todo application will include the following features:

1. Multiple Todo Lists:
    
    * Users can create, view, update, and delete multiple todo lists.
        
    * Each list has a name and contains multiple todo items.
        
2. Todo Items:
    
    * Within each list, users can add, view, update, and delete todo items.
        
    * Each item has a label, a checked/unchecked status, and belongs to a specific list.
        
3. Real-time Updates:
    
    * The UI updates in real-time when changes are made to lists or items.
        
4. Responsive Design:
    
    * The application will be responsive and work well on both desktop and mobile devices.
        

### System architecture

Our todo application will follow a typical FARM stack architecture:

1. Frontend (React):
    
    * Provides the user interface for interacting with todo lists and items.
        
    * Communicates with the backend via RESTful API calls.
        
2. Backend (FastAPI):
    
    * Handles API requests from the frontend.
        
    * Implements business logic for managing todo lists and items.
        
    * Interacts with the MongoDB database for data persistence.
        
3. Database (MongoDB):
    
    * Stores todo lists and items.
        
    * Provides efficient querying and updating of todo data.
        
4. Docker:
    
    * Containerizes each component (frontend, backend, database) for easy development and deployment.
        

### Data model design

Our MongoDB data model will consist of two main structures:

1. Todo List:
    

```json
   {
     "_id": ObjectId,
     "name": String,
     "items": [
       {
         "id": String,
         "label": String,
         "checked": Boolean
       }
     ]
   }
```

2. List Summary (for displaying in the list of all todo lists):
    

```json
   {
     "_id": ObjectId,
     "name": String,
     "item_count": Integer
   }
```

### API endpoint design

Our FastAPI backend will expose the following RESTful endpoints:

1. Todo Lists:
    
    * GET /api/lists: Retrieve all todo lists (summary view)
        
    * POST /api/lists: Create a new todo list
        
    * GET /api/lists/{list\_id}: Retrieve a specific todo list with all its items
        
    * DELETE /api/lists/{list\_id}: Delete a specific todo list
        
2. Todo Items:
    
    * POST /api/lists/{list\_id}/items: Add a new item to a specific list
        
    * PATCH /api/lists/{list\_id}/checked\_state: Update the checked state of an item
        
    * DELETE /api/lists/{list\_id}/items/{item\_id}: Delete a specific item from a list
        

This project will provide a solid foundation in FARM stack development and Docker containerization, which you can then expand upon for more complex applications in the future.

So let's get started with the project.

# Project Tutorial

## Project Setup and Backend Development

Step 1: Set up the project structure

Create a new directory for your project:

```csharp
   mkdir farm-stack-todo
   cd farm-stack-todo
```

Create subdirectories for the backend and frontend:

```csharp
   mkdir backend frontend
```

Step 2: Set up the backend environment

Navigate to the backend directory:

```csharp
   cd backend
```

Create a virtual environment and activate it:

```csharp
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

Create the following files in the backend directory:

3. * Dockerfile
        
    * pyproject.toml
        
    
    In your terminal, install the required packages:
    

```powershell
pip install "fastapi[all]" "motor[srv]" beanie aiostream
```

Generate the requirements.txt file:

```powershell
pip freeze > requirements.txt
```

After creating the requirements.txt file (either through pip-compile or manually), you can install the dependencies using:

```csharp
   pip install -r requirements.txt
```

Add the following content to Dockerfile:

```csharp
   FROM python:3

   WORKDIR /usr/src/app
   COPY requirements.txt ./

   RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

   EXPOSE 3001

   CMD [ "python", "./src/server.py" ]
```

Add the following content to pyproject.toml:

```csharp
   [tool.pytest.ini_options]
   pythonpath = "src"
```

Step 4: Set up the backend structure

Create a src directory inside the backend directory:

```csharp
   mkdir src
```

Create the following files inside the src directory:

2. * [server.py](http://server.py)
        
    * [dal.py](http://dal.py)
        

Step 5: Implement the Data Access Layer (DAL)

Open src/[dal.py](http://dal.py) and add the following content:

```python
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import ReturnDocument

from pydantic import BaseModel

from uuid import uuid4

class ListSummary(BaseModel):
  id: str
  name: str
  item_count: int

  @staticmethod
  def from_doc(doc) -> "ListSummary":
      return ListSummary(
          id=str(doc["_id"]),
          name=doc["name"],
          item_count=doc["item_count"],
      )

class ToDoListItem(BaseModel):
  id: str
  label: str
  checked: bool

  @staticmethod
  def from_doc(item) -> "ToDoListItem":
      return ToDoListItem(
          id=item["id"],
          label=item["label"],
          checked=item["checked"],
      )

class ToDoList(BaseModel):
  id: str
  name: str
  items: list[ToDoListItem]

  @staticmethod
  def from_doc(doc) -> "ToDoList":
      return ToDoList(
          id=str(doc["_id"]),
          name=doc["name"],
          items=[ToDoListItem.from_doc(item) for item in doc["items"]],
      )

class ToDoDAL:
  def __init__(self, todo_collection: AsyncIOMotorCollection):
      self._todo_collection = todo_collection

  async def list_todo_lists(self, session=None):
      async for doc in self._todo_collection.find(
          {},
          projection={
              "name": 1,
              "item_count": {"$size": "$items"},
          },
          sort={"name": 1},
          session=session,
      ):
          yield ListSummary.from_doc(doc)

  async def create_todo_list(self, name: str, session=None) -> str:
      response = await self._todo_collection.insert_one(
          {"name": name, "items": []},
          session=session,
      )
      return str(response.inserted_id)

  async def get_todo_list(self, id: str | ObjectId, session=None) -> ToDoList:
      doc = await self._todo_collection.find_one(
          {"_id": ObjectId(id)},
          session=session,
      )
      return ToDoList.from_doc(doc)

  async def delete_todo_list(self, id: str | ObjectId, session=None) -> bool:
      response = await self._todo_collection.delete_one(
          {"_id": ObjectId(id)},
          session=session,
      )
      return response.deleted_count == 1

  async def create_item(
      self,
      id: str | ObjectId,
      label: str,
      session=None,
  ) -> ToDoList | None:
      result = await self._todo_collection.find_one_and_update(
          {"_id": ObjectId(id)},
          {
              "$push": {
                  "items": {
                      "id": uuid4().hex,
                      "label": label,
                      "checked": False,
                  }
              }
          },
          session=session,
          return_document=ReturnDocument.AFTER,
      )
      if result:
          return ToDoList.from_doc(result)

  async def set_checked_state(
      self,
      doc_id: str | ObjectId,
      item_id: str,
      checked_state: bool,
      session=None,
  ) -> ToDoList | None:
      result = await self._todo_collection.find_one_and_update(
          {"_id": ObjectId(doc_id), "items.id": item_id},
          {"$set": {"items.$.checked": checked_state}},
          session=session,
          return_document=ReturnDocument.AFTER,
      )
      if result:
          return ToDoList.from_doc(result)

  async def delete_item(
      self,
      doc_id: str | ObjectId,
      item_id: str,
      session=None,
  ) -> ToDoList | None:
      result = await self._todo_collection.find_one_and_update(
          {"_id": ObjectId(doc_id)},
          {"$pull": {"items": {"id": item_id}}},
          session=session,
          return_document=ReturnDocument.AFTER,
      )
      if result:
          return ToDoList.from_doc(result)
```

This concludes Part 1 of the tutorial, where we set up the project structure and implemented the Data Access Layer for our FARM stack todo application. In the next part, we'll implement the FastAPI server and create the API endpoints.

## Implementing the FastAPI Server

Step 6: Implement the FastAPI server

Open src/[server.py](http://server.py) and add the following content:

```python
from contextlib import asynccontextmanager
from datetime import datetime
import os
import sys

from bson import ObjectId
from fastapi import FastAPI, status
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import uvicorn

from dal import ToDoDAL, ListSummary, ToDoList

COLLECTION_NAME = "todo_lists"
MONGODB_URI = os.environ["MONGODB_URI"]
DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup:
    client = AsyncIOMotorClient(MONGODB_URI)
    database = client.get_default_database()

    # Ensure the database is available:
    pong = await database.command("ping")
    if int(pong["ok"]) != 1:
        raise Exception("Cluster connection is not okay!")

    todo_lists = database.get_collection(COLLECTION_NAME)
    app.todo_dal = ToDoDAL(todo_lists)

    # Yield back to FastAPI Application:
    yield

    # Shutdown:
    client.close()


app = FastAPI(lifespan=lifespan, debug=DEBUG)


@app.get("/api/lists")
async def get_all_lists() -> list[ListSummary]:
    return [i async for i in app.todo_dal.list_todo_lists()]


class NewList(BaseModel):
    name: str


class NewListResponse(BaseModel):
    id: str
    name: str


@app.post("/api/lists", status_code=status.HTTP_201_CREATED)
async def create_todo_list(new_list: NewList) -> NewListResponse:
    return NewListResponse(
        id=await app.todo_dal.create_todo_list(new_list.name),
        name=new_list.name,
    )


@app.get("/api/lists/{list_id}")
async def get_list(list_id: str) -> ToDoList:
    """Get a single to-do list"""
    return await app.todo_dal.get_todo_list(list_id)


@app.delete("/api/lists/{list_id}")
async def delete_list(list_id: str) -> bool:
    return await app.todo_dal.delete_todo_list(list_id)


class NewItem(BaseModel):
    label: str


class NewItemResponse(BaseModel):
    id: str
    label: str


@app.post(
    "/api/lists/{list_id}/items/",
    status_code=status.HTTP_201_CREATED,
)
async def create_item(list_id: str, new_item: NewItem) -> ToDoList:
    return await app.todo_dal.create_item(list_id, new_item.label)


@app.delete("/api/lists/{list_id}/items/{item_id}")
async def delete_item(list_id: str, item_id: str) -> ToDoList:
    return await app.todo_dal.delete_item(list_id, item_id)


class ToDoItemUpdate(BaseModel):
    item_id: str
    checked_state: bool


@app.patch("/api/lists/{list_id}/checked_state")
async def set_checked_state(list_id: str, update: ToDoItemUpdate) -> ToDoList:
    return await app.todo_dal.set_checked_state(
        list_id, update.item_id, update.checked_state
    )


class DummyResponse(BaseModel):
    id: str
    when: datetime


@app.get("/api/dummy")
async def get_dummy() -> DummyResponse:
    return DummyResponse(
        id=str(ObjectId()),
        when=datetime.now(),
    )


def main(argv=sys.argv[1:]):
    try:
        uvicorn.run("server:app", host="0.0.0.0", port=3001, reload=DEBUG)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
```

This implementation sets up the FastAPI server with CORS middleware, connects to MongoDB, and defines the API endpoints for our todo application.

Step 7: Set up environment variables

Create a .env file in the root directory with the following content. Make sure to add the database name ("todo") at the end of ".mongodb.net/".

```csharp
MONGODB_URI='mongodb+srv://beau:codecamp@cluster0.ji7hu.mongodb.net/todo?retryWrites=true&w=majority&appName=Cluster0'
```

Step 8: Create a docker-compose file

In the root directory of your project (farm-stack-todo), create a file named compose.yml with the following content:

```csharp
name: todo-app
services:
  nginx:
    image: nginx:1.17
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf
    ports:
      - 8000:80
    depends_on:
      - backend
      - frontend
  frontend:
    image: "node:22"
    user: "node"
    working_dir: /home/node/app
    environment:
      - NODE_ENV=development
      - WDS_SOCKET_PORT=0
    volumes:
      - ./frontend/:/home/node/app
    expose:
      - "3000"
    ports:
      - "3000:3000"
    command: "npm start"
  backend:
    image: todo-app/backend
    build: ./backend
    volumes:
      - ./backend/:/usr/src/app
    expose:
      - "3001"
    ports:
      - "8001:3001"
    command: "python src/server.py"
    environment:
      - DEBUG=true
    env_file:
      - path: ./.env
        required: true
```

Step 9: Set up Nginx configuration

Create a directory named nginx in the root of your project:

```csharp
mkdir nginx
```

Create a file named nginx.conf inside the nginx directory with the following content:

```python
server {
    listen 80;
    server_name farm_intro;

    location / {
        proxy_pass http://frontend:3000;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location /api {
        proxy_pass http://backend:3001/api;
    }
}
```

This concludes Part 2 of the tutorial, where we implemented the FastAPI server, set up environment variables, created a docker-compose file, and configured Nginx. In the next part, we'll focus on setting up the React frontend for our FARM stack todo application.

# Setting up the React Frontend

Step 10: Create the React application

Navigate to the frontend directory:

```python
cd ../frontend
```

Create a new React application using Create React App:

```python
npx create-react-app .
```

Install additional dependencies:

```python
   npm install axios react-icons
```

Step 11: Set up the main App component

Replace the content of src/App.js with the following:

```javascript
import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";
import ListToDoLists from "./ListTodoLists";
import ToDoList from "./ToDoList";

function App() {
  const [listSummaries, setListSummaries] = useState(null);
  const [selectedItem, setSelectedItem] = useState(null);

  useEffect(() => {
    reloadData().catch(console.error);
  }, []);

  async function reloadData() {
    const response = await axios.get("/api/lists");
    const data = await response.data;
    setListSummaries(data);
  }

  function handleNewToDoList(newName) {
    const updateData = async () => {
      const newListData = {
        name: newName,
      };

      await axios.post(`/api/lists`, newListData);
      reloadData().catch(console.error);
    };
    updateData();
  }

  function handleDeleteToDoList(id) {
    const updateData = async () => {
      await axios.delete(`/api/lists/${id}`);
      reloadData().catch(console.error);
    };
    updateData();
  }

  function handleSelectList(id) {
    console.log("Selecting item", id);
    setSelectedItem(id);
  }

  function backToList() {
    setSelectedItem(null);
    reloadData().catch(console.error);
  }

  if (selectedItem === null) {
    return (
      <div className="App">
        <ListToDoLists
          listSummaries={listSummaries}
          handleSelectList={handleSelectList}
          handleNewToDoList={handleNewToDoList}
          handleDeleteToDoList={handleDeleteToDoList}
        />
      </div>
    );
  } else {
    return (
      <div className="App">
        <ToDoList listId={selectedItem} handleBackButton={backToList} />
      </div>
    );
  }
}

export default App;
```

Step 12: Create the ListTodoLists component

Create a new file src/ListTodoLists.js with the following content:

```javascript
import "./ListTodoLists.css";
import { useRef } from "react";
import { BiSolidTrash } from "react-icons/bi";

function ListToDoLists({
  listSummaries,
  handleSelectList,
  handleNewToDoList,
  handleDeleteToDoList,
}) {
  const labelRef = useRef();

  if (listSummaries === null) {
    return <div className="ListToDoLists loading">Loading to-do lists ...</div>;
  } else if (listSummaries.length === 0) {
    return (
      <div className="ListToDoLists">
        <div className="box">
        <label>
          New To-Do List:&nbsp;
          <input id={labelRef} type="text" />
        </label>
        <button
          onClick={() =>
            handleNewToDoList(document.getElementById(labelRef).value)
          }
        >
          New
        </button>
        </div>
        <p>There are no to-do lists!</p>
      </div>
    );
  }
  return (
    <div className="ListToDoLists">
      <h1>All To-Do Lists</h1>
      <div className="box">
        <label>
          New To-Do List:&nbsp;
          <input id={labelRef} type="text" />
        </label>
        <button
          onClick={() =>
            handleNewToDoList(document.getElementById(labelRef).value)
          }
        >
          New
        </button>
      </div>
      {listSummaries.map((summary) => {
        return (
          <div
            key={summary.id}
            className="summary"
            onClick={() => handleSelectList(summary.id)}
          >
            <span className="name">{summary.name} </span>
            <span className="count">({summary.item_count} items)</span>
            <span className="flex"></span>
            <span
              className="trash"
              onClick={(evt) => {
                evt.stopPropagation();
                handleDeleteToDoList(summary.id);
              }}
            >
              <BiSolidTrash />
            </span>
          </div>
        );
      })}
    </div>
  );
}

export default ListToDoLists;
```

Create a new file src/ListTodoLists.css with the following content:

```css
.ListToDoLists .summary {
    border: 1px solid lightgray;
    padding: 1em;
    margin: 1em;
    cursor: pointer;
    display: flex;
}

.ListToDoLists .count {
    padding-left: 1ex;
    color: blueviolet;
    font-size: 92%;
}
```

Step 13: Create the ToDoList component

Create a new file src/ToDoList.js with the following content:

```javascript
import "./ToDoList.css";
import { useEffect, useState, useRef } from "react";
import axios from "axios";
import { BiSolidTrash } from "react-icons/bi";

function ToDoList({ listId, handleBackButton }) {
  let labelRef = useRef();
  const [listData, setListData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get(`/api/lists/${listId}`);
      const newData = await response.data;
      setListData(newData);
    };
    fetchData();
  }, [listId]);

  function handleCreateItem(label) {
    const updateData = async () => {
      const response = await axios.post(`/api/lists/${listData.id}/items/`, {
        label: label,
      });
      setListData(await response.data);
    };
    updateData();
  }

  function handleDeleteItem(id) {
    const updateData = async () => {
      const response = await axios.delete(
        `/api/lists/${listData.id}/items/${id}`
      );
      setListData(await response.data);
    };
    updateData();
  }

  function handleCheckToggle(itemId, newState) {
    const updateData = async () => {
      const response = await axios.patch(
        `/api/lists/${listData.id}/checked_state`,
        {
          item_id: itemId,
          checked_state: newState,
        }
      );
      setListData(await response.data);
    };
    updateData();
  }

  if (listData === null) {
    return (
      <div className="ToDoList loading">
        <button className="back" onClick={handleBackButton}>
          Back
        </button>
        Loading to-do list ...
      </div>
    );
  }
  return (
    <div className="ToDoList">
      <button className="back" onClick={handleBackButton}>
        Back
      </button>
      <h1>List: {listData.name}</h1>
      <div className="box">
        <label>
          New Item:&nbsp;
          <input id={labelRef} type="text" />
        </label>
        <button
          onClick={() =>
            handleCreateItem(document.getElementById(labelRef).value)
          }
        >
          New
        </button>
      </div>
      {listData.items.length > 0 ? (
        listData.items.map((item) => {
          return (
            <div
              key={item.id}
              className={item.checked ? "item checked" : "item"}
              onClick={() => handleCheckToggle(item.id, !item.checked)}
            >
              <span>{item.checked ? "✅" : "⬜️"} </span>
              <span className="label">{item.label} </span>
              <span className="flex"></span>
              <span
                className="trash"
                onClick={(evt) => {
                  evt.stopPropagation();
                  handleDeleteItem(item.id);
                }}
              >
                <BiSolidTrash />
              </span>
            </div>
          );
        })
      ) : (
        <div className="box">There are currently no items.</div>
      )}
    </div>
  );
}

export default ToDoList;
```

Create a new file src/ToDoList.css with the following content:

```css
.ToDoList .back {
    margin: 0 1em;
    padding: 1em;
    float: left;
}

.ToDoList .item {
    border: 1px solid lightgray;
    padding: 1em;
    margin: 1em;
    cursor: pointer;
    display: flex;
}

.ToDoList .label {
    margin-left: 1ex;
}

.ToDoList .checked .label {
    text-decoration: line-through;
    color: lightgray;
}
```

Step 14: Update the main CSS file

Replace the content of src/index.css with the following:

```css
html, body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 12pt;
}

input, button {
  font-size: 1em;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}

.box {
    border: 1px solid lightgray;
    padding: 1em;
    margin: 1em;
}

.flex {
  flex: 1;
}
```

This concludes Part 3 of the tutorial, where we set up the React frontend for our FARM stack todo application. We've created the main App component, the ListTodoLists component for displaying all todo lists, and the ToDoList component for individual todo lists. In the next part, we'll focus on running and testing the application.

# Running and Testing the Application

Step 18: Run the application using Docker Compose

1. Make sure you have Docker and Docker Compose installed on your system
    
2. Open a terminal in the root directory of your project (farm-stack-todo)
    
3. Build and start the containers:
    

```python
docker-compose up --build
```

4. Once the containers are up and running, open your web browser and go to [http://localhost:8000](http://localhost:8000/)
    

Step 19: Stopping the application

1. If you're running the application without Docker:
    
    * Stop the React development server by pressing Ctrl+C in its terminal
        
    * Stop the FastAPI server by pressing Ctrl+C in its terminal
        
    * Stop the MongoDB server by pressing Ctrl+C in its terminal
        
2. If you're running the application with Docker Compose:
    
    * Press Ctrl+C in the terminal where you ran docker-compose up
        
    * Run the following command to stop and remove the containers:
        

```python
     docker-compose down
     ```
```

Congratulations! You have successfully built and tested a FARM stack todo application. This application demonstrates the integration of FastAPI, React, and MongoDB in a full-stack web application.

Here are some potential next steps to enhance your application:

1. Add user authentication and authorization
    
2. Implement data validation and error handling
    
3. Add more features like due dates, priorities, or categories for todo items
    
4. Improve the UI/UX with a more polished design
    
5. Write unit and integration tests for both frontend and backend
    
6. Set up continuous integration and deployment (CI/CD) for your application
    

Remember to keep your dependencies updated and follow best practices for security and performance as you continue to develop your application.

# Conclusion and Next Steps

Congratulations on completing this comprehensive FARM stack tutorial! By building this todo application, you've gained hands-on experience with some of the most powerful and popular technologies in modern web development. You've learned how to create a robust backend API with FastAPI, build a dynamic and responsive frontend with React, persist data with MongoDB, and containerize your entire application using Docker. This project has demonstrated how these technologies work together seamlessly to create a full-featured, scalable web application.
