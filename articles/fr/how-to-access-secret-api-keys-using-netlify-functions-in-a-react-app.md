---
title: Comment accéder en toute sécurité aux clés API secrètes en utilisant les fonctions
  Netlify dans une application React
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2021-06-28T21:17:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-access-secret-api-keys-using-netlify-functions-in-a-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/pexels-noelle-otto-906018.jpg
tags:
- name: Application Security
  slug: application-security
- name: create-react-app
  slug: create-react-app
- name: information security
  slug: information-security
- name: Netlify
  slug: netlify
- name: React
  slug: react
seo_title: Comment accéder en toute sécurité aux clés API secrètes en utilisant les
  fonctions Netlify dans une application React
seo_desc: 'In this article, you will learn how to securely access secret API keys
  using Netlify functions in a React app.

  Netlify provides rich features that help you easily deploy Single Page Applications
  built using frameworks like React, Vue and Angular amon...'
---

Dans cet article, vous apprendrez comment accéder en toute sécurité aux clés API secrètes en utilisant les fonctions Netlify dans une application React.

Netlify fournit des fonctionnalités riches qui vous aident à déployer facilement des applications monopages construites à l'aide de frameworks comme [React](https://reactjs.org/), [Vue](https://v3.vuejs.org/) et [Angular](https://angular.io/) parmi d'autres. Cela élimine le fardeau de coder et de maintenir du code côté serveur.

Dans certains cas, une application front-end doit communiquer avec une API tierce externe. Certaines de ces API tierces nécessitent des clés API secrètes pour y accéder.

Imaginons une situation où vous souhaitez inclure des alertes météo dans votre application front-end. Par conséquent, vous vous inscrivez au plan payant de l'API [open weather map](https://openweathermap.org/api) qui nécessite une clé API secrète pour y accéder.

Dans de telles situations, vous devrez veiller à ne pas exposer la clé API secrète sur le front-end.

Netlify fournit une fonctionnalité sur son interface utilisateur web que vous pouvez utiliser pour masquer les clés API. Mais la clé API peut être accessible depuis le côté client si la variable d'environnement dans laquelle elle est stockée est accessible depuis le code front-end.

## Ce que vous apprendrez dans cet article

Dans cet article, vous allez masquer la clé API secrète sur l'interface utilisateur de Netlify et y accéder en toute sécurité en utilisant les fonctions Netlify dans une application React créée avec [create-react-app(CRA)](https://create-react-app.dev/). L'utilisation des fonctions Netlify garantit que la clé API n'est pas exposée côté client.

Le processus devrait être similaire pour d'autres frameworks, bien que nous utilisions [React](https://reactjs.org/) dans cet article.

À la fin de cet article, vous serez en mesure de faire ce qui suit :

* Ajouter une fonction Netlify à une application React

* Utiliser les fonctions Netlify pour accéder en toute sécurité aux clés API secrètes

* Utiliser l'outil [netlify-cli](https://docs.netlify.com/cli/get-started/) pour tester vos fonctions Netlify

## Prérequis

Voici quelques-uns des prérequis pour cet article. Il est utile de noter que vous pouvez toujours suivre même si vous ne cochez pas toutes les cases.

Vous pouvez rechercher sur Google si quelque chose ne vous est pas clair ou poser une question sur le [forum freeCodeCamp](https://forum.freecodecamp.org/). Nous serons heureux de vous aider.

* Avoir au moins une compréhension de base de [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), du framework [React](https://reactjs.org/), et d'un système de contrôle de version comme [Git](https://git-scm.com/).

* Avoir [Node](https://nodejs.org/en/) installé sur votre machine. Si vous ne l'avez pas installé, vous pouvez le télécharger pour votre système depuis la [page de téléchargements de Node](https://nodejs.org/en/download/).

* Avoir [Git](https://git-scm.com/) installé sur votre machine. Si vous ne l'avez pas installé, vous pouvez le faire depuis la [page de téléchargements de Git](https://git-scm.com/downloads).

* Avoir un éditeur de texte comme [VS code](https://code.visualstudio.com/) ou [Atom](https://atom.io/) installé.

* Avoir un compte [Netlify](https://www.netlify.com/). Si vous n'en avez pas, vous pouvez [vous inscrire](https://app.netlify.com/signup) sans frais en utilisant votre adresse e-mail.

* Avoir une connaissance de base de la fonctionnalité de [déploiement continu](https://docs.netlify.com/site-deploys/create-deploys/#deploy-with-git) de Netlify. Vous l'utiliserez pour déployer votre application React sur Netlify depuis [GitHub](https://github.com/).

* Avoir un compte [GitHub](https://github.com/) car nous utiliserons la fonctionnalité de [déploiement continu](https://docs.netlify.com/site-deploys/create-deploys/#deploy-with-git) de Netlify. Si vous n'avez pas de compte, vous pouvez [vous inscrire](https://github.com/) en utilisant votre adresse e-mail.

## Comment utiliser les variables d'environnement dans une application React créée avec `create-react-app`

Dans cette section, vous apprendrez comment utiliser les variables d'environnement dans une application React créée avec [`CRA`](https://create-react-app.dev/). Si vous êtes déjà familier avec cette méthode, vous pouvez passer à la section suivante.

Les applications React créées avec [CRA](https://create-react-app.dev/) sont configurées pour que vous puissiez créer des variables d'environnement personnalisées dans le fichier `.env` et y accéder dans votre codebase en utilisant `process.env`.

Pour utiliser cette fonctionnalité, vous pouvez suivre les étapes ci-dessous. Ces étapes supposent que vous avez déjà créé une application React avec [CRA](https://create-react-app.dev/).

### Étape 1 - Créer un fichier `.env` à la racine du répertoire du projet

Commencez par créer un fichier `.env` à la racine du répertoire du projet. Vous pouvez ensuite ajouter vos variables d'environnement dans le fichier `.env` pour qu'elles ressemblent à ceci :

```shell
REACT_APP_FIRST_SECRET=12345678
REACT_APP_SECOND_SECRET=123456789
```

Dans le fichier `.env` ci-dessus, les variables d'environnement sont `REACT_APP_FIRST_SECRET` et `REACT_APP_SECOND_SECRET`. Leurs valeurs correspondantes sont du côté droit. Vous devez noter quelques points lors de l'utilisation des variables d'environnement avec [CRA](https://create-react-app.dev/) :

* La variable d'environnement doit toujours commencer par `REACT_APP` et être suivie du nom de la variable pour qu'elle fonctionne. Par exemple, vous pouvez nommer la variable contenant votre clé API `REACT_APP_API_KEY`.

* Il ne doit y avoir aucun espace avant et après le `=`.

### Étape 2 - Accéder à la variable d'environnement dans votre application en utilisant `process.env`

Vous pouvez ensuite accéder à ces variables d'environnement dans votre application React en utilisant `process.env.REACT_APP_FIRST_SECRET` et `proces.env.REACT_APP_SECOND_SECRET`. Ces variables sont ajoutées à votre codebase au moment de la construction, vous devez donc redémarrer votre serveur de développement si vous exécutez l'application sur `localhost` pour que les modifications prennent effet.

L'accès à la variable d'environnement de cette manière vous empêche de pousser votre clé API secrète vers un service d'hébergement Git distant comme [GitHub](https://github.com/).

[CRA](https://create-react-app.dev/) ajoute le fichier `.gitignore` par défaut. Vous devez simplement ajouter le fichier `.env` pour que Git ignore votre fichier `.env` lorsque vous validez vos modifications.

Ce que vous venez d'apprendre sur les variables d'environnement gardera vos secrets en sécurité pendant le développement.

Mais que se passera-t-il si vous faites la même chose en production puisque les variables d'environnement sont ajoutées à votre codebase au moment de la construction ? La section suivante répondra à cette question.

## Accéder aux variables d'environnement depuis une application React créée avec `create-react-app` expose vos clés API

Oui, en effet. Malheureusement, certains débutants absolus pensent le contraire. Cela m'incluait lorsque je commençais. Mais même la [documentation de create-react-app](https://create-react-app.dev/) indique que :

> Les variables d'environnement sont intégrées dans la construction, ce qui signifie que quiconque peut les consulter en inspectant les fichiers de votre application - [documentation de create-react-app](https://create-react-app.dev/)

Pour illustrer cela, j'ai construit une [simple application de démonstration](https://netlify-secrets-demo.netlify.app/) et l'ai déployée sur Netlify. Il s'agit d'une simple application React créée avec [CRA](https://create-react-app.dev/). Si vous êtes intéressé, vous pouvez forker le [dépôt du projet](https://github.com/nibble0101/netlify-secrets-demo-app) et déployer l'application sur Netlify sous votre compte.

Dans cette application, je récupère un élément de todo de remplissage depuis l'API [JSON placeholder](https://jsonplaceholder.typicode.com/todos) et l'affiche à l'utilisateur.

L'API [JSON placeholder](https://jsonplaceholder.typicode.com/todos) ne nécessite pas de clé API pour y accéder. Mais pour cette illustration, j'utilise l'URL de base comme "secret" que je ne veux pas exposer.

La plupart des API basées sur le web nécessitent de passer la clé API comme paramètre de requête lors de l'autorisation des utilisateurs. Lors du déploiement de l'application, j'ai défini la valeur de `REACT_APP_TODO_BASE_URL` sur `https://jsonplaceholder.typicode.com/todos` sur l'interface web de Netlify.

Il existe deux façons d'accéder à la valeur que j'ai masquée dans la variable d'environnement depuis le front-end :

1. En inspectant le codebase de l'application

2. En inspectant l'onglet Network dans les [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

### Comment inspecter le codebase de l'application

Pour inspecter le codebase de l'application, suivez les étapes ci-dessous :

1. Accédez à l'application de démonstration déployée [demo app](https://netlify-secrets-demo-app.netlify.app/).

2. Ouvrez les outils de développement du navigateur. Vous pouvez les ouvrir en appuyant sur la combinaison de touches `CTRL + SHIFT + I` sur Chrome ou en cliquant avec le bouton droit et en sélectionnant l'option Inspecter dans Chrome. Cliquez sur l'onglet `Sources`. Voici à quoi cela ressemble pour moi dans Chrome si l'onglet `Sources` est actif. Cela peut être différent dans d'autres navigateurs.

    ![005-01-sources-tab](https://www.freecodecamp.org/news/content/images/2021/06/005-01-sources-tab.png align="left")

3. Dans l'onglet `Sources`, vous devriez voir le dossier `top` sous l'onglet `Page`. Naviguez ensuite depuis le dossier `top` vers `main.e54a1b49.chunk.js` en suivant le chemin `top/netlify-secrets-demo-app.netlify.app/static/js/main.e54a1b49.chunk.js`. `main.e54a1b49.chunk.js` est un fichier minifié en une seule ligne qui n'est pas lisible.

    ![005-02-sources-folder](https://www.freecodecamp.org/news/content/images/2021/06/005-02-sources-folder.png align="left")

4. Cliquez sur le symbole `{}` en bas à gauche du panneau pour afficher le code de manière lisible.

5. Le secret que nous avons masqué dans la variable d'environnement est là dans le codebase à la ligne 37 comme montré dans l'image ci-dessous.

    ![005-03-pretty-code](https://www.freecodecamp.org/news/content/images/2021/06/005-03-pretty-code.png align="left")

### Comment inspecter l'onglet Network dans les [Devtools](https://developer.chrome.com/docs/devtools/)

1. Accédez à l'application de démonstration déployée [demo app](https://netlify-secrets-demo-app.netlify.app/)

2. Ouvrez l'outil de développement du navigateur, puis ouvrez l'onglet Network. L'onglet Network devrait ressembler à l'image ci-dessous dans Chrome. Cela peut être différent dans d'autres navigateurs.

    ![005-04-network-tab](https://www.freecodecamp.org/news/content/images/2021/06/005-04-network-tab.png align="left")

3. Cliquez sur le bouton `Get another todo` dans le navigateur. Vous devriez voir une autre ligne dans le panneau ouvert indiquant qu'une autre requête a été faite. Voici à quoi cela ressemble pour moi dans l'image ci-dessous.

    ![005-05-network-request-made](https://www.freecodecamp.org/news/content/images/2021/06/005-05-network-request-made.png align="left")

4. Cliquez sur la dernière ligne. Un autre panneau s'ouvrira montrant les en-têtes de requête et de réponse. Encore une fois, notre "secret" a été exposé.

    ![005-06-response-header-open](https://www.freecodecamp.org/news/content/images/2021/06/005-06-response-header-open.png align="left")

Comme vous pouvez le voir ci-dessus, votre clé API peut ne pas être visible dans le codebase qui a été validé sur [GitHub](https://github.com/), mais elle est toujours accessible côté client. Maintenant, vous savez ce qui se passerait si votre clé était pour un plan payant.

Pour garder votre clé secrète secrète, vous devez accéder à votre variable d'environnement en utilisant les [fonctions Netlify](https://www.netlify.com/products/functions/).

Dans la section suivante, vous apprendrez comment accéder en toute sécurité aux variables d'environnement en utilisant les fonctions Netlify. Vous le ferez en ajoutant des fonctions Netlify à une application React et en la déployant sur Netlify.

## Comment accéder en toute sécurité aux variables d'environnement avec les fonctions Netlify

Dans cette section, vous allez forker une simple application React qui a été créée avec [CRA](https://create-react-app.dev/) et ajouter une fonction Netlify. Vous utiliserez ensuite votre fonction pour accéder à la variable d'environnement au lieu d'y accéder depuis votre code front-end.

Cela garantira que vous n'exposez pas votre clé API secrète comme illustré dans la section ci-dessus. Vous déployerez ensuite l'application sur Netlify en utilisant la fonctionnalité de [déploiement continu](https://docs.netlify.com/site-deploys/create-deploys/#deploy-with-git) de Netlify.

### Qu'est-ce qu'une fonction Netlify ?

Il s'agit d'une fonction que vous pouvez utiliser pour exécuter du code côté serveur sans avoir à déployer votre propre serveur.

Selon la [documentation](https://docs.netlify.com/functions/overview/), si vous utilisez les fonctions Netlify, vous utilisez indirectement les fonctions Lambda serverless d'AWS qui sont utilisées pour exécuter du code côté serveur à la demande sans avoir à exécuter un serveur dédié.

Voici quelques-unes des raisons pour lesquelles vous pourriez avoir besoin d'utiliser les fonctions Netlify.

* Récupérer des données en direct depuis une API

* Retourner des images dynamiques

* Envoyer des e-mails automatisés

Pour commencer à utiliser les fonctions Netlify, créez un dossier à la racine du répertoire du projet et nommez-le `netlify`.

À l'intérieur du dossier Netlify, vous devez créer un autre dossier appelé `functions`. Dans le dossier `functions`, vous pouvez créer un fichier qui contient une fonction exécutant votre code. Par conséquent, le chemin vers les fichiers contenant vos fonctions doit être `netlify/functions`.

Il s'agit de l'emplacement par défaut où Netlify recherchera vos fonctions. Si vous souhaitez changer le répertoire où vos fonctions sont situées à l'intérieur du dossier `netlify`, vous devez ajouter cette information à un fichier de configuration `netlify.toml` à la racine du répertoire du projet afin que Netlify sache où les rechercher.

L'utilisation de `netlify.toml` est hors du cadre de cet article. Nous utiliserons la configuration par défaut.

Voici à quoi ressemble une fonction Netlify. Supposons que j'ai créé un fichier `todo.js` dans `netlify/functions` et que j'ai ajouté le code ci-dessous.

```js
const axios = require("axios");

exports.handler = async function (event, context) {
  // Accéder en toute sécurité aux variables d'environnement ici
};
```

Vous remarquerez que la fonction a deux paramètres, `event` et `context`. Si la fonction a besoin d'une dépendance, assurez-vous de l'ajouter au fichier `package.json` de votre projet.

Dans ce cas, j'ai ajouté `axios` comme dépendance. Cette fonction est exécutée chaque fois que nous atteignons le point de terminaison `netlify/functions/todo`.

Il existe d'autres moyens de déclencher les fonctions Netlify, mais pour cet article, concentrons-nous sur le cas d'utilisation le plus simple.

Les données passées depuis le front-end peuvent être accessibles dans le paramètre `event`. Dans le corps de la fonction, vous pouvez faire ce que vous voulez, y compris accéder en toute sécurité à votre clé API et envoyer des données au front-end.

C'est ce que vous devez savoir pour commencer à utiliser les fonctions Netlify. Si vous souhaitez approfondir et explorer ce que vous pouvez faire d'autre avec elles, consultez la [documentation](https://docs.netlify.com/functions/overview/).

Maintenant que vous comprenez les bases des [fonctions Netlify](https://docs.netlify.com/functions/overview/), suivez les étapes ci-dessous pour apprendre comment les implémenter dans une base de code.

Vous allez forker [cette application de démonstration](https://github.com/nibble0101/netlify-secrets-demo-app) et ajouter des fonctions Netlify. Il s'agit d'un simple projet React créé avec [CRA](https://create-react-app.dev/).

### Étape 1 - Comment forker le projet sous votre propre compte GitHub

Dans cette étape, vous allez forker l'application de démonstration [demo app](https://github.com/nibble0101/netlify-secrets-demo-app) sous votre propre compte GitHub. Il est nécessaire de forker le projet sous votre compte afin de pouvoir le déployer sur Netlify.

Si vous n'êtes pas intéressé par le fork du projet mais souhaitez implémenter les fonctions Netlify dans votre projet, passez à l'étape 6.

Si vous ne savez pas comment forker un dépôt GitHub, vous pouvez suivre les étapes décrites dans la section [comment forker un dépôt](https://docs.github.com/en/get-started/quickstart/fork-a-repo) de la documentation GitHub.

### Étape 2 - Comment cloner le projet sur votre machine locale

Dans cette étape, vous allez cloner le projet sur votre machine locale en exécutant la commande ci-dessous (en supposant que vous avez forké le projet sous votre compte). N'oubliez pas de remplacer `GITHUB_USER_NAME` par votre nom d'utilisateur GitHub.

```shell
git clone git@github.com:GITHUB_USER_NAME/netlify-secrets-demo-app.git
```

ou

```shell
git clone https://github.com/GITHUB_USER_NANE/netlify-secrets-demo-app.git
```

Après avoir cloné le projet avec succès sur votre machine, vous devriez voir le dossier `netlify-secrets-demo-app` contenant votre projet dans le répertoire où le projet a été cloné.

Vous pouvez naviguer vers le répertoire du projet et l'ouvrir dans votre éditeur de texte préféré.

À l'étape suivante, vous installerez les dépendances.

### Étape 3 - Comment installer les dépendances

Dans cette étape, vous installerez les dépendances en exécutant la commande ci-dessous sur le terminal.

```shell
npm install
```

La commande ci-dessus installera les dépendances dont vous avez besoin. Le processus d'installation peut prendre quelques minutes, vous devez donc être patient.

À l'étape suivante, vous créerez un fichier `.env` et y ajouterez des variables d'environnement.

### Étape 4 - Comment créer un fichier `.env`

Dans cette étape, vous allez créer un fichier `.env` à la racine du répertoire du projet en exécutant la commande ci-dessous sur le terminal :

```shell
touch .env
```

Vous devriez voir le fichier `.env` créé à la racine du répertoire du projet. Copiez et collez le contenu du fichier `example.env` dans celui-ci.

Puisque nous utiliserons les fonctions Netlify pour accéder aux variables d'environnement, vous n'avez pas besoin de préfixer le nom de la variable avec `REACT_APP` comme décrit au début de l'article. Changez la variable d'environnement `REACT_APP_TODO_BASE_URL` en `TODO_BASE_URL` et définissez sa valeur sur `https://jsonplaceholder.typicode.com/todos`.

À l'étape suivante, vous ajouterez des fonctions Netlify à votre application.

### Étape 5 - Comment ajouter des fonctions Netlify à votre application

Dans cette étape, vous ajouterez une fonction Netlify à l'application et l'utiliserez pour accéder en toute sécurité à vos variables d'environnement.

Comme je l'ai mentionné ci-dessus, par défaut, Netlify recherchera vos fonctions dans le répertoire `functions` qui doit être situé dans le dossier `netlify`.

Si vous conservez les fonctions dans un répertoire différent à l'intérieur du dossier `netlify`, vous devez fournir des informations supplémentaires dans le fichier de configuration `netlify.toml` à la racine du répertoire du projet. Cela garantira que Netlify sait où localiser vos fonctions. Mais dans cet article, nous utiliserons la configuration par défaut de Netlify.

Créez un dossier à la racine du répertoire du projet et nommez-le `netlify`. Dans le dossier `netlify`, créez un autre dossier et appelez-le `functions`. Dans le dossier `functions`, créez le fichier `todo.js`.

Copiez et collez le code ci-dessous dans le fichier `todo.js` :

```js
const axios = require("axios");

exports.handler = async function (event, context) {
  console.log(event);
  console.log(context);
  try {
    const { id } = event.queryStringParameters;
    const response = await axios.get(`${process.env.TODO_BASE_URL}/${id}`);
    return {
      statusCode: 200,
      body: JSON.stringify({ title: response.data.title }),
    };
  } catch (err) {
    return {
      statusCode: 404,
      body: err.toString(),
    };
  }
};
```

Nous allons envoyer des données depuis le front-end en tant que valeur du paramètre `id` dans la chaîne de requête. Il est accessible dans la propriété `queryStringParameters` de l'objet `event`.

Vous pouvez également `console.log` les paramètres `event` et `context` pour voir quelles sont leurs propriétés.

Nous accédons en toute sécurité à la variable d'environnement et utilisons `axios` pour récupérer notre todo. Si cela réussit, nous renvoyons un objet de réponse avec un `statusCode` de 200 avec les données dans le corps de l'objet de réponse. Si une erreur se produit, nous renvoyons un `statusCode` de 404 et l'erreur est renvoyée dans le corps de l'objet de réponse.

La fonction que vous avez ajoutée ci-dessus sera exposée à votre code front-end via le point de terminaison `/.netlify/functions/todo`. Elle sera exécutée chaque fois que vous atteignez le point de terminaison `/.netlify/functions/todo`. Maintenant, exécutons la fonction depuis le front-end.

Naviguez vers le composant `App.js` dans le dossier `src`. Dans le hook `useEffect` à la ligne 15, au lieu d'accéder à `process.env.` dans le front-end, nous faisons plutôt une requête `GET` à notre point de terminaison exposé par la fonction Netlify que nous avons déclarée à l'étape précédente.

Changez donc la ligne 15 de :

```js
const url = `${process.env.REACT_APP_TODO_BASE_URL}/${todoId}`;
```

en :

```js
const url = `/.netlify/functions/todo?id=${todoId}`;
```

Votre composant `App.js` devrait maintenant ressembler à ceci :

```js
import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [todoId, setTodoId] = useState(1);
  const [todo, setTodo] = useState("");
  const [loading, setLoading] = useState(false);

  function getNewTodo() {
    setTodoId((todoId) => (todoId === 20 ? 1 : todoId + 1));
  }

  useEffect(() => {
    async function fetchTodo() {
      const url = `/.netlify/functions/todo?id=${todoId}`;
      try {
        setLoading(true);
        const todo = await fetch(url).then((res) => res.json());
        setTodo(todo.title);
      } catch (err) {
        console.log(err);
      } finally {
        setLoading(false);
      }
    }
    fetchTodo();
  }, [todoId]);

  return (
    <div className="App">
      <p>
        <button onClick={getNewTodo}> Get another todo </button>
      </p>
      <p>{loading ? "Loading..." : todo}</p>
    </div>
  );
}

export default App;
```

Dans le code ci-dessus, nous stockons `todo` et `todoId` dans l'état. Remarquez que la requête `GET` que nous faisons au point de terminaison `/.netlify/functions/todo` dans le hook `useEffect`. Nous passons `todoId` comme valeur du paramètre de requête `id`.

Après avoir fait la requête fetch, notre fonction `todo.js` sera invoquée. À l'intérieur de `todo.js`, comme expliqué ci-dessus, nous accéderons à la variable d'environnement et récupérerons le todo qui est retourné par la fonction pour que le code front-end l'utilise. Cela garde notre variable d'environnement en sécurité puisque elle n'est pas accessible depuis le front-end. Le front-end ne consomme que ce que la fonction retourne.

À l'étape suivante, vous testerez si la fonction que vous venez de définir fonctionne comme prévu.

### Étape 6 - Comment tester votre fonction Netlify

Dans cette étape, vous utiliserez [netlify-cli](https://docs.netlify.com/cli/get-started/) pour tester si la fonction que vous avez définie fonctionne comme prévu.

Exécutez la commande ci-dessous pour installer `netlify-cli` globalement. L'installation prendra un peu de temps, soyez patient :

```js
npm install netlify-cli -g
```

Après que `netlify-cli` soit installé globalement, exécutez cette commande pour tester votre fonction :

```js
netlify dev
```

L'exécution de la commande ci-dessus démarrera un serveur de développement local sur le port 8888. Vous verrez également les paramètres `event` et `context` imprimés sur la console lorsque votre fonction sera invoquée.

Vous pouvez également tester la fonction en exécutant la commande ci-dessous sur un autre terminal. Assurez-vous que le serveur est en cours d'exécution avant d'exécuter la commande ci-dessous, sinon vous obtiendrez une erreur.

```js
netlify functions:invoke --querystring "id=1"
```

Cette commande invoquera la fonction avec la chaîne de requête spécifiée. Vous serez invité à faire quelques sélections sur le terminal. Appuyez simplement sur Entrée.

L'exécution de la commande ci-dessus récupérera notre todo qui sera ensuite imprimé sur le terminal.

```js
{"title":"delectus aut autem"}
```

À l'étape suivante, vous déployerez le projet sur votre machine locale vers GitHub.

### Étape 7 - Comment valider vos modifications et les pousser vers GitHub

Dans cette étape, vous validerez les modifications sur votre machine locale et les pousserez vers GitHub en utilisant les commandes ci-dessous.

```shell
git commit -m "Add netlify functions"
git push origin master
```

À l'étape suivante, vous utiliserez la fonctionnalité de [déploiement continu](https://docs.netlify.com/site-deploys/create-deploys/#deploy-with-git) de Netlify pour déployer l'application depuis GitHub.

### Étape 8 - Comment déployer l'application sur Netlify depuis GitHub

Dans cette étape, vous utiliserez la fonctionnalité de [déploiement continu](https://docs.netlify.com/site-deploys/create-deploys/#deploy-with-git) de Netlify pour déployer depuis GitHub.

Cette étape nécessite que vous ayez un compte Netlify. Si vous ne vous êtes pas inscrit, vous pouvez le faire depuis la [page d'inscription](https://app.netlify.com/signup) sans frais.

Connectez-vous à votre compte Netlify et suivez le processus de liaison d'un dépôt GitHub à Netlify pour le déploiement continu [comme décrit dans la documentation](https://docs.netlify.com/configure-builds/get-started/#basic-build-settings). N'oubliez pas d'ajouter la variable d'environnement `TODO_BASE_URL` et de définir sa valeur sur `https://jsonplaceholder.typicode.com/todos` sous les paramètres avancés lors du déploiement de l'application sur Netlify.

Et voilà ! C'est ainsi que vous masquez les clés API secrètes en utilisant les fonctions Netlify. J'espère que vous avez apprécié la lecture de l'article.

## Conclusion

Dans cet article, nous avons appris comment :

* Ajouter une fonction Netlify à une application React

* Utiliser les fonctions Netlify pour accéder en toute sécurité aux clés API secrètes

* Utiliser l'outil [netlify-cli](https://docs.netlify.com/cli/get-started/) pour tester vos fonctions Netlify

Avec les [fonctions serverless de Netlify](https://www.netlify.com/products/functions/), vous pouvez envoyer des e-mails, récupérer des données depuis une API comme nous venons de le faire, et bien plus encore. Cela a équipé les développeurs front-end avec les outils pour écrire du code back-end sans se soucier de la maintenance du serveur.

Vous pouvez explorer davantage ce que vous pouvez faire avec les fonctions Netlify dans la [section des fonctions de la documentation](https://docs.netlify.com/functions/overview/).

Enfin, si vous avez des questions sur ce que nous avons couvert dans cet article, n'hésitez pas à demander sur le [forum freeCodeCamp](https://forum.freecodecamp.org/) ou à m'envoyer un message sur [Twitter](https://twitter.com/MJMAWA). Vous pouvez également poser votre question dans le [forum Netlify](https://answers.netlify.com/).

Merci d'avoir lu !