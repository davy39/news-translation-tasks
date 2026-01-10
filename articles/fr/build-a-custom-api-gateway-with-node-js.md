---
title: Comment construire une passerelle API personnalisée avec Node.js
subtitle: ''
author: Iroro Chadere
co_authors: []
series: null
date: '2024-03-08T23:16:38.000Z'
originalURL: https://freecodecamp.org/news/build-a-custom-api-gateway-with-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Building-custom-API-gateway.jpg
tags:
- name: api
  slug: api
- name: Microservices
  slug: microservices
- name: node js
  slug: node-js
seo_title: Comment construire une passerelle API personnalisée avec Node.js
seo_desc: "In the era of microservices, where applications are divided into smaller,\
  \ independently deployable services, managing and securing the communication between\
  \ these services becomes crucial. This is where an API gateway comes into play.\
  \ \nAn API gateway..."
---

À l'ère des [microservices](https://www.brightsidecodes.com/blog/understanding-microservices-and-api-gateway), où les applications sont divisées en services plus petits et déployables indépendamment, la gestion et la sécurisation de la communication entre ces services deviennent cruciales. C'est là qu'intervient une passerelle API. 

Une passerelle API sert de point d'entrée central pour toutes les requêtes des clients. Elle fournit diverses fonctionnalités telles que le routage, l'équilibrage de charge, l'authentification et la limitation de débit.

Dans cet article, nous explorerons comment vous pouvez construire une passerelle API personnalisée en utilisant Node.js.

### Voici ce que nous allons couvrir:

1. [Qu'est-ce qu'une passerelle API ?](#heading-quest-ce-quune-passerelle-api)
2. [Sécurité dans les passerelles API](#heading-securite-dans-les-passerelles-api)
3. [Comment construire une passerelle API personnalisée avec Node.js](#heading-comment-construire-une-passerelle-api-personnalisee-avec-nodejs)
4. [Conclusion](#heading-conclusion)

### Prérequis

Ce guide pour débutants devrait être relativement facile à suivre. Mais pour le comprendre pleinement et en tirer le meilleur parti, une connaissance de base de [Node.js](https://nodejs.org/) telle que l'installation, la configuration et le démarrage d'un serveur est essentielle. 

Sans plus tarder, plongeons-nous dans le sujet !

## Qu'est-ce qu'une passerelle API ?

Les passerelles API agissent comme des intermédiaires entre les clients et les services back-end dans une architecture de microservices. Elles abstraient la complexité des services sous-jacents et exposent une API unifiée aux clients. 

En consolidant plusieurs points de terminaison de services en un seul point d'entrée, les passerelles API simplifient le code côté client et améliorent la scalabilité et les performances globales du système.

Comparé à d'autres solutions populaires de passerelles API comme Kong, AWS API Gateway et Tyke, la construction d'une passerelle API personnalisée en utilisant Node.js offre une flexibilité et des options de personnalisation adaptées à vos exigences spécifiques de projet.

Pour mieux comprendre ce qu'est une passerelle API, je vous recommande de [consulter cet article](https://www.brightsidecodes.com/blog/understanding-microservices-and-api-gateway) si vous ne l'avez pas déjà fait.

### Avantages de l'utilisation d'une passerelle API :

* **Amélioration de la scalabilité et des performances grâce au routage des requêtes et à l'équilibrage de charge** : Les passerelles API facilitent le routage des requêtes et l'équilibrage de charge, distribuant le trafic entrant sur plusieurs services back-end pour assurer des performances et une scalabilité optimales.
* **Simplification du code côté client en fournissant un point de terminaison API unifié** : Avec un point de terminaison API unifié fourni par la passerelle API, les clients peuvent interagir de manière transparente avec plusieurs services, réduisant la complexité et améliorant la maintenabilité du code côté client.
* **Sécurité renforcée** : Les passerelles API offrent des fonctionnalités de sécurité robustes telles que l'authentification, l'autorisation et la limitation de débit, protégeant les services back-end contre les accès non autorisés et les potentielles menaces de sécurité.

## Sécurité dans les passerelles API

La sécurité est primordiale dans le développement logiciel moderne, surtout lorsqu'il s'agit de systèmes distribués et de microservices. Les passerelles API jouent un rôle crucial dans l'application de mesures de sécurité pour protéger les données sensibles et prévenir les accès non autorisés aux API.

Les fonctionnalités de sécurité courantes mises en œuvre dans les passerelles API incluent :

* Authentification JWT : Vérification de l'identité des clients à l'aide de JSON Web Tokens (JWT) pour assurer une communication sécurisée entre les clients et les services back-end.
* Intégration OAuth2 : Fourniture de mécanismes de contrôle d'accès et d'autorisation sécurisés à l'aide de protocoles OAuth2 pour authentifier et autoriser les requêtes des clients.
* Terminaison SSL : Chiffrement du trafic entre les clients et la passerelle API à l'aide de protocoles SSL/TLS pour protéger les données en transit contre l'écoute et la falsification.

Maintenant, vous devriez avoir une vue d'ensemble générale de ce qu'est une passerelle API et de son importance.

Dans la section suivante, nous allons nous plonger dans le processus de construction d'une passerelle API personnalisée en utilisant Node.js. Je vais démontrer comment implémenter des fonctionnalités de sécurité en utilisant le package http-proxy-middleware.

## Comment construire une passerelle API personnalisée avec Node.js

Comme je l'ai déjà discuté, nous allons utiliser Node.js pour ce tutoriel. À mon avis, Node.js est de loin le framework web le plus facile et le plus populaire. Tout le monde peut apprendre à l'utiliser.

Pour ce guide, je suppose que vous connaissez déjà ou avez une compréhension de base de Node.js et de la façon de configurer un serveur.

### Getting Started – Installations et Configuration

Pour commencer, créez un nouveau dossier appelé « API-gateway » entièrement en dehors de votre code front-end ou back-end. Une fois le dossier créé, ouvrez-le dans votre terminal et exécutez `npm init -y`. Cela configurera ``npm`` et vous serez prêt à démarrer !

Nous allons utiliser quelques packages NPM, et il est préférable de les installer maintenant. Le plus important est ``http-proxy-middleware``. Ce middleware ou package est ce qui routera nos requêtes d'un point de terminaison (www.domain.com/auth) à chaque point de terminaison correspondant (www.externaldomain.com/v1/bla/auth, www.externaldomain.com/v1/bla/projects) tel que défini dans nos microservices.

Pour installer le http-proxy-middleware, exécutez simplement `npm i http-proxy-middleware` dans le dossier racine de votre terminal. Si c'est installé, vous êtes prêt à partir.

Ensuite, nous aurons besoin des packages restants. Exécutez simplement ``npm install express cors helmet morgan`` dans votre terminal dans le dossier racine de la passerelle API. 


La commande ci-dessus installe les éléments suivants :

* **Express** : notre bibliothèque Node.js pour créer notre serveur et exécuter notre code
* **Cors** : middleware pour gérer et contrôler les requêtes cross-origin
* **Helmet** : un autre middleware pour sécuriser nos en-têtes de réponse HTTP
* **Morgan** : un outil de journalisation que nous pouvons utiliser pour suivre les logs de succès et d'erreurs

Enfin, installez Nodemon. C'est un outil qui démarre votre serveur chaque fois que vous enregistrez un fichier en utilisant `npm install --save-dev nodemon`.


Maintenant, allez dans votre fichier package.js et mettez à jour la section scripts. Elle devrait ressembler à ceci :

```
"scripts": {
 "start": "node index.js",
 "dev": "nodemon index.js",
 "test": "echo \"Error: no test specified\" && exit 1"
},
```

Pour enfin commencer à tester les choses, créez un nouveau fichier appelé index.js dans ce même dossier api-gateway.  
  
Si vous avez tout fait correctement, vous devriez avoir les fichiers suivants :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-from-2024-03-04-12-50-56.png)
_Une image montrant la structure des fichiers de notre base de code_

### Mettre tout ensemble

Une bonne pratique de codage consiste à décomposer les choses autant que possible en composants plus petits. 

Mais pour ce guide, nous allons enfreindre cette règle et mettre tout le code dans ce seul fichier `index.js` que nous avons créé à partir des étapes ci-dessus. Nous allons procéder de cette manière car avoir trop de fichiers et une configuration trop complexe ici pourrait être déroutant, surtout pendant que vous apprenez comment les choses fonctionnent.

Tout d'abord, ouvrez le fichier index.js que vous avez créé et collez le code suivant dedans :

```
const express = require("express");
const cors = require("cors");
const helmet = require("helmet");
const morgan = require("morgan");
const { createProxyMiddleware } = require("http-proxy-middleware");

```

Dans le code ci-dessus, nous importons simplement les packages. 

Ensuite, initialisez et configurez les packages importés comme ceci :

```
// Créer une instance de l'application Express
const app = express();


// Configuration du middleware
app.use(cors()); // Activer CORS
app.use(helmet()); // Ajouter des en-têtes de sécurité
app.use(morgan("combined")); // Journaliser les requêtes HTTP
app.disable("x-powered-by"); // Masquer les informations du serveur Express
```

Rappelez-vous qu'une passerelle API est une source unique de vérité pour tous vos services ou URLs externes. Cela signifie que vous devez avoir d'autres services ou URLs vers lesquels vous souhaitez transférer les requêtes. 

En supposant que vous avez déjà vos autres services en cours d'exécution, soit localement soit déployés, passons à la section suivante du code.


```
// Définir les routes et les microservices correspondants
const services = [
 {
   route: "/auth",
   target: "https://your-deployed-service.herokuapp.com/auth",
 },
 {
   route: "/users",
   target: "https://your-deployed-service.herokuapp.com/users/",
 },
 {
   route: "/chats",
   target: "https://your-deployed-service.herokuapp.com/chats/",
 },
 {
   route: "/payment",
   target: "https://your-deployed-service.herokuapp.com/payment/",
 },
 // Ajoutez plus de services si nécessaire, soit déployés soit localement.
];

```

Dans le code ci-dessus, nous avons créé une liste de services et défini des objets contenant chacun des routes (où nous ferons des requêtes) et des cibles (où les requêtes seront transférées).  
  
Assurez-vous de mettre à jour les routes et les cibles pour répondre à vos besoins.

Devinez ce qui vient ensuite...

Eh bien, il est enfin temps de créer la logique simple pour transférer les requêtes vers notre URL cible, en configurant une limite de débit et des délais d'attente. Et savez-vous ce qui vient ensuite ? Un exemple de code, lol :

```
// Définir les constantes de limite de débit
const rateLimit = 20; // Nombre maximum de requêtes par minute
const interval = 60 * 1000; // Fenêtre de temps en millisecondes (1 minute)

// Objet pour stocker les comptes de requêtes pour chaque adresse IP
const requestCounts = {};

// Réinitialiser le compte de requêtes pour chaque adresse IP toutes les 'interval' millisecondes
setInterval(() => {
  Object.keys(requestCounts).forEach((ip) => {
    requestCounts[ip] = 0; // Réinitialiser le compte de requêtes pour chaque adresse IP
  });
}, interval);

// Fonction middleware pour la limitation de débit et la gestion des délais d'attente
function rateLimitAndTimeout(req, res, next) {
  const ip = req.ip; // Obtenir l'adresse IP du client

  // Mettre à jour le compte de requêtes pour l'IP actuelle
  requestCounts[ip] = (requestCounts[ip] || 0) + 1;

  // Vérifier si le compte de requêtes dépasse la limite de débit
  if (requestCounts[ip] > rateLimit) {
    // Répondre avec un code d'état 429 Too Many Requests
    return res.status(429).json({
      code: 429,
      status: "Error",
      message: "Limite de débit dépassée.",
      data: null,
    });
  }

  // Définir un délai d'attente pour chaque requête (exemple : 10 secondes)
  req.setTimeout(15000, () => {
    // Gérer l'erreur de délai d'attente
    res.status(504).json({
      code: 504,
      status: "Error",
      message: "Délai d'attente de la passerelle.",
      data: null,
    });
    req.abort(); // Annuler la requête
  });

  next(); // Passer au middleware suivant
}

// Appliquer le middleware de limite de débit et de délai d'attente au proxy
app.use(rateLimitAndTimeout);

// Configurer le middleware proxy pour chaque microservice
services.forEach(({ route, target }) => {
  // Options de proxy
  const proxyOptions = {
    target,
    changeOrigin: true,
    pathRewrite: {
      [`^${route}`]: "",
    },
  };

  // Appliquer le middleware de limitation de débit et de délai d'attente avant le proxy
  app.use(route, rateLimitAndTimeout, createProxyMiddleware(proxyOptions));
});
```

J'ai ajouté un tas de bons commentaires de code pour vous aider à comprendre ce qui se passe.

Félicitations si vous savez ce qui se passe ci-dessus. Si ce n'est pas le cas, vous pouvez lire à propos du package [http-proxy-middleware](https://www.npmjs.com/package/http-proxy-middleware).

Mais soyons sérieux, nous n'avons pas encore terminé. 

Le code ci-dessus ne fonctionnera toujours pas, car nous avons besoin d'une dernière chose : écrire une fonction pour démarrer le serveur lorsqu'elle est appelée.

Ajoutez l'exemple de code suivant à la fin du fichier index.js après tout le code que vous avez ajouté ci-dessus :


```
// Définir le port pour le serveur Express
const PORT = process.env.PORT || 5000;


// Démarrer le serveur Express
app.listen(PORT, () => {
 console.log(`La passerelle est en cours d'exécution sur le port ${PORT}`);
});

```

Avec cela, lorsque vous exécutez `npm run dev`, cela démarre votre serveur et vous devriez pouvoir tester cela en utilisant des outils comme Postman ou tout autre outil que vous utilisez pour tester les API.

Maintenant, avant de partir, essayons d'ajouter un peu d'épices ! 

Ajoutons une fonction 404 pour suivre et retourner un joli message 404 à un utilisateur s'il navigue ou envoie une requête à une URL qui n'existe pas. 

Donc, dans notre tableau de services défini ci-dessus, nous n'avons aucune route définie pour `products`. Cela signifie que si un utilisateur envoie une requête à `/product`, il obtiendrait une erreur serveur car la requête ne peut pas être traitée. 

Pour informer l'utilisateur que l'URL est introuvable, nous pouvons ajouter l'exemple de code suivant juste avant de définir le port et de l'écouter :


```
// Gestionnaire pour la route non trouvée
app.use((_req, res) => {
 res.status(404).json({
   code: 404,
   status: "Error",
   message: "Route non trouvée.",
   data: null,
 });
});


// Définir le port pour le serveur Express
```

## Conclusion
Construire une passerelle API personnalisée avec Node.js offre aux développeurs une solution flexible et personnalisable pour gérer, router et sécuriser les appels API dans une architecture de microservices. 

Tout au long de ce tutoriel, nous avons exploré les concepts fondamentaux des passerelles API, y compris leur rôle dans la simplification du code côté client, l'amélioration de la scalabilité et des performances, et le renforcement de la sécurité.

En tirant parti de la puissance de Node.js et du package `http-proxy-middleware`, nous avons démontré comment implémenter une passerelle API de base qui transmet les requêtes à plusieurs services back-end. Nous avons également enrichi notre passerelle avec des fonctionnalités essentielles telles que la limitation de débit et les délais d'attente pour assurer une communication fiable et sécurisée entre les clients et les services.

Alors que vous continuez à explorer le monde des microservices et des systèmes distribués, rappelez-vous que les passerelles API jouent un rôle crucial dans l'orchestration de la communication et l'application de mesures de sécurité. Que vous choisissiez de construire une solution personnalisée ou d'utiliser des plateformes de passerelles existantes, la compréhension des principes et des meilleures pratiques décrits dans ce tutoriel vous permettra d'architecturer des systèmes robustes et scalables.

Je vous encourage à expérimenter avec les exemples de code fournis et à explorer d'autres options de personnalisation pour répondre aux exigences uniques de votre projet. Le code source complet de ce tutoriel peut être trouvé ici : https://github.com/irorochad/api-gateway.

Merci de m'avoir accompagné dans ce voyage pour explorer les intrications des passerelles API avec Node.js. Bon codage !