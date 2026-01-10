---
title: Comment créer une application TodoMVC avec React et l'API GraphQL de 8base
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-22T20:47:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-todomvc-app-with-react-and-8base-graphql-api-ea858952731b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2O1B3d5Pda95Isjc8OUN_w.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer une application TodoMVC avec React et l'API GraphQL de 8base
seo_desc: 'By Andrei Anisimov

  Requirements


  git

  npm or yarn (we use yarn here, but you can use npm if you prefer)

  Familiarity with React.js


  Introduction

  In this tutorial I’ll show you how to quickly create a GraphQL API using 8base and
  connect to it from a Rea...'
---

Par Andrei Anisimov

### Prérequis

* [git](https://git-scm.com/downloads)
* [npm](https://www.npmjs.com/get-npm) ou [yarn](https://yarnpkg.com/lang/en/docs/install/#mac-stable) (nous utilisons `yarn` ici, mais vous pouvez utiliser `npm` si vous préférez)
* Connaissance de [React.js](https://reactjs.org/)

### Introduction

Dans ce tutoriel, je vais vous montrer comment créer rapidement une API GraphQL en utilisant [8base](https://www.8base.com/?utm_source=freecodecamp&utm_campaign=todomvc) et comment s'y connecter depuis une application React. 8base est une plateforme d'accélération pour les développeurs offrant une multitude de fonctionnalités pour aider les développeurs front-end à construire des applications plus rapidement et plus simplement que jamais. Avec 8base, il n'est plus nécessaire de dépendre des développeurs back-end ou des DevOps !

En utilisant la plateforme 8base, vous pouvez construire votre backend GraphQL en utilisant une interface graphique simple qui vous permet d'effectuer des actions telles que :

* Définir votre schéma de données : créer des tables/relations entre tables
* Télécharger des fichiers
* Définir des rôles
* Gérer divers projets en utilisant les "Workspaces"
* Concevoir des requêtes et mutations GraphQL en utilisant l'explorateur d'API

Je pense que la meilleure façon d'illustrer l'utilité de GraphQL est de montrer aux développeurs intéressés comment il peut être intégré dans des projets sur lesquels ils travaillent déjà. En connectant une simple application Todo MVC à un backend GraphQL, nous apprendrons comment :

* Définir des tables de données dans 8base pour créer une API GraphQL
* Écrire des requêtes en utilisant GraphQL
* Accéder à vos données depuis un front-end React.js

### Public visé

Ce tutoriel s'adresse principalement aux utilisateurs qui n'ont pas beaucoup d'expérience préalable avec GraphQL. Si vous êtes familier avec GraphQL, la connexion à votre backend 8base devrait être un processus quelque peu familier. Nous vous encourageons à suivre ce tutoriel et à voir comment une application React statique prend vie en la connectant à une API GraphQL dynamique.

### Préparation de l'environnement/Interface utilisateur de 8base

Dans ce tutoriel, nous n'utiliserons que quelques fonctionnalités offertes par 8base, mais je vous encourage vivement à explorer l'intégralité de la plateforme et à utiliser d'autres outils de la suite.

1. **Créez un compte** sur [8base](https://www.8base.com/?utm_source=freecodecamp&utm_campaign=todomvc) *(C'est gratuit pour les petites équipes. Vous serez invité à vérifier votre email et ensuite redirigé vers l'interface utilisateur de 8base)._
2. Une fois dans l'interface utilisateur de 8base, naviguez simplement vers "Data" et cliquez sur "New Table" pour commencer à construire votre backend. Après que votre nouvelle table soit chargée, vous serez redirigé vers le Schéma afin de commencer à définir les champs. Jetons un coup d'œil et notons quelques choses. À gauche, vous verrez qu'il y a des `System Tables` et `Your Tables`. Chaque nouvel espace de travail 8base est automatiquement préemballé avec un certain nombre de tables intégrées. Ces tables sont utilisées pour gérer des choses comme les fichiers, les paramètres et les permissions et peuvent toutes être accessibles via l'API GraphQL de 8base. Pour l'instant, la seule table système exposée via l'interface utilisateur est Users, mais vous pouvez trouver une liste complète des tables système de 8base en utilisant la requête `tablesList` dans l'`API Explorer`.
3. Allez-y et **créez une table** `Todo` avec les champs `text` (type de champ : TEXT), `completed` (type de champ : SWITCH, format : Oui/Non). *Switch est un type de champ particulièrement intéressant. Au premier abord, il peut sembler être une valeur booléenne, mais le champ switch est en réalité capable de gérer plusieurs options, et permet donc une grande flexibilité. Cependant, pour les besoins de ce projet, nous utiliserons simplement Oui/Non.*
4. Ensuite, **copiez l'URL de l'endpoint de l'API** (disponible en bas à gauche) — c'est votre principale ligne de communication entre votre front-end et votre backend 8base (vous en aurez besoin plus tard où il est indiqué `8BASE_API_URL`).
5. Enfin, pour les besoins de ce tutoriel, nous allons **autoriser l'accès ouvert aux invités** par défaut afin que la gestion de l'authentification soit optionnelle. Pour autoriser l'accès invité à votre nouvelle table Todo, naviguez vers Settings > Roles > Guest et cochez les cases appropriées sous _Todo. Tous les utilisateurs non authentifiés qui accèdent à votre endpoint API se voient attribuer le rôle de Guest par défaut. L'authentification n'est pas couverte dans ce tutoriel. Vous pouvez voir comment l'authentification doit être gérée en plus de [détail](https://docs.8base.com/docs/authentication) ici._

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kd0z58jTVcR2oyT-BBiNIQ.png)
_Assurez-vous que vos permissions d'invité pour Todos correspondent à celles ci-dessus_

Maintenant que vous avez préparé votre backend, dirigeons-nous vers le [dépôt TodoMVC de 8base](https://github.com/8base-examples/todomvc) pour préparer notre application cliente.

* Clonez le dépôt TodoMVC et exécutez `git checkout workshop` pour passer à la branche `workshop`.

*La branche master contient le code terminé pour ce projet, vous ne pourrez donc pas suivre le tutoriel si vous ne complétez pas cette étape.*

* Installez les dépendances :

`yarn add @8base/app-provider graphql graphql-tag react-apollo && yarn`

* Testez que l'application fonctionne sans backend : `yarn start`

![Image](https://cdn-media-1.freecodecamp.org/images/1*qvTFzoUgTA-anWaPb9cqPA.png)

* (Facultatif) Configurez l'extension VS Code [Apollo GraphQL](https://marketplace.visualstudio.com/items?itemName=apollographql.vscode-apollo) : Créez le fichier `apollo.config.js` à la racine du projet avec le contenu suivant (remplacez `8BASE_API_URL` par votre URL d'endpoint API) :

```
module.exports = {  client: {    service: {      name: '8base',      url: '8BASE_API_URL',    },    includes: [      "src/*.{ts,tsx,js,jsx}"    ]  },};
```

*L'extension Apollo GraphQL pour VS Code fournit une validation et une complétion automatique pour l'écriture de requêtes GraphQL.*

### Connexion du Backend

Le dépôt de l'application que nous avons configuré contient le code suivant intégré, afin que vous puissiez vous concentrer sur la compréhension de ce qui se passe. Dans les cas où vous devez ajouter du code, il suffit de décommenter ce qui est spécifié. Dans les cas où le code doit être supprimé, le code spécifié est suivi du commentaire `//Remove this` dans la base de code.

*Notez que tout le code pertinent de ce tutoriel sera placé dans le fichier src/App.js — ce n'est pas une bonne pratique avec React mais cela a été fait de cette manière pour simplifier le tutoriel.*

1. **Importer les dépendances liées à GraphQL**

Vous verrez ici que nous n'importons pas seulement `gql` et `graphql`, mais nous importons également `EightBaseAppProvider` depuis le SDK de 8base. Le SDK de 8base simplifie l'intégration avec 8base et GraphQL. Nous avons fait cela en prenant beaucoup de code boilerplate/setup et en l'emballant à l'intérieur du SDK, afin que le développeur n'ait qu'à envelopper son application dans la balise `<EightBaseAppProvider>` et lui passer les props appropriées pour permettre l'accès aux données à tous les composants enfants. EightBaseAppProvider [utilise Apollo](https://www.apollographql.com/docs/react/) Client, donc si vous êtes déjà familier avec celui-ci, il n'y a rien de nouveau à apprendre.

**2. Initialiser `EightBaseAppProvider`**

Vous devez fournir une fonction en tant qu'enfant de EightBaseAppProvider qui indiquera à React ce que nous voulons rendre. Nous pouvons utiliser la propriété `loading` pour afficher un chargeur pendant que l'application est initialisée. Pendant l'initialisation, EightBaseAppProvider charge le schéma des tables 8base qui vous donne accès à toutes les propriétés du modèle de données dans votre code front-end. Nous aborderons cette fonctionnalité plus en détail dans un futur tutoriel.

**3. Ajouter une requête pour récupérer les todos**

* Requête et HOC

Dans le code ci-dessus, nous créons un [Higher-Order Component](https://reactjs.org/docs/higher-order-components.html) (HOC) en utilisant la fonction `graphql()` fournie par [react-apollo](https://www.apollographql.com/docs/react/).

> *De [react-apollo](https://www.apollographql.com/docs/react/api/react-apollo.html#graphql) — La fonction graphql() est la chose la plus importante exportée par react-apollo. Avec cette fonction, vous pouvez créer des composants d'ordre supérieur qui peuvent exécuter des requêtes et se mettre à jour de manière réactive en fonction des données dans votre magasin Apollo. La fonction graphql() retourne une fonction qui « améliorera » tout composant avec des capacités GraphQL réactives. Cela suit le modèle de composant d'ordre supérieur de React qui est également utilisé par la fonction `connect` de react-redux.*

Essentiellement, en utilisant `graphql()`, nous sommes capables d'écrire le code pour interroger notre backend en un seul endroit et d'injecter cette fonctionnalité dans plusieurs composants plutôt que de l'écrire partout où nous voulons pouvoir l'utiliser.

La fonction `graphql` prend une requête comme premier paramètre, la configuration comme second, et la valeur de retour est un HOC qui doit être exécuté avec le composant souhaité comme argument. Notez que dans notre exemple, nous utilisons le paramètre de configuration dans `graphql()` pour spécifier que nos données seront accessibles en tant que `props.todos` plutôt que `props.data.todosList.items`.

En ce qui concerne notre `TODO_LIST_QUERY`, nous vous avons déjà donné la syntaxe appropriée, mais typiquement nous pourrions concevoir nos requêtes dans l'_8base API Explorer_. Si vous naviguez vers l'API Explorer et copiez/collez la `TODO_LIST_QUERY`, vous pouvez voir quelles données seront retournées. Expérimentez avec cette requête et voyez d'autres façons dont les données peuvent être retournées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WtuMwVMPyfXCgubcEw2c4Q.png)
_8base API Explorer_

* Enveloppez `Main` et `Footer` dans `withTodos`

En fin de compte, dans notre exemple, nous voulons afficher toutes les données de notre backend 8base dans le composant Main et le composant Footer. Dans le code ci-dessus, nous utilisons la fonction `compose()` fournie par la bibliothèque lodash pour enchaîner plusieurs Higher-Order Components ensemble, donnant à nos composants cibles la fonctionnalité de chaque HOC. Vous pouvez en savoir plus sur le fonctionnement de la fonction `compose()` [ici](https://redux.js.org/api/compose).

* Supprimez le code qui passe la prop `todos` aux composants `Main` et `Footer`

Lorsque nous avons configuré notre application pour la première fois, tous les Todos étaient conservés dans l'état car nous n'étions pas connectés à un backend. Nos composants ont toujours besoin d'accéder aux props todos, mais nous n'avons plus à les passer explicitement car ils sont fournis par `withTodos`.

**4. Ajouter une requête pour créer un todo**

Ici, nous répétons le processus que nous avons pris précédemment pour interroger notre backend 8base. Mais cette fois, nous utilisons la mutation GraphQL pour créer un Todo, puis nous appelons `refetchQueries` pour mettre à jour l'état de notre application avec nos données nouvellement ajoutées. Cela permettra aux nouvelles données de se propager dans toute l'application sans avoir à faire une requête séparée à notre backend.

* Enveloppez `Header`

La syntaxe ci-dessus illustre l'amélioration du composant Header en utilisant notre HOC. Notez que withCreateTodo agit comme une fonction, le composant `Header` est passé à la fonction comme argument et le composant amélioré est ensuite défini à la variable `Header` pour être utilisé dans notre application.

* Supprimez `createTodo` de `Header`

**5. Ajouter une requête pour mettre à jour les todos**

* Mutation et HOC

* Enveloppez `Main` dans `withToggleTodo`

* Supprimez `toggleTodo` de `Main`

Ci-dessus, nous avons répété le schéma précédent pour ajouter une fonctionnalité au composant `Main`. Cela donnera à l'utilisateur la possibilité de basculer les Todos comme complets ou incomplets.

**6. Ajouter une requête pour marquer tous les todos comme complets**

* Nous avons seulement besoin d'un nouveau HOC, nous pouvons réutiliser la mutation. Toutes les mutations dans la boucle seront regroupées en une seule requête.

* Enveloppez `Main` dans `withToggleAllTodos`

* Supprimez `toggleAllTodos` de `Main`

**7. Ajouter une requête pour supprimer les todos**

* Mutation et HOC

* Enveloppez `Main` dans `withRemoveTodo`

* Supprimez `removeTodo` de `Main`

Comme vous pouvez le voir, une fois que vous comprenez le schéma de base de l'amélioration des composants en utilisant le HOC graphql(), il devient assez simple d'écrire de nouvelles requêtes qui peuvent être facilement accessibles dans toute votre application.

Enfin, testez que votre application fonctionne correctement en naviguant vers le répertoire racine et en exécutant `yarn start`.

Vous devriez maintenant être en mesure de créer, mettre à jour et supprimer des Todos qui sont persistés dans la base de données.

* Pour voir 8base en action, ouvrez votre espace de travail 8base dans un onglet séparé et ouvrez le _Data Viewer_ sur la table Todos. Vous devriez voir toutes les données de votre application dans cette fenêtre. Créez de nouveaux Todos dans votre application et actualisez la page pour les voir dans votre base de données !

![Image](https://cdn-media-1.freecodecamp.org/images/1*kYA02Tq9ob9pIkD8cdA43w.png)
_8base Data Viewer_

8base travaille actuellement sur des implémentations utilisant d'autres frameworks et bibliothèques. Nous avons actuellement des exemples utilisant [React](https://github.com/8base/app-example) et [React-Native](https://github.com/8base/react-native-app-example) ainsi que des exemples plus [simples](https://docs.8base.com/docs/connecting-to-your-frontend) utilisant CURL, Node et Vanilla JS. N'hésitez pas à visiter notre [Docs](https://docs.8base.com/), envoyer un message sur notre [site web](https://8base.com/?utm_source=freecodecamp&utm_campaign=todomvc), ou me contacter personnellement pour des retours sur votre expérience avec 8base.

Un exemple complet avec le backend 8base connecté peut être trouvé dans la branche [master](https://github.com/8base/todomvc).

Pour commencer avec 8base ou simplement obtenir plus d'informations, visitez [**www.8base.com**](https://www.8base.com/?utm_source=freecodecamp&utm_campaign=todomvc), [**docs.8base.com**](https://docs.8base.com/?utm_source=freecodecamp&utm_campaign=todomvc), suivez-nous sur Twitter à **@[8baseinc](https://twitter.com/8baseinc)**, ou envoyez-nous un email directement à **_info@8base.com_**_._

*Originalement publié sur [blog.8base.com](https://blog.8base.com/tutorial-building-todomvc-with-8base-and-graphql-34a33357b784) le 22 février 2019.*