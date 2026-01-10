---
title: Qu'est-ce que la bibliothèque tRPC ? Explications avec un projet de démonstration
subtitle: ''
author: Afan Khan
co_authors: []
series: null
date: '2024-07-11T19:09:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-trpc
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/trpc-image.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que la bibliothèque tRPC ? Explications avec un projet de démonstration
seo_desc: 'For a while now, I''ve been noticing a technology named tRPC that''s cited
  in many modern tech stacks, including T3. But I didn''t know what it was or why
  it had become so popular.

  So I began researching and learning about it. I didn''t know what it mean...'
---

Depuis quelque temps, je remarque une technologie nommée [tRPC](https://trpc.io/) qui est citée dans de nombreuses piles technologiques modernes, y compris [T3](https://create.t3.gg/). Mais je ne savais pas ce que c'était ni pourquoi elle était devenue si populaire.

J'ai donc commencé à faire des recherches et à apprendre à son sujet. Je ne savais pas ce que cela signifiait ni quel était son but. J'ai donc creusé davantage du côté de [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call), [gRPC](https://en.wikipedia.org/wiki/GRPC) et d'autres technologies pour le découvrir.

J'ai découvert que tRPC est un style architectural sécurisé au niveau des types (type-safe) pour la conception d'API. Mais cette définition n'est que la partie émergée de l'iceberg.

Dans cet article, je veux aller plus loin dans les racines de cet iceberg et comprendre ce qu'est tRPC. Cet article est une explication approfondie de tRPC, de pourquoi nous en avons besoin et de comment l'utiliser.

Notez que je suis un apprenant comme vous qui écrit cet article. J'explore tRPC pour la première fois à vos côtés, sur la base des articles que j'ai étudiés. Il s'adresse aux débutants et aux nouveaux apprenants. Plongeons-y ensemble.

## Prérequis

1. Connaissances intermédiaires en JavaScript.
    
2. Connaissances de base en TypeScript.
    
3. Connaissances intermédiaires en React.
    
4. Expérience avec Fetch et l'API REST.
    
5. Expérience de l'utilisation d'un terminal ou d'une console.
    
6. Expérience de l'utilisation de NPM et de ses commandes.
    
7. Expérience de l'utilisation de CORS et de la connexion front-end/back-end.
    
8. Aimer apprendre quelque chose de nouveau.
    

Vous pouvez trouver le dépôt GitHub et toutes les autres ressources pour cet article [ici](https://github.com/whyafan/trpc-demo).

## Table des matières

1. [Qu'est-ce que tRPC ?](#heading-questcetrpc)
    
2. [Pourquoi avons-nous besoin de tRPC ?](#heading-pourquoiavonsnousbesoindetrpc)
    
3. [Comment utiliser tRPC](https://www.freecodecamp.org/news/p/96029b5d-38ad-4b3c-a021-661b70eb6dd3/how-to-use-trpc)
    
4. [Conclusion](https://www.freecodecamp.org/news/p/96029b5d-38ad-4b3c-a021-661b70eb6dd3/conclusion)
    

## Qu'est-ce que tRPC ?

[tRPC](https://trpc.io/) est une bibliothèque basée sur TypeScript et sécurisée au niveau des types qui exploite la conception d'API RPC pour traiter les requêtes API et fournir une réponse.

[RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) signifie Remote Procedural Call (Appel de procédure distante). Notre tRPC s'appuie sur RPC. RPC est un style architectural pour concevoir des API comme [REST](https://www.ibm.com/topics/rest-apis). En utilisant RPC, vous vous débarrassez de [Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) et de l'API [REST API](https://www.ibm.com/topics/rest-apis).

Comme son nom l'indique, tRPC ajoute une couche de sécurité des types (type safe) sur la conception architecturale RPC. Traditionnellement, nous utilisons l'API REST. Elle possède [GET, POST, PULL et d'autres types de requêtes](https://restfulapi.net/http-methods/). Dans tRPC, il n'y a pas de types de requêtes.

Chaque requête vers le back-end tRPC passe par un système de requête (query) et reçoit une réponse du back-end tRPC basée sur l'entrée et la requête.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-10.png align=\"left\")

*Source :* [*Adeesh Sharma*](https://adeesh.hashnode.dev/building-an-express-trpc-and-react-monorepo-setup-with-yarn-workspaces-tailwind-zod-and-react-query)

À la place, des fonctions intégrées sont disponibles avec tRPC et react-query pour traiter vos requêtes. Chaque requête est traitée de la même manière. Cela dépend si le point de terminaison (endpoint) de l'API accepte une entrée, renvoie une sortie, la mute, et ainsi de suite.

Lors de l'utilisation de REST, vous créez un dossier principal nommé `/api` et des fichiers de routage à l'intérieur. Pour tRPC, vous n'avez pas besoin de dossier avec de nombreux fichiers. Vous avez besoin de quelques fonctions intégrées et d'un système react-query simplifié.

Vous n'avez pas besoin d'utiliser `fetch()`, de traiter la sortie, etc. tRPC fonctionne en utilisant des URL représentant une requête spécifique, comme vous le verrez bientôt.

### Pourquoi avons-nous besoin de tRPC ?

tRPC rend le RPC sécurisé au niveau des types. Cela signifie que votre client ne peut pas envoyer de données que le serveur ne peut pas accepter. Je ne peux pas passer une chaîne de caractères pour une propriété basée sur un nombre.

Si le client essaie de faire cela, vous recevrez immédiatement une erreur — **Type invalide**. L'IDE et les navigateurs renvoient des erreurs si les types de données ne correspondent pas.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/type-error.png align=\"left\")

*Erreur de sécurité des types tRPC après avoir soumis une valeur de type de données inattendue*

La sécurité des types est cruciale pour les applications utilisant JavaScript. tRPC exploite donc [TypeScript](https://www.typescriptlang.org/). Cela facilite la création de routes et l'exécution d'opérations sur le back-end.

tRPC nécessite une bibliothèque nommée [Zod](https://zod.dev/). Elle aide tRPC à construire le schéma de données de chaque route. Un schéma est un objet avec des propriétés et un type de données équivalent lié à chaque propriété.

Par exemple, si une route d'API nécessite les détails de l'utilisateur, vous créeriez un objet sur le back-end et assigneriez un type de données à chaque propriété à l'aide de Zod.

Sur le front-end, tRPC vérifiera si les données fournies par l'utilisateur ou la requête API correspondent aux types de données enregistrés par le back-end. tRPC exploite cette intégration sécurisée au niveau des types entre le front-end et le back-end.

Voyons comment tRPC, Zod et d'autres bibliothèques fonctionnent ensemble dans un projet de démonstration.

## Comment utiliser tRPC

Vous pouvez lancer un serveur Express en quelques secondes et commencer à écrire des routes et des requêtes tRPC — c'est facile.

Traditionnellement, le côté client (front-end) et le côté serveur (back-end) sont séparés. Nous suivrons cette séparation pour cet exemple.

Commençons par créer le côté client avec React et le côté serveur avec Express + CORS pour les connecter.

### Structure des dossiers

Tout d'abord, créez un répertoire nommé `tRPC Demo`. À l'intérieur de ce répertoire, créez un autre répertoire nommé `trpclibrary` pour séparer les côtés client et serveur et les exécuter ensemble en tant que bibliothèque plus tard.

Dans le répertoire `trpclibrary`, vous placerez bientôt votre serveur (Express) et votre client (React).

Dans le répertoire racine `tRPC Demo`, insérez un fichier `package.json` avec le code suivant pour interconnecter tous les dossiers et exécuter le client et le serveur avec une seule commande.

```json
{
  "name": "trpclibrary",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "private": true,
  "scripts": {
    "start": "concurrently \"wsrun --parallel start\""
  },
  "workspaces": [
    "trpclibrary/*"
  ],
  "devDependencies": {
    "concurrently": "^5.2.0",
    "wsrun": "^5.2.0"
  }
}
```

Après avoir configuré le `package.json` dans le répertoire racine, vous commencerez par configurer votre serveur Express à l'intérieur du répertoire `trpclibrary`.

Conseil : Utilisez la commande `cd <nom_du_dossier>` pour entrer dans un dossier à l'aide du terminal et exécuter des commandes. Dans notre cas, vous êtes dans le répertoire racine. Donc `cd .\\trpclibrary` vous aidera. Vous pouvez également utiliser le terminal de VS Code.

Vous utiliserez la commande de démarrage `npx create-mf-app` pour initier votre serveur avec un modèle prédéfini qui vous fera gagner du temps.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/sever-side-x2.png align=\"left\")

*Configuration côté serveur*

Vous pourriez obtenir des erreurs indiquant que vous n'avez pas Express ou d'autres bibliothèques installées. Ne vous inquiétez pas – vous installerez toutes les bibliothèques requises sous peu.

Après avoir créé le serveur, créons le client en utilisant React et la même commande dans le même répertoire `trpclibrary`.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-11.png align=\"left\")

*Configuration côté client*

Voilà, votre côté client React est prêt. Mais vous pourriez être submergé par toutes les erreurs concernant les modules et les paquets. Téléchargeons-les d'abord.

J'utilise yarn, et je vous recommande de faire de même. Utilisez la commande `yarn` dans le répertoire racine `trpcDemo`.

Conseil : Vous pouvez utiliser la commande `cd ..` pour quitter le répertoire actuel et entrer dans le répertoire parent.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-13.png align=\"left\")

Votre côté serveur, votre côté client, ou les deux, pourraient ne pas avoir de fichier de configuration TS. Je recommande donc de l'installer à l'aide de la commande `npx tsc --init` dans les deux répertoires.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-14.png align=\"left\")

*Initialisation du fichier de configuration TS*

Maintenant, vous devez télécharger tRPC, CORS et Zod pour votre côté serveur du projet.

Au 2 juillet 2024, le paquet [*@trpc/server*](https://www.npmjs.com/package/@trpc/server) est à la version la plus récente 10.45.2. N'oubliez pas que même le [paquet tRPC côté client](https://www.npmjs.com/package/@trpc/client) doit être en version 10.45.2.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-16.png align=\"left\")

*Installation de Zod, CORS et @trpc/server côté serveur*

Ensuite, vous devez installer [@trpc/client](https://www.npmjs.com/package/@trpc/client), [@trpc/react-query](https://www.npmjs.com/package/@trpc/react-query), [@tanstack/react-query](https://www.npmjs.com/package/@tanstack/react-query), [@trpc/server](https://www.npmjs.com/package/@trpc/server) et [Zod](https://www.npmjs.com/package/zod) pour le côté client. Vous utiliserez la même commande "[yarn add &lt;package\_names&gt;](https://classic.yarnpkg.com/lang/en/docs/cli/add/)".

Cette fois, je ne partagerai pas la capture d'écran. Reportez-vous aux étapes précédentes et essayez de les télécharger.

Nous avons terminé la plupart des installations et de la configuration. Voici à quoi devrait ressembler votre structure de dossiers :

```markdown
tRPC Demo
├── trpclibrary
│   ├── client-side (Dossier App React)
│   └── server-side (Dossier Serveur Express)
└── package.json
```

### Configuration de tRPC

Voici ce que nous allons faire dans cette section :

1. Créer une instance tRPC avec Context
    
2. Créer des routes tRPC et configurer les requêtes
    
3. Configurer une URL de base
    
4. Configurer CORS
    

Commençons par créer une instance tRPC dans le fichier `index.ts` du répertoire côté serveur. Conformément à la documentation, vous ne devriez initier qu'une seule instance par application.

En utilisant l'instance tRPC, créez un routeur. Un routeur vous aide à enregistrer les routes où les requêtes API arrivent et sont traitées.

Les routes sont l'endroit où vous traiterez la requête et émettrez une réponse. Une route est un point de terminaison API connecté à une URL de base.

Par exemple, [`http://localhost:3005/api/hello`](http://localhost:3005/api/hello) illustre un point de terminaison API nommé `hello` et l'URL de base `api` pour appeler le point de terminaison API.

```typescript
import { initTRPC } from "@trpc/server";
import * as trpcExpress from "@trpc/server/adapters/express";

const createContext = ({}: trpcExpress.CreateExpressContextOptions) => ({});
type Context = Awaited<ReturnType<typeof createContext>>;

const trpc = initTRPC.context<Context>().create();
```

Vous devez placer ce code au-dessus du code boilerplate existant dans le fichier `index.ts` et en dessous des instructions d'importation. Il doit être au-dessus des déclarations des variables app et port et en dessous de l'instruction d'importation express.

Voilà ! J'ai créé une instance tRPC en utilisant le Builder `initTRPC` du paquet `@trpc/server`. Nous utiliserons cette instance pour tout ce qui concerne le back-end.

De plus, j'ai ajouté un [Context](https://trpc.io/docs/v10/server/context) au routeur tRPC. C'est une fonctionnalité de tRPC. Elle vous permet de mettre des détails tels que les connexions aux bases de données et les informations d'authentification.

tRPC partage le Context entre toutes les procédures tRPC. C'est un lieu d'information et de stockage pour éviter la duplication de code et garder le code organisé.

Jusqu'à présent, vous avez initialisé l'instance tRPC avec Context. Maintenant, vous allez coder le routeur — placez donc le code suivant en dessous du précédent :

```typescript
import zod from "zod";

const appRouter = trpc.router({
  hello: trpc.procedure
    .input(
      zod.object({
        name: zod.string(),
      })
    )
    .query(({ input }) => {
      return {
        name: input.name,
      };
    }),
});

export type AppRouter = typeof appRouter;
```

Enfin, vous avez importé Zod. Vous avez également créé un point de terminaison API nommé `hello` qui prend une entrée à l'aide de la méthode `input()` et fait correspondre la requête API de l'utilisateur avec l'objet Zod spécifié dans ce point de terminaison.

Avec ce code, Zod et tRPC s'attendent à ce que le front-end fournisse un objet avec une seule propriété de type chaîne nommée `name`. tRPC utilisera cette propriété et répondra en utilisant l'entrée.

Vous avez pris l'entrée, l'avez déstructurée et l'avez traitée à l'intérieur de la méthode `query()`. Toutes ces méthodes sont des procédures tRPC. tRPC partage le Context entre ces procédures.

Comme je l'ai mentionné plus tôt, vous aurez besoin de l'instance tRPC partout. Je l'ai utilisée pour créer un routeur afin de stocker les routes (points de terminaison API), les enregistrer et les traiter.

Vous pouvez créer un nombre illimité de routes à l'intérieur de la procédure `router()`. C'est comme un gestionnaire de routes. Ce point de terminaison est un objet dont chaque route agit comme une propriété.

Vous aurez besoin du builder de procédure pour accéder aux procédures comme `query()`, `input()`, et ainsi de suite. Nous l'avons donc lié à l'instance tRPC et accédé à ces méthodes.

Maintenant, il est temps de définir l'URL de base. Vous utiliserez l'adaptateur Express de la bibliothèque `@trpc/server` pour définir l'URL de base.

Placez le code suivant au-dessus des routes `app.get()` dans le fichier `index.ts` :

```typescript
app.use(
  "/api",
  trpcExpress.createExpressMiddleware({
    router: appRouter,
    createContext,
  })
);
```

`/api` représente votre URL de base. Chaque route sera au-dessus de l'URL `/api`. Maintenant, votre point de terminaison API `hello` est devenu [`http://localhost:3005/api/hello`](http://localhost:3005/api/hello).

Essayons de tester cela en utilisant votre navigateur. Vous souvenez-vous que je vous ai demandé de créer un fichier `package.json` avec un code pré-écrit dans le répertoire racine tRPC Demo ?

C'était pour exécuter à la fois le serveur et le côté client en tant que bibliothèque. Placez votre terminal dans le répertoire racine. Ensuite, exécutez `yarn start` pour lancer le serveur et le côté client ensemble et rendez-vous sur l'URL [`http://localhost:3005/api/hello`](http://localhost:3005/api/hello).

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-23.png align=\"left\")

*Erreur de type invalide tRPC*

Oh-oh ! Avez-vous reçu une erreur ? Si l'erreur indique "Invalid Type", vous êtes sur la bonne voie. Voyez-vous, c'est là que tRPC nous aide.

Dans le code ci-dessus, lorsque j'ai envoyé une requête API en tant qu'utilisateur au point de terminaison API `hello`, je n'ai passé aucun objet ou valeur que tRPC attendait pour ce point de terminaison.

tRPC attendait un objet avec une propriété de type chaîne nommée `name` avec une valeur. Lorsque je ne l'ai pas fournie, tRPC a restreint mon accès. C'est là qu'il brille.

"C'est très bien, mais on fait quoi maintenant ?" Vous devez connecter le front-end avec le côté serveur pour envoyer l'objet avec les données attendues.

Il reste une chose pour le côté serveur. CORS ! C'est simple à mettre en place. Trouvez le code d'initialisation d'Express dans le fichier `index.ts`. Il a été fourni avec le modèle Express. Ensuite, insérez la ligne suivante :

```javascript
import cors from "cors";

app.use(cors());
```

Voici un indice : Recherchez la déclaration des variables port et app dans votre fichier `index.ts`.

Une fois que vous avez inséré la ligne, cela pourrait vous donner une erreur parce que vous n'avez pas encore installé les types de CORS. Allez dans votre terminal et installez `@types/cors` à l'intérieur du répertoire côté serveur.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-24.png align=\"left\")

*Téléchargement de @types/cors.*

CORS est prêt et sécurisé. Votre côté serveur est prêt ! Maintenant, essayons de connecter le côté serveur avec le côté client en utilisant les bibliothèques respectives.

Avant de passer au côté client, je veux m'assurer que nous sommes sur la même longueur d'onde. Jusqu'à présent, vous avez codé une instance de tRPC, formé un routeur, défini une URL de base et testé les points de terminaison API avec un contexte optionnel.

Vous avez codé tout cela dans le fichier `index.ts` du côté serveur. Passons au côté client et terminons la dernière partie de ce tutoriel.

### Côté client

Nous avons déjà téléchargé les paquets requis. Nous allons commencer par créer un fichier `trpc.ts` dans le répertoire `/src` du répertoire côté client. Il gérera les requêtes et les demandes émises par le front-end.

Vous avez créé une instance tRPC pour construire le routeur et d'autres composants côté serveur, n'est-ce pas ? Eh bien, vous devez maintenant faire la même chose côté client. Vous devez créer une instance tRPC côté client en utilisant `@trpc/react-query`.

Aussi, puisque vous voulez lier votre instance tRPC côté client avec celle du côté serveur, vous devez importer l'instance tRPC côté serveur et son type.

Pour importer l'instance tRPC côté serveur, insérez une propriété `main` à l'intérieur du fichier `package.json` du côté serveur. Cela définit `index.ts` comme fichier d'entrée lorsque vous importez le dossier côté serveur sur votre côté client.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-25.png align=\"left\")

*Fichier* `package.json` *côté serveur.*

Après avoir défini cette propriété, vous pouvez importer l'instance tRPC dans le côté client à l'aide du terminal. Pour moi, le back-end s'appelle `server-side` dans mon fichier `package.json` à l'intérieur du répertoire côté serveur avec la version `1.0.0`.

J'exécuterai donc `yarn add server-side@1.0.0` dans le terminal côté client. L'installation peut sembler familière car c'est ainsi que les développeurs construisent des bibliothèques.

Cette commande devrait ajouter votre dossier côté serveur en tant que paquet dans le répertoire node modules côté client. Vous pouvez le vérifier avec le fichier `package.json` côté client.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-26.png align=\"left\")

*Fichier* `package.json` *côté client.*

Il devrait contenir le nom de votre paquet côté serveur en tant que dépendance.

En d'autres termes, vous avez installé le paquet côté serveur dans votre application côté client. Vous pouvez maintenant importer le tRPC côté serveur et l'utiliser comme une bibliothèque.

Si vous vous souvenez bien, nous avons ajouté une ligne d'exportation supplémentaire AppRouter lors de la création du routeur sur le serveur. Nous avons fait cela parce que nous devions importer le type AppRouter côté client pour utiliser l'instance tRPC côté serveur sur le client.

Voici à quoi devrait ressembler le fichier `trpc.ts` maintenant :

```typescript
import { createTRPCReact } from "@trpc/react-query";
import type { AppRouter } from "server-side";

export const trpc = createTRPCReact<AppRouter>();
```

Avec ce code, vous avez créé une instance tRPC côté client en utilisant les caractéristiques de l'instance tRPC côté serveur.

Parfait. Maintenant, créons un autre fichier nommé `AppComponent.tsx` dans le répertoire `/src`.

Ce fichier contiendra votre composant App principal. Il importera l'instance client `trpc` du fichier `trpc.ts` et l'utilisera pour appeler votre point de terminaison API `hello`.

```typescript
import React from "react";
import { trpc } from "./trpc";
```

Puisque vous avez créé une instance tRPC côté client, vous pouvez accéder à tous les points de terminaison API côté client et appeler la méthode `useQuery()` pour envoyer des requêtes à ces points de terminaison API.

```typescript
import React from "react";
import { trpc } from "./trpc";

const AppComponent = () => {
  const userQuery = trpc.hello.useQuery({ name: "Afan" });

  return (
    <div className="mt-10 text-3xl mx-auto max-w-6xl">
      <div>{JSON.stringify(userQuery.data?.name)}</div>
    </div>
  );
};

export default AppComponent;
```

Si vous vous souvenez, le point de terminaison API `hello` nécessite un objet avec la propriété `name` de type chaîne avec une valeur. Vous passerez donc l'objet à l'aide de la méthode `useQuery()` avec la valeur pour éviter les discordances tRPC.

À l'intérieur du code JSX, vous déstructurerez la réponse API envoyée par le point de terminaison API à l'aide de la méthode `JSON.stringify()` et accéderez au résultat par le point de terminaison API.

Votre fichier `AppComponent.tsx` est un composant React standard. Vous devez donc importer ce composant dans le fichier `App.tsx` principal. `App.tsx` côté client est l'équivalent d'`index.ts` côté serveur.

Pour le fichier `App.tsx`, vous suivrez une configuration similaire. Importez l'instance tRPC client du fichier `trpc.ts`. Ensuite, définissez l'URL de base et configurez React Query.

Vous importerez React Query de TanStack, trpc du fichier `./trpc.ts`, `httpBatchLink` de `@trpc/client`, `useState` de React, et votre `AppComponent` du fichier `AppComponent.tsx`.

```typescript
// Instructions d'importation par défaut

import React from "react";
import ReactDOM from "react-dom/client";
import "./index.scss";

// Ajoutez les instructions d'importation suivantes

import { useState } from "react";

import { trpc } from "./trpc";
import { httpBatchLink } from "@trpc/client";
import AppComponent from "./AppComponent";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
```

Vous utiliserez chaque instruction d'importation. Ignorez toute erreur concernant des objets importés non utilisés. Ensuite, créez une instance de client React Query comme vous l'avez fait pour tRPC.

```typescript
const client = new QueryClient();
```

Une fois que vous avez fait cela, vous devez configurer l'URL de base. Vous le ferez à l'intérieur de la fonction App principale.

De plus, déplacez les instructions de code suivantes du dessous de la fonction App vers le haut de la fonction App sous l'instruction de déclaration du client React Query.

```typescript
const rootElement = document.getElementById("app");
if (!rootElement) throw new Error("Failed to find the root element");

const root = ReactDOM.createRoot(rootElement as HTMLElement);
```

Ensuite, supprimez le code HTML JSX par défaut de la fonction App. Vous pouvez supprimer en toute sécurité tout le code HTML dans la fonction App.

Ensuite, vous devez configurer l'URL de base pour le côté client. Chaque fois que le front-end invoque les points de terminaison de l'API, il utilisera cette URL de base. Elle doit correspondre à l'URL de base que vous avez définie côté serveur.

Remplacez le code de votre fonction App de l'HTML par le code d'URL de base suivant :

```typescript
const App = () => {
  const [trpcClient] = useState(() =>
    trpc.createClient({
      links: [
        httpBatchLink({
          // URL de base
          url: "http://localhost:3005/api",
        }),
      ],
    })
  );

  return <></>;
};
```

Votre fichier `App.tsx` devrait ressembler à ceci :

```typescript
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.scss";

import { useState } from "react";

import { trpc } from "./trpc";
import { httpBatchLink } from "@trpc/client";
import AppComponent from "./AppComponent";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const client = new QueryClient();

const rootElement = document.getElementById("app");
if (!rootElement) throw new Error("Failed to find the root element");

const root = ReactDOM.createRoot(rootElement as HTMLElement);

const App = () => {
  const [trpcClient] = useState(() =>
    trpc.createClient({
      links: [
        httpBatchLink({
          // URL de base
          url: "http://localhost:3005/api",
        }),
      ],
    })
  );

  return <></>;
};

root.render(<App />);
```

Je n'ai pas encore beaucoup parlé de l'instruction `return`. Faisons-le maintenant. Nous ne garderons pas l'instruction `return` vide.

Elle affichera les données renvoyées par le point de terminaison API, qui devraient être la chaîne de caractères que vous avez soumise à l'aide de la méthode `useQuery()` dans le fichier de composant `AppComponent.tsx`.

L'instruction `return` concerne les wrappers et le composant AppComponent. Si vous avez besoin que vos composants et pages utilisent tRPC, React Query, etc., vous devez envelopper vos composants comme `AppComponent` avec les `Providers` (fournisseurs) de ces bibliothèques.

```typescript
  return (
    // Fournisseur tRPC
    <trpc.Provider client={trpcClient} queryClient={client}>
      {/* Fournisseur React Query */}
      <QueryClientProvider client={client}>
        {/* Composant React HTML */}
        <AppComponent />
      </QueryClientProvider>
    </trpc.Provider>
  );
```

Maintenant, vous allez envelopper le composant `AppComponent` avec React Query et passer l'instance du client React Query que vous avez créée à l'aide de `QueryClient()` dans ce fichier. Ensuite, vous envelopperez le React Query Provider avec le tRPC Provider.

Le fournisseur tRPC nécessite le client React Query et le client tRPC avec l'URL de base. Nous fournirons donc également ces informations.

Une fois que vous avez passé les informations requises et fait correspondre votre code au mien, vous pouvez visiter [http://localhost:3000](http://localhost:3000) et regarder la sortie. Elle affichera les données que vous avez passées en utilisant le point de terminaison API `hello`.

Note : Vous devez exécuter la commande `yarn start` dans votre répertoire racine `tRPC Demo` pour activer les ports localhost afin de voir la sortie.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-27.png align=\"left\")

*Image de sortie*

Voilà ! Tout est prêt. tRPC invoque le point de terminaison API `hello` depuis le front-end. Il donne la priorité à la sécurité des types et utilise TypeScript pour éviter des millions d'autres problèmes JavaScript.

Vous pouvez ajouter d'autres routes et points de terminaison API comme `hello` dans votre gestionnaire de routes. C'est aussi simple que d'ajouter une nouvelle propriété à un objet. C'est ainsi que tRPC vous facilite la vie.

## Conclusion

tRPC est une bibliothèque de style RPC sécurisée au niveau des types. Elle intègre RPC à TypeScript pour éliminer REST, `fetch()` et d'autres techniques de création et d'appel d'API.

Elle agit comme une alternative à REST et Fetch. Je l'utiliserai dans un avenir proche.

J'ai aimé découvrir cette nouvelle technologie. Il peut y avoir quelques défauts dans cet article, mais je suis un apprenant, alors signalez mes erreurs dès que vous le pouvez et aidez-moi à m'améliorer.

Abonnez-vous à [ma newsletter](https://www.freecodecamp.org/news/p/96029b5d-38ad-4b3c-a021-661b70eb6dd3/Subscribe%20to%20my%20newsletter%20for%20the%20weekly%20emails%20about%20Software%20Engineering,%20Tech%20Jobs%20&%20Careers,%20and%20resources%20to%20excel%20in%20your%20career.) pour recevoir des e-mails hebdomadaires sur le génie logiciel, les emplois et les carrières dans la technologie, ainsi que des ressources, y compris des articles payants gratuitement, pour vous aider à exceller dans votre carrière.

*Au plaisir de vous retrouver dans le prochain article ✌️*