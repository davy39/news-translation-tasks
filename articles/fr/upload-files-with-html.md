---
title: Comment télécharger des fichiers avec HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-04T20:17:14.000Z'
originalURL: https://freecodecamp.org/news/upload-files-with-html
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/HTML-Blog-Cover-1.png
tags:
- name: HTML
  slug: html
seo_title: Comment télécharger des fichiers avec HTML
seo_desc: 'By Austin Gil

  When building applications with HTML, you may eventually come to a point where you
  need to allow users to upload files. Surprisingly, it''s not quite as straightforward
  as you might assume.

  In this post, we''ll look at all things you need...'
---

Par Austin Gil

Lors de la création d'applications avec HTML, vous pourriez éventuellement arriver à un point où vous devez permettre aux utilisateurs de télécharger des fichiers. Étonnamment, ce n'est pas aussi simple que vous pourriez le penser.

Dans cet article, nous examinerons tout ce dont vous avez besoin pour prendre en charge les téléchargements de fichiers en HTML.

## Comment accéder aux fichiers

La toute première étape consiste à accéder à un fichier à télécharger. Malheureusement, ou plutôt heureusement, les navigateurs ne peuvent pas accéder à nos systèmes de fichiers. Si c'était le cas, ce serait une préoccupation majeure en matière de sécurité.

Des travaux sont en cours sur l'[API d'accès au système de fichiers](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API), mais elle est expérimentale et aura un accès limité, alors faisons semblant qu'elle n'existe pas.

L'accès à un fichier nécessite une interaction de l'utilisateur, ce qui signifie que nous avons besoin de quelque chose dans l'interface utilisateur avec laquelle l'utilisateur peut interagir. Heureusement, il existe l'[élément input avec un attribut de type `file`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file).

```html
<input type="file" />
```

Seul, un input de fichier n'est pas très utile. Il permet à un utilisateur de sélectionner un fichier depuis son appareil, mais c'est à peu près tout.

Pour envoyer réellement le fichier à un serveur, nous devons faire une [requête HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP), ce qui signifie que nous avons besoin d'un `[<form>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)`. Nous placerons l'input de fichier à l'intérieur avec un `[<button>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)` pour soumettre le formulaire.

L'input aura également besoin d'un `[<label>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)` pour le rendre [accessible](https://austingil.com/category/accessibility/) pour les technologies d'assistance, d'un attribut `[id](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)` pour l'associer à l'étiquette, et d'un attribut `name` afin d'inclure ses données avec la requête HTTP.

```html
<form>
  <label for="file">Fichier</label>
  <input id="file" type="file" />
  <button>Télécharger</button>
</form>
```

Cela a l'air bien 👍.

Mais cela ne fonctionne pas bien, cependant 👎.

## Comment inclure un corps de requête

Si nous observons l'[onglet réseau](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/network/) lorsque nous soumettons le formulaire, nous pouvons voir qu'il génère une requête [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET), et la charge utile est envoyée sous forme de [chaîne de requête](https://en.wikipedia.org/wiki/Query_string) qui ressemble à ceci : "`?name=filename.txt`". Il s'agit essentiellement d'une paire clé-valeur, la clé étant le `name` de l'input et la valeur étant le nom du fichier.

Cela est envoyé sous forme de chaîne.

Ce n'est pas tout à fait ce que nous recherchons ici.

Nous ne pouvons pas réellement envoyer un fichier en utilisant une requête GET car vous ne pouvez pas mettre un fichier dans les paramètres de la chaîne de requête. Nous devons mettre le fichier dans le [corps de la requête](https://developer.mozilla.org/en-US/docs/Web/API/Request/body).

Pour ce faire, nous devons envoyer une requête [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST), ce que nous pouvons faire en changeant l'attribut `[method](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/method)` du formulaire en `"post"`.

```html
<form method="post">
  <label for="file">Fichier</label>
  <input id="file" name="file" type="file" />
  <button>Télécharger</button>
</form>
```

Maintenant, si nous explorons cette requête, nous pouvons voir que nous faisons une requête POST. Nous pouvons également voir que la requête contient une charge utile avec les données du formulaire. Malheureusement, les données sont toujours une simple paire clé-valeur avec le `name` de l'input et le nom du fichier.

## Comment définir le Content-Type

Nous n'envoyons toujours pas réellement le fichier, et la raison a à voir avec le "[`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)" de la requête.

Par défaut, lorsqu'un formulaire est soumis, la requête est envoyée avec un `Content-Type` de `application/x-www-form-urlencoded`. Et malheureusement, nous ne pouvons pas envoyer les informations binaires du fichier en tant que [données encodées en URL](https://en.wikipedia.org/wiki/URL_encoding).

Afin d'envoyer le contenu du fichier en tant que [données binaires](https://en.wikipedia.org/wiki/Binary_data), nous devons changer le `Content-Type` de la requête en `multipart/form-data`. Et pour ce faire, nous pouvons définir l'attribut `[enctype](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/enctype)` du formulaire.

```html
<form method="post" enctype="multipart/form-data">
  <label for="file">Fichier</label>
  <input id="file" name="file" type="file" />
  <button>Télécharger</button>
</form>
```

Maintenant, si nous soumettons le formulaire une fois de plus, nous pouvons voir que la requête utilise la méthode POST et que le `Content-Type` est défini sur `multipart/form-data`. Dans les navigateurs Chromium, vous ne verrez plus la charge utile de la requête, mais vous pouvez la voir dans les outils de développement de Firefox sous l'onglet Params de la requête.

Nous l'avons fait !

## Récapitulatif

Avec tout cela en place, nous pouvons télécharger des fichiers en utilisant HTML. Pour réitérer, l'envoi de fichiers avec HTML nécessite trois choses :

1. Créer un input avec le `type` de fichier pour accéder au système de fichiers.
2. Utiliser un formulaire avec `method="post"` pour inclure un corps dans la requête.
3. Définir le `Content-Type` de la requête sur `multipart/form-data` en utilisant l'attribut `enctype`.

Merci beaucoup d'avoir lu. Si vous avez aimé cet article et souhaitez me soutenir, les meilleures façons de le faire sont de [le partager](https://twitter.com/share?via=heyAustinGil), [vous inscrire à ma newsletter](https://austingil.com/newsletter/), et [me suivre sur Twitter](https://twitter.com/heyAustinGil).