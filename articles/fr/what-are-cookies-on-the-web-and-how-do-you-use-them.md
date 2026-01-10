---
title: Qu'est-ce que les Cookies sur le Web et Comment les Utiliser ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-cookies-on-the-web-and-how-do-you-use-them
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ce9740569d1a4ca34d9.jpg
tags:
- name: Productivity
  slug: productivity
- name: toothbrush
  slug: toothbrush
- name: web performance
  slug: web-performance
seo_title: Qu'est-ce que les Cookies sur le Web et Comment les Utiliser ?
seo_desc: 'Manipulating Cookies

  Getting or setting cookies is a straightforward operation that can be achieved by
  accessing the cookie property on the browser’s document object.

  Let''s say you find an amazing and informative recipe website to cook a fun meal
  for...'
---

## **Manipuler les Cookies**

Obtenir ou définir des cookies est une opération simple qui peut être réalisée en accédant à la propriété cookie de l'objet document du navigateur.

Imaginons que vous trouviez un site web de recettes incroyable et informatif pour cuisiner un repas amusant pour vos invités, mais il est dans une langue étrangère. Heureusement, vous pouvez changer la langue sur le site web en utilisant un menu déroulant.

Quelques jours plus tard, vous visitez à nouveau le même site pour préparer un plat pour votre mère, mais maintenant vous voyez le site web dans votre langue maternelle par défaut.

Comment cela s'est-il produit ? Le site web se souvient de la langue que vous avez sélectionnée lors de votre dernière visite et la stocke sous la forme d'un **cookie**. Maintenant, il sélectionne automatiquement votre langue préférée en lisant ce cookie.

`userLanguage:french`

Les cookies sont utilisés pour stocker des données sous la forme de paires `name:value` côté client. Ils permettent à un site web de stocker des informations spécifiques à l'utilisateur sur le navigateur pour une utilisation ultérieure. Les informations stockées pourraient être `sessionID`, `userCountry`, `visitorLanguage`, etc.

Une autre façon de stocker les données côté client est `localstorage`.

### **Définir un Cookie**

Un cookie peut être défini en utilisant la syntaxe ci-dessous. Mais l'utilisation d'une bibliothèque, comme celle mentionnée à la fin, est fortement recommandée pour faciliter le développement pour tout le monde.

Lors de la définition du cookie, vous pouvez également définir la date d'expiration. Si vous omettez cela, les cookies sont effacés lorsque le navigateur est fermé.

**Gardez à l'esprit** qu'un **cookie défini par un domaine particulier ne peut être lu que par ce domaine et ses sous-domaines uniquement.**

```javascript
// Utilisation de vanilla javascript
document.cookie = 'userLanguage=french; expires=Sun, 2 Dec 2017 23:56:11 UTC; path=/';

// Utilisation de la bibliothèque JS cookie
Cookies.set('userLanguage', 'french', { expires: 7, path: '/' });
```

*Le cookie ci-dessus expire dans 7 jours.*

### **Obtenir un Cookie**

```javascript
// Utilisation de vanilla javascript
console.log(document.cookie)

// => "_ga=GA1.2.1266762736.1473341790; userLanguage=french"

// Utilisation de la bibliothèque JS cookie
Cookies.get('userLanguage');

// => "french"
```

### **Supprimer un Cookie**

Pour supprimer un cookie, définissez la date d'expiration à une date passée.

```javascript
// Utilisation de vanilla javascript
document.cookie = 'userLanguage; expires=Thu, 01 Jan 1970 00:00:01 GMT; path=/';

// Utilisation de la bibliothèque JS cookie
Cookies.remove('userLanguage');
```

*Si vous vous retrouvez à manipuler souvent des cookies dans votre projet, utilisez une bibliothèque comme celle-ci [JS Cookie](https://github.com/js-cookie/js-cookie) et économisez-vous beaucoup de temps.*