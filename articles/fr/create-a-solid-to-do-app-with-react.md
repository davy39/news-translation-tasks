---
title: Comment créer une application To-Do solide avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-02T16:37:00.000Z'
originalURL: https://freecodecamp.org/news/create-a-solid-to-do-app-with-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/603a6472a675540a229246bc.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: React
  slug: react
- name: Web Applications
  slug: web-applications
seo_title: Comment créer une application To-Do solide avec React
seo_desc: "By Virginia Balseiro\nIn this tutorial you will learn how to create a basic\
  \ Solid to-do app. But what is Solid – not to be confused with SOLID? Well, it's\
  \ a set of conventions and tools used to build decentralized apps.  \nSo what do\
  \ I mean by decentra..."
---

Par Virginia Balseiro

Dans ce tutoriel, vous apprendrez à créer une application de base [Solid](https://solidproject.org/about) de type to-do. Mais qu'est-ce que Solid – à ne pas confondre avec [SOLID](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/) ? Eh bien, il s'agit d'un ensemble de conventions et d'outils utilisés pour construire des applications décentralisées. 
  
Alors, que veux-je dire par décentralisé ? Actuellement, toutes nos données sont centralisées sur quelques plateformes web : Facebook, Google, et autres. Cela a diverses conséquences pour la vie privée dont nous sommes tous conscients, mais cela met également en danger le principe d'universalité du web : le web doit être accessible à tous.   
  
Permettez-moi d'illustrer cela avec un exemple : si mon professeur d'allemand décide de créer un groupe Facebook pour partager des matériaux de classe, je dois avoir un compte Facebook pour y accéder. De même, si le professeur décide de quitter Facebook, elle doit déplacer les étudiants vers une autre application avec les données.   
  
Avec Solid, les données et l'application sont découplées. Les données résident à un endroit et l'application lit et écrit à cet endroit. L'utilisateur contrôle où se trouvent ces données, et avec quelles personnes ou applications il souhaite les partager. Les utilisateurs peuvent décider quelles applications utiliser en fonction de celles qui répondent le mieux à leurs besoins, et ils ont un contrôle total sur leurs données. 

Cela présente également de nombreux avantages pour les développeurs, car la concurrence est alors basée sur la qualité d'une application, plutôt que sur la quantité de données utilisateur que vous contrôlez.

Et pour les développeurs frontend, il y a l'avantage supplémentaire de ne pas avoir à se soucier de la configuration d'une base de données si vous souhaitez enregistrer des données utilisateur.

Ce tutoriel vous aidera à vous familiariser avec certains des outils disponibles pour écrire des applications Solid. Nous utiliserons les bibliothèques suivantes :

* [solid-client](https://docs.inrupt.com/developer-tools/javascript/client-libraries/tutorial/read-write-data/) : Bibliothèque pour lire et écrire des données dans les Pods Solid
* [solid-ui-react](https://docs.inrupt.com/developer-tools/javascript/react-sdk/) : Bibliothèque de composants UI qui facilitent l'interaction avec les données.

## Prérequis

Ce tutoriel suppose une connaissance de base de React.

Vous devrez également [avoir votre propre Pod](https://solidproject.org/users/get-a-pod). Vous pouvez le créer au préalable, ou dans le cadre du processus de connexion lorsque nous ajouterons l'authentification à l'application de to-do, en vous inscrivant au lieu de vous connecter.

Voici un lien vers le dépôt où vous pouvez trouver le code : [https://github.com/VirginiaBalseiro/solid-todo-tutorial](https://github.com/VirginiaBalseiro/solid-todo-tutorial)

Et voici un lien vers CodeSandbox : [https://codesandbox.io/s/solid-todo-tutorial-7uz4j](https://codesandbox.io/s/solid-todo-tutorial-7uz4j). Si vous souhaitez tester l'application sur CodeSandbox, assurez-vous simplement de l'ouvrir dans un onglet séparé.

# Mise en route

Nous allons commencer par créer une application React en utilisant [create-react-app.](https://create-react-app.dev/) Cela créera un nouveau répertoire avec le nom de votre application dans le répertoire à partir duquel vous l'exécutez. Naviguez donc vers le répertoire où vous conservez vos projets et exécutez :

```jsx
npx create-react-app solid-todo-tutorial

```

Cela crée un nouveau répertoire nommé `solid-todo-tutorial`. Allez dans ce répertoire et installez les deux bibliothèques Solid que j'ai mentionnées précédemment :

```jsx
cd solid-todo-tutorial
npm install @inrupt/solid-client @inrupt/solid-ui-react

```

Maintenant, nous sommes prêts à commencer à coder.

# Comment authentifier un utilisateur

J'ai laissé les noms de classe dans ces extraits au cas où vous souhaiteriez utiliser les feuilles de style disponibles dans le dépôt.

### Comment utiliser le composant LoginButton pour connecter les utilisateurs

La première chose que nous devons faire pour pouvoir écrire dans notre Pod est de nous authentifier en tant qu'utilisateur avec des permissions d'écriture (afin d'avoir les permissions nécessaires). Heureusement, cela est très simple en utilisant le [bouton de connexion](https://solid-ui-react.docs.inrupt.com/?path=/story/authentication-login-button--with-children) de `solid-ui-react`.

Nous devons importer `LoginButton` de `solid-ui-react`. Ce composant accepte deux props obligatoires : `oidcIssuer`, le fournisseur de Pod, et une `redirectUrl` qui est l'URL vers laquelle nous voulons être redirigés après nous être connectés.

Nous obtiendrons le fournisseur de Pod sous forme de chaîne de caractères de l'utilisateur via une zone de texte, et nous fournirons également quelques options de fournisseurs de Pod.

Le `LoginButton` accepte également une prop optionnelle `authOptions`, qui est un objet avec la propriété `clientName`. Cela est utile car nous voulons afficher le nom de notre application à l'utilisateur lorsqu'ils s'authentifient. 

Si nous ne passons pas le `clientName`, une chaîne aléatoire sera générée, ce qui est déroutant pour l'utilisateur lorsqu'ils accordent à notre application la permission de faire des choses.

Dans `App.js`, supprimons tout le code standard qui accompagne notre application React et utilisons le `LoginButton` :

```jsx
// App.js

import React from "react";
import { LoginButton } from "@inrupt/solid-ui-react";

const authOptions = {
    clientName: "Solid Todo App",
  };

function App() {
const [oidcIssuer, setOidcIssuer] = useState("");

  const handleChange = (event) => {
    setOidcIssuer(event.target.value);
  };

  return (
    <div className="app-container">
	 <span>
            Connectez-vous avec :
            <input
              className="oidc-issuer-input "
              type="text"
              name="oidcIssuer"
              list="providers"
              value={oidcIssuer}
              onChange={handleChange}
            />
          <datalist id="providers">
            <option value="https://broker.pod.inrupt.com/" />
            <option value="https://inrupt.net/" />
          </datalist>
          </span>
		  <LoginButton
		     oidcIssuer={oidcIssuer}
		     redirectUrl={window.location.href}
		     authOptions={authOptions}
		   />
    </div>
  );
}

export default App;

```

Dans le fichier `index.js`, enveloppons notre composant App avec le composant `SessionProvider`. Maintenant, nous pouvons utiliser le hook `useSession` dans toute l'application, qui retourne des informations de session qui nous permettent de faire des requêtes authentifiées.

Remplacez le code standard dans `index.js` par ce qui suit :

```jsx
// index.js

import ReactDOM from "react-dom";
import App from "./App";
import { SessionProvider } from "@inrupt/solid-ui-react";

ReactDOM.render(
  <SessionProvider>
    <App />
  </SessionProvider>,
  document.getElementById("root")
);

```

Une fois cela fait, vous pouvez le tester ! Lancez votre application avec `npm start` et cliquez sur le bouton de connexion. Cela devrait vous emmener à une page où vous pouvez soit vous connecter, soit vous inscrire. Si vous n'avez pas de compte, vous pouvez cliquer sur "S'inscrire" pour en créer un. 

Une fois connecté, vous serez redirigé vers la page principale. Comme vous pouvez le voir, notre page principale ne contient que le bouton de connexion. Nous sommes connectés, mais nous ne faisons rien avec cette information. Changeons cela !

### Comment utiliser les données de profil

Nous allons modifier notre code pour que notre application affiche le bouton de connexion si nous sommes déconnectés, et notre nom si nous sommes connectés.

Pour cela, nous allons utiliser `CombinedDatasetProvider` et `Text` de `solid-ui-react`. `CombinedDatasetProvider` a besoin de deux props : `datasetUrl` et `thingUrl` qui, dans ce cas, peuvent tous deux être définis sur le WebID de l'utilisateur.

Un **WebID** est un URI HTTP qui fait référence à un agent (par exemple, une personne), qui, lorsqu'il est recherché, se résout en un document de profil.

`CombinedDatasetProvider` récupère le dataset et la chose pour nous afin que nous puissions les passer directement aux enfants.

L'enfant dans notre application sera le composant `Text`.

Le composant `Text` prend une prop, soit `property` soit `properties`, qui spécifie la valeur à récupérer et à afficher à partir du dataset/chose récupéré. 

Dans notre cas, nous voulons que le composant Text récupère et affiche le nom de l'utilisateur à partir du profil de l'utilisateur. `property` ou `properties` est l'URL ou les URL que nous avons choisies pour le **prédicat** pour lequel nous voulons récupérer les données.

Dans notre cas, nous voulons obtenir le nom de l'utilisateur.

Les données de profil d'un utilisateur sont stockées sous forme de données [Resource Description Framework (RDF)](https://www.w3.org/RDF/). RDF est un modèle standard pour l'échange de données sur le Web. Les données RDF sont stockées en **triplets**, qui sont composés d'un **sujet**, d'un **prédicat** et d'un **objet**. 

Ainsi, par exemple, si je veux écrire une application de réseau social et que je veux stocker les connaissances de Bob, je pourrais en ajouter une comme suit : `<http://example.org/bob#me> <http://xmlns.com/foaf/0.1/knows> <http://example.org/alice#me> .`

Dans ce cas, `<http://example.org/bob#me>` est le sujet, `<http://xmlns.com/foaf/0.1/knows>` est le prédicat, et `<http://example.org/alice#me>` est l'objet.

Pour spécifier que nous voulons récupérer le nom, nous utilisons un identifiant de nom. Dans notre exemple, nous utilisons un identifiant de nom provenant d'un vocabulaire existant.

Les vocabulaires sont des collections d'identifiants (URI) avec une signification clairement définie. Un exemple de vocabulaire populaire est **[FOAF (Friend Of A Friend)](http://xmlns.com/foaf/spec/)**, qui définit des URI pour décrire les personnes et leurs relations. 

Vous pouvez trouver plus d'informations sur les vocabulaires sur [le site web du projet Solid](https://solidproject.org/developers/vocabularies).

Le nom de l'utilisateur connecté, dans la plupart des cas, sera stocké dans le document de profil sous "[http://www.w3.org/2006/vcard/ns#fn](http://www.w3.org/2006/vcard/ns#fn)" ou "[http://xmlns.com/foaf/0.1/name](http://xmlns.com/foaf/0.1/name)". `fn` signifie nom formaté. En RDF, cela ressemble à ceci :

```jsx
:me <http://www.w3.org/2006/vcard/ns#fn> "Virginia Balseiro" .

```

ou

```jsx
:me <[<http://xmlns.com/foaf/0.1/name>](<http://xmlns.com/foaf/0.1/name>)> "Virginia Balseiro" 

```

Mais dans notre cas, nous voulons qu'il vérifie sous [`http://www.w3.org/2006/vcard/ns#fn`](http://www.w3.org/2006/vcard/ns#fn) et s'il ne trouve rien, qu'il vérifie sous [`http://xmlns.com/foaf/0.1/name`](http://xmlns.com/foaf/0.1/name). Nous pouvons utiliser `properties`, qui est un tableau de propriétés à tenter de lire, dans notre composant `Text`.

```jsx
// App.js

import React from "react";
import {
  LoginButton,
  Text,
  useSession,
  CombinedDataProvider,
} from "@inrupt/solid-ui-react";

const authOptions = {
    clientName: "Solid Todo App",
  };

function App() {
  const { session } = useSession();
  const [oidcIssuer, setOidcIssuer] = useState("");

  const handleChange = (event) => {
    setOidcIssuer(event.target.value);
  };
  return (
    <div className="app-container">
      {session.info.isLoggedIn ? (
        <CombinedDataProvider
          datasetUrl={session.info.webId}
          thingUrl={session.info.webId}
        >
          <div className="message logged-in">
            <span>Vous êtes connecté en tant que : </span>
            <Text properties={[
                "http://www.w3.org/2006/vcard/ns#fn",
                "http://xmlns.com/foaf/0.1/name",
              ]} />
          </div>
        </CombinedDataProvider>
      ) : (
        <div className="message">
          <span>Vous n'êtes pas connecté. </span>
          <span>
            Connectez-vous avec :
            <input
              className="oidc-issuer-input "
              type="text"
              name="oidcIssuer"
              list="providers"
              value={oidcIssuer}
              onChange={handleChange}
            />
           <datalist id="providers">
             <option value="https://broker.pod.inrupt.com/" />
             <option value="https://inrupt.net/" />
           </datalist>
          </span>
          <LoginButton
            oidcIssuer={oidcIssuer}
            redirectUrl={window.location.href}
            authOptions={authOptions}
          />
        </div>
      )}
    </div>
  );
}

export default App;

```

Nous pouvons maintenant nous connecter et afficher des informations de notre Pod dans notre application.

### Comment déconnecter les utilisateurs

Ajoutons maintenant un [bouton de déconnexion](https://solid-ui-react.vercel.app/?path=/story/authentication-logout-button--with-children) afin de pouvoir nous déconnecter à tout moment. C'est simple : nous devons simplement importer le `LogoutButton` de `solid-ui-react` et l'afficher sous le Text avec le nom de l'utilisateur :

```jsx
// App.js

import {
  LoginButton,
  LogoutButton,
  Text,
  useSession,
  CombinedDataProvider,
} from "@inrupt/solid-ui-react";

function App() {
  const { session } = useSession();

	// ...
	
	<div className="message logged-in">
	  <span>Vous êtes connecté en tant que : </span>
	  <Text properties={[
	     "http://xmlns.com/foaf/0.1/name",
	     "http://www.w3.org/2006/vcard/ns#fn",
	   ]} />    
	   <LogoutButton />
	 </div>

	// ...

}

```

# Comment créer une To-Do

### Comment ajouter un bouton "Ajouter une tâche"

Pour créer un élément de to-do, nous allons avoir besoin d'un bouton qui déclenche une fonction qui ajoute un élément de to-do à notre liste de to-do. Mettons toute la logique et l'interface utilisateur pour ajouter une to-do dans un composant séparé dans `src/components/AddTodo/index.js` :

```jsx
// components/AddTodo/index.js

import React from "react";

function AddTodo() {
  return <button className="add-button">Ajouter une tâche</button>;
}

export default AddTodo;

```

Dans notre App, nous allons afficher ce bouton `AddTodo` uniquement aux utilisateurs connectés :

```jsx
// App.js

import AddTodo from "../src/components/AddTodo";

function App() {
// ...
      {session.info.isLoggedIn ? (
        <CombinedDataProvider
          datasetUrl={session.info.webId}
          thingUrl={session.info.webId}
        >
          <div className="message logged-in">
            <span>Vous êtes connecté en tant que : </span>
            <Text
              properties={[
                "http://xmlns.com/foaf/0.1/name",
                "http://www.w3.org/2006/vcard/ns#fn",
              ]} />
            <LogoutButton />
          </div>
          <section>
            <AddTodo />
          </section>
        </CombinedDataProvider>
      ) : 
// ...
}

```

Pour l'instant, ce bouton ne fait rien. Changeons cela.

### Comment initialiser le dataset des To-Dos

En termes formels, chacun de nos éléments de to-do sera structuré en tant que **choses** qui sont regroupées dans un **dataset**. Nous devons donc d'abord vérifier si le dataset existe déjà, et si ce n'est pas le cas, nous devons le créer. 

Écrivons une fonction qui fait cela, en supposant que nos données structurées seront stockées dans un dossier appelé "todos" à la racine de notre pod.

La bonne façon de faire cela serait de vérifier le profil (c'est-à-dire les données au WebID de l'utilisateur), de rechercher une URL pour un prédicat connu (par exemple `myVocab:todolistContainer`), puis de suivre ce lien pour accéder à ce dossier. 

Seulement si un tel lien n'existe pas, l'application initialiserait son propre dossier - et après l'initialisation, elle créerait un lien vers celui-ci à partir du WebID de l'utilisateur. 

Pour cela, nous devrions créer un nouveau vocabulaire, et pour des raisons de simplicité, cela n'est pas inclus dans ce tutoriel.

Mettons cette fonction dans `src/utils/index.js` car nous pourrions l'utiliser à nouveau à l'avenir ailleurs que dans notre composant `AddTodo`.

```jsx
// utils/index.js

import {
  createSolidDataset,
  getSolidDataset,
  saveSolidDatasetAt,
} from "@inrupt/solid-client";

export async function getOrCreateTodoList(containerUri, fetch) {
  const indexUrl = `${containerUri}index.ttl`;
  try {
    const todoList = await getSolidDataset(indexUrl, { fetch });
    return todoList;
  } catch (error) {
    if (error.statusCode === 404) {
      const todoList = await saveSolidDatasetAt(
        indexUrl,
        createSolidDataset(),
        {
          fetch,
        }
      );
      return todoList;
    }
  }
}

```

Nous utilisons ici trois fonctions de `solid-client` pour lire et écrire des données dans nos Pods :

* `getSolidDataset` : prend l'URI du dataset que nous voulons obtenir, plus un objet `options` où nous passons la fonction `fetch`. Il s'agit d'une fonction que nous obtenons de la session, et elle est utilisée pour faire des requêtes authentifiées.
* `createSolidDataset` : initialise un nouveau dataset en mémoire.
* `saveSolidDatasetAt` : prend un URI comme premier paramètre (où notre dataset sera sauvegardé), le dataset en question comme deuxième paramètre (dans ce cas, un nouveau dataset vide), et la fonction fetch.

Si le fichier d'index de la liste de to-do est trouvé, notre fonction getOrCreateTodoList le retournera. Sinon (s'il y a une erreur 404), elle créera le fichier à l'emplacement donné.

Maintenant, nous pouvons utiliser cette fonction dans notre composant `AddTodo`. Nous devons lui passer un URI de conteneur, que nous créons en concaténant l'URI du Pod avec le nom du dossier que nous avons choisi pour stocker notre liste de to-do. Donc, nous devons d'abord :

* Récupérer le dataset de profil en utilisant le WebID pour la session actuelle (le WebID de l'utilisateur actuel).
* Extraire la `Thing` de profil du dataset de profil avec la même URL (le WebID de l'utilisateur).
* Obtenir les URL des Pods de l'utilisateur. Pour cela, nous utilisons `getUrlAll`, qui retourne un tableau avec toutes les URL stockées sous le prédicat `http://www.w3.org/ns/pim/space#storage`. Nous supposerons que le premier élément du tableau est le Pod que nous voulons utiliser.

Une fois que nous avons l'URL du conteneur, nous pouvons maintenant vérifier si le dataset de la liste de to-do existe. S'il n'existe pas, nous pouvons le créer et l'utiliser n'importe où dans le composant :

```jsx
// components/AddTodo/index.js

import { getSolidDataset, getThing, getUrlAll } from "@inrupt/solid-client";
import { useSession } from "@inrupt/solid-ui-react";
import React, { useEffect, useState } from "react";
import { getOrCreateTodoList } from "../../utils";

function AddTodo() {
  const { session } = useSession();
  const [todoList, setTodoList] = useState();

  useEffect(() => {
    if (!session) return;
    (async () => {
      const profileDataset = await getSolidDataset(session.info.webId, {
        fetch: session.fetch,
      });
      const profileThing = getThing(profileDataset, session.info.webId);
      const podsUrls = getUrlAll(
        profileThing,
        "http://www.w3.org/ns/pim/space#storage"
      );
      const pod = podsUrls[0];
      const containerUri = `${pod}todos/`;
      const list = await getOrCreateTodoList(containerUri, session.fetch);
      setTodoList(list);
    })();
  }, [session]);

  return <button className="add-button">Ajouter une tâche</button>;
}

export default AddTodo;

```

Pour vérifier si cela a fonctionné, allez sur [PodBrowser](https://podbrowser.inrupt.com/login), connectez-vous en sélectionnant votre fournisseur de Pod dans la liste déroulante, entrez votre nom d'utilisateur et votre mot de passe, et vérifiez que le dossier "todos" a été créé dans votre Pod.

![Vue des fichiers dans PodBrowser montrant le dossier "todos" nouvellement créé](https://www.freecodecamp.org/news/content/images/2021/02/image-171.png)

Si vous allez dans le conteneur "todos", il devrait y avoir un fichier `index.ttl` dedans.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-173.png)
_Vue des fichiers dans PodBrowser montrant le fichier "index.tll" nouvellement créé_

Si vous cliquez sur `index.ttl`, un tiroir s'ouvrira à droite avec un lien "Télécharger". Cliquez dessus pour télécharger le fichier, que vous pouvez ouvrir avec n'importe quel éditeur de texte, comme le Bloc-notes. Le contenu du fichier devrait ressembler à ceci :

```jsx
@prefix as:    <https://www.w3.org/ns/activitystreams#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ldp:   <http://www.w3.org/ns/ldp#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix acl:   <http://www.w3.org/ns/auth/acl#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix dc:    <http://purl.org/dc/terms/> .
@prefix acp:   <http://www.w3.org/ns/solid/acp#> .

<https://pod.inrupt.com/virginiabalseiro/todos/index.ttl>
        rdf:type  ldp:RDFSource .

```

C'est le fichier où nous allons ajouter nos tâches.

Si à un moment donné vous faites une erreur dans votre liste de tâches en testant l'application au fur et à mesure que vous codez, vous pouvez supprimer ce fichier et ensuite le dossier qui le contient ("todos") sur PodBrowser en cliquant sur le bouton "Supprimer" dans le tiroir des détails. 

Ensuite, la prochaine fois que vous actualiserez votre application, le dossier et le fichier seront recréés afin que vous puissiez recommencer.

# Comment ajouter un élément au dataset

D'accord, maintenant nous pouvons enfin ajouter une tâche ! Ajouter une tâche consiste essentiellement à ajouter un élément, ou `[Thing](https://docs.inrupt.com/developer-tools/javascript/client-libraries/reference/glossary/)`, au dataset de la liste de tâches que nous venons de créer. Nos tâches auront trois propriétés :

* `text` - le contenu de la tâche. Il sera stocké sous le prédicat : [http://schema.org/text](http://schema.org/text)
* `created` - la date à laquelle cette tâche a été créée, stockée sous [http://www.w3.org/2002/12/cal/ical#created](http://www.w3.org/2002/12/cal/ical#created)
* `type` - le type de la tâche, qui, entre autres, nous aidera à filtrer plus tard. Cela est stocké sous [http://www.w3.org/2002/12/cal/ical#Vtodo](http://www.w3.org/2002/12/cal/ical#Vtodo)

Nous codons en dur les chaînes de prédicats ici, mais il existe des bibliothèques qui facilitent cela, comme [rdf-namespaces](https://www.npmjs.com/package/rdf-namespaces).

La date nous aidera à les trier plus tard. Nous devons donc créer une chose et ajouter ces éléments. Nous utiliserons :

* `addStringNoLocale` pour ajouter la chaîne de texte
* `addDatetime` pour ajouter la date de création

Écrivons une fonction qui fait cela afin que nous puissions la déclencher en cliquant sur le bouton.

```jsx
// components/AddTodo/index.js
import {
  addDatetime,
  addStringNoLocale,
  createThing,
  getSolidDataset,
  getSourceUrl,
  getThing,
  getUrlAll,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";

function AddTodo() { 
const { session } = useSession();
// ...
  const addTodo = async (text) => {
    const indexUrl = getSourceUrl(todoList);
    const todoWithText = addStringNoLocale(
      createThing(),
      "http://schema.org/text",
      text
    );
    const todoWithDate = addDatetime(
      todoWithText,
      "http://www.w3.org/2002/12/cal/ical#created",
      new Date()
    );
    const todoWithType = addUrl(todoWithDate, "http://www.w3.org/1999/02/22-rdf-syntax-ns#type", "http://www.w3.org/2002/12/cal/ical#Vtodo");
    const updatedTodoList = setThing(todoList, todoWithType);
    const updatedDataset = await saveSolidDatasetAt(indexUrl, updatedTodoList, {
      fetch: session.fetch,
    });
    setTodoList(updatedDataset);
  };
// ...
}

```

Nous créons d'abord la `Thing`, ajoutons une chaîne et une date, puis définissons la chose dans le dataset (`todoList`). Nous devons écraser le `todoList` en le sauvegardant dans son URL, que nous obtenons en utilisant `getSourceUrl`. 

Maintenant, nous devons modifier notre composant pour pouvoir obtenir le texte d'entrée de l'utilisateur. Mettons ces prédicats dans des constantes pour garder notre code propre et éviter les bugs dus aux fautes de frappe :

```jsx
// components/AddTodo/index.js

import {
  addDatetime,
  addStringNoLocale,
  createThing,
  getSolidDataset,
  getSourceUrl,
  getUrlAll,
  saveSolidDatasetAt,
  setThing,
  getThing,
} from "@inrupt/solid-client";
import { useSession } from "@inrupt/solid-ui-react";
import React, { useEffect, useState } from "react";
import { getOrCreateTodoList } from "../../utils";

const STORAGE_PREDICATE = "http://www.w3.org/ns/pim/space#storage";
const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";
const TODO_CLASS = "http://www.w3.org/2002/12/cal/ical#Vtodo";
const TYPE_PREDICATE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type";

function AddTodo() {
  const { session } = useSession();
  const [todoList, setTodoList] = useState();
  const [todoText, setTodoText] = useState("");

  useEffect(() => {
    if (!session) return;
    (async () => {
      const profileDataset = await getSolidDataset(session.info.webId, {
        fetch: session.fetch,
      });
      const profileThing = getThing(profileDataset, session.info.webId);
      const podsUrls = getUrlAll(profileThing, STORAGE_PREDICATE);
      const pod = podsUrls[0];
      const containerUri = `${pod}todos/`;
      const list = await getOrCreateTodoList(containerUri, session.fetch);
      setTodoList(list);
    })();
  }, [session]);

  const addTodo = async (text) => {
    const indexUrl = getSourceUrl(todoList);
    const todoWithText = addStringNoLocale(createThing(), TEXT_PREDICATE, text);
    const todoWithDate = addDatetime(
      todoWithText,
      CREATED_PREDICATE,
      new Date()
    );
    const todoWithType = addUrl(todoWithDate, TYPE_PREDICATE, TODO_CLASS);
    const updatedTodoList = setThing(todoList, todoWithType);
    const updatedDataset = await saveSolidDatasetAt(indexUrl, updatedTodoList, {
      fetch: session.fetch,
    });
    setTodoList(updatedDataset);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    addTodo(todoText);
  };

  const handleChange = (e) => {
    e.preventDefault();
    setTodoText(e.target.value);
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="todo-form">
        <label htmlFor="todo-input">
          <input
            id="todo-input"
            type="text"
            value={todoText}
            onChange={handleChange}
          />
        </label>
        <button type="submit" className="add-button">
          Ajouter une tâche
        </button>
      </form>
    </>
  );
}

export default AddTodo;

```

Maintenant, si nous écrivons du texte et cliquons sur `AddTodo`, notre tâche sera ajoutée ! Mais nous ne pouvons pas encore voir nos tâches. 

Pour vérifier si cela a fonctionné, sur [PodBrowser](https://podbrowser.inrupt.com/), naviguez jusqu'à votre dossier "todos", téléchargez à nouveau le fichier `index.ttl`, et voyez s'il y a des changements. Si tout s'est bien passé, vous devriez voir quelque chose comme ceci :

```jsx
<https://pod.inrupt.com/virginiabalseiro/todos/index.ttl#16141957896165236259077375411>
        <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/12/cal/ical#Vtodo> ;
        <http://www.w3.org/2002/12/cal/ical#created>  "2021-02-24T19:43:09.616Z"^^xsd:dateTime ;
        <http://schema.org/text>  "Terminer le tutoriel de l'application Solid Todo" .

```

Vous pouvez voir qu'un identifiant aléatoire a été généré pour notre tâche. Cela se produit lorsque nous créons une chose sans passer d'URL ou de chaîne de nom pour le sujet, ce qui est correct pour ce cas. Ensuite, nous verrons comment nous pouvons récupérer nos tâches pour les afficher.

# Comment afficher les tâches

Pour afficher les tâches, nous allons utiliser deux composants supplémentaires de `solid-ui-react` : les composants `Table` et `TableColumn`.

Le composant Table a une prop obligatoire `things`, qui est un tableau d'objets contenant chaque chose dans le dataset et le dataset auquel ils appartiennent. Cela devrait ressembler à ceci :

```jsx
[{ dataset: myDataset, thing: thing1 }, { dataset: myDataset, thing: thing2 } ];

```

Dans notre cas, nous avons déjà le dataset (notre liste de tâches), mais maintenant nous devons extraire les choses de celui-ci et les mapper pour obtenir un tableau qui ressemble à celui ci-dessus.

L'endroit où nous récupérons nos tâches est dans le composant `AddTodo`. Mais nous allons créer un composant appelé `TodoList` pour afficher notre tableau, donc nous aurons besoin d'utiliser la liste là aussi. 

Déplaçons le `useEffect` vers le composant `App`, afin que nous puissions passer `todoList` et `setTodoList` aux composants qui en ont besoin. Nous ajoutons une vérification pour voir si l'utilisateur est déconnecté, auquel cas nous quittons le `useEffect`.

```jsx
// App.js

import React, { useEffect, useState } from "react";
import {
  LoginButton,
  LogoutButton,
  Text,
  useSession,
  CombinedDataProvider,
} from "@inrupt/solid-ui-react";
import { getSolidDataset, getUrlAll, getThing } from "@inrupt/solid-client";
import AddTodo from "./components/AddTodo";
import TodoList from "./components/TodoList";
import { getOrCreateTodoList } from "./utils";

const STORAGE_PREDICATE = "http://www.w3.org/ns/pim/space#storage";

const authOptions = {
  clientName: "Solid Todo App",
};

function App() {
  const { session } = useSession();
  const [todoList, setTodoList] = useState();
  const [oidcIssuer, setOidcIssuer] = useState("");

  const handleChange = (event) => {
    setOidcIssuer(event.target.value);
  };

  useEffect(() => {
    if (!session || !session.info.isLoggedIn) return; 
    (async () => {
      const profileDataset = await getSolidDataset(session.info.webId, {
        fetch: session.fetch,
      });
      const profileThing = getThing(profileDataset, session.info.webId);
      const podsUrls = getUrlAll(profileThing, STORAGE_PREDICATE);
      const pod = podsUrls[0];
      const containerUri = `${pod}todos/`;
      const list = await getOrCreateTodoList(containerUri, session.fetch);
      setTodoList(list);
    })();
  }, [session, session.info.isLoggedIn]);

  return (
    <div className="app-container">
      {session.info.isLoggedIn ? (
        <CombinedDataProvider
          datasetUrl={session.info.webId}
          thingUrl={session.info.webId}
        >
          <div className="message logged-in">
            <span>Vous êtes connecté en tant que : </span>
            <Text
              properties={[
                "http://xmlns.com/foaf/0.1/name",
                "http://www.w3.org/2006/vcard/ns#fn",
              ]}
            />
            <LogoutButton />
          </div>
          <section>
            <AddTodo todoList={todoList} setTodoList={setTodoList} />
            <TodoList todoList={todoList} setTodoList={setTodoList} />
          </section>
        </CombinedDataProvider>
      ) : (
        <div className="message">
          <span>Vous n'êtes pas connecté. </span>
          <span>
            Connectez-vous avec :
            <input
              className="oidc-issuer-input "
              type="text"
              name="oidcIssuer"
              list="providers"
              value={oidcIssuer}
              onChange={handleChange}
            />
           <datalist id="providers">
            <option value="https://broker.pod.inrupt.com/" />
            <option value="https://inrupt.net/" />
           </datalist>
          </span>
          <LoginButton
            oidcIssuer={oidcIssuer}
            redirectUrl={window.location.href}
            authOptions={authOptions}
          />
        </div>
      )}
    </div>
  );
}

export default App;

```

Et notre composant AddTodo ressemblera maintenant à ceci :

```jsx
// components/AddTodo/index.jsx

import {
  addDatetime,
  addStringNoLocale,
  createThing,
  getSourceUrl,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";
import { useSession } from "@inrupt/solid-ui-react";
import React, { useState } from "react";

const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";
const TODO_CLASS = "http://www.w3.org/2002/12/cal/ical#Vtodo";
const TYPE_PREDICATE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type";

function AddTodo({ todoList, setTodoList }) {
  const { session } = useSession();
  const [todoText, setTodoText] = useState("");

  const addTodo = async (text) => {
    const indexUrl = getSourceUrl(todoList);
    const todoWithText = addStringNoLocale(createThing(), TEXT_PREDICATE, text);
    const todoWithDate = addDatetime(
      todoWithText,
      CREATED_PREDICATE,
      new Date()
    );
    const todoWithType = addUrl(todoWithDate, TYPE_PREDICATE, TODO_CLASS);
    const updatedTodoList = setThing(todoList, todoWithType);
    const updatedDataset = await saveSolidDatasetAt(indexUrl, updatedTodoList, {
      fetch: session.fetch,
    });
    setTodoList(updatedDataset);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    addTodo(todoText);
    setTodoText("");
  };

  const handleChange = (e) => {
    e.preventDefault();
    setTodoText(e.target.value);
  };

  return (
      <form className="todo-form" onSubmit={handleSubmit}>
        <label htmlFor="todo-input">
          <input
            id="todo-input"
            type="text"
            value={todoText}
            onChange={handleChange}
          />
        </label>
        <button className="add-button" type="submit">Ajouter une tâche</button>
      </form>
  );
}

export default AddTodo;

```

Remarquez que nous avons ajouté une ligne dans `handleSubmit` pour définir le texte à une chaîne vide après avoir ajouté la tâche, afin que le contenu de la zone de saisie soit effacé.

Pour notre composant `TodoList`, nous allons avoir besoin des composants `Table` et `TableColumn` de `solid-ui-react`. Nous allons également utiliser `getThingAll` de solid-client pour extraire les choses de notre dataset afin que nous puissions créer le tableau dont nous avons besoin pour la Table. 

Pour l'instant, affichons simplement le nombre de choses que contient notre dataset :

```jsx
// components/TodoList/index.jsx

import { getThingAll } from "@inrupt/solid-client";
import { Table, TableColumn } from "@inrupt/solid-ui-react";
import React, { useEffect, useState } from "react";

function TodoList({ todoList }) {
	const todoThings = todoList ? getThingAll(todoList) : [];

  return <div>Votre liste de tâches contient {todoThings.length} éléments</div>;
}

export default TodoList;

```

Une fois que vous avez ajouté le composant `TodoList`, vous devrez peut-être arrêter et redémarrer votre application avec `npm start` si vous voyez des erreurs. 

Pour voir si cela fonctionne, essayez d'ajouter des tâches et voyez si le nombre d'éléments change. Vous remarquerez que la longueur du tableau indique un élément de plus que le nombre de tâches que vous avez créées. Cela est dû au fait qu'il y a un autre élément dans le dataset des tâches qui n'est pas une tâche. Nous corrigerons cela plus tard.

Pour utiliser le composant `Table`, nous devons créer le tableau avec les objets dont nous avons besoin et le passer à la table :

```jsx
// components/TodoList/index.jsx

function TodoList({ todoList }) {
// ...
const thingsArray = todoThings.map((t) => {
    return { dataset: todoList, thing: t };
  });
// ...
}

```

Mais pour afficher réellement quelque chose, nous devons utiliser le composant `TableColumn` à l'intérieur de la `Table`. Le composant `TableColumn` a besoin d'une prop obligatoire `property`, qui est la propriété que nous voulons afficher. Cela signifie le prédicat sous lequel les données que nous voulons afficher sont stockées. 

Dans le cas de nos tâches, nous avons deux propriétés : le `text` et la `date` à laquelle la tâche a été créée, stockées sous [http://schema.org/text](http://schema.org/text) et [http://www.w3.org/2002/12/cal/ical#created](http://www.w3.org/2002/12/cal/ical#created), respectivement :

```jsx
// ./components/TodoList/index.jsx

const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";

function TodoList({ todoList }) {
// ...
<div>
  Votre liste de tâches contient {todoThings.length} éléments
  <Table things={thingsArray}>
    <TableColumn property={TEXT_PREDICATE} />
    <TableColumn property={CREATED_PREDICATE} />
   </Table>
 </div>
// ...
}

```

Vous remarquerez deux choses : d'abord, les en-têtes. Le `TableColumn` accepte une prop optionnelle `header`, avec laquelle nous pouvons définir l'en-tête de la colonne. Si nous ne passons pas cette prop, l'en-tête sera l'URL du prédicat pour cette propriété. Vous pouvez également passer une chaîne vide si vous ne voulez pas d'en-têtes. Faisons cela pour le texte de notre tâche, et passons "Créé" pour la date.

Deuxièmement, il n'y a rien d'affiché pour la colonne créée à. Cela est dû au fait que `TableColumn` accepte également une prop optionnelle `dataType`, qui par défaut est 'string' si elle n'est pas définie, mais les données que nous avons ne sont pas une chaîne mais un datetime, donc nous devons la définir :

```jsx
// components/TodoList/index.jsx

const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";

function TodoList({ todoList }) {
// ...
	<div className="table-container">
		<span className="tasks-message">
		  Votre liste de tâches contient {todoThings.length} éléments
		</span>
	  <Table className="table" things={thingsArray}>
	    <TableColumn property={TEXT_PREDICATE} header="" />
	     <TableColumn
	       property={CREATED_PREDICATE}
	       dataType="datetime"
	       header="Créé le"
	      />
	   </Table>
	 </div>
// ...
}

```

Enfin, il serait bien si nous pouvions formater la date pour qu'elle ressemble à ceci : `sam. 26 déc. 2020`, au lieu d'une chaîne plus longue. 

La prop body nous permet de passer un corps personnalisé à la colonne, où nous pouvons formater la valeur que nous obtenons pour chaque cellule. Cette prop est super utile lorsque nous voulons passer un composant personnalisé à la cellule, par exemple un lien, au lieu de la valeur telle qu'elle vient du dataset.

Avant de faire cela, cependant, nous devons filtrer les choses non-tâches que nous avons dans notre dataset. Si vous regardez le fichier `index.ttl`, vous remarquerez une ligne qui ressemble à ceci :

```jsx
<https://pod.inrupt.com/virginiabalseiro/todos/index.ttl>
        rdf:type  ldp:RDFSource .

```

Cela est automatiquement ajouté par le serveur pour identifier le type de ressource avec lequel nous traitons, mais cela générera une erreur lorsque nous essaierons de formater la date, car il n'aura pas de propriété `created`. C'est aussi pourquoi nous avions un élément supplémentaire dans notre compte de tâches. 

Nous devons donc filtrer toutes les choses contenant une propriété `type` avec la valeur `RDFSource`.

Nous allons également passer de `todoThing` à `thingsArray` dans le message affichant le nombre d'éléments, sinon nous comptons également le `type`.

Notre composant `TodoList` ressemble maintenant à ceci :

```jsx
// ./components/TodoList/index.jsx

import React from "react";
import { getThingAll, getUrl } from "@inrupt/solid-client";
import { Table, TableColumn } from "@inrupt/solid-ui-react";

function TodoList({ todoList }) {
  const todoThings = todoList ? getThingAll(todoList) : [];

  const TEXT_PREDICATE = "http://schema.org/text";
  const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";
  const TODO_CLASS = "http://www.w3.org/2002/12/cal/ical#Vtodo";
  const TYPE_PREDICATE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type";

  const thingsArray = todoThings.filter((t) => getUrl(t, TYPE_PREDICATE) === TODO_CLASS).map((t) => {
    return { dataset: todoList, thing: t };
  });

  if (!thingsArray.length) return null;

  return (
    <div className="table-container">
      <span className="tasks-message">
        Votre liste de tâches contient {thingsArray.length} éléments
      </span>
      <Table className="table" things={thingsArray}>
        <TableColumn property={TEXT_PREDICATE} header="" />
        <TableColumn
          property={CREATED_PREDICATE}
          dataType="datetime"
		      header="Créé le"
          body={({ value }) => value.toDateString()}
        />
      </Table>
    </div>
  );
}

export default TodoList;

```

# Comment marquer une tâche comme terminée

Maintenant que nous pouvons afficher nos tâches, nous avons besoin d'un moyen de les marquer comme terminées. Nous allons stocker cet état "terminé" sous "[http://www.w3.org/2002/12/cal/ical#completed"](http://www.w3.org/2002/12/cal/ical#completed%22%5D(http://www.w3.org/2002/12/cal/ical#completed%22), avec une date et une heure comme objet. 

Ajoutons une nouvelle colonne à notre tableau :

```jsx
// components/TodoList/index.jsx

const COMPLETED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#completed";
// ...
<TableColumn
  property={COMPLETED_PREDICATE}
  dataType="datetime"
  header="Terminé"
  body={({ value }) => (
     <label>
       <input type="checkbox" />
      </label>
     )}
 />
// ...

```

Pour l'instant, cette case à cocher ne fait rien. Nous devons ajouter cette propriété avec une valeur de date et d'heure à notre chose de tâche lorsque nous cliquons sur la case à cocher. Pour cela, nous allons avoir besoin de l'URL de notre tâche, afin de pouvoir la trouver et ajouter des propriétés.

Pour cela, nous allons utiliser le hook `useThing` de `solid-ui-react`.

Nous devons écrire une fonction qui gère l'ajout d'une propriété `completed` à notre chose de tâche. Cette fonction prendra la chose de tâche comme argument, ajoutera une propriété `completed` avec une valeur `datetime`, la définira dans le dataset et sauvegardera le dataset mis à jour.

```jsx
// components/TodoList/index.jsx
import {
  addDatetime,
  getSourceUrl,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";
import {
  Table,
  TableColumn,
  useSession,
} from "@inrupt/solid-ui-react";

function TodoList({ todoList, setTodoList }) {
  const { fetch } = useSession();
  // ...
  const handleCheck = async (todo) => {
	    const todosUrl = getSourceUrl(todoList);
	    const date = new Date();
	    const doneTodo = addDatetime(
	      todo,
	      "http://www.w3.org/2002/12/cal/ical#completed",
	      date
	    );
	    const updatedTodos = setThing(todoList, doneTodo, { fetch });
	    await saveSolidDatasetAt(todosUrl, updatedTodos, {
	      fetch,
	    });
	  };
  // ...
}

```

Pour accéder à la chose de tâche, nous devons d'abord créer un composant de corps personnalisé pour notre `TableColumn`. Il doit s'agir d'un composant approprié afin que nous puissions utiliser le hook `useThing`, alors mettons-le à l'extérieur du composant `TodoList` mais dans le même fichier. Nous allons également lui passer une prop `checked` que nous utiliserons pour définir la propriété `checked` dans la case à cocher, et notre fonction `handleCheck`.

```jsx
// components/TodoList/index.jsx
import {
  Table,
  TableColumn,
  useThing,
  useSession,
} from "@inrupt/solid-ui-react";

function CompletedBody({ checked, handleCheck }) {
    const { thing } = useThing();
    return (
      <label>
        <input
          type="checkbox"
          checked={checked}
          onChange={() => handleCheck(thing)}
        />
      </label>
    );
  }

```

Maintenant, nous pouvons utiliser ce composant dans le `body` de notre colonne :

```jsx
// components/TodoList/index.jsx

<TableColumn
  property={COMPLETED_PREDICATE}
  dataType="datetime"
  header="Terminé"
  body={({ value }) => <CompletedBody checked={Boolean(value)} handleCheck={handleCheck} />}
 />

```

Maintenant, si vous cliquez sur la case à cocher, une propriété est ajoutée à la tâche. Si vous vérifiez le fichier `index.ttl`, vous verrez quelque chose comme ceci :

```jsx
<https://pod.inrupt.com/virginiabalseiro/todos/index.ttl#16089989748796144560745441174>
        <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/12/cal/ical#Vtodo> ;        
        <http://www.w3.org/2002/12/cal/ical#created>  "2020-12-26T16:09:34.880Z"^^xsd:dateTime ;
        <http://schema.org/text>  "Promener le chien" ;
        <http://www.w3.org/2002/12/cal/ical#completed>  "2020-12-26T16:09:39.853Z"^^xsd:dateTime .

```

Nous voudrons également marquer les tâches comme "non terminées", ce qui revient essentiellement à supprimer cette propriété de la tâche. Pour cela, nous devrons modifier notre fonction `handleCheck` afin qu'elle supprime la tâche si elle était marquée comme terminée au moment de cliquer sur la case à cocher, ou l'ajoute si elle était non terminée :

```jsx
// components/TodoList/index.jsx
import {
  addDatetime,
  getDatetime,
  getSourceUrl,
  getThingAll,
  getUrl, 
  removeDatetime,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";

const COMPLETED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#completed";

function TodoList({ todoList, setTodoList }) {
const { fetch } = useSession();
// ...

const handleCheck = async (todo, checked) => {
    const todosUrl = getSourceUrl(todoList);
    let updatedTodos;
    let date;
    if (!checked) {
      date = new Date();
      const doneTodo = addDatetime(todo, COMPLETED_PREDICATE, date);
      updatedTodos = setThing(todoList, doneTodo, { fetch });
    } else {
      date = getDatetime(todo, COMPLETED_PREDICATE);
      const undoneTodo = removeDatetime(todo, COMPLETED_PREDICATE, date);
      updatedTodos = setThing(todoList, undoneTodo, { fetch });
    }
    const updatedList = await saveSolidDatasetAt(todosUrl, updatedTodos, {
      fetch,
    });
    setTodoList(updatedList);
  };
// ...
}

```

Et nous devons également mettre à jour le composant `CompletedBody` :

```jsx
// components/TodoList/index.jsx

function CompletedBody({ checked, handleCheck }) {
    const { thing } = useThing();
    return (
      <label>
        <input
          type="checkbox"
          checked={checked}
          onChange={() => handleCheck(thing, checked)}
        />
      </label>
    );
  }

```

Remarquez que nous devons utiliser `setTodoList` ici pour mettre à jour la liste de tâches, que nous obtenons du composant `App`.

Il y a cependant un petit bug : chaque fois que nous cocher une tâche, notre liste se réorganise.

Pour corriger cela, nous pouvons trier le tableau des choses après avoir extrait les choses du dataset de la liste de tâches. Nous voulons qu'elles soient triées par la date à laquelle elles ont été créées :

```jsx
// components/TodoList/index.jsx

const todoThings = todoList ? getThingAll(todoList) : [];
  todoThings.sort((a, b) => {
    return (
      getDatetime(a, CREATED_PREDICATE) - getDatetime(b, CREATED_PREDICATE)
    );
  });

```

De plus, avec le composant `TableColumn`, nous pouvons trier les éléments par propriété. Si nous passons une prop `sortable` à l'une de nos colonnes, nous pouvons organiser nos tâches en fonction de cette propriété, alors utilisons la colonne "Créé le" et la colonne de contenu de la tâche pour voir comment cela fonctionne. Ajoutons également un en-tête "À faire" à la colonne de contenu afin que nous puissions voir selon quels critères nous trions. 

Notre composant `TodoList` (presque) terminé ressemble maintenant à ceci :

```jsx
// components/TodoList/index.jsx

import {
  addDatetime,
  getDatetime,
  getSourceUrl,
  getThingAll,
  getUrl,
  removeDatetime,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";
import {
  Table,
  TableColumn,
  useThing,
  useSession,
} from "@inrupt/solid-ui-react";
import React from "react";

const TEXT_PREDICATE = "http://schema.org/text";
const CREATED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#created";
const COMPLETED_PREDICATE = "http://www.w3.org/2002/12/cal/ical#completed";

function CompletedBody({ checked, handleCheck }) {
    const { thing } = useThing();
    return (
      <label>
        <input
          type="checkbox"
          checked={checked}
          onChange={() => handleCheck(thing, checked)}
        />
      </label>
    );
  }

function TodoList({ todoList, setTodoList }) {
  const todoThings = todoList ? getThingAll(todoList) : [];
  todoThings.sort((a, b) => {
    return (
      getDatetime(a, CREATED_PREDICATE) - getDatetime(b, CREATED_PREDICATE)
    );
  });

  const { fetch } = useSession();

  const handleCheck = async (todo, checked) => {
    const todosUrl = getSourceUrl(todoList);
    let updatedTodos;
    if (!checked) {
      const date = new Date();
      const doneTodo = addDatetime(todo, COMPLETED_PREDICATE, date);
      updatedTodos = setThing(todoList, doneTodo, { fetch });
    } else {
      const date = getDatetime(todo, COMPLETED_PREDICATE);
      const undoneTodo = removeDatetime(todo, COMPLETED_PREDICATE, date);
      updatedTodos = setThing(todoList, undoneTodo, { fetch });
    }
    const updatedList = await saveSolidDatasetAt(todosUrl, updatedTodos, {
      fetch,
    });
    setTodoList(updatedList);
  };

  const thingsArray = todoThings
    .filter((t) => getUrl(t, TYPE_PREDICATE) === TODO_CLASS)
    .map((t) => {
      return { dataset: todoList, thing: t };
    });
  if (!thingsArray.length) return null;

  return (
    <div className="table-container">
      <span className="tasks-message">
        Votre liste de tâches contient {thingsArray.length} éléments
      </span>
      <Table className="table" things={thingsArray}>
        <TableColumn property={TEXT_PREDICATE} header="À faire" sortable />
        <TableColumn
          property={CREATED_PREDICATE}
          dataType="datetime"
          header="Créé le"
          body={({ value }) => value.toDateString()}
          sortable
        />
        <TableColumn
          property={COMPLETED_PREDICATE}
          dataType="datetime"
          header="Terminé"
          body={({ value }) => <CompletedBody checked={Boolean(value)} handleCheck={handleCheck} />}
        />
      </Table>
    </div>
  );
}

export default TodoList;

```

# Comment supprimer une tâche

Pour supprimer une tâche, nous aurons besoin d'une nouvelle colonne pour ajouter un bouton de suppression.

Nous devrons également écrire une fonction qui prend la `Thing` de la tâche et la supprime au clic :

```jsx
// components/TodoList/index.jsx

import {
  addDatetime,
  getDatetime,
  getSourceUrl,
  getThingAll,
  getUrl,
  removeDatetime,
	removeThing,
  saveSolidDatasetAt,
  setThing,
} from "@inrupt/solid-client";

function TodoList({ todoList, setTodoList }) {
// ...
	const deleteTodo = async (todo) => {
	    const todosUrl = getSourceUrl(todoList);
	    const updatedTodos = removeThing(todoList, todo);
	    const updatedDataset = await saveSolidDatasetAt(todosUrl, updatedTodos, {
	      fetch,
	    });
	    setTodoList(updatedDataset);
	  };
// ...
}

```

Nous pouvons obtenir la `Thing` de la tâche en utilisant le hook `useThing` (comme nous l'avons fait précédemment avec le composant `CompleteBody` pour marquer les tâches comme terminées), donc cela n'a pas vraiment d'importance quelle propriété nous utilisons. Mais parce que `property` n'est pas optionnel dans le composant `TableColumn`, nous utiliserons le texte de la tâche.

Puisque nous devons utiliser un hook, nous devons écrire un composant React approprié pour le corps personnalisé en dehors du composant `TodoList` :

```jsx
// components/TodoList/index.jsx

function DeleteButton({ deleteTodo }) {
    const { thing } = useThing();
    return (
      <button className="delete-button" onClick={() => deleteTodo(thing)}>
        Supprimer
      </button>
    );
  }

```

Et ajoutons la colonne au tableau, après la dernière colonne :

```jsx
// components/TodoList/index.jsx

<TableColumn
          property={TEXT_PREDICATE}
          header=""
          body={() => <DeleteButton deleteTodo={deleteTodo} />}
        />

```

C'est tout ! Maintenant, si nous cliquons sur le bouton de suppression, nous pouvons supprimer la tâche.

# Conclusion

### Où aller à partir de là

Vous avez terminé le tutoriel ! Vous connaissez maintenant les bases de la création de votre propre application Solid. Vous pouvez maintenant créer votre propre application à partir de zéro, expérimenter et apprendre davantage. Voici quelques ressources pour vous aider :

* [Documentation de Solid UI React](https://solid-ui-react.docs.inrupt.com/?path=/story/intro--page)
* [Documentation des bibliothèques clientes Solid](https://docs.inrupt.com/developer-tools/javascript/client-libraries/)
* [Applications Solid que vous pouvez tester et avec lesquelles vous pouvez jouer](https://inrupt.com/solidApps/solid-app-listing)
* [Le forum de la communauté Solid, où vous pouvez poser des questions et voir de quoi parlent les gens](https://forum.solidproject.org/)