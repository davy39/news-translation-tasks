---
title: Utiliser la FARM Stack pour développer des applications Full Stack
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
seo_title: Utiliser la FARM Stack pour développer des applications Full Stack
seo_desc: 'The FARM stack is a modern web development stack that combines three powerful
  technologies: FastAPI, React, and MongoDB. This full-stack solution provides developers
  with a robust set of tools to build scalable, efficient, and high-performance web
  ap...'
---

La FARM stack est une stack de développement web moderne qui combine trois technologies puissantes : FastAPI, React et MongoDB. Cette solution Full Stack offre aux développeurs un ensemble d'outils robustes pour créer des applications web évolutives, efficaces et performantes.

Dans cet article, je vais vous présenter chacune des technologies clés, puis nous construirons un projet en utilisant la FARM stack et Docker afin que vous puissiez voir comment tout fonctionne ensemble.

Cet article est basé sur un cours que j'ai créé [sur la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=PWG7NlUDVaA). Regardez-le ici :

%[https://www.youtube.com/watch?v=PWG7NlUDVaA] 

# Introduction à la FARM Stack

Le terme FARM dans FARM stack signifie :

* F : FastAPI (Backend)
    
* R : React (Frontend)
    
* M : MongoDB (Base de données)
    

La FARM stack est conçue pour exploiter les points forts de chaque composant, permettant aux développeurs de créer des applications riches en fonctionnalités avec une expérience de développement fluide.

### Composants de la FARM Stack

1. **FastAPI :** FastAPI est un Framework web Python moderne et performant pour la création d'API. Il est conçu pour être facile à utiliser, rapide à coder et prêt pour les environnements de production. FastAPI est construit au-dessus de Starlette pour les parties web et Pydantic pour les parties de données, ce qui en fait un choix puissant pour construire des services backend robustes.
    
2. **React** : React est une bibliothèque JavaScript populaire pour la création d'interfaces utilisateur. Développée et maintenue par Facebook, React permet aux développeurs de créer des composants UI réutilisables qui se mettent à jour et s'affichent efficacement à mesure que les données changent. Son architecture basée sur les composants et son DOM virtuel en font un excellent choix pour construire des applications frontend dynamiques et réactives.
    
3. **MongoDB :** MongoDB est une base de données NoSQL orientée document. Elle stocke les données dans des documents flexibles de type JSON, ce qui signifie que les champs peuvent varier d'un document à l'autre et que la structure des données peut être modifiée au fil du temps. Cette flexibilité fait de MongoDB un choix idéal pour les applications qui doivent évoluer rapidement et gérer divers types de données.
    

### Avantages de l'utilisation de la FARM Stack

1. Haute Performance : FastAPI est l'un des Frameworks Python les plus rapides disponibles, tandis que le DOM virtuel de React assure des mises à jour efficaces de l'UI. Le modèle de document de MongoDB permet des lectures et écritures rapides.
    
2. Évolutivité : Tous les composants de la FARM stack sont conçus pour évoluer. FastAPI peut gérer efficacement les requêtes simultanées, les applications React peuvent gérer des interfaces utilisateur complexes et MongoDB peut distribuer les données sur plusieurs serveurs.
    
3. Communauté et Écosystème : Les trois technologies disposent de grandes communautés actives et de riches écosystèmes de bibliothèques et d'outils.
    
4. Flexibilité : La FARM stack est suffisamment flexible pour s'adapter à divers types d'applications web, des simples applications CRUD aux systèmes complexes et gourmands en données.
    

En combinant ces technologies, la FARM stack fournit une solution complète pour construire des applications web modernes. Elle permet aux développeurs de créer des backends rapides et évolutifs avec FastAPI, des frontends intuitifs et réactifs avec React, et un stockage de données flexible et efficace avec MongoDB. Cette stack est particulièrement adaptée aux applications nécessitant des mises à jour en temps réel, des modèles de données complexes et une haute performance.

# Aperçu du projet : Application de liste de tâches

Dans le cours vidéo, je détaille davantage chaque technologie individuelle de la FARM Stack. Mais dans cet article, nous allons passer directement à un projet pour tout mettre en pratique.

Nous allons créer une application de liste de tâches (todo application) pour nous aider à comprendre la FARM stack. Avant de commencer à créer l'application, discutons davantage des fonctionnalités et de l'architecture logicielle.

### Fonctionnalités de l'application de liste de tâches

Notre application de liste de tâches FARM stack comprendra les fonctionnalités suivantes :

1. Listes de tâches multiples :
    
    * Les utilisateurs peuvent créer, consulter, mettre à jour et supprimer plusieurs listes de tâches.
        
    * Chaque liste a un nom et contient plusieurs éléments de tâche.
        
2. Éléments de tâche :
    
    * Dans chaque liste, les utilisateurs peuvent ajouter, consulter, mettre à jour et supprimer des éléments de tâche.
        
    * Chaque élément possède un libellé, un état coché/décoché et appartient à une liste spécifique.
        
3. Mises à jour en temps réel :
    
    * L'UI se met à jour en temps réel lorsque des modifications sont apportées aux listes ou aux éléments.
        
4. Design réactif (Responsive) :
    
    * L'application sera réactive et fonctionnera bien sur les ordinateurs de bureau et les appareils mobiles.
        

### Architecture du système

Notre application de liste de tâches suivra une architecture FARM stack typique :

1. Frontend (React) :
    
    * Fournit l'interface utilisateur pour interagir avec les listes et les éléments de tâches.
        
    * Communique avec le backend via des appels d'API RESTful.
        
2. Backend (FastAPI) :
    
    * Gère les requêtes API provenant du frontend.
        
    * Implémente la logique métier pour la gestion des listes et des éléments de tâches.
        
    * Interagit avec la base de données MongoDB pour la persistance des données.
        
3. Base de données (MongoDB) :
    
    * Stocke les listes et les éléments de tâches.
        
    * Permet l'interrogation et la mise à jour efficaces des données de tâches.
        
4. Docker :
    
    * Conteneurise chaque composant (frontend, backend, base de données) pour faciliter le développement et le déploiement.
        

### Conception du modèle de données

Notre modèle de données MongoDB consistera en deux structures principales :

1. Liste de tâches (Todo List) :
    

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

2. Résumé de la liste (pour l'affichage dans la liste de toutes les listes de tâches) :
    

```json
   {
     "_id": ObjectId,
     "name": String,
     "item_count": Integer
   }
```

### Conception des points de terminaison API

Notre backend FastAPI exposera les points de terminaison RESTful suivants :

1. Listes de tâches :
    
    * GET /api/lists : Récupérer toutes les listes de tâches (vue résumée)
        
    * POST /api/lists : Créer une nouvelle liste de tâches
        
    * GET /api/lists/{list\_id} : Récupérer une liste de tâches spécifique avec tous ses éléments
        
    * DELETE /api/lists/{list\_id} : Supprimer une liste de tâches spécifique
        
2. Éléments de tâche :
    
    * POST /api/lists/{list\_id}/items : Ajouter un nouvel élément à une liste spécifique
        
    * PATCH /api/lists/{list\_id}/checked\_state : Mettre à jour l'état coché d'un élément
        
    * DELETE /api/lists/{list\_id}/items/{item\_id} : Supprimer un élément spécifique d'une liste
        

Ce projet fournira une base solide pour le développement avec la FARM stack et la conteneurisation Docker, que vous pourrez ensuite étendre pour des applications plus complexes à l'avenir.

Commençons donc le projet.

# Tutoriel du projet

## Configuration du projet et développement du backend

Étape 1 : Configurer la structure du projet

Créez un nouveau répertoire pour votre projet :

```csharp
   mkdir farm-stack-todo
   cd farm-stack-todo
```

Créez des sous-répertoires pour le backend et le frontend :

```csharp
   mkdir backend frontend
```

Étape 2 : Configurer l'environnement backend

Naviguez vers le répertoire backend :

```csharp
   cd backend
```

Créez un environnement virtuel et activez-le :

```csharp
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez : venv\\Scripts\\activate
```

Créez les fichiers suivants dans le répertoire backend :

3. * Dockerfile
        
    * pyproject.toml
        
    
    Dans votre terminal, installez les paquets requis :
    

```powershell
pip install "fastapi[all]" "motor[srv]" beanie aiostream
```

Générez le fichier requirements.txt :

```powershell
pip freeze > requirements.txt
```

Après avoir créé le fichier requirements.txt (soit via pip-compile ou manuellement), vous pouvez installer les dépendances en utilisant :

```csharp
   pip install -r requirements.txt
```

Ajoutez le contenu suivant au Dockerfile :

```csharp
   FROM python:3

   WORKDIR /usr/src/app
   COPY requirements.txt ./

   RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

   EXPOSE 3001

   CMD [ "python", "./src/server.py" ]
```

Ajoutez le contenu suivant à pyproject.toml :

```csharp
   [tool.pytest.ini_options]
   pythonpath = "src"
```

Étape 4 : Configurer la structure du backend

Créez un répertoire src à l'intérieur du répertoire backend :

```csharp
   mkdir src
```

Créez les fichiers suivants à l'intérieur du répertoire src :

2. * [server.py](http://server.py)
        
    * [dal.py](http://dal.py)
        

Étape 5 : Implémenter la couche d'accès aux données (DAL)

Ouvrez src/[dal.py](http://dal.py) et ajoutez le contenu suivant :

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

Ceci conclut la partie 1 du tutoriel, où nous avons configuré la structure du projet et implémenté la couche d'accès aux données pour notre application de liste de tâches FARM stack. Dans la partie suivante, nous implémenterons le serveur FastAPI et créerons les points de terminaison de l'API.

## Implémentation du serveur FastAPI

Étape 6 : Implémenter le serveur FastAPI

Ouvrez src/[server.py](http://server.py) et ajoutez le contenu suivant :

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
    # Démarrage :
    client = AsyncIOMotorClient(MONGODB_URI)
    database = client.get_default_database()

    # S'assurer que la base de données est disponible :
    pong = await database.command("ping")
    if int(pong["ok"]) != 1:
        raise Exception("La connexion au cluster n'est pas correcte !")

    todo_lists = database.get_collection(COLLECTION_NAME)
    app.todo_dal = ToDoDAL(todo_lists)

    # Retour à l'Application FastAPI :
    yield

    # Arrêt :
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
    """Récupérer une seule liste de tâches"""
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

Cette implémentation configure le serveur FastAPI avec le middleware CORS, se connecte à MongoDB et définit les points de terminaison de l'API pour notre application de liste de tâches.

Étape 7 : Configurer les variables d'environnement

Créez un fichier .env dans le répertoire racine avec le contenu suivant. Assurez-vous d'ajouter le nom de la base de données ("todo") à la fin de ".mongodb.net/".

```csharp
MONGODB_URI='mongodb+srv://beau:codecamp@cluster0.ji7hu.mongodb.net/todo?retryWrites=true&w=majority&appName=Cluster0'
```

Étape 8 : Créer un fichier docker-compose

Dans le répertoire racine de votre projet (farm-stack-todo), créez un fichier nommé compose.yml avec le contenu suivant :

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

Étape 9 : Configurer la configuration Nginx

Créez un répertoire nommé nginx à la racine de votre projet :

```csharp
mkdir nginx
```

Créez un fichier nommé nginx.conf à l'intérieur du répertoire nginx avec le contenu suivant :

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

Ceci conclut la partie 2 du tutoriel, où nous avons implémenté le serveur FastAPI, configuré les variables d'environnement, créé un fichier docker-compose et configuré Nginx. Dans la partie suivante, nous nous concentrerons sur la mise en place du frontend React pour notre application de liste de tâches FARM stack.

# Configuration du frontend React

Étape 10 : Créer l'application React

Naviguez vers le répertoire frontend :

```python
cd ../frontend
```

Créez une nouvelle application React en utilisant Create React App :

```python
npx create-react-app .
```

Installez les dépendances supplémentaires :

```python
   npm install axios react-icons
```

Étape 11 : Configurer le composant App principal

Remplacez le contenu de src/App.js par ce qui suit :

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
    console.log("Sélection de l'élément", id);
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

Étape 12 : Créer le composant ListTodoLists

Créez un nouveau fichier src/ListTodoLists.js avec le contenu suivant :

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
    return <div className="ListToDoLists loading">Chargement des listes de tâches...</div>;
  } else if (listSummaries.length === 0) {
    return (
      <div className="ListToDoLists">
        <div className="box">
        <label>
          Nouvelle liste de tâches :&nbsp;
          <input id={labelRef} type="text" />
        </label>
        <button
          onClick={() =>
            handleNewToDoList(document.getElementById(labelRef).value)
          }
        >
          Nouveau
        </button>
        </div>
        <p>Il n'y a pas de listes de tâches !</p>
      </div>
    );
  }
  return (
    <div className="ListToDoLists">
      <h1>Toutes les listes de tâches</h1>
      <div className="box">
        <label>
          Nouvelle liste de tâches :&nbsp;
          <input id={labelRef} type="text" />
        </label>
        <button
          onClick={() =>
            handleNewToDoList(document.getElementById(labelRef).value)
          }
        >
          Nouveau
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
            <span className="count">({summary.item_count} éléments)</span>
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

Créez un nouveau fichier src/ListTodoLists.css avec le contenu suivant :

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

Étape 13 : Créer le composant ToDoList

Créez un nouveau fichier src/ToDoList.js avec le contenu suivant :

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
          Retour
        </button>
        Chargement de la liste de tâches...
      </div>
    );
  }
  return (
    <div className="ToDoList">
      <button className="back" onClick={handleBackButton}>
        Retour
      </button>
      <h1>Liste : {listData.name}</h1>
      <div className="box">
        <label>
          Nouvel élément :&nbsp;
          <input id={labelRef} type="text" />
        </label>
        <button
          onClick={() =>
            handleCreateItem(document.getElementById(labelRef).value)
          }
        >
          Nouveau
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
              <span>{item.checked ? "✅" : "⬜"} </span>
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
        <div className="box">Il n'y a actuellement aucun élément.</div>
      )}
    </div>
  );
}

export default ToDoList;
```

Créez un nouveau fichier src/ToDoList.css avec le contenu suivant :

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

Étape 14 : Mettre à jour le fichier CSS principal

Remplacez le contenu de src/index.css par ce qui suit :

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

Ceci conclut la partie 3 du tutoriel, où nous avons mis en place le frontend React pour notre application de liste de tâches FARM stack. Nous avons créé le composant App principal, le composant ListTodoLists pour afficher toutes les listes de tâches, et le composant ToDoList pour les listes de tâches individuelles. Dans la partie suivante, nous nous concentrerons sur l'exécution et le test de l'application.

# Exécution et test de l'application

Étape 18 : Exécuter l'application avec Docker Compose

1. Assurez-vous d'avoir Docker et Docker Compose installés sur votre système.
    
2. Ouvrez un terminal dans le répertoire racine de votre projet (farm-stack-todo).
    
3. Construisez et démarrez les conteneurs :
    

```python
docker-compose up --build
```

4. Une fois les conteneurs opérationnels, ouvrez votre navigateur web et allez sur [http://localhost:8000](http://localhost:8000/)
    

Étape 19 : Arrêter l'application

1. Si vous exécutez l'application sans Docker :
    
    * Arrêtez le serveur de développement React en appuyant sur Ctrl+C dans son terminal.
        
    * Arrêtez le serveur FastAPI en appuyant sur Ctrl+C dans son terminal.
        
    * Arrêtez le serveur MongoDB en appuyant sur Ctrl+C dans son terminal.
        
2. Si vous exécutez l'application avec Docker Compose :
    
    * Appuyez sur Ctrl+C dans le terminal où vous avez lancé docker-compose up.
        
    * Exécutez la commande suivante pour arrêter et supprimer les conteneurs :
        

```python
     docker-compose down
     ```

Félicitations ! Vous avez construit et testé avec succès une application de liste de tâches avec la FARM stack. Cette application démontre l'intégration de FastAPI, React et MongoDB dans une application web Full Stack.

Voici quelques prochaines étapes potentielles pour améliorer votre application :

1. Ajouter l'authentification et l'autorisation des utilisateurs.
    
2. Implémenter la validation des données et la gestion des erreurs.
    
3. Ajouter plus de fonctionnalités comme des dates d'échéance, des priorités ou des catégories pour les tâches.
    
4. Améliorer l'UI/UX avec un design plus raffiné.
    
5. Écrire des tests unitaires et d'intégration pour le frontend et le backend.
    
6. Mettre en place l'intégration et le déploiement continus (CI/CD) pour votre application.
    

N'oubliez pas de maintenir vos dépendances à jour et de suivre les meilleures pratiques en matière de sécurité et de performance au fur et à mesure que vous continuez à développer votre application.

# Conclusion et prochaines étapes

Félicitations pour avoir terminé ce tutoriel complet sur la FARM stack ! En construisant cette application de liste de tâches, vous avez acquis une expérience pratique avec certaines des technologies les plus puissantes et populaires du développement web moderne. Vous avez appris à créer une API backend robuste avec FastAPI, à construire un frontend dynamique et réactif avec React, à assurer la persistance des données avec MongoDB et à conteneuriser l'ensemble de votre application avec Docker. Ce projet a démontré comment ces technologies fonctionnent ensemble de manière transparente pour créer une application web complète et évolutive.