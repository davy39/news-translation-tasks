---
title: Comment télécharger des fichiers avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-06T20:27:40.000Z'
originalURL: https://freecodecamp.org/news/upload-files-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/JavaScript-Blog-Cover.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment télécharger des fichiers avec JavaScript
seo_desc: 'By Austin Gil

  I recently published a tutorial showing how to upload files with HTML. That''s great,
  but it''s a bit limited to using the native browser form behavior, which causes
  the page to refresh.

  In this tutorial, I want to show you how to do the ...'
---

Par Austin Gil

J'ai récemment publié [un tutoriel montrant comment télécharger des fichiers avec HTML](https://austingil.com/uploading-files-with-html/). C'est bien, mais c'est un peu limité à l'utilisation du comportement natif du formulaire du navigateur, ce qui provoque le rechargement de la page.

Dans ce tutoriel, je veux vous montrer comment faire la même chose avec [JavaScript](https://austingil.com/category/javascript/) pour éviter le rechargement de la page. Ainsi, vous pouvez avoir la même fonctionnalité, mais avec une meilleure expérience utilisateur.

%[https://www.youtube.com/watch?v=Zyjgc2bySZo]

## Comment configurer un gestionnaire d'événements

Supposons que vous avez un formulaire [HTML](https://austingil.com/category/html/) qui ressemble à ceci :

```html
<form action="/api" method="post" enctype="multipart/form-data">
  <label for="file">Fichier</label>
  <input id="file" name="file" type="file" />
  <button>Télécharger</button>
</form>
```

Avec HTML, pour accéder à un fichier sur l'appareil de l'utilisateur, nous devons utiliser un [`<input>` avec le type "file"](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file). Et afin de créer la [requête HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) pour télécharger le fichier, nous devons utiliser un élément `[<form>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)`.

Lors de la manipulation avec JavaScript, la première partie est toujours vraie. Nous avons toujours besoin de l'entrée de fichier pour accéder aux fichiers sur l'appareil. Mais les navigateurs ont une [API Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) que nous pouvons utiliser pour faire des requêtes HTTP sans formulaires.

J'aime toujours inclure un formulaire parce que :

1. [Amélioration progressive](https://austingil.com/resilient-applications-progressive-enhancement/) : Si JavaScript échoue pour une raison quelconque, le formulaire HTML fonctionnera toujours.
2. Je suis paresseux : Le formulaire facilitera réellement mon travail plus tard, comme nous le verrons.

Avec cela à l'esprit, pour que JavaScript soumette ce formulaire, je vais configurer un gestionnaire d'événements "submit".

```js
const form = document.querySelector('form');
form.addEventListener('submit', handleSubmit);

/** @param {Event} event */
function handleSubmit(event) {
  // Le reste de la logique ira ici.
}
```

Tout au long du reste de cet article, nous ne regarderons que la logique à l'intérieur de la fonction du gestionnaire d'événements, `handleSubmit`.

## Comment préparer la requête HTTP

La première chose que je dois faire dans ce gestionnaire de soumission est d'appeler la méthode `[preventDefault](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)` de l'événement pour empêcher le navigateur de recharger la page pour soumettre le formulaire. J'aime mettre cela à la fin du gestionnaire d'événements afin que si une [exception](https://developer.mozilla.org/en-US/docs/Glossary/Exception) est levée dans le corps de cette fonction, `preventDefault` ne sera **pas** appelée, et le navigateur reviendra au comportement par défaut.

```js
/** @param {Event} event */
function handleSubmit(event) {
  // Tout JS qui pourrait échouer va ici
  event.preventDefault();
}
```

Ensuite, nous voudrons construire la requête HTTP en utilisant l'API Fetch. L'API Fetch attend [le premier argument soit une URL](https://developer.mozilla.org/en-US/docs/Web/API/fetch#resource), et un deuxième [argument optionnel sous forme d'objet](https://developer.mozilla.org/en-US/docs/Web/API/fetch#options).

Nous pouvons obtenir l'URL à partir de la propriété `[action](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/action)` du formulaire. Elle est disponible sur tout [nœud DOM de formulaire](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement) auquel nous pouvons accéder en utilisant la propriété `[currentTarget](https://developer.mozilla.org/en-US/docs/Web/API/Event/currentTarget)` de l'événement. Si l'`action` n'est pas définie dans le HTML, elle sera par défaut l'URL actuelle du navigateur.

```js
/** @param {Event} event */
function handleSubmit(event) {
  const form = event.currentTarget;
  const url = new URL(form.action);

  fetch(url);

  event.preventDefault();
}
```

S'appuyer sur le HTML pour définir l'URL le rend plus déclaratif, garde notre gestionnaire d'événements réutilisable, et nos bundles JavaScript plus petits. Cela maintient également la fonctionnalité si le JavaScript échoue.

Par défaut, Fetch envoie des requêtes HTTP en utilisant la méthode `[GET](https://www.freecodecamp.org/news/javascript-get-request-tutorial/)`, mais pour télécharger un fichier, nous devons utiliser une méthode `[POST](https://www.freecodecamp.org/news/javascript-post-request-how-to-send-an-http-post-request-in-js/)`. Nous pouvons changer la méthode en utilisant le deuxième argument optionnel de `fetch`. Je vais créer une variable pour cet objet et assigner la propriété `method`, mais une fois de plus, je vais récupérer la valeur de l'attribut `[method](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/method)` du formulaire dans le HTML.

```js
const url = new URL(form.action);

/** @type {Parameters<fetch>[1]} */
const fetchOptions = {
  method: form.method,
};

fetch(url, fetchOptions);
```

Maintenant, la seule pièce manquante est d'inclure réellement la charge utile dans le corps de la requête.

## Comment ajouter le corps de la requête

Si vous avez déjà créé une requête Fetch dans le passé, vous avez peut-être inclus le corps sous forme de [chaîne JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) ou d'objet `[URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)`. Malheureusement, aucun de ceux-ci ne fonctionnera pour envoyer un fichier, car ils n'ont pas accès au contenu binaire du fichier.

Heureusement, il y a l'API `[FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData)` du navigateur. Nous pouvons l'utiliser pour construire le corps de la requête à partir du nœud DOM du formulaire. Et commodément, lorsque nous le faisons, il définit même l'en-tête `[Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)` de la requête sur `multipart/form-data` – également une étape nécessaire pour transmettre les données binaires.

```js
const url = new URL(form.action);
const formData = new FormData(form);

/** @type {Parameters<fetch>[1]} */
const fetchOptions = {
  method: form.method,
  body: formData,
};

fetch(url, fetchOptions);
```

C'est vraiment le minimum nécessaire pour télécharger des fichiers avec JavaScript. Faisons un petit récapitulatif :

1. Accès au système de fichiers en utilisant une entrée de type fichier.
2. Construire une requête HTTP en utilisant l'API Fetch (ou [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)).
3. Définir la méthode de requête sur `POST`.
4. Inclure le fichier dans le corps de la requête.
5. Définir l'en-tête HTTP `Content-Type` sur `multipart/form-data`.

Aujourd'hui, nous avons examiné une manière pratique de faire cela, en utilisant un élément de formulaire HTML avec un gestionnaire d'événements de soumission, et en utilisant un objet `FormData` dans le corps de la requête. La fonction `handleSumit` actuelle devrait ressembler à ceci :

```js
/** @param {Event} event */
function handleSubmit(event) {
  const url = new URL(form.action);
  const formData = new FormData(form);

  /** @type {Parameters<fetch>[1]} */
  const fetchOptions = {
    method: form.method,
    body: formData,
  };

  fetch(url, fetchOptions);

  event.preventDefault();
}
```

Malheureusement, le gestionnaire de soumission actuel n'est pas très réutilisable. Chaque requête inclura un corps défini sur un objet `FormData` et un en-tête "`Content-Type`" défini sur `multipart/form-data`. C'est trop fragile. Les corps ne sont pas autorisés dans les requêtes `GET`, et nous pouvons vouloir supporter différents types de contenu dans d'autres requêtes POST.

## Comment le rendre réutilisable

Nous pouvons rendre notre code plus robuste pour gérer les requêtes `GET` et `POST`, et envoyer l'en-tête `Content-Type` approprié. Nous le ferons en créant un objet `[URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)` en plus du `FormData`, et en exécutant une logique basée sur le fait que la méthode de requête doit être `POST` ou `GET`. J'essaierai de décrire la logique ci-dessous :

La requête utilise-t-elle une méthode `POST` ?

— Oui : l'attribut `[enctype](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/enctype)` du formulaire est-il `multipart/form-data` ?

— — Oui : définir le corps de la requête sur l'objet `FormData`. Le navigateur définira automatiquement l'en-tête "`Content-Type`" sur `multipart/form-data`.

— — Non : définir le corps de la requête sur l'objet `URLSearchParams`. Le navigateur définira automatiquement l'en-tête "`Content-Type`" sur `application/x-www-form-urlencoded`.

— Non : Nous pouvons supposer qu'il s'agit d'une requête `GET`. Modifier l'URL pour inclure les données en tant que paramètres de chaîne de requête.

La solution refactorisée ressemble à ceci :

```js
/** @param {Event} event */
function handleSubmit(event) {
  /** @type {HTMLFormElement} */
  const form = event.currentTarget;
  const url = new URL(form.action);
  const formData = new FormData(form);
  const searchParams = new URLSearchParams(formData);

  /** @type {Parameters<fetch>[1]} */
  const fetchOptions = {
    method: form.method,
  };

  if (form.method.toLowerCase() === 'post') {
    if (form.enctype === 'multipart/form-data') {
      fetchOptions.body = formData;
    } else {
      fetchOptions.body = searchParams;
    }
  } else {
    url.search = searchParams;
  }

  fetch(url, fetchOptions);

  event.preventDefault();
}
```

J'aime vraiment cette solution pour un certain nombre de raisons :

* Elle peut être utilisée pour n'importe quel formulaire.
* Elle s'appuie sur le HTML sous-jacent comme source déclarative de configuration.
* La requête HTTP se comporte de la même manière qu'avec un formulaire HTML. Cela suit le principe de l'amélioration progressive, donc le téléchargement de fichiers fonctionne de la même manière lorsque JavaScript fonctionne correctement ou lorsqu'il échoue.

Donc, c'est tout. C'est [télécharger des fichiers avec JavaScript](https://austingil.com/upload-files-with-javascript/).

Merci beaucoup d'avoir lu. J'espère que vous avez trouvé cela utile. Si vous avez aimé cet article et souhaitez me soutenir, les meilleures façons de le faire sont de [le partager](https://twitter.com/share?via=heyAustinGil), [de vous inscrire à ma newsletter](https://austingil.com/newsletter/), et [de me suivre sur Twitter](https://twitter.com/heyAustinGil).