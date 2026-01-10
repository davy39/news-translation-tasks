---
title: Quels éléments doivent être configurables dans une application ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-27T20:30:15.000Z'
originalURL: https://freecodecamp.org/news/what-should-be-configurable-in-apps
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/sigmund-f0dJjQMhfXo-unsplash.jpg
tags:
- name: configuring settings
  slug: configuring-settings
- name: configuration
  slug: configuration
- name: Web Applications
  slug: web-applications
seo_title: Quels éléments doivent être configurables dans une application ?
seo_desc: "By Kenneth Angelo Reyes\nConfiguration is an essential part of every application.\
  \ It helps enhance an application's flexibility and maintainability. \nWith this\
  \ in mind, it's very important that developers are able to correctly identify what\
  \ items shou..."
---

Par Kenneth Angelo Reyes

La configuration est une partie essentielle de chaque application. Elle aide à améliorer la flexibilité et la maintenabilité d'une application. 

Avec cela à l'esprit, il est très important que les développeurs soient capables d'identifier correctement les éléments qui doivent être configurables.

Dans cet article, je vais vous présenter 8 éléments qui doivent être configurables dans vos applications.

## Définir "Configuration"

Nous ne nous alignerons pas sur les plateformes existantes.

Pour le contexte de cet article, une configuration d'application a les caractéristiques suivantes :

* Un ensemble de valeurs simples ou complexes qui peuvent affecter le comportement d'une application
* Les valeurs peuvent être facilement modifiées sans nécessiter de déploiement de code

Cela étant dit, passons à notre liste !

## Les "Configurables"

Voici les 8 éléments qui doivent être configurables dans vos applications.

### Nombres Magiques

Ce sont des nombres spéciaux utilisés dans certains affichages, validations ou règles métiers.

**Exemples :**

* Nombre de jours avant qu'un SLA (Service Level Agreement) soit violé
* Nombre de décimales lors de l'affichage d'une devise

### URLs

Lors de la connexion à des services tiers, on ne sait jamais quand leurs URLs changeront. Il est préférable de garder ces valeurs configurables. De plus, des URLs configurables peuvent vous aider à contrôler la valeur dans différents environnements.

**Exemples :**

* Points de terminaison d'API
* Sites web externes

### Basculage de Fonctionnalités

Cela est utile lorsqu'il y a une fonctionnalité déjà en production, mais qui ne peut être activée qu'après un certain temps.

Un exemple de cela est une fonctionnalité qui ne peut être activée qu'après un événement en direct. Normalement, cela peut être une valeur booléenne, mais vous pouvez également utiliser une date et une heure pour cela. Cela signifie simplement que la fonctionnalité sera automatiquement activée une fois ce temps écoulé.

### Modèles Regex

Certains modèles Regex, en particulier ceux utilisés dans la validation, ont le potentiel de changer régulièrement.

Un exemple de cela est la validation des numéros de téléphone. Initialement, votre application peut permettre les numéros de téléphone de plusieurs pays. Ensuite, peut-être qu'un changement de exigences est survenu où vous devez maintenant permettre uniquement les numéros de téléphone de pays spécifiques. 

Si votre modèle de validation est dans la configuration, alors vous pouvez rapidement apporter cette modification.

### Dates Spéciales

Pas les romantiques ! Dans certaines applications, il est nécessaire de "bloquer" certaines dates pour qu'elles ne puissent pas être sélectionnées par les utilisateurs.

Un exemple parfait de cela sont les jours fériés. Puisque ces dates peuvent changer régulièrement, elles doivent être placées dans la configuration.

### Chaînes de Connexion

Les chaînes de connexion à la base de données ne doivent jamais être placées dans votre code ! Lorsque vous placez les chaînes de connexion dans la configuration, vous pourrez également définir une valeur différente par environnement.

### Formules

Pour les applications liées à la finance, rendre les formules configurables est très important. Pour ces types d'applications, s'adapter aux changements de politique ou de réglementation dès que possible est une nécessité.

### Messages Spéciaux

Cela peut être plus applicable aux applications non-CMS. Dans certains cas, les changements réguliers dans les messages textuels sont liés à des politiques légales ou réglementaires. Par conséquent, ces messages doivent être faciles à mettre à jour.

Un bon exemple de cela est une annonce qui indique si l'application rencontre actuellement des problèmes ou est en maintenance.

## Conclusion

Ce sont les 8 éléments que je crois doivent être configurables dans chaque application. Je suis sûr que vous avez d'autres éléments en tête. Faites-moi savoir ! J'ai hâte d'avoir de vos nouvelles.

Heureux que vous ayez atteint la fin de cet article. J'espère que vous avez appris quelque chose de nouveau de moi aujourd'hui.

_[Photo de couverture](https://unsplash.com/photos/f0dJjQMhfXo) [f](https://unsplash.com/@sigmund?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)rom [Unsplash](https://unsplash.com/s/photos/settings?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_