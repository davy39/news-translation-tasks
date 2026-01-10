---
title: Comment créer une application CRUD avec TanStack Start et TanStackDB (avec
  intégration RxDB)
subtitle: ''
author: Andrew Baisden
co_authors: []
series: null
date: '2025-10-27T21:08:27.001Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-crud-app-with-tanstack-start-and-tanstackdb-with-rxdb-integration
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761589878275/a36fe1d2-edf5-4339-b594-b1e55066485c.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
- name: React
  slug: reactjs
- name: tanstack
  slug: tanstack
seo_title: Comment créer une application CRUD avec TanStack Start et TanStackDB (avec
  intégration RxDB)
seo_desc: TanStack Start is a new full-stack framework for React. It’s been growing
  in popularity ever since it reached the Release Candidate stage of its development
  in September, 2025. The Release Candidate stage is basically a version of software
  which is c...
---

TanStack Start est un nouveau Framework full-stack pour React. Sa popularité ne cesse de croître depuis qu'il a atteint l'étape de Release Candidate de son développement en septembre 2025. L'étape Release Candidate est essentiellement une version d'un logiciel considérée comme presque complète, dans un état stable et prête pour les derniers tests publics avant son lancement officiel.

TanStack Start a déjà commencé à s'imposer comme une bonne alternative à d'autres Frameworks React populaires comme Next.js et Remix. L'écosystème TanStack est déjà très apprécié des développeurs, et d'autres outils bien connus incluent :

* [TanStack Router](https://tanstack.com/router/latest) : Routage Type-safe pour les applications React et Solid
    
* [TanStack Query](https://tanstack.com/query/latest) : Gestion d'état asynchrone puissante, utilitaires d'état serveur et récupération de données
    
* [TanStack Form](https://tanstack.com/form/latest) : UI Headless pour construire des formulaires performants et Type-safe
    
* [TanStackDB](https://tanstack.com/db/latest) : Un store client réactif pour construire des applications ultra-rapides sur synchronisation
    

Dans ce tutoriel, nous allons construire une application CRUD de liste de tâches simple mais puissante en utilisant [TanStack Start](https://tanstack.com/start), [TanStackDB](https://tanstack.com/db) et [RxDB](https://rxdb.info/). Vous pouvez voir à quoi ressemble l'application ci-dessous :

![TanStack to do list CRUD App](https://cdn.hashnode.com/res/hashnode/image/upload/v1761220967371/3bd1f03c-e844-42bc-ac0f-b637e7cd6e61.png align="center")

Ce tutoriel vous apprendra comment :

* Créer et persister des données localement avec RxDB
    
* Créer un projet TanStack Start qui utilise TanStackDB pour le stockage des données
    
* Construire une application CRUD (Create, Read, Update, Delete) complète
    

À la fin de ce guide, nous examinerons également ce qui différencie TanStack Start des autres Frameworks React comme Next.js et Remix, et comment TanStackDB s'intègre dans cet écosystème en pleine expansion.

Commençons.

## Table des matières

* [Qu'est-ce que TanStack Start ?](#heading-qu-est-ce-que-tanstack-start)
    
* [Qu'est-ce que TanStack DB (avec intégration RxDB) ?](#heading-qu-est-ce-que-tanstack-db-avec-integration-rxdb)
    
* [Configuration de notre projet](#heading-configuration-de-notre-projet)
    
* [Création du client de base de données](#heading-creation-du-client-de-base-de-donnees)
    
* [Comprendre la persistance locale avec RxDB](#heading-comprendre-la-persistance-locale-avec-rxdb)
    
* [Création d'une collection Todo](#heading-creation-d-une-collection-todo)
    
* [Création de nos actions CRUD](#heading-creation-de-nos-actions-crud)
    
* [Création de la page frontend](#heading-creation-de-la-page-frontend)
    
* [Comment TanStack Start se compare-t-il à Next.js et Remix ?](#heading-comment-tanstack-start-se-compare-t-il-a-nextjs-et-remix)
    
* [Quand devriez-vous utiliser TanStack Start, Next.js ou Remix ?](#heading-quand-devriez-vous-utiliser-tanstack-start-nextjs-ou-remix)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Heureusement, peu de choses sont nécessaires – seulement les suivantes :

* Node et npm installés
    
* Éditeur de code/IDE
    

## Qu'est-ce que TanStack Start ?

TanStack Start est un méta-Framework moderne basé sur React, créé par le développeur Tanner Linsley (célèbre pour avoir construit l'écosystème TanStack).

TanStack Start est conçu pour être :

* Incroyablement rapide, car il est propulsé par Vite, Bun ou d'autres bundlers modernes
    
* Type-safe, car il est profondément intégré à TypeScript ainsi qu'à TanStack Router
    
* Léger, car il n'y a pas de Server-side rendering à moins que vous ne le souhaitiez
    
* Prêt pour le full-stack, car il fonctionne avec des loaders, des actions et des mutations de données tout comme Remix
    

Si vous êtes déjà familier avec Next.js et Remix, vous pouvez considérer TanStack Start comme une manière plus modulaire, transparente et flexible de construire des applications React full-stack.

## Qu'est-ce que TanStack DB (avec intégration RxDB) ?

TanStackDB est une couche de gestion de données réactive qui se situe entre votre interface utilisateur et votre source de données. Ce n'est pas un ORM (Object Relational Mapper) typique. Au lieu de cela, il vous offre une couche d'abstraction unifiée pour travailler avec des collections de données local-first qui sont réactives.

Ainsi, lorsque vous combinez TanStackDB avec RxDB, vous obtenez une persistance de base de données locale qui fonctionne en utilisant IndexDB ou SQLite et une réactivité en temps réel. Cela vous donne la possibilité de synchroniser les données vers des backends distants plus tard, comme PostgreSQL par exemple.

Dans ce projet, nous allons utiliser RxDB pour le stockage local-first qui se comporte comme SQLite lorsqu'il est à l'intérieur d'un navigateur.

## Configuration de notre projet

Commençons de zéro. Trouvez un emplacement sur votre ordinateur pour créer ce projet et exécutez ces commandes dans votre terminal pour le configurer :

```bash
npm create @tanstack/start@latest my-app
cd my-app
npm install rxdb @tanstack/react-db @tanstack/rxdb-db-collection
mkdir -p src/db
touch src/db/actions.ts src/db/client.ts src/db/todoCollection.ts
```

Ce script de démarrage crée un projet TanStack Start, installe les dépendances pour RxDB et TanStackDB, et crée les dossiers et fichiers dont nous avons besoin pour notre application.

À la fin, nous allons également remplacer la page `index.tsx` existante par notre propre code d'application CRUD, tout en conservant les routes de démonstration dans la navigation afin que vous puissiez toujours les explorer.

## Création du client de base de données

Tout d'abord, occupons-nous de notre fichier `src/db/client.ts`. Copiez et collez le code ci-dessous dans le fichier :

```ts
import { createRxDatabase, removeRxDatabase } from "rxdb";
import { getRxStorageDexie } from "rxdb/plugins/storage-dexie";

let dbInstance: any = null;

export async function initDB() {
  // Initialiser uniquement dans l'environnement du navigateur
  if (typeof window === "undefined") {
    console.log("initDB: Pas dans le navigateur, saut de l'étape");
    return null;
  }

  if (dbInstance) {
    console.log("initDB: Retour de l'instance existante");
    return dbInstance;
  }

  try {
    console.log("initDB: Création d'une nouvelle instance de base de données");
    const storage = getRxStorageDexie();

    // Toujours supprimer la base de données existante en développement
    if (import.meta.env.DEV) {
      try {
        console.log("initDB: Suppression de la base de données existante (mode dev)");
        await removeRxDatabase("appdb", storage);
      } catch (e) {
        console.log("initDB: Aucune base de données existante à supprimer");
      }
    }

    dbInstance = await createRxDatabase({
      name: "appdb",
      storage,
      multiInstance: false,
      eventReduce: true,
    });

    console.log("initDB: Base de données créée avec succès");
    return dbInstance;
  } catch (error) {
    console.error("initDB: Échec de la création de la base de données", error);
    throw error;
  }
}

// Nettoyage pour le HMR
if (typeof window !== "undefined" && import.meta.hot) {
  import.meta.hot.dispose(async () => {
    console.log("HMR: Destruction de la base de données");
    if (dbInstance) {
      await dbInstance.destroy();
      dbInstance = null;
    }
  });
}
```

Ce code utilise RxDB pour créer une base de données côté client nommée `appdb`. Nous utilisons la fonction `getRxStorageDexie()` pour fournir un stockage IndexDB lorsqu'il est utilisé dans les navigateurs.

En mode dev, nous pouvons effacer la DB à chaque rechargement, nous offrant un état propre. L'exécution côté serveur est protégée par la vérification `window`. Le nettoyage HMR garantit que la DB est réinitialisée correctement lors du rechargement à chaud.

## Comprendre la persistance locale avec RxDB

Avant de passer à la section suivante, passons en revue le concept de persistance locale avec RxDB. Nos données sont susceptibles de disparaître lorsque la page est rechargée pendant le développement car RxDB utilise un moteur de base de données basé sur le navigateur pour persister les données localement. Nous utiliserons donc l'adaptateur de stockage Dexie qui stocke toutes les données de nos applications dans l'IndexedDB d'un navigateur.

Fondamentalement, cela signifie que nos todos ne persistent pas réellement dans le navigateur, même si nous fermons et rouvrons l'application – mais il existe un moyen de faire fonctionner cela dans notre application.

Dans le fichier `src/db/client.ts`, il se trouve justement une section de code qui ressemble à ceci :

```typescript
    if (import.meta.env.DEV) {
      try {
        console.log("initDB: Suppression de la base de données existante (mode dev)");
        await removeRxDatabase("appdb", storage);
      } catch (e) {
        console.log("initDB: Aucune base de données existante à supprimer");
      }
    }
```

Ce code s'assure que lorsque nous sommes en mode développement, notre base de données est supprimée puis recréée à chaque rechargement de l'application. C'est assez utile car lorsque nous développons activement et modifions les schémas, cela garantit que les anciennes données n'entreront pas en conflit avec les nouvelles structures de base de données.

L'inconvénient, cependant, est que les todos disparaîtront à chaque rafraîchissement de la page. Ce comportement est attendu lors de l'exécution locale de notre application en mode dev. Si vous voulez que les todos persistent entre les rechargements, il vous suffit de commenter ce bloc de code :

```typescript
// Commentez ou supprimez ce bloc de code pour persister les données entre les rechargements
   if (import.meta.env.DEV) {
      try {
        console.log("initDB: Suppression de la base de données existante (mode dev)");
        await removeRxDatabase("appdb", storage);
      } catch (e) {
        console.log("initDB: Aucune base de données existante à supprimer");
      }
    }
```

Après avoir effectué cette mise à jour, RxDB stockera désormais vos todos dans IndexedDB et ils seront automatiquement chargés chaque fois que vous reviendrez sur l'application. Vous pouvez même le voir par vous-même en ouvrant votre navigateur pendant que l'application est en cours d'exécution et en allant dans DevTools -> Application -> IndexedDB -> appdb.

Voir les exemples présentés ici :

![TanStack to do list app](https://cdn.hashnode.com/res/hashnode/image/upload/v1761221020837/2a7fd37f-e638-4c6b-997f-ecde0aa789bb.png align="center")

Voici un exemple de ce à quoi ressemble notre application avec quelques tâches :

![IndexedDB in the browser with tasks](https://cdn.hashnode.com/res/hashnode/image/upload/v1761221062751/431c4ac5-39d3-4adb-b197-bd4cc01a538e.png align="center")

Ici, vous pouvez voir que nos données sont stockées à l'intérieur d'IndexedDB dans notre navigateur.

Les tâches devraient y rester jusqu'à ce que vous ayez manuellement effacé les données du navigateur.

## Création d'une collection Todo

Maintenant, travaillons sur notre fichier `src/db/todoCollection.ts`. Copiez et collez ce code dans le fichier vide du projet :

```ts
import { initDB } from "./client";

let todoCollectionInstance: any = null;

export async function createTodoCollection() {
  // Protection contre l'exécution côté serveur
  if (typeof window === "undefined") {
    console.log("createTodoCollection: Pas dans le navigateur, saut de l'étape");
    return null;
  }

  if (todoCollectionInstance) {
    console.log("createTodoCollection: Retour de la collection existante");
    return todoCollectionInstance;
  }

  try {
    console.log("createTodoCollection: Initialisation de la base de données");
    const db = await initDB();

    if (!db) {
      console.error(
        "createTodoCollection: L'initialisation de la base de données a renvoyé null",
      );
      return null;
    }

    console.log("createTodoCollection: Ajout des collections");
    if (!db.todos) {
      await db.addCollections({
        todos: {
          schema: {
            version: 0,
            primaryKey: "id",
            type: "object",
            properties: {
              id: {
                type: "string",
                maxLength: 100,
              },
              title: {
                type: "string",
              },
              completed: {
                type: "boolean",
              },
            },
            required: ["id", "title", "completed"],
          },
        },
      });
      console.log("createTodoCollection: Collections ajoutées avec succès");
    }

    // Retourner directement la collection RxDB
    todoCollectionInstance = db.todos;

    console.log("createTodoCollection: Collection créée avec succès");
    return todoCollectionInstance;
  } catch (error) {
    console.error("createTodoCollection: Échec de la création de la collection", error);
    throw error;
  }
}
```

Avec ce fichier, nous définissons un schéma de collection `todos` qui possède des champs `id`, `title` et `completed`. Ce schéma permet de s'assurer que la structure et la validation sont correctes, et nous mémoïsons l'instance de la collection, ce qui empêche la création de multiples connexions à la DB. Le code renvoie ensuite une collection RxDB en direct, prête pour les requêtes et les mutations.

## Création de nos actions CRUD

Il est maintenant temps de travailler sur nos actions CRUD. Celles-ci nous permettent d'effectuer les mises à jour/modifications habituelles des données de notre liste de tâches.

Ouvrez le fichier `src/db/actions.ts` et copiez-y ce code :

```ts
import { createTodoCollection } from "./todoCollection";

let collectionPromise: Promise<any> | null = null;

async function getCollection() {
  if (typeof window === "undefined") {
    return null;
  }

  if (!collectionPromise) {
    collectionPromise = createTodoCollection();
  }
  return collectionPromise;
}

export const TodoActions = {
  async getAll() {
    try {
      const collection = await getCollection();
      if (!collection) return [];

      const docs = await collection.find().exec();
      return docs.map((doc: any) => ({
        id: doc.id,
        title: doc.title,
        completed: doc.completed,
      }));
    } catch (error) {
      console.error("Erreur TodoActions.getAll :", error);
      throw error;
    }
  },

  async add(title: string) {
    const collection = await getCollection();
    if (!collection) throw new Error("Collection non initialisée");

    await collection.insert({
      id: crypto.randomUUID(),
      title,
      completed: false,
    });
  },

  async update(
    id: string,
    changes: Partial<{ title: string; completed: boolean }>
  ) {
    const collection = await getCollection();
    if (!collection) throw new Error("Collection non initialisée");

    const doc = await collection.findOne(id).exec();
    if (doc) {
      const patch: any = {};
      if (typeof changes.title !== "undefined") patch.title = changes.title;
      if (typeof changes.completed !== "undefined")
        patch.completed = changes.completed;
      if (Object.keys(patch).length > 0) {
        await doc.patch(patch);
      }
    }
  },

  async toggle(id: string) {
    const collection = await getCollection();
    if (!collection) throw new Error("Collection non initialisée");

    const doc = await collection.findOne(id).exec();
    if (doc) {
      await doc.patch({ completed: !doc.completed });
    }
  },

  async remove(id: string) {
    const collection = await getCollection();
    if (!collection) throw new Error("Collection non initialisée");

    const doc = await collection.findOne(id).exec();
    if (doc) {
      await doc.remove();
    }
  },
};
```

Avec ce code, nous utilisons la fonction `getCollection()` pour nous assurer que nous n'initialisons la collection qu'une seule fois. Chaque méthode CRUD (getAll, add, toggle, remove) interagit directement avec RxDB et les méthodes utilisent le `crypto.randomUUID()` natif du navigateur pour générer un ID unique. Nous pouvons maintenant gérer en toute sécurité le rendu côté serveur, car nous sautons l'accès à la DB sur le serveur grâce à cette stratégie.

## Création de la page frontend

Tout ce qu'il reste à faire est l'interface utilisateur frontend, car nous avons déjà écrit l'essentiel de la logique. Nous allons remplacer le fichier `src/routes/index.tsx` par défaut par notre propre UI CRUD, remplacez donc tout le code de ce fichier par celui-ci :

```tsx
import * as React from "react";
import { createFileRoute } from "@tanstack/react-router";
import { TodoActions } from "../db/actions";

function Index() {
  const [todos, setTodos] = React.useState<
    Array<{ id: string; title: string; completed: boolean }>
  >([]);
  const [title, setTitle] = React.useState("");
  const [isLoading, setIsLoading] = React.useState(true);
  const [error, setError] = React.useState<Error | null>(null);
  const [editingId, setEditingId] = React.useState<string | null>(null);
  const [editingTitle, setEditingTitle] = React.useState("");

  React.useEffect(() => {
    let active = true;

    (async () => {
      try {
        console.log("Index: Chargement des todos");
        const data = await TodoActions.getAll();
        console.log("Index: Todos chargés", data);
        if (active) {
          setTodos(data);
          setIsLoading(false);
        }
      } catch (err) {
        console.error("Index: Échec du chargement des todos :", err);
        if (active) {
          setError(err as Error);
          setIsLoading(false);
        }
      }
    })();

    return () => {
      active = false;
    };
  }, []);

  const handleAdd = async (e: React.FormEvent) => {
    e.preventDefault();
    if (title.trim()) {
      try {
        await TodoActions.add(title);
        setTodos(await TodoActions.getAll());
        setTitle("");
      } catch (err) {
        console.error("Échec de l'ajout du todo :", err);
        setError(err as Error);
      }
    }
  };

  const handleToggle = async (id: string) => {
    try {
      await TodoActions.toggle(id);
      setTodos(await TodoActions.getAll());
    } catch (err) {
      console.error("Échec du basculement du todo :", err);
    }
  };

  const handleRemove = async (id: string) => {
    try {
      await TodoActions.remove(id);
      setTodos(await TodoActions.getAll());
    } catch (err) {
      console.error("Échec de la suppression du todo :", err);
    }
  };

  const startEdit = (todo: { id: string; title: string }) => {
    setEditingId(todo.id);
    setEditingTitle(todo.title);
  };

  const cancelEdit = () => {
    setEditingId(null);
    setEditingTitle("");
  };

  const saveEdit = async () => {
    if (!editingId) return;
    const newTitle = editingTitle.trim();
    if (!newTitle) return;
    try {
      await TodoActions.update(editingId, { title: newTitle });
      setTodos(await TodoActions.getAll());
      setEditingId(null);
      setEditingTitle("");
    } catch (err) {
      console.error("Échec de la mise à jour du todo :", err);
    }
  };

  if (isLoading) {
    return (
      <main className="p-6 max-w-lg mx-auto">
        <div className="text-center">Chargement de la base de données...</div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="p-6 max-w-lg mx-auto">
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
          <strong className="font-bold">Erreur : </strong>
          <span className="block sm:inline">{error.message}</span>
          <details className="mt-2">
            <summary className="cursor-pointer">Afficher les détails</summary>
            <pre className="mt-2 text-xs overflow-auto">{error.stack}</pre>
          </details>
        </div>
      </main>
    );
  }

  return (
    <main className="p-6 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">TanStack CRUD (RxDB)</h1>

      <form onSubmit={handleAdd} className="flex gap-2 mb-4">
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Ajouter une nouvelle tâche"
          className="border rounded px-3 py-2 flex-1"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Ajouter
        </button>
      </form>

      <ul>
        {todos.length === 0 ? (
          <li className="text-gray-500 text-center py-4">Pas encore de todos</li>
        ) : (
          todos.map((todo) => (
            <li
              key={todo.id}
              className="flex justify-between items-center py-2 border-b"
            >
              {editingId === todo.id ? (
                <div className="flex w-full items-center gap-2">
                  <input
                    value={editingTitle}
                    onChange={(e) => setEditingTitle(e.target.value)}
                    className="border rounded px-2 py-1 flex-1"
                  />
                  <button
                    onClick={saveEdit}
                    className="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600"
                  >
                    Enregistrer
                  </button>
                  <button
                    onClick={cancelEdit}
                    className="px-3 py-1 rounded border"
                  >
                    Annuler
                  </button>
                </div>
              ) : (
                <>
                  <span
                    onClick={() => handleToggle(todo.id)}
                    className={
                      todo.completed
                        ? "line-through cursor-pointer"
                        : "cursor-pointer"
                    }
                  >
                    {todo.title}
                  </span>
                  <div className="flex items-center gap-3">
                    <button
                      onClick={() => startEdit(todo)}
                      className="text-blue-500 hover:text-blue-700"
                    >
                      Modifier
                    </button>
                    <button
                      onClick={() => handleRemove(todo.id)}
                      className="text-red-500 hover:text-red-700"
                    >
                      ✕
                    </button>
                  </div>
                </>
              )}
            </li>
          ))
        )}
      </ul>
    </main>
  );
}

export const Route = createFileRoute("/")({
  component: Index,
});
```

Notre fichier `index.tsx` mis à jour utilise TanStack Router pour définir notre page racine, et nous avons des hooks React pour gérer l'état, la gestion des erreurs et les mises à jour CRUD.

Notre frontend est configuré pour afficher des états de chargement/erreur pour une UX beaucoup plus fluide, et chaque bouton déclenche une méthode `TodoActions` correspondante. Le résultat est que nous avons une application CRUD locale entièrement réactive.

C'est tout ce qu'il y a à faire. Pour lancer l'application, utilisez la commande habituelle pour une application Vite :

```bash
npm run dev
```

## Comment TanStack Start se compare-t-il à Next.js et Remix ?

TanStack Start semble assez impressionnant, n'est-ce pas ? Mais voyons comment il se compare aux deux autres grands Frameworks établis, Next.js et Remix.

Next.js a récemment publié la [version 16](https://nextjs.org/blog/next-16), qui a apporté de nouvelles améliorations et fonctionnalités que vous pouvez découvrir. C'est sans aucun doute le Framework React le plus connu et le plus utilisé actuellement.

Remix a également beaucoup d'atouts, avec son récent [événement récapitulatif Remix Jam 2025](https://remix.run/blog/remix-jam-2025-recap) que vous pouvez également consulter.

TanStack Start, quant à lui, est construit en utilisant l'outil de build populaire [Vite](https://vite.dev/) qu'il utilise pour son développement, son workflow et ses builds de production aux côtés de TanStack Router et d'autres bibliothèques.

Voici comment les trois se comparent lorsqu'on les met côte à côte dans un tableau :

| Fonctionnalité | **TanStack Start** | **Next.js** | **Remix** |
| --- | --- | --- | --- |
| Routage | TanStack Router | Basé sur les fichiers | Routes imbriquées |
| Sécurité des types | Intégration TS profonde | Partielle | Complète |
| Chargement des données | Loaders/Actions | Server Components | Loaders/Actions |
| Support SSR | Optionnel | Intégré | Intégré |
| Bundler | Vite / Bun | Webpack / Turbopack | Remix Compiler |
| DX | Simple, minimal | Écosystème full-stack | Full-stack avec conventions |

Comme vous pouvez le voir, TanStack Start offre une grande flexibilité. Il n'impose pas de conventions comme Next.js ou Remix en raison de sa conception et il possède juste la bonne dose de structure pour les développeurs qui veulent du contrôle et de la transparence dans leurs projets. Les trois sont cependant d'excellentes options.

## Quand devriez-vous utiliser TanStack Start, Next.js ou Remix ?

Chacun de ces Frameworks a ses avantages et ses inconvénients en fonction de la configuration et des priorités de votre projet. Nous devons prendre en compte la performance, la flexibilité, l'écosystème ainsi que l'expérience développeur (DX).

Tout cela permet de dresser un portrait plus clair du moment idéal pour les utiliser.

### Quand utiliser TanStack Start

Si vous voulez un contrôle total sur votre architecture sans être enfermé dans des conventions, alors TanStack Start est un excellent choix. Il est idéal si vous appréciez la transparence ainsi que la flexibilité qui en découle.

Vous constaterez qu'il est particulièrement utile dans les projets qui nécessitent un contrôle précis sur le routage, la récupération de données et la mise en cache – sans avoir à vous soucier de la surcharge d'un Framework large et directif.

L'intégration entre Vite et TanStack Router en fait un outil léger et incroyablement rapide qui peut être idéal pour les nouveaux projets et les équipes qui souhaitent une configuration modulaire.

### Quand utiliser Next.js

Next.js est une excellente option lorsque vous avez besoin d'une scalabilité prête pour la production et d'une documentation étendue, avec un très large écosystème. Le Framework est devenu une référence pour les startups comme pour les entreprises en raison de son intégration étroite avec les React Server Components, l'hébergement avec Vercel et les packages communautaires.

Ainsi, si le SEO, le SSR ou le rendu hybride font partie des besoins fondamentaux de votre équipe, ou si vous voulez livrer quelque chose rapidement avec une base éprouvée, alors Next.js est la voie la plus sûre et la plus mature.

### Quand utiliser Remix.js

Remix est un excellent choix lorsque vous voulez mettre l'accent sur les fondamentaux du web, l'amélioration progressive et une UX fiable. Il est adapté aux applications où vous souhaitez utiliser les capacités natives du navigateur telles que les formulaires, la mise en cache et l'accessibilité, tout en bénéficiant d'un workflow full-stack moderne.

C'est également idéal pour les équipes qui veulent la simplicité du routage conventionnel et des loaders tout en restant proches de la plateforme originale.

## Conclusion

Dans cet article, nous avons construit une application CRUD à partir de zéro en utilisant :

* TanStack Start pour la structure de l'application et le routage
    
* TanStackDB pour la gestion réactive des données
    
* RxDB pour une expérience offline-first et une persistance locale
    

Vous avez appris comment initialiser une base de données locale et des collections, ainsi qu'à effectuer des opérations CRUD en toute sécurité.

L'écosystème TanStack est très puissant et de nombreux outils sont disponibles. Ils s'emboîtent tous parfaitement pour vous offrir une expérience de développement web réactive, local-first et de nouvelle génération. TanStack Start est susceptible de devenir l'une de vos méthodes préférées pour construire des applications React et possède un fort potentiel de croissance.

Les démos officielles de TanStack sont toujours disponibles dans votre navigation sur la page d'accueil, et elles valent le détour. Essayez l'écosystème TanStack. Je pense qu'il pourrait facilement devenir votre stack technique principale.