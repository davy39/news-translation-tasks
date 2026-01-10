---
title: Comment corriger les fuites de mémoire dans les applications React
subtitle: ''
author: Olaleye Blessing
co_authors: []
series: null
date: '2025-09-24T19:17:26.321Z'
originalURL: https://freecodecamp.org/news/fix-memory-leaks-in-react-apps
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758741256644/817dba0f-bf49-424c-9b13-86bf81dc327f.png
tags:
- name: React
  slug: reactjs
- name: optimization
  slug: optimization
seo_title: Comment corriger les fuites de mémoire dans les applications React
seo_desc: Have you ever noticed your React application getting slower the longer you
  use it? This could be a result of memory leaks. Memory leaks are a common performance
  issue in React applications. They can slow down your application, crash your browser,
  and...
---

Avez-vous déjà remarqué que votre application React ralentit au fur et à mesure que vous l'utilisez ? Cela pourrait être le résultat de fuites de mémoire. Les fuites de mémoire sont un problème de performance courant dans les applications React. Elles peuvent ralentir votre application, faire planter votre navigateur et frustrer les utilisateurs.

Dans ce tutoriel, vous apprendrez ce qui cause les fuites de mémoire et comment les corriger.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Que sont les fuites de mémoire dans React ?](#heading-que-sont-les-fuites-de-memoire-dans-react)
    
* [Quand un composant se démonte-t-il ?](#heading-quand-un-composant-se-demonte-t-il)
    
* [Causes communes des fuites de mémoire et comment les corriger](#heading-causes-communes-des-fuites-de-memoire-et-comment-les-corriger)
    
    * [Écouteurs d'événements](#heading-ecouteurs-devenements)
        
    * [Timers](#heading-timers)
        
    * [Abonnements](#heading-abonnements)
        
    * [Opérations asynchrones](#heading-operations-asynchrones)
        
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de continuer, assurez-vous d'avoir :

* Des connaissances de base en JavaScript, React et les React hooks
    
* Une compréhension de la gestion des événements, des timers et des appels asynchrones
    
* Un environnement de développement React.
    

Si vous n'avez pas d'environnement de développement React, vous pouvez vous rendre sur le [repo memory-leak](https://github.com/Olaleye-Blessing/freecodecamp-fix-memory-leak). Exécutez les commandes ci-dessous pour le configurer :

```bash
# clone the repo
git clone <https://github.com/Olaleye-Blessing/freecodecamp-fix-memory-leak.git>

# navigate to the folder
cd freecodecamp-fix-memory-leak.git

# install the packages
pnpm install

# start development
pnpm dev
```

## Que sont les fuites de mémoire dans React ?

En JavaScript, les fuites de mémoire surviennent lorsqu'une application alloue de la mémoire mais ne parvient pas à la libérer. Cela se produit même lorsque la mémoire n'est plus nécessaire.

Dans React, les fuites de mémoire se produisent lorsqu'un composant crée des ressources mais ne les supprime pas lorsqu'il se démonte. Ces ressources peuvent être des écouteurs d'événements, des timers ou des abonnements.

Plus un utilisateur reste longtemps dans l'application, plus ces ressources non libérées s'accumulent. Cette accumulation oblige l'application à consommer plus de RAM. Cela finira par entraîner plusieurs problèmes :

* Une application lente
    
* Le plantage du navigateur
    
* Une mauvaise expérience utilisateur
    

Par exemple, un composant peut créer un écouteur d'événement « resize » lors de son montage, mais oublier de le supprimer lors de son démontage. Cela accumule de la mémoire à mesure que l'utilisateur reste dans l'application et redimensionne l'écran.

## Quand un composant se démonte-t-il ?

Un composant se démonte lorsqu'il n'existe plus dans le DOM. Cela peut arriver si :

1. Un utilisateur quitte la page.
    
    ```typescript
    <Routes>
      <Route path="/posts" element={<Posts />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
    ```
    
    Le composant dashboard se démontera immédiatement lorsqu'un utilisateur naviguera de `/dashboard` vers n'importe quelle autre route de l'application.
    
2. Un composant est rendu de manière conditionnelle.
    
    ```typescript
    function App() {
      const [show, setShow] = useState(true);
    
      return <div>{show && <Component />}</div>;
    }
    ```
    
    `<Component />` se démontera lorsque `show` deviendra faux.
    
3. La clé d'un composant change.
    
    ```typescript
    function App() {
      const [key, setKey] = useState(Date.now());
    
      return (
        <>
          <button onClick={() => setKey(Date.now())}>Change Key</button>
          <Form key={key} />
        </>
      );
    }
    ```
    
    Le composant `<Form />` se démontera à chaque fois que la clé change. Notez également qu'un nouveau composant `<Form />` sera monté à chaque changement de clé.
    

## Causes communes des fuites de mémoire et comment les corriger

Comme indiqué précédemment, il y aura une fuite de mémoire lorsque les ressources ne sont pas supprimées après le démontage d'un composant. Le hook `useEffect` de React vous permet de renvoyer une fonction qui sera appelée lors du démontage du composant.

```typescript
useEffect(() => {
  return () => {
    // code to remove resources
  };
}, []);
```

Vous pouvez nettoyer toutes les ressources créées dans cette fonction de retour. Nous allons passer en revue la manière de nettoyer certaines de ces ressources.

### Écouteurs d'événements

Les écouteurs d'événements persistent s'ils ne sont pas supprimés après le démontage d'un composant. Regardez le code ci-dessous :

```typescript
import { useEffect, useState } from "react";

const EventListener = () => {
  const [windowWidth, setWindowWidth] = useState(0);

  useEffect(() => {
    function handleResize() {
      const width = window.innerWidth;
      console.log("__ Resizing Event Listerner __", width);
      setWindowWidth(width);
    }

    window.addEventListener("resize", handleResize);
  }, []);

  return <div>Width is: {windowWidth}</div>;
};

export default EventListener;
```

Nous ne supprimons pas l'écouteur d'événement de redimensionnement au démontage, donc chaque montage ajoute un nouvel écouteur. Ce défaut de nettoyage entraîne une fuite de mémoire.

![Le GIF montre plusieurs écouteurs d'événements 'resize' créés à chaque montage d'un composant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758149182882/58ddc026-d6b8-4120-9144-53b6d87fb63e.gif align="center")

Comme le montre le GIF ci-dessus, nous enregistrons la largeur dans la console chaque fois que nous redimensionnons la fenêtre. Nous enregistrons toujours les mêmes informations après le démontage du composant. De plus, lorsque nous vérifions l'onglet « Event Listeners », le nombre d'écouteurs continue d'augmenter de 2 au lieu d'être de seulement 1 à chaque remontage du composant.

Nous voyons deux écouteurs lors du montage du composant car React utilise StrictMode en développement. Cela aide à voir les effets secondaires en mode développement. C'est la même raison pour laquelle les écouteurs augmentent de 2 à chaque montage du composant.

Pour corriger cette fuite de mémoire, nous devons supprimer l'écouteur d'événement dans notre fonction de nettoyage.

```typescript
useEffect(() => {
  // previous code

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

La fonction de nettoyage s'exécute lors du démontage du composant. Cela, à son tour, supprime notre écouteur d'événement et empêeche une fuite de mémoire.

![Le GIF montre un écouteur d'événement 'resize' qui est supprimé lorsque le composant se démonte.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758149497654/f95d75b4-f41f-4bb0-806b-546555be813a.gif align="center")

Remarquez cette fois que rien ne s'affiche dans la console lorsque nous masquons le composant. De plus, l'écouteur d'événement de redimensionnement a été réduit à 0 lorsque nous avons masqué (démonté) le composant, et est passé à 1 lorsque nous l'avons affiché (monté).

### Timers

Les timers comme `setInterval` et `setTimeout` peuvent également causer des fuites de mémoire s'ils ne sont pas effacés après le démontage du composant. Regardez ceci :

```typescript
const Timers = () => {
  const [countDown, setCountDown] = useState(0);

  useEffect(() => {
    setInterval(() => {
      console.log("__ Set Interval __");
      setCountDown((prev) => prev + 1);
    }, 1000);
  }, []);

  console.log({ countDown });

  return <div>Countdown: {countDown}</div>;
};
```

L'intervalle continuera de s'exécuter même après que React a masqué ou démonté le composant.

Notez que, dans React 18+, React ignore une mise à jour d'état lorsqu'un composant est déjà démonté.

![Le GIF montre un composant de compte à rebours qui continue de s'exécuter et de mettre à jour l'état après avoir été démonté du DOM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758149517577/34868e3e-e8f6-495a-a2f8-ef0e1e745051.gif align="center")

Dans le GIF, nous remarquons que la console cesse d'afficher "__ Outside effect " chaque fois que nous masquons/démontons le composant. Mais la chaîne " Interval __" s'affiche à chaque fois.

Nous pouvons corriger cela en utilisant la fonction de nettoyage. Tous les timers (`setInterval`, `setTimeout`) renvoient un identifiant de timer unique que nous pouvons utiliser pour effacer le timer après le démontage du composant.

```typescript
const [countDown, setCountDown] = useState(0);
useEffect(() => {
  const timer = setInterval(() => {
    console.count("__ Interval __");
    setCountDown((prev) => prev + 1);
  }, 1000);

  return () => {
    clearInterval(timer);
  };
}, []);
```

Nous sauvegardons maintenant l'ID du timer et utilisons cet ID pour effacer l'intervalle lors du démontage du composant. La même méthode s'applique à `setTimeout` ; sauvegardez l'ID et effacez-le avec `clearTimeout`.

![Le GIF montre un composant de compte à rebours qui s'arrête de s'exécuter et de mettre à jour l'état après son démontage.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758149580900/7c37c824-93db-4b73-8ff4-c45c6404bb65.gif align="center")

### Abonnements

Lorsqu'un composant s'abonne à des données externes, il est toujours approprié de se désabonner après le démontage du composant. La plupart des sources de données renvoient une fonction de rappel pour se désabonner de ces données. Prenons Firebase pour exemple :

```typescript
import { collection, onSnapshot } from "firebase/firestore";
import { useEffect } from "react";

const Subscriptions = () => {
  useEffect(() => {
    const unsubscribe = onSnapshot(collection(db, "cities"), () => {
		// Respond to data
		// ...
	});
  }, [])
  
	return <div>Subscriptions</div>;
};

export default Subscriptions;
```

La fonction `onSnapshot` de `firebase/firestore` obtient des mises à jour en temps réel de notre base de données. Elle renvoie une fonction de rappel qui arrête d'écouter les mises à jour de la DB. Si vous ne parvenez pas à appeler cette fonction, notre application continue d'écouter ces mises à jour même lorsqu'elle n'en a plus besoin.

```typescript
useEffect(() => {
  const unsubscribe = onSnapshot(collection(db, "cities"), () => {
    // Respond to data
    // ...
  });

  return () => {
    unsubscribe();
  };
}, []);
```

Appeler `unsubscribe()` dans la fonction retournée signifie que nous ne sommes plus intéressés par l'écoute des mises à jour de données.

### Opérations asynchrones

Une erreur courante consiste à ne pas annuler un appel API lorsqu'il n'est plus nécessaire. C'est un gaspillage de ressources que de laisser un appel API continuer à s'exécuter lorsque le composant se démonte. En effet, le navigateur continue de conserver des références en mémoire jusqu'à ce que la promesse soit résolue. Regardez cet exemple :

```typescript
import { useEffect, useState } from "react";

interface Post {
  id: string;
  title: string;
  views: number;
}

const ApiCall = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [data, setData] = useState<Post[] | null>(null);

  useEffect(() => {
    const getTodos = async () => {
      try {
        setLoading(true);

        console.time("POSTS");
        const req = await fetch("<http://localhost:3001/posts>");
        const res = await req.json();
        console.timeLog("POSTS");
        setData(res.posts);
      } catch (error) {
        setError("Try again");
      } finally {
        setLoading(false);
      }
    };

    getTodos();
  }, []);

  return (
    <div style={{ marginTop: "2rem" }}>
      <p>ApiCall Component</p>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>{error}</p>
      ) : data ? (
        <p>Views: {data[0].views}</p>
      ) : null}
    </div>
  );
};

export default ApiCall;
```

Ce composant récupère une liste de publications de notre serveur dès qu'il est monté. Il modifie l'interface utilisateur en fonction de l'état de l'appel API :

* Il affiche un texte de chargement lorsque vous cliquez sur le bouton.
    
* Il affiche une erreur si l'API échoue.
    
* Il affiche les données si l'API réussit.
    

Nous avons un serveur simple qui renvoie la liste des publications. Le problème avec le serveur est qu'il lui faut trois secondes pour renvoyer la liste.

Que se passe-t-il lorsqu'un utilisateur arrive sur cette page mais décide de la quitter avant trois secondes ? (Nous simulons le départ de la page en cliquant sur le bouton Hide Component.)

![Le GIF montre un composant qui continue un appel API après son démontage.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758149803784/bf5cf55f-75fe-472f-9a08-653c53bdafaa.gif align="center")

Comme vous pouvez le voir, le navigateur conserve toujours une référence à la requête même si elle n'est plus nécessaire.

Une manière appropriée de corriger cela est d'annuler la requête lorsque le composant se démonte. Nous pouvons le faire en utilisant l'[AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController). Nous pouvons utiliser la méthode `abort` pour annuler la requête avant qu'elle ne soit terminée, libérant ainsi de la mémoire.

```typescript
import { useEffect, useState } from "react";

interface Post {
  id: string;
  title: string;
  views: number;
}

const ApiCall = () => {
  // previous code

  useEffect(() => {
    const controller = new AbortController();

    const getTodos = async () => {
      try {
        // previous code

        const req = await fetch("<http://localhost:3001/posts>", {
          signal: controller.signal,
        });

        // previous code
      } catch (error) {
        if (error instanceof Error && error.name === "AbortError") {
          console.log("Request was cancelled");
          return;
        }

        setError("Try again");
      } finally {
        setLoading(false);
      }
    };

    getTodos();

    return () => {
      controller.abort();
    };
  }, []);

  return (
    <div style={{ marginTop: "2rem" }}>
      <p>ApiCall Component</p>
      {/* previous code */}
    </div>
  );
};

export default ApiCall;
```

Nous avons créé un contrôleur pour suivre notre requête API lors du montage du composant. Nous attachons ensuite le contrôleur à notre requête API. Notre fonction de nettoyage annule la requête si les utilisateurs quittent la page dans les trois secondes.

Nous pouvons voir le résultat de cela dans le GIF ci-dessous :

![Le GIF montre un appel API en cours d'annulation après le démontage de son composant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758149811531/5497edbd-050c-4059-b088-239e8c5b65ef.gif align="center")

La plupart des applications React en production utilisent des bibliothèques externes pour effectuer des appels API. Par exemple, [react query](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation#using-fetch) nous permet d'annuler une promesse en cours :

```typescript
const query = useQuery({
  queryKey: ["todos"],
  queryFn: async ({ signal }) => {
    const todosResponse = await fetch("/todos", { signal });
    const todos = await todosResponse.json();

    return todos;
  },
});
```

## Conclusion

Les fuites de mémoire peuvent avoir un impact significatif sur les performances de votre application React et sur l'expérience utilisateur. Vous pouvez prévenir ces problèmes en nettoyant correctement les ressources lorsqu'un composant se démonte. En résumé, n'oubliez jamais de :

* Supprimer les écouteurs d'événements avec `removeEventListener`.
    
* Effacer les timers avec `clearInterval` et `clearTimeout`.
    
* Se désabonner des sources de données externes.
    
* Annuler les requêtes API à l'aide d'un `AbortController`.