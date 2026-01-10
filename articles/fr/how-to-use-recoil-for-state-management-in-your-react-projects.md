---
title: Comment utiliser Recoil pour la gestion d'état dans vos projets React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-28T23:19:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-recoil-for-state-management-in-your-react-projects
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/fcc-recoil-article.png
tags:
- name: React
  slug: react
- name: 'State Management '
  slug: state-management
seo_title: Comment utiliser Recoil pour la gestion d'état dans vos projets React
seo_desc: "By Abdullah Adeel\nIf you're a React developer, you've probably used a\
  \ library for managing state in your React applications. And you've likely heard\
  \ of Redux \"the state management\" library for React. \nFor a long time, Redux\
  \ was the only reliable and ..."
---

Par Abdullah Adeel

Si vous êtes un développeur React, vous avez probablement utilisé une bibliothèque pour gérer l'état dans vos applications React. Et vous avez probablement entendu parler de Redux, la bibliothèque de "gestion d'état" pour React. 

Pendant longtemps, Redux était la seule solution fiable et la plus largement adoptée pour la gestion d'état dans les applications React. Et Redux a prouvé ses cas d'utilisation dans les grandes applications. 

Mais le principal problème que les développeurs rencontraient souvent avec Redux était l'expérience globale du développeur. Dans les premières versions de Redux, vous deviez configurer manuellement votre magasin de données global et connecter manuellement chaque composant pour le consommer et mettre à jour l'état global. En gros, cela prenait beaucoup de temps et d'efforts pour les développeurs pour configurer et utiliser Redux dans leurs applications. 

Avec le temps, Redux s'est amélioré et propose désormais des solutions de plugins simples comme **redux-toolkit**. Mais il existe maintenant des solutions de gestion d'état encore plus simples pour React comme [zustand](https://github.com/pmndrs/zustand), [recoil](https://github.com/facebookexperimental/Recoil), et [react-query](https://github.com/tannerlinsley/react-query) pour n'en nommer que quelques-unes.

Dans cet article, nous allons voir comment configurer et utiliser **Recoil** dans vos applications React en construisant une simple application de liste de tâches traditionnelle.

Avant de commencer, je tiens simplement à mentionner que tout le code pour l'exemple de l'application de liste de tâches se trouve dans [ce sandbox](https://codesandbox.io/s/wwlgu). N'hésitez pas à vous y référer et à le modifier.

%[https://codesandbox.io/embed/to-do-app-using-recoil-wwlgu?fontsize=14&hidenavigation=1&theme=dark]

## Comment installer Recoil

Commençons par installer la bibliothèque. Si vous travaillez sur votre ordinateur local, vous pouvez installer Recoil en utilisant `npm` ou `yarn`.

```node
npm i recoil

// ou

yarn add recoil
```

## Comment ajouter le composant racine de Recoil

La première chose que vous devez faire est d'envelopper toute votre application avec le composant `RecoilRoot` fourni par `recoil`. 

Puisque Recoil utilise une approche 100% basée sur les hooks, il est bon d'envelopper toute votre application avec le composant racine fourni par Recoil afin que vous puissiez accéder à l'état de votre application depuis n'importe quel composant. 

Vous pouvez simplement faire cela en important et en ajoutant `RecoilRoot` dans votre index.js (fichier d'entrée). Voici à quoi ressemblera votre index.js après l'avoir ajouté:

```js

import { StrictMode } from "react";
import ReactDOM from "react-dom";
import { RecoilRoot } from "recoil";
import App from "./App";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <StrictMode>
    <RecoilRoot>
      <App />
    </RecoilRoot>
  </StrictMode>,
  rootElement
);
```

## Comment créer un atome dans Recoil

Après cela, nous devons créer un **atome**. Un atome dans Recoil est simplement un morceau isolé de mémoire qui contient des données. Vous pouvez créer autant d'atomes que vous le souhaitez. 

Par exemple, disons que vous créez une application de médias sociaux où les utilisateurs peuvent marquer un certain poste. Pour stocker les postes marqués par les utilisateurs, vous pouvez avoir un atome séparé contenant uniquement les données pour les marque-pages. 

Lorsque certaines données changent dans l'atome - par exemple, l'utilisateur marque un poste - cela va re-rendre les composants abonnés à ou utilisant cet atome. 

C'est là que la partie performance de `recoil` entre en jeu. Recoil s'assurera que seuls les composants qui sont abonnés à cet atome spécifique sont re-rendus.

Créer un atome est extrêmement facile. Créez un fichier `src/recoil/atom/todoAtom.js` et ajoutez le code suivant:

```js
import { atom } from "recoil";

export const todoListAtom = atom({
  key: "todoListState",
  default: [],
});
```

## Comment créer votre premier atome

Vous devez simplement importer la fonction `atom` de `recoil`. Cette fonction prend un objet comme argument. 

La première entrée dans cet objet est `key`. Il s'agit d'une chaîne unique qui représentera cet atome spécifique. `default` est l'état initial de cet atome. Et c'est tout. C'est tout ce que vous devez faire pour le configurer. 

Assurez-vous d'exporter `todoListAtom` car nous l'utiliserons pour référencer cet atome.

## Comment ajouter des données à un atome

Maintenant, créons une entrée où l'utilisateur peut taper sa tâche. Créez `components/TodoItemCreator.js`. 

Dans ce composant, nous avons une entrée où l'utilisateur tapera et nous verrons à quel point il est simple d'ajouter une nouvelle tâche dans l'atome. Plus tard, nous verrons comment tous les composants qui utilisent le même atome se mettent à jour pour afficher la nouvelle tâche ajoutée. Vous pouvez être aussi créatif que vous le souhaitez lors du stylage de l'entrée. 

Ici, je vais simplement montrer comment nous pouvons utiliser le hook `useRecoilState` (il est fourni par la bibliothèque `recoil` pour obtenir l'état actuel des données à l'intérieur de l'atome) et une fonction pratique pour mettre à jour l'état. 

Si vous avez utilisé `useState` dans React, cela ressemblera beaucoup à ce à quoi vous êtes habitué dans l'état local de votre composant. Le hook `useRecoilState` prend un atome comme argument.

```js
import { useState } from "react";
import { useRecoilState } from "recoil";
import { todoListAtom } from "../recoil/atoms/todoAtom";
import { generateUID } from "../utils/uuid";

export const TodoItemCreator = () => {
  const [inputValue, setInputValue] = useState("");
  const [_, setTodoList] = useRecoilState(todoListAtom);

  const onChange = (event) => {
    setInputValue(event.target.value);
  };

  const addTodoItem = () => {
    if (inputValue) {
      setTodoList((oldTodoList) => [
        ...oldTodoList,
        {
          id: generateUID(),
          text: inputValue,
          isComplete: false
        }
      ]);
      setInputValue("");
    }
  };

  return (
    <div className="todo-creator">
      <input type="text" value={inputValue} onChange={onChange} />
      <button className="add-btn" onClick={addTodoItem}>
        Ajouter une tâche
      </button>
    </div>
  );
};


```

Lorsque l'utilisateur tape dans l'entrée et clique sur le bouton `Ajouter une tâche`, une fonction `addTodoItem` est appelée. Cette fonction appelle simplement la fonction `setTodoList` donnée par le hook. 

Puisqu'il est recommandé de ne jamais mettre à jour votre état global directement, créez plutôt une copie superficielle des tâches précédentes et ajoutez-en une nouvelle. Dans l'extrait de code ci-dessus, `generateUID` est simplement une fonction utilitaire qui retournera un `uuidv4` unique pour retourner un identifiant unique aléatoire que nous utiliserons plus tard pour mettre à jour une tâche simple à partir d'une liste de `tâches`.

## Comment consommer des données de l'atome

Maintenant, créons un composant pour afficher une tâche dans une liste et permettre à l'utilisateur de mettre à jour, supprimer ou marquer les tâches comme terminées. Créez `src/components/TodoMain.js`.

```js
import { useRecoilValue } from "recoil";
import { TodoItemCreator } from "./TodoItemCreator";
import { TodoItem } from "./TodoItem";
import { todoListAtom } from "../recoil/atoms/todoAtom";
import "./todo.css";

export const TodoMain = () => {
  const todoList = useRecoilValue(todoListAtom);

  return (
    <div className="parent-container">
      <div>
        <TodoItemCreator />
        {todoList.length > 0 && (
          <div className="todos-list">
            {todoList.map((todoItem) => (
              <TodoItem key={todoItem.id} item={todoItem} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};


```

`useRecoilValue` est un hook fourni par `recoil` qui retourne uniquement l'état actuel des données dans l'atome. Nous utiliserons ce hook pour obtenir toutes les tâches et les `mapper` pour les afficher à l'écran. 

## Comment mettre à jour les données dans l'atome

`TodoItem` est un composant qui utilise le même hook `useRecoilState` et quelques fonctions auxiliaires pour trouver et mettre à jour l'état d'une tâche spécifique.

```js
import { useRecoilState } from "recoil";
import { todoListAtom } from "../recoil/atoms/todoAtom";

export const TodoItem = ({ item }) => {
  const [todoList, setTodoList] = useRecoilState(todoListAtom);
  const index = todoList.findIndex((listItem) => listItem === item);

  const editItemText = (event) => {
    const newList = replatItemAtIndex(todoList, index, {
      ...item,
      text: event.target.value
    });

    setTodoList(newList);
  };

  const toggleItemCompletion = () => {
    const newList = replatItemAtIndex(todoList, index, {
      ...item,
      isComplete: !item.isComplete
    });

    setTodoList(newList);
  };

  const deleteItem = () => {
    const newList = removeItemAtIndex(todoList, index);

    setTodoList(newList);
  };

  return (
    <div className="container">
      <input
        className={item.isComplete.toString() === "true" && "done-task"}
        type="text"
        value={item.text}
        onChange={editItemText}
      />
      <input
        type="checkbox"
        checked={item.isComplete}
        onChange={toggleItemCompletion}
      />
      <button className="del-btn" onClick={deleteItem}>
        X
      </button>
    </div>
  );
};

const replatItemAtIndex = (arr, index, newValue) => {
  return [...arr.slice(0, index), newValue, ...arr.slice(index + 1)];
};

const removeItemAtIndex = (arr, index) => {
  return [...arr.slice(0, index), ...arr.slice(index + 1)];
};


```

Et c'est tout. Avec deux hooks et une fonction, vous pouvez gérer toutes les exigences de gestion d'état de vos applications React. La puissance de Recoil réside dans son API simple et conviviale pour les débutants et ses performances.

Sur ce, je vous remercie beaucoup d'avoir pris le temps de lire cet article. Si vous le trouvez intéressant, rejoignez-moi sur [Twitter](https://twitter.com/abdadeel_) [abdadeel_](https://twitter.com/abdadeel_) où je partage du contenu intéressant sur le développement web.