---
title: JavaScript document.ready() – Exemple de document prêt en JS et jQuery
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-27T21:03:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-document-ready-jquery-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/joan-gamell-ZS67i1HLllo-unsplash.jpg
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
seo_title: JavaScript document.ready() – Exemple de document prêt en JS et jQuery
seo_desc: "When working with JavaScript and the Document Object Model (DOM), you might\
  \ want your script to run only when the DOM has loaded. \nYou can do this using\
  \ the $(document).ready() method in jQuery, or the DOMContentLoaded event in vanilla\
  \ JavaScript.\nIn..."
---

Lorsque vous travaillez avec JavaScript et le Document Object Model (DOM), vous pouvez vouloir que votre script s'exécute uniquement lorsque le DOM est chargé. 

Vous pouvez faire cela en utilisant la méthode `$(document).ready()` dans jQuery, ou l'événement `DOMContentLoaded` en JavaScript vanilla.

Dans cet article, vous apprendrez comment faire en sorte que votre code JavaScript s'exécute uniquement lorsque le DOM est chargé en utilisant jQuery et JavaScript vanilla.

## Comment utiliser la méthode `$(document).ready()` dans jQuery

Avant que JavaScript ne s'exécute dans le navigateur, il attend que le contenu du document soit chargé. Cela inclut les feuilles de style, les images, etc.

Par convention, placer l'élément script juste avant la balise de fermeture body fait attendre le script que le reste du document soit chargé avant de s'exécuter. 

Nous pouvons également rendre ce processus plus rapide dans jQuery en utilisant la méthode `$(document).ready()`. La méthode `$(document).ready()` attend uniquement que le DOM soit chargé, elle n'attend pas les feuilles de style, les images et les iframes. 

Voici un exemple :

```javascript
$(document).ready(function () {
  console.log("Bonjour le monde !");
});
```

Dans le code ci-dessus, la méthode `$(document).ready()` ne s'exécutera qu'après le chargement du DOM. Vous ne verrez donc "Bonjour le monde !" dans la console qu'après le début de l'exécution de la méthode `$(document).ready()`. 

En résumé, vous pouvez écrire tout votre code jQuery à l'intérieur de la méthode `$(document).ready()`. Ainsi, votre code attendra que le DOM soit chargé avant de s'exécuter. 

## Comment utiliser l'événement `DOMContentLoaded` en JavaScript

Tout comme la méthode `$(document).ready()` de jQuery, l'événement `DOMContentLoaded` se déclenche une fois que le DOM est chargé – il n'attend pas les feuilles de style et les images. 

Voici comment utiliser l'événement `DOMContentLoaded` :

```javascript
document.addEventListener("DOMContentLoaded", () => {
  console.log("Bonjour le monde !");
});
```

Une fois le DOM chargé, l'événement `DOMContentLoaded` le détectera et s'exécutera.

Vous devriez utiliser l'événement `DOMContentLoaded` lorsque :

* Vous avez certaines fonctionnalités dans votre page web qui doivent se déclencher immédiatement sans attendre le reste du contenu de la page.
* Vous avez une balise script placée dans l'élément head.

## Résumé

Dans cet article, nous avons parlé de la méthode `$(document).ready()` dans jQuery, et de l'événement `DOMContentLoaded` en JavaScript vanilla.

Nous les utilisons pour exécuter du code JavaScript lorsque le DOM est chargé. 

L'aspect intéressant de ces fonctionnalités est qu'elles permettent au code JavaScript de s'exécuter sans attendre que les images et les feuilles de style soient complètement chargées dans une page web. 

Bon codage !