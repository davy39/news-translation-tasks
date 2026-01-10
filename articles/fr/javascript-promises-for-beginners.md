---
title: Les Promesses JavaScript pour Débutants
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2022-05-25T14:56:17.000Z'
originalURL: https://freecodecamp.org/news/javascript-promises-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Web-capture_11-5-2022_134720_127.0.0.1-1.jpeg
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: Les Promesses JavaScript pour Débutants
seo_desc: 'In JavaScript, a promise is a placeholder (proxy) for the value of an ongoing
  operation.

  You typically use a promise to manage situations where you must wait for the outcome
  of an operation. For example, uploading files to the server and awaiting the...'
---

En JavaScript, une promesse est un espace réservé (proxy) pour la valeur d'une opération en cours.

Vous utilisez généralement une promesse pour gérer des situations où vous devez attendre le résultat d'une opération. Par exemple, télécharger des fichiers sur le serveur et attendre la réponse d'un appel API, ou simplement demander à l'utilisateur de choisir un fichier depuis son ordinateur.

Vous apprendrez les promesses JavaScript dans cet article en construisant une application exemple du monde réel comme celle ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Web-capture_11-5-2022_134720_127.0.0.1.jpeg align="left")

## Qu'est-ce qu'une Promesse ?

Une promesse est simplement une fonction qui retourne un `Object` auquel vous pouvez attacher des callbacks.

Les callbacks attachés à un objet promesse ne seront appelés que lorsque l'opération sera terminée. Les callbacks devront attendre jusqu'à ce que l'opération soit **réussie** ou **rejetée** :

```js
fetch(`some_api_url`).then((response) => {
  // Tout ici attendra que l'opération fetch soit terminée
});
```

Avant qu'une promesse ne se termine (la promesse est soit réussie soit rejetée), elle doit passer par différents états :

| État | Description | Callback |
| --- | --- | --- |
| en attente | Signifie que l'opération est toujours en cours et que la promesse est en attente | \- |
| réussie | L'opération a été terminée et elle a réussi | `.then()` |
| rejetée | L'opération a été terminée mais il y a eu une erreur | `.catch()` |
| terminée | La promesse a soit été résolue soit rejetée, dans les deux cas ce callback est appelé | `.finally()` |

Lorsque qu'une promesse est créée, l'état initial est en attente. Ensuite, selon le résultat de l'opération, la promesse est soit réussie soit rejetée.

D'après le tableau ci-dessus, vous pouvez facilement voir le callback qui sera appelé selon chaque état de la Promesse :

```js
fetch(`some_api_url`).then((response) => {
  // Cela sera appelé lorsque la promesse est réussie
}).catch((error) => {
  // Cela sera appelé lorsque la promesse est rejetée
}).finally(() => {
  // Cela sera appelé à chaque fois
})
```

## Comment Utiliser les Promesses en JavaScript

Maintenant que vous avez appris ce qu'est une promesse, démontrons comment vous pouvez utiliser les promesses en JavaScript en construisant l'application de recherche de films que nous avons vue plus tôt.

Une application de recherche de films basique devrait avoir un champ de saisie où les utilisateurs peuvent rechercher leurs films préférés. Elle devrait également avoir une interface utilisateur pour afficher quelques informations de base sur le film qu'ils ont recherché.

Commençons par créer le **HTML**.

### Comment écrire le HTML

Pour les besoins de ce tutoriel et pour afficher des exemples en direct, je vais utiliser **Codepen**, mais vous pouvez utiliser votre éditeur de code préféré.

Créez un fichier `index.html` et ajoutez le code suivant :

```html
  <div class="wrapper">
      <header class="header">
        <div class="header_logo">Film</div>
        <div class="header_actions">
          <form onsubmit="handle_form(event)" id="header_form">
            <div class="header_form-icon">
            <input type="search" class="header_form-input" placeholder="Rechercher, Appuyez sur Entrée pour Soumettre" />
            <svg class="icon" width="22px" height="22px"><use href="#icon-search" /></svg>
          </div>
          </form>
          <img id="img_icon" width="32px" height="32px" src="" alt="" >
        </div>
      </header>
      <main id="main">
        <section>
          <article class="movie">
            <div class="movie_img">
              <img id="img_src" src="" alt="" srcset="">
            </div>
            <div class="movie_info">
              <header><h1 class="movie_title"></h1></header>
              <div class="movie_desc"></div>
              <div class="movie_details">
                <h2>Détails</h2>
                <ul class="flex">
                  <li>Première diffusion : <span id="movie_date"></span></li>
                  <li>Note : <span id="movie_rating"></span></li>
                  <li>Durée : <span id="movie_runtime"></span></li>
                  <li>Statut : <span id="movie_status"></span></li>
                </ul>
              </div>
              <a href="" class="btn" target="_blank" rel="noopener noreferrer">
            <svg class="icon" width="16px" height="16px"><use href="#icon-play" /></svg>
                Regarder le Film</a>
            </div>
          </article>
          <div class="episodes_list">
            <h3 class="episodes_title"></h3>
          <ol class="episodes" id="episodes"></ol>
        </div>
        </section>
      </main>
    </div>
```

Ci-dessus, nous avons simplement créé le squelette de notre application de films. Alors maintenant, donnons-lui un peu de vie avec du CSS :

%[https://codepen.io/Spruce_khalifa/pen/wvygzLq?editors=0100] 

### Comment récupérer un film

Pour récupérer notre film, nous allons utiliser l'API TVMAZE. Créez le fichier `main.js` et ajoutez le code suivant :

```js
const get_movie = (value = "Game of thrones") => {
   fetch(
    `https://api.tvmaze.com/singlesearch/shows?q=${value}&embed=episodes`
  ).then((response) => create_UI(response.json()));
};
```

Nous avons créé une fonction `get_movie(value = "Game of thrones")` qui utilise l'API fetch de JavaScript. Nous l'utilisons pour faire une requête `GET` à notre endpoint d'API de films.

L'API fetch retourne une promesse. Pour utiliser la réponse de l'API, nous attachons le callback `.then()` dans lequel nous passons le `response.json()` dans une nouvelle fonction `create_UI()`. Allons-y et créons la fonction `create_UI` :

```js
const create_UI = (data) => {
  const movie_img = document.querySelector("#img_src");
  const movie_icon = document.querySelector("#img_icon");
  const movie_title = document.querySelector(".movie_title");
  const movie_desc = document.querySelector(".movie_desc");
  const movie_link = document.querySelector(".btn");
  const movie_date = document.querySelector("#movie_date");
  const movie_rating = document.querySelector("#movie_rating");
  const movie_runtime = document.querySelector("#movie_runtime");
  const movie_status = document.querySelector("#movie_status");

  // définir l'UI
  movie_icon.src = data.image.medium;
  movie_img.src = data.image.original;
  movie_title.textContent = data.name;
  movie_desc.innerHTML = data.summary;
  movie_link.href = data.officialSite;
  movie_date.textContent = data.premiered;
  movie_rating.textContent = data.rating.average;
  movie_runtime.textContent = data.runtime;
  movie_status.textContent = data.status;
};
```

La fonction ci-dessus, comme son nom l'indique, nous aide à créer l'UI pour notre application de films. Mais bien sûr, nous avons encore besoin d'un moyen de collecter le nom du film auprès des utilisateurs, alors corrigeons cela.

La première chose que nous devons faire est d'ajouter un gestionnaire d'événement `onsubmit` à notre formulaire HTML :

```html
<form onsubmit="search(event)" id="header_form">
  <input type="search" class="header_form-input" placeholder="Rechercher, Appuyez sur Entrée pour Soumettre" />
//
</form>
```

Maintenant, dans notre fichier `main.js`, nous pouvons gérer ce qui se passe lorsque nous soumettons le formulaire :

```js
// gérer la soumission du formulaire
const search = (event) => {
  event.preventDefault();
  const value = document.querySelector(".header_form-input").value;

  get_movie(value);
};
```

À chaque fois que l'utilisateur soumet le formulaire, nous obtenons la valeur qu'il a entrée dans la boîte de recherche et nous la passons à la fonction `get_movie(value = "Game of thrones")` que nous avons créée plus tôt.

## Chaînage de Promesses

Contrairement à ce que nous avons vu dans nos exemples précédents, le callback `.then()` n'est pas vraiment la fin. C'est parce que lorsque vous retournez la valeur d'une promesse, vous obtenez une autre promesse. Cela devient très utile lorsque vous voulez exécuter une série d'opérations asynchrones dans l'ordre.

Par exemple, notre API de films ne retourne pas seulement des informations sur un film, elle retourne également des informations sur tous les épisodes. Supposons que nous ne voulons pas afficher tous les épisodes de Game of Thrones, nous ne voulons que les quatre (4) premiers épisodes.

Avec le chaînage de promesses, nous pouvons facilement atteindre cet objectif :

```js
const get_movie = (value = "Game of thrones") => {
  fetch(`https://api.tvmaze.com/singlesearch/shows?q=${value}&embed=episodes`)
    .then((response) => response.json())
    .then((data) => {
      if (data._embedded.episodes.length > 0) {
        const new_data = data._embedded.episodes.slice(0, 4);

        create_UI(data);
        return create_episodesUI(new_data);
      } else {
        return create_UI(data);
      }
    });
};
```

C'est toujours notre fonction `get_movie()`, mais cette fois, au lieu de passer les données à la fonction `create_UI`, nous retournons la réponse `.then((response) => response.json())`. Cela crée une nouvelle promesse, à laquelle nous pouvons attacher plus de callbacks.

Idéalement, cette chaîne peut continuer indéfiniment. Rappelez-vous, tout ce que vous avez à faire est de retourner la valeur de la promesse.

## Comment Gérer les Erreurs dans les Promesses

Les erreurs qui se produisent dans une promesse vont immédiatement au callback `.catch()` :

```js
fetch(`https://api.tvmaze.com/singlesearch/shows?q=${value}&embed=episodes`)
    .then((response) => response.json())
    .then((data) => {
      // toute erreur ici déclenchera le callback .catch()
    }).catch((error) => {
    // toutes les erreurs sont capturées et traitées ici
    })
```

Le callback `.catch()` est une abréviation de `.then(null, (error) => {})`. Vous pourriez aussi écrire ce qui précède comme :

```js
fetch(`https://api.tvmaze.com/singlesearch/shows?q=${value}&embed=episodes`)
    .then((response) => response.json())
    .then((data) => {
      // toute erreur ici déclenchera le callback .catch()
    }, (error) => {
    // toutes les erreurs sont capturées et traitées ici
    })
```

Avec notre application de recherche de films, par exemple, lorsque nous rencontrons des erreurs, nous pouvons les gérer et afficher un joli message d'erreur aux utilisateurs dans le callback `.catch()` :

```js
const get_movie = (value = "Game of thrones") => {
  fetch(`https://api.tvmaze.com/singlesearch/shows?q=${value}&embed=episodes`)
    .then((response) => response.json())
    .then((data) => {
      if (data._embedded.episodes.length > 0) {
        const new_data = data._embedded.episodes.slice(0, 4);

        create_UI(data);
        return create_episodesUI(new_data);
      } else {
        return create_UI(data);
      }
    })
    .catch((error) => {
      console.log(error.message);
      // Défi : afficher votre erreur ici
    });
};
```

Maintenant, si pour une raison quelconque nous obtenons une erreur, le callback `.catch()` est appelé et nous affichons l'erreur correcte à l'utilisateur.

## Comment Créer des Promesses en JavaScript

Maintenant que nous avons appris ce que sont les promesses et comment les utiliser, voyons comment nous pouvons créer une promesse en JavaScript.

Pour créer une promesse en JavaScript, vous utilisez le constructeur de promesse. Le constructeur prend un argument : une fonction avec deux paramètres, `resolve` et `reject` :

```js
const is_true = true
const new_promise = new Promise((resolve,reject) => {
  if(is_true) {
    // tout s'est bien passé
    resolve()
  } else {
    // Oups, il y a eu une erreur
    reject()
  }
})
```

Ensuite, nous pouvons utiliser notre `new_promise` en attachant les callbacks :

```js
new_promise
  .then((response) => {
    // tout s'est bien passé
  })
  .catch((error) => {
    // gérer les erreurs
  });
```

## Conclusion

Dans ce tutoriel, nous avons appris les promesses, ce qu'elles sont et comment les utiliser en construisant une application de recherche de films. L'intégralité du code et l'aperçu en direct de notre application de films peuvent être trouvés sur Codepen : [Application de Recherche de Films](https://codepen.io/Spruce_khalifa/pen/wvygzLq?editors=0100).

### Défi

En créant notre application de films, j'ai laissé de côté certaines parties que je pense seraient idéales pour vous afin de pratiquer vos nouvelles compétences en Promesses :

1. Notre application de films semble gelée lorsque nous attendons la réponse de l'API. Vous pouvez essayer d'ajouter un chargeur pour indiquer à l'utilisateur que la promesse est en attente.
    
2. Nous utilisons actuellement `console.log(error)` pour enregistrer les erreurs. Mais nous ne voulons pas cela, alors vous pouvez trouver comment afficher toutes les erreurs aux utilisateurs de manière conviviale.
    

Si vous avez créé quelque chose de merveilleux avec cela, n'hésitez pas à tweeter à ce sujet et à me taguer [@sprucekhalifa](https://twitter.com/sprucekhalifa). Et n'oubliez pas de cliquer sur le bouton suivre.

Bon codage !