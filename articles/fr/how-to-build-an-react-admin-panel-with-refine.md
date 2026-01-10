---
title: Comment construire un panneau d'administration React avec Refine
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2023-02-03T23:46:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-react-admin-panel-with-refine
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/database-admin.jpg
tags:
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment construire un panneau d'administration React avec Refine
seo_desc: 'React is a popular front-end framework for building interactive user interfaces.
  It has helped revolutionize the development of data-intensive front-end applications.

  React''s declarative nature makes building user interfaces intuitive. And reusable
  R...'
---

React est un framework front-end populaire pour construire des interfaces utilisateur interactives. Il a aidé à révolutionner le développement d'applications front-end intensives en données.

La nature déclarative de React rend la construction d'interfaces utilisateur intuitive. Et les composants React réutilisables augmentent la vitesse de développement et réduisent le temps de production.

Pour améliorer davantage l'expérience de développement lors de la construction d'interfaces utilisateur, plusieurs frameworks React ont émergé. L'un de ces frameworks est [refine](https://github.com/refinedev/refine).

refine est un framework basé sur React pour construire des applications web. Il est similaire à [React-admin](https://marmelab.com/react-admin/), [Redwood](https://redwoodjs.com/), et [Retool](https://retool.com/).

L'écosystème refine vient avec des intégrations prêtes à l'emploi pour l'authentification des utilisateurs, le routage, la mise en réseau, l'internalisation, et plus encore.

Dans cet article, vous apprendrez refine en construisant un simple panneau d'administration. Cela aidera à mettre en évidence les principaux blocs de construction du framework refine. Nous explorerons également les principales fonctionnalités et cas d'utilisation possibles de refine.

## Qu'est-ce que refine ?

refine est un framework React open-source, sous licence MIT, pour construire des applications front-end. Il est similaire à React-admin, Retool, et Redwood. refine est un framework React "headless". Il n'est pas opinionné sur vos choix de style et de design.

Cela signifie que vous pouvez utiliser refine avec un design personnalisé ou une bibliothèque de composants UI. Il est livré avec des intégrations pour les bibliothèques de composants et les systèmes de design les plus populaires, tels que Material UI, Chakra UI, et Ant Design.

refine dispose de fournisseurs de routage intégrés pour les bibliothèques de routage les plus populaires, telles que React Router, Remix Router, Next.js Router, et React Location. Vous pouvez choisir une bibliothèque de routage qui répond aux exigences de votre projet.

Vous pouvez utiliser refine pour construire des applications intensives en données telles que des panneaux d'administration, des tableaux de bord, des outils internes, et des vitrines. L'outil de ligne de commande, qui fait partie de l'écosystème React, peut vous aider à configurer rapidement une application refine.

Vous pouvez vous lancer rapidement si vous avez des connaissances de base à intermédiaires de React, puisque refine est un framework basé sur React. Vous pouvez également utiliser refine avec d'autres frameworks React comme Next et Remix.

## Prérequis – Outils de développement

Vous aurez besoin des outils suivants pour exécuter certains des exemples de cet article.

### L'environnement d'exécution Node

Si vous n'avez pas Node, téléchargez-le et installez-le depuis la page [Téléchargements Node](https://nodejs.org/en/download/). Après l'installation, exécutez la commande ci-dessous sur la ligne de commande pour vérifier si l'installation a réussi.

```sh
node -v
```

La commande ci-dessus affichera la version de Node sur votre machine si l'installation est réussie.

Les versions récentes de Node sont également livrées avec `npm`. Exécutez la commande ci-dessous sur le terminal pour vous assurer que vous avez `npm`. Elle devrait afficher la version de `npm` que vous avez installée avec Node.

```sh
npm -v
```

### Un éditeur de texte

Vous aurez besoin d'un éditeur de texte comme VS Code ou Sublime Text. Mon préféré est VS Code. Vous pouvez le télécharger depuis la page [Téléchargements VS Code](https://code.visualstudio.com/download). Alternativement, téléchargez Sublime Text pour votre système depuis la page [Téléchargements Sublime Text](https://www.sublimetext.com/download).

## Comment configurer une application refine

Vous pouvez configurer une application refine personnalisée ou utiliser l'utilitaire de ligne de commande refine pour démarrer rapidement une application refine. Si vous débutez, je vous recommande d'utiliser l'outil de ligne de commande refine pour une configuration de projet rapide.

L'outil de ligne de commande créera un projet refine avec toutes les configurations requises. Suivez les étapes ci-dessous pour créer un simple projet refine en utilisant l'outil de ligne de commande. Vous devez avoir les outils de développement que j'ai mis en évidence dans la section précédente pour suivre les étapes ci-dessous.

### Étape 1 – Créer une application refine

Naviguez vers le répertoire où vous souhaitez créer l'application refine et exécutez la commande ci-dessous sur la ligne de commande. J'utilise `npm` comme gestionnaire de paquets. Mais vous pouvez également utiliser un autre gestionnaire de paquets.

Notez également que si c'est la première fois que vous créez un projet refine, la commande ci-dessous vous demandera d'installer le paquet `create-refine-app`.

```sh
npm create refine-app@latest
```

La commande ci-dessus lancera le processus d'installation. Répondez aux prompts pendant l'installation. J'ai choisi le modèle de projet `refine-react`, l'intégration back-end RESTful, et Material UI comme framework UI pour ce projet.

Vous remarquerez que j'ai opté pour ne pas utiliser les autres configurations de mise en place.

```txt
✓ Downloaded remote source successfully.
✓ Choose a project template · refine-react
✓ What would you like to name your project?: · refine-demo
✓ Choose your backend service to connect: · data-provider-custom-json-rest
✓ Do you want to use a UI Framework?: · mui
✓ Do you want to add example pages?: · no
✓ Do you want to add dark mode support?: · no
✓ Do you want to customize the Material UI theme?: · no
✓ Do you want to customize the Material UI layout?: · no
✓ Do you need any Authentication logic?: · none
✓ Do you need i18n (Internationalization) support?: · no
✓ Do you want to add kbar command interface support?: · no
✓ Choose a package manager: · npm
✓ Would you mind sending us your choices so that we can improve superplate? · no
```

### Étape 2 – Ouvrir le projet dans un éditeur de texte

Une fois l'installation terminée, ouvrez le répertoire du projet dans un éditeur de texte. Si vous utilisez VS Code, utilisez la commande globale `code` avec le nom du répertoire du projet pour ouvrir le répertoire du projet dans VS Code.

La commande ci-dessous suppose que le nom de votre répertoire de projet est `refine-demo`.

```sh
code refine-demo
```

### Étape 3 – Lancer le serveur de développement

Vous pouvez démarrer le serveur de développement en exécutant la commande ci-dessous sur la ligne de commande.

```sh
npm run dev
```

La commande ci-dessus lancera le serveur de développement pour votre projet refine dans votre navigateur par défaut sur localhost, port 3000. La page d'accueil devrait ressembler à la capture d'écran ci-dessous :

![page d'accueil du modèle de projet refine](https://www.freecodecamp.org/news/content/images/2023/02/refine-project-template-landing-page.png align="left")

## Concepts principaux dans refine

Vous rencontrerez plusieurs concepts possiblement inconnus lorsque vous travaillerez avec refine. Voici les explications de certains de ces concepts courants que vous pourriez rencontrer.

### Fournisseurs de données

Plus souvent qu'autrement, vous devez communiquer avec une API lorsque vous construisez des applications front-end intensives en données avec React. Contrairement à React, refine abstrait les requêtes HTTP vers les API dans des fournisseurs de données.

Un fournisseur de données effectue des requêtes réseau vers une API et transmet la réponse au composant qui en a besoin.

L'écosystème refine dispose de fournisseurs de données pour les API REST, les API GraphQL, les bases de données cloud comme Firebase, et certains des systèmes de gestion de contenu headless populaires comme Strapi.

Vous pouvez déclarer un fournisseur de données personnalisé si vous ne prévoyez pas d'utiliser les fournisseurs de données de l'écosystème refine. Un fournisseur de données refine doit avoir la forme et les méthodes ci-dessous.

```ts
const dataProvider = {
    create: ({ resource, variables, metaData }) => Promise,
    createMany: ({ resource, variables, metaData }) => Promise,
    deleteOne: ({ resource, id, variables, metaData }) => Promise,
    deleteMany: ({ resource, ids, variables, metaData }) => Promise,
    getList: ({
        resource,
        pagination,
        hasPagination,
        sort,
        filters,
        metaData,
    }) => Promise,
    getMany: ({ resource, ids, metaData }) => Promise,
    getOne: ({ resource, id, metaData }) => Promise,
    update: ({ resource, id, variables, metaData }) => Promise,
    updateMany: ({ resource, ids, variables, metaData }) => Promise,
    custom: ({
        url,
        method,
        sort,
        filters,
        payload,
        query,
        headers,
        metaData,
    }) => Promise,
    getApiUrl: () => "",
};
```

Les noms des méthodes dans un fournisseur de données sont auto-explicatifs. La méthode `create` crée un élément dans une ressource comme son nom l'indique et retourne une promesse. Et elle prend plusieurs paramètres. Les autres noms de méthodes sont également auto-descriptifs.

Votre application refine interagit avec les fournisseurs de données via des hooks de données. Pour effectuer une opération CRUD, vous pouvez déclencher les méthodes dans votre fournisseur de données en utilisant des hooks de données.

### Hooks de données

Comme indiqué ci-dessus, vous pouvez déclencher l'une des méthodes du fournisseur de données depuis un composant en utilisant des hooks de données. Chaque méthode dans un fournisseur de données a un hook de données correspondant. Par exemple, le hook `useCreate` déclenche la méthode `create` dans votre fournisseur de données.

Vous pouvez utiliser le hook `useCreate` dans votre composant comme suit :

```ts
import { useCreate } from "@pankod/refine-core";

const MyComponent = () => {
  const { mutate } = useCreate();
  const clickHandler = () => {
    mutate({ resource: "posts", values: { title: "Refine hello world!" } });
  };
  return <button onClick={clickHandler}>Cliquez pour créer un élément</button>;
};
```

Bien que le hook `useCreate` retourne un objet avec plusieurs propriétés, nous nous intéressons à la fonction `mutate` dans l'exemple ci-dessus.

L'invocation de la fonction `mutate` comme nous l'avons fait déclenche la méthode `create` dans votre fournisseur de données. Après cela, la méthode `create` effectue une requête réseau vers votre API et transmet la réponse à votre composant.

Il existe plusieurs hooks de données que vous pouvez consulter dans la [documentation Refine](https://refine.dev/docs/).

### Ressources

Comme suggéré ci-dessus, travailler avec des API est inévitable lors de la construction d'applications front-end. L'API consiste généralement en des ressources auxquelles vous pouvez accéder via des endpoints et effectuer des opérations CRUD.

Le composant `Refine` est le point d'entrée pour toute application refine. Lorsque vous créez une application refine en utilisant `create-refine-app`, le composant `App.tsx` rendra toujours le composant `Refine` comme dans l'exemple ci-dessous.

```ts
function App() {
  return (
    <Refine
      dataProvider={dataProvider(apiUrl)}
      routerProvider={routerProvider}
      resources={[
        {
          name: "users",
          list: List,
          show: Show,
          create: Create,
          edit: Edit,
        },
      ]}
    />
  );
}
```

L'un des props que vous passez au composant `Refine` est le prop `resources`. La valeur du prop `resources` est un tableau d'objets de ressources. Chaque objet de ressource doit avoir une propriété `name`.

Comme dans l'exemple ci-dessus, vous pouvez passer des propriétés supplémentaires telles que `list`, `show`, `create`, et `edit`.

Les valeurs de `list`, `show`, `create`, et `edit` sont des composants. Dans l'exemple ci-dessus, la valeur du champ `name` est `"users"`.

Le champ `name` détermine les routes dans votre application front-end. Lorsque vous naviguez vers la route `/users` dans votre application, refine rendra le composant `List`.

De même, lorsque vous naviguez vers la route `/users/show`, refine rendra le composant `Show`. Le tableau ci-dessous résume la relation entre les champs de l'objet de ressource ci-dessus et les routes dans votre application.

| Propriété de l'objet de ressource | Route | Composant rendu |
| --- | --- | --- |
| `list` | `/users` | `List` |
| `show` | `/users/show` | `Show` |
| `create` | `/users/create` | `Create` |
| `edit` | `/users/edit` | `Edit` |

Au lieu de créer des composants à partir de zéro, vous pouvez également les générer en fonction de vos ressources en utilisant un [Inferencer](https://refine.dev/docs/api-reference/mui/components/inferencer/).

### Inferencer

[Inferencer](https://refine.dev/docs/api-reference/mui/components/inferencer/) est l'un des packages de l'écosystème de packages refine. Il augmente votre vitesse de développement en générant des pages CRUD après avoir analysé votre modèle de données. Vous pouvez ensuite personnaliser les composants auto-générés pour répondre aux exigences de votre projet.

Au lieu de définir les valeurs des propriétés de l'objet de ressource `list`, `show`, `create`, et `edit` à un composant personnalisé comme dans la sous-section précédente, l'Inferencer peut générer les composants pour vous. Vous pouvez ensuite personnaliser les composants selon vos besoins.

```ts
import { HeadlessInferencer } from "@pankod/refine-inferencer/headless";

function App() {
  return (
    <Refine
      dataProvider={dataProvider(apiUrl)}
      routerProvider={routerProvider}
      resources={[
        {
          name: "topics",
          list: HeadlessInferencer,
          show: HeadlessInferencer,
          create: HeadlessInferencer,
          edit: HeadlessInferencer,
        },
      ]}
    />
  );
}
```

Le code ci-dessus suppose que vous utilisez `HeadlessInferencer`. Vous pouvez également utiliser `MuiInferencer` si vous utilisez Material UI.

L'Inferencer repose sur les packages `@pankod/refine-react-hook-form` et `@pankod/refine-react-table` en interne pour générer des formulaires et des tableaux. Assurez-vous donc de les installer.

```sh
npm i @pankod/refine-react-table @pankod/refine-react-hook-form
```

## Comment construire un panneau d'administration avec refine

Dans cette section, vous allez construire un simple panneau d'administration en modifiant l'application refine que vous avez créée ci-dessus.

Rappelez-vous, nous avons choisi l'intégration back-end de l'API RESTful lors du démarrage de l'application en utilisant `create-refine-app`. Nous allons donc utiliser une [fausse API RESTful](https://api.fake-rest.refine.dev/) pour cette illustration.

Dans une application réelle, vous travaillerez avec une intégration back-end différente. Cela peut être une API RESTful, une API GraphQL, des bases de données cloud comme Firebase, ou un système de gestion de contenu comme Strapi.

Vous devez lire la [documentation refine](https://refine.dev/docs/) sur l'utilisation des différentes intégrations back-end disponibles dans l'écosystème refine.

La fausse API RESTful dispose de plusieurs endpoints pour accéder aux ressources disponibles. Nous allons construire un panneau d'administration pour la ressource [users](https://api.fake-rest.refine.dev/users). Suivez les étapes ci-dessous si vous avez ouvert le projet refine que nous avons créé au début de cet article dans un éditeur de texte.

### Étape 1 – Installer les dépendances de l'Inferencer

Nous allons utiliser `MuiInferencer` pour générer des pages CRUD. L'Inferencer repose sur les packages `@pankod/refine-react-hook-form` et `@pankod/refine-react-table` en interne. Exécutez la commande ci-dessous sur le terminal pour les installer.

```sh
npm i @pankod/refine-react-table @pankod/refine-react-hook-form
```

### Étape 2 – Importer `MuiInferencer`

Après avoir installé avec succès les dépendances requises, ouvrez le fichier `src/App.tsx` et ajoutez l'instruction d'importation suivante en haut :

```ts
import { MuiInferencer } from "@pankod/refine-inferencer/mui";
```

### Étape 3 – Générer des composants en utilisant l'Inferencer

Comme expliqué dans la section "Concepts principaux", les valeurs des propriétés `list`, `show`, `create`, et `edit` de l'objet `resource` sont des composants. Vous pouvez créer ces composants à partir de zéro ou les générer en utilisant l'Inferencer. Dans cet exemple, nous allons utiliser `MuiInferencer` pour les créer.

Dans le fichier `src/App.tsx`, le composant `App` rend le composant intégré `Refine`. `Refine` est le point d'entrée pour toute application refine. Ajoutez la prop `resources` à votre composant `Refine` afin que le composant `App` ressemble à ceci :

```ts
function App() {
  return (
    <ThemeProvider theme={LightTheme}>
      <CssBaseline />
      <GlobalStyles styles={{ html: { WebkitFontSmoothing: "auto" } }} />
      <RefineSnackbarProvider>
        <Refine
          dataProvider={dataProvider("https://api.fake-rest.refine.dev")}
          notificationProvider={notificationProvider}
          Layout={Layout}
          ReadyPage={ReadyPage}
          catchAll={<ErrorComponent />}
          routerProvider={routerProvider}
          resources = {[
            {
              name: 'users',
              list: MuiInferencer,
              show: MuiInferencer,
              create: MuiInferencer,
              edit: MuiInferencer

            }
          ]}
        />
      </RefineSnackbarProvider>
    </ThemeProvider>
  );
}
}
```

### Étape 4 – Prévisualiser les changements

#### Voir la liste des utilisateurs

Après avoir sauvegardé les changements ci-dessus, refine générera les pages CRUD et redirigera vers la route `/users`. Votre page d'accueil devrait ressembler à l'image ci-dessous. Le composant généré par l'Inferencer rend un tableau d'utilisateurs à partir de la ressource `users`.

Le tableau a plusieurs colonnes, dont certaines sont masquées si vous utilisez un petit écran. Faites défiler horizontalement pour les voir toutes.

![page de liste des utilisateurs](https://www.freecodecamp.org/news/content/images/2023/02/users-list-page.png align="left")

#### Créer un nouvel utilisateur

Vous pouvez également naviguer vers la route `users/create` pour créer un nouvel utilisateur en cliquant sur le bouton "CRÉER". refine rendra le composant généré par l'Inferencer. Il a un formulaire qui ressemble à l'image ci-dessous pour créer un nouvel utilisateur.

![page de création d'un nouvel utilisateur](https://www.freecodecamp.org/news/content/images/2023/02/create-new-user-page.png align="left")

#### Mettre à jour un utilisateur existant

Pour mettre à jour une ressource existante, naviguez vers la route `/users/edit/:id`. Le paramètre de route `id` doit être l'`id` d'un objet dans la ressource `users`.

Pour modifier les détails de l'utilisateur dont l'`id` est 1, naviguez vers l'endpoint `/users/edit/1` en cliquant sur le bouton de modification du premier enregistrement dans le tableau des utilisateurs.

Le bouton de modification se trouve sous la dernière colonne intitulée "Actions". La page de modification devrait ressembler à l'image ci-dessous.

![page de mise à jour d'un utilisateur existant](https://www.freecodecamp.org/news/content/images/2023/02/edit-an-existing-user-page.png align="left")

#### Voir un utilisateur spécifique

Pour voir les détails d'un utilisateur avec un `id` spécifique, naviguez vers la route `/users/show/:id`. L'`id` doit être celui d'un objet existant dans la ressource `users`.

Pour voir les détails du premier utilisateur, cliquez sur le bouton d'affichage du premier enregistrement dans le tableau des utilisateurs. Le bouton d'affichage se trouve sous la dernière colonne intitulée "Actions".

Lorsque vous naviguez vers l'endpoint `/users/show/1`, vous devriez voir les détails du premier utilisateur dont l'`id` est 1.

![page de visualisation d'un utilisateur](https://www.freecodecamp.org/news/content/images/2023/02/show-user-page.png align="left")

### Étape 5 – Voir le code généré par l'Inferencer

L'Inferencer a créé des composants pour nous en utilisant la réponse de l'endpoint `/users` de notre fausse API RESTful. Dans chacune des pages que vous avez visitées ci-dessus, il y a un bouton en bas à droite avec l'étiquette "AFFICHER LE CODE".

Cliquez dessus pour afficher le code généré par l'Inferencer pour chaque page.

![voir le code généré par l'Inferencer](https://www.freecodecamp.org/news/content/images/2023/02/view-generated-code.png align="left")

### Étape 6 – Personnaliser les composants générés

Dans les étapes précédentes, vous avez généré des pages CRUD en utilisant `MuiInferencer`. L'utilisation de `MuiInferencer` vous permettra de démarrer en générant le code de base. Mais dans une application réelle, vous souhaitez presque toujours personnaliser les composants pour répondre à vos besoins.

Pour personnaliser le code généré, créez un répertoire `src/users`. Dans le répertoire `src/users`, créez quatre fichiers avec les noms suivants. Vous pouvez les nommer différemment si vous le souhaitez.

* `List.tsx`
    
* `Create.tsx`
    
* `Edit.tsx`
    
* `Show.tsx`
    

Dans l'étape précédente, vous avez appris comment voir le code généré pour chaque page.

Copiez et collez le code de la page `/users` dans le fichier `List.tsx` que vous avez créé. De la même manière, copiez et collez le code de la page `/users/create` dans le fichier `Create.tsx`. Vous faites de même pour les autres pages et leurs composants correspondants.

Importez les composants que vous avez créés ci-dessus dans votre `App.tsx` comme suit :

```ts
import { UserList } from "users/List";
import { UserCreate } from "users/Create";
import { UserShow  } from "users/Show";
import { UserEdit } from "users/Edit";
```

Dans le fichier `App.tsx`, le composant `App` rend le composant intégré `Refine`. Modifiez la prop `resources` que vous passez au composant `Refine` pour qu'elle ressemble à ceci :

```ts
<Refine
  ...
  resources={[
    {
      name: "users",
      list: UserList,
      show: UserShow,
      create: UserCreate,
      edit: UserEdit,
    },
  ]}
/>;
```

Espérons que vous avez remarqué comment les valeurs des propriétés `list`, `show`, `create`, et `edit` de l'objet de ressource ont changé de `MuiInferencer` à `UserList`, `UserShow`, `UserCreate`, et `UserEdit`, respectivement. Vous pouvez maintenant modifier le code dans les composants que vous avez créés.

C'est à peu près aussi facile que cela de créer des tableaux de bord et des panneaux d'administration avec refine.

En quelques minutes, vous avez démarré un modèle de projet basé sur votre modèle de données. Vous pouvez ensuite le personnaliser davantage. Démarrer un tel projet à partir de zéro nécessiterait beaucoup de travail.

## Conclusion

refine est un framework React open-source sous licence MIT pour construire des applications front-end. Il est utile lors de la construction de tableaux de bord, de panneaux d'administration, d'outils internes et de vitrines. Vous pouvez l'utiliser dans presque toutes les applications qui utilisent React.

refine vient avec des fonctionnalités prêtes à l'emploi pour la mise en réseau, l'authentification, le routage et l'internationalisation. Il dispose également d'intégrations pour les bases de données cloud les plus populaires, telles que Firebase et Supabase, et les systèmes de gestion de contenu, comme Strapi.

Si vous cherchez à commencer à utiliser refine, utilisez l'outil de ligne de commande. Avec l'outil de ligne de commande, vous pouvez choisir une configuration headless ou utiliser l'un des systèmes de composants ou de design intégrés tels que Material UI et Ant Design.

Espérons que cet article vous a introduit aux bases de refine. refine a plusieurs autres fonctionnalités et cas d'utilisation que je n'ai pas mis en évidence ici. Consultez la [documentation](https://refine.dev/docs/) pour comprendre pleinement refine et ses capacités.

## Lectures complémentaires

* [Documentation Refine](https://refine.dev/docs/)
    
* [Dépôt GitHub du projet Refine](https://github.com/refinedev)