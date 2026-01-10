---
title: Comment créer un raccourcisseur d'URL dans Deno
subtitle: ''
author: Akash Joshi
co_authors: []
series: null
date: '2020-10-07T15:40:28.000Z'
originalURL: https://freecodecamp.org/news/build-a-url-shortener-in-deno
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9848740569d1a4ca192c.jpg
tags:
- name: Deno
  slug: deno
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Comment créer un raccourcisseur d'URL dans Deno
seo_desc: 'In this article, we’re going to learn the basics of Deno, like how to run
  a program and embrace security.

  Deno is the new JavaScript and TypeScript runtime written in Rust. It offers tight
  security, TypeScript support out-of-the-box, a single executa...'
---

Dans cet article, nous allons apprendre les bases de Deno, comme comment exécuter un programme et adopter la sécurité.

Deno est le nouveau runtime JavaScript et TypeScript écrit en Rust. Il offre une sécurité renforcée, le support de TypeScript dès la sortie de la boîte, un seul exécutable pour le faire fonctionner, et un ensemble de modules standards révisés et audités.

Comme [npm](https://npmjs.com) dans Node.js, les packages dans Deno sont gérés dans un dépôt centralisé de packages appelé [X](https://deno.land/x/). Nous allons utiliser l'une de ces bibliothèques, Oak, pour construire un serveur basé sur une API REST dans Deno.

Après avoir appris les bases en utilisant le package de routage similaire à Express [Oak](https://deno.land/x/oak@v6.3.0), nous allons plonger dans le grand bain de Deno et construire une application complète.

Voici ce que nous allons mettre en place dans cette application :

1. Mapping des codes courts d'URL vers des endpoints en utilisant un fichier de configuration basé sur JSON.

2. Avoir des dates d'expiration attachées à chaque URL afin que ces redirections ne soient valides que pour une période limitée.

## 0. Prérequis

1. Installez Deno depuis [ce lien](https://deno.land/#installation).

2. Assurez-vous de connaître les bases de JavaScript.

Bien que ce ne soit pas vraiment nécessaire pour suivre cet article, vous pouvez regarder la vidéo YouTube ci-dessous pour obtenir une introduction à Deno en format vidéo.

%[https://youtu.be/VQ8Jb7GLHgk]

Alors, commençons. ?

## 1. Comment construire le routeur

Pour écrire le code côté serveur de notre application, nous allons utiliser le module Oak. Il a une syntaxe similaire à Express pour définir les routes de l'API.

Si nous regardons sa [documentation ici](https://deno.land/x/oak), la section "[Basic Usage](https://deno.land/x/oak#basic-usage)" couvre à peu près tous les cas d'utilisation dont nous aurons besoin dans notre routeur. Nous allons donc développer ce code pour construire notre application.

Pour tester ce code, vous pouvez créer un fichier appelé `index.ts` dans un dossier, et copier le code "Basic Usage" dedans.

Pour comprendre comment exécuter des fichiers TypeScript ou JavaScript dans Deno, vous devez d'abord comprendre comment Deno exécute les fichiers.

Vous exécutez un fichier en exécutant la commande `deno run file_name.ts` ou `file_name.js`, suivie d'un ensemble de flags fournissant certaines permissions système à votre application.

Pour tester cela, exécutez le fichier que nous venons de créer, contenant le code "Basic Usage", en utilisant la commande `deno run index.ts`.

Vous verrez que Deno se plaint que vous n'avez pas donné l'accès réseau à votre application. Donc, pour faire cela, vous ajoutez `-allow-net` à la commande d'exécution. La commande ressemblera à `deno run index.ts -allow-net`.

Le routeur écrit dans le code "Basic Usage" ressemble à ceci :

```jsx
router
  .get("/", (context) => {
    context.response.body = "Hello world!";
  })
  .get("/book", (context) => {
    context.response.body = Array.from(books.values());
  })
  .get("/book/:id", (context) => {
    if (context.params && context.params.id && books.has(context.params.id)) {
      context.response.body = books.get(context.params.id);
    }
  });
```

Pour décomposer le code ci-dessus, un objet `router` a d'abord été défini. Ensuite, la fonction `get` est appelée sur le routeur, pour définir les différents endpoints de notre application. La logique respective est définie à l'intérieur des fonctions de rappel.

Par exemple, pour l'endpoint "/", une fonction de rappel qui retourne "Hello World" dans le corps de la réponse a été définie. Nous pouvons garder cet endpoint inchangé pour tester si notre serveur d'application fonctionne en recevant cette réponse.

Nous n'avons pas besoin de l'URL "/book" qui a été définie, donc sa définition peut être supprimée en toute sécurité. À ce stade, votre routeur devrait avoir la structure suivante :

```javascript
router
  .get("/", (context) => {
    context.response.body = "Hello world!";
  })
  .get("/book/:id", (context) => {
    if (context.params && context.params.id && books.has(context.params.id)) {
      context.response.body = books.get(context.params.id);
    }
  });
```

Dans la section suivante, nous allons commencer à construire l'application réelle.

## 2. Comment construire le raccourcisseur d'URL

Maintenant, commençons à construire le raccourcisseur d'URL réel.

Il devrait rediriger vers une destination (`dest`), basée sur un `shortcode`. La redirection ne devrait également être valide que jusqu'à une `expiryDate`, qui peut être fournie au format Année-Mois-Jour.

Sur la base de ces hypothèses, créons le fichier de configuration, nommé `urls.json`. Le format du fichier sera :

```jsx
{
  "shortcode": {
    "dest": "destination_url_string",
    "expiryDate": "YYYY-MM-DD"
  }
}
```

Vous pouvez [consulter le fichier JSON ici](https://github.com/akash-joshi/deno-url-shortener/blob/master/urls.json).

Pour lire ce fichier JSON dans votre code, ajoutez ce qui suit en haut de votre `index.ts` :

```jsx
import { Application, Router } from "<https://deno.land/x/oak/mod.ts>";

const urls = JSON.parse(Deno.readTextFileSync("./urls.json"));

console.log(urls);
```

Maintenant, pour exécuter votre `index.ts`, vous aurez besoin d'un autre flag `--allow-read`, sinon Deno lancera une erreur "read permissions not provided". Votre commande finale devient `deno run --allow-net --allow-read index.ts`.

Après avoir exécuté cette commande, vous verrez le fichier JSON s'afficher dans votre fenêtre de terminal. Cela signifie que votre programme est capable de lire correctement le fichier JSON.

Si nous revenons à l'exemple "Basic Usage" que nous avons vu ci-dessus, la route "/book/:id" est exactement ce dont nous avons besoin.

Au lieu de "/book/:id", nous pouvons utiliser "/shrt/:urlid", où nous obtiendrons les URL individuelles en fonction de l'ID d'URL (`:urlid`).

Remplacez le code existant présent à l'intérieur de la route "/book/:id" par ceci :

```jsx
.get("/shrt/:urlid", (context) => {
    if (context.params && context.params.urlid && urls[context.params.urlid]) {
      context.response.redirect(urls[context.params.urlid].dest);
    } else {
      context.response.body = "404";
    }
  });
```

La condition `if` dans la route fait ce qui suit :

1. Vérifie si des paramètres sont attachés à la route

2. Vérifie si le paramètre `urlid` est dans la liste des paramètres.

3. Vérifie si l'`urlid` correspond à une URL dans notre JSON.

Si cela correspond à tout cela, l'utilisateur est redirigé vers l'URL correcte. Sinon, une réponse 404 sur le corps est retournée.

Pour tester cela, copiez cette route dans `index.ts`. Le routeur ressemblera maintenant à ceci :

```jsx
router
  .get("/", (context) => {
    context.response.body = "Hello world!";
  })
	.get("/shrt/:urlid", (context) => {
	    if (context.params && context.params.urlid && urls[context.params.urlid]) {
	      context.response.redirect(urls[context.params.urlid].dest);
	    } else {
	      context.response.body = "404";
	    }
	  });
```

Et exécutez le fichier en utilisant `deno run --allow-net --allow-read index.ts`.

Si vous avez copié le fichier JSON de l'exemple, et si vous allez sur `http://localhost:8000/shrt/g`, vous serez redirigé vers la page d'accueil de Google.

D'un autre côté, si vous utilisez un code court aléatoire qui ne fonctionne pas dans la configuration de notre URL, il vous amène à la page 404.

Cependant, vous verrez que notre raccourcisseur ne réagit pas en direct aux changements dans le fichier JSON. Pour tester cela, essayez d'ajouter une nouvelle redirection à `urls.json` dans le même format que :

```javascript
"shortcode": {
    "dest": "destination_url_string",
    "expiryDate": "YYYY-MM-DD"
  }
```

La raison à cela est que `urls.json` n'est lu qu'une seule fois au début. Donc, maintenant nous allons ajouter le rechargement en direct à notre serveur.

## 3. Comment ajouter le rechargement en direct

Pour faire en sorte que l'objet `urls` réagisse en direct aux changements dans le fichier JSON, nous déplaçons simplement l'instruction de lecture à l'intérieur de notre route. Cela devrait ressembler à ceci :

```jsx
.get("/shrt/:urlid", (context) => {
  const urls = JSON.parse(Deno.readTextFileSync("./urls.json"));

  if (context.params && context.params.urlid && urls[context.params.urlid]) {
    context.response.redirect(urls[context.params.urlid].dest);
  } else {
    context.response.body = "404";
  }
});
```

Remarquez comment nous avons déplacé l'objet URLs à l'intérieur de notre routeur. Maintenant, dans ce cas, le fichier de configuration est lu chaque fois que cette route est appelée, donc il peut réagir en direct à tout changement fait dans le fichier `urls.json`. Ainsi, même si nous ajoutons ou supprimons d'autres redirections à la volée, notre code réagit à cela.

## 4. Comment ajouter une expiration aux URL

Pour faire expirer nos URL à une certaine date, nous allons utiliser la bibliothèque populaire Moment.js, qui facilite le travail avec les dates.

Heureusement, elle a également été [portée pour Deno](https://deno.land/x/moment). Pour comprendre comment elle fonctionne, consultez sa documentation dans le lien précédent.

Pour l'utiliser dans notre code, importez-la directement via son URL comme ceci :

```jsx
import { Application, Router } from "<https://deno.land/x/oak/mod.ts>";
import { moment } from "<https://deno.land/x/moment/moment.ts>";

const router = new Router();
```

Pour vérifier la date à laquelle l'URL expirera, nous vérifions la clé `expiryDate` sur notre objet `urls`. Cela rendra le code comme ceci :

```jsx
if (context.params && context.params.urlid && urls[context.params.urlid]) {
  if (
    urls[context.params.urlid].expiryDate > moment().format("YYYY-MM-DD")
  ) {
    context.response.redirect(urls[context.params.urlid].dest);
  } else {
    context.response.body = "Lien expiré";
  }
} else {
  context.response.body = "404";
}
```

Dans `moment().format("YYYY-MM-DD")`, nous obtenons la date et l'heure actuelles en utilisant `moment()`. Nous pouvons la convertir au format "YYYY-MM-DD" (Année-Mois-Jour) en utilisant la fonction `.format("YYYY-MM-DD")`.

En la comparant avec notre clé `expiryDate`, nous pouvons vérifier si l'URL a expiré ou non.

C'est tout ! Vous avez construit un raccourcisseur d'URL entièrement fonctionnel dans Deno. Vous pouvez trouver le code final [dans le dépôt GitHub ici](https://github.com/akash-joshi/deno-url-shortener).

Testez-le en définissant `expiryDate` comme la date actuelle et en apportant d'autres modifications à `urls.json` et à notre code.

### Mes réflexions sur Deno

Pour conclure l'article, je vais donner mes réflexions finales sur deno.land.

Bien qu'il soit rafraîchissant de voir un langage côté serveur qui prend en compte la sécurité et supporte TypeScript dès la sortie de la boîte, Deno a encore un long chemin à parcourir avant d'être prêt pour une utilisation dans des systèmes de production.

Par exemple, la compilation TypeScript est encore très lente, avec des temps de compilation ~20 secondes, même pour des programmes simples comme celui que nous venons de développer.

Sur le front de la déclaration d'erreurs, il est encore assez mauvais pour décrire les erreurs. Par exemple, lors de l'intégration du code pour lire `urls.json` dans la fonction elle-même, Deno n'est pas capable de signaler que le flag `-allow-read` n'a pas été défini. Au lieu de cela, il lance simplement une erreur interne de serveur sans une erreur correcte imprimée sur le terminal.

### Et ensuite ?

Vous pouvez améliorer vos compétences Deno ou Typescript en construisant des applications plus complexes comme une [Application de Chat](https://css-tricks.com/build-a-chat-app-using-react-hooks-in-100-lines-of-code/) ou un [Clone de Wikipedia](https://auth0.com/blog/building-a-wikipedia-app-using-react-hooks-and-auth0/).

Vous pouvez également parcourir la documentation Deno sur [deno.land](http://deno.land/) pour vous familiariser davantage avec les bases.

Merci d'avoir lu jusqu'ici et bon codage ? !!

### Liens importants

Deno - https://deno.land  
Deno X (dépôt de packages) - https://deno.land/x/  
Oak (framework REST) - [https://deno.land/x/oak](https://deno.land/x/oak)  
Oak Basic Usage - [https://deno.land/x/oak@v6.3.1#basic-usage](https://deno.land/x/oak@v6.3.1#basic-usage)  
Dépôt GitHub final - [https://github.com/akash-joshi/deno-url-shortener](https://github.com/akash-joshi/deno-url-shortener)