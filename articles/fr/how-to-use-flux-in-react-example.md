---
title: Comment utiliser Flux pour gérer l'état dans ReactJS - Expliqué avec un exemple
subtitle: ''
author: Sharvin Shah
co_authors: []
series: null
date: '2020-04-20T19:25:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-flux-in-react-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Flux-4.png
tags:
- name: Flux
  slug: flux
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
seo_title: Comment utiliser Flux pour gérer l'état dans ReactJS - Expliqué avec un
  exemple
seo_desc: 'If you have started working on ReactJS recently then you might be wondering
  how to manage state in React so that your application can scale.

  To solve this state management issue, many companies and people have developed various
  solutions. Facebook, w...'
---

Si vous avez commencé à travailler sur ReactJS récemment, vous vous demandez peut-être comment gérer l'état dans React afin que votre application puisse évoluer.

Pour résoudre ce problème de gestion d'état, de nombreuses entreprises et personnes ont développé diverses solutions. Facebook, qui a développé ReactJS, a proposé une solution appelée [**Flux**](https://facebook.github.io/flux/).

Vous avez peut-être entendu parler de **Redux** si vous avez travaillé sur des technologies front-end telles que **AngularJS** ou **EmberJS**. ReactJS dispose également d'une bibliothèque pour implémenter Redux.

Mais avant d'apprendre Redux, je vous conseille de vous familiariser avec Flux et de le comprendre. Ensuite, essayez Redux. Je dis cela parce que Redux est une version plus avancée de Flux. Si les concepts de Flux sont clairs, alors vous pouvez apprendre Redux et l'intégrer dans votre application.

## Qu'est-ce que Flux ?

Flux utilise un **modèle de flux de données unidirectionnel** pour résoudre la complexité de la gestion d'état. Rappelez-vous, ce n'est pas un framework, mais plutôt un modèle qui vise à résoudre le problème de la gestion d'état.

Vous vous demandez peut-être ce qui ne va pas avec le framework MVC existant ? Imaginez que l'application de votre client s'agrandit. Vous avez des interactions entre de nombreux modèles et vues. À quoi cela ressemblerait-il ?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-16-at-6.38.14-PM.png align="left")

*Crédit : Image de l'événement Facebook F8 Flux*

La relation entre les composants devient compliquée. Il devient difficile de faire évoluer l'application. Facebook a été confronté au même problème. Pour résoudre ce problème, ils ont architecturé un **flux de données unidirectionnel**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Flux-3.png align="left")

*Crédit : Image de la documentation Flux de Facebook*

Comme vous pouvez le voir sur l'image ci-dessus, il y a beaucoup de composants utilisés dans Flux. Passons en revue tous les composants un par un.

**Vue (View) :** ce composant rend l'interface utilisateur. Chaque fois qu'une interaction utilisateur se produit (comme un événement), il déclenche l'action. De plus, lorsque le Store informe la Vue qu'un changement a eu lieu, elle se ré-affiche. Par exemple, si un utilisateur clique sur le bouton **Ajouter**.

**Action :** ce composant gère tous les événements. Ces événements sont transmis par le composant de vue. Cette couche est généralement utilisée pour effectuer des appels API. Une fois l'action terminée, elle est dispatchée à l'aide du Dispatcher. L'action peut être quelque chose comme ajouter un post, supprimer un post, ou toute autre interaction utilisateur.

La structure commune de la charge utile pour dispatcher un événement est la suivante :

```js
{
	actionType: "",
    data: {
        title: "Comprendre Flux étape par étape",
        author: "Sharvin"
    }
}
```

La clé actionType est obligatoire et elle est utilisée par le dispatcher pour transmettre les mises à jour au store concerné. Il est également une pratique courante d'utiliser des constantes pour contenir le nom de la valeur de la clé actionType afin d'éviter les fautes de frappe. Data contient les informations de l'événement que nous voulons dispatcher de l'Action au Store. Le nom de cette clé peut être n'importe quoi.

**Dispatcher :** c'est le hub central et le registre singleton. Il dispatch la charge utile des Actions au Store. Il s'assure également qu'il n'y a pas d'effets en cascade lorsqu'une action est dispatchée au store. Il garantit qu'aucune autre action ne se produit avant que la couche de données ait terminé le traitement et les opérations de stockage.

Considérez ce composant comme un contrôleur de trafic dans le système. C'est une liste centralisée de callbacks. Il invoque le callback et diffuse la charge utile qu'il a reçue de l'action.

Grâce à ce composant, le flux de données est prévisible. Chaque action met à jour le store spécifique avec le callback qui est enregistré auprès du dispatcher.

**Store :** il contient l'état de l'application et est la couche de données de ce modèle. Ne le considérez pas comme un modèle MVC. Une application peut avoir un ou plusieurs stores. Les stores sont mis à jour car ils ont un callback qui est enregistré en utilisant le dispatcher.

L'émetteur d'événements de Node est utilisé pour mettre à jour le store et diffuser la mise à jour à la vue. La vue ne met jamais directement à jour l'état de l'application. Il est mis à jour en raison des changements apportés au store.

Ce n'est que la partie de Flux qui peut mettre à jour les données. Les interfaces implémentées dans le store sont les suivantes :

1. **EventEmitter** est étendu pour informer la vue que les données du store ont été mises à jour.

2. Des écouteurs comme **addChangeListener** et **removeChangeListener** sont ajoutés.

3. **emitChange** est utilisé pour émettre le changement.

Considérez le diagramme ci-dessus avec plus de stores et de vues. Pourtant, le modèle et le flux de données seront les mêmes. Cela est dû au fait que ce flux est unidirectionnel et prévisible, contrairement au MVC ou au Two-way binding. Cela améliore la **cohérence des données** et il est **plus facile de trouver les bugs**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Flux-Flow-3.png align="left")

*Flux de données Flux*

Flux apporte les avantages clés suivants avec l'aide du **flux de données unidirectionnel** :

1. Le code devient assez clair et facile à comprendre.

2. Facilement testable avec des tests unitaires.

3. Des applications évolutives peuvent être construites.

4. Flux de données prévisible.

> ***Note :*** *Le seul inconvénient avec Flux est qu'il y a un peu de code standard à écrire. En dehors du code standard, il y a peu de code à écrire lors de l'ajout de composants à l'application existante.*

## Modèle d'application

Pour apprendre à implémenter Flux dans ReactJS, nous allons construire une page de posts. Ici, nous afficherons tous les posts. Le modèle d'application est disponible à ce [commit](https://github.com/Sharvin26/DummyBlog/tree/0d56987b2d461b794e7841302c9337eda1ad0725). Nous utiliserons cela comme modèle pour intégrer Flux par-dessus.

Pour cloner le code à partir de ce commit, utilisez la commande suivante :

```shell
git clone https://github.com/Sharvin26/DummyBlog.git
```

```shell
git checkout 0d56987b2d461b794e7841302c9337eda1ad0725
```

Nous aurons besoin des modules **react-router-dom** et **bootstrap**. Pour installer ces packages, utilisez la commande suivante :

```python
npm install react-router-dom@5.0.0 bootstrap@4.3.1
```

Une fois terminé, vous verrez l'application suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/captured.gif align="left")

*DummyBlog*

Pour comprendre Flux en détail, nous n'implémenterons que la page des posts **GET**. Une fois cela fait, vous réaliserez que le processus est le même pour **POST**, **EDIT** et **DELETE**.

Ici, vous verrez la structure de répertoire suivante :

```shell
+-- README.md 
+-- package-lock.json
+-- package.json
+-- node_modules
+-- .gitignore
+-- public
|   +-- index.html
+-- src
|   +-- +-- components
|   +-- +-- +-- common
|   +-- +-- +-- +-- NavBar.js
|   +-- +-- +-- PostLists.js
|	+-- +-- pages
|   +-- +-- +-- Home.js
|   +-- +-- +-- NotFound.js
|   +-- +-- +-- Posts.js
|   +-- index.js
|   +-- App.js
|   +-- db.json
```

> **Note :** Nous avons ajouté ici un fichier `db.json`. Il s'agit d'un fichier de données factices. Puisque nous ne voulons pas construire des API et préférons nous concentrer sur Flux, nous récupérerons les données à partir de ce fichier.

Le composant de base de notre application est `index.js`. Ici, nous avons rendu `App.js` à l'intérieur de `index.html` sous le répertoire public en utilisant les méthodes **render** et **getElementById**. `App.js` est utilisé pour configurer les routes.

Nous ajoutons également le composant **NavBar** en haut des autres afin qu'il soit disponible pour tous les composants.

Dans le répertoire **pages**, nous avons 3 fichiers =&gt; `Home.js`, `Posts.js`, et `NotFound.js`. `Home.js` est simplement utilisé pour afficher le composant Home. Lorsque l'utilisateur accède à une URL qui n'existe pas, `NotFound.js` est rendu.

`Posts.js` est le composant parent et il est utilisé pour obtenir les données du fichier `db.json`. Il transmet ces données à `PostLists.js` sous le répertoire **components**. Ce composant est un composant simple et il ne gère que l'interface utilisateur. Il reçoit les données en tant que props de son composant parent (`Posts.js`) et les affiche sous forme de cartes.

Maintenant que nous sommes clairs sur le fonctionnement de notre application de blog, nous commencerons à intégrer Flux par-dessus.

## Intégration de Flux

Installez Flux en utilisant la commande suivante :

```shell
npm install flux@3.1.3
```

Pour intégrer Flux dans notre application, nous diviserons cette section en 4 sous-sections :

1. Dispatcher

2. Actions

3. Stores

4. Vue

Note : Le code complet est disponible dans ce [dépôt](https://github.com/Sharvin26/DummyBlog).

### Dispatcher

Tout d'abord, créez deux nouveaux dossiers nommés **actions** et **stores** sous le répertoire **src**. Après cela, créez un fichier nommé `appDispatcher.js` sous le même répertoire src.

**Note :** À partir de maintenant, tous les fichiers liés à Flux auront une **casse Camel** car ils ne sont pas des composants ReactJS.

Allez dans `appDispatcher.js` et copiez-collez le code suivant :

```js
import { Dispatcher } from "flux";
const dispatcher = new Dispatcher();
export default dispatcher;
```

Ici, nous importons le Dispatcher de la bibliothèque flux que nous avons installée, créons un nouvel objet et l'exportons afin que notre module d'actions puisse l'utiliser.

### Actions

Maintenant, allez dans le répertoire **actions** et créez deux fichiers nommés `actionTypes.js` et `postActions.js`. Dans `actionTypes.js`, nous définirons les constantes dont nous avons besoin dans `postActions.js` et le module store.

La raison derrière la définition des constantes est que nous ne voulons pas faire de fautes de frappe. Vous n'êtes pas obligé de définir des constantes, mais c'est généralement considéré comme une bonne pratique.

```js
// actionTypes.js

export default {
    GET_POSTS: "GET_POSTS",
};
```

Maintenant, dans `postActions.js`, nous récupérerons les données de `db.json` et utiliserons l'objet dispatcher pour les dispatcher.

```js
//postActions.js

import dispatcher from "../appDispatcher";
import actionTypes from "./actionTypes";
import data from "../db.json";

export function getPosts() {
    dispatcher.dispatch({
        actionTypes: actionTypes.GET_POSTS,
        posts: data["posts"],
    });
}
```

Ici, dans le code ci-dessus, nous avons importé l'objet dispatcher, la constante actionTypes et les données. Nous utilisons la méthode dispatch de l'objet dispatcher pour envoyer les données au store. Les données dans notre cas seront envoyées dans le format suivant :

```json
{
	actionTypes: "GET_POSTS",
    posts: [
        {
            "id": 1,
            "title": "Bonjour le monde",
            "author": "Sharvin Shah",
            "body": "Exemple d'application de blog"
        },
        {
            "id": 2,
            "title": "Bonjour à nouveau",
            "author": "John Doe",
            "body": "Test d'un autre composant"
        }
    ]
}
```

### Stores

Maintenant, nous devons construire le store qui servira de **couche de données** pour stocker les posts. Il aura un **écouteur d'événements** pour informer la vue qu'un changement a eu lieu, et s'**enregistrera** en utilisant le dispatcher avec les actions pour obtenir les données.

Allez dans le répertoire store et créez un nouveau fichier appelé `postStore.js`. Maintenant, nous importerons d'abord **EventEmitter** du package Events. Il est disponible dans NodeJS par défaut. Nous importerons également l'objet dispatcher et le fichier de constantes actionTypes ici.

```js
import { EventEmitter } from "events";
import dispatcher from "../appDispatcher";
import actionTypes from "../actions/actionTypes";
```

Nous déclarerons la constante de l'événement **change** et une variable pour contenir les posts chaque fois que le dispatcher les transmet.

```js
const CHANGE_EVENT = "change";
let _posts = [];
```

Maintenant, nous allons écrire une classe qui étend **EventEmitter** comme classe de base. Nous déclarerons les méthodes suivantes dans cette classe :

`addChangeListener` : Il utilise **EventEmitter.on** de NodeJS. Il ajoute un écouteur de changement qui accepte la fonction de callback.

`removeChangeListener` : Il utilise **EventEmitter.removeListener** de NodeJS. Chaque fois que nous ne voulons plus écouter un événement spécifique, nous utilisons la méthode suivante.

`emitChange` : Il utilise **EventEmitter.emit** de NodeJS. Chaque fois qu'un changement se produit, il émet ce changement.

Cette classe aura également une méthode appelée `getPosts` qui retourne la variable `_posts` que nous avons déclarée au-dessus de la classe.

Sous la déclaration de variable, ajoutez le code suivant :

```js
class PostStore extends EventEmitter {
    addChangeListener(callback) {
        this.on(CHANGE_EVENT, callback);
    }

    removeChangeListener(callback) {
        this.removeListener(CHANGE_EVENT, callback);
    }

    emitChange() {
        this.emit(CHANGE_EVENT);
    }

    getPosts() {
        return _posts;
    }
}
```

Maintenant, créez l'objet `store` de notre classe PostStore. Nous exporterons cet objet afin de pouvoir l'utiliser dans la vue.

```js
const store = new PostStore();
```

Après cela, nous utiliserons la méthode **register** du dispatcher pour recevoir la charge utile de notre composant Actions.

Pour s'enregistrer pour un événement spécifique, nous devons utiliser la valeur `actionTypes` et déterminer quelle action a eu lieu et traiter les données en conséquence. Ajoutez le code suivant sous la déclaration de l'objet :

```js
dispatcher.register((action) => {
    switch (action.actionTypes) {
        case actionTypes.GET_POSTS:
            _posts = action.posts;
            store.emitChange();
            break;
        default:
    }
});
```

Nous exporterons l'objet de ce module afin que d'autres puissent l'utiliser.

```js
export default store;
```

### Vue

Maintenant, nous allons mettre à jour notre vue pour envoyer l'événement à `postActions` chaque fois que notre page de posts est chargée et recevoir la charge utile de postStore. Allez dans `Posts.js` sous le répertoire **pages**. Vous trouverez le code suivant à l'intérieur de la méthode **useEffect** :

```js
useEffect(() => {
	setposts(data["posts"]);
}, []);
```

Nous allons changer la façon dont notre useEffect lit et met à jour les données. Tout d'abord, nous utiliserons la méthode `addChangeListener` de la classe postStore et nous lui passerons un callback `onChange`. Nous définirons la valeur d'état `posts` pour qu'elle ait une valeur de retour de la méthode `getPosts` du fichier `postStore.js`.

Au début, le store retournera un tableau vide car il n'y a pas de données disponibles. Nous appellerons donc une méthode `_getPosts_` de `postActions.js`. Cette méthode lira les données et les transmettra au store. Ensuite, le store émettra le changement et `addChangeListener` écoutera le changement et mettra à jour la valeur de `posts` dans son callback `onChange`.

Si cela semble confus, ne vous inquiétez pas, consultez le diagramme ci-dessous qui facilite la compréhension.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/FluxBlogFlow-1.png align="left")

Supprimez l'ancien code et mettez à jour le code suivant dans `Posts.js` :

```js
import React, { useState, useEffect } from "react";
import PostLists from "../components/PostLists";
import postStore from "../stores/postStore";
import { getPosts } from "../actions/postActions";

function PostPage() {
    const [posts, setPosts] = useState(postStore.getPosts());

    useEffect(() => {
        postStore.addChangeListener(onChange);
        if (postStore.getPosts().length === 0) getPosts();
        return () => postStore.removeChangeListener(onChange);
    }, []);

    function onChange() {
        setPosts(postStore.getPosts());
    }

    return (
        <div>
            <PostLists posts={posts} />
        </div>
    );
}

export default PostPage;
```

Ici, vous trouverez que nous avons également supprimé l'import et que nous utilisons `setPosts` à l'intérieur de notre callback au lieu de la méthode useEffect. `return () => postStore.removeChangeListener(onChange);` est utilisé pour supprimer l'écouteur une fois que l'utilisateur quitte cette page.

Avec cela, allez à la page du blog et vous trouverez que notre application de blog fonctionne. La seule différence est que maintenant, au lieu de lire les données dans la méthode **useEffect**, nous les lisons dans les actions, les stockons dans le store et les envoyons aux composants qui en ont besoin.

Lorsque vous utilisez l'API réelle, vous trouverez que l'application charge les données de l'API une fois et les stocke dans le store. Lorsque nous revisitons la même page, vous observerez qu'aucun appel API n'est nécessaire à nouveau. Vous pouvez le surveiller sous l'onglet source dans la console de développement Chrome.

Et nous avons terminé !! J'espère que ce tutoriel a rendu l'idée de Flux plus claire et que vous serez en mesure de l'utiliser dans vos projets.

> N'hésitez pas à me contacter sur [Twitter](https://twitter.com/sharvinshah26) et [Github](https://github.com/Sharvin26).