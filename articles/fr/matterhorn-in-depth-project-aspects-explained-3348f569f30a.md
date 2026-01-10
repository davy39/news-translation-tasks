---
title: Matterhorn en profondeur — Aspects du projet expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-01T20:25:08.000Z'
originalURL: https://freecodecamp.org/news/matterhorn-in-depth-project-aspects-explained-3348f569f30a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1eutc7Qqi17u6Ll0E4wKoA.jpeg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Testing
  slug: testing
- name: TypeScript
  slug: typescript
seo_title: Matterhorn en profondeur — Aspects du projet expliqués
seo_desc: 'By Ethan Arrowood

  Recently, I published an article on my new project, Matterhorn ?, a Node.js API
  server boilerplate. It provides a set of opinionated configuration files and some
  basic example code. These help developers get up and running faster wi...'
---

Par Ethan Arrowood

Récemment, j'ai publié un [article](https://medium.freecodecamp.org/announcing-matterhorn-a-node-js-api-server-boilerplate-4994759f1bf6) sur mon nouveau projet, [Matterhorn ?,](https://github.com/Ethan-Arrowood/matterhorn) un modèle de serveur API Node.js. Il fournit un ensemble de fichiers de configuration opinionnés et quelques exemples de code de base. Ceux-ci aident les développeurs à démarrer plus rapidement avec Node.js et TypeScript.

Matterhorn est inspiré par des projets comme Create React App et Gatsby CLI. L'objectif du projet est d'éliminer la barrière à l'entrée requise pour utiliser des outils de programmation tels que les systèmes de typage, les frameworks de test et de linting, et même l'intégration continue de base.

Cet article de blog passera en revue chacun des aspects principaux de Matterhorn. Je discuterai des détails et des décisions opinionnées derrière le framework de choix.

### Runtime & Système de types

Le cœur de ce projet est construit avec Node.js, un runtime JavaScript basé sur le [moteur V8 JavaScript de Chrome](https://developers.google.com/v8/). Il est recommandé d'utiliser la dernière version stable de Node.js pour exécuter ce projet. Au moment de la rédaction de cet article, il s'agit de la **11.7.0**.

Node.js est piloté par une boucle d'événements non bloquante, ce qui en fait un excellent choix pour construire des applications réseau scalables. Pour plus d'informations sur Node.js, consultez leur [site web](https://nodejs.org/en/).

De nombreux projets Node.js sont écrits en JavaScript. Cependant, TypeScript, un système de types pour JavaScript, a connu un pic d'attention à la fin de 2018. De nombreux développeurs sont intéressés à apprendre TypeScript en 2019. Son adoption dans les projets JavaScript open source est en augmentation. L'objectif initial de Matterhorn était de permettre aux développeurs intéressés de construire des applications backend Node.js avec TypeScript de démarrer plus rapidement. Ainsi, Matterhorn lui-même est écrit en TypeScript.

En tant que système de types, TypeScript est très complet. Bien qu'il puisse avoir une courbe d'apprentissage abrupte au début, les avantages de son utilisation sont primordiaux. Il aide les développeurs à écrire un code plus propre et moins bogué. Et une fois que vous êtes familiarisé avec l'écosystème et le processus de configuration, vous écrirez de nouvelles fonctionnalités plus rapidement qu'avec JavaScript natif. Des éditeurs comme [VSCode](https://code.visualstudio.com/) ont TypeScript activé par défaut. Il fournit un ensemble complet d'outils de développement pour améliorer davantage l'expérience des développeurs.

### Framework API

Bien qu'il soit possible d'écrire une API HTTP en utilisant uniquement Node.js, si un développeur souhaite atteindre la maintenabilité de l'écosystème, la sécurité et la scalabilité, il devrait utiliser un framework API. En ce qui concerne les frameworks API Node.js, il y en a beaucoup parmi lesquels choisir, tels que Express, Koa et Hapi. Mais il y a un framework plus rapide et plus résilient que tous les autres : [Fastify](https://www.fastify.io/).

![Image](https://cdn-media-1.freecodecamp.org/images/Q8r068DOB8vOuyi-G1DtNEQWMUW-so1bn6xN)
_Logo Fastify de [https://www.fastify.io](https://www.fastify.io" rel="noopener" target="_blank" title=")_

Fastify est un framework web rapide et à faible surcharge, pour Node.js. Il est inspiré par Hapi et Express et fonctionne sur une architecture basée sur des plugins. Il dispose d'une communauté open source très active, et de plus de 90 plugins publics, allant de l'authentification aux liaisons de bases de données et tout ce qui se trouve entre les deux. De plus, Fastify maintient son propre ensemble de liaisons TypeScript qui sont livrées avec le module directement depuis NPM.

### Test Runner et Linter

Soutenir votre code avec des tests unitaires est une norme dans l'écosystème de programmation d'aujourd'hui. Matterhorn est livré avec Jest, un test runner JavaScript populaire. Il est configuré pour fonctionner avec TypeScript et contient même quelques exemples pour tester votre API Fastify. Notez la méthode `inject` de Fastify ; elle est très utile pour tester le comportement de vos routes.

En plus d'exécuter des tests, Jest est également configuré pour générer des documents de couverture de code. Bien que la couverture de code ne soit pas la métrique la plus importante à considérer lors de l'écriture de tests unitaires, elle est précieuse et peut vous aider à vérifier que vous couvrez au moins autant de votre base de code que possible.

Dans la communauté open source, les linters de code sont un choix populaire pour imposer un certain style de programmation. Ils éliminent le besoin de revues de code stylistiques. Ils peuvent aider les développeurs à détecter des erreurs dans leur code avant de l'exécuter.

Matterhorn est équipé de ESLint, un choix populaire pour le linting JavaScript. Le projet était initialement livré avec TSLint. Cependant, cela a été remplacé en faveur de ESLint parce que TypeScript a [officiellement annoncé](https://github.com/Microsoft/TypeScript/issues/29288) des plans pour soutenir directement le projet ESLint. Le linter est configuré pour correspondre aux opinions des mainteneurs du projet. Il peut facilement être reconfiguré pour vos propres directives stylistiques.

### Intégration Continue

Le dernier aspect de Matterhorn est l'inclusion d'un pipeline d'intégration continue entièrement configuré. Pour de nombreux développeurs, en particulier ceux qui apprennent ou qui bricolent, cette fonctionnalité peut ne pas avoir beaucoup d'utilité. Cependant, pour ceux qui tentent de développer une application complète et qui veulent la stabilité du développement d'entreprise, cette CI est faite pour eux.

Le pipeline est construit sur Azure DevOps (anciennement nommé Visual Studio Team Services). Azure DevOps est gratuit pour les dépôts publics, et les utilitaires de pipeline sont extensifs. Il peut être configuré de manière programmatique ([Matterhorn](https://github.com/Ethan-Arrowood/matterhorn/blob/master/azure-pipelines.yml)) ou via un éditeur visuel (dans un navigateur). Vous pouvez consulter le pipeline CI de Matterhorn [ici](https://dev.azure.com/arrowoode/matterhorn/_build?definitionId=3). Il construit automatiquement pour les mises à jour des pull requests et tout nouveau commit sur _master_.

### Conclusion

Merci d'avoir pris le temps de lire les différents aspects de Matterhorn. Beaucoup de réflexion a été mise dans le choix des services et des modules utilitaires pour ce projet. Le projet est open source, et il y a beaucoup de place pour des améliorations, donc si vous souhaitez contribuer, consultez-le ci-dessous.

[**Ethan-Arrowood/matterhorn**](https://github.com/Ethan-Arrowood/matterhorn)  
[_Un projet de modèle d'API construit sur Node.js et TypeScript ? - Ethan-Arrowood/matterhorng_ithub.com](https://github.com/Ethan-Arrowood/matterhorn)