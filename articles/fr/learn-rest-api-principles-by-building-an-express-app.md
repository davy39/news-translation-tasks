---
title: Apprendre les principes de l'API REST en construisant une application Express
subtitle: ''
author: Ikegah Oliver
co_authors: []
series: null
date: '2025-04-21T15:20:53.838Z'
originalURL: https://freecodecamp.org/news/learn-rest-api-principles-by-building-an-express-app
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745003938509/442fd99e-d098-4a5a-98d7-94c4af9a5d55.png
tags:
- name: REST API
  slug: rest-api
- name: Express
  slug: express
- name: Web Development
  slug: web-development
seo_title: Apprendre les principes de l'API REST en construisant une application Express
seo_desc: Web development revolves around communication – communication between browsers
  and servers, as well as frontend applications and backends. At the centre of this
  is the API. And the REST architecture has become a popular way to design APIs that
  are cl...
---

Le développement web tourne autour de la communication – communication entre les navigateurs et les serveurs, ainsi qu'entre les applications frontales et les backends. Au centre de cela se trouve l'API. Et l'architecture REST est devenue une manière populaire de concevoir des API qui sont propres, cohérentes et faciles à utiliser dans le développement web.

REST fonctionne si bien parce qu'il parle le langage natif du web. Il utilise des méthodes HTTP familières comme `GET`, `POST`, `PUT` et `DELETE`, traite les données comme des ressources et suit des conventions claires. Tout cela le rend facile à comprendre, rapide à implémenter et largement soutenu, ce qui explique pourquoi la plupart des API web modernes suivent les principes REST.

Dans cet article, j'explorerai les concepts REST et les principes fondamentaux tout en construisant une simple application Express étape par étape. Vous apprendrez :

* Qu'est-ce que l'architecture REST et quels sont ses avantages dans le développement web ?

* Les principes fondamentaux de REST (sans état, ressources, méthodes HTTP, etc.)

* Comment implémenter ces principes dans une véritable application Express.js

* Les meilleures pratiques pour concevoir des API propres et cohérentes

### Voici ce que nous allons couvrir :

* [Qu'est-ce que REST](#heading-quest-ce-que-rest)

* [Pourquoi utiliser REST ?](#heading-pourquoi-utiliser-rest)

* [Principes fondamentaux de l'architecture REST](#heading-principes-fondamentaux-de-larchitecture-rest)

* [Construire une application Express simple](#heading-construire-une-application-express-simple)

  * [Qu'est-ce qu'Express ?](#heading-quest-ce-quexpress)

  * [Configurer l'application Express](#heading-configurer-lapplication-express)

  * [Construire des ressources RESTful](#heading-construire-des-ressources-restful)

  * [Middlewares](#heading-middlewares)

  * [Tester votre application Express](#heading-tester-votre-application-express)

* [Mauvaises pratiques REST à éviter](#heading-mauvaises-pratiques-rest-a-eviter)

* [Conclusion](#heading-conclusion)

## Qu'est-ce que REST ?

Le transfert d'état représentationnel (REST) est un style de conception d'applications en réseau qui met l'accent sur un modèle de communication client-serveur sans état centré sur les ressources. Pensez-y comme à commander dans un restaurant : chaque fois que vous demandez quelque chose, vous devez dire exactement au serveur ce que vous voulez, et ils ne se souviennent pas de vos commandes précédentes.

Les API RESTful traitent les données comme des ressources, chacune accessible via une adresse web unique (URI). Ensuite, elles exploitent les actions standard définies par les méthodes HTTP – POST pour créer de nouvelles ressources, GET pour les récupérer, PUT pour modifier celles existantes et DELETE pour les supprimer – fournissant une manière cohérente et bien comprise d'interagir avec les données sur Internet.

## Pourquoi utiliser REST ?

Les principes architecturaux REST offrent un ensemble convaincant d'avantages qui contribuent à la construction de services web robustes, évolutifs et maintenables. Voici quelques-uns des principaux avantages qui font de REST un choix privilégié pour le développement web moderne :

* **Simplicité et familiarité** : REST exploite le HTTP standard, qui est déjà bien compris par les développeurs et les infrastructures.

* **Évolutivité** : La nature sans état de REST permet une mise à l'échelle facile des composants client et serveur de manière indépendante.

* **Flexibilité et interopérabilité** : Les API RESTful peuvent être consommées par une grande variété de clients, indépendamment de la pile technologique.

* **Cacheabilité** : La conception de REST supporte les mécanismes de cache, conduisant à des performances améliorées et à une charge serveur réduite.

* **Couplage lâche** : Le client et le serveur sont indépendants, permettant des changements de chaque côté sans nécessairement affecter l'autre.

* **Visibilité et surveillance** : La nature simple des requêtes et réponses HTTP facilite la surveillance et le débogage des interactions.

## Principes fondamentaux de l'architecture REST

REST (Representational State Transfer) est construit sur quelques principes simples qui rendent les API faciles à comprendre et à utiliser. Voici un bref aperçu des principaux :

### Sans état

Chaque requête du client vers le serveur doit contenir toutes les informations nécessaires pour la traiter. Le serveur ne stocke rien sur le client entre les requêtes – pas de session, pas de mémoire des actions précédentes.

**Exemple** : Si un utilisateur envoie `GET /movies/1`, le serveur retourne les données du film sans avoir besoin de savoir si l'utilisateur est connecté ou ce qu'il a demandé auparavant.

Cela rend les API plus faciles à mettre à l'échelle, puisque chaque requête peut être traitée indépendamment.

### Ressources et URIs

Dans REST, tout ce avec quoi vous travaillez est considéré comme une ressource – utilisateurs, produits, etc. Chaque ressource doit être accessible via une URL unique et significative.

**Exemple** :

* `/movies` – une collection de ressources de films

* `/movies/42` – un film spécifique avec l'ID 42

Les ressources sont traitées comme des noms. Les actions sont déterminées par la méthode HTTP utilisée.

### Méthodes HTTP standard

REST tire pleinement parti des méthodes HTTP pour décrire l'action que vous effectuez sur une ressource :

* `GET` – récupérer des données

* `POST` – créer une nouvelle ressource

* `PUT` – mettre à jour ou remplacer une ressource

* `PATCH` – mettre à jour partiellement une ressource

* `DELETE` – supprimer une ressource

**Exemple** : Pour supprimer un film, vous enverriez une requête `DELETE` à `/movies/42`. C'est clair, cohérent et intuitif.

### Interface uniforme

REST impose une structure cohérente pour la communication entre le client et le serveur. Cela signifie que toutes les API REST doivent se comporter de manière similaire, peu importe qui les a construites. Cela inclut :

* Utiliser des URIs pour identifier les ressources

* Utiliser des méthodes HTTP standard

* Représenter les données dans des formats comme JSON ou XML

* Messages auto-descriptifs (par exemple, codes de statut et en-têtes appropriés)

Cette cohérence facilite la compréhension et l'intégration des API RESTful par les développeurs.

### Cacheabilité

Les serveurs doivent étiqueter les réponses comme cacheables (stockées pour être récupérées plus tard) ou non, afin que les clients puissent réutiliser les réponses lorsque cela est approprié. Cela réduit la charge inutile du serveur et améliore les performances.

**Exemple** : Une réponse `GET /movies` peut être mise en cache pendant 5 minutes si les données ne changent pas fréquemment. Cela signifie moins d'appels répétés pour les mêmes informations.

### Séparation client-serveur

Le client (frontend) et le serveur (backend) fonctionnent indépendamment. Le client doit simplement savoir comment communiquer avec l'API – il ne se soucie pas de la manière dont le serveur gère les données, et vice versa.

Cette séparation permet aux équipes de développer et de mettre à l'échelle les systèmes frontend et backend séparément.

Les principes ci-dessus aident à créer des API qui sont évolutives, prévisibles et faciles à utiliser.

## Comment construire une application Express simple

### Qu'est-ce qu'Express ?

Express.js est un framework d'application web Node.js léger et flexible. Construit sur Node.js, il fournit un ensemble robuste de fonctionnalités pour construire des applications web monopage, multipage et hybrides ainsi que des API. Pensez-y comme à une boîte à outils utile qui simplifie le processus de configuration et de gestion des serveurs web et du routage des requêtes.

Dans cet exercice, vous allez construire une application Express qui :

1. Gère une collection simple en mémoire de films comme ressource RESTful

2. Supporte les opérations CRUD de base en utilisant les méthodes HTTP appropriées (GET, POST, PUT, DELETE)

3. Analyse les requêtes JSON entrantes en utilisant un middleware intégré

4. Utilise une fonction middleware personnalisée pour valider l'entrée de film avant de créer ou de mettre à jour des entrées

5. Envoie des réponses claires et significatives basées sur le résultat de chaque requête

À la fin, vous aurez une API fonctionnelle qui suit les principes REST et qui peut être testée en utilisant un outil comme Thunder Client ou Postman.

### Configurer l'application Express

Pour tirer le meilleur parti de cet exercice, il y a quelques outils et concepts avec lesquels vous devriez déjà être familier. Puisque nous nous concentrons sur les principes REST et comment les appliquer en utilisant Express, nous n'approfondirons pas les bases de ces prérequis. Assurez-vous d'être à l'aise avec les éléments suivants :

* Node.js

* Npm

* Extension Thunderclient

* JavaScript de base

Avec cela, commençons.

Ouvrez votre invite de commande et créez un nouveau répertoire (dossier) :

```bash
mkdir express-app
```

Naviguez dans votre nouveau répertoire :

```bash
cd express-app
```

Initialisez un projet npm :

```bash
npm init -y
```

Installez le package Express dans votre projet :

```bash
npm install express
```

Maintenant, ouvrez votre répertoire dans votre éditeur de code avec la commande suivante :

```bash
code .
```

Créez un nouveau fichier, server.js, et configurez votre application Express dans ce fichier :

```javascript
const express = require('express');
const app = express();
app.use(express.json());

app.listen(8000, () => console.log('Server running on port 8000'));
```

Ce snippet ci-dessus configure un serveur Express de base. Il commence par importer la bibliothèque Express que vous avez installée, active l'analyse JSON pour les requêtes entrantes (afin que nous puissions travailler avec les corps de requête), et écoute sur le port 3000. Il est prêt à gérer les routes RESTful comme `GET`, `POST`, `PUT` et `DELETE` alors que nous développons notre API.

Pour démarrer votre serveur, retournez à votre invite de commande et tapez cette commande :

```bash
node server.js
```

Vous devriez voir ceci enregistré dans votre invite de commande :

![Une capture d'écran d'une invite de commande ou d'une fenêtre de terminal. L'invite montre le répertoire actuel comme "C:sersSEResktopest-tutorial>". La commande "node server.js" a été exécutée, et la sortie en dessous indique "Server is running on port 8000".](https://cdn.hashnode.com/res/hashnode/image/upload/v1744840192457/818bc1a4-3e96-4494-9895-d02cf816e3f3.png align="left")

### Construire des ressources RESTful

Avec notre application Express configurée, construisons la ressource `/movies` en utilisant des routes RESTful. Nous traiterons chaque film comme une ressource et utiliserons des méthodes HTTP pour définir ce que nous voulons faire – récupérer, ajouter, mettre à jour ou supprimer des films. Pour simplifier, nous stockerons les films dans un tableau en mémoire.

Voici l'ensemble complet des routes. Ajoutez-le dans votre fichier server.js juste sous votre ligne `app.use(express.json());` :

```javascript
// Base de données en mémoire (à des fins de démonstration)
// Dans une application réelle, vous utiliseriez une base de données comme MongoDB ou PostgreSQL
const movies = [];

// Obtenir tous les films
app.get('/movies', (req, res) => {
  res.json(movies);
  console.log(movies);
});

// Obtenir un film particulier par ID
app.get('/movies/:id', (req, res) => {
  const movie = movies.find(m => m.id === parseInt(req.params.id));
  if (!movie) return res.status(404).send('Film non trouvé');
  res.json(movie);
});

// Ajouter un nouveau film
app.post('/movies', (req, res) => {
  const movie = {
    id: movies.length + 1,
    title: req.body.title,
    genre: req.body.genre,
    year: req.body.year
  };
  movies.push(movie);
  res.status(201).json(movie);
});

// Mettre à jour un film
app.put('/movies/:id', (req, res) => {
  const movie = movies.find(m => m.id === parseInt(req.params.id));
  if (!movie) return res.status(404).send('Film non trouvé');

  movie.title = req.body.title;
  movie.genre = req.body.genre;
  movie.year = req.body.year;

  res.json(movie);
});

// Supprimer un film
app.delete('/movies/:id', (req, res) => {
  const movieIndex = movies.findIndex(m => m.id === parseInt(req.params.id));
  if (movieIndex === -1) return res.status(404).send('Film non trouvé');

  const deletedMovie = movies.splice(movieIndex, 1);
  res.json(deletedMovie);
});
```

Le code ci-dessus définit un ensemble complet de routes RESTful pour gérer une ressource de films en utilisant Express.

Il commence par un tableau en mémoire, `movies`, qui agit comme notre stockage de données temporaire. La route `GET /movies` retourne tous les films, tandis que `GET /movies/:id` recherche un film par son ID en utilisant `Array.find()`, retournant un statut 404 s'il n'est pas trouvé. La route `POST /movies` accepte une entrée JSON, crée un nouveau film avec un ID auto-incrémenté et l'ajoute au tableau, retournant la nouvelle ressource avec un statut `201 Created`.

La route `PUT /movies/:id` gère les mises à jour complètes. Elle trouve d'abord le film, et si trouvé, met à jour son `title`, `genre` et `year` avec les nouvelles valeurs du corps de la requête. La route `DELETE /movies/:id` supprime un film en trouvant son index dans le tableau et en utilisant `splice()`. Si le film n'existe pas, PUT et DELETE retournent tous deux une erreur 404.

Ces routes démontrent l'idempotence – c'est-à-dire, envoyer la même requête PUT ou DELETE plusieurs fois aura le même effet que de l'envoyer une fois, un principe clé de REST. Chaque route retourne également des codes de statut HTTP appropriés et des réponses JSON, suivant de près les conventions REST.

Chaque route suit un principe REST :

* Utilise des noms pour les points de terminaison (`/movies`)

* Utilise des méthodes HTTP standard pour exprimer les actions

* Assure l'idempotence lorsque cela est approprié (PUT, DELETE)

* Retourne des codes de statut et des messages appropriés

Cette structure garde votre API prévisible et facile à utiliser – exactement ce que REST est.

### Middlewares

Dans les API RESTful construites avec des frameworks comme Express, le middleware joue un rôle clé dans le maintien d'une gestion des requêtes propre, modulaire et cohérente.

Les middlewares sont des fonctions qui se situent au milieu du cycle requête-réponse dans une application Express. Lorsqu'un client envoie une requête, les fonctions middleware ont accès aux objets `req` (requête), `res` (réponse) et `next`. Elles peuvent inspecter, modifier ou agir sur la requête avant qu'elle n'atteigne le gestionnaire de route ou même terminer la réponse plus tôt.

Vous avez déjà vu un middleware ici : `app.use(express.json());`. Il s'agit d'un middleware global utilisé pour analyser le JSON. Nous allons créer un middleware personnalisé pour valider l'entrée de nos requêtes POST et PUT.

Ajoutez le code suivant dans votre fichier server.js juste avant vos routes :

```javascript
// Middleware pour une validation simple
const validateMovie = (req, res, next) => {
  if (!req.body.title || !req.body.genre || !req.body.year) {
      return res.status(400).send('Le titre, le genre et l\'année sont requis');
  }
  next();
};
```

Cette fonction middleware, `validateMovie`, effectue une validation de base sur les requêtes entrantes avant qu'elles n'atteignent le gestionnaire de route. Elle vérifie si les champs `title`, `genre` et `year` sont présents dans le corps de la requête. Si l'un de ces champs est manquant, elle répond immédiatement avec un statut `400 Bad Request` et un message d'erreur. Si tous les champs requis sont fournis, elle appelle `next()` pour passer le contrôle au middleware ou à la route suivante. Cela garde la logique de validation séparée et réutilisable, aidant à maintenir des gestionnaires de route propres et RESTful.

Pour utiliser ce middleware, passez-le comme argument dans vos routes POST et PUT, par exemple :

```javascript
app.post('/movies', validateMovie, (req, res) => {
  const movie = {
    id: movies.length + 1,
    title: req.body.title,
    genre: req.body.genre,
    year: req.body.year
  };
  movies.push(movie);
  res.status(201).json(movie);
});
```

### Tester votre application Express

Pour tester les modifications que vous avez apportées, vous devez redémarrer votre serveur. Allez dans votre invite de commande et appuyez sur CTRL + C (pour Windows) ou Command + . (pour MacOS). Entrez la commande de démarrage comme avant pour redémarrer le serveur.

Pour cet exercice, vous allez tester les points de terminaison avec l'extension Thunder Client sur VSCode. Thunder Client est une extension REST API légère pour VSCode. Avec Thunder Client, vous pouvez tester vos routes et points de terminaison REST API directement dans VSCode.

Pour télécharger Thunder Client, cliquez sur l'icône Extension dans la barre des tâches à gauche et recherchez « Thunder Client ». Ensuite, cliquez sur Installer :

![Une capture d'écran de la place de marché des extensions dans Visual Studio Code (VS Code). La barre de recherche en haut contient le texte "Thunder". En dessous de la barre de recherche, une liste d'extensions liées à "Thunder" est affichée. Le premier résultat, "Thunder Client", montre un bouton d'installation. Une flèche rouge pointe vers l'icône Extensions dans la barre d'activités de VS Code à gauche, qui est mise en surbrillance pour indiquer que c'est l'icône à cliquer.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744234771851/a5d7a3e4-384b-47e9-8b2d-47bc45a2007d.png align="left")

Après l'installation, vous verrez l'icône Thunder Client apparaître dans votre barre latérale en dessous de l'icône Extensions. Cliquez dessus, puis appuyez sur Nouvelle Requête pour ouvrir un nouvel onglet. L'onglet de requête s'ouvrira avec une mise en page propre, prête pour vous à envoyer et tester des appels API :

![Une capture d'écran de l'interface Thunder Client dans Visual Studio Code. Un nouvel onglet de requête est ouvert, affichant une requête GET configurée à l'URL "https://www.thunderclient.com/welcome". La méthode HTTP est définie sur "GET" dans un menu déroulant. En dessous de la barre d'URL, des onglets pour "Query", "Headers", "Auth", "Body", "Tests" et "Pre Run" sont visibles, avec "Query" actuellement sélectionné, montrant une section pour "Query Parameters" avec des champs pour "parameter" et "value". En bas, un message indique "Non-Commercial Use" avec un lien pour voir les termes. La barre latérale de gauche montre "THUNDER CLIENT" avec des options comme "New Request", "Activity" et "Collections".](https://cdn.hashnode.com/res/hashnode/image/upload/v1744282644259/dfe4b735-c465-4993-bc46-cce28966deb3.png align="center")

Pour commencer à tester votre API, définissez la méthode de requête (GET, POST, PUT ou DELETE) à partir du menu déroulant et entrez la route appropriée, comme `http://localhost:3000/movies`. Pour les requêtes GET, il suffit de cliquer sur Envoyer et vous devriez voir une réponse, dans ce cas, un tableau vide `[]`. Pour obtenir un film spécifique, vous incluez un ID (par exemple, `/movies/1`).

Pour les requêtes `POST`, `PUT` et `DELETE`, basculez vers l'onglet Body et sélectionnez le format JSON. Ensuite, fournissez les données que vous souhaitez envoyer :

* **POST** `/movies` : Ajoutez un nouveau film avec `{"title": "Titre du film", "genre": "Nom du genre", "year": 0000}`.

* **PUT** `/movies/1` : Mettez à jour un film existant avec la même structure JSON.

* **DELETE** `/movies/1` : Supprimez un film par son ID – aucun corps n'est nécessaire.

Après l'envoi de chaque requête, Thunder Client affichera le corps de la réponse, les en-têtes et le code de statut. Exemple :

![Une capture d'écran de l'interface Thunder Client dans Visual Studio Code, montrant une requête POST réussie. À gauche, les détails de la requête sont visibles : la méthode HTTP est définie sur "POST" avec l'URL "http://localhost:8000/movies". L'onglet "Body" est sélectionné, affichant le contenu JSON : {"title": "Home Alone", "genre": "Comedy", "year": 1999}. À droite, les détails de la réponse indiquent un "Status: 201 Created", "Size: 58 Bytes", et "Time: 5 ms". L'onglet "Response" est sélectionné, montrant la réponse JSON : {"id": 1, "title": "Home Alone", "genre": "Comedy", "year": 1999}.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744840699502/4ea83fbc-7b47-4aea-b8ff-a6e351bf54be.png align="left")

## Mauvaises pratiques REST à éviter

Lors de la construction d'API REST, en plus d'utiliser les bonnes méthodes HTTP, vous devez également considérer éviter les pratiques qui violent les principes fondamentaux de REST. Ces mauvaises pratiques peuvent rendre votre API plus difficile à utiliser, moins prévisible ou même trompeuse.

Voici quelques mauvaises pratiques REST courantes et comment les éviter :

### **Utiliser des verbes dans les points de terminaison**

Évitez les routes comme `/getMovies` ou `/createMovie`. Les API RESTful s'appuient sur les méthodes HTTP pour exprimer les actions, donc utilisez des noms pour les points de terminaison et laissez les méthodes faire le travail – par exemple, utilisez `GET /movies` pour récupérer des films et `POST /movie` pour en créer un.

### **Ignorer les codes de statut HTTP**

Retourner `200 OK` pour chaque réponse, même les erreurs, brise les conventions REST. Utilisez les codes de statut appropriés : `201 Created` pour les POST réussis, `404 Not Found` lorsqu'une ressource n'existe pas, et `400 Bad Request` pour les problèmes de validation. Cela aide les clients à interpréter correctement les réponses.

### **Surcharger un seul point de terminaison**

Évitez d'écrire un seul point de terminaison qui change de comportement en fonction du corps de la requête ou des en-têtes. Chaque route doit clairement correspondre à une ressource et à une méthode, comme `GET /movies/1` pour récupérer, et `DELETE /movies/1` pour supprimer, rendant l'API prévisible et facile à suivre.

### **Ne pas être idempotent là où c'est attendu**

`PUT` et `DELETE` doivent être idempotents, ce qui signifie que des requêtes répétées doivent avoir le même effet. Si l'appel de `DELETE /movies/1` deux fois provoque une erreur ou un comportement inattendu, c'est un signal d'alarme. Concevez vos gestionnaires pour gérer ces cas avec grâce.

### **Exposer la logique interne ou la structure de la base de données**

Ne laissez pas fuir des détails internes comme les noms de tables de la base de données ou la logique de requête dans la nomination de vos routes (`/api/movie_table_data`). Gardez vos URIs propres, abstraites et centrées sur la ressource réelle, comme `/movies`.

Éviter ces pratiques non seulement garde votre API RESTful mais améliore également l'expérience du développeur, la cohérence et la maintenabilité à long terme.

## Conclusion

Vous avez exploré les idées fondamentales derrière REST et les avez mises en pratique en construisant et en testant une véritable API Express. Cette approche pratique devrait aider à combler le fossé entre la théorie et l'application dans le monde réel.

En cours de route, vous avez appris comment REST traite les ressources, comment écrire des routes propres et prévisibles, et pourquoi ces principes comptent lors de la conception d'API qui sont faciles à utiliser et à maintenir.

Voici un bref récapitulatif de ce que vous avez construit et appris :

* Définir ce qu'est REST et pourquoi il est largement utilisé dans le développement web

* Explorer les principes fondamentaux de REST comme l'absence d'état, le routage basé sur les ressources, les méthodes HTTP, les codes de statut et l'idempotence

* Configurer un serveur Express simple pour servir de base à une API RESTful

* Construire un ensemble complet de routes (GET, POST, PUT, DELETE) pour gérer une ressource `movies`

* Utiliser des middlewares pour des tâches comme l'analyse JSON et la validation des entrées

* Tester les routes en utilisant Thunder Client et apprendre à interagir avec chaque méthode HTTP

* Identifier les anti-modèles REST courants et comment les éviter pour une conception plus propre

Pour aller plus loin avec votre API et suivre des pratiques RESTful plus avancées, envisagez :

* Organiser les routes avec Express Router pour garder votre code modulaire

* Ajouter une gestion des erreurs robuste pour retourner des réponses cohérentes et informatives

* Utiliser des outils de journalisation comme `morgan` pour surveiller les requêtes et déboguer plus facilement

* Sécuriser les points de terminaison avec des méthodes d'authentification comme JWT ou des clés API

* Structurer les réponses de manière cohérente, éventuellement avec pagination et filtrage pour des ensembles de données plus grands

* Valider les entrées utilisateur de manière approfondie avec des bibliothèques comme `Joi` ou `express-validator`

Explorez le projet complet sur [GitHub](https://github.com/oliverTwist2/rest-tutorial), passez en revue le code et essayez de l'étendre avec vos propres fonctionnalités. Bon codage !