---
title: Comment créer une application CRUD en utilisant React et Convex
subtitle: ''
author: Sanjay
co_authors: []
series: null
date: '2024-10-24T14:52:06.527Z'
originalURL: https://freecodecamp.org/news/build-crud-app-react-and-convex
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729397399755/9c747607-fa82-4caf-9c20-8e64ec82c3f2.jpeg
tags:
- name: React
  slug: reactjs
- name: crud
  slug: crud
seo_title: Comment créer une application CRUD en utilisant React et Convex
seo_desc: Learn to build a CRUD app with React and Convex, simplifying backend development
  using real-time databases and efficient data operations
---

Les opérations CRUD sont la base de toute application, il est donc essentiel de les maîtriser lors de l'apprentissage de nouvelles technologies.

Dans ce tutoriel, vous apprendrez à créer une application CRUD en utilisant React et Convex. Nous aborderons ces opérations en construisant un projet appelé Collections de Livres. Dans ce projet, les utilisateurs pourront ajouter des livres et mettre à jour leur statut une fois qu'ils ont terminé un livre.

## Table des Matières

* [Qu'est-ce que Convex ?](#heading-quest-ce-que-convex)
    
* [Comment installer votre projet](#heading-comment-installer-votre-projet)
    
* [Comment créer le schéma](#heading-comment-creer-le-schema)
    
* [Comment créer l'interface utilisateur](#heading-comment-creer-linterface-utilisateur)
    
* [Comment créer les fonctions CRUD](#heading-comment-creer-les-fonctions-crud)
    
* [Stylisation](#heading-stylisation)
    
* [Résumé](#heading-resume)
    

## Qu'est-ce que Convex ?

Convex est la plateforme Baas qui simplifie le développement backend. Convex est livré avec une base de données en temps réel, et vous n'avez pas besoin de vous soucier de l'écriture de la logique côté serveur séparément car il fournit des méthodes pour interroger et mutuer la base de données.

### Prérequis

Pour suivre ce tutoriel, vous devez connaître les fondamentaux de React. J'utiliserai TypeScript dans ce projet, mais c'est optionnel, donc vous pouvez également suivre avec JavaScript.

## Comment installer votre projet

Créez un dossier séparé pour le projet et nommez-le comme vous le souhaitez – je nommerai le mien **Books**. Nous installerons Convex et React dans ce dossier.

Vous pouvez créer une application React en utilisant cette commande :

```bash
npm create vite@latest my-app -- --template react-ts
```

Si vous souhaitez travailler avec JavaScript, supprimez le `ts` à la fin. C'est-à-dire :

```bash
npm create vite@latest my-app -- --template react
```

### Comment installer Convex

Nous devons installer Convex dans le même dossier. Vous pouvez le faire en utilisant cette commande :

```bash
npm install convex
```

Ensuite, exécutez `npx convex dev`. Si vous faites cela pour la première fois, il devrait vous demander une authentification. Sinon, il devrait demander le nom du projet.

Vous pouvez visiter le [tableau de bord Convex](https://www.convex.dev/) pour voir le projet que vous avez créé.

Maintenant que nous avons installé Convex et l'application React, nous devons connecter le backend Convex à l'application React.

Dans le fichier **src/main.tsx**, enveloppez votre composant `App` avec le `ConvexReactClient` :

```typescript
import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import { ConvexProvider, ConvexReactClient } from "convex/react";
import "./index.css"

const convex = new ConvexReactClient(import.meta.env.VITE_CONVEX_URL as string);

createRoot(document.getElementById("root")!).render(
  <ConvexProvider client={convex}>
    <App />
  </ConvexProvider>
);
```

Lorsque vous avez installé Convex, un fichier `.env.local` a été créé. Vous pouvez voir l'URL de votre backend dans ce fichier.

Dans la ligne ci-dessous, nous avons instancié le client React Convex avec l'URL.

```typescript
const convex = new ConvexReactClient(import.meta.env.VITE_CONVEX_URL as string); 
```

## Comment créer le schéma

Dans votre répertoire principal de projet, vous devriez voir le répertoire **convex**. Nous gérerons les requêtes et mutations de la base de données ici.

Créez un fichier **schema.ts** dans le dossier **convex** :

```typescript
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  books: defineTable({
    title: v.string(),
    author: v.string(),
    isCompleted: v.boolean(),
  }),
});
```

Vous pouvez définir un schéma pour votre document avec `defineSchema` et créer une table avec `defineTable`. Convex fournit ces fonctions pour définir un schéma et créer une table.

`v` est le validateur de type, il est utilisé pour fournir des types pour chaque donnée que nous ajoutons à la table.

Pour ce projet, comme il s'agit d'une application de collection de livres, la structure aura `title`, `author` et `isCompleted`. Vous pouvez ajouter plus de champs.

Maintenant que vous avez défini votre schéma, configurons l'interface utilisateur de base dans React.

## Comment créer l'interface utilisateur

Dans le dossier **src**, créez un dossier appelé **component** et un fichier **Home.tsx**. Ici, vous pouvez définir l'interface utilisateur.

```typescript
import { useState } from "react";
import "../styles/home.css";

const Home = () => {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  return (
    <div className="main-container">
      <h1>Collections de Livres</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="titre du livre"
        />
        <br />
        <input
          type="text"
          name="author"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          placeholder="auteur du livre"
        />
        <br />
        <input type="submit" />
      </form>
      {books ? <Books books={books} /> : "Chargement..."}
    </div>
  );
};

export default Home;
```

Vous pouvez créer votre composant comme vous le souhaitez. J'ai ajouté deux champs de saisie `title`, `author` et un bouton `submit`. C'est la structure de base. Maintenant, nous pouvons créer des méthodes CRUD dans le backend.

## Comment créer des fonctions CRUD

Dans le dossier **convex**, vous pouvez créer un fichier **queries.ts** séparé pour les fonctions CRUD.

### Fonction de création

Dans **convex/queries.ts** :

Vous pouvez définir une fonction `createBooks`. Vous pouvez utiliser la fonction `mutation` de Convex pour créer, mettre à jour et supprimer des données. La lecture des données relèvera de `query`.

La fonction `mutation` attend ces arguments :

* `args` : les données que nous devons stocker dans la base de données.
    
* `handler` : gère la logique pour stocker la date dans la base de données. Le `handler` est une fonction asynchrone, et il a deux arguments : `ctx` et `args`. Ici, `ctx` est l'objet contexte que nous utiliserons pour gérer les opérations de la base de données.
    

Vous utiliserez la méthode `insert` pour insérer de nouvelles données. Le premier paramètre dans `insert` est le nom de la table et le second est les données qui doivent être insérées.

Enfin, vous pouvez retourner les données de la base de données.

Voici le code :

```typescript
import { mutation} from "./_generated/server";
import { v } from "convex/values";

export const createBooks = mutation({
  args: { title: v.string(), author: v.string() },
  handler: async (ctx, args) => {
    const newBookId = await ctx.db.insert("books", {
      title: args.title,
      author: args.author,
      isCompleted: false,
    });
    return newBookId;
  },
});
```

### Fonction de lecture

Dans **convex/queries.ts** :

```typescript
import { query } from "./_generated/server";
import { v } from "convex/values";

//lecture
export const getBooks = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("books").collect();
  },
});
```

Dans cette opération de lecture, nous avons utilisé la fonction intégrée `query` de Convex. Ici, `args` sera vide puisque nous ne recevons aucune donnée de l'utilisateur. De même, la fonction `handler` est asynchrone et utilise l'objet `ctx` pour interroger la base de données et retourner les données.

### Fonction de mise à jour

Dans **convex/queries.ts** :

Créez une fonction `updateStatus`. Nous allons uniquement mettre à jour le statut `isCompleted`.

Ici, vous devez obtenir l'ID du document et le statut de l'utilisateur. Dans `args`, nous définirons `id` et `isCompleted`, qui proviendront de l'utilisateur.

Dans le `handler`, nous utiliserons la méthode `patch` pour mettre à jour les données. La méthode `patch` attend deux arguments : le premier argument est l'`id` du document et le second est les données mises à jour.

```typescript
import { mutation } from "./_generated/server";
import { v } from "convex/values";

//mise à jour
export const updateStatus = mutation({
  args: { id: v.id("books"), isCompleted: v.boolean() },
  handler: async (ctx, args) => {
    const { id } = args;
    await ctx.db.patch(id, { isCompleted: args.isCompleted });
    return "mis à jour"
  },
});
```

### Fonction de suppression

Dans **convex/queries.ts** :

Créez une fonction `deleteBooks` et utilisez la fonction `mutation`. Nous aurons besoin de l'ID du document à supprimer. Dans `args`, définissez un ID. Dans le `handler`, utilisez la méthode `delete` de l'objet `ctx` et passez l'ID. Cela supprimera le document.

```typescript
import { mutation } from "./_generated/server";
import { v } from "convex/values";

//suppression
export const deleteBooks = mutation({
  args: { id: v.id("books") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
    return "supprimé";
  },
});
```

Pour l'instant, vous avez terminé les fonctions CRUD dans le backend. Maintenant, nous devons les faire fonctionner dans l'interface utilisateur. Revenons à React.

### Mettre à jour l'interface utilisateur

Vous avez déjà créé une interface utilisateur de base dans l'application React, avec quelques champs de saisie. Mettons-la à jour.

Dans **src/component/Home.tsx** :

```typescript
import { useQuery, useMutation } from "convex/react";
import { api } from "../../convex/_generated/api";
import { Books } from "./Books";
import { useState } from "react";
import "../styles/home.css";

const Home = () => {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const books = useQuery(api.queries.getBooks);
  const createBooks = useMutation(api.queries.createBooks);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>): void => {
    e.preventDefault();
    createBooks({ title, author })
      .then(() => {
        console.log("créé");
        setTitle("");
        setAuthor("");
      })
      .catch((err) => console.log(err));
  };
  return (
    <div className="main-container">
      <h1>Collections de Livres</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="titre du livre"
        />
        <br />
        <input
          type="text"
          name="author"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          placeholder="auteur du livre"
        />
        <br />
        <input type="submit" />
      </form>
      {books ? <Books books={books} /> : "Chargement..."}
    </div>
  );
};

export default Home;
```

Nous pouvons maintenant utiliser les fonctions API backend en utilisant `api` de Convex. Comme vous pouvez le voir, nous avons appelé deux fonctions API : vous pouvez utiliser `useQuery` si vous allez lire des données et `useMutation` si vous voulez changer des données. Maintenant dans ce fichier, nous faisons deux opérations qui sont créer et lire.

Nous avons obtenu toutes les données en utilisant cette méthode :

```javascript
 const books = useQuery(api.queries.getBooks);
```

Le tableau d'objets sera stocké dans la variable books.

Nous avons obtenu la fonction de création du backend avec cette ligne de code :

```javascript
const createBooks = useMutation(api.queries.createBooks);
```

### Comment utiliser la fonction de création dans l'interface utilisateur

Utilisons la fonction de création dans l'interface utilisateur.

Puisque les champs de saisie sont dans la balise `form`, nous utiliserons l'attribut `onSubmit` pour gérer la soumission du formulaire.

```typescript
//Dans le Home.tsx
 
const handleSubmit = (e: React.FormEvent<HTMLFormElement>): void => {
    e.preventDefault();
    createBooks({ title, author })
      .then(() => {
        console.log("créé");
        setTitle("");
        setAuthor("");
      })
      .catch((err) => console.log(err));
  };
```

Lorsque vous cliquez sur submit, cela déclenche la fonction `handleSubmit`.

Nous avons utilisé `createBooks` pour passer le `title` et `author` de l'état. La fonction d'extrémité est asynchrone, donc nous pouvons utiliser `handleSubmit` comme asynchrone ou utiliser `.then`. J'ai utilisé la méthode `.then` pour gérer les données asynchrones.

Vous pouvez créer un composant séparé pour afficher les données récupérées de la base de données. Les données retournées sont dans **Home.tsx**, donc nous passerons les données au composant **Books.tsx** en tant que props.

Dans **Books.tsx** :

```typescript
import { useState } from "react";
import { book } from "../types/book.type";
import { useMutation } from "convex/react";
import { api } from "../../convex/_generated/api";
import { Id } from "../../convex/_generated/dataModel";
import "../styles/book.css";

export const Books = ({ books }: { books: book[] }) => {
  const [update, setUpdate] = useState(false);
  const [id, setId] = useState("");

  const deleteBooks = useMutation(api.queries.deleteBooks);
  const updateStatus = useMutation(api.queries.updateStatus);

  const handleClick = (id: string) => {
    setId(id);
    setUpdate(!update);
  };

  const handleDelete = (id: string) => {
    deleteBooks({ id: id as Id<"books"> })
      .then((mess) => console.log(mess))
      .catch((err) => console.log(err));
  };

  const handleUpdate = (e: React.FormEvent<HTMLFormElement>, id: string) => {
    e.preventDefault();
    const formdata = new FormData(e.currentTarget);
    const isCompleted: boolean =
      (formdata.get("completed") as string) === "true";
    updateStatus({ id: id as Id<"books">, isCompleted })
      .then((mess) => console.log(mess))
      .catch((err) => console.log(err));
    setUpdate(false);
  };

  return (
    <div>
      {books.map((data: book, index: number) => {
        return (
          <div
            key={data._id}
            className={`book-container ${data.isCompleted ? "completed" : "not-completed"}`}
          >
            <h3>Livre n° : {index + 1}</h3>
            <p>Titre du livre : {data.title}</p>
            <p>Auteur du livre : {data.author}</p>
            <p>
              Statut de complétion :{" "}
              {data.isCompleted ? "Complété" : "Non complété"}
            </p>
            <button onClick={() => handleClick(data._id)}>Mettre à jour</button>
            {id === data._id && update && (
              <>
                <form onSubmit={(e) => handleUpdate(e, data._id)}>
                  <select name="completed">
                    <option value="true">Complété</option>
                    <option value="false">Non complété</option>
                  </select>
                  <input type="submit" />
                </form>
              </>
            )}
            <button onClick={() => handleDelete(data._id)}>Supprimer</button>
          </div>
        );
      })}
    </div>
  );
};
```

Dans le composant **Books.jsx**, vous pouvez afficher les données de la base de données et gérer la fonctionnalité pour mettre à jour et supprimer les enregistrements.

Parcourons chacune de ces fonctionnalités étape par étape.

### Comment afficher les données

Vous pouvez obtenir les données passées en tant que prop dans le composant `Home.tsx`. Si vous utilisez TypeScript, j'ai défini un type pour l'objet qui est retourné par la requête. Vous pouvez ignorer cela si vous utilisez JavaScript.

Créez **books.types.ts** :

```typescript
export type book = {
    _id: string,
    title: string,
    author: string,
    isCompleted: boolean
}
```

Vous pouvez utiliser la fonction `map` pour afficher les données.

```typescript
import { useState } from "react";
import { book } from "../types/book.type";
import { useMutation } from "convex/react";
import { api } from "../../convex/_generated/api";
import { Id } from "../../convex/_generated/dataModel";
import "../styles/book.css";

export const Books = ({ books }: { books: book[] }) => {
  const [update, setUpdate] = useState(false);
  
  return (
    <div>
      {books.map((data: book, index: number) => {
        return (
          <div
            key={data._id}
            className={`book-container ${data.isCompleted ? "completed" : "not-completed"}`}
          >
            <h3>Livre n° : {index + 1}</h3>
            <p>Titre du livre : {data.title}</p>
            <p>Auteur du livre : {data.author}</p>
            <p>
              Statut de complétion :{" "}
              {data.isCompleted ? "Complété" : "Non complété"}
            </p>
            <button onClick={() => handleClick(data._id)}>Mettre à jour</button>
            {id === data._id && update && (
              <>
                <form onSubmit={(e) => handleUpdate(e, data._id)}>
                  <select name="completed">
                    <option value="true">Complété</option>
                    <option value="false">Non complété</option>
                  </select>
                  <input type="submit" />
                </form>
              </>
            )}
            <button onClick={() => handleDelete(data._id)}>Supprimer</button>
          </div>
        );
      })}
    </div>
  );
};
```

C'est la structure de base. Nous avons affiché le titre, l'auteur et le statut, ainsi qu'un bouton de mise à jour et de suppression.

Maintenant, ajoutons les fonctionnalités.

```typescript
import { useState } from "react";
import { book } from "../types/book.type";
import { useMutation } from "convex/react";
import { api } from "../../convex/_generated/api";
import { Id } from "../../convex/_generated/dataModel";
import "../styles/book.css";

export const Books = ({ books }: { books: book[] }) => {
  const [update, setUpdate] = useState(false);
  const [id, setId] = useState("");

  const deleteBooks = useMutation(api.queries.deleteBooks);
  const updateStatus = useMutation(api.queries.updateStatus);

  const handleClick = (id: string) => {
    setId(id);
    setUpdate(!update);
  };

  const handleDelete = (id: string) => {
    deleteBooks({ id: id as Id<"books"> })
      .then((mess) => console.log(mess))
      .catch((err) => console.log(err));
  };

  const handleUpdate = (e: React.FormEvent<HTMLFormElement>, id: string) => {
    e.preventDefault();
    const formdata = new FormData(e.currentTarget);
    const isCompleted: boolean =
      (formdata.get("completed") as string) === "true";
    updateStatus({ id: id as Id<"books">, isCompleted })
      .then((mess) => console.log(mess))
      .catch((err) => console.log(err));
    setUpdate(false);
  };

  return (
    <div>
      {books.map((data: book, index: number) => {
        return (
          <div
            key={data._id}
            className={`book-container ${data.isCompleted ? "completed" : "not-completed"}`}
          >
            <h3>Livre n° : {index + 1}</h3>
            <p>Titre du livre : {data.title}</p>
            <p>Auteur du livre : {data.author}</p>
            <p>
              Statut de complétion :{" "}
              {data.isCompleted ? "Complété" : "Non complété"}
            </p>
            <button onClick={() => handleClick(data._id)}>Mettre à jour</button>
            {id === data._id && update && (
              <>
                <form onSubmit={(e) => handleUpdate(e, data._id)}>
                  <select name="completed">
                    <option value="true">Complété</option>
                    <option value="false">Non complété</option>
                  </select>
                  <input type="submit" />
                </form>
              </>
            )}
            <button onClick={() => handleDelete(data._id)}>Supprimer</button>
          </div>
        );
      })}
    </div>
  );
};
```

C'est le code complet du composant. Laissez-moi expliquer ce que nous avons fait.

Tout d'abord, nous devons basculer la mise à jour, donc nous avons défini la fonction `handleClick` et lui avons passé un ID de document.

```typescript
//handleClick
 const handleClick = (id: string) => {
    setId(id);
    setUpdate(!update);
  };
```

Dans `handleClick`, vous pouvez mettre à jour l'état de l'ID et basculer l'état de la mise à jour afin qu'il bascule l'entrée de mise à jour lorsqu'il est cliqué, et à un autre clic, il se fermera.

Ensuite, nous avons `handleUpdate`. Nous avons besoin de l'ID du document pour mettre à jour les données, donc nous avons passé l'objet événement ainsi que l'ID du document. Pour obtenir l'entrée, nous pouvons utiliser `FormData`.

```typescript
const updateStatus = useMutation(api.queries.updateStatus);

const handleUpdate = (e: React.FormEvent<HTMLFormElement>, id: string) => {
    e.preventDefault();
    const formdata = new FormData(e.currentTarget);
    const isCompleted: boolean =
      (formdata.get("completed") as string) === "true";
    updateStatus({ id: id as Id<"books">, isCompleted })
      .then((mess) => console.log(mess))
      .catch((err) => console.log(err));
    setUpdate(false);
  };
```

Nous devons utiliser `useMutation` pour obtenir la fonction `updateStatus`. Passez l'ID et le statut de complétion à la fonction, et gérez la partie asynchrone en utilisant `.then`.

Pour la fonction de suppression, l'ID du document suffit. Tout comme la précédente, appelez la fonction de suppression en utilisant `useMutation` et passez-lui l'ID.

Puis passez l'ID du document et gérez la promesse.

```typescript
const deleteBooks = useMutation(api.queries.deleteBooks);

const handleDelete = (id: string) => {
    deleteBooks({ id: id as Id<"books"> })
      .then((mess) => console.log(mess))
      .catch((err) => console.log(err));
 };
```

## Stylisation

Enfin, il reste à ajouter un peu de style. J'ai ajouté un style de base. Si le livre n'a pas été complété, il sera en rouge, et si le livre a été complété, il sera en vert.

Voici la capture d'écran :

![final output](https://cdn.hashnode.com/res/hashnode/image/upload/v1729428111374/1d1a69ef-5d35-4410-91f4-d8cf4817991d.png align="center")

C'est tout les gars !!

Vous pouvez vérifier mon dépôt pour le code complet : [convex-curd](https://github.com/sanjayr-12/convex-crud)

## Résumé

Dans cet article, nous avons implémenté les opérations CRUD (Create, Read, Update, and Delete) en construisant une application de collections de livres. Nous commençons par configurer Convex et React, et écrire la logique CRUD.

Ce tutoriel a couvert à la fois le frontend et le backend, démontrant comment construire une application serverless.

Vous pouvez trouver le code complet ici : [convex-curd](https://github.com/sanjayr-12/convex-crud)

Si vous avez des erreurs ou des doutes, contactez-moi sur [LinkedIn](https://www.linkedin.com/in/sanjay-r-ab6064294/), [Instagram](https://www.instagram.com/_sanjayxr_12_/).

Merci d'avoir lu !