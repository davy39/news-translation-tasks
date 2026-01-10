---
title: Comment coder un site d'actualités en tant qu'application web progressive
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-15T19:06:46.000Z'
originalURL: https://freecodecamp.org/news/coding-a-newspaper-as-a-freakin-progressive-web-app-e456d4a2b9cd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UIn33AVqRy28zwx7SIojaw.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment coder un site d'actualités en tant qu'application web progressive
seo_desc: 'By James Y Rauhut

  For the last two weeks, I worked on a personal project called The Global Upvote.
  The Global Upvote aggregates top voted stories from across the web, summarized and
  updated every sixty seconds.

  This article focuses on how I was able ...'
---

Par James Y Rauhut

Pendant les deux dernières semaines, j'ai travaillé sur un projet personnel appelé The Global Upvote. The Global Upvote agrège les histoires les plus votées sur le web, résumées et mises à jour toutes les soixante secondes.

Cet article se concentre sur la manière dont j'ai pu implémenter The Global Upvote pour les développeurs en herbe. J'ai écrit un article séparé sur le [processus de design derrière cela](https://medium.com/@seejamescode/designing-a-newspaper-as-a-freakin-progressive-web-app-22acf4eb5a68). Ces deux histoires peuvent sembler complètement séparées. Mais le processus de design et de développement était profondément entrelacé dans la vie réelle.

Notez que j'ai écrit un article complémentaire sur la façon de concevoir ce site d'actualités en tant qu'application web progressive [ici](https://medium.freecodecamp.org/designing-a-newspaper-as-a-freakin-progressive-web-app-22acf4eb5a68).

### Trouver les données

En design, il y a un concept de "content-first". Le Content-First Design dit que vous devez concevoir autour du contenu. Pour cela, je devais m'assurer de pouvoir récupérer les bonnes données. Avant de commencer tout travail réel sur le front-end, j'ai travaillé avec l'API Reddit et mon serveur Node.

Je savais qu'il y avait deux parties de contenu que je voulais capturer depuis Reddit :

1. Les meilleurs posts de r/WorldNews pour leurs titres
2. Un commentaire d'un bot utilisateur qui résumait l'histoire

![Image](https://cdn-media-1.freecodecamp.org/images/D47NNgQ3LaXnrwje5PulcM2QJQzP4nl598z3)
_Ces objets étaient de délicieuses données Reddit._

Heureusement, il y avait un excellent wrapper Node pour l'API appelé [Snoowrap](https://github.com/not-an-aardvark/snoowrap). Il était facile à utiliser et m'a permis de [récupérer du contenu](https://github.com/seejamescode/global-upvote/blob/master/server.js#L33-L92) en un rien de temps.

Une grande chose que j'ai apprise sur ce projet était la gestion des requêtes. Dans le passé, j'avais utilisé mon serveur Node comme un demandeur d'API chaque fois qu'un utilisateur visitait mon application. Mais j'ai eu une épiphanie évidente.

Je pouvais conserver la petite quantité de données (histoires) sur mon serveur et les mettre à jour une fois par minute avec un simple `setInterval`. Cela a stoppé le risque d'abuser des limites de mon API Reddit et a raccourci les temps de chargement des histoires car je n'aurais pas à interagir avec l'API Reddit à chaque fois.

### Garder le caractère progressif

Vous voulez connaître le secret bon marché et sale pour créer une application web progressive en React ? Utilisez simplement [Create-React-App](https://github.com/facebookincubator/create-react-app). Les contributeurs de ce projet ont fait un travail merveilleux en ajoutant des service workers pour des chargements quasi instantanés et un fichier manifest pour vos métadonnées, et en optimisant le bundling Webpack du mieux qu'ils peuvent. Dans le passé, j'ai dû faire beaucoup de travail pour les PWAs (Progressive Web Apps) et j'ai même écrit un [tutoriel](https://medium.freecodecamp.org/how-to-crank-your-progressive-web-apps-google-lighthouse-score-up-to-100-cfc053eb7661) sur la façon de les perfectionner.

C'était la première fois que je travaillais sur un mode hors ligne pour Chrome et Firefox pour faire des choses comme lire des articles avant que mon ordinateur ne se connecte au wifi.

La première moitié consistait à faire des choses chaque fois que la [connexion internet](https://github.com/seejamescode/global-upvote/blob/master/src/App.js#L156-L157) changeait en utilisant des écouteurs d'événements. Ainsi, une nouvelle connexion à internet pouvait déclencher la récupération des histoires, et une connexion perdue pouvait notifier l'utilisateur qu'il est hors ligne.

La seconde moitié du mode hors ligne consistait à sauvegarder les nouvelles histoires sur l'appareil de l'utilisateur chaque fois qu'elles étaient récupérées. C'était ma première fois en utilisant [LocalStorage](https://github.com/seejamescode/global-upvote/blob/master/src/App.js#L192-L194), et j'ai été agréablement surpris par la facilité avec laquelle cela se faisait.

![Image](https://cdn-media-1.freecodecamp.org/images/rJs8r6M4IuHi4L3RVeiOo98f6LFglv6tjw6Y)

Un dernier détail de la PWA à finaliser était l'amélioration de l'indice de vitesse perceptuelle. Vous pouvez voir cette métrique centrée sur l'utilisateur en ouvrant Chrome DevTools et en exécutant un [audit](https://medium.com/design-ibm/the-quick-new-way-designers-can-test-user-centric-metrics-37e78daf48df). Pour améliorer ce score, j'ai créé des squelettes qui apparaissaient lorsque l'état de mon application était en [récupération](https://github.com/seejamescode/global-upvote/blob/master/src/Placeholder.js#L8).

### Utiliser un plugin

J'avais déterminé que je voulais que l'utilisateur puisse enregistrer l'expérience comme leur nouvel onglet pour Chrome et Firefox. Les navigateurs supportent nativement la définition d'une page d'accueil. Mais cela ne vous donne pas le contrôle de la barre d'URL immédiatement. C'était un détail important car un utilisateur ne veut pas avoir à cliquer sur la barre d'URL chaque fois qu'il ouvre un nouvel onglet.

![Image](https://cdn-media-1.freecodecamp.org/images/-hOZgtc9wGhISJgIVQhgAYJsCZq8naTqKZMd)

Je craignais de devoir plonger dans le développement d'extensions de navigateur. C'était quelque chose que je ne connaissais pas, à part un vérificateur de grille pour aider mes compétences visuelles. Une fois de plus, cette solution s'est avérée être livrée sur un plateau d'argent. Google inclut une extension similaire dans leurs [téléchargements d'exemples](https://developer.chrome.com/extensions/samples). J'ai travaillé en un rien de temps avec l'[Extension d'onglet Global Upvote](https://github.com/seejamescode/global-upvote-tab). Aucun changement n'a même été nécessaire pour la soumission au magasin de Firefox !

### Le résultat final

D'un point de vue développement, j'ai adoré toutes les différentes solutions que j'ai pu mettre en place pour [The Global Upvote](https://www.globalupvote.com/). Ces solutions me disent que la communauté web s'améliore pour travailler ensemble afin de rendre l'expérience de développement moins frustrante. Obtenir un score parfait dans l'audit Chrome DevTools, anciennement l'extension Google Lighthouse, est également devenu plus facile que jamais.

![Image](https://cdn-media-1.freecodecamp.org/images/zntcHCafx0kyMI3lfg5cenMGFu4hyBEoGQ32)

[Tout le code source](https://github.com/seejamescode/global-upvote) a été open-sourcé au cas où vous voudriez fouiller ou le faire fonctionner pour vous.

Plusieurs choses rapides à noter :

* Où sont les fichiers CSS ?!
Il n'y en a pas. J'utilise [Styled Components](https://www.styled-components.com/) pour attacher les styles directement à leur composant !

Consultez cette conférence que j'ai donnée chez IBM sur pourquoi le CSS-in-JS est incroyablement bon : [https://vimeo.com/230614037](https://vimeo.com/230614037)
* Où est le code source de votre extension d'onglet ?
Consultez-le dans le dépôt séparé pour [Global Upvote Tab](https://github.com/seejamescode/global-upvote-tab).
* Comment puis-je commencer à exécuter cela localement ?
Consultez la documentation pour [Create-React-App](https://github.com/facebookincubator/create-react-app#getting-started) si vous ne l'avez pas déjà fait.

Beaucoup de wow. Vous avez également besoin d'un fichier appelé `keys.json` dans le répertoire racine avec vos informations pour [Snoowrap](https://github.com/not-an-aardvark/snoowrap). Il devrait ressembler à ceci :

```json
{
  "userAgent": "random-term",
  "clientId": "FromYourRedditAPISettings",
  "clientSecret": "FromYourRedditAPISettings",
  "username": "YourRedditUsername",
  "password": "YourRedditPassword"
}
```

J'espère que vous avez apprécié ce compte rendu de cas !

Encore une fois, j'ai écrit un article complémentaire sur la façon de concevoir ce site d'actualités en tant qu'application web progressive [ici](https://medium.freecodecamp.org/designing-a-newspaper-as-a-freakin-progressive-web-app-22acf4eb5a68).

Pour plus d'informations : N'hésitez pas à me contacter via les commentaires, [email](mailto:james@seejamescode.com), ou [@seejamescode](https://twitter.com/seejamescode). Je travaille à ATX pour IBM Design et j'adore toujours discuter avec la communauté du design web. Laissez toutes les questions que vous pourriez avoir et j'essaierai d'y répondre pour vous !