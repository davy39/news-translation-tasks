---
title: Les meilleures façons de se connecter au serveur en utilisant Angular CLI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-02T12:22:22.000Z'
originalURL: https://freecodecamp.org/news/the-best-ways-to-connect-to-the-server-using-angular-cli-b0c6b699716c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s64f5zH_kuv8HAoSCLYYhA.jpeg
tags:
- name: Angular
  slug: angularjs
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Les meilleures façons de se connecter au serveur en utilisant Angular CLI
seo_desc: 'By Moshe Vilner

  Everybody who has used Angular CLI knows that it is a powerful tool which can take
  a front-end development job to a completely different level. It has all the common
  tasks like live reload, typescript transpiling, minification, and mo...'
---

Par Moshe Vilner

Tout le monde qui a utilisé [Angular CLI](https://cli.angular.io/) sait que c'est un outil puissant qui peut élever un travail de développement front-end à un niveau complètement différent. Il possède toutes les tâches courantes comme le rechargement en direct, la transpilation TypeScript, la minification, et plus encore. Et tout cela est préconfiguré et prêt à être utilisé avec une simple commande :

```
ng build, ng serve, ng test.
```

Mais il y a une tâche (et une très importante) qui doit être configurée une fois que l'application est prête à commencer à afficher des données provenant du serveur...

Oui, peu importe à quel point le framework Angular est génial, et à quel point ses composants sont rapides et performants — à la fin, le but d'une SPA (single page application) est d'interagir avec le serveur via des requêtes HTTP.

Et voici le premier obstacle qui apparaît devant chaque débutant avec Angular CLI : le projet Angular s'exécute sur son propre serveur (qui s'exécute par défaut sur [http://localhost:4200](http://localhost:4200)). Par conséquent, les requêtes vers le serveur API sont **cross-domain**, et, comme vous le savez peut-être, la sécurité du navigateur web interdit l'exécution de requêtes cross-domain.

### Approche #1 : proxy

Bien sûr, les personnes derrière Angular CLI ont prévu ce problème et ont même construit une option spéciale pour exécuter un projet Angular en utilisant une configuration de proxy :

```
ng serve --proxy-config proxy.conf.json
```

Qu'est-ce qu'un proxy, pourriez-vous demander ? Eh bien, les navigateurs ne vous permettent pas de faire des requêtes cross-domain, mais les serveurs, si. Utiliser l'option proxy signifie que vous dites au serveur d'Angular CLI de gérer la requête envoyée depuis Angular et de la renvoyer depuis le serveur de développement. De cette façon, celui qui « parle » avec le serveur de l'API est le serveur d'Angular CLI.

La configuration du proxy nécessite l'ajout du fichier **_proxy.conf.json_** au projet. Il s'agit d'un fichier JSON avec quelques paramètres de base. Voici un exemple du contenu de **_proxy.conf_** :

```
{  "/api/*": {    "target": "http://localhost:3000",    "secure": false,    "pathRewrite": {"^/api" : ""}  }}
```

Ce code signifie que toutes les requêtes commençant par **api/** seront renvoyées vers [**http://localhost:3000**](http://localhost:3000) (qui est l'adresse du serveur API).

### Approche #2 : CORS

La sécurité du navigateur ne vous permet pas de faire des requêtes cross-domain à moins que l'en-tête `Control-Allow-Origin` n'existe dans la réponse du serveur. Une fois que vous avez configuré votre serveur API pour « répondre » avec cet en-tête, vous pouvez récupérer et envoyer des données depuis un domaine différent.

Cette technique est appelée Cross Origin Resource Sharing, ou CORS. La plupart des serveurs et frameworks serveurs courants comme [Express](https://expressjs.com/) de Node.js, ou [Java Spring Boot](https://projects.spring.io/spring-boot/) peuvent être facilement configurés pour activer le CORS.

Voici un exemple de code qui configure le serveur Node.js Express pour utiliser le CORS :

```
const cors = require('cors'); //<-- nécessite l'installation de 'cors' (npm i cors --save)
const express = require('express');
const app = express();
app.use(cors()); //<-- C'est tout, pas besoin de plus de code !
```

Notez que lors de l'utilisation du CORS, avant chaque envoi de requêtes HTTP, une requête OPTIONS (à la même URL) sera envoyée pour vérifier si le protocole **CORS** est compris. Cette « double requête » peut affecter vos performances.

![Image](https://cdn-media-1.freecodecamp.org/images/3PLfIx18PwpP6fjgwMSgKP4wlTA3ya9kc6YK)

### Approche de production

D'accord, votre projet Angular « parle » en douceur avec le serveur, recevant et envoyant des données dans l'environnement de développement. Mais le moment du déploiement est enfin arrivé, et vous avez besoin que votre belle et performante application Angular soit hébergée quelque part (loin de Papa Angular CLI). Vous êtes donc à nouveau confronté au même problème : comment la faire se connecter au serveur.

Seulement maintenant, il y a une grande différence : dans l'environnement de production (après avoir exécuté la commande `ng build`), l'application Angular n'est plus qu'un ensemble de fichiers HTML et JavaScript.

En fait, la décision de la manière d'héberger l'application sur le serveur de production est une décision architecturale, et l'architecture est bien au-delà du cadre de cet article. Mais il y a une option que je vous recommande de considérer.

### Servir des fichiers statiques depuis le serveur de l'API

Oui, vous pouvez héberger votre projet Angular (une fois qu'il ne contient que des fichiers HTML et JavaScript) sur le même serveur où les données (API) sont servies.

L'un des avantages de cette stratégie est que vous ne rencontrez plus aucun problème de « cross-domain », puisque le client et l'API sont en fait sur le même serveur !

Bien sûr, cette approche nécessite que le serveur de l'API soit correctement configuré.

Voici le code qui expose le répertoire « public » où les fichiers Angular peuvent être hébergés lors de l'utilisation du serveur Node Express :

```
app.use(express.static('public'));  //<-- répertoire public qui contient tous les fichiers Angular
```

Notez que dans ce cas, la manière dont votre application accède à l'API dans l'environnement de développement sera différente de la manière dont l'API y accède en production. Ainsi, vous devrez peut-être utiliser différentes URLs HTTP dans différents environnements (comme **api/users/1** en développement et **users/1** en production). Vous pouvez utiliser l'option d'environnement d'Angular CLI pour y parvenir :

```
// users.service.ts
```

```
const URL = 'users';
return this.http.get(`${environment.baseUrl}/${URL}`);
...
```

```
// exemple de fichier environment.ts :
export const environment = {
  production: false,
  baseUrl: 'api',
//<-- préfixe 'API/' nécessaire pour la configuration du proxy
};
```

```
// exemple de fichier environment.prod.ts :
export const environment = {
  production: true,
  baseUrl: '', //<-- pas de préfixe 'API/' nécessaire
};
```

### Conclusion

Angular CLI est sans aucun doute un outil très puissant et robuste. Il facilite notre vie en tant que développeurs front-end de nombreuses manières. Mais il nécessite également que vous preniez une décision architecturale concernant la connexion au serveur de l'API. Par conséquent, vous devez avoir une compréhension claire des différentes façons dont la communication client-serveur peut être établie.

Cet article liste deux approches pour gérer ce problème dans l'environnement de développement et donne également une recommandation sur l'architecture de production. Essayez de jouer avec diverses compilations et voyez laquelle vous semble la plus pratique pour vous et votre équipe.

Amusez-vous et faites-moi savoir comment cela se passe !