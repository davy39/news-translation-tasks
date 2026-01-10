---
title: Comment tirer parti des paramètres par défaut de JavaScript pour l'injection
  de dépendances
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-22T10:46:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-take-advantage-of-javascripts-default-parameters-for-dependency-injection-98fc423328e1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FbjjCStVtHqlJdO4vpLLtQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment tirer parti des paramètres par défaut de JavaScript pour l'injection
  de dépendances
seo_desc: 'By Ricardo Sousa

  These days it’s quite common to use Dependency Injection, which allows a projects’
  modules to be loosely coupled. But as projects grow in complexity, we have an astronomical
  number of dependencies to control.

  To work around this prob...'
---

Par Ricardo Sousa

De nos jours, il est assez courant d'utiliser [l'injection de dépendances](https://en.wikipedia.org/wiki/Dependency_injection), ce qui permet aux modules d'un projet d'être faiblement couplés. Mais à mesure que les projets gagnent en complexité, nous avons un nombre astronomique de dépendances à contrôler.

Pour contourner ce problème, nous nous tournons souvent vers des conteneurs d'injection de dépendances. Mais est-ce nécessaire dans toutes les situations ?

Dans cet article, j'aborderai la manière dont les [paramètres par défaut de JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters) peuvent nous aider sur cette question. Pour ce faire, nous allons implémenter une application simple en Node.JS. Elle disposera des fonctionnalités de création et de lecture des informations des utilisateurs en utilisant trois approches différentes :

1. Sans injection de dépendances
2. Avec injection de dépendances
3. Avec injection de dépendances et paramètres par défaut

### Structure du projet

Nous allons structurer notre exemple de projet [par fonctionnalité](https://blog.risingstack.com/node-hero-node-js-project-structure-tutorial/) (au passage — ne structurez pas vos fichiers par rôles). Ainsi, la structure ressemblera à ceci :

```
├── users/
│   ├── users-repository.js
│   ├── users.js
│   ├── users.spec.js
│   ├── index.js
├── app.js
```

**Note** : Pour les besoins de cet exemple, nous enregistrerons les informations des utilisateurs en mémoire.

### Sans injection de dépendances

En analysant le code précédent, nous vérifions que nous sommes limités par l'instruction : `const usersRepo = require('./users-repository')` dans **users**. Le module **users**, avec cette approche, est fortement couplé à **users-repository**.

Cela nous limite à l'utilisation de l'implémentation d'un autre dépôt sans modifier l'instruction **require**. Lorsque le **require** est utilisé, nous créons une dépendance statique vers le module requis. De ce fait, nous ne pouvons pas utiliser un autre dépôt dans le modèle d'application en dehors de celui défini par le module **users-repository**.

En plus de cela, nous sommes également liés à **users-repository** dans **users-spec** à cause de la dépendance statique mentionnée précédemment. Ces tests unitaires servent à tester uniquement le module **users** et rien d'autre. Imaginez si le dépôt était connecté à une base de données externe. Nous devrions interagir avec la base de données pour pouvoir effectuer les tests.

### Avec injection de dépendances

Avec l'injection de dépendances, le module **users** n'est plus couplé au module **users-repository**.

La principale différence par rapport à l'approche précédente est que nous n'avons plus de dépendance statique dans le module **users** (nous n'avons plus l'instruction : `const usersRepo = require('./users-repository')`). Au lieu de cela, le module **users** exporte une [fonction usine (factory function)](https://medium.com/javascript-scene/javascript-factory-functions-with-es6-4d224591a8b1) avec un paramètre pour le dépôt. Cela nous permet de passer n'importe quel dépôt au module à un niveau supérieur.

Une alternative à la fonction usine consiste à ajouter un paramètre pour l'argument du dépôt dans les fonctions **create** et **read**. Mais si les deux fonctions dépendent du même dépôt, nous pouvons les encapsuler avec une fonction et tirer parti des [fermetures (closures) de JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures).

Désormais, dans le module **app**, nous avons la liberté de définir le dépôt que nous souhaitons utiliser. Regardez également les tests unitaires. Nous pouvons maintenant tester le module **users** sans nous soucier du dépôt. Il suffit de le [mocker](https://en.wikipedia.org/wiki/Mock_object) !

Cependant, soyons honnêtes — à quelle fréquence définissons-nous des dépendances qui changent tout au long du cycle de vie de l'application ? Normalement, nous essayons d'éviter les dépendances statiques car elles rendent les tests plus difficiles. Mais maintenant, puisque nous voulons de la testabilité, nous devons passer une instance du dépôt au module **users** chaque fois que nous voulons l'utiliser.

Vous savez ce qui serait vraiment génial ? Si nous pouvions utiliser le module sans avoir à lui fournir un dépôt à chaque fois. Nous pouvons le faire en JavaScript avec les paramètres par défaut.

### Avec injection de dépendances et paramètres par défaut

Avec cette stratégie, en plus de l'injection de dépendances que nous avons vue dans l'approche précédente, le paramètre défini dans la fonction usine exportée par le module **users** est désormais un paramètre par défaut : `usersRepo = defaultUsersRepo`.

Avec le paramètre par défaut, si nous ne passons pas d'argument, la valeur du paramètre par défaut est utilisée par la fonction. Sinon, la valeur de l'argument est utilisée. C'est la même chose que d'utiliser la technique d'injection de dépendances définie dans l'approche précédente.

Maintenant, nous avons à nouveau la dépendance statique dans le module **users**. Cependant, cette dépendance statique sert uniquement à définir la valeur utilisée dans le paramètre par défaut si aucun argument n'est passé à la fonction usine.

Avec cette approche, nous ne sommes pas obligés de passer le dépôt dans le module **app** lors de l'appel du module **users**. Pourtant, nous pouvons toujours le faire. Nous pouvons également vérifier que les tests unitaires peuvent continuer à utiliser le dépôt simulé (mock), car nous sommes en mesure de le passer au lieu d'utiliser la valeur du paramètre par défaut.

### Conclusion

Les [paramètres par défaut](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters) sont une fonctionnalité simple de JavaScript, mais puissante. Grâce à eux, nous pouvons implémenter de meilleures solutions.

N'hésitez pas à me poser des questions.

### Ressources supplémentaires

Dépôt GitHub avec les exemples : [ici](https://github.com/rikmms/js-default-params-and-di).

[Mattias Petter Johansson](https://www.freecodecamp.org/news/how-to-take-advantage-of-javascripts-default-parameters-for-dependency-injection-98fc423328e1/undefined) propose une excellente vidéo explicative sur l'injection de dépendances :

Si vous avez apprécié cet article, n'hésitez pas à m'applaudir (claps) pour que plus de personnes puissent le voir. Merci !