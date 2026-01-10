---
title: Erreur 429 – Code HTTP "Trop de requêtes" expliqué
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-28T15:45:26.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-429-too-many-requests-http-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/429.png
tags:
- name: beginner
  slug: beginner
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: http
  slug: http
seo_title: Erreur 429 – Code HTTP "Trop de requêtes" expliqué
seo_desc: 'Whether you are a web developer or you are a regular internet user, you
  might have encountered a 429 error. It means that the website can''t handle the
  number of requests being sent to it.

  For a developer, this error can be hard to resolve because, on...'
---

Que vous soyez un développeur web ou un simple utilisateur d'internet, vous avez peut-être rencontré une erreur 429. Cela signifie que le site web ne peut pas gérer le nombre de requêtes qui lui sont envoyées.

Pour un développeur, cette erreur peut être difficile à résoudre car, dans de nombreux cas, elle n'indique pas ce qu'il faut faire pour la corriger.
![deve-429](https://www.freecodecamp.org/news/content/images/2022/06/deve-429.png)

Mais si vous surfez sur le net en tant qu'utilisateur et que vous rencontrez cette erreur, il pourrait y avoir un indice vous indiquant quoi faire.
![429-clinet](https://www.freecodecamp.org/news/content/images/2022/06/429-clinet.png)

Dans ce cas, vous devriez attendre un peu avant de faire une autre requête. Pour des raisons de sécurité, la période d'attente peut ne pas être spécifiée. Mais si le site privilégie l'expérience utilisateur, il vous indiquera combien de temps attendre avant de faire une autre requête.

Dans cet article, je vais expliquer ce que signifie l'erreur 429 et comment un développeur pourrait l'avoir implémentée. Je vais également montrer ce que vous pouvez faire pour la résoudre en tant qu'utilisateur d'internet.

## Qu'est-ce que l'erreur 429 ?

L'erreur 429 est un code de statut HTTP. Elle vous indique lorsque l'utilisation d'une ressource internet a dépassé le nombre de requêtes qu'elle peut envoyer dans un laps de temps donné.

Cette erreur peut vous être présentée sous une autre forme comme :
- Erreur 429
- 429 Trop de requêtes
- 429 (Trop de requêtes)

Tout dépend de la manière dont l'administrateur responsable de la ressource internet la personnalise.

Dans la petite application que j'ai construite pour vous montrer comment la limitation de débit est implémentée dans une application Express, voici comment j'ai personnalisé l'erreur :
![custom429](https://www.freecodecamp.org/news/content/images/2022/06/custom429.png)

Avec cette erreur, les administrateurs responsables d'un site web ou d'une ressource internet vous disent qu'ils n'ont pas assez de ressources pour gérer le nombre de requêtes que vous envoyez. Cela s'appelle la "limitation de débit".

## Qu'est-ce qui provoque l'erreur 429 ?

La cause la plus courante de l'erreur 429 est de ne pas avoir assez de ressources pour gérer autant de requêtes simultanées.

Par exemple, si cette erreur s'affiche sur un serveur d'hébergement, cela pourrait signifier que le forfait que vous utilisez a une limite pour le nombre de requêtes que vous pouvez envoyer.

Et si l'erreur apparaît lors de l'envoi d'une requête API, cela signifie que vous avez dépassé le nombre de requêtes que vous pouvez faire pendant une certaine période.

De plus, si un utilisateur essaie d'accéder à une page sur un site web trop souvent, le serveur de ce site web pourrait déclencher une fonctionnalité de limitation de débit implémentée dans celui-ci. C'est donc une bonne mesure de sécurité à mettre en place afin de prévenir les attaques de pirates informatiques.

Par exemple, voici comment vous pouvez implémenter la limitation de débit dans une application Express en utilisant le [package express-rate-limit](https://www.npmjs.com/package/express-rate-limit) :

```js
// Importation des dépendances
const express = require("express");
const rateLimit = require("express-rate-limit");

const app = express();

// Port
const port = 4000;

const limiter = rateLimit({
  windowMs: 5 * 60 * 1000,
  max: 5, // Limite chaque IP à 5 requêtes par 15 minutes
  message:
    `<h1 style='display:flex; align-items:center; justify-content:center; height:100vh'>
     429 - Trop de requêtes <br> Réessayez plus tard !
    </h1>`,
});

// Appliquer à toutes les requêtes
app.use(limiter);

app.get("/", limiter, (req, res) => res.send("Hello World!"));

app.listen(port, () => console.log(`App listening on port ${port}!`));

```

Et lorsque la limite est dépassée pour le nombre de secondes spécifié, ce message est affiché à l'utilisateur :
![custom429](https://www.freecodecamp.org/news/content/images/2022/06/custom429.png)

## Ce que vous pouvez faire pour résoudre l'erreur 429

En tant qu'utilisateur d'internet, vous devriez attendre un peu avant de faire une autre requête. Mais si l'erreur persiste, vous devriez contacter l'administrateur du site web.

Si vous êtes un administrateur web, vous devriez réduire le nombre de requêtes que vous faites dans le temps spécifié (si applicable). Si vous contrôlez vous-même la limite, vous devriez l'augmenter pour une période particulière.

Si le site web que vous gérez est un site WordPress, l'un de vos plugins ou thèmes pourrait être à l'origine de l'erreur 429. Vous devriez désactiver les plugins et thèmes de votre site un par un pour voir lequel en est la cause.

Si l'erreur est liée à l'hébergement, vous devriez contacter le service client de votre fournisseur d'hébergement.

## Conclusion

Aucun administrateur de site web ne souhaite que son serveur soit surchargé ou plante. Donc, d'un point de vue technique, l'erreur 429 n'est pas une erreur. C'est la manière qu'a le serveur de vous dire qu'il n'a pas assez de ressources pour gérer le grand nombre de requêtes que vous faites.

Merci d'avoir lu.