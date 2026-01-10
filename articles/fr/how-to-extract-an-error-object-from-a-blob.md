---
title: Comment extraire un objet d'erreur d'une réponse d'API Blob en JavaScript
subtitle: ''
author: Olabisi Olaoye
co_authors: []
series: null
date: '2024-03-29T00:34:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-extract-an-error-object-from-a-blob
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/React-form-validation--1-.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
seo_title: Comment extraire un objet d'erreur d'une réponse d'API Blob en JavaScript
seo_desc: "I encountered an issue when I made a GET request in my React project which\
  \ was supposed to return a file I could download. For the file to download properly,\
  \ I had to make the response type a blob. \nBut if an error occurred when the server\
  \ returns a ..."
---

J'ai rencontré un problème lorsque j'ai fait une requête GET dans mon projet React qui était censée retourner un fichier que je pouvais télécharger. Pour que le fichier se télécharge correctement, j'ai dû définir le type de réponse comme un [blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob).

Mais si une erreur se produisait lorsque le serveur retourne un objet JSON, je ne pourrais pas obtenir cet objet car j'avais déjà défini le type de réponse comme un blob. Et si je retire la définition du blob, le fichier serait simplement retourné comme un JSON régulier et pourrait ne pas se télécharger correctement.

Alors, comment faire pour télécharger le blob et récupérer l'objet d'erreur au cas où quelque chose ne se passerait pas bien du côté du serveur ? Heureusement, il existe un moyen d'y parvenir.

Ce guide vous montrera comment conserver un objet JSON à des fins de gestion des erreurs, tout en étant capable de télécharger un fichier depuis un serveur. Nous utiliserons [Axios](https://axios-http.com/), une bibliothèque JavaScript utilisée pour faire des requêtes HTTP, pour effectuer notre appel API.

## Étape 1 : Définir le type de réponse dans l'appel API

Tout d'abord, définissez une fonction qui fait la requête HTTP vers le serveur. Dans ce cas, nous attendons un fichier, donc le verbe HTTP conventionnel serait GET.

Le type de réponse pour les requêtes Axios est JSON par défaut, mais nous voulons le changer en blob comme ceci :

```javascript
import axios from "axios";

const getFileFromServer = () => {
    const res = await axios.get('https://api.some-server.com', {responseType: 'blob'})?.data;
    return res;
}
```

## Étape 2 : Convertir le Blob en texte

Dans l'étape précédente, nous avons pu obtenir notre fichier sous forme de blob facilement. Mais lorsqu'il s'agit d'afficher l'erreur, nous avons besoin qu'elle s'affiche sous forme de JSON.

Tout d'abord, nous devons envelopper la requête dans une instruction [try/catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) pour spécifier ce qui doit se passer si une erreur est levée pendant que la requête est en cours.

```javascript
import axios from "axios";

const getFileFromServer = async () => {
    try {
        const res = await axios.get('https://api.some-server.com', {responseType: 'blob'}).data;
    return res;
    }
    catch (error) {
        let errorResponse = await error.response.data.text();
        const errorObj = JSON.parse(errorResponse);
        console.log(errorObj) // journaliser l'erreur dans la console
    }
}
```

La conversion de type a été effectuée à l'intérieur du bloc `catch`. Tout d'abord, nous avons converti les données de réponse en une chaîne JSON en utilisant la méthode `text()` de l'API [Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) de JavaScript.

Enfin, nous avons utilisé la méthode `JSON.parse()` pour convertir cette chaîne en JSON réel. De cette manière, nous pouvons accéder à l'objet dans son format prévu tout en étant capable de récupérer le fichier du serveur s'il n'y a pas d'erreur.

Journaliser l'objet d'erreur dans la console donnera quelque chose comme ceci :

```json
{
  "statusCode": 400,
  "message": "Une erreur est survenue"
}
```

## Conclusion

C'est l'un des problèmes que j'ai rencontrés dans la vie réelle, alors j'ai pensé le partager au cas où quelqu'un d'autre le rencontrerait.

Faites-moi part de vos réflexions sur l'article et n'hésitez pas à faire des suggestions que vous pensez pouvoir améliorer ma solution.

Merci d'avoir lu !