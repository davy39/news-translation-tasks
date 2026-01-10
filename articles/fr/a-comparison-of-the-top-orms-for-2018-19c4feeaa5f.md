---
title: Quel ORM JavaScript devriez-vous utiliser en 2018 ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-03T22:24:30.000Z'
originalURL: https://freecodecamp.org/news/a-comparison-of-the-top-orms-for-2018-19c4feeaa5f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1fDVMWj-QH04s4QxaGwOsg.jpeg
tags:
- name: api
  slug: api
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Quel ORM JavaScript devriez-vous utiliser en 2018 ?
seo_desc: 'By John Vandivier

  NOTE: May 2018: Read From TypeORM to LoopBack: A Retrospective for an updated perspective!

  — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

  This article reviews Object Relational Mapping (ORM) solutions in the JavaScrip...'
---

Par John Vandivier

**NOTE : Mai 2018 : Lisez** [***De TypeORM à LoopBack : Une rétrospective***](https://hackernoon.com/from-typeorm-to-loopback-a-retrospective-188ea18527a2) pour une perspective actualisée !

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Cet article passe en revue les solutions de [Mapping Objet-Relationnel](https://en.wikipedia.org/wiki/Object-relational_mapping) (ORM) dans l'écosystème JavaScript, et identifie une solution idéale basée sur des exigences spécifiques.

### **Qu'est-ce qu'un ORM et pourquoi est-ce si important ?**

Les solutions ORM sont utiles pour faciliter le développement d'API pilotées par les données. Les utilisateurs ont des besoins concrets qui orientent le modèle de données d'une application. Dans le développement traditionnel, cette architecture de données est généralement implémentée et versionnée à l'aide de scripts de base de données tels que des scripts SQL. Une bibliothèque distincte est ensuite utilisée pour l'application serveur afin d'exécuter des actions CRUD sur la base de données.

Les ORM fonctionnent comme une API de haut niveau pour exécuter le CRUD, et de nos jours, les ORM de qualité nous permettent également d'initialiser les données par le code. La manipulation complexe des données, le nettoyage, etc., est souvent plus facile dans le code. Bien que des outils dédiés d'Extraction, Transformation et Chargement ([ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load)) existent, les mêmes tâches ETL peuvent être facilement implémentées dans un ORM.

L'implémentation de l'extraction, de la transformation et du chargement avec du code permet à un système d'intégrer plus facilement des données provenant de sources très différentes. Les bases de données SQL de plusieurs types, les données NoSQL, les données du système de fichiers et les données tierces peuvent toutes être intégrées sous un seul langage avec un ORM JavaScript.

Enfin, le contrôle des données orienté code permet également à un système d'implémenter l'utilisation des données au moment de l'exécution ou dans le processus de build, et d'adapter de manière flexible l'utilisation pendant le processus de développement selon les besoins.

Pour résumer, les ORM améliorent la productivité des développeurs en fournissant une API de haut niveau, dans un seul langage, avec des fonctionnalités qui nécessiteraient traditionnellement plusieurs outils et compétences différents. Moins de besoins en compétences, en outils et d'heures requises favorisent la marge du projet. Les exigences imprévues et le calendrier du projet sont mieux préparés grâce à une configuration flexible des données au build et à l'exécution.

### **Capacités ORM préférées**

Le contexte particulier du projet menant à cette revue d'ORM nécessite l'implémentation d'une application [JavaScript universelle](https://medium.com/@mjackson/universal-javascript-4761051b7ae9) de pointe, de type CMS.

Les frameworks JavaScript universels de pointe se déclinent essentiellement en 3 saveurs : Angular, React et Vue. C'est-à-dire [Angular Universal](https://universal.angular.io/), [Next](https://github.com/zeit/next.js/) et [Nuxt](https://nuxtjs.org/).

Node prend en charge nativement les opérations sur le système de fichiers, de sorte que les exigences en matière de données de système de gestion de contenu se résument à une préférence pour une large prise en charge des bases de données. Au total, les exigences suivantes sont prises en compte :

1. Prise en charge de Mongo et MySQL, avec une préférence pour la prise en charge d'options supplémentaires
    
2. Intégration avec Webpack
    
3. Intégration avec Express
    
4. Impact minimal sur les [performances](https://medium.com/@ameykpatil/why-orm-shouldnt-be-your-best-bet-fffb66314b1b) au moment de l'exécution
    
5. Syntaxe intuitive
    
6. Fonctionnalités supplémentaires
    
7. Ratio élevé d'étoiles GitHub par rapport aux tickets (issues)
    
8. Activement maintenu sans échec de build ou dépendances obsolètes
    

### **Les candidats et les résultats**

Chaque candidat a reçu un score entre 0 et 10 pour chaque capacité préférée. Un score de 5 signifie acceptable. La moyenne d'une colonne peut être supérieure ou inférieure à 5. Par exemple, un ORM prenant en charge plusieurs bases de données NoSQL et aucune base de données SQL recevra un score entre 2 et 4. 0 indique l'absence totale d'une fonctionnalité.

![Image](https://cdn-media-1.freecodecamp.org/images/xZdD-bktDeeZ0Q6fQxxooOyg0kaoWEu3DA3J align="left")

*Consultez* [*cette feuille Google*](https://docs.google.com/spreadsheets/d/1sSbY8SLWA9lvvnTHX41t0TVPXwZ4A4ddO_KJMa20fA4/edit#gid=0) *pour cliquer sur les hyperliens ou copier les données sous forme de tableau.*

Une mention spéciale à [joi](https://github.com/hapijs/joi), [pg](https://github.com/go-pg/pg) et [knex](http://knexjs.org/). Ces bibliothèques ne sont pas des ORM complets mais elles sont excellentes dans ce qu'elles font. Si vous n'avez pas besoin d'un ORM complet, jetez-y un coup d'œil pour voir si elles peuvent répondre à votre besoin.

### **Conclusion**

Les totaux reflètent l'utilité globale de chaque solution. Les 5 meilleurs résultats étaient :

1. Loopback
    
2. Waterline
    
3. Mongoose
    
4. TypeORM
    
5. Sequelize
    

Une combinaison de besoins spécifiques au projet, de facteurs omis et de préférences personnelles a conduit aux 3 meilleurs choix.

Waterline est fortement intégré au framework Sails et Mongoose ne prend en charge que MongoDB.

Sequelize et NodeORM2 sont limités au SQL et manquent de génération d'API.

Grâce à la syntaxe TypeScript, TypeORM s'intègre bien à un projet Angular.

En tant que développeur, je recommande de prototyper plus d'une solution de tête pour identifier le véritable gagnant. Les 3 meilleures solutions, qui sont toutes des candidates au prototypage, incluent :

1. Loopback
    
2. TypeORM
    
3. Caminte
    

J'ai soumis ces informations aux autres développeurs du projet, et en tant qu'équipe, nous avons décidé d'essayer d'abord TypeORM. Revenez plus tard pour la rétrospective !

Que pensez-vous de ce résultat ? Laissez un commentaire ou partagez vos réflexions sur [cette comparaison Slant](https://www.slant.co/improve/topics/11235/~javascript-orms).