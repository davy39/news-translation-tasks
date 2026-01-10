---
title: Comment obtenir l'URL actuelle avec JavaScript - Tutoriel JS Location
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-04-25T00:34:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-current-url-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-template--10-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment obtenir l'URL actuelle avec JavaScript - Tutoriel JS Location
seo_desc: 'If you''re a web developer, you''ll work with JavaScript when building
  dynamic and interactive web applications. One common task that you''ll need to perform
  is getting the current URL of a web page.

  In this article, you will learn how to get the curren...'
---

Si vous êtes un développeur web, vous travaillerez avec JavaScript lors de la création d'applications web dynamiques et interactives. Une tâche courante que vous devrez effectuer consiste à obtenir l'URL actuelle d'une page web.

Dans cet article, vous apprendrez comment obtenir l'URL actuelle en utilisant l'objet Location de JavaScript. Je vous montrerai quelques exemples ainsi que quelques bonnes pratiques.

## Comment utiliser l'objet Location

L'objet Location est un objet JavaScript intégré qui fournit des informations sur l'URL actuelle d'une page web. Il contient diverses propriétés permettant d'accéder et de modifier différentes parties d'une URL.

Pour accéder à l'objet Location, vous pouvez utiliser la propriété `window.location`. Cela retourne l'objet Location pour la page web actuelle. Cet objet contient de nombreuses données, telles que l'URL, le chemin, l'origine, l'hôte, les données de recherche, et plus encore.

Par exemple :

```json
{
  "ancestorOrigins": {
    "0": "https://codepen.io"
  },
  "href": "https://cdpn.io/cpe/boomboom/index.html?editors=0012&key=index.html-f1981af8-7dc2-f8b6-669a-8980d4a8d02a",
  "origin": "https://cdpn.io",
  "protocol": "https:",
  "host": "cdpn.io",
  "hostname": "cdpn.io",
  "port": "",
  "pathname": "/cpe/boomboom/index.html",
  "search": "?editors=0012&key=index.html-f1981af8-7dc2-f8b6-669a-8980d4a8d02a",
  "hash": ""
}
```

## Comment accéder à l'URL actuelle avec JavaScript

Un cas d'utilisation courant de l'objet Location est d'obtenir l'URL actuelle d'une page web. Vous pouvez le faire en accédant à la propriété `href` de l'objet Location.

La propriété `href` contient l'URL complète de la page web actuelle :

```js
const currentUrl = window.location.href;
console.log(currentUrl);
```

Cela enregistrera l'URL actuelle de la page web dans la console.

## Comment analyser l'URL actuelle avec JavaScript

En plus d'obtenir l'URL actuelle, vous devrez peut-être l'analyser pour en extraire des parties spécifiques. Par exemple, vous souhaiterez peut-être extraire le protocole, l'hôte ou le chemin de l'URL.

Pour analyser l'URL actuelle, vous pouvez utiliser les différentes propriétés de l'objet Location. Par exemple, vous pouvez utiliser la propriété `protocol` pour obtenir le protocole de l'URL actuelle :

```js
const protocol = window.location.protocol;
console.log(protocol);
```

Cela enregistrera le protocole de l'URL actuelle (par exemple, "http:" ou "https:") dans la console.

D'autres propriétés de l'objet Location que vous pouvez utiliser pour extraire des parties de l'URL actuelle incluent `host`, `hostname`, `port`, `pathname`, `search` et `hash`.

```js
const host = window.location.host;
const pathname = window.location.pathname;
const search = window.location.search;
const hash = window.location.hash;
```

En utilisant ces propriétés, vous pouvez extraire diverses parties de l'URL actuelle.

## Comment mettre à jour l'URL actuelle avec JavaScript

En plus d'obtenir et d'analyser l'URL actuelle, vous devrez peut-être la mettre à jour. Par exemple, vous devrez peut-être rediriger l'utilisateur vers une URL différente ou modifier dynamiquement l'URL actuelle.

Pour mettre à jour l'URL actuelle, vous pouvez utiliser les différentes méthodes de l'objet Location. Par exemple, vous pouvez utiliser la méthode `replace()` pour remplacer l'URL actuelle par une nouvelle URL :

```js
const newUrl = "https://example.com/new-page.html";
window.location.replace(newUrl);
```

Cela remplacera l'URL actuelle par la nouvelle, redirigeant l'utilisateur vers la nouvelle page.

## Bonnes pratiques lors de l'utilisation de l'objet Location

Lors de l'utilisation de l'objet Location, il existe certaines bonnes pratiques que vous devriez suivre pour éviter les pièges potentiels. Par exemple, vous devriez toujours vérifier si l'objet Location est disponible avant de l'utiliser.

```js
if (window.location) {
  // Accéder ou modifier l'objet Location
}
```

Vous devriez également être prudent lorsque vous modifiez l'URL actuelle, car cela peut affecter l'expérience de navigation de l'utilisateur. Par exemple, vous devriez éviter de modifier le protocole, l'hôte ou le port de l'URL, sauf si cela est absolument nécessaire.

## Conclusion

Dans cet article, vous avez appris comment obtenir l'URL actuelle d'une page web en utilisant l'objet Location de JavaScript. En comprenant comment travailler avec l'objet Location, vous pouvez créer des applications web plus dynamiques et interactives qui offrent une meilleure expérience utilisateur.

Merci d'avoir lu cet article, et j'espère que vous l'avez trouvé informatif et utile. Vous pouvez lire cet article sur [comment rafraîchir une page avec JavaScript](https://www.freecodecamp.org/news/javascript-refresh-page-how-to-reload-a-page-in-js/) pour plus d'informations sur le travail avec les URL en JavaScript.

Si vous souhaitez en savoir plus sur JavaScript et le développement web, [parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents) écrits par moi, et consultez également [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant.

Amusez-vous bien en codant !