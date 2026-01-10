---
title: Comment utiliser localStorage avec les Hooks React pour définir et obtenir
  des éléments
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-02-22T14:53:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-localstorage-with-react-hooks-to-set-and-get-items
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Yellow-and-Purple-Geometric-Covid-19-General-Facts-Twitter-Post.jpg
tags:
- name: localstorage
  slug: localstorage
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment utiliser localStorage avec les Hooks React pour définir et obtenir
  des éléments
seo_desc: 'localStorage is a web storage object that allows JavaScript sites and apps
  to keep key-value pairs in a web browser with no expiration date.

  This means the data survives page refreshes (sessionStorage) and even browser restarts.
  This indicates that t...'
---

localStorage est un objet de stockage web qui permet aux sites et applications JavaScript de conserver des paires clé-valeur dans un navigateur web sans date d'expiration.

Cela signifie que les données survivent aux actualisations de page (sessionStorage) et même aux redémarrages du navigateur. Cela indique que les données stockées dans le navigateur resteront même lorsque la fenêtre du navigateur est fermée.

En termes simples, le stockage local permet aux développeurs de stocker et de récupérer des données dans le navigateur.

Il est cependant crucial de comprendre que l'utilisation de localStorage comme base de données pour votre projet n'est pas une bonne pratique, car les données seront perdues lorsque l'utilisateur effacera le cache, entre autres.

Les développeurs utilisent fréquemment localStorage pour ajouter une fonctionnalité de mode sombre à une application, sauvegarder un élément de liste de tâches ou persister les valeurs de saisie de formulaire d'un utilisateur, parmi de nombreux autres scénarios.

Dans cet article, nous allons examiner comment utiliser localStorage avec les hooks React pour définir et obtenir des éléments facilement.

### Voici un scrim interactif sur la façon d'utiliser localStorage avec les Hooks React pour définir et obtenir des éléments :

<iframe src="https://scrimba.com/scrim/crdLpnSG?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## Qu'est-ce que les Hooks React ?

Les Hooks React sont des fonctions JavaScript que vous pouvez importer depuis le package React pour ajouter des capacités à vos composants.

Les Hooks permettent aux développeurs React d'utiliser l'état et les méthodes de cycle de vie au sein de composants fonctionnels. Ils fonctionnent également avec le code existant, ce qui les rend facilement adoptables dans une base de code.

Nous aurons besoin de deux hooks pour utiliser localStorage avec les hooks React :

* `useState()` – L'état de votre application est garanti de changer à un moment donné. Le hook `useState()` est une fonction qui accepte un paramètre, l'état initial (qui peut être la valeur d'une variable, un objet ou tout autre type de données dans votre composant), et retourne deux valeurs : l'état actuel et une fonction qui peut être utilisée pour mettre à jour l'état.

* `useEffect()` – Le hook Effect est activé par défaut après le premier rendu et chaque fois que l'état est modifié. Comme le suggèrent les noms, il est utilisé pour effectuer un effet chaque fois que l'état change. Ce hook est idéal pour configurer des écouteurs, récupérer des données depuis l'API et supprimer des écouteurs avant que le composant ne soit retiré du DOM.

## Comment implémenter localStorage dans React

localStorage nous donne accès à un objet de stockage du navigateur, qui inclut cinq méthodes :

* `setItem()` : Cette méthode est utilisée pour ajouter une clé et une valeur à localStorage.

* `getItem()` : Cette méthode est utilisée pour obtenir un élément de localStorage en utilisant la clé.

* `removeItem()` : Cette technique est utilisée pour supprimer un élément de localStorage en fonction de sa clé.

* `clear()` : Cette technique est utilisée pour supprimer toutes les instances de localStorage.

* `key()` : Lorsque vous fournissez un nombre, cela aide à la récupération d'une clé localStorage.

Dans cet article, nous ne considérerons que les méthodes les plus populaires, qui sont les deux premières méthodes.

### Comment utiliser la méthode `setItem()`

En donnant des valeurs à une clé, cette technique est utilisée pour stocker des objets dans localStorage. Cette valeur peut être de n'importe quel type de données, y compris du texte, un entier, un objet, un tableau, etc.

Il est vital de se rappeler que pour stocker des données dans localStorage, vous devez d'abord les convertir en chaîne de caractères avec la fonction `JSON.stringify()`.

```bash
const [items, setItems] = useState([]);

useEffect(() => {
  localStorage.setItem('items', JSON.stringify(items));
}, [items]);
```

Dans le code ci-dessus, nous avons d'abord créé un état et lui avons assigné un tableau vide (le vôtre pourrait être un autre type de données). Ensuite, nous avons utilisé `useEffect()` pour ajouter des objets à localStorage chaque fois que la valeur de notre état changeait. Nous l'avons fait en passant l'état comme second argument.

En gros, voici le code principal responsable de l'ajout de paires clé-valeur à localStorage :

```bash
localStorage.setItem('items', JSON.stringify(items));
```

Simplement, le code précédent nomme la clé (items) puis lui attribue une valeur, mais nous avons dû d'abord nous assurer que les données que nous ajoutions étaient une chaîne JSON.

Nous utilisons JSON.stringify() pour convertir un objet JSON en texte JSON stocké dans une chaîne, qui peut ensuite être transmis au serveur web.

![Image](https://paper-attachments.dropbox.com/s_EAEEAE9063B0CA7CBC6574F36123E82B36B6C1EC3724A86DA7C0B4C67C2DD652_1645380076460_explaining+useeffect+local+storage.jpg align="left")

*Structure de fonctionnement des hooks avec localStorage pour définir des éléments*

### Comment utiliser la méthode `getItem()`

Cette méthode récupère des objets depuis localStorage. Il existe d'autres méthodes pour accomplir cela avec React, mais nous utiliserons le hook `useEffect()` car c'est le meilleur.

Le hook `useEffect()` nous aide à récupérer tous les éléments au premier rendu, ce qui signifie que lorsque le composant est monté ou re-rendu, il obtient toutes nos données depuis localStorage.

Notez que c'est pourquoi nous avons passé un second argument vide.

```bash
const [items, setItems] = useState([]);

useEffect(() => {
  const items = JSON.parse(localStorage.getItem('items'));
  if (items) {
   setItems(items);
  }
}, []);
```

Il est important de se rappeler que lorsque nous avons stocké les données, nous les avons d'abord converties en chaîne JSON. Cela signifie que pour pouvoir maintenant les utiliser, nous devons convertir la chaîne JSON en objet JSON. Nous faisons cela avec la méthode `JSON.parse()`.

![Image](https://paper-attachments.dropbox.com/s_EAEEAE9063B0CA7CBC6574F36123E82B36B6C1EC3724A86DA7C0B4C67C2DD652_1645369611908_explaining+useeffect+local+storage2.jpg align="left")

*Structure de fonctionnement des hooks avec localStorage pour obtenir des éléments*

## Conclusion

Dans cet article, nous avons appris comment utiliser localStorage avec les hooks React, quand l'utiliser et quel hook utiliser.

Si vous voulez voir comment cela fonctionne en pratique, vous pouvez obtenir le code source d'une application simple de liste de tâches qui utilise localStorage et ces hooks [ici](https://github.com/olawanlejoel/Todo-App).

Vous pouvez en apprendre davantage sur [l'état et les props dans cet article détaillé](https://joelolawanle.com/posts/understanding-state-props-react-key-differences-explained) écrit par moi. Vous pouvez également consulter tous les articles écrits par moi dans ce [dépôt de contenu](https://joelolawanle.com/contents).