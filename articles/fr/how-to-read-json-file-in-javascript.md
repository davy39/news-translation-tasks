---
title: Comment lire un fichier JSON en JavaScript – Lecture de JSON en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-02T21:35:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-read-json-file-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template--5-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: json
  slug: json
seo_title: Comment lire un fichier JSON en JavaScript – Lecture de JSON en JS
seo_desc: 'When fetching data from external sources or servers, you need to make sure
  that the data returned is in JSON format. Then you can consume the data within your
  application.

  In some situations, when you''re working locally or when you upload the data fi...'
---

Lorsque vous récupérez des données à partir de sources externes ou de serveurs, vous devez vous assurer que les données retournées sont au format JSON. Ensuite, vous pouvez consommer les données dans votre application.

Dans certaines situations, lorsque vous travaillez localement ou lorsque vous téléchargez le fichier de données sur un serveur, nous pourrions vouloir lire ces données JSON à partir d'un fichier.

Nous allons apprendre comment faire cela dans ce tutoriel.

## Comment lire un fichier JSON en JavaScript avec l'API Fetch

Une méthode standard que nous pouvons utiliser pour lire un fichier JSON (qu'il s'agisse d'un fichier local ou téléchargé sur un serveur) est l'API Fetch. Elle utilise la même syntaxe pour les deux. La seule différence serait l'URL.

Par exemple, supposons que nous avons un fichier local dans le dossier de notre projet nommé `data.json` qui contient les données JSON suivantes :

```json
<!--./data.JSON-->

{
    "id": 1,
    "title": "Hello World",
    "completed": false
}
```

Nous pouvons maintenant lire ce fichier en JavaScript en utilisant la méthode de l'API Fetch :

```js
<!--./index.js-->

fetch('./data.json')
    .then((response) => response.json())
    .then((json) => console.log(json));
```

Dans l'exemple ci-dessus, nous avons pu lire un fichier JSON local. Mais malheureusement, lorsque nous exécutons cela dans un navigateur, nous pourrions obtenir l'erreur CORS suivante parce que notre fichier n'est pas sur un serveur :

![](https://paper-attachments.dropbox.com/s_9630F87AB23B79DCD31DCDD0E14D2C6C4A3007934D2E561803A41CF5C1FE0085_1659464623693_image.png align="left")

Pour corriger cela, nous devons nous assurer que notre fichier JSON est sur un serveur local ou distant. Si nous utilisons le serveur Live sur notre IDE, nous n'aurons pas cette erreur. Mais lorsque nous chargeons notre fichier directement, nous obtiendrons cette erreur.

Comme je l'ai dit précédemment, supposons que nous avons ce fichier JSON sur un serveur distant et que nous essayons de lire ce fichier en JavaScript. La même syntaxe fonctionnera :

```js
<!--./index.js-->

fetch('https://server.com/data.json')
    .then((response) => response.json())
    .then((json) => console.log(json));
```

L'API Fetch est la méthode préférable à utiliser lorsque nous voulons lire un fichier JSON soit à partir d'un serveur externe ou d'un fichier local dans notre fichier JavaScript.

## Comment lire un fichier JSON en JavaScript avec l'instruction Import

Une autre méthode que nous pouvons utiliser en dehors de la requête HTTP est l'instruction import. Cette méthode a quelques complications, mais nous allons les aborder toutes.

Tout comme dans la section précédente, supposons que nous avons notre fichier JSON qui contient des données utilisateur, telles que `user.json` :

```json
<!--./user.JSON-->

{
    "id": 1,
    "name": "John Doe",
    "age": 12
}
```

Nous pouvons lire ces données JSON en JavaScript en utilisant l'instruction import de cette manière :

```js
<!---./index.js-->

import data from './data.json';
console.log(data);
```

Malheureusement, cela générera une erreur disant que nous ne pouvons pas utiliser l'instruction import en dehors d'un module. Il s'agit d'une erreur standard lorsque nous essayons d'utiliser l'instruction `import` dans un fichier JavaScript régulier, surtout pour les développeurs qui sont nouveaux en JavaScript.

Pour corriger cela, nous pouvons ajouter la balise script `type="module"` dans notre fichier HTML où nous avons référencé le fichier JavaScript, comme ceci :

```HTML
<html lang="en">
    // ...
    <body>
        <script type="module" src="./index.js"></script>
    </body>
</html>
```

Lorsque nous faisons cela, nous obtiendrons toujours une autre erreur :

![](https://paper-attachments.dropbox.com/s_9630F87AB23B79DCD31DCDD0E14D2C6C4A3007934D2E561803A41CF5C1FE0085_1659465574774_image.png align="left")

Pour corriger cette erreur, nous devons ajouter le type de fichier JSON à l'instruction import, et ensuite nous pourrons lire notre fichier JSON en JavaScript :

```bash
import data from './data.json' assert { type: 'json' };
console.log(data);
```

Cela fonctionne parfaitement tant que nous exécutons nos fichiers sur un serveur local ou distant. Mais supposons que nous exécutons cela localement – alors nous obtiendrions l'erreur CORS.

![](https://paper-attachments.dropbox.com/s_9630F87AB23B79DCD31DCDD0E14D2C6C4A3007934D2E561803A41CF5C1FE0085_1659464623693_image.png align="left")

## Conclusion

Dans cet article, nous avons appris comment lire un fichier JSON en JavaScript et les erreurs possibles que nous pourrions rencontrer en utilisant chaque méthode.

Il est préférable d'utiliser la méthode de l'API Fetch lorsque vous voulez faire une requête HTTP. Par exemple, supposons que nous récupérons des données à partir d'un fichier JSON simulé que nous allons éventuellement extraire d'une API.

Encore, dans une situation où nous n'avons pas besoin d'utiliser une requête HTTP, nous pourrions utiliser l'instruction import. Nous pouvons utiliser l'instruction import lorsque nous utilisons une bibliothèque comme React, Vue, et ainsi de suite qui a à voir avec les modules. Cela signifie que nous n'aurons pas besoin d'ajouter le type de module, et aussi, nous n'aurons pas besoin d'ajouter le type de fichier.

Aucune des méthodes ne nécessite d'installer un package ou d'utiliser une bibliothèque car elles sont intégrées. Le choix de la méthode à utiliser dépend entièrement de vous.

Mais un conseil rapide qui différencie ces méthodes est que l'API Fetch lit un fichier JSON en JavaScript en envoyant une requête HTTP, tandis que l'instruction import ne nécessite aucune requête HTTP mais fonctionne plutôt comme toutes les autres importations que nous faisons.

Embarquez pour un voyage d'apprentissage ! [Parcourez 200+ articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.