---
title: 'Stratégies d''applications Web réutilisables : trois modèles pour exécuter
  la même application à plusieurs endroits'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-25T19:44:20.000Z'
originalURL: https://freecodecamp.org/news/reusable-web-application-strategies-d51517ea68c8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0uyfg5ldLO2nfH7wZqJnfw.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Stratégies d''applications Web réutilisables : trois modèles pour exécuter
  la même application à plusieurs endroits'
seo_desc: 'By Cory House

  Imagine your team just deployed an amazing todo list app. A month later, another
  team in your company wants to run your todo app within their invoice app.

  So now you need to run your todo app in two spots:


  By itself

  Embedded within the...'
---

Par Cory House

Imaginez que votre équipe vient de déployer une application de liste de tâches incroyable. Un mois plus tard, une autre équipe de votre entreprise souhaite exécuter votre application de tâches dans leur application de facturation.

Vous devez donc exécuter votre application de tâches à deux endroits :

1. Seule
2. Intégrée dans l'application de facturation

Quelle est la meilleure façon de gérer cela ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/BXFbpSm9d5kyu0gTY7oqSyL-u5nElkgfvRim)

Pour exécuter une application à plusieurs endroits, vous avez trois options :

1. **iframe** — Intégrez l'application de tâches dans l'application de facturation via une balise <iframe>.
2. **Composant d'application réutilisable** — Partagez l'ensemble de l'application de tâches.
3. **Composant d'interface utilisateur réutilisable** — Partagez uniquement le balisage de l'application de tâches.

Les options 2 et 3 sont généralement partagées via npm pour les applications côté client.

Pressé ? Voici le résumé.

![Image](https://cdn-media-1.freecodecamp.org/images/em5yNxf2bIJblyiQ66ykXdffXWZQn8VRHuC5)
_Le vert est bon. Le rouge est mauvais. L'orange est un avertissement._

Explorons les mérites de chaque approche.

# Option 1 : iFrame

Avec une iframe, vous pouvez composer deux applications ensemble en plaçant l'application "enfant" dans une iframe. Dans notre exemple, l'application de facturation intégrerait l'application de tâches via une iframe. Facile. Mais pas si vite...

## Quand une iframe est-elle adaptée ?

1. **Technologies incompatibles** — Si les applications que vous composez utilisent des technologies incompatibles, c'est votre seule option. Par exemple, si une application est construite en Ruby et l'autre en ASP.NET, une iframe permet aux deux applications de s'afficher côte à côte, même si elles sont en réalité incompatibles et hébergées séparément.
2. **Dimensions petites et statiques** — L'application que vous intégrez a une hauteur et une largeur statiques. Le redimensionnement dynamique des iframes est possible, mais ajoute de la complexité.
3. **Histoire d'authentification commune** — Une application intégrée dans une iframe ne devrait pas nécessiter une authentification séparée. Une authentification séparée peut entraîner des interactions maladroites, car l'application intégrée peut demander des identifiants séparés ou expirer à un moment différent de l'application hôte.
4. **Fonctionne de la même manière partout** — Avec une iframe, l'application intégrée fonctionnera de la même manière à chaque endroit où elle est intégrée. Si vous avez besoin d'un comportement significativement différent dans différents contextes, voir les autres approches ci-dessous.
5. **Aucune donnée commune** — Avec une iframe, les applications composées doivent éviter d'afficher les mêmes données. L'intégration d'une application peut entraîner des appels API dupliqués et inutiles, ainsi que des problèmes de désynchronisation entre l'application intégrée et son parent. Les changements de données dans l'iframe doivent être soigneusement communiqués au parent et vice-versa, sinon l'utilisateur verra des données désynchronisées.
6. **Peu d'interactions inter-applications** — Il devrait y avoir très peu d'interactions entre l'application hôte et l'application intégrée dans l'iframe. Bien sûr, vous pouvez utiliser [window.postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) pour passer des messages entre l'iframe et l'application hôte, mais cette approche doit être utilisée avec parcimonie car elle est fragile.
7. **Une seule équipe supporte les deux applications** — Avec les iframes, la même équipe devrait idéalement posséder et maintenir à la fois l'application parente et l'application intégrée. Sinon, vous devez accepter une relation de coordination continue entre les équipes qui supportent les applications pour assurer leur compatibilité. Des équipes séparées créent un risque continu et une charge de maintenance pour maintenir une intégration réussie et stable.
8. **Besoin de le faire une seule fois** — En raison du point ci-dessus, vous ne devriez intégrer une application dans une iframe qu'une seule fois pour éviter de créer une charge de maintenance significative. Plus une application est intégrée dans des iframes, plus vous risquez de la casser lorsque vous apportez des modifications.
9. **À l'aise avec les risques de déploiement** — Avec une iframe, vous devez accepter le risque qu'un déploiement en production de l'application intégrée puisse impacter l'application parente à tout moment. C'est une autre raison pour laquelle il est utile que la même équipe supporte à la fois l'application parente et l'application intégrée.

# Option 2 : Partager le composant d'application

Le gestionnaire de paquets de Node, npm, est devenu le moyen de facto de partager du JavaScript. Avec cette approche, vous créez un package npm et placez l'application complète à l'intérieur. Et il n'a pas besoin d'être public — vous pouvez créer un package npm privé sur npm également.

Le processus de création d'une bibliothèque de composants réutilisables dépasse le cadre de cet article. J'explore comment construire votre propre bibliothèque de composants réutilisables dans « [Building Reusable React Components](https://app.pluralsight.com/library/courses/react-creating-reusable-components) ».

Puisque vous partagez l'ensemble de l'application, elle peut inclure des appels API, des préoccupations d'authentification et des préoccupations de flux de données comme Flux/Redux, etc. Il s'agit d'un morceau de code très opinionné.

## Quand l'approche du composant d'application réutilisable est-elle adaptée ?

1. **Technologies compatibles** — Puisque vous partagez un composant réutilisable, l'application parente doit être compatible. Par exemple, si vous partagez un composant React, l'application parente devrait idéalement être écrite en React également.
2. **Taille dynamique** — Cette approche est utile si la largeur/hauteur de votre application est dynamique et ne s'adapte pas bien à un cadre de taille statique.
3. **Histoire d'authentification commune** — Les deux applications devraient idéalement utiliser la même authentification. Une authentification séparée peut entraîner des interactions maladroites, car chaque application peut demander des identifiants séparés ou expirer à un moment différent.
4. **Vous voulez que l'application fonctionne de la même manière partout** — Puisque l'API, l'authentification et la gestion d'état sont intégrées, l'application fonctionnera de la même manière partout.
5. **Aucune donnée commune** — Les deux applications travaillent principalement avec des données séparées. L'affichage d'applications côte à côte peut entraîner des appels API dupliqués et inutiles, car chaque application fait des requêtes pour les mêmes données. Cela peut également entraîner des problèmes de désynchronisation entre les deux applications. Les changements de données dans l'une doivent être soigneusement communiqués à l'autre, sinon l'utilisateur verra des données désynchronisées entre les deux applications.
6. **Peu d'interactions inter-applications** — Il devrait y avoir peu d'interactions entre les deux applications. Bien sûr, vous pouvez utiliser [window.postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) pour passer des messages entre elles, mais cette approche doit être utilisée avec parcimonie car elle est fragile.
7. **Une seule équipe supporte les deux applications** — Avec cette approche, idéalement, la même équipe possède et maintient les deux applications. Sinon, vous devez être prêt à accepter une relation de coordination continue entre les équipes qui supportent les deux applications pour assurer leur compatibilité. Des équipes séparées créent un risque continu et une charge de maintenance pour maintenir une intégration réussie et stable.

# Option 3 : Partager le composant d'interface utilisateur

Cette option est similaire à l'option #2 ci-dessus, sauf que vous **partagez uniquement le balisage**. Avec cette approche, vous omettez l'authentification, les appels API et la gestion d'état afin que **le composant soit essentiellement du HTML réutilisable**.

Des exemples populaires de composants simples comme celui-ci incluent [Material-UI](http://www.material-ui.com/#/) et [React Bootstrap](https://react-bootstrap.github.io/). Bien sûr, un composant d'application réutilisable a plus de parties mobiles, mais il fonctionne sur la même idée.

Avant de discuter des mérites de cette approche, laissez-moi répondre à une question courante : « Les composants réutilisables doivent-ils intégrer des appels API et de l'authentification ? »

Mon avis ? **Évitez d'intégrer des appels API, de l'authentification et des préoccupations de gestion d'état dans les composants réutilisables.**

Voici pourquoi :

1. Cela limite la réutilisation en liant le front-end à une API, une authentification et une gestion d'état spécifiques.
2. Souvent, des développeurs/équipes séparés gèrent l'interface utilisateur et l'API. L'intégration d'appels API dans un composant réutilisable couple l'équipe UI et l'équipe API ensemble. Si un côté change, cela impacte l'autre, ce qui crée une surcharge de coordination continue et une charge de maintenance.

Mais oui, cela signifie que chaque fois que quelqu'un utilise votre composant réutilisable, il doit configurer les appels API et les passer en props.

## Quand l'approche du composant d'interface utilisateur réutilisable est-elle adaptée ?

1. **Technologies compatibles** — Puisque vous partagez un composant réutilisable, l'application parente doit être compatible. Par exemple, si vous partagez un composant React, l'application parente devrait être écrite en React également.
2. **Taille dynamique** — Cette approche est utile si la largeur/hauteur de votre application est dynamique et ne s'adapte pas bien à un cadre de taille statique.
3. **Histoires d'authentification différentes** — Puisque cette approche est essentiellement du HTML réutilisable, les applications que vous souhaitez composer peuvent avoir des histoires d'authentification différentes, ou l'histoire d'authentification peut différer à chaque endroit où le composant est utilisé.
4. **Comportements différents dans chaque cas d'utilisation** — Avec cette approche, vous pouvez réutiliser un front-end, mais appeler différentes API dans chaque cas d'utilisation. Chaque copie du front-end peut fonctionner complètement différemment. Vous pouvez définir différentes props et appeler différentes API dans chaque cas d'utilisation pour adapter le comportement selon les besoins.
5. **Données communes** — Avec cette approche, l'interface utilisateur que vous composez peut utiliser et afficher les données de l'application parente. C'est une application unique et cohésive. Cela évite les appels API dupliqués et les problèmes de désynchronisation, économise de la bande passante et améliore les performances.
6. **Nombreuses interactions inter-applications** — Si il y a des interactions significatives et des données partagées entre les applications, cette approche assure que les deux applications semblent être une expérience unique et cohésive... car **cette approche crée une application unique et cohésive**.
7. **La découvrabilité est souhaitable** — Vous souhaitez publiciser l'existence d'un front-end riche et réutilisable en tant que composant. Vous pouvez placer ce composant dans votre bibliothèque de composants réutilisables et documenter les props qu'il accepte afin que d'autres puissent facilement le trouver et le réutiliser dans différents contextes.
8. **Plusieurs cas d'utilisation** — Vous prévoyez de déployer ce front-end à de nombreux endroits. Cette approche est plus flexible que les autres approches puisque vous partagez simplement un front-end hautement configurable.
9. **Équipes UI et API séparées** — Si vous avez une équipe UI séparée, lier l'UI à l'API via les autres approches est peu attrayant en raison de la surcharge de coordination mentionnée précédemment. Avec cette approche, vous contrôlez quand mettre à jour le package npm. Vous pouvez déployer une nouvelle version du front-end réutilisable lorsque vous le souhaitez, sur une base par application.

# Résumé

Comme toujours, le contexte est roi. Dans la plupart des cas, je recommande l'approche #3, mais chacune a des cas d'utilisation valides. Avez-vous une autre façon de gérer cela ? N'hésitez pas à commenter.

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com/), architecte logiciel chez VinSolutions, un MVP Microsoft, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).