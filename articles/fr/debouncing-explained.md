---
title: Debouncing dans React – Comment retarder une fonction JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-14T16:42:51.000Z'
originalURL: https://freecodecamp.org/news/debouncing-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/How-to-Build-a-Weather-Application-using-React--14-.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Debouncing dans React – Comment retarder une fonction JS
seo_desc: 'By Nishant Kumar

  There are some heavy tasks in software development. Take calling an API, for example.
  Suppose we have an API that searches a list of users, and we can''t afford to fire
  it too often. We want to search only when we have typed the whole...'
---

Par Nishant Kumar

Il existe certaines tâches lourdes dans le développement logiciel. Prenons l'appel à une API, par exemple. Supposons que nous avons une API qui recherche une liste d'utilisateurs, et nous ne pouvons pas nous permettre de l'appeler trop souvent. Nous voulons rechercher uniquement lorsque nous avons tapé la requête de recherche complète. 

Eh bien, [le debouncing est une pratique en développement logiciel](https://www.freecodecamp.org/news/javascript-debounce-example/) qui garantit que certaines tâches lourdes comme celle ci-dessus ne sont pas déclenchées trop souvent.

## Quand utiliser le Debouncing

Comprenons cela avec un exemple. Supposons que nous avons un élément d'entrée qui obtient des données lorsque nous tapons quelque chose. Par exemple, disons que nous tapons un code postal, et il retourne des données. 

Mais il y a un piège ici. Supposons que notre code postal est 800001. Si nous tapons le premier caractère, c'est-à-dire 8, nous enverrons une requête au serveur backend. Ensuite, nous tapons 0, et nous enverrons une autre requête au serveur, et ainsi de suite.  

Cela appelle l'API tant de fois, et à son tour surutilise les requêtes. Donc, pour éviter cela, nous utilisons quelque chose appelé une fonction de debounce.

Pour y parvenir, nous avons une fonctionnalité en JavaScript appelée Debouncing.

## Debouncing en JavaScript – un exemple pratique

Dans l'exemple ci-dessous, nous appelons simplement une API en utilisant la méthode **axios.get** lorsque nous tapons un caractère numérique dans la zone de saisie. 

Le caractère saisi est passé à la fonction en tant qu'argument et nous passons la valeur en tant que paramètres de chemin. Nous enregistrons également la réponse dans la console. 

```
import axios from "axios";
import React from "react";
import "./styles.css";

export default function App() {
  const setInput = (value) => {
    axios
      .get(`https://api.postalpincode.in/pincode/${value}`)
      .then((response) => {
        console.log(response.data[0]?.PostOffice[0]);
      });
  };
  return (
    <div className="app">
      <input
        placeholder="Rechercher..."
        onChange={(e) => setInput(e.target.value)}
      />
    </div>
  );
}

```

Mais le piège ici est que chaque fois que nous écrivons un caractère, notre API sera déclenchée. Donc, en revenant à notre exemple ci-dessus, disons que nous voulons taper 800001. Encore une fois, dès que nous tapons 8, l'API sera déclenchée et elle recherchera le caractère 8. Ensuite, nous taperons 0 (zéro), et l'API recherchera 80, et ainsi de suite.

Maintenant, changeons tout le flux afin d'ajouter le debouncing. Dans le cas du Debouncing, l'API ne se déclenchera qu'une seule fois après 2 secondes, après avoir tapé notre code postal complet.

Tout d'abord, créez un état en utilisant le hook **useState** dans React.

```
const [pinCode, setPinCode] = React.useState("");
```

Maintenant, nous devons définir les données dans l'état **pinCode** lorsque nous tapons quelque chose, en utilisant le gestionnaire d'événements **onChange**.

```
<input
      placeholder="Rechercher..."
      onChange={(event) => setPinCode(event.target.value)}
 />
```

Maintenant, utilisons un **useEffect Hook** qui s'exécutera chaque fois que notre code postal changera, ou lorsque nous taperons quelque chose dans la saisie de recherche.

```
React.useEffect(() => {

}, [pinCode])
```

Dans ce hook useEffect, nous aurons une fonction appelée **getData**. Cette fonction getData aura une fonction de rappel appelée **setTimeOut**. Et nous définirons le minuteur pour 2 secondes.

```
React.useEffect(() => {
    const getData = setTimeout(() => {
      
    }, 2000)
}, [pinCode])
```

Et maintenant dans cette fonction **getData**, appelons notre API.

```
React.useEffect(() => {
    const getData = setTimeout(() => {
      axios
      .get(`https://api.postalpincode.in/pincode/${pinCode}`)
      .then((response) => {
        console.log(response.data[0]);
      });
    }, 2000)
}, [pinCode])
```

Nous devrons également détruire l'instance du **useEffect hook** en utilisant **return**, suivi de **clearTimeout**, chaque fois qu'il se termine.

```
React.useEffect(() => {
    const getData = setTimeout(() => {
      axios
      .get(`https://api.postalpincode.in/pincode/${pinCode}`)
      .then((response) => {
        console.log(response.data[0]);
      });
    }, 2000)

    return () => clearTimeout(getData)
  }, [pinCode])
```

Et nous avons terminé. Tapons quelque chose dans la saisie, et après 2 secondes nous obtiendrons nos résultats.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-06-11-200335.png)

Et voilà !

## Conclusion

Maintenant, vous savez comment et pourquoi utiliser la fonction de debounce. Si simple et facile, n'est-ce pas ? 

Maintenant, si nous tapons une requête de recherche dans la saisie, elle s'affichera après 2 secondes, juste lorsque nous arrêtons de modifier la saisie. Et nous avons utilisé le **debouncing** pour faire cela. 

Il existe de multiples applications du debouncing. Nous pouvons l'utiliser pour éviter de solliciter notre API encore et encore. Et nous pouvons l'utiliser pour nous assurer que les données du formulaire sont soumises une seule fois, même si nous cliquons plusieurs fois sur le bouton de soumission.

Vous pouvez également consulter ma vidéo sur YouTube sur [React Debounce Function in 100 Seconds - Delay a function in React](https://youtu.be/EApDvKguG_0).

Obtenez le code [ici](https://codesandbox.io/s/react-debouncing-k5qdlv?file=/src/App.js).

Bonne apprentissage.