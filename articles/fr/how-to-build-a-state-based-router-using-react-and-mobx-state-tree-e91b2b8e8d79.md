---
title: Comment créer un routeur basé sur l'état avec React et MobX State Tree
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-03T17:31:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-state-based-router-using-react-and-mobx-state-tree-e91b2b8e8d79
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IIwgT670HJ7Ni-_UDA3-Ow.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: routing
  slug: routing
- name: 'tech '
  slug: tech
seo_title: Comment créer un routeur basé sur l'état avec React et MobX State Tree
seo_desc: 'By Miles Till

  Introducing mobx-state-tree-router


  _Image by [Flickr](https://www.flickr.com/photos/medithit/" rel="noopener" target="_blank"
  title="">medithIT on <a href="https://www.flickr.com/photos/medithit/10363854753/"
  rel="noopener" target="bla...'
---

Par Miles Till

**Présentation de [mobx-state-tree-router](https://github.com/miles-till/mobx-state-tree-router)**

![Image](https://cdn-media-1.freecodecamp.org/images/q2nzV7mcMyhC5USDlGtwtCaFCkdhdaj93Q48)
_Image par [Flickr](https://www.flickr.com/photos/medithit/" rel="noopener" target="_blank" title="">medithIT</a> sur <a href="https://www.flickr.com/photos/medithit/10363854753/" rel="noopener" target="_blank" title=")_

*Si vous souhaitez passer directement à l'exemple final, vous pouvez le consulter sur [mobx-state-tree-router-demo](https://github.com/miles-till/mobx-state-tree-router-demo).*

J'ai écrit une bibliothèque qui facilite la configuration du routage basé sur l'état dans les applications React alimentées par MobX State Tree, et je souhaite la partager avec vous. Pour cela, je vais démontrer comment créer une application Todo très simple.

[Michel Weststrate](https://www.freecodecamp.org/news/how-to-build-a-state-based-router-using-react-and-mobx-state-tree-e91b2b8e8d79/undefined), le créateur de MobX, a écrit un excellent article intitulé [Comment découpler l'état et l'UI (a.k.a. vous n'avez pas besoin de componentWillMount)](https://hackernoon.com/how-to-decouple-state-and-ui-a-k-a-you-dont-need-componentwillmount-cc90b787aa37). Je vous recommande de le lire pour comprendre la philosophie qui m'a inspiré à écrire mobx-state-tree-router. L'idée clé est que l'UI de l'application doit être une fonction de l'état.

> « Cette approche offre un meilleur découplage de l'état et de l'UI. Cela présente quelques avantages :

> 1. Le flux complet de l'application peut être testé sans jamais avoir besoin d'instancier un composant.

> 2. Plus de composants peuvent être "bêtes" ; ils n'ont pas besoin de récupérer des données ou de traiter le routage.

> 3. Nos stores deviennent plus comme une machine à états, ce qui facilite le suivi des transitions de notre application. »

> - Michel Weststrate

### Prérequis

Ces éléments devront être installés pour suivre ce tutoriel :

* [Node.js](https://nodejs.org/en/) — utilisé pour exécuter le serveur de développement
* [Yarn](https://yarnpkg.com/en/) — utilisé pour la gestion des paquets

*Note : NPM peut être utilisé à la place de Yarn, mais certaines commandes peuvent être différentes.*

### Créer une application React de base

#### Utiliser create-react-app pour démarrer rapidement

Si vous ne l'avez pas encore utilisé, le moyen le plus simple de démarrer avec une application React est d'utiliser un outil de scaffolding développé par les créateurs de React appelé [Create React App](https://github.com/facebook/create-react-app). Cet outil configure [Webpack](https://webpack.js.org/) et [Babel](https://babeljs.io/) pour vous avec les exigences les plus courantes.

Dans votre terminal, exécutez les commandes suivantes :

```
npx create-react-app state-router-democd state-router-demoyarn start
```

Vous disposez maintenant d'une application React de base entièrement fonctionnelle à explorer.

#### Supprimer les éléments non nécessaires de create-react-app pour cet exemple

Pour les besoins de ce tutoriel, nous n'avons pas besoin de beaucoup d'éléments générés par create-react-app, alors supprimez les fichiers suivants :

```
src/App.csssrc/App.test.jssrc/index.csssrc/logo.svgsrc/serviceWorker.js
```

*Note : N'hésitez pas à conserver les fichiers CSS et à ajouter votre propre style.*

Pour garder les choses organisées, créez un répertoire `components` dans notre `src` et déplacez `src/App.js` vers `src/components/App.js`.

Mettez maintenant à jour les fichiers suivants pour supprimer les références aux fichiers que nous avons supprimés :

**src/components/App.js**

**src/index.js**

Si vous avez toujours l'application en cours d'exécution, vous remarquerez que votre navigateur a été mis à jour pour afficher ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/HmmOo0FbypGJUW0fxqIAjxU-Vpv3ApchARCJ)

#### Créer un composant de page d'accueil

Dans le répertoire `components`, créez un fichier pour notre composant de page d'accueil :

**src/components/Home.js**

Mettez à jour le composant App pour rendre notre nouveau composant de page d'accueil :

**src/components/App.js**

![Image](https://cdn-media-1.freecodecamp.org/images/NCx1sB4ZwpZrNUG4giyv6GWhjB1VQSf5cMMZ)

### Ajouter des modèles MobX State Tree

#### Installer MobX et MobX State Tree

[MobX](https://github.com/mobxjs/mobx) est une bibliothèque de gestion d'état, et elle fonctionne très bien avec React comme moteur de rendu. [MobX State Tree](https://github.com/mobxjs/mobx-state-tree) est un conteneur d'état en forme d'arbre construit sur MobX.

Dans votre terminal, exécutez :

```
yarn add mobx mobx-react mobx-state-tree
```

Comme nous l'avons fait pour nos composants, créez un répertoire `models` pour garder nos modèles MobX State Tree organisés.

#### Créer un modèle RootStore

Dans notre arbre d'état, nous aurons un `RootStore` qui contient nos stores de données (dans ce cas, un `TodoStore`) et notre `RouterStore`, mais nous y viendrons plus tard.

**src/models/RootStore.js**

#### Créer des modèles TodoStore et Todo

Notre `TodoStore` contient des objets `Todo` qui peuvent être créés, supprimés et mis à jour. Nous devons également pouvoir trouver un objet `Todo` par son `id`.

**src/models/TodoStore.js**

#### Initialiser le RootStore

Lorsque notre application se charge, nous voulons initialiser le `RootStore` avec un état connu. Pour cet exemple trivial, nous ne nous préoccuperons pas de persister nos données dans un stockage quelconque. Nous voulons ensuite nous assurer que le `RootStore` est disponible pour être injecté dans nos composants, nous utilisons donc le composant MobX React `Provider` pour cela.

**src/index.js**

#### Créer un composant de page TodoList

Maintenant que nous avons un `RootStore` pour notre arbre d'état, nous avons besoin de composants pour visualiser et modifier les données.

**src/components/TodoList.js**

Mettez à jour le composant `App` pour afficher notre nouveau composant `TodoList`.

**src/components/App.js**

À ce stade, l'application devrait avoir une liste d'objets `Todo` que vous pouvez ajouter et supprimer.

![Image](https://cdn-media-1.freecodecamp.org/images/R2JwZQj-xFt2LdACX-zYQHZtZVNtujhZn5Oj)

#### Créer un composant de page Todo

Nous voulons maintenant créer un nouveau composant pour afficher et éditer un objet `Todo`. Notez que nous utilisons `inject` pour rendre le `RootStore` disponible dans les props du composant.

**src/components/Todo.js**

Mettez à jour le composant `App` pour afficher notre nouveau composant `Todo`.

Notre application mise à jour nous permet maintenant de modifier les données du `Todo` dont l'id est passé au composant de page Todo dans `<Todo todoId={0}` />.

![Image](https://cdn-media-1.freecodecamp.org/images/NMq1Crdl8b1XeXy-3L95whd2bp7j1VV7LnoN)

### Ajouter un routage basé sur l'état

À ce stade, nous devrions avoir une application React avec nos données stockées dans un conteneur MobX State Tree. Le conteneur de données est ensuite injecté dans les composants qui ont besoin d'accéder aux données. Maintenant, nous voulons connecter ensemble nos composants de page dans notre application. Une approche courante serait d'utiliser un routeur basé sur les composants tel que [React Router](https://github.com/ReactTraining/react-router). Souvent, les composants deviennent encombrés de définitions de routes et de gestionnaires d'événements de montage. Cela ne convient pas à notre philosophie "state-first".

Je vais maintenant vous montrer comment ajouter mobx-state-tree-router à votre application.

#### Installer mobx-state-tree-router

Dans votre terminal, exécutez :

```
yarn add mobx-state-tree-router
```

#### Ajouter le routeur au RootStore

**src/models/RootStore.js**

#### Créer des vues

Le routeur doit être configuré avec une carte de modèles de vue qui définissent les chemins de route à correspondre et les composants de page à afficher. Des hooks dans le cycle de changement de page peuvent être définis sur une vue pour effectuer la récupération de données, l'annulation de changement de route, la redirection et d'autres tâches. Ces hooks peuvent être synchrones ou asynchrones.

Ces hooks sont :

* `beforeExit(self, params)`
* `beforeEnter(self, params)`
* `onExit(self, params)`
* `onEnter(self, params)`

Si l'un des hooks "before" retourne `false`, le changement de route sera annulé.

Créez un fichier `views` :

**src/views.js**

#### Initialiser le routeur lorsque notre application démarre

Le routeur peut être démarré en appelant `startRouter(router)`. Cette fonction connecte le routeur à l'historique du navigateur et configure le routage en fonction des vues du routeur.

**src/index.js**

#### Rendre le StateRouter

Mettez à jour le composant `App` pour inclure le composant `StateRouter`, qui rend le composant approprié pour la vue actuelle du routeur.

**src/components/App.js**

Maintenant, notre application répondra aux changements dans le chemin de l'URL, par exemple `/todos` affichera notre composant `TodoList` et `/todos/0` affichera notre composant `Todo` comme configuré dans `views.js`.

![Image](https://cdn-media-1.freecodecamp.org/images/OAPfHYOwTqQ494DZyUiiC3th5XHaP8ffaC9w)

![Image](https://cdn-media-1.freecodecamp.org/images/K3rVKI18B-2Belhpaqe2B1r4EoMMHEFFx5pG)

#### Ajouter des liens de navigation

Actuellement, notre application n'a aucun moyen de naviguer autre que de changer l'URL directement. Cela ne fonctionne pas particulièrement bien dans cet exemple simple car les données dans notre `RootStore` seront réinitialisées à l'état initial tel que défini dans `index.js` à chaque fois que la page se charge.

Il existe 2 autres façons de changer la route en utilisant mobx-state-tree-router :

* Composants `Link`
* Appeler directement `router.setView(view, params)`

Je recommande d'utiliser les composants `Link` lorsque cela est possible, mais dans certains cas (comme les redirections), la définition directe de la vue peut être inévitable. Mettons à jour nos composants `App` et `TodoList` pour ajouter des liens de navigation en utilisant les deux méthodes :

**src/components/App.js**

**src/components/TodoList.js**

Vous pourrez maintenant ajouter un élément `Todo` dans la vue `todos`, puis cliquer sur le bouton d'ouverture pour accéder à la vue `todo` pour le nouvel élément :

![Image](https://cdn-media-1.freecodecamp.org/images/8eH6t6vmnyuG3xWb0zVME9Rg7-d4VKj2GouY)

### Conclusion

J'ai créé mobx-state-tree-router parce que j'ai constaté qu'il y avait un manque dans le paysage pour une bibliothèque de routage basée sur l'état à utiliser avec MobX State Tree. Je l'ai trouvée utile pour moi, alors j'espère qu'elle pourra également être utile à la communauté plus large.

Si vous ne l'avez pas encore fait, veuillez lire [l'article de Michel Weststrate](https://hackernoon.com/how-to-decouple-state-and-ui-a-k-a-you-dont-need-componentwillmount-cc90b787aa37) pour obtenir des informations sur le routage basé sur l'état.

Si vous avez des problèmes à signaler ou des contributions à apporter, veuillez vous rendre sur [mobx-state-tree-router sur Github](https://github.com/miles-till/mobx-state-tree-router).