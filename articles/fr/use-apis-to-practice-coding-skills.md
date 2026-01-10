---
title: Comment utiliser les APIs dans vos projets pour pratiquer vos compétences en
  codage
subtitle: ''
author: Rahul
co_authors: []
series: null
date: '2023-04-20T22:28:01.000Z'
originalURL: https://freecodecamp.org/news/use-apis-to-practice-coding-skills
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-build-projects.png
tags:
- name: api
  slug: api
- name: projects
  slug: projects
seo_title: Comment utiliser les APIs dans vos projets pour pratiquer vos compétences
  en codage
seo_desc: 'As web developers, we all know that practice makes perfect. But when it
  comes to practice, it''s easy to get stuck in a programming rut.

  But how do you come up with new ideas to build? Sooner or later, you will find yourself
  running out of features to...'
---

En tant que développeurs web, nous savons tous que la pratique rend parfait. Mais lorsqu'il s'agit de pratiquer, il est facile de se retrouver dans une routine de programmation.

Mais comment trouver de nouvelles idées à construire ? Tôt ou tard, vous vous retrouverez à court de fonctionnalités à ajouter ou d'algorithmes à implémenter.

Heureusement, il existe une solution simple : les APIs. Les [APIs](https://www.freecodecamp.org/news/how-apis-work/) sont infiniment polyvalentes et vous pouvez les utiliser pour créer d'innombrables projets uniques.

Pour vous aider à démarrer votre pratique du codage, je vais vous montrer 9 idées de projets différentes – toutes utilisant des APIs d'une manière ou d'une autre – que vous pouvez utiliser pour développer vos compétences en programmation.

Commençons !

## **Comment construire une application de signature électronique**

Nous commencerons par construire une application de signature électronique en utilisant quelques APIs. Ces APIs possèdent la plupart des fonctionnalités requises pour construire une application de signature électronique.

Vous pouvez utiliser l'[API DocuSign](https://developers.docusign.com/docs/esign-rest-api/reference/) pour générer des signatures numériques personnalisées, configurer des flux de travail, des modèles, des règles de balisage, un stockage sécurisé de documents, un chiffrement, et bien plus encore dans un environnement sécurisé.

Alors, comment démarrer avec ce projet ? Je recommande d'utiliser React, Node et MongoDB pour créer ce type d'application. Voici un aperçu des étapes que vous pourriez suivre :

* Lire la documentation de l'API DocuSign et s'inscrire pour un compte développeur.
* Concevoir l'interface utilisateur en utilisant React ou Angular
* Implémenter la logique back-end en utilisant NodeJS
* Tester et déboguer votre application dans le bac à sable de l'API DocuSign, et vous êtes prêt à partir.

## **Comment construire une application de suivi du marché boursier**

Si vous cherchez à affûter vos compétences en développement tout en produisant quelque chose de valable et d'impressionnant, la création d'une application de suivi du marché boursier pourrait être une excellente option.

Ce type d'application peut surveiller les valeurs boursières et les stocker dans une base de données pour un accès et une évaluation rapides. En utilisant l'[API Alpha Vantage](https://www.alphavantage.co/documentation/), vous pouvez accéder à des données sur les actions et les prix.

Pour ce projet, vous devrez utiliser une bibliothèque de graphiques comme Chart.js, Highcharts ou D3.js. Ces bibliothèques aideront à afficher les données de manière plus visuellement attrayante.

Vous pourriez également vouloir stocker des données telles que les cotations boursières, les données historiques et les portefeuilles utilisateurs, vous aurez donc besoin d'une base de données pour cela. Je suggère MongoDB ou PostgreSQL comme deux bons choix. Pour le front-end, React serait un bon choix, et vous pouvez utiliser Node pour le back-end.

Alors, comment démarrer ?

1. Tout d'abord, vous voudrez identifier les fonctionnalités clés que vous souhaitez inclure, comme les cotations boursières en temps réel, les données historiques des actions, le suivi de portefeuille, les listes de surveillance personnalisables, les alertes, et ainsi de suite.
2. Vous utiliserez l'API Alpha Vantage comme source de données pour les données du marché boursier. Alpha Vantage fournit un ensemble complet et fiable d'APIs pour accéder aux données du marché boursier, y compris les cotations boursières, les indicateurs techniques, les données historiques, et plus encore.
3. Vous devrez également créer une interface intuitive et conviviale.
4. Vous devrez intégrer l'API Alpha Vantage pour récupérer les données boursières en temps réel ou historiques.
5. Ensuite, vous implémenterez la fonctionnalité principale en utilisant l'API Alpha Vantage. Cela peut inclure l'affichage des cotations boursières en temps réel, des graphiques, des nouvelles, le suivi de portefeuille, les listes de surveillance, les alertes et les notifications.
6. Enfin, vous vous assurerez que les données utilisateur et les informations financières sont protégées et sécurisées en implémentant des mesures de sécurité appropriées, telles que le chiffrement des données, l'authentification et l'autorisation.

Construire une application comme celle-ci est un excellent moyen de vous aider à pratiquer vos compétences en développement avec quelque chose d'excitant et d'utile.

## **Comment construire une application de gestion de livraison**

Créer une application de gestion de livraison est en fait assez simple. Elle aide les entrepreneurs et les propriétaires d'entreprises à livrer leurs marchandises aux clients de manière efficace.

* Vous aurez besoin d'outils comme [Google Maps](https://developers.google.com/maps), [Geocoding](https://developers.google.com/maps/documentation/geocoding/overview), ou d'autres APIs de géolocalisation pour commencer.
* Vous devrez créer une interface pour que les clients entrent leur adresse de livraison et suivent l'emplacement en temps réel des livreurs en utilisant l'API Google Maps.
* Pour chaque chauffeur, vous devriez créer un profil avec des informations de contact, une heure d'arrivée estimée et tous les détails sur les marchandises livrées.
* Les clients devraient pouvoir suivre leurs livraisons en temps réel tout en calculant la distance et l'optimisation de l'itinéraire pour de meilleures prédictions sur les heures d'arrivée.

C'est comme créer une version plus petite de Zomato ou DoorDash (aux États-Unis).

## **Comment développer une application de centre commercial en ligne**

Si vous êtes prêt à travailler avec de nombreuses APIs différentes, ce projet d'application de centre commercial en ligne sera amusant pour vous. Vous utiliserez les APIs ci-dessous pour construire une application e-commerce moderne pour vendre tout, des vêtements et accessoires aux épiceries ou meubles.

Pour ce projet, vous devrez utiliser les APIs suivantes :

* Une API de passerelle de paiement comme l'API PayPal ou l'API Stripe pour collecter les paiements des utilisateurs.
* Un langage de requête comme l'API GraphQL pour gérer les opérations de données et récupérer les données nécessaires à l'application.
* Une API d'expédition pour fournir des services de livraison aux clients.
* Une API d'inventaire pour synchroniser l'inventaire entre plusieurs magasins et entrepôts.
* Une API de commentaires pour enregistrer les avis des clients sur les produits.

En utilisant ces APIs et en développant votre propre code front-end, vous pouvez créer une application de centre commercial en ligne qui facilitera la commande de produits pour les clients dans plusieurs magasins.

## **Comment concevoir un outil de calculateur de taux d'imposition**

Pour votre prochain projet, pourquoi ne pas essayer de concevoir un outil de calculateur de taux d'imposition pour un usage personnel ?

Avec les taxes variant d'un pays à l'autre et d'un état à l'autre, il peut être confus de calculer avec précision votre taux d'imposition.

Vous aurez besoin d'une API, comme l'[API SalesTax de TaxJar](https://developers.taxjar.com/api/reference/), qui fournit des informations à jour sur les taxes de vente locales pour les produits et services.

Avec des connaissances de base en HTML, CSS, JavaScript et API, vous pouvez créer un outil de calculateur de taux d'imposition entièrement fonctionnel. Non seulement cela sera utile pour les utilisateurs, mais cela offre également une excellente expérience de pratique de développement pour les développeurs.

## **Comment développer une application d'édition d'images**

Développer une application web d'édition d'images peut être assez laborieux, mais il existe de nombreuses APIs qui peuvent vous aider à simplifier certains des processus comme l'ajustement du contraste, le redimensionnement d'une image, ou la réalisation de quelques éditions d'images rapides.

Si vous pensez à développer votre propre éditeur d'images, voici quelques ressources :

* Vous pouvez utiliser l'[API de traitement d'images d'ImageMagick](https://imagemagick.org/index.php) pour manipuler et transformer des images.
* Vous pouvez utiliser les [APIs de Vision par Ordinateur d'Azure](https://azure.microsoft.com/en-in/products/cognitive-services/computer-vision) pour ajouter des superpositions de texte sur les images.
* Vous pouvez utiliser l'API [Remove Background](https://www.slazzer.com/api) de Slazzer pour éliminer tout bruit de fond indésirable ou ajouter cette fonctionnalité si nécessaire.
* L'[API de Collage d'Images Everypixel](https://labs.everypixel.com/api) vous aide à créer des collages photo personnalisés.

## **Comment créer une application de conférence vidéo en ligne**

Les applications de conférence vidéo deviennent de plus en plus populaires car elles nous offrent un moyen facile de rester connectés, peu importe la distance.

Il est possible de construire votre propre application de conférence vidéo avec l'aide d'APIs et un peu de savoir-faire en codage.

Pour commencer, vous aurez besoin d'une API qui fournit la fonctionnalité de conférence vidéo, comme l'[API Vidéo Twilio](https://www.twilio.com/docs/video).

Vous aurez également besoin d'une API pour l'authentification comme l'[API Auth0](https://auth0.com/docs/api).

Avec ces deux APIs combinées, vous pouvez créer une application qui permet aux utilisateurs de s'inscrire et de se connecter de manière sécurisée, puis de commencer un appel vidéo avec leurs contacts.

## **Comment construire un système de gestion immobilière**

Construire un système de gestion immobilière pour suivre vos propriétés semble être une excellente idée de projet, n'est-ce pas ?

En combinant différentes APIs, vous pouvez assembler un système qui vous aiderait à gérer et à maintenir efficacement vos investissements.

Vous pouvez utiliser l'[API Google Maps](https://developers.google.com/maps) pour acquérir des informations géographiques concernant vos propriétés et les stocker dans la base de données.

De plus, avec l'assistance d'APIs comme l'API Zillow ou l'API Trulia, vous pouvez obtenir des informations de prix précises pour des propriétés similaires situées dans des zones particulières.

Cela est bénéfique lorsqu'il s'agit d'obtenir la valeur marchande de vos propriétés.

Enfin, l'[API Google Calendar](https://developers.google.com/calendar/api/guides/overview) ou l'API Microsoft Outlook peut être utilisée pour générer des notifications automatisées lors de la collecte des paiements de loyer des locataires.

En résumé, la fusion de ces APIs peut vous aider à créer un système de gestion immobilière efficace qui économise du temps et de l'argent tout en organisant correctement vos propriétés !

## **Comment construire un outil d'organisation de planification d'événements**

Les organisateurs cherchant à planifier des événements de toutes tailles – des anniversaires aux mariages, et aux rassemblements corporatifs – ont besoin d'aide pour gérer les tâches qui y sont associées.

Une application de planification d'événements fournit un excellent outil pour cela, donnant aux utilisateurs des délais et des rappels tout en travaillant pour préparer l'occasion.

* En utilisant Google Calendar et l'[API Trello](https://developer.atlassian.com/cloud/trello/rest/), il est possible de fournir des fonctionnalités d'intégration de calendrier qui récupèrent les détails des événements et permettent aux utilisateurs de synchroniser entre plusieurs plateformes.
* L'API Trello aide également les utilisateurs à garder une trace des tâches avant et après un événement, créant des listes qui détaillent ce qui doit être accompli.
* Chaque tâche peut se voir attribuer une date d'échéance et un niveau de priorité, afin que vous puissiez être sûr que rien n'est manqué ou négligé avant l'arrivée du grand jour.

Vous pouvez également configurer une fonctionnalité de notification pour les utilisateurs, les informant lorsqu'une tâche nécessite de l'attention ou en leur fournissant des rappels utiles concernant les délais à venir.

Toutes ces fonctionnalités combinées feraient de votre outil une ressource utile pour tout type de planificateur d'événements ou d'organisateur.

## **Conclusion**

Vous pouvez développer vos compétences et vos connaissances en tant que programmeur en construisant quelques projets de base. Avec l'aide des APIs et des idées de projets présentés dans cet article, vous pouvez construire des projets intéressants et améliorer votre parcours de développement.

Les APIs peuvent sembler intimidantes au premier abord, mais avec une pratique constante, vous vous habituerez à travailler avec elles. Et à mesure que vos compétences en programmation grandissent, vous pourrez repousser les limites et explorer plus de possibilités.

Bon codage !

Lire plus sur les APIs :

* [APIs Publiques pour Développeurs](https://www.freecodecamp.org/news/public-apis-for-developers/)
* [Meilleures Pratiques de Test d'API – Comment Tester les APIs pour Débutants](https://www.freecodecamp.org/news/rules-of-api-testing-for-beginners/)
* [Utiliser React et les APIs pour Construire une Application Météo](https://www.freecodecamp.org/news/use-react-and-apis-to-build-a-weather-app/)