---
title: Apprendre Node.js et Express en espagnol – Cours pour débutants
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2022-08-08T04:35:40.000Z'
originalURL: https://freecodecamp.org/news/learn-node-js-and-express-in-spanish-course-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/thumbnail.png
tags:
- name: Express
  slug: express
- name: node
  slug: node
seo_title: Apprendre Node.js et Express en espagnol – Cours pour débutants
seo_desc: "Hi! If you speak Spanish and you want to learn Node.js, and Express, you\
  \ are in the right place. \nIn this article, you will find a brief introduction\
  \ to back-end web development, Node.js, and Express. You will learn why they are\
  \ very powerful tools f..."
---

Salut ! Si vous parlez espagnol et que vous souhaitez apprendre Node.js et Express, vous êtes au bon endroit. 

Dans cet article, vous trouverez une brève introduction au développement web back-end, à Node.js et à Express. Vous apprendrez pourquoi ce sont des outils très puissants pour développer des serveurs web et pourquoi vous devriez les apprendre si votre objectif est de devenir développeur web back-end. 

Ensuite, vous trouverez [un cours de **8,5 heures** sur Node.js et Express](https://www.youtube.com/watch?v=1hpc70_OoAg) sur la chaîne YouTube espagnole de freeCodeCamp où vous pourrez apprendre les bases en espagnol et construire un projet étape par étape.

Si vous avez des amis hispanophones, vous êtes invité à partager la **[version espagnole de cet article](https://www.freecodecamp.org/espanol/news/aprende-node-js-y-express-curso-desde-cero/)** avec eux.

Commençons ! ✨

## **🔸 Qu'est-ce que le développement web back-end ?**

Le développement web a transformé notre monde moderne. Chaque jour, nous accédons à Internet pour trouver des informations, apprendre, acheter des produits, partager nos pensées et nous connecter avec notre famille et nos amis. 

En gros, notre vie ne serait plus jamais la même sans les sites web et les applications web. Êtes-vous d'accord ? 👋 

Si c'est le cas, alors apprendre le développement web peut vous mener vers une carrière très enrichissante, car vous pouvez avoir un impact énorme sur la vie de milliers, voire de millions d'utilisateurs. 

Parlons un peu des différentes zones du développement web. 

### ⬛️ Développement front-end vs. back-end

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-174.png)

Les développeurs qui créent des applications web incroyables sont appelés **développeurs web**. Ils peuvent se spécialiser pour développer différentes parties d'une application web :

* Les **développeurs front-end** implémentent la partie de l'application web avec laquelle les utilisateurs interagissent directement. Ils développent la partie visible des plateformes incroyables que nous utilisons et aimons chaque jour. Dans l'analogie du magasin que vous pouvez voir ci-dessus, le front-end serait représenté par la partie du magasin que les clients peuvent voir. 
* Les **développeurs back-end** implémentent toutes les fonctionnalités que les utilisateurs ne voient pas, comme les serveurs, les bases de données et leurs interactions avec la partie front-end des applications. Dans notre analogie de magasin, le back-end serait représenté par l'entrepôt, la partie du magasin qui soutient tout ce que les clients voient. 
* Les **développeurs full-stack** sont responsables des deux domaines. Ils ont une connaissance approfondie du développement web front-end et back-end. 

Intéressant, n'est-ce pas ? ✨

Maintenant, plongeons plus profondément dans le développement web back-end, car c'est l'une des principales applications de Node.js et Express.  

### Le modèle client-serveur

Internet est basé sur le **modèle client-serveur**, dans lequel deux appareils (le client et le serveur) communiquent entre eux. 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-173.png)
_Illustration du modèle client-serveur._

### Qu'est-ce qu'un client ?

Lorsque vous essayez d'accéder à un site web dans votre navigateur, le navigateur (**client**) envoie une requête HTTP pour ce site web au serveur. 

### Qu'est-ce qu'un serveur ?

Le **serveur** est un programme qui écoute les requêtes et génère des réponses appropriées. Ces réponses incluent souvent :

* L'envoi de données au client.
* L'exécution de certaines tâches.
* Le travail avec ou la mise à jour d'une base de données. 

Par exemple, nous pouvons envoyer une requête au serveur pour ajouter un nouvel utilisateur à la base de données d'une application web. Le serveur doit faire les mises à jour nécessaires dans la base de données et notifier le client que ce changement a été réussi. 

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-175.png)
_Client (gauche) - Serveur (centre) - Base de données (droite)_

Le développement et la maintenance des serveurs sont l'une des principales tâches des développeurs web back-end, et c'est précisément pour cela que **Node.js et Express** sont utilisés. 

## 🔹 Qu'est-ce que Node.js ? 

**Node.js** est un environnement d'exécution JavaScript asynchrone et piloté par événements, construit sur le moteur JavaScript V8 de Chrome. Il nous donne tous les outils dont nous avons besoin pour exécuter JavaScript dans le terminal sans navigateur web. 

💡 **Conseil :** Avant Node.js, nous ne pouvions pas exécuter de programmes JavaScript sans navigateur. Seuls les navigateurs étaient conçus pour cette tâche puisque JavaScript est l'un des principaux langages de programmation du web. 

L'aspect génial de Node.js est qu'il nous permet de construire des applications réseau scalables avec des performances élevées. 

Selon sa [documentation officielle](https://nodejs.org/en/about/) :

> Les utilisateurs de Node.js sont libres de s'inquiéter des blocages du processus, car il n'y a pas de verrous. Presque aucune fonction dans Node.js ne réalise directement des E/S, donc le processus ne se bloque jamais sauf lorsque les E/S sont réalisées en utilisant des méthodes synchrones de la bibliothèque standard de Node.js. **Parce que rien ne bloque, les systèmes scalables sont très raisonnables à développer dans Node.js.**

⚠️ Il est important de noter que **Node.js n'est pas** :

* Un langage de programmation.
* Un framework.
* Une bibliothèque.

C'est un **environnement d'exécution JavaScript** développé pour exécuter du code JavaScript. 

### **Pourquoi devriez-vous apprendre Node.js ?**

Maintenant que vous savez ce qu'est Node.js, voyons **pourquoi** vous devriez l'apprendre. 

**Node.js** est l'une des technologies web les plus populaires parmi les développeurs, y compris les débutants qui apprennent à coder, ainsi que les professionnels.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/node-logo.png)
_Logo de Node.js_

**Node.js** est extrêmement populaire. Selon le [sondage des développeurs Stack Overflow 2022](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe), c'est l'une des technologies web les plus populaires utilisées par les développeurs professionnels et par ceux qui apprennent à coder. 

Node.js a obtenu **47,12 %** des votes lorsque les répondants ont été interrogés sur les frameworks web et les technologies web avec lesquels ils avaient fait un travail de développement approfondi au cours de l'année passée, et avec lesquels ils voulaient travailler au cours de l'année suivante. 

**💡 Conseil :** c'est presque la moitié des 58 743 réponses !

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-171.png)
_Les résultats de la catégorie Frameworks Web et technologies dans le [sondage des développeurs Stack Overflow 2022](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe). **Node**.js mène avec **47,12 %** des réponses._

Ce pourcentage était encore plus élevé parmi les répondants qui apprenaient à coder : **52,86 %**. Génial, n'est-ce pas ? 😁

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-172.png)
_Les résultats de la catégorie Frameworks Web et technologies dans le [sondage des développeurs Stack Overflow 2022](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe) lorsque "Apprendre à coder" était sélectionné. **Node**.js mène avec **52,86 %** des réponses._

C'est une preuve claire de l'impact que Node.js a dans le développement web. En apprenant Node.js, vous investirez votre temps et vos ressources de manière judicieuse. Vous acquerrez des compétences précieuses très demandées dans ce domaine. 

## 🔸 Qu'est-ce qu'Express ? 

Si votre objectif est de développer un serveur avec Node.js, le processus peut être beaucoup plus facile si vous utilisez **Express**. C'est un framework d'application web spécifiquement développé pour Node.js. 

Selon la [documentation officielle](https://expressjs.com/) d'Express :

> Express est un framework d'application web minimal et flexible pour Node.js qui fournit un ensemble robuste de fonctionnalités pour les applications web et mobiles.

**💡 Conseil :** Express inclut de nombreux outils que vous pouvez utiliser pour écrire un code plus concis, lisible et maintenable. Croyez-moi. Une fois que vous commencez à travailler avec Express, vous ne voudrez plus jamais arrêter.

Express dispose de nombreuses méthodes utilitaires HTTP et de middleware que vous pouvez utiliser pour créer des API robustes (Interfaces de Programmation d'Applications), qui sont fondamentales pour le développement web back-end et full-stack.

Dans le [sondage des développeurs Stack Overflow 2022](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe), **Express** était la quatrième technologie web ou framework la plus utilisée avec **22,99 %** de tous les votes :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-177.png)
_Les résultats de la catégorie Frameworks Web et technologies dans le [sondage des développeurs Stack Overflow 2022](https://survey.stackoverflow.co/2022/#most-popular-technologies-webframe). **Express** était quatrième avec **22,99 %** des réponses._

Express a également obtenu **25,72 %** des votes des répondants qui apprennent à coder :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-176.png)
_**Express** a obtenu **25,72 %** des votes des répondants qui apprennent à coder. Il était troisième dans les résultats de la catégorie Frameworks Web et technologies._

**Génial !** Maintenant, vous savez pourquoi vous devriez apprendre Node.js et Express. Je vous promets que cela en vaudra totalement la peine. ✨

## 🔹 **Contenu du cours Node.js et Express**

Maintenant, passons en revue ce que vous apprendrez pendant le cours. 

**💡 Conseil :** pour suivre le cours, vous devez avoir des connaissances préalables en **JavaScript**. Si vous devez réviser ces sujets en espagnol, je vous recommande de regarder ce [cours de JavaScript](https://www.youtube.com/watch?v=ivdTnPl1ND0&t=3s) sur la chaîne YouTube espagnole de freeCodeCamp.

### Introduction à Node.js et concepts de base

* Introduction à Node.js.
* Concepts de base du développement web back-end.
* Applications de Node.js.
* API et à quoi elles servent.
* Avantages de Node.js.
* Comment télécharger et installer Node.js.
* Comment confirmer que Node.js a été installé avec succès.
* Comment vérifier votre version actuelle de Node.js.
* Le REPL de Node.js.

### Votre premier projet Node.js et les modules Node

* Qu'est-ce qu'un module ? Concept et avantages.
* Comment exporter et importer des modules.
* Comment exporter plusieurs éléments d'un module JavaScript. 
* Comment exécuter un fichier JavaScript avec la commande `node`. 
* Modules principaux de Node.js.
* Le module `console`.
* Le module `process`.
* Le module `os`.
* Le module `fs`.
* Le module `timers`.

### Introduction à npm et JSON

* Qu'est-ce que npm ? 
* Concepts de base de npm.
* Comment initialiser un package avec `npm init`.
* Le fichier `package.json`.
* Introduction à JSON.
* Comment installer et désinstaller des packages avec npm. 
* Le fichier `package-lock.json`.

### Événements et opérations asynchrones

* Qu'est-ce qu'un événement ?
* Événements dans Node.js.
* Événements asynchrones vs. synchrones.
* Promesses et fonctions de rappel en JavaScript.
* Promesses, `.then()` et `.catch()`.
* Fonctions asynchrones avec `async` et `await`.

### Serveurs Node.js et le protocole HTTP

* Le modèle client-serveur.
* Le format des requêtes et réponses HTTP. 
* Verbes HTTP : GET, POST, PUT, DELETE.
* Codes d'état HTTP. 
* Le module `http` dans Node.js
* Comment créer un serveur dans Node.js.
* Les objets `req` et `res`. 
* Structure d'une URL.
* Routage dans Node.js.

### Nodemon

* Qu'est-ce que Nodemon ?
* Comment installer Nodemon globalement.
* Comment utiliser Nodemon pour mettre à jour automatiquement les applications Node.js. 
* Concepts : CRUD, REST, API.

### Express

* Comment installer Express et comment démarrer un projet. 
* Routage dans Express.
* Express et Nodemon. 
* Comment faire correspondre plusieurs routes. 
* Paramètres de route et routes dynamiques. 
* Middleware dans Express.
* Gestion des requêtes GET, POST, PUT, PATCH et DELETE. 
* Paramètres de requête. 
* Routeurs dans Express.

💡 **Conseil :** Nous travaillerons avec Visual Studio Code pendant le cours et nous installerons une extension pour simuler les requêtes POST, PUT et DELETE. 

## 🔹 **Projet Node.js et Express**

Pendant le cours, vous apprendrez à travers des exemples pratiques et vous appliquerez tout ce que vous apprenez étape par étape.

![Image](https://www.freecodecamp.org/espanol/news/content/images/2022/08/image-3.png)
_Projet que nous construirons avec Node.js et Express_

Vous apprendrez à travailler avec les promesses avec un exemple de pizza 🍕, comment travailler avec JavaScript asynchrone, et vous développerez un serveur et une API simples avec Node.js pour envoyer des informations sur des cours de programmation et de mathématiques au navigateur.

Ensuite, nous adapterons ce serveur simple pour qu'il fonctionne avec Express. Vous appliquerez des concepts précédents et nouveaux étape par étape pour créer un serveur qui gérera plusieurs routes, paramètres et différents types de requêtes HTTP. 

## **📜 Cours Node.js et Express** sur YouTube

Génial. Maintenant que vous en savez plus sur Node.js et Express et sur ce que vous apprendrez pendant le cours, vous êtes invité à commencer à suivre le cours en **espagnol** :

%[https://www.youtube.com/watch?v=1hpc70_OoAg]

✍️ Cours créé par **Estefania Cassingena Navone** (Twitter : [@EstefaniaCassN](https://twitter.com/EstefaniaCassN), YouTube : [Coding with Estefania](https://youtube.com/codingwithestefania)).

J'espère vraiment que vous aimerez le cours et que vous le trouverez utile pour faire vos premiers pas dans le monde du développement web back-end.

Vous êtes également invité à continuer à apprendre avec nos cours en **espagnol** :

%[https://www.youtube.com/watch?v=XqFR2lqBYPs]

%[https://www.youtube.com/watch?v=ivdTnPl1ND0]

%[https://www.youtube.com/watch?v=DLikpfc64cA]

%[https://www.youtube.com/watch?v=6Jfk8ic3KVk]