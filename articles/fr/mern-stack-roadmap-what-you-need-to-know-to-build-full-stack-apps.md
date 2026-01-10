---
title: Guide MERN Stack – Comment apprendre MERN et devenir développeur Full-Stack
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2024-01-04T00:57:45.000Z'
originalURL: https://freecodecamp.org/news/mern-stack-roadmap-what-you-need-to-know-to-build-full-stack-apps
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Copy-of-mern-stack-hotel-booking-website--1-.png
tags:
- name: Express
  slug: express
- name: full stack
  slug: full-stack
- name: MongoDB
  slug: mongodb
- name: node js
  slug: node-js
- name: React
  slug: react
seo_title: Guide MERN Stack – Comment apprendre MERN et devenir développeur Full-Stack
seo_desc: 'Have you ever wondered how modern web applications are built? How you can
  learn and master the technologies that you can use to build your own full stack
  projects from scratch?

  In this handbook, I''m going to introduce you to the MERN stack, a widely-...'
---

Vous vous êtes déjà demandé comment les applications web modernes sont construites ? Comment vous pouvez apprendre et maîtriser les technologies qui vous permettent de construire vos propres projets full stack à partir de zéro ?

Dans ce guide, je vais vous présenter la stack MERN, une pile technologique largement utilisée et adoptée par de nombreuses entreprises leaders. Je vais vous guider à travers 7 étapes essentielles pour commencer à apprendre ces technologies par vous-même.

À la fin de votre lecture, vous aurez une compréhension solide de ce qu'implique la stack MERN, de ses technologies composantes et des diverses ressources pour l'apprendre. Vous aurez également 10 idées de projets que vous pouvez développer et présenter dans votre portfolio.

# Table des matières
1. [Qu'est-ce que la stack MERN ?](#heading-quest-ce-que-la-stack-mern)
2. [Guide de la stack MERN](#heading-guide-de-la-stack-mern)
   - [ÉTAPE 1 : Apprendre la bonne quantité de HTML, JavaScript et CSS](#heading-etape-1-apprendre-la-bonne-quantite-de-html-javascript-et-css)
   - [ÉTAPE 2 : Se familiariser avec React](#heading-etape-2-se-familiariser-avec-react)
   - [ÉTAPE 3 : Comprendre les API REST et le fonctionnement d'un serveur backend avec Express/Node](#heading-etape-3-comprendre-les-api-rest-et-le-fonctionnement-dun-serveur-backend-avec-expressnode)
   - [ÉTAPE 4 : Stocker des données avec MongoDB et Mongoose](#heading-etape-4-stocker-des-donnees-avec-mongodb-et-mongoose)
   - [ÉTAPE 5 : Écrire des tests](#heading-etape-5-ecrire-des-tests)
   - [ÉTAPE 6 : Utiliser Git](#heading-etape-6-utiliser-git)
   - [ÉTAPE 7 : Déploiements](#heading-etape-7-deploiements)
3. [Meilleures ressources pour apprendre la stack MERN](#heading-meilleures-ressources-pour-apprendre-la-stack-mern)
4. [10 idées de projets à essayer aujourd'hui](#heading-10-idees-de-projets-a-essayer-aujourdhui)
5. [Conclusion du voyage MERN stack](#heading-conclusion-du-voyage-mern-stack)

## Qu'est-ce que la stack MERN ?

![Image](https://www.freecodecamp.org/news/content/images/2024/01/MERN-Stack-wallpaper-gigapixel-hq-scale-6_00x.jpg)

La stack MERN, composée de MongoDB, Express.js, React et Node.js, est un ensemble cohérent de technologies utilisé pour construire des applications web efficaces et évolutives.

Sa popularité provient de l'intégration transparente de chaque composant : la gestion flexible des données de MongoDB, la mise en réseau côté serveur efficace d'Express.js, les interfaces utilisateur dynamiques de React et l'environnement d'exécution back-end puissant de Node.js.

Pour les débutants, la stack MERN est un choix judicieux car elle utilise JavaScript dans toutes les couches, simplifiant ainsi la courbe d'apprentissage. Cette uniformité, couplée à une communauté solide et à de nombreuses ressources d'apprentissage, en fait une boîte à outils accessible et pratique pour quiconque souhaite se lancer dans le développement full-stack.

La stack MERN est également largement utilisée dans l'industrie, prisée par les startups et les grandes entreprises pour son efficacité et les applications web modernes et robustes qu'elle peut produire. Cette adoption par l'industrie valide non seulement son efficacité, mais ouvre également de nombreuses opportunités de carrière pour ceux qui maîtrisent ces technologies.

Examinons un bref aperçu de ce à quoi ressemble chaque partie de la stack MERN :

### Frontend (React)

Le frontend d'un site web est comme la salle à manger d'un restaurant. C'est tout ce que vous voyez et avec quoi vous interagissez directement sur un site web – la mise en page, le design, les boutons et le texte.

**Exemple** : Lorsque vous visitez un site web et voyez une belle page d'accueil, interagissez avec des menus ou remplissez des formulaires, vous expérimentez le frontend.

### Backend (Node.js)

Le backend est comme la cuisine d'un restaurant. C'est là que tout le travail en coulisses se fait. Il inclut le serveur, les applications et les bases de données qui travaillent ensemble pour traiter les informations que vous voyez sur le frontend.

**Exemple** : Lorsque vous commandez de la nourriture (soumettez un formulaire sur le site web), la cuisine (backend) traite la commande (les données) et prépare votre repas (les informations ou le service que vous avez demandé).

### Base de données (MongoDB)

Une base de données en développement web est similaire à une réserve ou un stockage de restaurant où tous les ingrédients (données) sont conservés. Elle stocke et gère toutes les informations nécessaires au site web, comme les profils utilisateurs, le contenu et autres données.

**Exemple** : Dans un magasin en ligne, la base de données stocke les informations sur les produits, les prix, les avis des utilisateurs et les détails des clients.

### API REST (Express)

Les API REST sont comme les serveurs dans un restaurant. Ils sont les messagers ou intermédiaires entre le frontend et le backend. Ils prennent les requêtes (comme les commandes) du frontend (client), récupèrent ou mettent à jour les données dans le backend (cuisine), puis retournent les réponses (commandes préparées).

Les termes POST, PUT, DELETE et GET sont des types de requêtes utilisés dans les API REST :

* **POST** : Utilisé pour créer de nouvelles données. Comme passer une nouvelle commande dans le restaurant.
* **PUT** : Utilisé pour mettre à jour des données existantes. Similaire à changer une commande que vous avez déjà passée.
* **DELETE** : Utilisé pour supprimer des données. Comme annuler une commande.
* **GET** : Utilisé pour récupérer des données. Comparable à demander le menu ou vérifier l'état de votre commande.

## Guide de la stack MERN

### ÉTAPE 1 : Apprendre la bonne quantité de HTML, JavaScript et CSS

![Image](https://www.freecodecamp.org/news/content/images/2024/01/b59a78e2ed76c705f3c0dcb300f3f222aefdcd99-gigapixel-hq-scale-6_00x.png)

La stack MERN utilise largement JavaScript, donc c'est une première étape naturelle à apprendre. Dans cette section, vous allez examiner les principales choses que vous utiliserez au quotidien lors de la création d'applications full-stack MERN.

Comprendre JavaScript, c'est comme connaître la bonne quantité d'ingrédients nécessaires pour une recette. Vous n'avez pas besoin de maîtriser tout d'un coup, juste les ingrédients essentiels qui donnent vie à votre plat particulier (ou votre projet web).

### Variables

Les [variables en JavaScript](https://www.freecodecamp.org/news/javascript-variables-beginners-guide/) sont comme des bocaux étiquetés dans votre cuisine. Vous pouvez y stocker des choses (comme des nombres, du texte) et utiliser ces bocaux plus tard dans votre cuisine (ou votre codage).

**Exemple** : Une variable stockant le nom de l'utilisateur, afin de pouvoir l'utiliser plus tard pour dire "Bonjour, [Nom] !"

### Fonctions

Les [fonctions](https://www.freecodecamp.org/news/javascript-functions-and-scope/) sont comme des recettes dans un livre de cuisine. Ce sont des ensembles d'instructions qui effectuent une tâche spécifique. Vous pouvez réutiliser ces recettes chaque fois que vous devez effectuer cette tâche à nouveau.

**Exemple** : Une fonction qui calcule le prix total des articles dans un panier d'achat.

### Objets et tableaux

Les [objets](https://www.freecodecamp.org/news/javascript-basics-strings-arrays-objects/) sont comme des cartes d'information contenant des détails sur quelque chose (comme une carte de contact), et les tableaux sont comme des listes.

**Exemple d'un objet** : Une carte contenant les informations d'un utilisateur (nom, âge, email).
**Exemple d'un tableau** : Une liste de tous les titres de livres préférés de l'utilisateur.

### Instructions if/else, switch

Ce sont des processus de prise de décision. Les [instructions if/else](https://www.freecodecamp.org/news/javascript-if-else-and-if-then-js-conditional-statements/) sont comme choisir quoi porter en fonction de la météo, et les instructions switch sont comme une décision plus complexe, comme choisir quoi cuisiner en fonction de plusieurs ingrédients que vous avez.

**Exemple** : S'il pleut (if), prenez un parapluie (else), prenez des lunettes de soleil.

### Callbacks/Promesses/Async Await

Ce sont des moyens de gérer des tâches qui prennent du temps, comme commander de la nourriture et attendre qu'elle arrive. Les [callbacks](https://www.freecodecamp.org/news/what-is-a-callback-function-in-javascript-js-callbacks-example-tutorial/) sont comme appeler un ami pour faire quelque chose quand il est libre. Les [promesses](https://www.freecodecamp.org/news/javascript-promises-async-await-and-promise-methods/) sont comme votre ami promettant de le faire. [Async-await](https://www.freecodecamp.org/news/javascript-async-await/) est comme faire un plan pour effectuer des tâches les unes après les autres de manière organisée.

**Exemple** : Commander un café (une tâche) et attendre de l'obtenir avant de quitter le café (assurer l'ordre des actions).

### ECMAScript (Chaînes de caractères de modèle, affectation par décomposition, opérateur de propagation, paramètres par défaut, etc.)

Ce sont des outils et raccourcis avancés en JavaScript pour rendre le codage plus facile et plus propre. C'est comme avoir un robot de cuisine dans votre cuisine qui rend le hachage et le mélange plus rapides et plus efficaces.

**Exemple** : Créer automatiquement un message de bienvenue comme "Bonjour, [Nom] !" sans joindre manuellement des mots et des variables.

### TypeScript

[TypeScript](https://www.freecodecamp.org/news/typescript-tutorial-for-react-developers/) est comme JavaScript mais avec plus de règles pour organiser votre code (comme un livre de recettes plus détaillé). Il aide à gérer des projets plus grands en ajoutant des types à votre code, en vous assurant de ne pas mélanger des ingrédients incompatibles. [Ce guide](https://www.freecodecamp.org/news/learn-typescript-beginners-guide/) vous enseigne les bases de TypeScript.

**Exemple** : Spécifier qu'une fonction ne doit prendre qu'un nombre comme entrée, pas de texte ou autre chose.

## ÉTAPE 2 : Se familiariser avec React

![Image](https://www.freecodecamp.org/news/content/images/2024/01/communityIcon_4g1uo0kd87c61.png)

Une fois que vous avez une bonne compréhension de JavaScript, il est temps de vous aventurer dans le monde merveilleux du développement frontend.

React.js est une bibliothèque JavaScript populaire utilisée pour construire des interfaces utilisateur, particulièrement connue pour son efficacité à rendre des pages web dynamiques et interactives. Elle permet aux développeurs de créer de grandes applications web qui peuvent changer de données, sans recharger la page, offrant ainsi une expérience utilisateur plus fluide.

Ci-dessous se trouve une liste des choses courantes que vous voulez connaître lorsque vous travaillez avec React.

### Composants

Pensez aux [composants](https://www.freecodecamp.org/news/how-to-use-react-components/) comme à des blocs LEGO individuels dans un grand modèle LEGO. Chaque bloc est une petite pièce réutilisable que vous pouvez utiliser pour construire différentes parties de votre application web.

**Exemple** : Un composant 'bouton' dans un site web qui peut être utilisé à plusieurs endroits, comme pour soumettre un formulaire ou fermer une fenêtre contextuelle.

### JSX (JavaScript XML)

[JSX](https://www.freecodecamp.org/news/jsx-in-react-introduction/) vous permet d'écrire le code de conception de votre site web (comme HTML) à l'intérieur de votre code JavaScript. C'est comme écrire la recette et les instructions de cuisine au même endroit pour une référence plus facile.

**Exemple** : Écrire un morceau de code JSX qui inclut à la fois JavaScript et des balises de type HTML pour créer un formulaire de connexion utilisateur.

### Props (Propriétés)

Les [props sont comme des instructions](https://www.freecodecamp.org/news/props-in-react/) ou des paramètres que vous passez à vos blocs LEGO (composants) pour leur dire à quoi ils doivent ressembler ou ce qu'ils doivent faire.

**Exemple** : Passer une prop 'couleur' à un composant 'bouton' pour le rendre rouge ou bleu selon la situation.

### État

L'[état](https://www.freecodecamp.org/news/usestate-vs-redux-state-management/) est comme un carnet personnel pour chaque composant, où il garde une trace de ses propres informations, comme si un bouton est cliqué ou non. Voici un cours sur la [gestion de l'état dans React](https://www.freecodecamp.org/news/how-to-manage-state-in-react/).

**Exemple** : Un bouton 'like' qui garde une trace s'il a été cliqué (aimé) ou non.

### Hooks

Les [hooks sont des outils spéciaux dans React](https://www.freecodecamp.org/news/react-hooks-useeffect-usestate-and-usecontext/) qui vous permettent d'ajouter des fonctionnalités comme l'état à vos composants sans avoir besoin d'utiliser des structures de code complexes.

**Exemple** : Utiliser le hook useState pour garder une trace d'un compteur dans un composant.

### Gestion des événements

C'est ainsi que vous dites à un composant de faire quelque chose lorsque l'utilisateur interagit avec lui, comme cliquer sur un bouton ou entrer du texte dans un formulaire.

**Exemple** : Configurer un gestionnaire d'événements de sorte que lorsque l'utilisateur clique sur un bouton 'soumettre', il envoie ses informations au serveur.

### Rendu conditionnel

C'est comme avoir une peinture magique qui peut changer son image en fonction de certaines conditions. Dans React, vous pouvez [afficher différents composants en fonction de différentes conditions](https://www.freecodecamp.org/news/react-conditional-rendering/).

**Exemple** : Afficher un bouton 'connexion' si l'utilisateur n'est pas connecté, et un bouton 'déconnexion' s'il l'est.

### Listes et clés

Les clés sont comme des étiquettes de nom pour les éléments d'une liste. Elles aident React à garder une trace des éléments qui sont nouveaux, modifiés ou supprimés.

**Exemple** : Afficher une liste de messages dans une application de chat, où chaque message a une clé unique.

### API de contexte

L'[API de contexte](https://www.freecodecamp.org/news/context-api-in-react/) est un moyen de partager des informations (comme un paramètre de thème ou des données utilisateur) entre de nombreux composants sans passer les informations à travers chaque niveau manuellement.

**Exemple** : Utiliser l'API de contexte pour partager les informations de l'utilisateur actuellement connecté entre différents composants dans une application web.

### Fragment

Les fragments vous permettent de regrouper plusieurs composants ou éléments ensemble sans ajouter de couches supplémentaires au site web. C'est comme mettre plusieurs pièces LEGO sur une plaque de base sans que la plaque de base fasse partie du modèle final.

**Exemple** : Regrouper une liste d'éléments ensemble dans un menu sans ajouter de wrappers ou de divs supplémentaires autour d'eux.

## ÉTAPE 3 : Comprendre les API REST et le fonctionnement d'un serveur backend avec Express/Node

![Image](https://www.freecodecamp.org/news/content/images/2024/01/express-and-node-opengraph-v1.png)

Chaque interface utilisateur a besoin d'un moyen de stocker et de récupérer les données nécessaires pour faire fonctionner le frontend. C'est là que notre backend intervient.

Dans la stack MERN, le backend est composé de 3 éléments principaux : Express, un serveur Node.js et une base de données. Nous aborderons la base de données bientôt, pour l'instant nous nous concentrerons sur les parties Express/Node de la stack MERN, car elles sont étroitement liées.

Express.js est un framework léger et flexible pour Node.js, conçu pour construire des applications web et des [API REST](https://www.freecodecamp.org/news/build-consume-and-document-a-rest-api/) avec facilité et efficacité. Node.js est un puissant environnement d'exécution JavaScript qui permet le développement d'applications côté serveur évolutives, faisant du duo un choix populaire pour le développement backend.

### Node.js : Fondation pour la construction d'applications web

Pensez à Node.js comme la fondation pour construire un bâtiment moderne. C'est une plateforme qui vous permet de construire des applications web, similaire à la façon dont vous utiliseriez un ensemble d'outils et de matériaux de base pour commencer à construire une maison. Vous pourriez entendre cela être appelé le "backend".

**Exemple** : Construire une application de chat où plusieurs utilisateurs peuvent envoyer des messages en temps réel.

### Express : Simplification du développement d'API REST

Express est un outil d'aide pour Node.js. C'est comme avoir un kit pré-construit qui facilite et accélère la construction de certaines parties de votre maison, fournissant des modèles et des raccourcis pour que vous n'ayez pas à commencer de zéro.

**Exemple** : Utiliser Express pour configurer rapidement des routes pour un site web, comme une route vers une page de contact ou un catalogue de produits.

### Modules et packages : Composants prêts à l'emploi

Dans Node.js, les modules sont comme des composants ou des sections pré-fabriqués d'une maison (comme une unité de salle de bain ou un ensemble de cuisine) que vous pouvez simplement choisir et ajouter à votre projet de construction.

**Exemple** : Ajouter un module 'date-time' pour afficher les heures et dates actuelles sur votre application web.

### Node Package Manager (NPM) : L'entrepôt d'outils et de matériaux

NPM agit comme un vaste entrepôt où vous pouvez trouver toutes sortes d'outils et de matériaux (modules) dont vous pourriez avoir besoin. C'est un endroit central pour obtenir des ressources supplémentaires pour construire vos applications web.

**Exemple** : Installer 'body-parser' depuis npm pour gérer les données JSON dans votre application web.

### Routage : Direction du trafic web

Le routage dans Express est comme la mise en place de routes et de chemins dans un complexe résidentiel. Il s'agit de diriger le flux de trafic (données et requêtes utilisateur) vers différentes parties de votre application web.

**Exemple** : Créer des routes dans un magasin en ligne, comme `/products` pour la liste des produits et `/products/:id` pour les détails des produits individuels.

### Middleware : Couches fonctionnelles supplémentaires

Le middleware dans Express peut être vu comme des couches ou des services supplémentaires dans votre bâtiment, comme la sécurité, la plomberie ou les systèmes électriques. Ils ajoutent des fonctionnalités spécifiques à votre application web.

**Exemple** : Ajouter un middleware 'cookie-parser' pour gérer les cookies dans votre application web.

### Requête et réponse : Canaux de communication

Les requêtes et réponses dans Express sont comme l'envoi et la réception de courrier ou de messages. Ce sont les moyens par lesquels votre application web communique avec les utilisateurs, en leur envoyant des données ou en recevant leurs entrées.

**Exemple** : Votre application reçoit une requête de connexion de l'utilisateur (requête) puis envoie un message de confirmation (réponse).

### Variables d'environnement : Espaces de stockage sécurisés

Pensez aux variables d'environnement comme à des espaces de stockage sécurisés ou des coffres-forts dans votre bâtiment. Ils sont utilisés pour stocker des informations sensibles comme des mots de passe ou des paramètres personnels, les gardant sécurisés et séparés de la construction principale.

**Exemple** : Stocker la chaîne de connexion à la base de données dans une variable d'environnement pour la garder sécurisée.

### Sécurité : Construction de garde-fous

Dans le contexte des applications web, la sécurité consiste à construire des garde-fous dans votre projet. C'est comme installer des serrures, des systèmes de sécurité et des mesures de sécurité incendie dans un bâtiment pour le protéger contre diverses menaces.

**Exemple** : Mettre en œuvre HTTPS pour sécuriser la transmission des données et utiliser JWT (JSON Web Tokens) pour l'authentification des utilisateurs afin de protéger les données des utilisateurs.

## ÉTAPE 4 : Stocker des données avec MongoDB et Mongoose

![Image](https://www.freecodecamp.org/news/content/images/2024/01/MongoDB_Logo.svg.png)

MongoDB est une base de données NoSQL qui offre une grande flexibilité et évolutivité pour le stockage et la gestion des données, ce qui la rend idéale pour gérer de grands volumes et divers types de données.

Mongoose est une bibliothèque de modélisation de données objet (ODM) pour MongoDB, fournissant une solution basée sur un schéma simple pour modéliser les données de l'application, améliorant l'interaction avec la base de données avec des fonctionnalités utiles et une validation.

### MongoDB : Une base de données NoSQL

MongoDB est un type de base de données qui stocke les données dans un format flexible, similaire à JSON. Cela la rend différente des bases de données traditionnelles, qui utilisent des tables et des lignes. Elle est idéale pour gérer de grands volumes de données et est très évolutive.

**Exemple** : Utiliser MongoDB pour stocker des profils utilisateurs où chaque profil peut avoir des champs différents.

### Collections et documents

Dans MongoDB, les données sont stockées dans des 'collections', qui sont similaires aux tables dans une base de données relationnelle. À l'intérieur de ces collections, les données sont stockées dans des 'documents'. Pensez à un document comme un seul enregistrement dans votre collection, comme une entrée dans un journal ou un contact dans un carnet d'adresses.

**Exemple** : Une collection 'users' avec des documents représentant chacun un utilisateur avec des détails comme le nom et l'email.

### Mongoose : Un outil de modélisation d'objets MongoDB

Mongoose est une bibliothèque pour Node.js qui facilite l'interaction avec MongoDB. Elle fournit une solution simple et basée sur un schéma pour modéliser les données de votre application. C'est comme avoir un assistant personnel pour aider à gérer la communication entre votre application et MongoDB.

**Exemple** : Utiliser Mongoose pour ajouter, récupérer et gérer facilement les données utilisateur dans une base de données MongoDB.

### Schémas

Dans Mongoose, un schéma est une structure qui définit le format des données à stocker dans MongoDB (comme la définition des champs et des types de données). Pensez-y comme un plan pour la façon dont vos données doivent apparaître.

**Exemple** : Créer un schéma Mongoose pour un article de blog avec des champs comme le titre, l'auteur et le contenu.

### Modèles

Un modèle dans Mongoose agit comme un constructeur, compilé à partir des définitions de schéma. Il représente des documents dans une base de données MongoDB. Les modèles sont responsables de la création et de la lecture de documents à partir de la base de données MongoDB sous-jacente.

**Exemple** : Définir un modèle 'User' basé sur un schéma utilisateur pour interagir avec la collection 'users' dans la base de données.

### Opérations CRUD

CRUD signifie Create, Read, Update, Delete. Ce sont les opérations de base que vous pouvez effectuer sur la base de données. Mongoose fournit des méthodes faciles pour exécuter ces opérations sur vos données.

**Exemple** : Utiliser des méthodes Mongoose pour ajouter de nouveaux utilisateurs, trouver des utilisateurs par nom, mettre à jour les informations utilisateur ou supprimer des utilisateurs.

### Connexion à MongoDB

Vous pouvez utiliser Mongoose pour connecter votre application Node.js à une base de données MongoDB. C'est comme établir une ligne téléphonique entre votre application et la base de données pour qu'elles puissent communiquer entre elles.

**Exemple** : Écrire une fonction de connexion Mongoose pour lier votre application Node.js à une base de données MongoDB hébergée sur Atlas.

### Interrogation des données

Mongoose vous permet d'interroger votre base de données MongoDB. Cela signifie que vous pouvez rechercher des données spécifiques, filtrer vos données en fonction de certains critères, et plus encore.

**Exemple** : Utiliser une requête Mongoose pour trouver tous les articles de blog écrits par un auteur spécifique.

### Validation des données

Mongoose fournit une validation intégrée. C'est un moyen de s'assurer que les données enregistrées dans votre base de données sont dans le bon format, comme vérifier si une adresse email ressemble à une adresse email.

**Exemple** : Définir un schéma dans Mongoose où le champ email doit correspondre au format d'une adresse email.

### Middleware (Pre et Post Hooks)

Les middlewares de Mongoose sont des fonctions qui peuvent être exécutées automatiquement avant ou après certaines opérations, comme l'enregistrement d'un document. Ils sont utiles pour des logiques complexes comme le hachage des mots de passe avant de les enregistrer dans la base de données.

**Exemple** : Utiliser un middleware pre-save dans Mongoose pour hacher les mots de passe des utilisateurs avant de les enregistrer dans la base de données.

### Index

Les index dans MongoDB sont utilisés pour améliorer les performances des recherches. Ils sont similaires aux index dans un livre, aidant la base de données à trouver les données plus rapidement.

**Exemple** : Créer un index sur le champ 'email' dans une collection d'utilisateurs pour accélérer la recherche d'utilisateurs par email.

### Agrégation

L'agrégation dans MongoDB est un moyen puissant de traiter les données et d'obtenir des résultats calculés. C'est comme avoir une calculatrice sophistiquée pour effectuer des opérations complexes sur vos données, telles que la somme de valeurs ou leur moyenne.

**Exemple** : Utiliser le framework d'agrégation de MongoDB pour calculer le nombre moyen de commentaires sur les articles de blog.

## ÉTAPE 5 : Écrire des tests

![Image](https://www.freecodecamp.org/news/content/images/2024/01/opengraph.png)

Les tests en développement logiciel sont comme une vérification de sécurité pour s'assurer que tout dans votre application fonctionne comme prévu. C'est une étape cruciale dans le processus de développement où vous recherchez des bugs ou des problèmes avant que vos utilisateurs ne les trouvent. Pensez-y comme à la relecture d'un essai ou à la vérification d'une voiture avant un voyage sur la route – cela aide à détecter et à corriger les problèmes tôt.

Il existe différents types de tests, chacun servant un objectif unique :

### Tests unitaires

C'est la forme la plus basique de test. Ici, vous testez des parties individuelles de votre code (comme des fonctions ou des composants) en isolation. C'est comme vérifier chaque ampoule dans une guirlande de Noël.

Dans la stack MERN, des outils comme Jest ou Mocha sont couramment utilisés pour cela. Ils vous permettent d'écrire de petits tests pour vérifier si une partie spécifique de votre application se comporte comme prévu.

### Tests d'intégration

Ce type de test vérifie comment différentes parties de votre application fonctionnent ensemble. C'est comme s'assurer que toutes les ampoules s'allument lorsqu'elles sont connectées et que la guirlande est branchée.

Pour la stack MERN, vous pourriez toujours utiliser Jest ou Mocha, combinés avec d'autres outils comme Chai pour les assertions, afin de vous assurer que différents composants ou services de votre application interagissent correctement.

### Tests de bout en bout (E2E)

Ici, vous testez le flux de travail de votre application du début à la fin. C'est comme vérifier si tout l'arbre de Noël s'allume et scintille comme prévu.

Pour une application de stack MERN, Cypress ou Selenium sont des choix populaires. Ils simulent des scénarios d'utilisateurs réels, garantissant que l'ensemble de l'application, du front-end en React au back-end avec Express et Node.js, fonctionne ensemble de manière fluide.

### Tests de performance

Cela vérifie si votre application peut gérer le stress, comme un trafic intense ou un traitement de données. C'est similaire à s'assurer que les lumières de l'arbre de Noël ne font pas sauter un fusible lorsqu'elles sont toutes allumées. Des outils comme Loader.io ou Apache JMeter peuvent être utilisés ici.

Chaque type de test sert à s'assurer qu'un aspect différent de votre application fonctionne correctement, et ensemble, ils contribuent à construire une application robuste, fiable et conviviale.

En employant ces tests dans la stack MERN, vous détectez non seulement les bugs tôt, mais vous maintenez également un haut niveau de qualité pour votre application.

## ÉTAPE 6 : Utiliser Git

![Image](https://www.freecodecamp.org/news/content/images/2024/01/629b7adc7c5cd817694c3231.png)

Git est un système de contrôle de version, un outil qui suit les changements dans votre code au fil du temps. Pensez-y comme à un journal détaillé pour votre projet de codage. Chaque fois que vous apportez des modifications à votre code, Git conserve un enregistrement de ce qui a été changé, quand et par qui. Cela devient incroyablement utile lorsque vous travaillez sur des projets complexes, comme ceux impliquant la stack MERN.

Pourquoi Git est-il si important lors de la construction avec la stack MERN, ou tout autre logiciel d'ailleurs ?

### Collaboration

Git est comme un livre de jeu d'équipe. Il permet à plusieurs développeurs de travailler sur le même projet sans se marcher sur les pieds.

Tout le monde peut travailler sur différentes fonctionnalités ou parties de l'application simultanément (comme les schémas de base de données MongoDB, les composants React ou les routes Express.js). Git aide à gérer ces contributions, garantissant que les changements peuvent être fusionnés en douceur dans le projet principal.

### Suivi des changements

Imaginez que vous avez apporté des modifications à votre composant React, et soudainement les choses ne fonctionnent plus comme avant. Git vous permet de remonter dans le temps et de voir quels changements ont été apportés et par qui.

Ces données historiques sont inestimables pour comprendre comment votre projet a évolué et pour corriger les problèmes sans avoir à recommencer de zéro.

### Branchement et fusion

La fonctionnalité de branchement de Git vous permet de diverger de la ligne principale de développement et d'expérimenter de nouvelles fonctionnalités ou idées de manière contrôlée.

Vous pouvez créer une branche, apporter vos modifications, puis fusionner ces modifications dans le projet principal lorsqu'elles sont prêtes. Cela garantit que le projet principal (souvent appelé la branche 'master' ou 'main') reste stable.

### Sauvegarde et restauration

Avec Git, l'historique complet de votre projet est stocké dans le dépôt. Si quelque chose ne va pas, vous pouvez revenir à un état précédent. C'est comme avoir un système de sauvegarde infaillible.

### Documentation

Les messages de commit dans Git fournissent un récit pour votre projet. Ils vous permettent de documenter les changements apportés et pourquoi, ce qui est extrêmement utile pour votre futur vous-même et pour les autres développeurs qui pourraient travailler sur le projet.

Lors de la construction d'applications avec la stack MERN, Git offre un filet de sécurité et un espace de travail collaboratif. Il garde votre projet organisé, suit chaque changement et permet à plusieurs développeurs de travailler ensemble plus efficacement.

L'utilisation de Git est essentielle pour gérer des projets de développement complexes dans le monde du développement logiciel d'aujourd'hui.

## ÉTAPE 7 : Déploiements

![Image](https://www.freecodecamp.org/news/content/images/2024/01/img-blog-cico.jpg)

Le déploiement de code est le processus de prise de code écrit par les développeurs et de le rendre opérationnel dans un environnement en direct où les utilisateurs peuvent interagir avec lui.

Dans le contexte de la stack MERN, qui implique des technologies comme MongoDB, Express.js, React et Node.js, le déploiement est l'étape finale dans le voyage de donner vie à une application full-stack.

Imaginez que vous avez construit une maison (votre application web). Le déploiement est comme la déplacer du chantier (environnement de développement) à son emplacement réel où les gens peuvent y vivre (environnement de production). Ce processus implique plusieurs étapes clés pour s'assurer que tout fonctionne comme prévu lorsque les utilisateurs accèdent à votre application.

### Préparation au déploiement

Avant de déployer, vous devez préparer votre application. Cela implique de vous assurer que votre code est complet et testé, que les dépendances sont correctement gérées et que votre application est configurée pour l'environnement de production.

Pour les applications de stack MERN, cela peut signifier configurer des variables d'environnement, configurer votre connexion à la base de données (MongoDB) pour la production et optimiser votre front-end React pour les performances.

### Hébergement et serveurs

Choisir où héberger votre application est crucial. Pour les applications de stack MERN, vous pouvez utiliser des services d'hébergement basés sur le cloud comme AWS, Heroku ou DigitalOcean. Ces plateformes offrent des services pour héberger à la fois votre backend Node.js et votre base de données MongoDB, et elles offrent souvent des fonctionnalités supplémentaires comme la mise à l'échelle, la surveillance et la sécurité.

### Intégration continue/Déploiement continu (CI/CD)

CI/CD est une méthodologie qui automatise le processus de déploiement. Chaque fois que vous apportez des modifications à votre base de code (comme corriger un bug ou ajouter une nouvelle fonctionnalité), les outils CI/CD testent automatiquement votre code et le déploiement si les tests passent. Cela garantit que votre application est toujours à jour avec les dernières modifications.

Des outils comme Jenkins, Travis CI ou GitHub Actions sont couramment utilisés à cette fin.

### Surveillance et maintenance

Après le déploiement, il est important de surveiller votre application pour tout problème et d'effectuer une maintenance régulière. Cela pourrait impliquer de vérifier les journaux du serveur, de mettre à jour les dépendances ou de déployer des correctifs pour tout bug qui pourrait survenir.

### Retours en arrière

Une bonne stratégie de déploiement inclut également des plans pour les retours en arrière. Si quelque chose ne va pas après le déploiement, vous devez être en mesure de revenir à la version précédente rapidement pour minimiser les temps d'arrêt.

Dans la stack MERN, chaque composant (MongoDB, Express.js, React et Node.js) peut nécessiter des considérations spécifiques pour le déploiement. Par exemple, vous pourriez utiliser des conteneurs Docker pour empaqueter votre backend Node.js et Express.js, garantissant qu'il s'exécute de manière cohérente dans différents environnements. Les applications React peuvent être minifiées et regroupées pour des performances optimales.

En essence, le déploiement dans la stack MERN consiste à faire passer votre application de votre machine locale à un serveur où elle peut servir les utilisateurs de manière fiable et efficace. Cela implique une planification minutieuse, le choix des bonnes solutions d'hébergement, l'automatisation du processus autant que possible et la préparation à la résolution des problèmes post-déploiement.

## Meilleures ressources pour apprendre la stack MERN

Maintenant que vous avez une assez bonne idée de ce que vous devez apprendre pour maîtriser la stack MERN, examinons une liste de ressources gratuites que vous pouvez commencer à utiliser dès aujourd'hui pour commencer votre voyage !

* Le [programme freeCodeCamp](https://www.freecodecamp.org/learn/) est l'un des meilleurs endroits pour apprendre à coder gratuitement. Le programme est très approfondi et couvre de nombreux sujets mentionnés dans cet article.
* La chaîne YouTube freeCodeCamp propose également une tonne de cours gratuits que vous pouvez essayer. [Ce projet de livre sur la stack MERN est un excellent choix pour les débutants](https://www.youtube.com/watch?v=-42K44A1oMA&t=2950s).
* [Full Stack open](https://fullstackopen.com/) est une autre bonne ressource. Il n'enseigne pas MongoDB mais vous apprenez SQL à la place, ce qui est tout aussi utile.
* Mon [projet d'application de réservation d'hôtel MERN stack sur YouTube est un cours gratuit de 15 heures](https://www.youtube.com/watch?v=YdBy9-0pER4) où vous apprendrez tout ce dont il est question dans cet article.

## 10 idées de projets que vous pouvez essayer aujourd'hui

L'une de mes façons préférées d'apprendre de nouvelles technologies est de construire des projets. Si vous avez du mal à trouver des idées, voici 10 projets que vous pouvez commencer à construire dès aujourd'hui. Je vais construire certains de ces projets sur ma [chaîne YouTube](https://www.youtube.com/@ChrisBlakely), alors n'hésitez pas à vous abonner pour rester à jour !

### Site web de blog personnel

* **Fonctionnalités** : Les utilisateurs peuvent lire des articles, et l'administrateur peut créer, modifier ou supprimer des articles.
* **Focus d'apprentissage** : Opérations CRUD de base, authentification des utilisateurs, intégration de React avec l'API Express, et utilisation de MongoDB pour le stockage des données.

### Gestionnaire de tâches (Liste de choses à faire)

* **Fonctionnalités** : Les utilisateurs peuvent ajouter, voir, modifier et supprimer des tâches. Les tâches peuvent avoir des dates limites et des niveaux de priorité.
* **Focus d'apprentissage** : Gestion de l'état React, gestion des routes Express, opérations MongoDB, et développement d'interface utilisateur de base.

### Site de commerce électronique simple

* **Fonctionnalités** : Afficher des produits, ajouter au panier, et fonctionnalité de paiement. Fonctionnalités d'administration pour ajouter ou supprimer des produits.
* **Focus d'apprentissage** : Composants React pour la liste des produits, gestion du panier, Express.js pour les API de produits, MongoDB pour les données des produits, et gestion des entrées utilisateur.

### Application de partage de recettes

* **Fonctionnalités** : Les utilisateurs peuvent publier, voir, modifier et supprimer des recettes. Implémenter un système de notation ou de commentaires pour l'interaction.
* **Focus d'apprentissage** : Téléchargement de fichiers pour les images, gestion du contenu généré par les utilisateurs, et conception de schéma MongoDB.

### Suivi de budget

* **Fonctionnalités** : Les utilisateurs peuvent saisir leurs dépenses et revenus, les catégoriser et voir un résumé de leurs finances.
* **Focus d'apprentissage** : Gestion des formulaires dans React, création de services RESTful avec Express, et structuration efficace des données dans MongoDB.

### Application de planification d'événements

* **Fonctionnalités** : Les utilisateurs peuvent créer et gérer des événements, envoyer des invitations et suivre les réponses.
* **Focus d'apprentissage** : Gestion des dates en JavaScript, documents MongoDB complexes, et middleware Express pour l'authentification.

### Suivi de fitness

* **Fonctionnalités** : Enregistrer les séances d'entraînement, suivre les progrès au fil du temps, fixer des objectifs de fitness.
* **Focus d'apprentissage** : Visualisation de données avec React, création de points de terminaison d'API pour divers types de données, et MongoDB pour le stockage de données chronologiques.

### Application de chat

* **Fonctionnalités** : Salons de chat en temps réel, messagerie privée et profils utilisateur.
* **Focus d'apprentissage** : WebSockets avec Node.js pour la communication en temps réel, MongoDB pour le stockage des messages, et React pour les mises à jour dynamiques de l'interface utilisateur.

### Plateforme de critiques de livres

* **Fonctionnalités** : Les utilisateurs peuvent publier des critiques de livres, noter des livres et parcourir les critiques d'autres utilisateurs.
* **Focus d'apprentissage** : Intégration d'API externes pour les données de livres, modération du contenu généré par les utilisateurs, et requêtes complexes dans MongoDB.

### Annuaire d'entreprises locales

* **Fonctionnalités** : Liste d'entreprises locales avec catégories, avis des utilisateurs et informations de contact.
* **Focus d'apprentissage** : Géolocalisation, requêtes avancées et indexation dans MongoDB, et création d'une mise en page réactive avec React.

## Conclusion du voyage MERN stack

Alors que nous arrivons à la fin de notre exploration de la stack MERN, j'espère que ce guide a éclairé le chemin pour votre voyage dans le monde du développement full-stack.

Nous avons couvert les composants fondamentaux – MongoDB, Express.js, React et Node.js – et nous sommes plongés dans les aspects pratiques de la construction, des tests et du déploiement d'applications en utilisant cette pile polyvalente.

Rappelez-vous, la route pour maîtriser la stack MERN est à la fois difficile et gratifiante. Chaque projet que vous entreprenez ajoutera à vos compétences et à votre confiance. Utilisez les ressources et les idées de projets fournis comme des tremplins pour construire votre portfolio et approfondir votre compréhension.

La beauté de la stack MERN réside dans sa nature communautaire, alors n'hésitez pas à demander de l'aide, à collaborer et à partager vos expériences.

Si vous souhaitez entrer en contact, vous pouvez me joindre sur [LinkedIn](https://www.linkedin.com/in/chrisblakely01/), ou laisser un commentaire sur ma [chaîne YouTube](https://www.youtube.com/@ChrisBlakely). Bonne chance et bon codage !

%[https://www.youtube.com/@ChrisBlakely]