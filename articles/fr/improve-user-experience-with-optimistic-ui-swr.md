---
title: Comment améliorer l'expérience utilisateur avec l'UI Optimiste et SWR
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2024-07-09T22:33:50.000Z'
originalURL: https://freecodecamp.org/news/improve-user-experience-with-optimistic-ui-swr
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Article-cover.png
tags:
- name: UI Design
  slug: ui-design
- name: user experience
  slug: user-experience
seo_title: Comment améliorer l'expérience utilisateur avec l'UI Optimiste et SWR
seo_desc: 'Have you ever noticed how some apps feel like they can read your mind?
  You click a button, and before you can even blink, it''s done – no loading screens,
  no waiting around. It''s like magic, right? Well, let me tell you a little secret:
  that''s the pow...'
---

Avez-vous déjà remarqué comment certaines applications semblent pouvoir lire dans vos pensées ? Vous cliquez sur un bouton, et avant même de cligner des yeux, c'est fait – pas d'écrans de chargement, pas d'attente. C'est comme de la magie, n'est-ce pas ? Eh bien, laissez-moi vous révéler un petit secret : c'est le pouvoir de l'UI Optimiste.

Dans cet article, nous allons plonger dans l'UI Optimiste et explorer comment elle fonctionne et maintient votre expérience web fluide comme du beurre. Nous allons construire ensemble une simple application de tâches qui montrera comment l'UI Optimiste peut aider à transformer des tâches banales en interactions ultra-rapides qui laissent vos utilisateurs heureux.

### Prérequis

* Fondamentaux de JavaScript et React
* Fondamentaux de la programmation asynchrone et Axios
* La connaissance des bibliothèques de fetch orientées hooks serait également bénéfique

## **Ce que nous allons couvrir :**

1. [Qu'est-ce que l'UI Optimiste ?](#heading-quest-ce-que-lui-optimiste)
2. [Pourquoi l'UI Optimiste est-elle importante ?](#heading-pourquoi-lui-optimiste-est-elle-importante)
3. [Autres avantages de l'UI Optimiste](#heading-autres-avantages-de-lui-optimiste)
4. [Présentation de SWR : Stale-While-Revalidate](#heading-presentation-de-swr-stale-while-revalidate)
5. [Comment configurer l'environnement](#heading-comment-configurer-lenvironnement)
6. [Comment construire l'UI de l'application de tâches](#heading-comment-construire-lui-de-lapplication-de-taches)  
– [UI CRUD régulière](#heading-ui-crud-reguliere)  
– [UI CRUD optimiste](#heading-ui-crud-optimiste)
7. [Inconvénients de l'UI Optimiste](#heading-inconvenients-de-lui-optimiste)
8. [Cas d'utilisation idéaux pour l'UI Optimiste](#heading-cas-dutilisation-ideaux-pour-lui-optimiste)
9. [Conclusion](#heading-conclusion)

## Qu'est-ce que l'UI Optimiste ?

À sa base, l'UI Optimiste consiste à garder votre application réactive et rapide, même lorsque beaucoup de choses se passent en arrière-plan. C'est comme avoir un superpouvoir qui permet à votre application de prédire l'avenir – enfin, en quelque sorte.

Lorsque vous effectuez une action dans votre application – qu'il s'agisse d'ajouter un nouvel élément à une liste ou de mettre à jour un profil – l'UI Optimiste se met en marche pour que cela se produise immédiatement, sans attendre la confirmation du serveur. C'est l'optimiste ultime, supposant toujours que tout se passera bien.

## Pourquoi l'UI Optimiste est-elle importante ?

Alors, pourquoi devriez-vous vous soucier de l'UI Optimiste ? Simple : parce que c'est la sauce secrète qui transforme les bonnes applications en excellentes.

Réfléchissez-y : lorsque vous cliquez sur un bouton, vous vous attendez à ce que quelque chose se produise – et vous vous attendez à ce que cela se produise rapidement. C'est là que l'UI Optimiste brille. En donnant à vos utilisateurs un retour instantané et en gardant votre application réactive, l'UI Optimiste améliore l'expérience utilisateur globale.

Plus besoin de fixer des écrans de chargement ou de se demander si votre clic a _vraiment_ fait quelque chose – avec l'UI Optimiste, chaque action semble facile et efficace.

## Autres avantages de l'UI Optimiste

1. **Latence perçue réduite** : L'UI Optimiste réduit la latence perçue des actions en affichant les changements immédiatement sans attendre la confirmation du serveur. Cela crée une perception de temps de réponse plus rapides, même si la communication avec le serveur prend plus de temps.
2. **Réactivité améliorée** : L'UI Optimiste permet aux utilisateurs d'interagir avec l'application en continu sans interruptions dues aux indicateurs de chargement ou aux écrans d'attente. Ce flux ininterrompu améliore la réactivité globale de l'application.
3. **Support pour les interactions complexes** : L'UI Optimiste aide les interactions complexes, telles que le glisser-déposer, les processus multi-étapes et la collaboration en temps réel, à se sentir fluides et intuitives. Cette flexibilité ouvre des possibilités pour des fonctionnalités et des fonctionnalités innovantes dans l'application.
4. **Engagement utilisateur accru** : La réactivité et l'interactivité fournies par l'UI Optimiste peuvent conduire à un engagement et une rétention accrus des utilisateurs. Les utilisateurs sont plus susceptibles de revenir à une application qui offre une expérience fluide et agréable.

## Présentation de SWR : Stale-While-Revalidate

Avant de plonger dans l'implémentation, prenons un moment pour parler de SWR. SWR est une bibliothèque légère de hooks React pour la récupération de données. SWR signifie [Stale-While-Revalidate](https://swr.vercel.app/examples/optimistic-ui), et elle trouve le parfait équilibre entre performance et fraîcheur lors de la récupération de données dans vos applications React.

SWR révalide également automatiquement les données en arrière-plan tout en servant toujours les données obsolètes du cache. Cela signifie que votre application reste rapide et réactive, même lors de la récupération de nouvelles données depuis le serveur.

Mais ce n'est pas tout – SWR prend également en charge des fonctionnalités clés comme la mise en cache, la pagination et la gestion des erreurs, ce qui en fait un outil puissant dans votre arsenal pour construire des applications web rapides et fiables ainsi que pour implémenter l'UI Optimiste.

## Comment configurer l'environnement

J'ai préparé un dépôt GitHub avec des fichiers de démarrage pour accélérer les choses. Clonez simplement [ce dépôt](https://github.com/Daiveedjay/Optimistic-UI-with-SWR/tree/starter) et installez les dépendances.

Le code de démarrage se compose des composants JSX de base requis, ainsi que de certaines fonctions [Axios](https://axios-http.com/docs/intro) de base pour effectuer des opérations CRUD. Après avoir installé tous les packages nécessaires avec `npm i`, ouvrez votre terminal et démarrez votre endpoint local en utilisant [json-server](https://www.npmjs.com/package/json-server).

```bash
npx json-server data/db.json -p 3500
```

Pour voir toutes vos données présentes, rendez-vous sur cette route :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/1-Showing-initial-data.png)
_Affichage des données initiales_

## Comment construire l'UI de l'application de tâches

Dans cette section, nous allons d'abord implémenter des applications CRUD sans UI Optimiste puis avec UI Optimiste pour montrer les différences entre elles.

### UI CRUD régulière

Commencez par vous rendre dans votre composant `TaskContainer`, puis utilisez le hook `useSWR` pour appeler votre fonction de récupération.

```js
const {
    isLoading,
    error,
    data: tasks,
    mutate,
  } = useSWR(cacheKey, fetchTasks, {
    onSuccess: (data) =>
      data.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt)),
  });
```

SWR utilise un hook et un modèle de récupération de données similaires à d'autres bibliothèques telles que [React Query (TanStack Query)](https://tanstack.com/query/latest/docs/framework/react/overview) et [Redux Toolkit Query](https://redux-toolkit.js.org/rtk-query/overview). Ce modèle de hook de récupération retourne souvent un état de chargement, un état d'erreur, vos données récupérées (le cas échéant) et une fonction de mutation (mais nous en parlerons plus tard).

**Note** : La `cacheKey` est une clé unique utilisée pour notifier SWR quand et où rappeler votre fonction. La fonction `onSuccess` est une méthode utilisée pour déclencher une autre action lorsque la récupération est réussie – dans ce cas, trier les données par ordre décroissant.

Avec vos données de retour, vous pouvez maintenant créer le balisage JSX.

```jsx
return (
   
      <div className="flex flex-col gap-8 p-4">
       
        <div className="p-4 shadow-lg ">
          <div className="flex flex-col gap-4 ">
            {tasks &&
              tasks.map((task, index) => {
                return (
                  <div
                    key={task.id}
                    className="flex gap-4 items-center py-2 px-6 rounded-md bg-[#74a0a6]">
                    <div>
                      <label
                        htmlFor={`task-${task.id}`}
                        key={task.id}
                        className={`flex gap-4 text-[14px] items-center font-bold list-none p-4 rounded bg-[#88adb3] cursor-pointer hover:bg-[#609299]`}>
                        <div className="inline-flex items-center">
                          <label
                            className="relative flex items-center p-3 rounded-full cursor-pointer"
                            htmlFor="checkbox">
                            <input
                              type="checkbox"
                              name={`task-${task.id}`}
                              id={`task-${task.id}`}
                              className="before:content[''] peer relative h-5 w-5 cursor-pointer appearance-none rounded-md border border-[#edebd9] transition-all before:absolute before:top-2/4 before:left-2/4 before:block before:h-12 before:w-12 before:-translate-y-2/4 before:-translate-x-2/4 before:rounded-full before:bg-blue-gray-500 before:opacity-0 before:transition-opacity checked:border-lines checked:bg-[#545240] checked:before:bg-[#edebd9] hover:before:opacity-10 before:checked:hover:before:opacity-10 "
                              checked={task.completed}
                                                         />
                            <span className="absolute transition-opacity opacity-0 pointer-events-none text-stone-100 top-2/4 left-2/4 -translate-y-2/4 -translate-x-2/4 peer-checked:opacity-100">
                              <svg
                                xmlns="http://www.w3.org/2000/svg"
                                className="h-3.5 w-3.5"
                                viewBox="0 0 20 20"
                                fill="currentColor"
                                stroke="currentColor"
                                strokeWidth="1">
                                <path
                                  fillRule="evenodd"
                                  d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                                  clipRule="evenodd"></path>
                              </svg>
                            </span>
                          </label>
                        </div>
                      </label>
                    </div>
                    <div>
                      <h2 className="text-xl font-bold text-[#161515] ">
                        {task.title}
                      </h2>
                      <p className="text-sm font-semibold text-[#42403f] ">
                        {task.description}
                      </p>
                      <div className="flex gap-2 mt-2 text-xs font-bold">
                        <div className="flex items-center ">
                          <img
                            src={userImages[index]}
                            alt=""
                            className="w-10 h-10 rounded-full "
                          />
                          <span> {task.assignedTo}</span>
                        </div>
                      </div>
                    </div>
                    <div
                      className="p-2 ml-auto rounded-full cursor-pointer hover:bg-red-300"
                    >
                      <FaTrash color="#545240" />
                    </div>
                  </div>
                );
              })}
          </div>
        </div>
      </div>
  
  );
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/2-UI-after-fetcing-data.png)
_UI après la récupération des données_

Après cela, rendez-vous dans votre composant `Taskform` et créez une interface de formulaire pour créer de nouvelles tâches.

```jsx
import { addSingleTask } from "./services/api";
import toast from "react-hot-toast";
import { useState } from "react";

export default function Taskform() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [assignedTo, setAssignedTo] = useState("");

  return (
    <div className="bg-[#74a0a6] p-4 rounded-md">
      <form className="flex flex-col w-full gap-2 ">
        <label htmlFor="title">
          <p className="font-bold ">Titre</p>
          <input
            type="text"
            className="w-full font-medium  focus:outline-[#74a0a6] focus-within:outline-[#74a0a6] p-1 bg-transparent border rounded-md"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </label>

        <label htmlFor="description">
          <p className="font-bold ">Description</p>
          <input
            type="text"
            className="w-full font-medium  focus:outline-[#74a0a6] focus-within:outline-[#74a0a6] p-1 bg-transparent border rounded-md"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </label>

        <label htmlFor="assignedTo">
          <p className="font-bold ">Assigné à</p>
          <input
            type="text"
            className="w-full font-medium  focus:outline-[#74a0a6] focus-within:outline-[#74a0a6] p-1 bg-transparent border rounded-md"
            value={assignedTo}
            onChange={(e) => setAssignedTo(e.target.value)}
          />
        </label>
        <button className="p-2 mt-3 border text-white rounded-md w-max hover:bg-white hover:text-[#74a0a6]">
          Ajouter
        </button>
      </form>
    </div>
  );
}

```

Après cela, importez-le dans votre composant `TaskContainer`.

```jsx
return (
   
      <div className="flex flex-col gap-8 p-4">
        <Taskform />
        <div className="p-4 shadow-lg ">
          <div className="flex flex-col gap-4 ">
            {tasks &&
              tasks.map((task, index) => {
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3-UI-with-Form-added.png)
_UI avec le formulaire ajouté_

Pour ajouter une nouvelle tâche, créez une fonction de gestion dans le `Taskform`, puis importez votre fonction `POST` depuis votre fichier API.

```js
const addTaskMutation = async (e) => {
    e.preventDefault();
    const createdAt = new Date().toISOString(); // Obtenir l'horodatage actuel sous forme de chaîne

    try {
      await addSingleTask({
        title,
        description,
        assignedTo,
        completed: false,
        createdAt,
      });

      toast.success("Tâche ajoutée avec succès.");
      setTitle("");
      setDescription("");
      setAssignedTo("");
    } catch (err) {
      toast.error("Échec de l'ajout de la nouvelle tâche.");
    }
  };
```

Enfin, appelez la fonction `mutate` après votre appel de fonction `POST` pour permettre à SWR d'invalider vos données actuelles et de faire une nouvelle requête. Vous pouvez obtenir cette fonction de mutation depuis le hook `useSWR` dans le `TaskContainer`, puis la passer via les props au formulaire.

```jsx
const {
    isLoading,
    error,
    data: tasks,
    mutate,
  } = useSWR(cacheKey, fetchTasks, {
    onSuccess: (data) =>
      data.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt)),
  });
  return (
    <div className="flex flex-col gap-8 p-4">
      <Taskform mutate={mutate} />
```

Puis appelez-la dans le `TaskForm`.

```jsx
import { addSingleTask } from "./services/api";
import toast from "react-hot-toast";
import { useState } from "react";

export default function Taskform({ mutate }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [assignedTo, setAssignedTo] = useState("");

  const addTaskMutation = async (e) => {
    e.preventDefault();
    const createdAt = new Date().toISOString();
    try {
      await addSingleTask({
        title,
        description,
        assignedTo,
        completed: false,
        createdAt,
      });
      mutate();

      toast.success("Tâche ajoutée avec succès.");
      setTitle("");
      setDescription("");
      setAssignedTo("");
    } catch (err) {
      toast.error("Échec de l'ajout de la nouvelle tâche.");
    }
  };
  return (
    <div className="bg-[#74a0a6] p-4 rounded-md">
      <form
        className="flex flex-col w-full gap-2 "
        onSubmit={(e) => addTaskMutation(e)}>
        <label htmlFor="title">
          <p className="font-bold ">Titre</p>
          <input
            type="text"
            className="w-full font-medium  focus:outline-[#74a0a6] focus-within:outline-[#74a0a6] p-1 bg-transparent border rounded-md"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </label>

        <label htmlFor="description">
          <p className="font-bold ">Description</p>
          <input
            type="text"
            className="w-full font-medium  focus:outline-[#74a0a6] focus-within:outline-[#74a0a6] p-1 bg-transparent border rounded-md"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </label>

        <label htmlFor="assignedTo">
          <p className="font-bold ">Assigné à</p>
          <input
            type="text"
            className="w-full font-medium  focus:outline-[#74a0a6] focus-within:outline-[#74a0a6] p-1 bg-transparent border rounded-md"
            value={assignedTo}
            onChange={(e) => setAssignedTo(e.target.value)}
          />
        </label>
        <button className="p-2 mt-3 border text-white rounded-md w-max hover:bg-white hover:text-[#74a0a6]">
          Ajouter
        </button>
      </form>
    </div>
  );
}
```

Tester votre composant maintenant donne le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/1-Regular-Create-Operation.gif)
_Opération de création régulière_

Comme vous pouvez le voir, la liste est mise à jour après chaque soumission de formulaire. Mais cela ne met toujours pas en évidence notre besoin d'UI optimiste. Vous vous dites probablement, si l'opération s'est déroulée si rapidement, pourquoi s'embêter avec l'UI Optimiste ?

![Image](https://www.freecodecamp.org/news/content/images/2024/07/2-What-s-the-point.gif)
_Gif : Quel est l'intérêt ?_

Eh bien, pour commencer, aucune application réelle ne pourra jamais battre la vitesse de votre serveur JSON local, car les données sont immédiatement disponibles pour vous et les utilisateurs ont souvent des connexions réseau instables.

Ralentissons la récupération pour mieux illustrer une requête de données réelle. Cela simule mieux un scénario réel, car les utilisateurs viennent souvent de différents endroits avec des vitesses Internet variables.

Commencez par créer une fonction de délai qui s'exécute avant chacun de vos appels de fonction.

```js
import axios from "axios";

const tasksApi = axios.create({
  baseURL: "http://localhost:3500",
});

export const tasksUrlEndpoint = "/tasks";

const delay = () => new Promise((res) => setTimeout(() => res(), 1200));

export const fetchTasks = async () => {
   await delay();
  const response = await tasksApi.get(tasksUrlEndpoint);
  return response.data;
};

export const addSingleTask = async ({
  title,
  description,
  completed,
  assignedTo,
  createdAt,
}) => {
  await delay();
  const response = await tasksApi.post(tasksUrlEndpoint, {
    title,
    description,
    completed,
    assignedTo,
    createdAt,
  });
  return response.data;
};

export const updateSingleTask = async (task) => {
  await delay();
  const response = await tasksApi.patch(`${tasksUrlEndpoint}/${task.id}`, task);
  return response.data;
};

export const deleteSingleTask = async ({ id }) => {
  await delay();
  return await tasksApi.delete(`${tasksUrlEndpoint}/${id}`, id);
};
```

Puis essayez à nouveau votre opération de création.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3-Create-operation-after-delay.gif)
_Opération de création après le délai_

Comme vous l'avez peut-être remarqué, l'opération de création n'a été déclenchée qu'après que la fonction de délai (d'une durée de 1,2 seconde) ait terminé son exécution, ce qui a provoqué une brève période d'inactivité à l'écran.

La manière habituelle de gérer ces périodes de chargement est généralement un indicateur de chargement ou un indicateur vous informant qu'une activité en arrière-plan est en cours. Mais cela perturbe souvent votre flux de travail lorsque vous utilisez l'application, et franchement, c'est décevant.

Le même effet statique peut être observé dans l'opération de mise à jour, où les utilisateurs doivent attendre la confirmation du serveur pour voir les nouvelles données.

```jsx
const updateTaskMutation = async (updatedTask) => {
    try {
      await updateSingleTask(updatedTask);
      mutate();
      toast.success("Tâche mise à jour avec succès");
    } catch (err) {
      toast.error("Échec de la mise à jour de la tâche.");
    }
  };

  return (
    <div className="flex flex-col gap-8 p-4">
      <Taskform mutate={mutate} />
      <div className="p-4 shadow-lg ">
        <div className="flex flex-col gap-4 ">
          {tasks &&
            tasks.map((task, index) => {
              return (
                <div
                  key={task.id}
                  className="flex gap-4 items-center py-2 px-6 rounded-md bg-[#74a0a6]">
                  <div>
                    <label
                      htmlFor={`task-${task.id}`}
                      key={task.id}
                      className={`flex gap-4 text-[14px] items-center font-bold list-none p-4 rounded bg-[#88adb3] cursor-pointer hover:bg-[#609299]`}>
                      <div className="inline-flex items-center">
                        <label
                          className="relative flex items-center p-3 rounded-full cursor-pointer"
                          htmlFor="checkbox">
                          <input
                            type="checkbox"
                            name={`task-${task.id}`}
                            id={`task-${task.id}`}
                            className="before:content[''] peer relative h-5 w-5 cursor-pointer appearance-none rounded-md border border-[#edebd9] transition-all before:absolute before:top-2/4 before:left-2/4 before:block before:h-12 before:w-12 before:-translate-y-2/4 before:-translate-x-2/4 before:rounded-full before:bg-blue-gray-500 before:opacity-0 before:transition-opacity checked:border-lines checked:bg-[#545240] checked:before:bg-[#edebd9] hover:before:opacity-10 before:checked:hover:before:opacity-10 "
                            checked={task.completed === true}
                            onChange={() =>
                              updateTaskMutation({
                                ...task,
                                completed: !task.completed,
                              })
                            }
                          />
                          <span className="absolute transition-opacity opacity-0 pointer-events-none text-stone-100 top-2/4 left-2/4 -translate-y-2/4 -translate-x-2/4 peer-checked:opacity-100">
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              className="h-3.5 w-3.5"
                              viewBox="0 0 20 20"
                              fill="currentColor"
                              stroke="currentColor"
                              strokeWidth="1">
                              <path
                                fillRule="evenodd"
                                d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                                clipRule="evenodd"></path>
                            </svg>
                          </span>
                        </label>
                      </div>
                    </label>
                  </div>
                  <div>
                    <h2 className="text-xl font-bold text-[#161515] ">
                      {task.title}
                    </h2>
                    <p className="text-sm font-semibold text-[#42403f] ">
                      {task.description}
                    </p>
                    <div className="flex gap-2 mt-2 text-xs font-bold">
                      <div className="flex items-center ">
                        <img
                          src={userImages[index]}
                          alt=""
                          className="w-10 h-10 rounded-full "
                        />
                        <span> {task.assignedTo}</span>
                      </div>
                    </div>
                  </div>
                  <div
                    className="p-2 ml-auto rounded-full cursor-pointer hover:bg-red-300"
                   >
                    <FaTrash color="#545240" />
                  </div>
                </div>
              );
            })}
        </div>
      </div>
    </div>
  );
}

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/4-Update-operation-after-delay.gif)
_Opération de mise à jour après le délai_

Et dans l'opération de suppression, qui attend également la confirmation du serveur pour réhydrater la page.

```jsx
const deleteTaskMutation = async ({ id }) => {
    try {
      await deleteSingleTask({ id });
      mutate();
      toast.success("Tâche supprimée avec succès");
    } catch (err) {
      toast.error("Échec de la suppression de la tâche.");
    }
  };
  return (
    <div className="flex flex-col gap-8 p-4">
      <Taskform mutate={mutate} />
      <div className="p-4 shadow-lg ">
        <div className="flex flex-col gap-4 ">
          {tasks &&
            tasks.map((task, index) => {
              return (
                <div
                  key={task.id}
                  className="flex gap-4 items-center py-2 px-6 rounded-md bg-[#74a0a6]">
                  <div>
                    <label
                      htmlFor={`task-${task.id}`}
                      key={task.id}
                      className={`flex gap-4 text-[14px] items-center font-bold list-none p-4 rounded bg-[#88adb3] cursor-pointer hover:bg-[#609299]`}>
                      <div className="inline-flex items-center">
                        <label
                          className="relative flex items-center p-3 rounded-full cursor-pointer"
                          htmlFor="checkbox">
                          <input
                            type="checkbox"
                            name={`task-${task.id}`}
                            id={`task-${task.id}`}
                            className="before:content[''] peer relative h-5 w-5 cursor-pointer appearance-none rounded-md border border-[#edebd9] transition-all before:absolute before:top-2/4 before:left-2/4 before:block before:h-12 before:w-12 before:-translate-y-2/4 before:-translate-x-2/4 before:rounded-full before:bg-blue-gray-500 before:opacity-0 before:transition-opacity checked:border-lines checked:bg-[#545240] checked:before:bg-[#edebd9] hover:before:opacity-10 before:checked:hover:before:opacity-10 "
                            checked={task.completed === true}
                            onChange={() =>
                              updateTaskMutation({
                                ...task,
                                completed: !task.completed,
                              })
                            }
                          />
                          <span className="absolute transition-opacity opacity-0 pointer-events-none text-stone-100 top-2/4 left-2/4 -translate-y-2/4 -translate-x-2/4 peer-checked:opacity-100">
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              className="h-3.5 w-3.5"
                              viewBox="0 0 20 20"
                              fill="currentColor"
                              stroke="currentColor"
                              strokeWidth="1">
                              <path
                                fillRule="evenodd"
                                d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                                clipRule="evenodd"></path>
                            </svg>
                          </span>
                        </label>
                      </div>
                    </label>
                  </div>
                  <div>
                    <h2 className="text-xl font-bold text-[#161515] ">
                      {task.title}
                    </h2>
                    <p className="text-sm font-semibold text-[#42403f] ">
                      {task.description}
                    </p>
                    <div className="flex gap-2 mt-2 text-xs font-bold">
                      <div className="flex items-center ">
                        <img
                          src={userImages[index]}
                          alt=""
                          className="w-10 h-10 rounded-full "
                        />
                        <span> {task.assignedTo}</span>
                      </div>
                    </div>
                  </div>
                  <div
                    className="p-2 ml-auto rounded-full cursor-pointer hover:bg-red-300"
                    onClick={() => deleteTaskMutation({ id: task.id })}>
                    <FaTrash color="#545240" />
                  </div>
                </div>
              );
            })}
        </div>
      </div>
    </div>
  );
}

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/5-Delete-operation-after-delay.gif)
_Opération de suppression après le délai_

Ces quelques secondes d'inactivité ou de chargement peuvent impacter le niveau de satisfaction des utilisateurs de votre application, c'est pourquoi nous allons utiliser l'UI Optimiste pour le corriger.

### UI CRUD Optimiste

En termes pratiques, cela fonctionne de la manière suivante : lorsque vous effectuez une action, elle est immédiatement ajoutée à l'état de votre UI (cache) tandis que l'opération asynchrone s'exécute en arrière-plan.

Si l'opération réussit, rien ne change dans l'UI et tout se comporte comme si cela avait fonctionné du premier coup. Mais si elle échoue, l'état de l'UI revient à son état précédent et une erreur est affichée via votre toast.

Une approche d'UI optimiste offre une bien meilleure expérience utilisateur que les messages de chargement traditionnels ou les indicateurs de progression. Lorsque vous voyez une réponse immédiate après avoir cliqué sur un bouton, l'application semble plus rapide et plus réactive, vous gardant engagé et satisfait. Vous pouvez continuer à interagir avec l'application de manière fluide, sans attendre les confirmations du serveur, rendant l'expérience plus fluide et plus intuitive.

Ce retour immédiat réduit votre temps d'attente perçu et maintient l'interface visuellement stable, évitant les clignotements gênants ou les changements soudains. De plus, lorsque l'application semble aussi réactive, vous êtes plus susceptible de continuer à l'utiliser et d'avoir une expérience positive.

En revanche, les messages de chargement ou les indicateurs de progression peuvent interrompre votre flux, rendant l'application plus lente et potentiellement frustrante.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Group-369-1.png)
_Diagramme de l'UI Optimiste_

Cela semble encore un peu comme du charabia, n'est-ce pas ? Eh bien, apprenons en cours de route !

Dans votre fichier `swrAPI`, créez une autre fonction de mutation. Cette fonction prend deux paramètres : la nouvelle tâche que vous souhaitez ajouter et la liste des tâches déjà existantes.

```js
export const addTaskMutation = async (newTask, tasks) => {
  };
```

Ensuite, elle utilise votre fonction `create` déjà existante pour tenter de créer une nouvelle tâche. Après cela, vous stockez le résultat et retournez ce résultat dans un nouveau tableau, avec les tâches déjà existantes.

```js
export const addTaskMutation = async (newTask, tasks) => {
  const addedTask = await addSingleTask(newTask);
  return [...tasks, addedTask].sort(
    (a, b) => new Date(b.createdAt) - new Date(a.createdAt)
  );
};
```

Comme vous pouvez le suspecter, cette fonction fait la même chose que la fonction `create` précédente que nous avons écrite, mais c'est ce qui vient ensuite que nous recherchons.

Ensuite, créez une fonction `options` qui est responsable de traiter l'opération asynchrone comme une opération synchrone et qui renvoie immédiatement une réponse.

Cette fonction prend également certains paramètres tels que :

* **`optimisticData`** : qui est la nouvelle donnée que vous souhaitez afficher immédiatement.
* **`rollbackOnError`** : qui rétablit l'état précédent si la requête échoue.
* **`populateCache`** : qui définit immédiatement cette donnée optimiste dans notre état d'UI.
* **`revalidate`** : qui nous permet d'activer ou de désactiver une autre récupération après l'exécution de cette fonction.

```js
export const addTaskOptions = (newTask, tasks) => {
  return {
    optimisticData: [...tasks, newTask].sort(
      (a, b) => new Date(b.createdAt) - new Date(a.createdAt)
    ),
    rollbackOnError: true,
    populateCache: true,
    revalidate: false,
  };
};
```

Pour utiliser cette méthode d'UI optimiste avec une opération `create`, importez les deux fonctions dans votre `TaskForm`. Les deux fonctions doivent être enveloppées dans la fonction `mutate` puisqu'elles tentent toutes deux de muter les données.

```jsx
import {
  addTaskMutation as addSingleTask,
  addTaskOptions,
} from "./services/swrAPI";

import toast from "react-hot-toast";
import { useState } from "react";

export default function Taskform({ mutate, tasks }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [assignedTo, setAssignedTo] = useState("");

  const addTaskMutation = async (e) => {
    e.preventDefault();
    const createdAt = new Date().toISOString();
    try {
     
      await mutate(
        addSingleTask(
          {
            title,
            description,
            assignedTo,
            completed: false,
            createdAt,
          },
          tasks
        ),
        addTaskOptions(
          {
            title,
            description,
            assignedTo,
            completed: false,
            createdAt,
          },
          tasks
        )
      ); 
     toast.success("Tâche ajoutée avec succès.");

    } catch (err) {
      toast.error("Échec de l'ajout de la nouvelle tâche.");
    }
  };
```

**Note** : Le tableau des tâches est passé dans le `TaskForm` via les props pour que cette fonctionnalité fonctionne.

Pour voir des cas où il pourrait y avoir une erreur, donnez à vos fonctions une chance de 50/50 de succès ou d'échec, en ajoutant une condition aléatoire.

```js
export const addSingleTask = async ({
  title,
  description,
  completed,
  assignedTo,
  createdAt,
}) => {
  await delay();
  if (Math.random() < 0.5) throw new Error("Échec de l'ajout de la nouvelle tâche");
  const response = await tasksApi.post(tasksUrlEndpoint, {
    title,
    description,
    completed,
    assignedTo,
    createdAt,
  });
  return response.data;
};

export const updateSingleTask = async (task) => {
  await delay();
  if (Math.random() < 0.5) throw new Error("Échec de la mise à jour de la tâche");
  const response = await tasksApi.patch(`${tasksUrlEndpoint}/${task.id}`, task);
  return response.data;
};

export const deleteSingleTask = async ({ id }) => {
  await delay();
  if (Math.random() < 0.5) throw new Error("Échec de la mise à jour de la tâche");
  return await tasksApi.delete(`${tasksUrlEndpoint}/${id}`, id);
};
```

Tester votre endpoint `create` maintenant donne le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/6-Optimistic-UI-with-Create-operation.gif)
_UI Optimiste avec l'opération de création_

Et voilà ! Votre application est officiellement optimiste. Elle tente d'ajouter immédiatement la nouvelle tâche à la liste même si elle échoue et revient élégamment en arrière en cas d'erreur.

Cela fonctionne de manière similaire pour l'opération de mise à jour – en commençant par la fonction `update` mise à jour :

```js
export const updateTaskMutation = async (updatedTask, tasks) => {
  const updatedTaskResponse = await updateSingleTask(updatedTask);
  return tasks.map((task) =>
    task.id === updatedTask.id ? updatedTaskResponse : task
  );
};
```

Puis sa fonction `options` correspondante :

```js
export const updateTaskOptions = (updatedTask, tasks) => {
  return {
    optimisticData: tasks.map((task) =>
      task.id === updatedTask.id ? updatedTask : task
    ),
    rollbackOnError: true,
    populateCache: true,
    revalidate: false,
  };
};
```

Pour tester cela, importez la nouvelle fonction `updateSingleTask` et `updateOptions` dans votre `TaskConatiner`, et mettez à jour la fonction de gestion.

```jsx
const updateTaskMutation = async (updatedTask) => {
    try {
      await mutate(
        updateSingleTask(updatedTask, tasks),
        updateTaskOptions(updatedTask, tasks)
      );
      toast.success("Tâche mise à jour avec succès");
    } catch (err) {
      toast.error("Échec de la mise à jour de la tâche.");
    }
  };
```

Ce qui donne le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/7-Optimistic-UI-with-Update-operation---fix-gif.gif)
_UI Optimiste avec l'opération de mise à jour_

Et enfin pour l'action de suppression :

```js
// Fonction pour supprimer une tâche
export const deleteTaskMutation = async (taskToDelete, tasks) => {
  await deleteSingleTask(taskToDelete);
  return tasks.filter((task) => task.id !== taskToDelete.id);
};

// Options pour supprimer une tâche
export const deleteTaskOptions = (taskToDelete, tasks) => {
  return {
    optimisticData: tasks.filter((task) => task.id !== taskToDelete.id),
    rollbackOnError: true,
    populateCache: true,
    revalidate: false,
  };
};

```

Qui peut être utilisé dans le gestionnaire de suppression `TaskContainer` comme suit :

```jsx
const deleteTaskMutation = async ({ id }) => {
    try {
      await mutate(
        deleteSingleTask({ id }, tasks),
        deleteTaskOptions({ id }, tasks)
      );
      toast.success("Tâche supprimée avec succès");
    } catch (err) {
      toast.error("Échec de la suppression de la tâche.");
    }
  };
```

Ce qui donne ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/8-Optimistic-UI-with-Delete-operation.gif)
_UI Optimiste avec l'opération de suppression_

## Inconvénients de l'UI Optimiste

Maintenant, vous devez vous dire, si l'UI optimiste est si géniale, pourquoi ne pas l'utiliser partout ?

![Image](https://www.freecodecamp.org/news/content/images/2024/07/lighter-hairspray.gif)
_Gif de laque plus légère_

Eh bien, comme tout, cette action devient chaotique sans modération. Voici quelques raisons pour lesquelles vous devriez utiliser l'UI optimiste avec modération.

1. **Mises à jour excessives** : L'UI optimiste peut s'emballer un peu avec les mises à jour, surtout si votre application va plus vite que votre connexion Internet. Trop de mises à jour peuvent ralentir les choses, il est donc essentiel de trouver un équilibre.
2. **Exposition de la logique côté serveur** : Bien qu'il soit tentant de décharger toute l'intelligence à votre application (comme générer des identifiants uniques ou vérifier si ce nom d'utilisateur est déjà pris), n'oubliez pas que votre serveur joue également un rôle crucial. Laisser le front-end de votre application gérer tout peut entraîner des risques de sécurité et un code désordonné, alors soyez attentif à l'endroit où vous placez votre logique.
3. **Gestion des incidents** : Bien que l'UI optimiste s'attende généralement à une navigation fluide, la vie a une façon de lancer des balles courbes. D'un hoquet Internet soudain à un serveur prenant une pause café inattendue, les pépins peuvent être assez difficiles à gérer avec grâce.
4. **Éviter les changements rapides** : Imaginez ajouter un article à votre panier, puis décider de le supprimer avant même que la requête "ajouter" n'atteigne le serveur. C'est comme changer d'avis à la caisse – un peu déroutant, n'est-ce pas ? Des changements rapides comme ceux-ci peuvent laisser votre application désorientée, il est donc préférable de procéder avec prudence.

## Cas d'utilisation idéaux pour l'UI Optimiste

Bien que l'UI optimiste ne soit peut-être pas le Saint-Graal de la gestion d'état que vous espériez découvrir, elle a quelques bons cas d'utilisation tels que :

1. **Applications de messagerie instantanée** : Presque toutes les plateformes de messagerie instantanée utilisent actuellement ce modèle. Vos messages apparaissent instantanément dans la fenêtre de chat, même avant d'être confirmés par le serveur. Cela crée une expérience de chat fluide et réactive, maintenant la conversation sans effort.
2. **Outils d'édition collaboratifs** : Que vous travailliez sur un document avec des collègues ou collaboriez sur un projet avec des coéquipiers, l'UI optimiste garantit que les changements sont reflétés en temps réel. Lorsque vous tapez, éditez ou faites des mises à jour, vos changements sont immédiatement visibles pour les autres, favorisant la collaboration et la productivité.
3. **Flux de réseaux sociaux** : Faites défiler votre flux de réseaux sociaux, et vous verrez des publications, des likes et des commentaires apparaître comme par magie. L'UI optimiste garantit que les interactions, telles que l'appréciation d'une publication ou la rédaction d'un commentaire, sont reflétées instantanément, offrant une expérience de navigation plus engageante.
4. **Sites de commerce électronique** : L'ajout d'articles à votre panier, la mise à jour des quantités et le passage à la caisse devraient se faire en un clin d'œil. L'UI optimiste accélère le processus d'achat en mettant immédiatement à jour votre panier et en affichant des commentaires, tels que la disponibilité des articles ou les changements de prix, sans délai.

Pour votre commodité, voici quelques ressources dont vous pourriez avoir besoin :

* [Code de démarrage](https://github.com/Daiveedjay/Optimistic-UI-with-SWR/tree/starter)
* [Code final](https://github.com/Daiveedjay/Optimistic-UI-with-SWR/tree/final)

J'aimerais remercier [Dave Gray](https://x.com/yesdavidgray?t=DlFXltzVgL_iokc_225Fgw&s=08). C'est [sa vidéo YouTube](https://www.youtube.com/watch?v=6gb6oyO1Tyg) qui a inspiré cet article.

## Conclusion

Alors que nous concluons notre plongée dans l'UI Optimiste, il est clair que cette technique peut être un changement de jeu pour l'expérience utilisateur. C'est la rapidité de votre message qui apparaît instantanément ou de votre panier d'achat qui se met à jour en temps réel.

L'UI Optimiste concerne la vitesse ainsi que la manière dont elle fait sentir les utilisateurs – connectés, autonomes et ravis. Alors, la prochaine fois que vous cliquerez et verrez la magie se dérouler, rappelez-vous : ce n'est pas juste du code... c'est le pouls du bonheur des utilisateurs (pas une pub pour Coca-Cola 😊). Gardez cette magie vivante dans vos applications !

Bon codage, et passez une journée optimiste !

**Vous aimez mes articles ?**

N'hésitez pas à [m'offrir un café ici](https://www.buymeacoffee.com/JajaDavid), pour garder mon cerveau en marche et fournir plus d'articles comme celui-ci.

![coffee-tom](https://www.freecodecamp.org/news/content/images/2024/06/coffee-tom.gif)
_Café Tom_

### **Informations de contact**

Vous souhaitez me contacter ou me connecter ? N'hésitez pas à me contacter sur les plateformes suivantes :

* Twitter / X : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : Jajadavidjid@gmail.com