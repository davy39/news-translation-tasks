---
title: L'en-tête Access-Control-Allow-Origin expliqué – Avec un exemple CORS
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-07-17T07:18:00.000Z'
originalURL: https://freecodecamp.org/news/access-control-allow-origin-header-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99aa740569d1a4ca210e.jpg
tags:
- name: CORS
  slug: cors
- name: JavaScript
  slug: javascript
seo_title: L'en-tête Access-Control-Allow-Origin expliqué – Avec un exemple CORS
seo_desc: 'Often times when calling an API, you may see an error in your console that
  looks like this:


  Access to fetch at ''http://somesite.com'' from origin ''http://yoursite.com'' has
  been blocked by CORS policy: The ''Access-Control-Allow-Origin'' header has a va...'
---

Souvent, lorsque vous appelez une API, vous pouvez voir une erreur dans votre console qui ressemble à ceci :
```

L'accès à fetch à 'http://somesite.com' depuis l'origine 'http://yoursite.com' a été bloqué par la politique CORS : L'en-tête 'Access-Control-Allow-Origin' a une valeur qui n'est pas égale à l'origine fournie

```

Dans cet article, nous allons apprendre pourquoi cette erreur se produit et comment vous pouvez la corriger. 


## Qu'est-ce que l'en-tête `Access-Control-Allow-Origin` ?
`Access-Control-Allow-Origin` est un en-tête CORS. CORS, ou Cross Origin Resource Sharing, est un mécanisme pour les navigateurs permettant à un site s'exécutant à l'origine A de demander des ressources à l'origine B. 

L'origine n'est pas seulement le nom d'hôte, mais une combinaison de port, de nom d'hôte et de schéma, comme par exemple - `http://mysite.example.com:8080/`


Voici un exemple où cela entre en action :
1. J'ai une origine A : `http://mysite.com` et je veux obtenir des ressources de l'origine B : `http://yoursite.com`. 
2. Pour protéger votre sécurité, le navigateur ne me permettra pas d'accéder aux ressources de yoursite.com et bloquera ma demande. 
3. Pour permettre à l'origine A d'accéder à vos ressources, votre origine B devra informer le navigateur qu'il est acceptable pour moi d'obtenir des ressources de votre origine.


Voici un exemple du Mozilla Developer Network qui explique cela très bien :


![Image](https://www.freecodecamp.org/news/content/images/2020/07/CORS_principle.png)

Avec l'aide de CORS, les navigateurs permettent aux origines de partager des ressources entre elles. 

Il existe [plusieurs en-têtes](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#The_HTTP_response_headers) qui permettent le partage de ressources entre origines, mais le principal est `Access-Control-Allow-Origin`. Cela indique au navigateur quelles origines sont autorisées à recevoir des demandes de ce serveur. 


## Qui doit définir `Access-Control-Allow-Origin` ?

Pour comprendre qui doit définir cet en-tête, considérons ce scénario : Vous naviguez sur un site web utilisé pour visualiser et écouter des chansons. Le site tente de se connecter à votre banque en arrière-plan de manière malveillante. 

Alors, qui a la capacité ultime d'empêcher ce site malveillant de voler vos données bancaires ? La banque ! Donc, la banque devra protéger ses ressources en définissant l'en-tête `Access-Control-Allow-Origin` dans le cadre de la réponse.

Rappelez-vous simplement : l'origine responsable de la fourniture des ressources devra définir cet en-tête.


## Comment utiliser et quand passer cet en-tête
Voici un exemple de valeurs que vous pouvez définir : 

1. `Access-Control-Allow-Origin : *` : Autorise toute origine.
2. `Access-Control-Allow-Origin : http://mysite.com` : Autorise les demandes uniquement de mysite.com.


## Voir cela en action

Examinons un exemple. Vous pouvez consulter ce code [sur mon dépôt GitHub](https://github.com/shrutikapoor08/blogs/tree/master/code-examples/CORS). 

Nous allons construire un serveur sur l'origine A `http://localhost:8000` qui enverra une chaîne de `Hello` à un point de terminaison `api`. Nous allons appeler ce point de terminaison en créant un client sur l'origine B `http://localhost:3000` puis utiliser fetch pour demander la ressource. Nous nous attendons à voir la chaîne `Hello` passée par l'origine A dans la console du navigateur de l'origine B. 


Supposons que nous avons une origine sur `http://localhost:8000` qui fournit cette ressource sur le point de terminaison `/api`. Le serveur envoie une réponse avec l'en-tête `Access-Control-Allow-Origin`.

```
const express = require("express");

const app = express();
const port = process.env.SERVER_PORT || 8000;

// Ajouter les en-têtes Access Control Allow Origin
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "https://yoursite.com");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});

app.get("/api", (req, res) => {
  res.json("Hello");
});

app.listen(port, () => console.log(`Écoute sur le port ${port}`));

```

Côté client, vous pouvez appeler ce point de terminaison en appelant `fetch` comme ceci : 

```
fetch('http://localhost:8000/api')
.then(res => res.json())
.then(res => console.log(res));

```
Ouvrez maintenant la console de votre navigateur pour voir le résultat. 
Puisque l'en-tête est actuellement défini pour autoriser l'accès uniquement depuis `https://yoursite.com`, le navigateur bloquera l'accès à la ressource et vous verrez une erreur dans votre console.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CORS-access-denied.png)

Maintenant, pour corriger cela, changez les en-têtes comme suit :

```
 res.setHeader("Access-Control-Allow-Origin", "*");

```

Vérifiez la console de votre navigateur et vous pourrez maintenant voir la chaîne `Hello`.

### Intéressé par plus de tutoriels et de JSBytes de ma part ? Inscrivez-vous à ma newsletter.