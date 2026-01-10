---
title: Comment construire une application Full Stack avec Supabase, React et Tailwind
  CSS dans Next.js
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2022-01-26T23:03:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-full-stack-application-with-tailwind-css-and-supabase-in-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pexels-luis-gomes-546819.jpeg
tags:
- name: full stack
  slug: full-stack
- name: Next.js
  slug: nextjs
- name: React
  slug: react
- name: tailwind
  slug: tailwind
seo_title: Comment construire une application Full Stack avec Supabase, React et Tailwind
  CSS dans Next.js
seo_desc: "Serverless databases are all the rage these days. They allow you to develop\
  \ a fully functional app without building a server or writing server code. \nA serverless\
  \ database is a cloud computing solution that lets you distribute and flexibly manage\
  \ you..."
---

Les bases de données serverless sont très populaires ces jours-ci. Elles vous permettent de développer une application entièrement fonctionnelle sans construire un serveur ou écrire du code serveur. 

Une base de données serverless est une solution de cloud computing qui vous permet de distribuer et de gérer vos ressources de manière flexible.

Dans ce tutoriel, nous allons construire une application full-stack avec Supabase, React et TailwindCSS dans Next.js.

### Plan

- Qu'est-ce que Supabase ?
- Pourquoi devriez-vous utiliser Supabase ?
- Comment configurer un projet Supabase
- Comment configurer notre application Frontend
- Comment construire la mise en page de notre application Frontend avec le client Supabase
- Comment construire notre application
- Conclusion
- Ressources

### Prérequis

- Expérience pratique avec React.js
- Une compréhension de base des fonctions asynchrones
- Un compte GitHub

## Qu'est-ce que Supabase ?

[Supabase](https://supabase.io) est une base de données serverless open-source basée sur PostgreSQL qui vous permet de construire un backend en temps réel pour votre application en quelques minutes.

PostgreSQL est un système de base de données objet-relationnel qui est activement développé depuis plus de 25 ans et est connu pour sa fiabilité et ses performances.

[Supabase](https://supabase.io) inclut plusieurs services/fonctionnalités prêts à l'emploi conçus pour faciliter votre vie. Ceux-ci incluent, mais ne sont pas limités à :

- Authentification
- Base de données en temps réel
- Composants UI
- RLS (Sécurité au niveau des lignes)

### Pourquoi devriez-vous utiliser Supabase ?

- Supabase gère la mise à l'échelle (même s'il utilise une base de données SQL).
- Bien que Supabase soit basé sur PostgreSQL, la migration des données est facile.
- Vous pouvez exécuter des requêtes complexes ou des recherches de texte, contrairement à Firebase.

## Étape 1 : Comment configurer un projet Supabase

Cette section va construire notre projet et intégrer Supabase dans notre application.

### Inscription à un compte Supabase et création d'un projet

Pour commencer, inscrivons-nous à un compte Supabase [ici](https://api.supabase.io/platform/login). Pour continuer, vous aurez besoin d'un compte GitHub. Vous pouvez vous enregistrer [ici](http://github.com) si vous n'avez pas encore de compte sur GitHub.

![Tableau de bord Supabase - écran d'accueil](https://www.freecodecamp.org/news/content/images/2022/01/welcome-screen.png)

Après nous être connectés, nous sommes redirigés vers notre tableau de bord, comme montré dans la capture d'écran ci-dessus.

Ensuite, nous pouvons maintenant cliquer sur le bouton `Nouveau Projet` pour créer un nouveau projet pour notre application de démonstration, comme montré ci-dessous :

![Tableau de bord Supabase - créer un projet](https://www.freecodecamp.org/news/content/images/2022/01/create-project.png)

Ensuite, nous verrons l'écran ci-dessous, qui nous montre que le projet est maintenant en cours de construction.

![Tableau de bord Supabase - configuration du projet](https://www.freecodecamp.org/news/content/images/2022/01/project-setup.png)

Ensuite, nous devrons créer notre base de données en cliquant sur l'icône de la base de données affichée dans la barre latérale. Nous devons également cliquer sur l'icône plus affichée en haut à droite de l'écran pour créer chaque colonne dont nous avons besoin, comme montré ci-dessous.

![Tableau de bord Supabase - base de données](https://www.freecodecamp.org/news/content/images/2022/01/database.png)

### Comment créer les colonnes requises pour notre application

Pour ce projet de liste de tâches, nous allons créer cinq colonnes :

- `Name` : Il s'agit du nom de la tâche avec le type `text`.
- `Activity` : Il s'agit de l'activité de la tâche liée au type `text`.
- `StartDate` : Il s'agit de la date à laquelle la tâche est censée commencer avec le type `date`.
- `EndDate` : Il s'agit de la date à laquelle la tâche est censée se terminer avec le type `date`.

Après avoir créé tous ces champs, nous devrions avoir quelque chose de similaire à ce que nous avons ci-dessous.

![Tableau de bord Supabase - table de la base de données](https://www.freecodecamp.org/news/content/images/2022/01/database-table.png)

Nous avons créé notre projet et créé des colonnes individuelles. Nous allons procéder à l'étape suivante en configurant notre application frontend dans la section suivante.

## Étape 2 : Configuration de notre application Frontend

Pour créer un nouveau projet, nous utilisons la commande `npx create-next-app -e with-tailwindcss .` pour échafauder un nouveau projet dans un répertoire de notre choix.

La commande spécifiée ci-dessus configure un projet TailwindCSS dans Next.js.

[TailwindCSS](https://tailwindcss.com/) est un framework CSS contenant de nombreuses classes pour nous aider à styliser notre site web.

Nous utilisons les commandes suivantes pour installer les dépendances :

```Bash
    cd <nom du projet> 
    yarn add @supabase/supabase-js
```

Nous verrons un message avec des instructions pour naviguer sur notre site et l'exécuter localement après la création de l'application et l'installation des dépendances. En utilisant la commande ci-dessous, nous pouvons exécuter cela.

```Bash
    npm run dev
```

Next.js démarrera un environnement de développement avec rechargement à chaud accessible par défaut à <http://localhost:3000>.

Nous devrions voir quelque chose de similaire à ce que nous avons ci-dessous.

![page d'accueil nextjs](https://www.freecodecamp.org/news/content/images/2022/01/next-welcome.png)

## Étape 3 : Construction de la mise en page de notre application Frontend avec le client Supabase

Nous pouvons maintenant construire notre application front-end puisque nous avons terminé notre configuration front-end.

Mettons à jour notre fichier `pages/index.js` pour inclure le code suivant :

```Javascript
import Head from "next/head";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center py-2">
      <div>
        <Head>
          <title>Démonstration de Supabase et NextJs</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
          <h1 className="text-4xl font-bold mt-20">
            <a className="text-blue-600" href="/">
              Application Full Stack avec Tailwind CSS et Supabase dans NextJs
            </a>
          </h1>

          <div className="flex flex-wrap items-center justify-around max-w-4xl mt-6 sm:w-full">
            <div className="p-8 mt-6 border w-96 rounded-xl hover:text-blue-600 focus:text-blue-600">
              <div className="w-full max-w-sm">
                <form className="bg-white rounded px-8 pt-6 pb-8 mb-4">
                  <div className="mb-4">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="taskName"
                    >
                      Nom de la tâche
                    </label>
                    <input
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      id="taskName"
                      type="text"
                    />
                  </div>
                  <div className="mb-4">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="taskActivity"
                    >
                      Activité de la tâche
                    </label>

                    <textarea
                      className="form-textarea mt-1 block shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      rows="3"
                      placeholder="Activité de la tâche"
                    ></textarea>
                  </div>

                  <div className="mb-4">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="startDate"
                    >
                      Date de début de la tâche
                    </label>
                    <input
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      id="startDate"
                      type="date"
                    />
                  </div>
                  <div className="mb-4">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="endDate"
                    >
                      Date de fin de la tâche
                    </label>
                    <input
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      id="endDate"
                      type="date"
                    />
                  </div>
                  <div className="flex items-center justify-between">
                    <button
                      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                      type="button"
                    >
                      Ajouter une tâche
                    </button>
                  </div>
                </form>
              </div>
            </div>

            <div className="p-2 mt-6 w-96 rounded-xl focus:text-blue-600">
              <table className="shadow-lg bg-white">
                <tbody>
                  <tr>
                    <th className="bg-blue-400 border text-left px-4 py-4">
                      N°
                    </th>
                    <th className="bg-blue-400 border text-left px-8 py-4">
                      Nom
                    </th>
                    <th className="bg-blue-400 border text-left px-8 py-4">
                      Activité
                    </th>
                    <th className="bg-blue-400 border text-left px-14 py-4">
                      Date de début
                    </th>
                    <th className="bg-blue-400 border text-left px-16 py-4">
                      Date de fin
                    </th>

                    <th className="bg-blue-400 border text-left px-4 py-4">
                      Action
                    </th>
                  </tr>
                  <tr>
                    <td className="border px-4 py-4"></td>
                    <td className="border px-4 py-4"></td>
                    <td className="border px-8 py-4"></td>
                    <td className="border px-8 py-4"></td>
                    <td className="border px-8 py-4"></td>
                    <td className="border px-8 py-4">
                      {" "}
                      <button
                        className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        type="button"
                      >
                        Supprimer
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}

```

Nous avons ajouté une mise en page pour notre application dans l'extrait de code ci-dessus, et nous l'avons stylisée avec TailwindCSS.

Nous devrions avoir quelque chose de similaire à ce que nous avons ci-dessous si nous visitons notre application dans le navigateur.

![NextJs Supabase - index mis à jour](https://www.freecodecamp.org/news/content/images/2022/01/updated-index.png)

Nous allons utiliser le package `Supabase` pour lier notre application à notre base de données. Utiliser des variables d'environnement est la meilleure approche pour nous pour configurer cela.

Vous pouvez définir des variables d'environnement dans Next.js en créant un fichier appelé `.env` dans le répertoire racine du projet et en les sauvegardant là.

Il est préférable de faire précéder une variable par `NEXT_PUBLIC_` pour l'exposer au navigateur.

Ajoutez la configuration suivante à un fichier appelé `.env` dans le répertoire racine du projet :

```
NEXT_PUBLIC_SUPABASE_URL=https://app-id.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=votre-clé-publique-api
```

Nous pouvons trouver les valeurs de notre URL d'API et de notre clé d'API dans les paramètres du tableau de bord Supabase, comme montré ci-dessous :

![Index NexJs](https://www.freecodecamp.org/news/content/images/2022/01/api-1.png)

![Résultat de l'index NextJs](https://www.freecodecamp.org/news/content/images/2022/01/api-2.png)

Ensuite, nous allons créer un fichier appelé `client.js` à la racine du projet et ajouter le code suivant :

```

import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_TOKEN
);
```

Après l'avoir importé, nous pouvons maintenant utiliser l'instance Supabase partout dans notre application.

## Étape 4 : Construction de notre application

Mettons à jour notre fichier `pages/index.js` afin que nous puissions ajouter une nouvelle tâche en utilisant l'instance Supabase avec le code suivant :

```Javascript
// ...
import { useState, useEffect } from "react";
import { supabase } from "../client";

export default function Home() {

  // Déclarer une nouvelle variable d'état pour stocker les détails de la tâche
  const [task, setTask] = useState({
    Name: "",
    Activity: "",
    StartDate: "",
    EndDate: "",
  });

  const { Name, Activity, StartDate, EndDate } = task;

  // Créer une fonction qui gère la création de nouvelle tâche
  async function addTask() {
    await supabase
      .from("Task") // Sélectionner la table
      .insert([
        {
          Name,
          Activity,
          StartDate,
          EndDate,
        },
      ]) // Insérer la nouvelle tâche
      .single();
    setTask({
      Name: "",
      Activity: "",
      StartDate: "",
      EndDate: "",
    }); // Réinitialiser les détails de la tâche
  }

  return (
    <div className="flex flex-col items-center justify-center py-2">
      <div>
       // ...
        <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
          <h1 className="text-4xl font-bold mt-20">
            <a className="text-blue-600" href="/">
              Application Full Stack avec Tailwind CSS et Supabase dans NextJs
            </a>
          </h1>

          <div className="flex flex-wrap items-center justify-around max-w-4xl mt-6 sm:w-full">
            <div className="p-8 mt-6 border w-96 rounded-xl hover:text-blue-600 focus:text-blue-600">
              <div className="w-full max-w-sm">
                <form className="bg-white rounded px-8 pt-6 pb-8 mb-4">
                  <div className="mb-4">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="taskName"
                    >
                      Nom de la tâche
                    </label>
                    <input
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      id="taskName"
                      type="text"
                      value={Name.toString()}
                      onChange={(e) =>
                        setTask({ ...task, Name: e.target.value })
                      }
                    />
                  </div>
                  <div className="mb-4">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="taskActivity"
                    >
                      Activité de la tâche
                    </label>

                    <textarea
                      className="form-textarea mt-1 block shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      rows="3"
                      placeholder="Activité de la tâche"
                      value={Activity.toString()}
                      onChange={(e) =>
                        setTask({ ...task, Activity: e.target.value })
                      }
                    ></textarea>
                  </div>

                  <div className="mb-4">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="startDate"
                    >
                      Date de début de la tâche
                    </label>
                    <input
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      id="startDate"
                      type="date"
                      value={StartDate.toString()}
                      onChange={(e) =>
                        setTask({ ...task, StartDate: e.target.value })
                      }
                    />
                  </div>
                  <div className="mb-4">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="endDate"
                    >
                      Date de fin de la tâche
                    </label>
                    <input
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      id="endDate"
                      type="date"
                      value={EndDate.toString()}
                      onChange={(e) =>
                        setTask({ ...task, EndDate: e.target.value })
                      }
                    />
                  </div>
                  <div className="flex items-center justify-between">
                    <button
                      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                      type="button"
                      onClick={addTask} // Appeler la fonction addTask
                    >
                      Ajouter une tâche
                    </button>
                  </div>
                </form>
              </div>
            </div>

            <div className="p-2 mt-6 w-96 rounded-xl focus:text-blue-600">
              // ...
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}

```

Dans l'extrait de code ci-dessus, nous avons créé une fonction appelée `AddTask` pour ajouter une nouvelle tâche en utilisant l'instance Supabase. Nous l'avons également référencée dans l'attribut onClick de notre bouton `AddTask`.

Ensuite, après avoir testé notre application, vous avez peut-être remarqué qu'il ne se passe rien après avoir saisi les détails de la tâche et cliqué sur le bouton `Ajouter une tâche`. Cela est dû au fait que nous n'avons pas géré la récupération des tâches depuis notre base de données.

Mettons à jour notre fichier `pages/index.js` pour pouvoir récupérer toutes les tâches de notre base de données comme montré ci-dessous :

```Javascript
// ...
export default function Home() {
  const [loading, setLoading] = useState(true);
  const [tasks, setTasks] = useState([]);

  // ...

  async function getTasks() {
    const { data } = await supabase.from("Task").select(); // Sélectionner toutes les tâches de la table Task
    setTasks(data);
    setLoading(false);
  }

  // Exécuter la fonction getTasks lorsque le composant est monté
  useEffect(() => {
    getTasks();
  }, []);

  // Vérifier si chargement
  if (loading)
    return (
      <div className="flex justify-center items-center">
        <div
          className="
      animate-spin
      rounded-full
      h-32
      w-32
      border-t-2 border-b-2 border-blue-500 mt-36
    "
        ></div>
      </div>
    );
  return (
    <div className="flex flex-col items-center justify-center py-2">
      <div>
       // ...
        <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
          <h1 className="text-4xl font-bold mt-20">
            <a className="text-blue-600" href="/">
              Application Full Stack avec Tailwind CSS et Supabase dans NextJs
            </a>
          </h1>

          <div className="flex flex-wrap items-center justify-around max-w-4xl mt-6 sm:w-full">
            <div className="p-8 mt-6 border w-96 rounded-xl hover:text-blue-600 focus:text-blue-600">
              // ...
              </div>
            </div>

            <div className="p-2 mt-6 w-96 rounded-xl focus:text-blue-600">
              <table className="shadow-lg bg-white">
                <tbody>
                  <tr>
                    <th className="bg-blue-400 border text-left px-4 py-4">
                      N°
                    </th>
                    <th className="bg-blue-400 border text-left px-8 py-4">
                      Nom
                    </th>
                    <th className="bg-blue-400 border text-left px-8 py-4">
                      Activité
                    </th>
                    <th className="bg-blue-400 border text-left px-14 py-4">
                      Date de début
                    </th>
                    <th className="bg-blue-400 border text-left px-16 py-4">
                      Date de fin
                    </th>

                    <th className="bg-blue-400 border text-left px-4 py-4">
                      Action
                    </th>
                  </tr>
                  {task &&
                    tasks.map((task, index) => (
                      <tr key={task.id}>
                        <td className="border px-4 py-4">{index + 1}</td>
                        <td className="border px-4 py-4">{task.Name}</td>
                        <td className="border px-8 py-4">{task.Activity}</td>
                        <td className="border px-8 py-4">{task.StartDate}</td>
                        <td className="border px-8 py-4">{task.EndDate}</td>
                        <td className="border px-8 py-4">
                          {" "}
                          <button
                            className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                            type="button"
                          >
                            Supprimer
                          </button>
                        </td>
                      </tr>
                    ))}
                </tbody>
              </table>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}
```

Nous avons créé une fonction appelée `getTasks` pour récupérer toutes les tâches ajoutées en utilisant l'instance Supabase. Nous avons également itéré toutes les tâches récupérées et affiché tous les enregistrements dans un format de tableau, comme montré dans l'extrait de code ci-dessus.

Testons notre application, et nous devrions pouvoir ajouter une nouvelle tâche et voir toutes les tâches que nous avons créées jusqu'à présent.

![Résultat de l'application NextJs](https://www.freecodecamp.org/news/content/images/2022/01/app-result.png)

Cela fonctionne ! Mais nous avons dû actualiser la page lorsqu'une nouvelle tâche était ajoutée pour voir la nouvelle tâche. Nous ne voulons pas cela. Mettons à jour notre fonction `addTask` avec l'extrait de code ci-dessous :

```Javascript
  async function addTask() {
    await supabase
      .from("Task")
      .insert([
        {
          Name,
          Activity,
          StartDate,
          EndDate,
        },
      ])
      .single();
    setTask({
      Name: "",
      Activity: "",
      StartDate: "",
      EndDate: "",
    });
    getTasks(); // Rafraîchir les tâches
  }
```

Nous allons maintenant voir une nouvelle tâche ajoutée à notre tableau de tâches sans actualiser la page.

Faisons en sorte que le bouton `Supprimer` qui apparaît sur le côté droit du tableau supprime la tâche de notre base de données.

Mettons à jour notre fichier `pages/index.js` avec le snippet suivant :

```Javascript
 async function deleteTask(id) {
    await supabase.from("Task").delete().eq("id", id); // l'id de la ligne à supprimer
    getTasks();
  }

```

Mettons à jour l'attribut onClick du bouton de suppression comme montré ci-dessous :

```Javascript
     // ...

      <button
        className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        type="button"
        onClick={() => deleteTask(task.id)} // Supprimer la tâche
       >
        Supprimer
      </button>
```

Lorsque nous testons notre application, nous devrions pouvoir ajouter une nouvelle tâche, obtenir toutes les tâches ajoutées et supprimer n'importe quelle tâche que nous voulons. Nous pouvons voir à quoi cela devrait ressembler dans l'image ci-dessous, où nous avons supprimé l'une des tâches que nous avons créées précédemment.

![Résultat NextJs-Supabase](https://www.freecodecamp.org/news/content/images/2022/01/final-result.png)

Vous pouvez [cliquer ici](https://github.com/Olanetsoft/supabase-and-nextjs-demo) pour consulter le code complet sur GitHub.

## Conclusion

Ce tutoriel vous a montré comment construire une application full-stack avec Supabase, React et TailwindCSS dans Next.js.

Bon codage !

### Ressources

- [Documentation Supabase](https://supabase.io/docs/)
- [Documentation NextJs](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)