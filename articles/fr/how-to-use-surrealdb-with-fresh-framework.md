---
title: Comment utiliser SurrealDB avec le framework Fresh et Deno
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2022-09-23T17:51:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-surrealdb-with-fresh-framework
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Surreal-DB--and-deno-fresh-CMS--4-.png
tags:
- name: database
  slug: database
- name: Deno
  slug: deno
- name: TypeScript
  slug: typescript
seo_title: Comment utiliser SurrealDB avec le framework Fresh et Deno
seo_desc: 'SurrealDB is a newly launched database that has recently started gaining
  popularity in the programming world.

  SurrealDB was built with the Rust language and was created by Tobie Morgan Hitchcock
  and Jaime Morgan Hitchcock.

  SurrealDB''s new database co...'
---

SurrealDB est une base de données récemment lancée qui a commencé à gagner en popularité dans le monde de la programmation.

SurrealDB a été construite avec le langage Rust et a été créée par [Tobie Morgan Hitchcock](https://www.linkedin.com/in/tobiemorganhitchcock/) et [Jaime Morgan Hitchcock](https://www.linkedin.com/in/jaimemorganhitchcock/).

La nouvelle base de données de SurrealDB est dotée de nombreuses fonctionnalités, mais je suis particulièrement intéressé par la bibliothèque [Deno surrealDB](https://surrealdb.com/docs/integration/libraries/deno).

Dans cet article, nous allons créer une application de liste de tâches (todo app) simple avec le [framework Fresh](https://fresh.deno.dev/) et la base de données SurrealDB. Nous utiliserons le framework Fresh pour construire l'API avec SurrealDB.

Le framework Fresh est un nouveau framework JavaScript introduit par Deno lui-même. Fresh utilise la bibliothèque [Preact](https://preactjs.com/) pour concevoir et construire des composants. Fresh est livré avec un support intégré pour TypeScript et Tailwind CSS, ainsi qu'une architecture basée sur les **Islands** (îlots). De plus, aucune configuration n'est nécessaire.

Deno et Fresh sont **prêts pour la production**. Vous pouvez donc créer n'importe quelle application web et la déployer en un seul clic. Gardez toutefois à l'esprit que SurrealDB ne l'est peut-être pas encore tout à fait. Selon leur documentation, SurrealDB est prêt pour la production, mais la documentation n'est pas extrêmement claire sur le sujet.

Tout le code est [disponible sur GitHub.](https://github.com/officialrajdeepsingh/surrealDb-deno)

### Voici une démo de ce que nous allons construire :

![Démo de l'application TODO](https://www.freecodecamp.org/news/content/images/2022/09/tododemo.gif)
_Démo de l'application TODO_

## Comment installer SurrealDB, Deno et le framework Fresh

Il y a trois conditions préalables pour suivre ce tutoriel : la première est d'avoir **Deno** installé, la deuxième est d'avoir la base de données **SurrealDB**, et la dernière est d'utiliser le framework Fresh.

Tout d'abord, nous allons installer la base de données [SurrealDB](https://surrealdb.com/) et le [framework Fresh](https://fresh.deno.dev/) avec Deno. Vous pouvez ignorer cette partie si vous avez déjà installé Deno et les packages SurrealDB.

### Comment installer la base de données SurrealDB sur Linux

Le processus d'installation de SurrealDB est assez simple pour tous les systèmes d'exploitation. Par exemple, sous Linux, vous pouvez installer la base de données avec une seule commande curl.

Si vous avez un système d'exploitation différent, je vous suggère de lire la documentation d' [installation de SurrealDB](https://surrealdb.com/install).

Sous Linux, utilisez cette commande :

```bash
curl -sSf https://install.surrealdb.com | sh
```

![Installer la base de données SurrealDB sous Linux.](https://www.freecodecamp.org/news/content/images/2022/09/surrealdb.png)
_Installer la base de données SurrealDB sous Linux._

Pour démarrer la base de données SurrealDB sous Linux, exécutez la commande suivante :

```
surreal start --log debug --user root --pass root memory
```

1. Vous utilisez le drapeau `--user` pour votre nom d'utilisateur. Dans mon cas, mon nom d'utilisateur est root.
2. Vous utilisez le drapeau `--pass` pour votre mot de passe. Dans mon cas, mon mot de passe est root.

Pour en savoir plus sur tous les drapeaux ou options, exécutez la commande `surreal start --help`. Voici ce que vous verrez :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-from-2022-09-19-20-00-50.png)

Vous êtes maintenant prêt à utiliser la base de données SurrealDB.

### Comment installer Deno sur Linux

Deno est un environnement d'exécution JavaScript récent. Il est rapide et sécurisé par rapport à Node.js.

Pour en savoir plus sur Deno, vous pouvez [lire ce tutoriel utile que j'ai trouvé](https://www.freecodecamp.org/news/intro-to-deno/) sur freeCodeCamp, écrit par Brian Barrow.

Pour installer Deno sur Linux, vous avez besoin d'une seule commande :

```deno
curl -fsSL https://deno.land/install.sh | sh
```

![Installer deno sous Linux](https://www.freecodecamp.org/news/content/images/2022/09/install-deno-with-curl-command.png)
_Installer deno sous Linux_

### Comment installer le framework Fresh avec Deno

Fresh est un nouveau framework JavaScript basé sur Deno. Le framework Fresh supporte TypeScript par défaut. De plus, Fresh envoie par défaut zéro Ko de JavaScript au client.

Vous pouvez configurer un projet Fresh avec la commande suivante :

```deno
deno run -A -r https://fresh.deno.dev mon-nouveau-projet-fresh
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Install-surrealDB-deno.png)

Vous pouvez lancer un serveur de développement local avec `deno task start`.

**Notez** que le framework Fresh et SurrealDB utilisent tous deux le même port `8000`. Dans la documentation de SurrealDB, je n'ai trouvé aucune information sur le changement de port. Mais dans Fresh, vous pouvez facilement changer le port à l'intérieur du fichier `main.ts`. Sinon, sans changer le port, votre localhost Fresh redirigera vers le localhost de SurrealDB.

Par exemple, vous pouvez changer le port dans Fresh comme ceci :

```javascript
// changer le port dans main.ts

await start(manifest, { port:3002, plugins: [twindPlugin(twindConfig)] });


```

## Structure du projet framework Fresh

La structure des dossiers du projet est assez simple. Pour ce projet, nous devons suivre la structure des dossiers et des fichiers pour créer une application de liste de tâches avec SurrealDB.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/folder-strutucre.png)
_Structure des fichiers et des dossiers_

Discutons plus en détail de certains fichiers essentiels ici :

1. Le dossier **components** permet de contenir tous les composants personnalisés construits avec Preact.
2. Dans le fichier `deno.json`, vous ajoutez des tâches et le fichier importMap. Les tâches sont similaires aux scripts dans Node, et dans la section importMap, vous passez un fichier JSON qui contient tous vos packages d'importation de Deno.
3. `dev.ts` est un fichier créé uniquement pour le développement.
4. `fresh.gen.ts` est généré et mis à jour **automatiquement** en fonction de `dev.ts`. Il inclut toutes les routes, les islands et les autres configurations.
5. Le fichier `import_map.json` contient les importations de tous les packages dont vous avez besoin pour exécuter votre projet.
6. Les **Islands** permettent une interactivité basée sur le navigateur côté client dans Fresh. Fondamentalement, avec le dossier island, vous envoyez du JavaScript au navigateur. Par défaut, le framework Fresh envoie zéro Ko de JavaScript.
7. `main.ts` est le point d'entrée principal qui aide à démarrer votre application.
8. Le dossier `routes` gère vos chemins et votre API. Il est similaire au dossier pages de Next.js.
9. Le dossier `static` contient tous les fichiers statiques comme le JavaScript, les images et les polices sous un répertoire racine. Tous sont accessibles par référence et commencent par l'URL de base (`/`). Par exemple, `/logo.svg`.
10. `twind.config.ts` configure Tailwind CSS.
11. Le dossier `utility` contient la configuration de la base de données.

Vous pouvez en savoir plus sur la structure des dossiers dans la [documentation officielle](https://fresh.deno.dev/docs/getting-started/create-a-project) de Fresh.

Encore une fois, pour lancer un serveur de développement local, utilisez la commande `deno task start`.

## Comment installer la bibliothèque de base de données SurrealDB dans le framework Fresh

Vous avez besoin de la [bibliothèque SurrealDB](https://surrealdb.com/docs/integration/libraries/deno) (module) basée sur Deno. C'est une bibliothèque SurrealDB créée par l'équipe de SurrealDB.

La bibliothèque (module) SurrealDB vous aide à connecter votre application à votre base de données. Le module SurrealDB connecte très facilement vos bases de données locales et distantes.

Pour installer le module SurrealDB dans le framework Fresh, copiez simplement le code suivant et collez-le dans le fichier `import_map.json` :

```
  "surrealdb" : "https://deno.land/x/surrealdb@v0.2.0/mod.ts"
```

![Installer le module deno dans le framework fresh](https://www.freecodecamp.org/news/content/images/2022/09/import-package-in-fresh-cms.png)
_Collez le code suivant dans le fichier `import_map.json`_

### Comment configurer la base de données SurrealDB dans Fresh

La première étape consiste à créer un fichier de configuration pour la base de données SurrealDB. Ce fichier de configuration vous aide à connecter le framework Fresh à la base de données SurrealDB.

Dans mon cas, je crée une configuration de base de données dans un fichier séparé `utility/database.ts`. Le fichier séparé permet de réduire votre code et est plus facile à gérer.

```typescript
// utility/database.ts

// importer surrealdb 
import Surreal from "surrealdb";

// charger les variables d'environnement
import "https://deno.land/x/dotenv@v3.2.0/load.ts";

// obtenir l'URL DATABASE_URL
const domain = Deno.env.get("DATABASE_URL")

// base de données surreal
const db = new Surreal(domain);
    
// connexion
await db.signin({
    user: 'root',
    pass: 'root',
});



// Sélectionner un espace de noms / une base de données spécifique
await db.use('test', 'test');

export default db
```

Pour connecter la base de données, assurez-vous que votre base de données est en cours d'exécution et que votre mot de passe et votre nom d'utilisateur correspondent aux identifiants de votre base de données.

Par exemple, lancez votre SurrealDB local avec le nom d'utilisateur et le mot de passe identiques à ceux de votre fichier `utility/database.ts`.

```
surreal start --log debug --user root --pass root memory
```

## Comment utiliser les méthodes du module (bibliothèque) SurrealDB

Le module SurrealDB est livré avec des méthodes intégrées. Toutes ces méthodes vous aident à effectuer des opérations CRUD sur la base de données SurrealDB. Ces méthodes vous permettent de **créer** rapidement, ainsi que d' **obtenir**, **mettre à jour** et **supprimer** des éléments de la base de données.

Dans cet article, nous utiliserons quatre méthodes qui sont `create()`, `update()`, `delete()` et `select()`.

Il existe d'autres méthodes fournies par SurrealDB, que vous pouvez découvrir sur la [page de documentation du module SurrealDB](https://surrealdb.com/docs/integration/libraries/deno).

### Comment créer les points de terminaison API

Pour créer une application Todo, vous avez besoin de quatre points de terminaison. Nous utiliserons le framework Fresh pour créer les API. Toutes les routes de l'API vont dans le dossier `routes/api`.

1. Get
2. Post
3. Isdone (Mise à jour)
4. Delete

### L'API Get

L'API Get vous permet d'afficher toutes les données de la table todo. Pour accéder à toutes les données de la table Todo, vous avez besoin d'une fonction `select()` fournie par le module SurrealDB.

```get.ts
import { HandlerContext } from "$fresh/server.ts";
import db from "../../utility/database.ts";


export async function handler(_req: Request, _ctx: HandlerContext) {

    try {
        // obtenir toute la liste des tâches
        const todo = await db.select("todo");

        // retourner le todo 
        return Response.json(JSON.stringify(todo))

    } catch (error) {

        return new Response(error);
    }


}
```

### L'API Post

Dans l'API Post, vous allez créer une nouvelle tâche basée sur le titre. Toutes les tâches sont enregistrées dans la table todo. Avec l'API Get, vous accédez à toutes les tâches de la table todo.

Pour créer un nouvel élément de tâche dans la base de données, vous pouvez utiliser la fonction intégrée `create()` du module SurrealDB.

```post.ts
import { HandlerContext } from "$fresh/server.ts";

// importer le module uuid de deno 
import * as mod from "https://deno.land/std@0.156.0/uuid/mod.ts";

// importer la base de données 
import db from "../../utility/database.ts";


export async function handler(_req: Request, _ctx: HandlerContext) {
    // obtenir l'URL
    const url = new URL(_req.url);

    // obtenir le titre à partir de l'URL
    const title = url.searchParams.get("title") || "";

    try {

        // Créer une nouvelle personne avec un ID aléatoire

        const NAMESPACE_URL = "6ba7b810-9dad-11d1-80b4-00c04fd430c8";

        // créer un UUID unique à des fins de démonstration
        const uuid = await mod.v5.generate(NAMESPACE_URL, new TextEncoder().encode("python.org"));

        // créer de nouvelles données basées sur la valeur
        const created = await db.create("todo", {
            uuid: uuid,
            title: title,
            isDone: false
        });

        // retourner les données
        return Response.json({ sucessfull: "vos données ont été soumises avec succès", created })

    } catch (error) {

        return new Response(error);
    }


}
```

### L'API Isdone (Mise à jour)

L'API Isdone aide à mettre à jour les éléments de la table todo. Pour mettre à jour les données de la table, le module SurrealDB fournit une fonction intégrée `update` à cet effet.

Avec la fonction `update`, vous pouvez mettre à jour rapidement les tâches par un ou plusieurs éléments en une seule requête.

```isdone.ts
import { HandlerContext } from "$fresh/server.ts";

// importer la base de données 
import db from "../../utility/database.ts";



export async function handler(_req: Request, _ctx: HandlerContext) {
// obtenir l'URL
  const url = new URL(_req.url);
  // obtenir l'ID du todo – nous mettons à jour le todo sur la base de cet ID.
  const todoid = url.searchParams.get("todoID") || "";
  // obtenir le titre
  const todoTitle = url.searchParams.get("todoTitle") || "";
  // obtenir l'UUID
  const todoUuid = url.searchParams.get("todoUuid") || "";


    try {
      
        // mettre à jour le todo
        const person = await db.update(todoid, {
            isDone: true,
            title: todoTitle,
            uuid: todoUuid
        });
        
        return Response.json({sucessfull:"vos données ont été soumises avec succès ",person})

    } catch (error) {

        return new Response(error);
    }


}
```

### L'API Delete

Vous utilisez l'API Delete pour supprimer une tâche de la liste. Vous utiliserez la fonction intégrée `delete()`. Avec cette fonction, vous pouvez rapidement supprimer une tâche en fonction de son ID.

```javascript
import { HandlerContext } from "$fresh/server.ts";

// importer la base de données 
import db from "../../utility/database.ts";



export async function handler(_req: Request, _ctx: HandlerContext) {
    // obtenir l'URL
    const url = new URL(_req.url);

    // obtenir l'ID du todo – nous supprimons le todo sur la base de cet ID.
    const todoid = url.searchParams.get("todoID") || "";


    try {

        // supprimer l'élément todo spécifié 
        await db.delete(todoid);

        return Response.json({ sucessfull: "vos données ont été supprimées avec succès " })

    } catch (error) {

        return new Response(error);
    }

}
```

## Comment créer l'UI pour l'application Todo

![Image](https://www.freecodecamp.org/news/content/images/2022/09/todo-UI.png.png)
_UI pour le tableau de bord_

Les fichiers **`Box.tsx`** et **`Item.tsx`** proviennent d'un dossier island. Ces deux fichiers sont connus sous le nom de composants. Dans les deux composants, nous avons besoin d'une intégration JavaScript. Pour cette raison, nous créons les deux composants à l'intérieur du dossier island.

### Page d'index

La page d'index montre que les fichiers `Box.tsx` et `Item.tsx` proviennent de l'island. Nous allons concevoir la mise en page de la page d'accueil (Index) avec eux.

```typescript
import { Handlers } from "$fresh/server.ts";

// Importer les composants Box depuis island
import Box from "../islands/Box.tsx";

// Importer les composants Item depuis island
import Item from "../islands/Item.tsx";

// pour charger la variable d'environnement 
import "https://deno.land/x/dotenv@v3.2.0/load.ts";

// obtenir la variable d'environnement 
let domain= Deno.env.get("DOMAIN")


interface todo {
  id: string;
  title:string;
  isDone:boolean
}

// Appeler l'API get avec le handler Fresh
export const handler: Handlers<todo | null> = {

  async GET(_, ctx) {
    
    // appeler l'API get
    const response = await fetch(domain + "/api/get").then(      
      (response)=> response.json()
    ).then(
      (response)=> JSON.parse(response)
    ).catch(
      error=> console.log(error)
    );

    // passer les données dans les props du composant
    return ctx.render(response);
  }
};

export default function Home({data}: { data: any; }) {
  return (
    <div class="h-screen w-screen flex flex-col items-center justify-center bg-blue-600 font-sans">
      <div class="flex flex-row w-4/6 justify-center mx-auto">
        <h2 class="m-2 p-1 text-5xl font-mono font-serif cursor-pointer">Deno</h2>
        <h2 class="m-2 p-1 text-5xl font-mono font-serif cursor-pointer">SurrealDB</h2>
      </div>

      <div class="bg-white rounded shadow container mx-auto p-3 m-4 w-3/6 lg:w-3/6 xl:w-3/6 md:w-3/6 2xl:w-3/6 ">
            <div class=" flex mb-4 flex-col py-2">
                <h1 class="text-gray-500  text-lg">Todo List</h1>
                <Box/>
            </div>
            <div class="p-2">
              {
                data.map( (item: any) => 
                  <Item item={item} />
                )
              }
            </div>
        </div>
    </div>
  );
}
```

### Le composant Box.tsx

Le composant Box aide à appeler l'API post et à créer une nouvelle tâche dans la base de données. `Box.tsx` est un composant basé sur une island qui est créé avec Preact. Preact est similaire à React, mais Preact est une version légère de la bibliothèque.

Sur le composant Box, nous récupérons la valeur dans l'input avec l'événement onChange. Ensuite, après que l'utilisateur a cliqué sur le bouton d'ajout, nous appelons l'API post pour créer une nouvelle tâche dans la base de données SurrealDB.

![Concevoir le composant box avec le framework fresh](https://www.freecodecamp.org/news/content/images/2022/09/Box.tsx-in-index.png)
_Concevoir le composant box avec le framework Fresh_

```javascript
import { useState } from "preact/hooks";

// importer Notification depuis les composants
import Notification from "../components/Notification.tsx";

interface todo {
    id: string;
    title: string;
    isDone: boolean
}


export default function Box({ data }: { data: any; }) {

    // titre
    const [title, setTitle] = useState("");

    // afficher la Notification en fonction du succès
    const [successful, setSuccessful] = useState(false);


    function submit() {

        if (title) {
            // appeler l'API post 
            fetch(`/api/post?title=${encodeURIComponent(title)}`)
                .then((res) => res.json())
                .then((data) => {
                    console.log("vos données ont été soumises avec succès ");
                    
                    // changer false en true
                    setSuccessful(true)
                });
        }
    }



    return (
        <>
          <Notification  successful={successful}  setSuccessful={setSuccessful} />
            
            <div class="flex mt-4 justify-between">
                <input onChange={(event) => setTitle(event.currentTarget.value)} class="shadow appearance-none border rounded w-full py-2 px-3 mr-4 text-gray-600" placeholder="Add Todo" />
                <button onClick={submit} class="flex-shrink p-2 border-2 rounded text-purple-500 border-purple-500 hover:text-white hover:bg-purple-500 w-24">Add</button>
            </div>
        </>
    );
}
```

### Le composant Item.tsx

Le composant Item appelle deux API – l'une est l'API delete et la seconde est l'API update. L'API delete supprime un élément de la table todo et l'API update met à jour l'élément dans la table todo de la base de données.

`Item.tsx` est un composant island similaire au composant Box. Le composant item est également construit avec Preact.

Notre premier bouton change selon que la tâche est terminée ou en attente, et le second bouton supprime la tâche en fonction de son ID.

Tout d'abord, nous récupérons la valeur dans l'input avec l'événement onChange. Et après que l'utilisateur a cliqué sur le bouton d'ajout, nous appelons l'API post pour créer une nouvelle tâche dans la base de données SurrealDB.

Lorsque le bouton de suppression est cliqué, nous appelons l'API delete avec l'ID du todo pour supprimer la tâche de la base de données. Lorsque le bouton "Not Done" est cliqué, nous appelons l'API Isdone pour mettre à jour l'état dans la base de données.

![Composant Item dans le framework fresh](https://www.freecodecamp.org/news/content/images/2022/09/Item.tsx.png)
_Composant Item dans le framework Fresh_

```
import { useState } from "preact/hooks";

// importer Notification depuis les composants
import Notification from "../components/Notification.tsx";

interface todo {
    id: string;
    title: string;
    isDone: boolean
}


export default function Item({ item }) {

    // todo
    const [todo, setTodoID] = useState(
        {
            id: item.id,
            title: item.title,
            uuid: item.uuid
        }
    );

    // afficher la Notification en fonction du succès
    const [successful, setSuccessful] = useState(false);

    // fonction de suppression
    function deleteItem() {

        if (todo.id) {
            // appeler l'API delete
            fetch(`/api/delete?todoID=${encodeURIComponent(todo.id)}`)
                .then((res) => res.json())
                .then((data) => {
                    console.log("vos données ont été soumises avec succès ");
                    setSuccessful(true)
                });
        }
    }


    // isdone
    function isDone() {

        if (todo.id) {
            // appeler l'API isdone
            fetch(`/api/isdone?todoID=${encodeURIComponent(todo.id)}&todoTitle=${encodeURIComponent(todo.title)}&todoUuid=${encodeURIComponent(todo.uuid)}`)
                .then((res) => res.json())
                .then((data) => {
                    console.log("vos données ont été soumises avec succès ");
                    setSuccessful(true)
                });
        }
    }

    return (
        <>

            <Notification successful={successful} setSuccessful={setSuccessful} />

            <div class="flex mb-4 items-center">
                <p class={`${item.isDone === false ? "w-full text-green-500 cursor-pointer" : " w-full line-through decoration-purple-600 text-green-500 cursor-pointer"}`}>{item.title}</p>
                <button onClick={isDone} class="flex-shrink p-2 ml-4 mr-2 border-2 rounded hover:text-white text-gray-500 border-gray-500 hover:bg-gray-500 w-32">
                    {item.isDone === true ? "Done" : " Not done"}
                </button>
                <button onClick={deleteItem} class="flex-shrink p-2 ml-2 border-2 rounded text-red-500 border-red-500 hover:text-white hover:bg-red-500 w-24">Remove</button>
            </div>
        </>
    );
}

```

Et voilà – nous avons implémenté toutes les fonctionnalités de notre application Todo.

## Conclusion

SurrealDB est une base de données utile, et j'espère que vous avez apprécié d'en apprendre davantage à son sujet dans ce tutoriel.

Il y a souvent beaucoup d'exigences pour commencer à travailler avec d'autres bases de données, mais SurrealDB est très simple. Vous n'avez besoin que d'une seule commande pour démarrer la base de données localement et travailler avec elle. C'est une nouvelle révolution dans les bases de données.

Le gros problème est que SurrealDB n'est pas clair sur le fait qu'il soit livré avec des capacités de production. À l'heure actuelle, il ne semble pas remplir la promesse d'une application web prête pour la production en un clic (comme MongoDB Atlas, par exemple).

Vous pouvez déployer SurrealDB avec une image Docker. Le problème est que la documentation manque parfois d'informations pour un nouveau développeur (par exemple, comment changer les mots de passe et les utilisateurs dans un conteneur Docker).

Sans infrastructure cloud, vous ne seriez pas en mesure de déployer l'application avec SurrealDB. **Pour cette raison, je n'ai pas fourni de démo en direct de l'application Todo**. Mais je sais qu'à l'avenir, SurrealDB changera le futur des bases de données.