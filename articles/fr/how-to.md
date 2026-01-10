---
title: Apprendre à coder
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2021-03-17T05:55:00.000Z'
originalURL: https://freecodecamp.org/news/how-to
coverImage: https://cdn-media-2.freecodecamp.org/w1280/604f04d028094f59be255cc6.jpg
tags:
- name: Data Science
  slug: data-science
- name: Docker
  slug: docker
- name: how-to
  slug: how-to
- name: JavaScript
  slug: javascript
- name: programing
  slug: programing
- name: Python
  slug: python
- name: TypeScript
  slug: typescript
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre à coder
seo_desc: 'Are you a new developer just getting started? Or are you a seasoned developer
  looking to expand your skill set?

  Either way, the freeCodeCamp community''s got you covered.

  A lot of the time, learning how to program is not so much a straight line as it
  ...'
---

Êtes-vous un nouveau développeur qui commence tout juste ? Ou êtes-vous un développeur expérimenté cherchant à élargir vos compétences ?

Dans les deux cas, la communauté freeCodeCamp vous couvre.

Souvent, apprendre à programmer n'est pas tant une ligne droite qu'un vaste organigramme, avec de nombreuses sections répétées et des boucles :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/windows-system-calls.jpg)
_Un organigramme pour les appels système dans Windows Server Edition ([source](https://slideplayer.com/slide/11896895/))_

Mais cela n'a pas besoin d'être si compliqué.

J'ai parcouru notre vaste catalogue de tutoriels et créé une liste de certaines des meilleures ressources sur la façon d'apprendre à peu près tout ce que vous devez savoir en tant que développeur.

La liste est organisée de manière lâche en différentes sections et sous-sections. N'hésitez pas à parcourir la table des matières ci-dessous et à sauter pour chercher un article sur ce que vous essayez d'apprendre.

De plus, de nombreuses choses sur cette liste nécessitent certaines connaissances préalables d'une autre technologie. Ne soyez pas surpris si vous vous retrouvez à ouvrir des articles de plusieurs sections.

Enfin, il s'agit d'un document vivant, qui grandira à mesure que nous publierons plus d'articles utiles. Assurez-vous de vérifier souvent, et partagez cela avec vos amis si vous le trouvez utile.

## Table des matières

* [Comment construire un site web](#comment-construire-un-site-web)
    * [HTML](#html)
    * [CSS](#css)
* [Comment apprendre la programmation](#comment-apprendre-la-programmation)
    * [JavaScript](#javascript)
    * [Node.js](#node-js)
    * [TypeScript](#typescript)
    * [Deno](#deno)
    * [Python](#python)
    * [Java](#java)
    * [Go (Golang)](#go-golang)
    * [Rust](#rust)
    * [C](#c)
    * [C++](#c)
    * [C#](#c--1)
* [Comment apprendre Linux](#comment-apprendre-linux)
* [Comment apprendre Git et le contrôle de version](#comment-apprendre-git-et-le-controle-de-version)
* [Comment apprendre un Framework / Bibliothèque Frontend](#comment-apprendre-un-framework-bibliothèque-frontend)
    * [React](#react)
    * [Vue](#vue)
    * [Angular](#angular)
* [Comment apprendre les bases du web et la sécurité web](#comment-apprendre-les-bases-du-web-et-la-securite-web)
    * [Bases du web](#bases-du-web)
    * [HTTPS](#https)
    * [Cookies](#cookies)
* [Comment apprendre les bases de données](#comment-apprendre-les-bases-de-donnees)
    * [SQL / MySQL](#sql-mysql)
    * [MongoDB / Mongoose (NoSQL)](#mongodb-mongoose-nosql)
    * [Redis (NoSQL)](#redis-nosql)
    * [Postgres / PostgreSQL](#postgres-postgresql)
* [Comment apprendre le développement backend](#comment-apprendre-le-developpement-backend)
    * [Express](#express)
    * [Flask](#flask)
    * [Django](#django)
* [Comment apprendre les générateurs de sites statiques](#comment-apprendre-les-generateurs-de-sites-statiques)
    * [Gatsby](#gatsby)
    * [Next.js](#next-js)
    * [Hugo](#hugo)
    * [Nuxt.js](#nuxt-js)
    * [Vuepress](#vuepress)
* [Comment apprendre les Bundlers, Compilateurs, Gestionnaires de dépendances, Task Runners, Formatters, et Linters](#comment-apprendre-les-bundlers-compilateurs-gestionnaires-de-dependances-task-runners-formatters-et-linters)
    * [Webpack et Babel](#webpack-et-babel)
    * [ESLint et Prettier](#eslint-et-prettier)
    * [Parcel](#parcel)
    * [Gulp](#gulp)
    * [Scripts npm](#npm-scripts)
* [Comment apprendre le développement d'applications mobiles](#comment-apprendre-le-developpement-dapplications-mobiles)
    * [React Native](#react-native)
    * [Ionic](#ionic)
    * [Flutter](#flutter)
* [Comment apprendre le développement d'applications de bureau](#comment-apprendre-le-developpement-dapplications-de-bureau)
    * [Electron](#electron)
    * [Proton Native](#proton-native)
* [Comment apprendre la science des données et le machine learning](#comment-apprendre-la-science-des-donnees-et-le-machine-learning)
    * [Machine Learning général](#general-machine-learning)
    * [Pandas](#pandas)
    * [Numpy](#numpy)
    * [Scikit-Learn](#scikit-learn)
    * [Seaborn](#seaborn)
    * [Matplotlib](#matplotlib)
    * [TensorFlow](#tensorflow)
    * [PyTorch](#pytorch)
    * [Keras](#keras)
* [Comment apprendre la virtualisation et la conteneurisation](#comment-apprendre-la-virtualisation-et-la-conteneurisation)
    * [Machines virtuelles](#virtual-machines)
    * [Docker](#docker)
    * [Kubernetes](#kubernetes)
* [Comment apprendre le cloud computing](#comment-apprendre-le-cloud-computing)
    * [Amazon Web Services (AWS)](#amazon-web-services-aws)
    * [Google Cloud Platform (GCP)](#google-cloud-platform-gcp)
    * [Microsoft Azure](#microsoft-azure)
* [Comment apprendre DevOps](#comment-apprendre-devops)
    * [DevOps général](#general-devops)
    * [Travis CI](#travis-ci)
    * [Jenkins](#jenkins)
    * [GoCD](#gocd)
    * [Ansible](#ansible)
    * [Chef](#chef)
    * [Kafka](#kafka)
    * [Terraform](#terraform)

## Comment construire un site web

Pour construire un site web de base, tout ce dont vous avez vraiment besoin est HTML (Hypertext Markup Language) et CSS (Cascading Style Sheets). HTML fournit le contenu et la structure du site, et CSS est utilisé pour le styliser.

Voici quelques-unes des meilleures ressources sur HTML et CSS. Une fois que vous êtes familiarisé avec ces technologies, passez à la section suivante et apprenez JavaScript pour rendre vos sites web plus interactifs.

### HTML

* [Apprendre les bases de HTML pour les débutants en seulement 15 minutes](https://www.freecodecamp.org/news/html-basics-for-beginners/)
* [Comment créer des hyperliens HTML en utilisant l'attribut HREF sur les balises](https://www.freecodecamp.org/news/how-to-make-html-hyperlinks-using-the-href-attribute-on-tags/)
* [Comment utiliser HTML pour ouvrir un lien dans un nouvel onglet](https://www.freecodecamp.org/news/how-to-use-html-to-open-link-in-new-tab/)
* [Code de lien HTML – Comment insérer un lien vers un site web avec HREF](https://www.freecodecamp.org/news/html-link-code-how-to-insert-a-link-to-a-website-with-href-3/)
* [Entités HTML – Une liste des espaces HTML et autres symboles et caractères spéciaux](https://www.freecodecamp.org/news/html-entities-symbols-special-character-codes-list/)
* [Comment activer le mode sombre dans les e-mails HTML – Tout ce que vous devez savoir](https://www.freecodecamp.org/news/dark-mode-in-html-email-everything-you-need-to-know/)
* [Tutoriel HTML clignotant – Comment utiliser la balise Blink, avec des exemples de code](https://www.freecodecamp.org/news/make-it-blink-html-tutorial-how-to-use-the-blink-tag-with-code-examples/)
* [Bases de HTML : Un cours complet gratuit](https://www.freecodecamp.org/news/html-full-course-for-beginners/)
* [Le manuel HTML](https://www.freecodecamp.org/news/the-html-handbook/)

### CSS

* [Tutoriel sur la taille de police CSS – Comment changer la taille du texte en HTML](https://www.freecodecamp.org/news/css-font-size-tutorial-how-to-change-text-size-in-html/)
* [Tutoriel sur la couleur de fond HTML – Comment changer la couleur de fond d'une div, expliqué avec des exemples de code](https://www.freecodecamp.org/news/html-background-color-tutorial-how-to-change-a-div-background-color-explained-with-code-examples/)
* [Guide CSS en ligne – Comment styliser une balise HTML directement](https://www.freecodecamp.org/news/inline-css-guide-how-to-style-an-html-tag-directly/)
* [Texte centré HTML – Comment aligner verticalement une div avec CSS](https://www.freecodecamp.org/news/html-center-text-how-to-css-vertical-align-a-div/)
* [Comment centrer n'importe quoi avec CSS - Aligner une div, du texte, et plus](https://www.freecodecamp.org/news/how-to-center-anything-with-css-align-a-div-text-and-more/)
* [HTML vs Body : Comment définir la largeur et la hauteur pour une taille de page complète](https://www.freecodecamp.org/news/html-page-width-height/)
* [Tutoriel sur l'ombre de boîte CSS – Comment ajouter une ombre portée à n'importe quel élément HTML](https://www.freecodecamp.org/news/css-tutorial-drop-shadow/)
* [Comment fonctionne le positionnement CSS et Flexbox – Expliqué avec des exemples](https://www.freecodecamp.org/news/css-positioning-and-flexbox-explained/)
* [Flexbox - L'antisèche ultime de CSS Flex (avec des diagrammes animés !)](https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/)
* [Une introduction à la mise en page CSS Grid (avec des exemples)](https://www.freecodecamp.org/news/intro-to-css-grid-layout/)
* [Apprendre CSS Grid en construisant 5 mises en page en 17 minutes](https://www.freecodecamp.org/news/learn-css-grid-by-building-5-layouts/)
* [Comment CSS Grid change la façon dont nous pensons à structurer notre contenu](https://www.freecodecamp.org/news/css-grid-changes-how-we-can-think-about-structuring-our-content/)
* [Flexbox vs Grid - Comment construire les mises en page HTML les plus courantes](https://www.freecodecamp.org/news/flexbox-vs-grid-how-to-build-the-most-common-html-layouts/)
* [Apprendre CSS dans ce cours vidéo gratuit de 6 heures](https://www.freecodecamp.org/news/learn-css-in-this-free-6-hour-video-course/)
* [Le manuel CSS : Un guide pratique de CSS pour les développeurs](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/)

### Comment apprendre la programmation

En essence, la programmation est la façon dont les humains disent aux ordinateurs quoi faire. Qu'il s'agisse d'un ordinateur portable, d'un smartphone ou d'un navigateur, la programmation et les langages de programmation nous donnent un moyen d'interagir avec ces appareils.

Dans cette section, vous apprendrez les bases de la programmation et les bases de certains des langages de programmation les plus populaires aujourd'hui.

Si vous voulez apprendre le développement frontend et backend, apprenez définitivement JavaScript et Node.js. Et une fois que vous êtes familiarisé avec ceux-ci, regardez TypeScript.

Si vous êtes plus intéressé par la science des données et le machine learning, apprenez Python. Pour les applications mobiles, il est utile de connaître Java. Développement de jeux ? C++, C#, ou même Java.

Nous avons un peu de tout, y compris des langages de programmation plus récents comme Go.

### JavaScript

* [Variables JavaScript – Un guide pour débutants sur var, const, et let](https://www.freecodecamp.org/news/javascript-variables-beginners-guide/)
* [Exemple de division de chaîne JavaScript – Comment diviser une chaîne en un tableau en JS](https://www.freecodecamp.org/news/javascript-split-string-example/)
* [TypeOf JavaScript – Comment vérifier le type d'une variable ou d'un objet en JS](https://www.freecodecamp.org/news/javascript-typeof-how-to-check-the-type-of-a-variable-or-object-in-js/)
* [Comment vérifier si un tableau JavaScript est vide ou non avec .length](https://www.freecodecamp.org/news/check-if-javascript-array-is-empty-or-not-with-length/)
* [Tutoriel sur la boucle For JS – Comment itérer sur un tableau en JavaScript](https://www.freecodecamp.org/news/javascript-loop-tutorial-how-to-iterate-over-an-array-in-javascript/)
* [Tri de tableau JavaScript – Comment utiliser les méthodes de tri JS (avec des exemples de code)](https://www.freecodecamp.org/news/javascript-array-sort-tutorial-how-to-use-js-sort-methods-with-code-examples/)
* [Inverser un tableau JavaScript – Tutoriel avec exemple de code JS](https://www.freecodecamp.org/news/javascript-array-reverse-tutorial-with-example-js-code/)
* [JavaScript forEach – Comment parcourir un tableau en JS](https://www.freecodecamp.org/news/javascript-foreach-how-to-loop-through-an-array-in-js/)
* [JavaScript Array Slice vs Splice : la différence expliquée avec un gâteau](https://www.freecodecamp.org/news/javascript-array-slice-vs-splice-whats-the-difference/)
* [Tutoriel sur les clés d'objet JavaScript – Comment utiliser une paire clé-valeur JS](https://www.freecodecamp.org/news/javascript-object-keys-tutorial-how-to-use-a-js-key-value-pair/)
* [Créer un objet JavaScript – Comment définir des objets en JS](https://www.freecodecamp.org/news/javascript-create-object-how-to-define-objects-in-js/)
* [Programmation orientée objet en JavaScript – Expliqué avec des exemples](https://www.freecodecamp.org/news/how-javascript-implements-oop/)
* [Le mot-clé `this` en JavaScript + 5 règles de liaison clés expliquées pour les débutants JS](https://www.freecodecamp.org/news/javascript-this-keyword-binding-rules/)
* [Un guide pour débutants sur le prototype de JavaScript](https://www.freecodecamp.org/news/a-beginners-guide-to-javascripts-prototype/)
* [Date actuelle en JavaScript – Comment obtenir la date actuelle en JavaScript](https://www.freecodecamp.org/news/javascript-date-now-how-to-get-the-current-date-in-javascript/)
* [Le guide ultime de JavaScript Date et Moment.js](https://www.freecodecamp.org/news/the-ultimate-guide-to-javascript-date-and-moment-js/)
* [Qu'est-ce que la programmation fonctionnelle ? Un guide pour débutants en JavaScript](https://www.freecodecamp.org/news/javascript-array-reverse-tutorial-with-example-js-code/)
* [Apprendre JavaScript - Cours complet de 134 parties pour débutants](https://www.freecodecamp.org/news/learn-javascript-full-course/)
* [Structures de données et algorithmes en JavaScript - Cours complet pour débutants](https://www.freecodecamp.org/news/data-structures-and-algorithms-in-javascript/)
* [Tableaux clairsemés vs tableaux denses en JavaScript — Expliqué avec des exemples](https://www.freecodecamp.org/news/sparse-and-dense-arrays-in-javascript/)
* [Exemple de correspondance Regex JavaScript — Comment utiliser JS Replace sur une chaîne](https://www.freecodecamp.org/news/javascript-regex-match-example-how-to-use-the-js-replace-method-on-a-string/)
* [Un guide rapide et simple des expressions régulières JavaScript](https://www.freecodecamp.org/news/a-quick-and-simple-guide-to-javascript-regular-expressions-48b46a68df29/)
* [Liste des codes clés JavaScript — Codes clés d'événement de pression de touche pour Entrée, Espace, Retour arrière, et plus](https://www.freecodecamp.org/news/javascript-keycode-list-keypress-event-key-codes/)
* [Destructuration d'objet JavaScript, Syntaxe de propagation, et le paramètre Rest — Un guide pratique](https://www.freecodecamp.org/news/javascript-object-destructuring-spread-operator-rest-parameter/)
* [Comment fonctionne l'opérateur de coalescence nulle en JavaScript](https://www.freecodecamp.org/news/nullish-coalescing-operator-in-javascript/)
* [Try/Catch en JavaScript — Comment gérer les erreurs en JS](https://www.freecodecamp.org/news/try-catch-in-javascript/)
* [Comment utiliser Async/Await en JavaScript avec exemple de code JS](https://www.freecodecamp.org/news/async-await-in-javascript/)
* [Comment fonctionne l'opérateur de point d'interrogation (?) en JavaScript](https://www.freecodecamp.org/news/how-the-question-mark-works-in-javascript/)
* [Tutoriel sur l'opérateur ternaire JavaScript If Statement](https://www.freecodecamp.org/news/ternary-operator-javascript-if-statement-tutorial/)
* [Debounce — Comment retarder une fonction en JavaScript (exemple JS ES6)](https://www.freecodecamp.org/news/javascript-debounce-example/)
* [Comment trouver le nombre de voyelles dans une chaîne avec JavaScript](https://www.freecodecamp.org/news/find-the-number-of-vowels-in-a-string-with-javascript/)
* [Validation des données — Comment vérifier l'entrée utilisateur sur les formulaires HTML avec exemple de code JavaScript](https://www.freecodecamp.org/news/form-validation-with-html5-and-javascript/)
* [Qu'est-ce que la récursivité ? Une fonction récursive expliquée avec des exemples de code JavaScript](https://www.freecodecamp.org/news/what-is-recursion-in-javascript/)
* [Les compétences JavaScript dont vous avez besoin pour React (+ exemples pratiques)](https://www.freecodecamp.org/news/javascript-skills-you-need-for-react-practical-examples/)
* [Fonctions d'ordre supérieur en JavaScript — Atteignez de nouveaux sommets dans votre code JS](https://www.freecodecamp.org/news/higher-order-functions-in-javascript-examples/)
* [Exports de modules Node expliqués — Avec des exemples de fonctions d'exportation JavaScript](https://www.freecodecamp.org/news/node-module-exports-explained-with-javascript-export-function-examples/)
* [Comment créer une page de destination en utilisant HTML, SCSS, et JavaScript](https://www.freecodecamp.org/news/how-to-make-a-landing-page-using-html-scss-and-javascript/)
* [Comment construire et valider de beaux formulaires avec HTML, CSS, & JS vanille](https://www.freecodecamp.org/news/build-and-validate-beautiful-forms-with-vanilla-html-css-js/)
* [Comment construire une barre de progression réactive et dynamique avec HTML, CSS, et JavaScript](https://www.freecodecamp.org/news/how-to-build-a-responsive-and-dynamic-progress-bar/)
* [Le manuel JavaScript pour débutants](https://www.freecodecamp.org/news/the-complete-javascript-handbook-f26b2c71719c/)

### Node.js

* [Comment installer Node.js et npm sur Windows](https://www.freecodecamp.org/news/how-to-install-node-js-and-npm-on-windows/)
* [Comment installer Node.js sur Ubuntu et mettre à jour npm vers la dernière version](https://www.freecodecamp.org/news/how-to-install-node-js-on-ubuntu-and-update-npm-to-the-latest-version/)
* [Exports de modules Node expliqués — Avec des exemples de fonctions d'exportation JavaScript](https://www.freecodecamp.org/news/node-module-exports-explained-with-javascript-export-function-examples/)
* [Antisèche npm - Commandes les plus courantes et nvm](https://www.freecodecamp.org/news/npm-cheat-sheet-most-common-commands-and-nvm/)
* [Qu'est-ce que npm ? Un tutoriel sur le gestionnaire de paquets Node pour débutants](https://www.freecodecamp.org/news/what-is-npm-a-node-package-manager-tutorial-for-beginners/)
* [Comment ignorer des fichiers de votre package npm](https://www.freecodecamp.org/news/how-to-ignore-files-from-your-npm-package-4724e6d9575d/)
* [Comment publier des paquets sur npm (la manière dont l'industrie fait les choses)](https://www.freecodecamp.org/news/how-to-publish-packages-to-npm-the-way-the-industry-does-things-2077ec34d7e8/)
* [Comment créer un beau et petit package npm et le publier](https://www.freecodecamp.org/news/how-to-make-a-beautiful-tiny-npm-package-and-publish-it-2881d4307f78/)
* [Comment forcer l'utilisation de Yarn ou NPM](https://www.freecodecamp.org/news/how-to-force-use-yarn-or-npm/)
* [Comment activer la syntaxe ES6 (et au-delà) avec Node et Express](https://www.freecodecamp.org/news/how-to-enable-es6-and-beyond-syntax-with-node-and-express-68d3e11fe1ab/)
* [Comment automatiser des tâches simples avec Node.js](https://www.freecodecamp.org/news/automate-simple-tasks-with-nodejs/)
* [La liste de contrôle ultime de Node.js pour la production](https://www.freecodecamp.org/news/node-js-production-checklist/)
* [Comment commencer avec GraphQL et Node.js](https://www.freecodecamp.org/news/get-started-with-graphql-and-nodejs/)

### TypeScript

* [Comment installer et commencer à utiliser TypeScript](https://www.freecodecamp.org/news/how-to-install-and-begin-using-typescript/)
* [Comment ajouter TypeScript à un projet JavaScript](https://www.freecodecamp.org/news/how-to-add-typescript-to-a-javascript-project/)
* [Apprendre les types de données TypeScript – De zéro à héros](https://www.freecodecamp.org/news/learn-typescript-data-types-from-zero-to-hero/)
* [Tout sur les membres statiques TypeScript | TypeScript OOP](https://www.freecodecamp.org/news/all-about-typescript-static-members-typescript-oop/)
* [Non, les getters et setters en TypeScript & JavaScript ne sont pas inutiles](https://www.freecodecamp.org/news/typescript-javascript-getters-and-setters-are-they-useless/)
* [Un cours accéléré en TypeScript](https://www.freecodecamp.org/news/a-crash-course-in-typescript-e6bf9c10946/)
* [Types TypeScript expliqués – Un modèle mental pour vous aider à penser en types](https://www.freecodecamp.org/news/a-mental-model-to-think-in-typescript-2/)
* [L'antisèche React TypeScript – Comment configurer les types sur les hooks](https://www.freecodecamp.org/news/react-typescript-how-to-set-up-types-on-hooks/)
* [Comment les génériques TypeScript vous aident à écrire moins de code](https://www.freecodecamp.org/news/make-typescript-easy-using-basic-ts-generics/)
* [Comment créer une excellente expérience utilisateur avec React, TypeScript, et la bibliothèque de test React](https://www.freecodecamp.org/news/ux-studies-with-react-typescript-and-testing-library/)
* [Antisèche des types TypeScript avancés (avec exemples)](https://www.freecodecamp.org/news/advanced-typescript-types-cheat-sheet-with-examples/)
* [Un guide pratique de TypeScript – Comment construire une application Pokedex en utilisant HTML, CSS, et TypeScript](https://www.freecodecamp.org/news/a-practical-guide-to-typescript-how-to-build-a-pokedex-app-using-html-css-and-typescript/)
* [Comment construire une application Todo avec React, TypeScript, NodeJS, et MongoDB](https://www.freecodecamp.org/news/how-to-build-a-todo-app-with-react-typescript-nodejs-and-mongodb/)
* [Comment construire un chatbot RocketChat avec TypeScript](https://www.freecodecamp.org/news/how-to-build-a-rocketchat-bot-with-typescript/)
* [Le manuel définitif de TypeScript](https://www.freecodecamp.org/news/the-definitive-typescript-handbook/)
* [Apprendre TypeScript avec ce cours accéléré](https://www.freecodecamp.org/news/learn-typescript-with-this-crash-course/)
* [Comment construire une application de quiz en utilisant React et TypeScript](https://www.freecodecamp.org/news/how-to-build-a-quiz-app-using-react-and-typescript/)
* [Construire un panier d'achat avec React et TypeScript](https://www.freecodecamp.org/news/build-a-shopping-cart-with-react-and-typescript/)
* [Comment utiliser Typescript dans React](https://www.freecodecamp.org/news/typescript-in-react/)

### Deno

* [Apprendre Deno, une alternative à Node.js](https://www.freecodecamp.org/news/learn-deno-a-node-js-alternative/)
* [Comment construire des applications React avec Deno en utilisant la bibliothèque AlephJS](https://www.freecodecamp.org/news/build-react-app-using-deno-and-alephjs/)
* [Comment construire un raccourcisseur d'URL dans Deno](https://www.freecodecamp.org/news/build-a-url-shortener-in-deno/)
* [Comment créer une API Todo dans Deno et Oak](https://www.freecodecamp.org/news/create-a-todo-api-in-deno-written-by-a-guy-coming-from-node/)
* [Le manuel Deno : Un tutoriel de runtime TypeScript avec des exemples de code](https://www.freecodecamp.org/news/the-deno-handbook/)
* [Sécuriser les API RESTful Node.js avec les JSON Web Tokens](https://www.freecodecamp.org/news/securing-node-js-restful-apis-with-json-web-tokens-9f811a92bb52/)
* [Apprendre Node.js et commencer à exécuter JavaScript en dehors du navigateur](https://www.freecodecamp.org/news/getting-started-with-node-js/)

### Python

* [Tutoriel de programmation Hello World pour Python](https://www.freecodecamp.org/news/hello-world-programming-tutorial-for-python/)
* [Tutoriel sur la boucle While Python – Exemples de syntaxe While True et boucles infinies](https://www.freecodecamp.org/news/python-while-loop-tutorial/)
* [Nouvelle ligne Python et comment imprimer en Python sans nouvelle ligne](https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/)
* [Dictionnaires Python 101 : Une introduction visuelle détaillée](https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/)
* [Ensembles Python : Une introduction visuelle détaillée](https://www.freecodecamp.org/news/python-sets-detailed-visual-introduction/)
* [Lire un fichier JSON en Python – Comment charger JSON à partir d'un fichier et analyser les dumps](https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/)
* [Guide Python pour lister les fichiers dans un répertoire - listdir VS system("ls") expliqué avec des exemples](https://www.freecodecamp.org/news/python-list-files-in-a-directory-guide-listdir-vs-system-ls-explained-with-examples/)
* [Écrire dans un fichier Python – Ouvrir, Lire, Ajouter, et autres fonctions de gestion de fichiers expliquées](https://www.freecodecamp.org/news/python-write-to-file-open-read-append-and-other-file-handling-functions-explained/)
* [Tutoriel sur la liste vide Python – Comment créer une liste vide en Python](https://www.freecodecamp.org/news/python-empty-list-tutorial-how-to-create-an-empty-list-in-python/)
* [Ajouter à une liste Python – Comment ajouter un élément à un tableau, expliqué avec des exemples](https://www.freecodecamp.org/news/python-list-append-how-to-add-an-element-to-an-array-explained-with-examples/)
* [Ajouter à une liste Python VS Étendre une liste Python – La différence expliquée avec des exemples de méthodes de tableau](https://www.freecodecamp.org/news/python-list-append-vs-python-list-extend/)
* [La méthode de tri de liste Python – Tri ascendant et descendant expliqué avec des exemples](https://www.freecodecamp.org/news/the-python-sort-list-array-method-ascending-and-descending-explained-with-examples/)
* [Liste unique Python – Comment obtenir toutes les valeurs uniques dans une liste ou un tableau](https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/)
* [Valeurs truthy et falsy en Python : Une introduction détaillée](https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/)
* [L'opérateur modulo Python - Que signifie le symbole % en Python ? (Résolu)](https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/)
* [Le module datetime de Python – Comment gérer les dates en Python](https://www.freecodecamp.org/news/python-datetime-module/)
* [Comment gérer les exceptions en Python : Une introduction visuelle détaillée](https://www.freecodecamp.org/news/exception-handling-python/)
* [Le décorateur @property en Python : Ses cas d'utilisation, avantages, et syntaxe](https://www.freecodecamp.org/news/python-property-decorator/)
* [La fonction sleep de Python – Comment faire attendre Python quelques secondes avant de continuer, avec des commandes d'exemple](https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/)
* [Objets mutables vs immutables en Python – Un guide visuel et pratique](https://www.freecodecamp.org/news/mutable-vs-immutable-objects-python/)
* [Comment construire votre tout premier package Python](https://www.freecodecamp.org/news/build-your-first-python-package/)
* [Guide des dictionnaires Python – Comment itérer, copier, et fusionner des dictionnaires en Python 3.9](https://www.freecodecamp.org/news/python-dictionary-guide/)
* [Recherche binaire en Python : Une introduction visuelle](https://www.freecodecamp.org/news/binary-search-in-python-visual-introduction/)
* [Python multithreadé : Se faufiler à travers un goulot d'étranglement I/O ?](https://www.freecodecamp.org/news/multithreaded-python/)
* [Comment configurer un environnement virtuel Python sur Ubuntu 20.04](https://www.freecodecamp.org/news/how-to-set-up-python-virtual-environment-on-ubuntu-20-04/)
* [Comment configurer Virtualenv avec Virtualenvwrapper sur Ubuntu 18.04](https://www.freecodecamp.org/news/virtualenv-with-virtualenvwrapper-on-ubuntu-18-04/)
* [Installer plusieurs versions de Python sur Windows en utilisant Virtualenv](https://www.freecodecamp.org/news/installing-multiple-python-versions-on-windows-using-virtualenv/)
* [Passez vos compétences Python au niveau supérieur avec ce cours vidéo gratuit de 6 heures](https://www.freecodecamp.org/news/intermediate-python-course/)
* [Le manuel Python](https://www.freecodecamp.org/news/the-python-handbook/)

### Java

* [Java String vers Int – Comment convertir une chaîne en entier](https://www.freecodecamp.org/news/java-string-to-int-how-to-convert-a-string-to-an-integer/)
* [Tutoriel sur les méthodes de liste Java – Exemple d'API Util List](https://www.freecodecamp.org/news/java-list-tutorial-util-list-api-example/)
* [Méthodes de tableau Java – Comment imprimer un tableau en Java](https://www.freecodecamp.org/news/java-array-methods-how-to-print-an-array-in-java/)
* [Utilisation de Arrays.sort() de Java pour toute liste d'objets](https://www.freecodecamp.org/news/utilizing-javas-arrays-sort-for-any-list-of-objects-e3e2db61d70b/)
* [Comment gérer NullPointerException en Java](https://www.freecodecamp.org/news/how-to-handle-nullpointerexception-in-java/)
* [Files d'attente de priorité en Java expliquées avec des exemples](https://www.freecodecamp.org/news/priority-queue-implementation-in-java/)
* [Principes de programmation orientée objet en Java : Concepts OOP pour débutants](https://www.freecodecamp.org/news/java-object-oriented-programming-system-principles-oops-concepts-for-beginners/)
* [Tutoriel sur le polymorphisme en Java – Avec exemple de code de programmation orientée objet](https://www.freecodecamp.org/news/polymorphism-in-java-tutorial-with-object-oriented-programming-example-code/)
* [Apprendre la programmation fonctionnelle en Java - Cours complet](https://www.freecodecamp.org/news/functional-programming-in-java-course/)
* [Multithreading en Java : Comment commencer avec les threads](https://www.freecodecamp.org/news/how-to-get-started-with-multithreading-in-java/)
* [Générateur de nombres aléatoires Java – Comment générer des entiers avec Math Random](https://www.freecodecamp.org/news/generate-random-numbers-java/)
* [Collecte des déchets en Java – Qu'est-ce que GC et comment cela fonctionne dans la JVM](https://www.freecodecamp.org/news/garbage-collection-in-java-what-is-gc-and-how-it-works-in-the-jvm/)
* [Tutoriel JVM - Architecture de la machine virtuelle Java expliquée pour les débutants](https://www.freecodecamp.org/news/jvm-tutorial-java-virtual-machine-architecture-explained-for-beginners/)
* [Construire une application Android Java utilisant une API REST - Données réseau dans Android](https://www.freecodecamp.org/news/java-android-app-using-rest-api-network-data-in-android-course/)
* [Comment configurer l'autorisation et l'authentification JWT Java Spring Boot](https://www.freecodecamp.org/news/how-to-setup-jwt-authorization-and-authentication-in-spring/)
* [Tutoriel JVM - Architecture de la machine virtuelle Java expliquée pour les débutants](https://www.freecodecamp.org/news/jvm-tutorial-java-virtual-machine-architecture-explained-for-beginners/)
* [Utiliser Spring Boot et Java pour créer une API Rest (Tutoriel)](https://www.freecodecamp.org/news/use-spring-boot-and-java-to-create-a-rest-api-tutorial/)
* [Comment construire un jeu Sudoku Java Desktop Application – Un cours gratuit de 2 heures](https://www.freecodecamp.org/news/build-a-sudoku-java-desktop-application/)

### Go (Golang)

* [Langage de programmation Go (Golang)](https://www.freecodecamp.org/news/go-golang-programming-language/)
* [Apprendre Go — De zéro à héros](https://www.freecodecamp.org/news/learning-go-from-zero-to-hero-d2a3223b3d86/)
* [Comment automatiser votre README de profil GitHub](https://www.freecodecamp.org/news/go-automate-your-github-profile-readme/)
* [Comment construire votre propre liste d'abonnés serverless avec Go et AWS](https://www.freecodecamp.org/news/build-your-own-serverless-subscriber-list-with-go-and-aws/)
* [Comment valider les certificats SSL dans Go](https://www.freecodecamp.org/news/how-to-validate-ssl-certificates-in-go/)
* [Comment concevoir un magasin clé-valeur transactionnel dans Go](https://www.freecodecamp.org/news/design-a-key-value-store-in-go/)
* [Comment j'ai construit un serveur web en utilisant Go — et sur ChromeOS](https://www.freecodecamp.org/news/how-i-built-a-web-server-using-go-and-on-chromeos-3b83e4c2da5f/)
* [Comment configurer le streaming côté serveur gRPC avec Go](https://www.freecodecamp.org/news/grpc-server-side-streaming-with-go/)
* [Comment configurer un projet réel avec Go et Vue](https://www.freecodecamp.org/news/how-i-set-up-a-real-world-project-with-go-and-vue/)
* [Comment implémenter Elasticsearch dans Go](https://www.freecodecamp.org/news/go-elasticsearch/)
* [Comment implémenter Heap-Sort dans la bibliothèque standard Go](https://www.freecodecamp.org/news/reading-challenge-heap-sort-in-go/)
* [Apprendre le langage de programmation Go (Golang) rapide et simple en 7 heures](https://www.freecodecamp.org/news/go-golang-course/)
* [Apprendre Go dans ce cours accéléré](https://www.freecodecamp.org/news/learn-go-in-this-crash-course/)

### Rust

* [Rust pour débutants – Commencez avec le langage de programmation le plus aimé](https://www.freecodecamp.org/news/rust-getting-started-with-the-most-loved-programming-language/)
* [Comment apprendre Rust sans installer de logiciel](https://www.freecodecamp.org/news/learn-rust-with-github-actions/)
* [Tutoriel sur le langage de programmation Rust – Comment construire une application de liste de tâches](https://www.freecodecamp.org/news/how-to-build-a-to-do-app-with-rust/)
* [Comment construire des serveurs GraphQL puissants avec Rust](https://www.freecodecamp.org/news/building-powerful-graphql-servers-with-rust/)

### C

* [Boostez vos compétences en programmation en lisant le code de Git](https://www.freecodecamp.org/news/boost-programming-skills-read-git-code/)
* [Spécificateurs de format en C](https://www.freecodecamp.org/news/format-specifiers-in-c/)
* [Gestion de fichiers en C — Comment ouvrir, fermer et écrire dans des fichiers](https://www.freecodecamp.org/news/file-handling-in-c-how-to-open-close-and-write-to-files/)

### C++

* [Comment fonctionnent les classes en C++](https://www.freecodecamp.org/news/how-classes-work-in-cplusplus/)
* [Boucles Do While en C++ avec exemple de syntaxe de boucle](https://www.freecodecamp.org/news/do-while-loops-in-c-plus-plus-example-loop-syntax/)
* [Comment surcharger les opérateurs en C++](https://www.freecodecamp.org/news/how-to-overload-operators-in-cplusplus/)
* [C++ Map expliqué avec des exemples](https://www.freecodecamp.org/news/c-plus-plus-map-explained-with-examples/)
* [Comment écrire du code propre en C++](https://www.freecodecamp.org/news/how-to-write-clean-code-in-c/)
* [Comment compiler votre code C++ dans Visual Studio Code](https://www.freecodecamp.org/news/how-to-compile-your-c-code-in-visual-studio-code/)
* [Apprendre la programmation orientée objet (OOP) en C++ | Cours vidéo complet](https://www.freecodecamp.org/news/learn-object-oriented-programming-oop-in-c-full-video-course/)

### C#

* [Programmation C# : Une introduction pour débutants](https://www.freecodecamp.org/news/csharp/)
* [Bases de C# - Votre premier programme C#, types et variables, et instructions de contrôle de flux](https://www.freecodecamp.org/news/c-basics-your-first-c-program-types-and-variables-and-flow-control-statements/)
* [Le mot-clé interne C# est-il une mauvaise odeur de code ?](https://www.freecodecamp.org/news/is-the-c-internal-keyword-a-code-smell/)
* [Comment construire une SPA avec Vue.js et C# en utilisant .NET Core](https://www.freecodecamp.org/news/how-to-build-an-spa-with-vuejs-and-c-using-net-core/)
* [Apprendre C# et Unity en créant des jeux de table numériques](https://www.freecodecamp.org/news/learn-c-and-unity-by-making-digital-tabletop-games/)
* [Créer une application C# de A à Z - Cours complet de 24 heures](https://www.freecodecamp.org/news/c-sharp-24-hour-course/)

## Comment apprendre Linux

Que vous le sachiez ou non, vous utilisez probablement Linux tous les jours. Android est basé sur Linux, et macOS, qui est basé sur Unix comme Linux, est un cousin proche. Et une estimation de [74,2 %](https://w3techs.com/technologies/overview/operating_system) (en mars 2021) de tous les serveurs web fonctionnent sous Unix, dont la grande majorité sont probablement Linux.

En bref, si vous travaillez sur le web, vous devriez vous familiariser avec Linux et son shell par défaut, Bash. Et voici quelques-uns de nos meilleurs tutoriels pour commencer :

* [Commandes Linux - Conseils de base sur la ligne de commande Bash que vous devriez connaître](https://www.freecodecamp.org/news/basic-linux-commands-bash-tips-you-should-know/)
* [La commande Cat dans Linux – Concaténation expliquée avec des exemples Bash](https://www.freecodecamp.org/news/the-cat-command-in-linux-concatenation-explained-with-bash-examples/)
* [La commande Cat dans Linux – Comment créer un fichier texte avec Cat ou Touch](https://www.freecodecamp.org/news/the-cat-command-in-linux-how-to-create-a-text-file-with-cat-or-touch/)
* [Tutoriel sur la commande Grep – Comment rechercher un fichier dans Linux et Unix avec Find récursif](https://www.freecodecamp.org/news/grep-command-tutorial-how-to-search-for-a-file-in-linux-and-unix/)
* [Linux : Comment ajouter des utilisateurs et créer des utilisateurs avec useradd](https://www.freecodecamp.org/news/linux-how-to-add-users-and-create-users-with-useradd/)
* [Groupes d'utilisateurs Linux expliqués : Comment ajouter un nouveau groupe, un nouveau membre de groupe, et changer de groupes](https://www.freecodecamp.org/news/linux-user-groups-explained-how-to-add-a-new-group-a-new-group-member-and-change-groups/)
* [La commande LS de Linux – Comment lister les fichiers dans un répertoire + indicateurs d'option](https://www.freecodecamp.org/news/the-linux-ls-command-how-to-list-files-in-a-directory-with-options/)
* [Tar dans Linux – Exemples de commandes Tar GZ, Tar File, Tar Directory, et Tar Compress](https://www.freecodecamp.org/news/tar-in-linux-example-tar-gz-tar-file-and-tar-directory-and-tar-compress-commands/)
* [La commande Tar dans Linux : Tar CVF et Tar XVF expliqués avec des commandes d'exemple](https://www.freecodecamp.org/news/tar-command-linux-tar-cvf-tar-xvf/)
* [Tutoriel sur les liens symboliques dans Linux – Comment créer et supprimer un lien symbolique](https://www.freecodecamp.org/news/symlink-tutorial-in-linux-how-to-create-and-remove-a-symbolic-link/)
* [Gestion des paquets Linux avec Snaps](https://www.freecodecamp.org/news/linux-package-management-with-snaps/)
* [Comment construire votre propre gestionnaire de fichiers Linux Dotfiles à partir de zéro](https://www.freecodecamp.org/news/build-your-own-dotfiles-manager-from-scratch/)
* [Apprendre les bases de Linux et comment il peut être utilisé par les hackers éthiques](https://www.freecodecamp.org/news/linux-for-ethical-hackers-course/)
* [Comment configurer et exploiter des serveurs Linux - Cours complet](https://www.freecodecamp.org/news/linux-server-course-system-configuration-and-operation/)
* [Le manuel des commandes Linux](https://www.freecodecamp.org/news/the-linux-commands-handbook/)

## Comment apprendre Git et le contrôle de version

Une fois que vos programmes commencent à croître en taille et en complexité, vous voudrez un moyen de suivre vos modifications au cas où vous devriez revenir à une version antérieure.

Git vous permet de faire exactement cela, et est le logiciel de contrôle de version le plus populaire utilisé aujourd'hui. Si vous voulez collaborer avec d'autres développeurs et obtenir un emploi dans l'industrie, il est important de savoir comment Git fonctionne.

Certains de nos meilleurs articles sur Git sont listés ci-dessous. De plus, lorsque vous utilisez Git, ce sera probablement via la ligne de commande, alors assurez-vous de connaître quelques bases de Linux / Bash avant de plonger.

* [Qu'est-ce que Git ? Un guide pour débutants sur le contrôle de version Git](https://www.freecodecamp.org/news/what-is-git-learn-git-version-control/)
* [Apprendre Git et le contrôle de version en une heure](https://www.freecodecamp.org/news/learn-git-and-version-control-in-an-hour/)
* [Git vs GitHub – Qu'est-ce que le contrôle de version et comment cela fonctionne-t-il ?](https://www.freecodecamp.org/news/git-and-github-overview/)
* [Qu'est-ce que GitHub ? Qu'est-ce que Git ? Et comment utiliser ces outils de développeur](https://www.freecodecamp.org/news/what-is-github-what-is-git-and-how-to-use-these-developer-tools/)
* [Commandes Git que vous devriez connaître, avec des exemples de code](https://www.freecodecamp.org/news/5-git-commands-you-should-know-with-code-examples/)
* [Antisèche Git – 50 commandes Git que vous devriez connaître](https://www.freecodecamp.org/news/git-cheat-sheet/)
* [Git Reset vers la tête distante – Comment réinitialiser une branche distante vers l'origine](https://www.freecodecamp.org/news/git-reset-to-remote-head-how-to-reset-a-remote-branch-to-origin/)
* [Tutoriel Git Checkout Remote Branch](https://www.freecodecamp.org/news/git-checkout-remote-branch-tutorial/)
* [Comment utiliser les branches dans Git – l'antisèche ultime](https://www.freecodecamp.org/news/how-to-use-branches-in-git/)
* [Un guide pour débutants sur Git – Comment écrire un bon message de commit](https://www.freecodecamp.org/news/a-beginners-guide-to-git-how-to-write-a-good-commit-message/)
* [Comment écrire de bons messages de commit : Un guide pratique Git](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
* [Un guide pour débutants sur Git – Qu'est-ce qu'un journal des modifications et comment le générer](https://www.freecodecamp.org/news/a-beginners-guide-to-git-what-is-a-changelog-and-how-to-generate-it/)
* [Comment obtenir et configurer vos clés SSH Git et GitHub](https://www.freecodecamp.org/news/git-ssh-how-to/)
* [Comment utiliser plusieurs configurations Git sur un seul ordinateur](https://www.freecodecamp.org/news/how-to-handle-multiple-git-configurations-in-one-machine/)
* [Comment comprendre et résoudre les conflits dans Git](https://www.freecodecamp.org/news/how-to-handle-merge-conflicts-in-git/)
* [Comment annuler les erreurs avec Git](https://www.freecodecamp.org/news/how-to-undo-mistakes-with-git/)
* [Comment utiliser les alias Git pour augmenter votre productivité](https://www.freecodecamp.org/news/how-to-use-git-aliases/)
* [Git Reset expliqué – Comment sauver la journée avec la commande Reset](https://www.freecodecamp.org/news/save-the-day-with-git-reset/)
* [Secrets Git : 7 commandes que vous ne connaissez peut-être pas](https://www.freecodecamp.org/news/7-git-commands-you-might-not-know/)
* [Comment désengager les fichiers sensibles de Git](https://www.freecodecamp.org/news/how-to-uncommit-sensitive-files-from-git/)
* [Git Pull Force – Comment écraser les modifications locales avec Git](https://www.freecodecamp.org/news/git-pull-force-how-to-overwrite-local-changes-with-git/)
* [Git Clone Branch – Comment cloner une branche spécifique](https://www.freecodecamp.org/news/git-clone-branch-how-to-clone-a-specific-branch/)
* [Comment basculer entre les problèmes dans votre dépôt Git local](https://www.freecodecamp.org/news/how-to-switch-between-issues-in-git/)
* [Comment synchroniser votre fork avec le dépôt Git original](https://www.freecodecamp.org/news/how-to-sync-your-fork-with-the-original-git-repository/)
* [Cours accéléré sur Git et GitHub](https://www.freecodecamp.org/news/git-and-github-crash-course/)

## Comment apprendre un Framework / Bibliothèque Frontend

Une fois que vous savez comment construire des sites web de base avec HTML, CSS et JavaScript, améliorez vos compétences en apprenant un framework / bibliothèque frontend. Parmi ceux-ci, les trois plus populaires sont React, Vue et Angular.

Angular est considéré comme un framework car il inclut beaucoup de choses comme le routage dès le départ.

React, en revanche, est généralement appelé une bibliothèque car il ne vient pas avec beaucoup de choses par défaut. Au lieu de cela, vous devrez ajouter quelques paquets supplémentaires pour gérer le routage et autres.

Vue se situe quelque part au milieu en termes de fonctionnalité et de poids.

Quel que soit le nom que vous leur donnez, chacun a ses propres forces et faiblesses. Il n'y a pas de meilleur framework / bibliothèque – choisissez-en un qui semble le plus intéressant, ou que les entreprises de votre région recrutent, et allez-y.

### React

* [Comment installer React.js avec create-react-app](https://www.freecodecamp.org/news/install-react-with-create-react-app/)
* [Composants fonctionnels React, Props, et JSX – Tutoriel React.js pour débutants](https://www.freecodecamp.org/news/react-components-jsx-props-for-beginners/)
* [JSX dans React – Expliqué avec des exemples](https://www.freecodecamp.org/news/jsx-in-react-introduction/)
* [Tutoriel sur l'image de fond React – Comment définir backgroundImage avec le style CSS en ligne](https://www.freecodecamp.org/news/react-background-image-tutorial-how-to-set-backgroundimage-with-inline-css-style/)
* [Comment construire un menu accordéon dans React à partir de zéro – Aucune bibliothèque externe requise](https://www.freecodecamp.org/news/build-accordion-menu-in-react-without-external-libraries/)
* [Comment construire des formulaires React facilement avec react-hook-form](https://www.freecodecamp.org/news/how-to-build-react-forms/)
* [Comment construire vos propres hooks React : Un guide étape par étape](https://www.freecodecamp.org/news/how-to-create-react-hooks/)
* [React Testing Library – Tutoriel avec des exemples de code JavaScript](https://www.freecodecamp.org/news/react-testing-library-tutorial-javascript-example-code/)
* [Comment construire une application météo avec React et les hooks React](https://www.freecodecamp.org/news/learn-react-by-building-a-weather-app/)
* [Comment ajouter le glisser-déposer dans React avec React Beautiful DnD](https://www.freecodecamp.org/news/how-to-add-drag-and-drop-in-react-with-react-beautiful-dnd/)
* [Comment utiliser les icônes SVG dans React avec React Icons et Font Awesome](https://www.freecodecamp.org/news/how-to-use-svg-icons-in-react-with-react-icons-and-font-awesome/)
* [Comment construire une liste de courses en utilisant les hooks React (avec code de démarrage et visite guidée vidéo)](https://www.freecodecamp.org/news/how-to-build-a-shopping-list-using-react-hooks-w-starter-code-and-video-walkthrough/)
* [Construire une application de suivi de budget React – Apprendre React & Context API avec ce projet amusant](https://www.freecodecamp.org/news/react-budget-tracker-app/)
* [La meilleure structure de fichiers pour vos composants React](https://www.freecodecamp.org/news/best-file-structure-for-react-components/)
* [Antisèche des props React : 10 motifs que vous devriez connaître](https://www.freecodecamp.org/news/react-props-cheatsheet/)
* [Comment transformer Google Sheets en une API REST et l'utiliser avec une application React](https://www.freecodecamp.org/news/react-and-googlesheets/)
* [Comment récupérer des données dans React : Antisèche + Exemples](https://www.freecodecamp.org/news/fetch-data-react/)
* [Comment utiliser l'API YouTube IFrame dans React](https://www.freecodecamp.org/news/use-the-youtube-iframe-api-in-react/)
* [Comment configurer HTTPS localement avec create-react-app](https://www.freecodecamp.org/news/how-to-set-up-https-locally-with-create-react-app/)
* [Comment créer une application React avec un backend Node : Le guide complet](https://www.freecodecamp.org/news/how-to-create-a-react-app-with-a-node-backend-the-complete-guide/)
* [Comment ajouter une base de données serverless à vos projets React](https://www.freecodecamp.org/news/build-a-shopping-cart-with-react-and-typescript/)
* [La commande React Scripts Start – Les scripts npm de Create-React-App expliqués](https://www.freecodecamp.org/news/create-react-app-npm-scripts-explained/)
* [Construire un panier d'achat avec React et TypeScript](https://www.freecodecamp.org/news/build-a-shopping-cart-with-react-and-typescript/)
* [Apprendre React.js en construisant des projets – Créer une application de rappel d'anniversaire](https://www.freecodecamp.org/news/react-practice-project-birthday-reminder-app/)
* [Comment créer un démarreur Next.js pour démarrer facilement une nouvelle application React](https://www.freecodecamp.org/news/how-to-create-a-nextjs-starter-to-easily-bootstrap-a-new-react-app/)
* [Apprendre à utiliser React et GraphQL pour créer un réseau social full stack](https://www.freecodecamp.org/news/learn-how-to-use-react-and-graphql-to-make-a-full-stack-social-network/)
* [React pour débutants – Un manuel React.js pour les développeurs front-end](https://www.freecodecamp.org/news/react-beginner-handbook/)

### Vue

* [Apprendre Vue : Un tutoriel interactif Vue JS de 3 minutes](https://www.freecodecamp.org/news/learn-basic-vue-js-crash-course-guide-vue-tutorial-e3da361c635/)
* [Apprendre à utiliser le CLI Vue.js](https://www.freecodecamp.org/news/learn-how-to-use-the-vue-js-cli-8349fb23a566/)
* [Apprendre Vue.js - Cours complet pour débutants](https://www.freecodecamp.org/news/vue-js-full-course/)
* [Composants Vue : Un tutoriel interactif Vue JS](https://www.freecodecamp.org/news/vue-js-components-an-interactive-guide-1b8149ecc254/)
* [Comment utiliser le routage dans Vue.js pour créer une meilleure expérience utilisateur](https://www.freecodecamp.org/news/how-to-use-routing-in-vue-js-to-create-a-better-user-experience-98d225bbcdd9/)
* [Construire un aperçu Markdown avec Vue.js](https://www.freecodecamp.org/news/markdown-previewer-vue-js-tutorial/)
* [Comment ajouter l'internationalisation à une application Vue](https://www.freecodecamp.org/news/how-to-add-internationalization-to-a-vue-application-d9cfdcabb03b/)
* [Comment ajouter des graphiques et des diagrammes à une application Vue.js](https://www.freecodecamp.org/news/how-to-add-charts-and-graphs-to-a-vue-js-application-29f943a45d09/)
* [Comment construire un jeu de cartes mémoire avec Vue.js](https://www.freecodecamp.org/news/how-to-build-a-memory-card-game-with-vuejs/)
* [Comment créer et publier une bibliothèque de composants Vue](https://www.freecodecamp.org/news/how-to-create-and-publish-a-vue-component-library/)
* [Comment construire un générateur de personnages RPG full stack avec MongoDB, Express, Vue, et Node (la pile MEVN)](https://www.freecodecamp.org/news/build-a-full-stack-mevn-app/)
* [Comment ajouter l'authentification à une application Vue en utilisant Firebase](https://www.freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-firebase/)
* [Comment ajouter l'authentification à une application Vue en utilisant Auth0](https://www.freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-auth0/)
* [Comment ajouter l'authentification à une application Vue en utilisant AWS Amplify](https://www.freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-aws-amplify/)
* [Le manuel Vue : Une introduction approfondie à Vue.js](https://www.freecodecamp.org/news/the-vue-handbook-a-thorough-introduction-to-vue-js-1e86835d8446/)

### Angular

* [Comment installer Angular sur Windows : Un guide pour Angular CLI, Node.js, et les outils de construction](https://www.freecodecamp.org/news/how-to-install-angular-on-windows-a-guide-to-angular-cli-node-js-and-build-tools/)
* [Angular 9 pour débutants - Composants et interpolation de chaînes](https://www.freecodecamp.org/news/angular-9-for-beginners-components-and-string-interpolation/)
* [Angular 9 pour débutants — Comment installer votre première application avec Angular CLI](https://www.freecodecamp.org/news/angular-9-for-beginners-how-to-install-your-first-app-with-angular-cli/)
* [Tout ce que vous devez savoir sur ng-template, ng-content, ng-container, et *ngTemplateOutlet dans Angular](https://www.freecodecamp.org/news/everything-you-need-to-know-about-ng-template-ng-content-ng-container-and-ngtemplateoutlet-4b7b51223691/)
* [Que pourrait-il mal se passer ? Comment gérer les erreurs dans Angular](https://www.freecodecamp.org/news/global-error-handling-in-angular-with-the-help-of-the-cdk/)
* [Comment construire un validateur de formulaire générique dans Angular](https://www.freecodecamp.org/news/angular-generic-form-validator/)
* [Comment valider les formulaires pilotés par template Angular](https://www.freecodecamp.org/news/how-to-validate-angular-template-driven-forms/)
* [Comment valider les formulaires réactifs Angular](https://www.freecodecamp.org/news/how-to-validate-angular-reactive-forms/)
* [Comment créer un indicateur de chargement réutilisable pour les projets Angular](https://www.freecodecamp.org/news/how-to-create-reusable-loading-indicator-for-angular-projects-d0a11f4631e0/)
* [Comment j'ai construit un indicateur de chargement personnalisable avec les composants dynamiques Angular](https://www.freecodecamp.org/news/how-i-built-a-customizable-loading-indicator-with-angular-dynamic-components-a291310f01d/)
* [Comment créer un sondage en ligne avec ASP.NET Core, Angular 5, et Highcharts](https://www.freecodecamp.org/news/how-to-create-an-online-poll-with-asp-net-core-angular-5-and-highcharts-85ff7fecbaf1/)
* [Comment générer des codes QR dans Angular 10](https://www.freecodecamp.org/news/generate-qr-codes-in-angular-10/)
* [Utiliser Angular Material pour ajouter des composants d'interface utilisateur modernes à vos projets Angular](https://www.freecodecamp.org/news/angular-material-course/)
* [Angular RxJS en profondeur](https://www.freecodecamp.org/news/angular-rxjs-in-depth/)
* [Comment créer un lecteur de caractères optiques en utilisant Angular et Azure Computer Vision](https://www.freecodecamp.org/news/how-to-create-an-optical-character-reader-using-angular-and-azure-computer-vision/)
* [Apprendre Angular - Cours complet](https://www.freecodecamp.org/news/angular-tutorial-course/)

## Comment apprendre les bases du web et la sécurité web

Lorsque vous vous familiarisez avec la construction de sites web et d'applications web dans le framework / bibliothèque de votre choix, vous voudrez les déployer. Mais avant de mettre votre travail en ligne, il est utile de savoir comment fonctionne le web et les bases de la sécurité web.

### Bases du web

* [Comment fonctionne HTTP et pourquoi c'est important – Expliqué en anglais simple](https://www.freecodecamp.org/news/how-the-internet-works/)
* [Erreur HTTP 401 vs Erreur HTTP 403 – Réponses de code de statut expliquées](https://www.freecodecamp.org/news/http-401-error-vs-http-403-error-status-code-responses-explained/)
* [Erreur HTTP 403 Interdit : Ce que cela signifie et comment la corriger](https://www.freecodecamp.org/news/http-error-403-forbidden-what-it-means-and-how-to-fix-it/)
* [Erreur 403 Interdit expliquée - Comment puis-je corriger ce code d'erreur HTTP ?](https://www.freecodecamp.org/news/error-403-forbidden-explained-how-can-i-fix-this-http-error-code/)
* [Erreur HTTP 500 – Erreur de serveur interne expliquée en anglais simple](https://www.freecodecamp.org/news/http-error-500-internal-server-error-explained-in-plain-english/)
* [Erreur HTTP 503 Service indisponible expliquée – Ce que signifie le code d'erreur 503](https://www.freecodecamp.org/news/http-error-503-service-unavailable-explained-what-the-503-error-code-means/)
* [Une introduction approfondie à la mise en cache HTTP : Cache-control & Vary](https://www.freecodecamp.org/news/an-in-depth-introduction-to-http-caching-cache-control-vary/)
* [Une introduction à HTTP : Tout ce que vous devez savoir](https://www.freecodecamp.org/news/http-and-everything-you-need-to-know-about-it/)
* [Qu'est-ce que le modèle TCP/IP ? Couches et protocoles expliqués](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/)
* [Clé WPA, WPA2, WPA3, et clé WEP : Sécurité Wi-Fi expliquée](https://www.freecodecamp.org/news/wifi-security-explained/)
* [Qu'est-ce que TLS ? Chiffrement de la couche de transport expliqué en anglais simple](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/)

### HTTPS

* [Qu'est-ce que HTTPS ? Un guide pour la navigation web sécurisée et le chiffrement du navigateur](https://www.freecodecamp.org/news/what-is-https-a-guide-to-secure-web-browsing-and-browser-encryption/)
* [WTF est HTTPS ?](https://www.freecodecamp.org/news/wtf-is-https/)
* [Comment protéger votre site WordPress avec HTTPS en 5 étapes simples](https://www.freecodecamp.org/news/chrome-plans-to-implement-insecure-form-warnings-how-can-wordpress-plugins-help-fix-your-form/)
* [Comment rediriger HTTP vers HTTPS en utilisant .htaccess](https://www.freecodecamp.org/news/how-to-redirect-http-to-https-using-htaccess/)
* [Hébergement de site simple avec Amazon S3 et HTTPS](https://www.freecodecamp.org/news/simple-site-hosting-with-amazon-s3-and-https-5e78017f482a/)
* [HTTPS expliqué avec des pigeons voyageurs](https://www.freecodecamp.org/news/https-explained-with-carrier-pigeons-7029d2193351/)
* [Comment faire fonctionner HTTPS sur votre environnement de développement local en 5 minutes](https://www.freecodecamp.org/news/how-to-get-https-working-on-your-local-development-environment-in-5-minutes-7af615770eec/)
* [Comment ajouter HTTPS à votre site web gratuitement en 10 minutes, et pourquoi vous devez le faire maintenant plus que jamais](https://www.freecodecamp.org/news/free-https-c051ca570324/)

### Cookies

* [Sécurité web : Comment renforcer vos cookies HTTP](https://www.freecodecamp.org/news/web-security-hardening-http-cookies-be8d8d8016e1/)
* [Tout ce que vous devez savoir sur les cookies pour le développement web](https://www.freecodecamp.org/news/everything-you-need-to-know-about-cookies-for-web-development/)
* [Qu'est-ce que les cookies sur le web et comment les utilisez-vous ?](https://www.freecodecamp.org/news/what-are-cookies-on-the-web-and-how-do-you-use-them/)

## Comment apprendre les bases de données

À ce stade, vous avez probablement construit un tas de sites web et d'applications. Vous avez probablement utilisé une API pour obtenir des données sur des choses comme la météo, ou pour obtenir une citation aléatoire à afficher sur la page.

Mais si vous avez déjà voulu créer votre propre API, ou stocker des informations de vos utilisateurs, vous devrez apprendre à utiliser une base de données.

De manière générale, les bases de données se divisent en deux catégories : **relationnelles**, ou SQL, et **non relationnelles**, ou NoSQL. SQL signifie "langage de requête structuré", et est un terme large pour désigner les bases de données relationnelles. NoSQL, ou "not only SQL" désigne les bases de données non relationnelles.

Aucun type de base de données n'est meilleur ou pire que l'autre – cela dépend surtout du projet sur lequel vous travaillez, et du type de données avec lequel vous allez travailler.

Voici une liste de certains des meilleurs articles que nous avons sur les bases de données. Je ferai une note sur le fait que le système de base de données est relationnel (SQL) ou non relationnel (NoSQL) si ce n'est pas clair :

### SQL / MySQL

* [Qu'est-ce que SQL ? Qu'est-ce qu'une base de données ? Les systèmes de gestion de bases de données relationnelles (RDBMS) expliqués en anglais simple](https://www.freecodecamp.org/news/sql-and-databases-explained-in-plain-english/)
* [Pourquoi vous devriez apprendre SQL – Même si vous n'êtes pas un développeur](https://www.freecodecamp.org/news/why-learn-sql/)
* [Commandes SQL de base - La liste des requêtes et instructions de base de données que vous devriez connaître](https://www.freecodecamp.org/news/basic-sql-commands/)
* [Apprendre SQL avec ces 5 recettes faciles](https://www.freecodecamp.org/news/sql-recipes/)
* [Instruction SQL Create Table - Avec syntaxe d'exemple](https://www.freecodecamp.org/news/sql-create-table-statement-with-example-syntax/)
* [Tutoriel sur les opérateurs SQL – Exemples de requêtes d'opérateurs binaires, de comparaison, arithmétiques et logiques](https://www.freecodecamp.org/news/sql-operators-tutorial/)
* [Tutoriel sur les jointures SQL : Jointure croisée, jointure externe complète, jointure interne, jointure gauche et jointure droite](https://www.freecodecamp.org/news/sql-joins-tutorial/)
* [Clé étrangère SQL VS clé primaire expliquée avec des exemples de syntaxe MySQL](https://www.freecodecamp.org/news/sql-foreign-key-vs-primary-key-explained-with-mysql-syntax-examples/)
* [Vue SQL expliquée - Comment créer une vue en SQL et MySQL](https://www.freecodecamp.org/news/sql-create-view-mysql/)
* [L'instruction SQL Update expliquée : Requêtes pour mettre à jour les tables (y compris les exemples MySQL)](https://www.freecodecamp.org/news/the-sql-update-statement-explained/)
* [Instructions SQL Insert Into et Insert : Avec syntaxe d'exemple MySQL](https://www.freecodecamp.org/news/sql-insert-and-insert-into-statements-with-example-syntax/)
* [SQL Create Table expliqué avec des exemples de syntaxe pour MySQL et Postgres](https://www.freecodecamp.org/news/sql-create-table-explained-with-mysql-and-postgres-examples/)
* [Contrainte de vérification en SQL - Expliquée avec des exemples de syntaxe MySQL et SQL Server](https://www.freecodecamp.org/news/check-constraint-sql-server-mysql/)
* [Instruction SQL Delete Row - Comment supprimer des données d'une table avec des requêtes d'exemple](https://www.freecodecamp.org/news/sql-delete-row-statement-examples/)
* [Tutoriel SQL sur les clés primaires – Comment définir une clé primaire dans une base de données](https://www.freecodecamp.org/news/primary-key-sql-tutorial-how-to-define-a-primary-key-in-a-database/)
* [Apprendre les bases de l'injection SQL et comment protéger vos applications web](https://www.freecodecamp.org/news/learn-the-basics-of-sql-injection-and-how-to-protect-your-web-apps/)
* [Tutoriel sur l'injection SQL - Qu'est-ce que l'injection SQL et comment l'empêcher](https://www.freecodecamp.org/news/what-is-sql-injection-how-to-prevent-it/)
* [Instruction SQL Update — Exemples de requêtes pour mettre à jour les valeurs de table](https://www.freecodecamp.org/news/sql-update-statement-example-queries-for-updating-table-values/)
* [Comment s'assurer que votre base de données MySQL est sécurisée](https://www.freecodecamp.org/news/cjn-is-your-mysql-secured-7793e5444cf5/)
* [Comment créer et manipuler des bases de données SQL avec Python](https://www.freecodecamp.org/news/connect-python-with-sql/)
* [Comment construire votre première application CRUD avec Laravel et MySQL](https://www.freecodecamp.org/news/laravel-5-7-tutorial-build-your-first-crud-app-with-laravel-and-mysql-15cbd06c6cef/)
* [SQL et bases de données - Un cours complet pour débutants](https://www.freecodecamp.org/news/sql-and-databases-full-course/)

### MongoDB / Mongoose (NoSQL)

Note : Mongoose est un outil pour MongoDB qui vous permet de faire des choses comme la modélisation de données objet (ODM) pour créer des modèles ou des schémas pour vos données. Beaucoup de gens utilisent Mongoose pour interagir avec une base de données MongoDB, donc je les ai combinés ici.

* [Comment commencer avec MongoDB en 10 minutes](https://www.freecodecamp.org/news/learn-mongodb-a4ce205e7739/)
* [Comment gérer le traitement avancé des données avec le framework d'agrégation de MongoDB](https://www.freecodecamp.org/news/mongodb-aggregation-framework/)
* [Apprendre Node + MongoDB en créant un projet de raccourcisseur d'URL](https://www.freecodecamp.org/news/mongodb-node-express-project/)
* [Comment utiliser MongoDB + Mongoose avec Node.js – Bonnes pratiques pour les développeurs backend](https://www.freecodecamp.org/news/mongodb-mongoose-node-tutorial/)
* [Comment déployer une application MERN sur Heroku en utilisant MongoDB Atlas](https://www.freecodecamp.org/news/deploying-a-mern-application-using-mongodb-atlas-to-heroku/)
* [Comment construire une application Todo avec React, TypeScript, NodeJS, et MongoDB](https://www.freecodecamp.org/news/how-to-build-a-todo-app-with-react-typescript-nodejs-and-mongodb/)
* [Comment construire un générateur de personnages RPG full stack avec MongoDB, Express, Vue, et Node (la pile MEVN)](https://www.freecodecamp.org/news/build-a-full-stack-mevn-app/)
* [Comment construire une API GraphQL ultra-rapide avec Node.js, MongoDB et Fastify](https://www.freecodecamp.org/news/how-to-build-a-blazing-fast-graphql-api-with-node-js-mongodb-and-fastify-77fd5acd2998/)
* [Comment créer une application en temps réel utilisant Socket.io, React, Node & MongoDB](https://www.freecodecamp.org/news/how-to-create-a-realtime-app-using-socket-io-react-node-mongodb-a10c4a1ab676/)
* [Comment construire des API REST ultra-rapides avec Node.js, MongoDB, Fastify et Swagger](https://www.freecodecamp.org/news/how-to-build-blazing-fast-rest-apis-with-node-js-mongodb-fastify-and-swagger-114e062db0c9/)
* [Introduction à Mongoose pour MongoDB](https://www.freecodecamp.org/news/introduction-to-mongoose-for-mongodb-d2a7aa593c57/)
* [Comment journaliser une API Node.js dans une application Express.js avec des plugins Mongoose](https://www.freecodecamp.org/news/how-to-log-a-node-js-api-in-an-express-js-app-with-mongoose-plugins-efe32717b59/)
* [Mongoose 101 : Une introduction aux bases, sous-documents, et population](https://www.freecodecamp.org/news/mongoose101/)
* [Comment permettre aux utilisateurs de télécharger des images avec Node/Express, Mongoose, et Cloudinary](https://www.freecodecamp.org/news/how-to-allow-users-to-upload-images-with-node-express-mongoose-and-cloudinary-84cefbdff1d9/)
* [Démarrage rapide de MongoDB avec Python](https://www.freecodecamp.org/news/mongodb-quickstart-with-python/)
* [Tutoriel MongoDB - Application CRUD à partir de zéro en utilisant Node.js](https://www.freecodecamp.org/news/mongodb-crud-app/)
* [Cours complet MongoDB avec Node.js, Express, & Mongoose](https://www.freecodecamp.org/news/mongodb-full-course-nodejs-express-mongoose/)
* [Comment construire une API RESTful en utilisant Node, Express, et Mongo](https://www.freecodecamp.org/news/restful-api-using-node-express-mongo/)

### Redis (NoSQL)

* [Comment utiliser Redis pour supercharger vos API web](https://www.freecodecamp.org/news/redis-caching-essentials-with-node-and-mongoose/)
* [Un guide rapide pour le scripting Lua de Redis](https://www.freecodecamp.org/news/a-quick-guide-to-redis-lua-scripting/)
* [Comment fonctionne la fonction de scan de la table de hachage Redis](https://www.freecodecamp.org/news/redis-hash-table-scan-explained-537cc8bb9f52/)
* [Comment construire une application d'inscription multi-étapes avec des transitions animées en utilisant la pile MERN](https://www.freecodecamp.org/news/build-a-multi-step-registration-app-with-animated-transitions-using-mern-stack/)

### Postgres / PostgreSQL

* [Comment commencer avec PostgreSQL](https://www.freecodecamp.org/news/how-to-get-started-with-postgresql-9d3bc1dd1b11/)
* [Apprendre ces astuces rapides dans PostgreSQL](https://www.freecodecamp.org/news/postgresql-tricks/)
* [Comment utiliser la correspondance de chaînes floue avec PostgreSQL](https://www.freecodecamp.org/news/fuzzy-string-matching-with-postgresql/)
* [Comment mettre à jour des objets à l'intérieur des tableaux JSONB avec PostgreSQL](https://www.freecodecamp.org/news/how-to-update-objects-inside-jsonb-arrays-with-postgresql-5c4e03be256a/)
* [Comment déployer une application Rails 5.2 PostgreSQL sur AWS Elastic Beanstalk](https://www.freecodecamp.org/news/how-to-deploy-a-rails-5-2-postgresql-app-on-aws-elastic-beanstalk-34e5cec3a984/)
* [Comment créer un serveur Django exécutant uWSGI, NGINX et PostgreSQL sur AWS EC2 avec Python 3.6](https://www.freecodecamp.org/news/django-uwsgi-nginx-postgresql-setup-on-aws-ec2-ubuntu16-04-with-python-3-6-6c58698ae9d3/)
* [Comment construire des API web avec NestJS, Postgres, et Sequelize - Un guide pour débutants](https://www.freecodecamp.org/news/build-web-apis-with-nestjs-beginners-guide/)
* [Comment déployer une application React en production sur AWS en utilisant Express, Postgres, PM2 et NGINX](https://www.freecodecamp.org/news/production-fullstack-react-express/)
* [Flux de travail de développement Docker – Un guide avec Flask et Postgres](https://www.freecodecamp.org/news/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a/)
* [Apprendre SQL avec ce cours gratuit de 4 heures sur la base de données populaire PostgreSQL](https://www.freecodecamp.org/news/postgresql-full-course/)

## Comment apprendre le développement backend

Similaire à la façon dont le développement frontend est un sujet large, le développement backend peut faire référence à de nombreuses choses, et englobe beaucoup de technologies différentes.

Habituellement, lorsque vous commencez à travailler sur le backend, qui contrôle le fonctionnement des sites et des applications web en coulisses, vous utiliserez un framework comme Express, Flask ou Django.

### Express

* [Comment activer la syntaxe ES6 (et au-delà) avec Node et Express](https://www.freecodecamp.org/news/how-to-enable-es6-and-beyond-syntax-with-node-and-express-68d3e11fe1ab/)
* [Comment déployer votre application sur le web en utilisant Express.js et Heroku](https://www.freecodecamp.org/news/how-to-deploy-your-site-using-express-and-heroku/)
* [Comment ajouter un serveur GraphQL à une API RESTful Express.js en 2 minutes](https://www.freecodecamp.org/news/add-a-graphql-server-to-a-restful-express-js-api-in-2-minutes/)
* [Conseils de sécurité Express.js : Comment vous pouvez sauver et sécuriser votre application](https://www.freecodecamp.org/news/express-js-security-tips/)
* [Comment construire un générateur de personnages RPG full stack avec MongoDB, Express, Vue, et Node (la pile MEVN)](https://www.freecodecamp.org/news/build-a-full-stack-mevn-app/)
* [Comment construire un jeu de cartes multijoueur avec Phaser 3, Express, et Socket.IO](https://www.freecodecamp.org/news/how-to-build-a-multiplayer-card-game-with-phaser-3-express-and-socket-io/)
* [Comment construire un simulateur de jeu de table multijoueur avec Vue, Phaser, Node, Express, et Socket.IO](https://www.freecodecamp.org/news/how-to-build-a-multiplayer-tabletop-game-simulator/)
* [Comment rendre la validation des entrées simple et propre dans votre application Express.js](https://www.freecodecamp.org/news/how-to-make-input-validation-simple-and-clean-in-your-express-js-app-ea9b5ff5a8a7/)
* [Comment écrire une application Node et Express prête pour la production](https://www.freecodecamp.org/news/how-to-write-a-production-ready-node-and-express-app-f214f0b17d8c/)
* [Comment construire une API RESTful en utilisant Node, Express, et Mongo](https://www.freecodecamp.org/news/restful-api-using-node-express-mongo/)
* [Apprendre Express.js dans ce cours complet](https://www.freecodecamp.org/news/learn-express-js-in-this-complete-course/)

### Flask

* [Comment développer un projet de machine learning de bout en bout et le déployer sur Heroku avec Flask](https://www.freecodecamp.org/news/end-to-end-machine-learning-project-turorial/)
* [Apprendre les microservices Python en construisant une application utilisant Django, Flask, et React](https://www.freecodecamp.org/news/python-microservices-course/)
* [Comment utiliser Python et Flask pour construire une application web — Un tutoriel approfondi](https://www.freecodecamp.org/news/how-to-use-python-and-flask-to-build-a-web-app-an-in-depth-tutorial-437dbfe9f1c6/)
* [Configuration de CI/CD sur GitLab pour le déploiement d'une application Python Flask sur Heroku](https://www.freecodecamp.org/news/setting-up-a-ci-cd-on-gitlab-for-deploying-a-python-flask-application-on-heroku-e154db93952b/)
* [Apprendre le développement web Flask pour Python dans ce cours gratuit d'1 heure](https://www.freecodecamp.org/news/learn-flask-for-python-full-tutorial/)
* [Apprendre la programmation web avec Flask depuis le CS50 de Harvard](https://www.freecodecamp.org/news/learn-web-programming-with-flask-from-harvards-cs50/)
* [Apprendre le framework de développement web Flask Python en construisant une plateforme e-commerce](https://www.freecodecamp.org/news/learn-the-flask-python-web-framework-by-building-a-market-platform/)

### Django

* [Comment écrire des vues, modèles et requêtes efficaces dans Django](https://www.freecodecamp.org/news/how-to-write-efficient-views-models-and-queries-in-django/)
* [Comment manipuler les données avec les migrations Django](https://www.freecodecamp.org/news/how-to-manipulate-data-with-django-migrations/)
* [Bonnes pratiques de projet Django qui garderont vos développeurs heureux](https://www.freecodecamp.org/news/django-project-best-practices-for-happy-developers/)
* [Introduction à la suite de tests Django – Comment augmenter votre confiance en tant que développeur Python](https://www.freecodecamp.org/news/increase-developer-confidence-with-a-great-django-test-suite/)
* [ELI5 Bases de la pile complète : Percée avec Django & EmberJS](https://www.freecodecamp.org/news/eli5-full-stack-basics-breakthrough-with-django-emberjs-402fc7af0e3/)
* [J'ai construit une zone membres sur mon site web avec Python et Django. Voici ce que j'ai appris.](https://www.freecodecamp.org/news/i-built-a-members-area-on-my-website-with-python-and-django-heres-what-i-learned/)
* [Comment construire un tableau de bord basé sur le web avec Django, MongoDB, et Pivot Table](https://www.freecodecamp.org/news/how-to-build-a-web-based-dashboard-with-django-mongodb-and-pivot-table/)
* [Comment créer un tableau de bord d'analyse dans une application Django](https://www.freecodecamp.org/news/how-to-create-an-analytics-dashboard-in-django-app/)
* [Comment construire un site web de commerce électronique avec Django et Python](https://www.freecodecamp.org/news/how-to-build-an-e-commerce-website-with-django-and-python/)
* [Construire un clone Moodle / Blackboard avec Django Rest Framework & React](https://www.freecodecamp.org/news/django-rest-framework-react-tutorial/)
* [Comment construire une barre de progression pour le web avec Django et Celery](https://www.freecodecamp.org/news/how-to-build-a-progress-bar-for-the-web-with-django-and-celery-12a405637440/)
* [Comment documenter votre projet Django en utilisant l'outil Sphinx](https://www.freecodecamp.org/news/sphinx-for-django-documentation-2454e924b3bc/)
* [Framework web Python Django - Cours complet pour débutants](https://www.freecodecamp.org/news/python-django-course/)
* [Apprendre les microservices Python en construisant une application utilisant Django, Flask, et React](https://www.freecodecamp.org/news/python-microservices-course/)

## Comment apprendre les générateurs de sites statiques

Les générateurs de sites statiques ont été créés pour faciliter le développement, et ils représentent le "M" dans [JAMstack](https://www.freecodecamp.org/news/what-is-the-jamstack-and-how-do-i-host-my-website-on-it/) (JavaScript, APIs, et Markup). Avec un générateur de site statique, il est beaucoup plus facile de créer un site web, un blog ou une application web rapide et évolutif avec des avantages modernes comme le rendu côté serveur.

### Gatsby

* [Gatsby Starter Blog : Comment ajouter des images d'en-tête aux articles avec support pour les cartes Twitter](https://www.freecodecamp.org/news/gatsby-blog-header-image-twitter-card/)
* [Comment créer une galerie d'images en utilisant Gatsby et Cloudinary](https://www.freecodecamp.org/news/how-to-create-an-image-gallery-gatsby-and-cloudinary/)
* [Comment construire un blog avec Gatsby et Netlify CMS – Un guide complet](https://www.freecodecamp.org/news/how-to-build-a-blog-with-gatsby-and-netlify-cms/)
* [Créer un site web full-stack avec Strapi et GatsbyJS](https://www.freecodecamp.org/news/create-a-full-stack-website-with-strapi-and-gatsbyjs/)
* [Comment créer une carte de liste de voyages avec Gatsby, React Leaflet, & GraphCMS](https://www.freecodecamp.org/news/how-to-create-a-travel-bucket-list-map-with-gatsby-react-leaflet-graphcms/)
* [Comment activer le mode hors ligne pour votre site Gatsby](https://www.freecodecamp.org/news/how-to-enable-offline-mode-for-gatsby-site/)
* [Quelles sont les variables d'environnement et comment puis-je les utiliser avec Gatsby et Netlify ?](https://www.freecodecamp.org/news/what-are-environment-variables-and-how-can-i-use-them-with-gatsby-and-netlify/)
* [3 façons d'éditer Markdown avec TinaCMS](https://www.freecodecamp.org/news/3-ways-to-edit-markdown-with-tina-gatsby/) + Gatsby
* [Comment construire votre blog de codage à partir de zéro en utilisant Gatsby et MDX](https://www.freecodecamp.org/news/build-a-developer-blog-from-scratch-with-gatsby-and-mdx/)
* [Qu'est-ce que Gatsby et pourquoi il est temps de monter dans le train de la hype](https://www.freecodecamp.org/news/what-is-gatsby-and-why-its-time-to-get-on-the-hype-train/)
* [Comment construire des applications JAMstack authentifiées et serverless avec Gatsby et Netlify](https://www.freecodecamp.org/news/building-jamstack-apps/)
* [Comment garder l'état entre les pages avec l'état local dans Gatsby.js](https://www.freecodecamp.org/news/keeping-state-between-pages-with-local-state-in-gatsby-js/)
* [Comment publier automatiquement depuis votre blog GatsbyJS avec RSS](https://www.freecodecamp.org/news/how-to-automatically-cross-post-from-your-gatsbyjs-blog-with-rss/)
* [Comment créer un journal consultable avec Gatsby](https://www.freecodecamp.org/news/how-to-create-a-searchable-log-with-gatsby-d624bf3a05af/)
* [De zéro à déploiement : Comment j'ai créé un site web statique à partir de zéro en utilisant Netlify + Gatsby](https://www.freecodecamp.org/news/from-zero-to-deploy-how-i-created-a-static-website-from-scratch-using-netlify-gatsby-ebca82612ffd/)
* [Obtenez vos données GraphCMS dans Gatsby](https://www.freecodecamp.org/news/get-your-graphcms-data-into-gatsby-2018/)
* [Le grand bootcamp Gatsby.js](https://www.freecodecamp.org/news/great-gatsby-bootcamp/)

### Next.js

* [Qu'est-ce que la génération de site statique ? Comment Next.js utilise SSG pour les applications web dynamiques](https://www.freecodecamp.org/news/static-site-generation-with-nextjs/)
* [Tutoriel sur les bases de Next.js – Rendu côté serveur, sites statiques, API REST, routage, et plus](https://www.freecodecamp.org/news/nextjs-basics/)
* [Routage dans Next.js – Un guide complet pour débutants](https://www.freecodecamp.org/news/routing-in-nextjs-beginners-guide/)
* [Comment créer un démarreur Next.js pour démarrer facilement une nouvelle application React](https://www.freecodecamp.org/news/how-to-create-a-nextjs-starter-to-easily-bootstrap-a-new-react-app/)
* [Comment construire un site JAMstack avec Next.js et Vercel - Manuel JAMstack](https://www.freecodecamp.org/news/how-to-build-a-jamstack-site-with-next-js-and-vercel-jamstack-handbook/)
* [Comment créer un formulaire de contact avec Netlify Forms et Next.js](https://www.freecodecamp.org/news/how-to-create-a-contact-form-with-netlify-forms-and-nextjs/)
* [Comment construire une galerie d'images avec NextJS en utilisant l'API Pexels et Chakra UI](https://www.freecodecamp.org/news/build-an-image-gallery-with-nextjs/)
* [Comment ajouter des animations interactives et des transitions de page à une application web Next.js avec Framer Motion](https://www.freecodecamp.org/news/how-to-add-interactive-animations-and-page-transitions-to-a-next-js-web-app-with-framer-motion/)
* [Comment utiliser les actions Github pour déployer un site web Next.js sur AWS S3](https://www.freecodecamp.org/news/how-to-use-github-actions-to-deploy-a-next-js-website-to-aws-s3/)
* [Comment utiliser Chakra UI avec Next.js et React](https://www.freecodecamp.org/news/how-to-use-chakra-ui-with-next-js-and-react/)
* [Comment exécuter des tests de régression visuelle sur une application Next.js avec Cypress et Applitools](https://www.freecodecamp.org/news/how-to-use-sass-with-css-modules-in-next-js/)
* [Comment récupérer des données GraphQL dans Next.js avec Apollo GraphQL](https://www.freecodecamp.org/news/how-to-fetch-graphql-data-in-next-js-with-apollo-graphql/)
* [Découvrir Next.js et écrire des applications React côté serveur facilement](https://www.freecodecamp.org/news/discover-next-js-and-write-server-side-react-apps-the-easy-way-cc920dea2d9d/)
* [Le manuel Next.js](https://www.freecodecamp.org/news/the-next-js-handbook/)

### Hugo

* [Comment créer votre premier blog Hugo : un guide pratique](https://www.freecodecamp.org/news/your-first-hugo-blog-a-practical-guide/)
* [Un Makefile portable pour la livraison continue avec Hugo et GitHub Pages](https://www.freecodecamp.org/news/a-portable-makefile-for-continuous-delivery-with-hugo-and-github-pages/)
* [Deux façons de déployer un site GitHub Pages public à partir d'un dépôt Hugo privé](https://www.freecodecamp.org/news/two-ways-to-deploy-a-public-github-pages-site-from-a-private-hugo-repository-627312ec63b9/)
* [Hugo + Firebase : Comment créer votre propre site web statique gratuitement en quelques minutes](https://www.freecodecamp.org/news/hugo-firebase-how-to-create-your-own-dynamic-website-for-free-in-minutes-463b4fb7bf5a/)
* [Hugo vs Jekyll : une bataille épique des thèmes de générateurs de sites statiques](https://www.freecodecamp.org/news/hugo-vs-jekyll-battle-of-static-site-generator-themes/)
* [Comment auto-héberger une application web Hugo](https://www.freecodecamp.org/news/my-latest-self-hosted-hugo-workflow/)

### Nuxt.js

* [Comment utiliser des données de fichiers plats dans une application Nuxt statique](https://www.freecodecamp.org/news/how-to-use-flat-file-data-in-a-static-nuxt-app/)
* [Up & Going avec Nuxt.js, Bulma et Sass](https://www.freecodecamp.org/news/up-goind-with-nuxt-js-bulma-and-sass/)
* [Structure de code d'application universelle dans Nuxt.js](https://www.freecodecamp.org/news/universal-application-code-structure-in-nuxt-js-4cd014cc0baa/)
* [Comment architecturer une DApp en utilisant Nuxt.js et Nebulas](https://www.freecodecamp.org/news/architecting-dapp-using-nuxt-js-nebulas-fc00712ae341/)
* [Déployer une application Nuxt sur S3 en 5 minutes](https://www.freecodecamp.org/news/deploy-a-nuxt-app-to-s3-in-5-minutes-515a161eb74f/)

### Vuepress

* [Comment créer un site web de documentation en utilisant VuePress](https://www.freecodecamp.org/news/how-to-create-a-documentation-website-using-vuepress-eeabe8a99045/)

## Comment apprendre les Bundlers, Compilateurs, Gestionnaires de dépendances, Task Runners, Formatters, et Linters

Une fois que vous commencez à travailler avec des frameworks / bibliothèques frontend, ou que vos projets commencent à croître en taille et en complexité, les choses peuvent rapidement devenir ingérables.

Pour garder les choses organisées et propres, il est utile d'apprendre le linting, surtout si vous travaillez sur de grandes équipes. Avec le linting, vous pouvez attraper les erreurs avant qu'elles ne se produisent, et avec un formatter comme prettier, vous pouvez imposer un guide de style de code pour toute votre équipe.

Et bien que beaucoup de projets Angular, Vue et React incluent déjà un bundler comme Webpack, il est utile d'en apprendre davantage sur son fonctionnement au cas où vous devriez ajuster son comportement plus tard.

### Webpack et Babel

* [Une introduction à Webpack : Qu'est-ce que c'est et comment l'utiliser](https://www.freecodecamp.org/news/an-intro-to-webpack-what-it-is-and-how-to-use-it-8304ecdc3c60/)
* [Comment créer une configuration Webpack 4 prête pour la production à partir de zéro](https://www.freecodecamp.org/news/creating-a-production-ready-webpack-4-config-from-scratch/)
* [Comment partager des variables entre HTML, CSS et JavaScript en utilisant Webpack](https://www.freecodecamp.org/news/how-to-share-variables-across-html-css-and-javascript-using-webpack/)
* [Comment combiner Webpack 4 et Babel 7 pour créer une application React fantastique](https://www.freecodecamp.org/news/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff/)
* [Comment configurer et déployer votre application React à partir de zéro en utilisant Webpack et Babel](https://www.freecodecamp.org/news/how-to-set-up-deploy-your-react-app-from-scratch-using-webpack-and-babel-a669891033d4/)
* [Comment utiliser les macros Babel avec React Native](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/)
* [Apprendre Webpack pour simplifier et accélérer votre site web](https://www.freecodecamp.org/news/webpack-course/)

### ESLint et Prettier

* [Qu'est-ce que le Linting et comment peut-il vous faire gagner du temps ?](https://www.freecodecamp.org/news/what-is-linting-and-how-can-it-save-you-time/)
* [Ne vous contentez pas de lint votre code - Corrigez-le avec Prettier](https://www.freecodecamp.org/news/dont-just-lint-your-code-fix-it-with-prettier/)
* [Comment créer votre propre package de configuration ESLint](https://www.freecodecamp.org/news/creating-your-own-eslint-config-package/)
* [ESLint : Les faits essentiels sur les outils essentiels du frontend](https://www.freecodecamp.org/news/the-essentials-eslint/)
* [Comment arrêter les erreurs avant qu'elles n'atteignent votre base de code avec Travis CI et ESLint](https://www.freecodecamp.org/news/how-to-stop-errors-before-they-ever-hit-your-codebase-with-travis-ci-and-eslint-7a5a6b1fcd4a/)

### Parcel

* [Comment configurer une application React avec Parcel](https://www.freecodecamp.org/news/how-to-up-a-react-app-with-parcel/)
* [Comment utiliser Parcel pour bundler votre application React.js](https://www.freecodecamp.org/news/how-to-use-parcel-to-bundle-your-react-js-application-d023979e9fe4/)
* [Comment construire des extensions Chrome avec React + Parcel](https://www.freecodecamp.org/news/building-chrome-extensions-in-react-parcel-79d0240dd58f/)
* [Utilisation de Parcel Bundler avec React](https://www.freecodecamp.org/news/using-parcel-bundler-with-react/)

### Gulp

* [Tutoriel Gulp super simple pour débutants](https://www.freecodecamp.org/news/super-simple-gulp-tutorial-for-beginners-45141974bfe8/)
* [Utilisation de Gulp 4 dans votre flux de travail pour les fichiers Sass et JS](https://www.freecodecamp.org/news/gulp-4-walk-through-with-example-code-c3c018eab306/)
* [Comment minifier des images avec Gulp & Gulp-imagemin et améliorer les performances de votre site](https://www.freecodecamp.org/news/how-to-minify-images-with-gulp-gulp-imagemin-and-boost-your-sites-performance-6c226046e08e/)

### Scripts npm

* [Pourquoi j'ai quitté Gulp et Grunt pour les scripts npm](https://www.freecodecamp.org/news/why-i-left-gulp-and-grunt-for-npm-scripts-3d6853dd22b8/)
* [La commande React Scripts Start – Les scripts npm de Create-React-App expliqués](https://www.freecodecamp.org/news/create-react-app-npm-scripts-explained/)

## Comment apprendre le développement d'applications mobiles

De nos jours, beaucoup de développement d'applications mobiles est fait avec un framework comme React Native.

Alors qu'auparavant vous deviez connaître un langage spécifique comme Java pour développer une application mobile, avec un framework, beaucoup de vos connaissances en framework / bibliothèque frontend peuvent être utilisées pour développer une application mobile.

De plus, si vous utilisez un framework, vous pouvez simplement construire l'application une fois, et créer des versions iOS et Android à partir de la même base de code.

### React Native

* [Comment fonctionnent les animations dans React Native](https://www.freecodecamp.org/news/how-react-native-animations-work/)
* [Comment utiliser la vidéo comme arrière-plan dans React Native](https://www.freecodecamp.org/news/how-to-create-a-background-video-in-react-native-cb53304ee4f6/)
* [Comment gérer la navigation dans React Native avec react-navigation 5](https://www.freecodecamp.org/news/introducing-react-navigation-5/)
* [Pourquoi je suis passé à React Native pour créer une feuille de fond super facile](https://www.freecodecamp.org/news/i-switched-to-react-native-and-created-a-bottom-sheet-its-easier-than-native/)
* [Comment React Native construit les mises en page des applications (et comment Fabric est sur le point de le changer)](https://www.freecodecamp.org/news/how-react-native-constructs-app-layouts-and-how-fabric-is-about-to-change-it-dd4cb510d055/)
* [Comment créer une application caméra avec Expo et React Native](https://www.freecodecamp.org/news/how-to-create-a-camera-app-with-expo-and-react-native/)
* [Comment construire votre première application React Native serverless avec authentification utilisateur](https://www.freecodecamp.org/news/build-react-native-app-user-authentication/)
* [Comment ajouter l'authentification à React Native en trois étapes en utilisant Firebase](https://www.freecodecamp.org/news/how-to-add-authentication-to-react-native-in-three-steps-using-firebase/)
* [Comment construire une application React Native et l'intégrer avec Firebase](https://www.freecodecamp.org/news/react-native-firebase-tutorial/)
* [Comment configurer la connexion Google dans React Native & Firebase](https://www.freecodecamp.org/news/google-login-with-react-native-and-firebase/)
* [Ajouter des gestes et des animations aux projets React Native](https://www.freecodecamp.org/news/react-native-gestures-animations-tutorial/)
* [Comment utiliser les macros Babel avec React Native](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/)
* [Construire un clone d'Instagram avec React Native, Firebase Firestore, Redux, et Expo](https://www.freecodecamp.org/news/build-an-instagram-clone-with-react-native-firebase-firestore-redux-and-expo/)
* [Cours React Native : Comment construire une application iPhone, une application Android, et un site web - Tout avec la même base de code](https://www.freecodecamp.org/news/create-an-app-that-works-on-ios-android-and-the-web-with-react-native-web/)
* [Comment intégrer Redux dans votre application avec React Native et Expo](https://www.freecodecamp.org/news/how-to-integrate-redux-into-your-application-with-react-native-and-expo-ec37c9ca6033/)
* [Comment convertir une application React en React Native](https://www.freecodecamp.org/news/converting-a-react-app-to-react-native/)
* [Introduction au cours React Native](https://www.freecodecamp.org/news/react-native-course-for-beginners/)

### Ionic

* [Comment écrire "Hello, World!" dans Ionic](https://www.freecodecamp.org/news/how-to-write-hello-world-in-ionic/)
* [Comment créer une application To-do CRUD en utilisant Ionic 3](https://www.freecodecamp.org/news/creating-a-crud-to-do-app-using-ionic-4/)
* [Comment construire votre première application Ionic 4 avec des appels API](https://www.freecodecamp.org/news/how-to-build-your-first-ionic-4-app-with-api-calls-f6ea747dc17a/)
* [Comment faire fonctionner les notifications push avec Ionic 4 et Firebase](https://www.freecodecamp.org/news/how-to-get-push-notifications-working-with-ionic-4-and-firebase-ad87cc92394e/)
* [Comment développer un excellent flux de connexion Facebook avec Firebase et Ionic](https://www.freecodecamp.org/news/how-to-develop-a-great-facebook-login-flow-with-firebase-and-ionic-656a295c4fe9/)
* [Comment intégrer la connexion Google dans une application Ionic avec Firebase](https://www.freecodecamp.org/news/how-to-integrate-google-login-into-an-ionic-app-with-firebase-41cb69234919/)
* [Apprendre Ionic 4 et commencer à créer des applications iOS / Android](https://www.freecodecamp.org/news/ionic-full-course/)

### Flutter

* [Une introduction simplifiée à Dart et Flutter](https://www.freecodecamp.org/news/https-medium-com-rahman-sameeha-whats-flutter-an-intro-to-dart-6fc42ba7c4a3/)
* Une introduction à Flutter : Les bases
* [Comment sérialiser un objet dans Flutter](https://www.freecodecamp.org/news/serialize-object-flutter/)
* [Comment gérer l'état dans Flutter en utilisant le motif BLoC](https://www.freecodecamp.org/news/how-to-handle-state-in-flutter-using-the-bloc-pattern-8ed2f1e49a13/)
* [Comment utiliser les Streams, BLoCs, et SQLite dans Flutter](https://www.freecodecamp.org/news/using-streams-blocs-and-sqlite-in-flutter-2e59e1f7cdce/)
* [Comment gérer la navigation dans vos applications Flutter](https://www.freecodecamp.org/news/how-to-handle-navigation-in-your-flutter-apps-ceaf2f411dcd/)
* [Comment utiliser le motif Provider dans Flutter](https://www.freecodecamp.org/news/provider-pattern-in-flutter/)
* [Comment construire une interface utilisateur d'application de chat avec Flutter et Dart](https://www.freecodecamp.org/news/build-a-chat-app-ui-with-flutter/)
* [Comment ajouter des notifications push à une application Flutter en utilisant Firebase Cloud Messaging](https://www.freecodecamp.org/news/how-to-add-push-notifications-to-flutter-app/)
* [Comment intégrer Google AdMob dans Flutter](https://www.freecodecamp.org/news/how-to-add-google-admob-to-flutter/)
* [Comment construire un pont de communication natif dans Flutter avec WebView et JavaScript](https://www.freecodecamp.org/news/how-to-build-a-native-communication-bridge-in-flutter-with-webview-and-javascript/)
* [Comment utiliser Flutter pour construire une calculatrice de pourboire](https://www.freecodecamp.org/news/build-a-tip-calculator-with-flutter/)
* [Comment construire une application de liste de prix de cryptomonnaie en utilisant le SDK Flutter](https://www.freecodecamp.org/news/how-to-build-a-cryptocurrency-price-list-app-using-flutter-sdk-1c75998e1a58/)
* [Tutoriel UI Flutter – Comment construire une application de chat avec des histoires en utilisant le SDK Flutter](https://www.freecodecamp.org/news/flutter-messenger-clone/)
* [Cours Flutter – Comment créer une application de production iPhone et Android avec le kit d'outils UI Flutter](https://www.freecodecamp.org/news/how-to-create-a-production-app-with-flutter/)
* [Utiliser Flutter pour créer une application pour mobile, web et bureau - Tout avec une seule base de code](https://www.freecodecamp.org/news/flutter-app-course-mobile-web-desktop/)
* [Apprendre à construire des applications iOS et Android avec Flutter](https://www.freecodecamp.org/news/flutter-course-ios-android/)

## Comment apprendre le développement d'applications de bureau

Similaire au développement moderne d'applications mobiles, de nombreuses applications de bureau de nos jours sont développées en utilisant un framework. Cela présente beaucoup des mêmes avantages, et signifie que vous pouvez écrire votre application de bureau une seule fois, et créer des versions Windows, macOS, et même Linux à partir de la même base de code.

### Electron

* [Écrire du code spécifique au système d'exploitation dans Electron](https://www.freecodecamp.org/news/how-to-write-os-specific-code-in-electron-bf6379c62ff6/)
* [Construire une application Electron avec create-react-app](https://www.freecodecamp.org/news/building-an-electron-application-with-create-react-app-97945861647c/)
* [Mises à jour automatiques rapides et indolores dans Electron](https://www.freecodecamp.org/news/quick-painless-automatic-updates-in-electron-d993d5408b3a/)
* [Voici comment j'ai créé une application Markdown avec Electron et React](https://www.freecodecamp.org/news/heres-how-i-created-a-markdown-app-with-electron-and-react-1e902f8601ca/)
* [Comment créer une application Electron en utilisant Angular et SQLite3](https://www.freecodecamp.org/news/creating-an-electron-app-using-angular-and-sqlite3-24ca7d892810/)
* [Choses que j'aurais aimé savoir avant de travailler avec Electron.js](https://www.freecodecamp.org/news/lessons-learned-from-electronjs/)
* [Comment construire une application de bureau Electron en JavaScript : Multithreading, SQLite, Modules natifs, et autres points de douleur courants](https://www.freecodecamp.org/news/how-to-build-an-electron-desktop-app-in-javascript-multithreading-sqlite-native-modules-and-1679d5ec0ac/)

### Proton Native

* [Comment construire des applications de bureau natives avec JavaScript (Pr](https://www.freecodecamp.org/news/build-native-desktop-apps-with-javascript-a49ede90d8e9/)oton Native)

## Comment apprendre la science des données et le machine learning

La science des données et le machine learning sont à la mode, et le nombre d'emplois dans chaque domaine augmente chaque année.

En termes simples, la science des données fait référence à une large gamme de techniques utilisées pour analyser et donner un sens à de vastes quantités de données.

Le machine learning relève de l'ombre de la science des données, et il emploie des techniques que les scientifiques des données utilisent pour permettre aux ordinateurs d'apprendre à partir de toutes ces données.

C'est beaucoup à assimiler, mais pas de soucis – voici quelques-uns des meilleurs articles et cours que nous avons sur le machine learning, et les différentes bibliothèques et frameworks que vous utiliserez sur le terrain.

### Machine Learning général

* [Bases du Machine Learning pour les développeurs](https://www.freecodecamp.org/news/machine-learning-basics-for-developers/)
* [Qu'est-ce qu'un réseau de neurones convolutionnel ? Un tutoriel pour débutants en machine learning et deep learning](https://www.freecodecamp.org/news/convolutional-neural-network-tutorial-for-beginners/)
* [Algorithmes de clustering en machine learning que tous les scientifiques des données devraient connaître](https://www.freecodecamp.org/news/8-clustering-algorithms-in-machine-learning-that-all-data-scientists-should-know/)
* [Algorithmes clés de machine learning expliqués en anglais simple](https://www.freecodecamp.org/news/a-no-code-intro-to-the-9-most-important-machine-learning-algorithms-today/)
* [Tutoriel sur le classificateur de forêt aléatoire : Comment utiliser les algorithmes basés sur les arbres pour le machine learning](https://www.freecodecamp.org/news/how-to-use-the-tree-based-algorithm-for-machine-learning/)
* [Tutoriel Google BERT NLP Machine Learning](https://www.freecodecamp.org/news/google-bert-nlp-machine-learning-tutorial/)
* [Tutoriel SVM Machine Learning – Qu'est-ce que l'algorithme de machine à vecteurs de support, expliqué avec des exemples de code](https://www.freecodecamp.org/news/svm-machine-learning-tutorial-what-is-the-support-vector-machine-algorithm-explained-with-code-examples/)
* [Machine Learning avec Scikit-Learn—Cours complet](https://www.freecodecamp.org/news/machine-learning-with-scikit-learn-full-course/)

### Pandas

* [Le guide ultime de la bibliothèque Pandas pour la science des données en Python](https://www.freecodecamp.org/news/the-ultimate-guide-to-the-pandas-library-for-data-science-in-python/)
* [Comment commencer avec Pandas en Python – un guide pour débutants](https://www.freecodecamp.org/news/python-pandas-functions/)
* [Comment utiliser Python et Pandas pour cartographier les principales tempêtes, le pessimisme et les données dures](https://www.freecodecamp.org/news/python-pandas-major-storms-hard-data/)
* [Comment analyser des données avec Python, Pandas & Numpy - Cours de 10 heures](https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/)

### Numpy

* [Le guide ultime du package NumPy pour le calcul scientifique en Python](https://www.freecodecamp.org/news/the-ultimate-guide-to-the-numpy-scientific-computing-library-for-python/)
* [Cours accéléré Python NumPy – Comment construire des tableaux N-dimensionnels pour le machine learning](https://www.freecodecamp.org/news/numpy-crash-course-build-powerful-n-d-arrays-with-numpy/)
* [Apprendre NumPy et commencer à faire du calcul scientifique en Python](https://www.freecodecamp.org/news/numpy-python-tutorial/)

### Scikit-Learn

* [Machine Learning avec Scikit-Learn—Cours complet](https://www.freecodecamp.org/news/machine-learning-with-scikit-learn-full-course/)
* [Comment j'ai utilisé l'analyse de régression pour analyser l'espérance de vie avec Scikit-Learn et Statsmodels](https://www.freecodecamp.org/news/regression-analysis-on-life-expectancy/)

### Seaborn

* [Analyse de données Python : Comment visualiser un ensemble de données Kaggle avec Pandas, Matplotlib, et Seaborn](https://www.freecodecamp.org/news/kaggle-dataset-analysis-with-pandas-matplotlib-seaborn/)

### Matplotlib

* [Cours Matplotlib – Apprendre la visualisation de données Python](https://www.freecodecamp.org/news/matplotlib-course-learn-python-data-visualization/)
* [Comment intégrer des visualisations Python interactives sur votre site web avec Python et Matplotlib](https://www.freecodecamp.org/news/how-to-embed-interactive-python-visualizations-on-your-website-with-python-and-matplotlib/)
* [Comment créer des visualisations de données auto-mises à jour en Python avec IEX Cloud, Matplotlib, et AWS](https://www.freecodecamp.org/news/how-to-create-auto-updating-data-visualizations-in-python-with-matplotlib-and-aws/)
* [Analyse de données Python : Comment visualiser un ensemble de données Kaggle avec Pandas, Matplotlib, et Seaborn](https://www.freecodecamp.org/news/kaggle-dataset-analysis-with-pandas-matplotlib-seaborn/)
* [Science des données Python – Un cours gratuit de 12 heures pour débutants. Apprendre Pandas, NumPy, Matplotlib, et plus](https://www.freecodecamp.org/news/python-data-science-course-matplotlib-pandas-numpy/)

### TensorFlow

* [Apprendre à utiliser TensorFlow 2.0 pour le machine learning dans ce cours massif gratuit](https://www.freecodecamp.org/news/massive-tensorflow-2-0-free-course/)
* [Apprendre le traitement du langage naturel avec Python et TensorFlow 2.0 – Aucune expérience en machine learning requise](https://www.freecodecamp.org/news/learn-natural-language-processing-no-experience-required/)
* [Apprendre à appliquer le deep learning avec Pytorch dans ce cours complet](https://www.freecodecamp.org/news/applied-deep-learning-with-pytorch-full-course/)
* [Apprendre à développer des réseaux de neurones en utilisant TensorFlow 2.0 dans ce cours pour débutants](https://www.freecodecamp.org/news/learn-to-develop-neural-networks-using-tensorflow-2-0-in-this-beginners-course/)

### PyTorch

* [Méthodes de tenseur PyTorch – Comment créer des tenseurs en Python](https://www.freecodecamp.org/news/pytorch-tensor-methods/)
* [Comment construire un réseau de neurones à partir de zéro avec PyTorch](https://www.freecodecamp.org/news/how-to-build-a-neural-network-with-pytorch/)
* [Apprendre à utiliser PyTorch pour le deep learning](https://www.freecodecamp.org/news/pytorch-full-course/)
* [Cours en direct gratuit : Deep Learning avec PyTorch](https://www.freecodecamp.org/news/free-deep-learning-with-pytorch-live-course/)

### Keras

* [Cours Keras – Apprendre le deep learning Python et les réseaux de neurones](https://www.freecodecamp.org/news/keras-video-course-python-deep-learning/)
* [Comment classifier les papillons avec le deep learning dans Keras](https://www.freecodecamp.org/news/classify-butterfly-images-deep-learning-keras/)
* [Comment construire votre premier réseau de neurones pour prédire les prix des maisons avec Keras](https://www.freecodecamp.org/news/how-to-build-your-first-neural-network-to-predict-house-prices-with-keras-f8db83049159/)

## Comment apprendre la virtualisation et la conteneurisation

Une fois que vous avez appris les bases de Linux, vous voudrez apprendre les machines virtuelles / la virtualisation, et la conteneurisation.

La principale différence entre les deux est que la virtualisation est une abstraction au niveau matériel, et permet à plusieurs machines émulées de fonctionner sur une seule machine.

Par exemple, avec la virtualisation, vous pouvez diviser les ressources d'une seule machine (CPU, SSD, RAM, etc.) en deux machines plus petites, l'une fonctionnant sous Windows Server et l'autre sous Ubuntu.

D'autre part, la conteneurisation est une émulation au niveau logiciel. Cela vous permet d'emballer des applications et toutes leurs dépendances dans un petit conteneur portable qui fonctionne presque partout.

Avec la conteneurisation, vous avez une application Node.js qui fonctionne sur Ubuntu. Vous pouvez inclure votre application, tous ses fichiers `node_module`, et même l'ensemble du système d'exploitation Ubuntu, dans un petit conteneur d'environ 1 Go. Les machines virtuelles font généralement entre 20 et 160 Go.

Mais les deux sont utiles et servent différents objectifs. Consultez nos tutoriels ci-dessous pour en savoir plus sur la virtualisation et la conteneurisation.

### Machines virtuelles

* [Virtualisation de serveur Linux : Les bases](https://www.freecodecamp.org/news/linux-server-virtualization-the-basics/)
* [VirtualBox : Obtenez-vous le meilleur rapport qualité-prix ?](https://www.freecodecamp.org/news/virtualbox-are-you-getting-your-moneys-worth/)
* [Comment installer Ubuntu sur VirtualBox](https://www.freecodecamp.org/news/how-to-install-ubuntu-with-oracle-virtualbox/)
* [Qu'est-ce qu'une machine virtuelle et comment configurer une VM sur Windows, Linux et Mac](https://www.freecodecamp.org/news/what-is-a-virtual-machine-and-how-to-setup-a-vm-on-windows-linux-and-mac/)

### Docker

* [À quoi sert Docker ? Un tutoriel sur les conteneurs Docker pour débutants](https://www.freecodecamp.org/news/what-is-docker-used-for-a-docker-container-tutorial-for-beginners/)
* [Une introduction complète à Docker, aux machines virtuelles et aux conteneurs](https://www.freecodecamp.org/news/comprehensive-introductory-guide-to-docker-vms-and-containers-4e42a13ee103/)
* [Docker 101 - Comment passer de la création au déploiement](https://www.freecodecamp.org/news/docker-101-creation-to-deployment/)
* [Un guide pour débutants sur Docker — Comment créer votre première application Docker](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f/)
* [Docker Remove Image : Comment supprimer des images Docker expliqué avec des exemples](https://www.freecodecamp.org/news/docker-remove-image-how-to-delete-docker-images-explained-with-examples/)
* [Comment obtenir une adresse IP de conteneur Docker - Expliqué avec des exemples](https://www.freecodecamp.org/news/how-to-get-a-docker-container-ip-address-explained-with-examples/)
* [Comment installer Docker sur Ubuntu 18.04 [Guide pour CE et EE]](https://www.freecodecamp.org/news/how-to-install-docker-on-ubuntu-18-04-guide-for-both-ce-and-ee/)
* [Comment exécuter Docker sur Windows 10 Édition Familiale](https://www.freecodecamp.org/news/how-to-run-docker-on-windows-10-home-edition/)
* [Comment déboguer une application Node.js avec VSCode, Docker, et votre terminal](https://www.freecodecamp.org/news/node-js-debugging/)
* [Docker Exec - Comment exécuter une commande à l'intérieur d'une image ou d'un conteneur Docker](https://www.freecodecamp.org/news/docker-exec-how-to-run-a-command-inside-a-docker-image-or-container/)
* [Où sont stockées les images Docker ? Chemins des conteneurs Docker expliqués](https://www.freecodecamp.org/news/where-are-docker-images-stored-docker-container-paths-explained/)
* [Conteneurs de données Docker](https://www.freecodecamp.org/news/docker-data-containers/)
* [Guide des images Docker : Comment supprimer des images Docker, arrêter des conteneurs, et supprimer tous les volumes](https://www.freecodecamp.org/news/docker-image-guide-how-to-remove-and-delete-docker-images-stop-containers-and-remove-all-volumes/)
* [Nettoyer Docker](https://www.freecodecamp.org/news/cleaning-up-docker/)
* [Une introduction rapide aux balises Docker](https://www.freecodecamp.org/news/an-introduction-to-docker-tags-9b5395636c2a/)
* [Comment activer le rechargement en direct sur les applications basées sur Docker avec les volumes Docker](https://www.freecodecamp.org/news/how-to-enable-live-reload-on-docker-based-applications/)
* [Une introduction pratique à Docker Compose](https://www.freecodecamp.org/news/a-practical-introduction-to-docker-compose/)
* [Un guide pour débutants sur Docker — Comment créer un côté client/serveur avec docker-compose](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-a-client-server-side-with-docker-compose-12c8cf0ae0aa/)
* [Guide de déploiement Docker — Comment déployer des conteneurs dans le cloud avec AWS Lightsail](https://www.freecodecamp.org/news/how-do-deploy-docker-containers-to-the-cloud-with-aws-lightsail/)
* [Le manuel Docker — Édition 2021](https://www.freecodecamp.org/news/the-docker-handbook/)
* [Cours gratuit de 4 heures sur Docker et Kubernetes](https://www.freecodecamp.org/news/course-on-docker-and-kubernetes/)
* [Apprendre les bases de DevOps avec ce cours gratuit de 2 heures sur Docker](https://www.freecodecamp.org/news/docker-devops-course/)

### Kubernetes

* [Kubernetes VS Docker : Quelle est la différence ? Expliqué avec des exemples](https://www.freecodecamp.org/news/kubernetes-vs-docker-whats-the-difference-explained-with-examples/)
* [Une introduction simple à l'orchestration de conteneurs Kubernetes](https://www.freecodecamp.org/news/a-simple-introduction-to-kubernetes-container-orchestration/)
* [Une introduction amicale à Kubernetes](https://www.freecodecamp.org/news/a-friendly-introduction-to-kubernetes-670c50ce4542/)
* [Comment développer des applications Kubernetes avec joie](https://www.freecodecamp.org/news/developing-kubernetes-applications-with-joy/)
* [Qu'est-ce qu'un Helm Chart ? Un tutoriel pour les débutants de Kubernetes](https://www.freecodecamp.org/news/what-is-a-helm-chart-tutorial-for-kubernetes-beginners/)
* [Tutoriel Helm Charts : Le gestionnaire de paquets Kubernetes expliqué](https://www.freecodecamp.org/news/helm-charts-tutorial-the-kubernetes-package-manager-explained/)
* [Apprendre Kubernetes en moins de 3 heures : Un guide détaillé pour orchestrer des conteneurs](https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882/)
* [Docker Swarm vs Kubernetes : Comment configurer les deux dans deux machines virtuelles](https://www.freecodecamp.org/news/docker-swarm-vs-kubernetes-how-to-setup-both-in-two-virtual-machines-f8897fce7967/)
* [Le manuel Kubernetes](https://www.freecodecamp.org/news/the-kubernetes-handbook/)
* [Une introduction au gestionnaire de paquets Helm pour Kubernetes](https://www.freecodecamp.org/news/an-introduction-to-the-helm-package-manager-for-kubernetes/)

## Comment apprendre le cloud computing

Une fois que vous avez appris les bases des machines virtuelles, vous voudrez apprendre le cloud computing.

Il n'y a pas si longtemps, si une entreprise voulait faire fonctionner un serveur pour héberger un site web, elle devait construire et maintenir le serveur elle-même.

Avec le cloud computing, vous pouvez lancer une machine virtuelle exécutant votre système d'exploitation de choix en quelques minutes. Mieux encore, l'entreprise hébergeant votre machine virtuelle s'occupera de la maintenance générale pour vous, et s'assurera que le serveur est en ligne et hautement disponible.

Et avec le cloud computing, vous n'avez même pas besoin d'avoir un serveur fonctionnant 24/7 – avec certains services, vous pouvez exécuter une fonction et ne payer que pour les millisecondes de temps qu'il a fallu pour la compléter.

Consultez nos tutoriels ci-dessous pour en savoir plus sur le cloud computing sur les trois grands acteurs de ce domaine : Amazon Web Services, Google Cloud Platform et Microsoft Azure.

### Amazon Web Services (AWS)

* [Formation AWS – Apprendre les bases d'Amazon Web Services](https://www.freecodecamp.org/news/learn-the-basics-of-amazon-web-services/)
* [Antisèche AWS : Les 5 choses à apprendre en premier lorsque vous commencez avec Amazon Web Services](https://www.freecodecamp.org/news/top-5-things-to-learn-first-when-getting-started-with-aws/)
* [Tout ce que vous devez savoir sur AWS S3](https://www.freecodecamp.org/news/everything-you-need-to-know-about-aws-s3/)
* [Comment lancer un serveur distant sur AWS](https://www.freecodecamp.org/news/getting-started-with-server-administration-on-aws/)
* [Comment installer l'AWS Elastic Beanstalk CLI sur un Mac](https://www.freecodecamp.org/news/install-elastic-bean-cli-on-mac/)
* [Tutoriel AWS CLI – Comment installer, configurer et utiliser AWS CLI pour comprendre votre environnement de ressources](https://www.freecodecamp.org/news/aws-cli-tutorial-install-configure-understand-resource-environment/)
* [Comment héberger un site statique dans le cloud en quatre étapes](https://www.freecodecamp.org/news/how-to-host-a-static-site-in-the-cloud-in-4-steps/)
* [Comment héberger et déployer un site web statique ou une application JAMstack sur AWS S3 et CloudFront](https://www.freecodecamp.org/news/how-to-host-and-deploy-a-static-website-or-jamstack-app-to-s3-and-cloudfront/)
* [Comment héberger votre site web statique avec AWS - Un guide pour débutants](https://www.freecodecamp.org/news/a-beginners-guide-on-how-to-host-a-static-site-with-aws/)
* [Tutoriel sur les fonctions AWS Lambda Cron Job – Comment planifier des tâches](https://www.freecodecamp.org/news/using-lambda-functions-as-cronjobs/)
* [Comment construire et déployer des applications AWS sur votre machine locale](https://www.freecodecamp.org/news/how-to-build-and-deploy-aws-applications-on-local-machine/)
* [Comment construire une application serverless en utilisant AWS SAM](https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-sam/)
* [Comment construire une application serverless en utilisant AWS Chalice](https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-chalice/)
* [Comment concevoir presque n'importe quel backend et le déployer sur AWS sans code](https://www.freecodecamp.org/news/design-and-deploy-backend-with-amplify-sandbox/)
* [Comment ajouter l'authentification à une application Vue en utilisant AWS Amplify](https://www.freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-aws-amplify/)
* [Comment construire une API de capture d'écran en utilisant Terraform, AWS API Gateway, et AWS Lambda](https://www.freecodecamp.org/news/build-a-screenshot-capture-api-using-terraform-aws-api-gateway-and-aws-lambda/)
* [Comment construire votre propre liste d'abonnés serverless avec Go et AWS](https://www.freecodecamp.org/news/build-your-own-serverless-subscriber-list-with-go-and-aws/)
* [Comment sécuriser vos charges de travail sur AWS](https://www.freecodecamp.org/news/how-to-secure-your-workloads-on-aws/)
* [Comment construire une application full stack avec AWS Amplify et React](https://www.freecodecamp.org/news/ultimate-guide-to-aws-amplify-and-reacxt/)
* [Comment utiliser les actions Github pour déployer un site web Next.js sur AWS S3](https://www.freecodecamp.org/news/how-to-use-github-actions-to-deploy-a-next-js-website-to-aws-s3/)
* [Comment optimiser les coûts de votre architecture cloud AWS](https://www.freecodecamp.org/news/cost-optimization-in-aws/)
* [Le guide complet pour construire une API avec TypeScript et AWS](https://www.freecodecamp.org/news/build-an-api-with-typescript-and-aws/)
* [Comment construire et déployer un serveur GraphQL dans AWS Lambda en utilisant Node.js et CloudFormation](https://www.freecodecamp.org/news/how-to-build-and-deploy-graphql-server-in-aws-lambda-using-nodejs-and-cloudformation/)
* [Comment construire un système backend complet avec Serverless](https://www.freecodecamp.org/news/complete-back-end-system-with-serverless/)
* [Hébergement de site simple avec Amazon S3 et HTTPS](https://www.freecodecamp.org/news/simple-site-hosting-with-amazon-s3-and-https-5e78017f482a/)
* [Passez l'examen AWS SysOps Administrator Associate avec ce cours gratuit de 14 heures](https://www.freecodecamp.org/news/aws-sysops-adminstrator-associate-certification-exam-course/)
* [Antisèche DynamoDB – Tout ce que vous devez savoir sur Amazon Dynamo DB pour la certification AWS Certified Developer Associate 2020](https://www.freecodecamp.org/news/ultimate-dynamodb-2020-cheatsheet/)
* [Passez l'examen AWS Developer Associate avec ce cours gratuit de 16 heures](https://www.freecodecamp.org/news/pass-the-aws-developer-associate-exam-with-this-free-16-hour-course/)

### Google Cloud Platform (GCP)

* [Tutoriel Google Cloud Platform : De zéro à héros avec GCP](https://www.freecodecamp.org/news/google-cloud-platform-from-zero-to-hero/)
* [Comment créer et se connecter à une machine virtuelle Google Cloud avec SSH](https://www.freecodecamp.org/news/how-to-create-and-connect-to-google-cloud-virtual-machine-with-ssh-81a68b8f74dd/)
* [Comment passer presque tous les examens de certification professionnelle Google Cloud Platform](https://www.freecodecamp.org/news/how-to-pass-almost-every-google-cloud-professional-certification-exam/)
* [Comment exécuter Laravel sur Google Cloud Run avec intégration continue - un guide étape par étape](https://www.freecodecamp.org/news/how-to-setup-laravel-6-on-google-cloud-run-with-continuous-integration-ci-step-by-step/)
* [Comment effectuer des opérations CRUD en utilisant Blazor et Google Cloud Firestore](https://www.freecodecamp.org/news/how-to-perform-crud-operations-using-blazor-and-google-cloud-firestore-52890b06e2f8/)
* [Le tutoriel JavaScript + Firestore pour 2020 : Apprendre par l'exemple](https://www.freecodecamp.org/news/the-firestore-tutorial-for-2020-learn-by-example/)
* [Firestore : Comment rester dans les limites du nouveau niveau gratuit de la base de données Firebase](https://www.freecodecamp.org/news/firestoreliving/)
* [Construire un clone d'Instagram avec React Native, Firebase Firestore, Redux, et Expo](https://www.freecodecamp.org/news/build-an-instagram-clone-with-react-native-firebase-firestore-redux-and-expo/)
* [Comment commencer avec Firebase en utilisant Python](https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/)
* [Comment ajouter l'authentification à une application Vue en utilisant Firebase](https://www.freecodecamp.org/news/how-to-add-authentication-to-a-vue-app-using-firebase/)
* [Comment construire une application Android avec Firebase et Kotlin](https://www.freecodecamp.org/news/how-to-build-an-android-app-with-firebase-and-kotlin/)
* [Comment authentifier les utilisateurs et sauvegarder des données dans une base de données en utilisant Firebase](https://www.freecodecamp.org/news/authenticate-users-and-save-data-in-a-database-using-firebase/)
* [Comment configurer la connexion Google dans React Native & Firebase](https://www.freecodecamp.org/news/google-login-with-react-native-and-firebase/)
* [Comment construire une TodoApp en utilisant ReactJS et Firebase](https://www.freecodecamp.org/news/how-to-build-a-todo-application-using-reactjs-and-firebase/)
* [Comment construire une application de réservation d'événements en utilisant HTML, CSS, JavaScript, et Firebase](https://www.freecodecamp.org/news/how-to-build-an-event-booking-app-using-html-css-javascript-and-firebase/)
* [Comment j'ai réussi à faire fonctionner Netlify Functions, Firebase, et GraphQL ensemble enfin](https://www.freecodecamp.org/news/netlify-functions-firebase-and-graphql-working-together-at-last/)
* [Vous ne pouvez pas y arriver d'ici : Comment Netlify Lambda et Firebase m'ont conduit à une impasse serverless](https://www.freecodecamp.org/news/you-cant-get-there-from-here-how-netlify-lambda-and-firebase-led-me-to-a-serverless-dead-end/)
* [Construire un clone d'Evernote en utilisant React et Firebase (Tutoriel vidéo)](https://www.freecodecamp.org/news/evernote-clone-react-firebase-tutorial/)
* [Apprendre à créer une application de réseau social à partir de zéro en utilisant React, Firebase, Redux, et Express](https://www.freecodecamp.org/news/react-firebase-social-media-app-course/)

### Microsoft Azure

* [Comment commencer avec Microsoft Azure - Applications de fonction, déclencheurs HTTP, et files d'attente d'événements](https://www.freecodecamp.org/news/getting-started-with-microsoft-azure/)
* [Une introduction rapide aux proxys de fonction Azure](https://www.freecodecamp.org/news/introduction-to-azure-function-proxies/)
* [Comprendre les fonctions durables Azure](https://www.freecodecamp.org/news/making-sense-of-azure-durable-functions/)
* [Une introduction aux fonctions durables Azure : Modèles et meilleures pratiques](https://www.freecodecamp.org/news/an-introduction-to-azure-durable-functions-patterns-and-best-practices-b1939ae6c717/)
* [Comment implémenter Azure Serverless avec Blazor WebAssembly](https://www.freecodecamp.org/news/how-to-implement-azure-serverless-with-blazor-web-assembly/)
* [Comment utiliser les fonctions Azure pour traiter des messages à haut débit](https://www.freecodecamp.org/news/how-to-use-azure-functions-to-process-high-throughput-messages-996d05d4ab23/)
* [Certification Azure Fundamentals (AZ-900) – Passez l'examen avec ce cours gratuit de 3 heures](https://www.freecodecamp.org/news/azure-fundamentals-course-az900/)

## Comment apprendre DevOps

Maintenant que vous connaissez la virtualisation, la conteneurisation et le cloud computing, il est temps de passer au niveau supérieur.

DevOps est à parts égales développement logiciel et opérations informatiques. Si vous êtes impliqué dans DevOps, non seulement vous pouvez construire une application, mais vous pouvez également lancer les machines virtuelles, déployer l'application, surveiller les serveurs et mettre à l'échelle l'application et les ressources à mesure que plus de personnes commencent à l'utiliser.

Il y a beaucoup à couvrir, et ces articles devraient vous mettre sur la voie de DevOps.

### DevOps général

* [La feuille de route du développeur web 2020 – Un guide visuel pour devenir un développeur front-end, back-end ou DevOps](https://www.freecodecamp.org/news/2019-web-developer-roadmap/)
* [Comment rendre le cloud de votre startup plus stable : 4 conseils pratiques DevOps](https://www.freecodecamp.org/news/how-to-make-your-startups-cloud-more-stable-4-practical-devops-tips-823e4202518c/)
* [Apprendre les bases de DevOps avec ce cours gratuit de 2 heures sur Docker](https://www.freecodecamp.org/news/docker-devops-course/)
* [Vous voulez apprendre DevOps ? Ce cours gratuit de 3 heures vous enseignera les prérequis pour commencer](https://www.freecodecamp.org/news/devops-prerequisites-course/)

### Travis CI

* [Comment arrêter les erreurs avant qu'elles n'atteignent votre base de code avec Travis CI et ESLint](https://www.freecodecamp.org/news/how-to-stop-errors-before-they-ever-hit-your-codebase-with-travis-ci-and-eslint-7a5a6b1fcd4a/)
* [Comment automatiser le déploiement sur GitHub-Pages avec Travis CI](https://www.freecodecamp.org/news/learn-how-to-automate-deployment-on-github-pages-with-travis-ci/)
* [Comment configurer un déploiement automatique avancé avec Travis CI](https://www.freecodecamp.org/news/advanced-automatic-deployment-with-travis-ci-1da32f7930ce/)
* [Comment utiliser Travis CI et GitHub pour le travail lourd de votre flux de travail de développement web](https://www.freecodecamp.org/news/how-to-wire-travis-ci-to-do-the-heavy-lifting-in-your-workflow-72693c855696/)

### Jenkins

* [Vous avez sonné, M'Lord ? Docker dans Docker avec les pipelines déclaratifs Jenkins](https://www.freecodecamp.org/news/you-rang-mlord-docker-in-docker-with-jenkins-declarative-pipelines/)
* [Comment créer un système de construction iOS à la demande avec Jenkins et Fastlane](https://www.freecodecamp.org/news/how-to-make-an-ios-on-demand-build-system-with-jenkins-and-fastlane-8eb1e02c73d1/)

### GoCD

* [Comment intégrer DangerJS dans les pipelines GoCD](https://www.freecodecamp.org/news/how-to-integrate-dangerjs-into-gocd-pipelines-7f930932ea07/)

### Ansible

* [Comment utiliser Ansible pour gérer vos ressources AWS](https://www.freecodecamp.org/news/ansible-manage-aws/)
* [Pourquoi vous pourriez avoir besoin d'Ansible et ne pas même le savoir](https://www.freecodecamp.org/news/why-you-might-need-ansible-and-not-even-know-it-d33b6e4b2ebe/)

### Chef

* [Un guide complet pour débutants sur Chef et l'infrastructure en tant que code](https://www.freecodecamp.org/news/an-introduction-to-chef-and-infrastructure-as-code-7d8ad2689b8/)

### Kafka

* [Comment implémenter la capture des données de changement en utilisant les flux Kafka](https://www.freecodecamp.org/news/how-to-implement-the-change-data-capture-pattern-using-kafka-streams/)
* [Ce qu'il faut considérer pour une intégration Apache Kafka sans douleur](https://www.freecodecamp.org/news/what-to-consider-for-painless-apache-kafka-integration-df559e828876/)
* [Comment ingérer des données dans Neo4j à partir d'un flux Kafka](https://www.freecodecamp.org/news/how-to-ingest-data-into-neo4j-from-a-kafka-stream-a34f574f5655/)
* [Comment construire un bot Chatops simple avec Kafka, Grafana, Prometheus et Slack](https://www.freecodecamp.org/news/simple-chatops-with-kafka-grafana-prometheus-and-slack-764ece59e707/)

### Terraform

* [Flux de travail Terraform : Comment travailler individuellement et en équipe](https://www.freecodecamp.org/news/terraform-workflow-working-individually-and-in-a-team/)
* [Que sont les modules Terraform et comment fonctionnent-ils ?](https://www.freecodecamp.org/news/terraform-modules-explained/)
* [Comment utiliser Terraform pour automatiser votre infrastructure cloud AWS – Tutoriel](https://www.freecodecamp.org/news/how-to-use-terraform-to-automate-your-aws-cloud-infrastructure-tutorial/)
* [Comment étendre votre infrastructure AWS avec Direct Connect en utilisant Terraform](https://www.freecodecamp.org/news/how-to-extend-your-aws-infrastructure/)
* [Comment gérer les ressources Wavefront en utilisant Terraform](https://www.freecodecamp.org/news/how-to-manage-wavefront-resources-using-terraform/)
* [Comment construire une API de capture d'écran en utilisant Terraform, AWS API Gateway, et AWS Lambda](https://www.freecodecamp.org/news/build-a-screenshot-capture-api-using-terraform-aws-api-gateway-and-aws-lambda/)

## En conclusion

Merci d'avoir lu jusqu'ici. Si vous avez trouvé cette compilation de ressources utile, partagez-la avec vos amis pour qu'ils puissent apprendre quelque chose aussi.

Y avait-il un article ou un tutoriel vidéo que vous avez aimé ? Ai-je manqué quelque chose ? Faites-le moi savoir sur [Twitter](https://twitter.com/kriskoishigawa).