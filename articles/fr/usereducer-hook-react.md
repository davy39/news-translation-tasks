---
title: Tutoriel React Hooks – Comment utiliser le Hook useReducer
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2023-01-30T23:15:08.000Z'
originalURL: https://freecodecamp.org/news/usereducer-hook-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/photo-1672309046475-4cce2039f342.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Tutoriel React Hooks – Comment utiliser le Hook useReducer
seo_desc: 'State is an important part of a React application. Most functionalities
  involve making state updates in your component.

  But as your application grows, state updates become more and more complex. These
  complex state updates might get overwhelming when...'
---

L'état est une partie importante d'une application React. La plupart des fonctionnalités impliquent des mises à jour de l'état dans votre composant.

Mais à mesure que votre application grandit, les mises à jour de l'état deviennent de plus en plus complexes. Ces mises à jour d'état complexes peuvent devenir accablantes lorsque vous revisitez votre code.

Il existe une autre façon de gérer les mises à jour d'état, et c'est en utilisant des reducers. Mais qu'est-ce qu'un reducer ? Comment les utilisez-vous ? Que fait le hook `useReducer` ? Dans cet article, je répondrai à toutes ces questions.

## Qu'est-ce qu'un Reducer et pourquoi en avez-vous besoin ?

Prenons l'exemple d'une application de liste de tâches. Cette application implique l'ajout, la suppression et la mise à jour d'éléments dans la liste de tâches. L'opération de mise à jour elle-même peut impliquer la mise à jour de l'élément ou le marquage comme terminé.

Lorsque vous implémentez une liste de tâches, vous aurez une variable d'état `todoList` et vous effectuerez des mises à jour d'état pour chaque opération. Cependant, ces mises à jour d'état peuvent apparaître à différents endroits, parfois même en dehors du composant.

Pour rendre votre code plus lisible, vous pouvez déplacer toutes vos mises à jour d'état dans une seule fonction qui peut exister en dehors de votre composant. Lors de l'exécution des opérations requises, votre composant doit simplement appeler une seule méthode et sélectionner l'opération qu'il souhaite effectuer.

La fonction qui contient toutes vos mises à jour d'état est appelée le **reducer**. Cela est dû au fait que vous réduisez la logique d'état dans une fonction séparée. La méthode que vous appelez pour effectuer les opérations est la méthode **dispatch**.

## Comment fonctionne le Hook useReducer

Vous pouvez ajouter un reducer à votre composant en utilisant le hook `useReducer`. Importez la méthode useReducer depuis la bibliothèque comme ceci :

```python
import { useReducer } from 'react'
```

La méthode `useReducer` vous donne une variable d'état et une méthode `dispatch` pour effectuer des changements d'état. Vous pouvez définir l'état de la manière suivante :

```javascript
const [state, dispatch] = useReducer(reducerMethod, initialValue)
```

La méthode reducer contient votre logique d'état. Vous pouvez choisir quelle logique d'état appeler en utilisant la méthode `dispatch`. L'état peut également avoir une valeur initiale similaire au hook `useState`.

## Exemple de Hook useReducer

Prenons un exemple simple où nous avons une liste d'utilisateurs. Nous pouvons ajouter un nouvel utilisateur, supprimer un utilisateur existant et mettre à jour les détails de l'utilisateur. Normalement, nous créerions une variable d'état `user` et effectuerions des mises à jour d'état à différents endroits.

Essayons de faire la même chose en utilisant des reducers :

```javascript
const [users, dispatch] = useReducer(reducerMethod, userData);
```

Utilisez les données initiales suivantes :

```javascript
const userData = [
    {
        id:1,
        name: 'kunal',
        age: 22,
        admin: true
    },
    {
        id:2,
        name: 'rounak',
        age: 23,
        admin: false
    },
    {
        id:3,
        name: 'utkarsh',
        age: 22,
        admin: false
    },   
]
```

### Comment définir la méthode Reducer

La méthode reducer contient nos mises à jour d'état. La méthode prend deux arguments, la valeur actuelle de l'état et un objet action. L'objet action contient le type de l'action et les données supplémentaires nécessaires pour effectuer la mise à jour.

Nous effectuerons trois types de mises à jour – pour l'utilisateur ajouté, mis à jour et supprimé. Nous utiliserons switch-case pour sélectionner le type d'opération à effectuer.

```python
const reducerMethod = (users, action) => {
    switch(action.type) {
        // Mises à jour d'état ici
    }
}
```

Le champ `type` contient le nom de l'opération à effectuer. Il s'agit d'une chaîne de caractères et vous pouvez définir n'importe quelle valeur que vous souhaitez. Assurez-vous simplement qu'elle est pertinente pour l'action effectuée pour une meilleure lisibilité. Effectuons d'abord l'opération d'ajout :

```python
case 'addUser': {
    return [
        ...users,
        action.newUser
    ]
}
```

La logique de mise à jour de l'état est similaire à `setState`. Ici, vous retournez une nouvelle valeur d'état plutôt que de modifier directement la variable d'état.

Effectuons maintenant l'opération de mise à jour. Lors de l'exécution de l'opération de mise à jour, la méthode dispatch passe un objet `updatedUser` pour mettre à jour un utilisateur existant. Ces données supplémentaires sont passées via l'objet `action`.

```python
case 'updateUser': {
    return users.map(user => {
        if(user.id == action.updatedUser.id)
        	return action.updatedUser
        return user;
    })
}
```

Maintenant, pour l'opération de suppression, la méthode `dispatch` passe uniquement l'`id` de l'objet afin que le tableau d'état puisse le filtrer.

```javascript
case 'deleteUser': {
	return users.filter(user => user.id !== action.id)
}
```

Ajoutons également un cas par défaut si une action autre que les trois ci-dessus est spécifiée.

```python
default: {
	// Gérer l'erreur ici
}
```

Maintenant, créons les composants qui utiliseront réellement ce reducer.

Affichez la liste des utilisateurs dans le composant `UserDetails` avec les props suivantes :

```javascript
<UsersList users={users}
           handleUpdateUser={handleUpdateUser}
           handleDeleteUser={handleDeleteUser}
 />
```

Créez également un formulaire pour ajouter de nouveaux utilisateurs dans le composant `AddUserForm`.

```javascript
<AddUserForm handleAddUser={handleAddUser} />
```

Je n'ai pas mentionné les implémentations réelles des composants ici, car l'accent est uniquement mis sur la partie de mise à jour de l'état.

Nous effectuerons les mises à jour d'état à l'intérieur des méthodes de gestion en appelant la méthode `dispatch` et en passant le type de la mise à jour d'état avec certaines données. Pour l'opération d'ajout, passez le nouvel utilisateur à ajouter.

```python
const handleAddUser = (user) => {
    dispatch({
        type: 'addUser',
        newUser: user
    })
}
```

De même, vous pouvez implémenter `handleUpdateUser` et `handleDeleteUser`.

```python
const handleUpdateUser = (updatedUser) => {
    dispatch({
        type: 'updateUser',
        updatedUser: updatedUser
    })
}

const handleDeleteUser = (userId) => {
    dispatch({
        type: 'deleteUser',
        id: userId
    })
}
```

Les paramètres `newUser`, `updatedUser` et `userId` sont passés depuis les composants `AddUserForm` et `UsersList`. Ils contiennent les données nécessaires pour effectuer les mises à jour d'état.

## Conclusion

Pour toute fonctionnalité que vous créez, les mises à jour d'état constituent une partie cruciale de l'implémentation dans React. À mesure que la complexité de l'application augmente, le nombre de mises à jour d'état augmente également.

Dans cet article, j'ai expliqué ce qu'est un reducer et pourquoi nous en avons besoin. À l'aide d'un exemple, je vous ai montré à quel point il est pratique d'avoir toutes les mises à jour d'état en un seul endroit dans une fonction séparée. Cela rend le code plus lisible et accessible.

J'espère que ce tutoriel a aidé à éliminer toute confusion concernant le hook `useReducer`. J'ai essayé de l'expliquer en termes très simples.

Si vous n'êtes pas en mesure de comprendre le contenu ou si vous trouvez l'explication insatisfaisante, faites-le moi savoir. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me contacter sur Twitter. En attendant, au revoir !