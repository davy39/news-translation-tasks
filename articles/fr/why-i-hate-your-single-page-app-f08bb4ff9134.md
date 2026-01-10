---
title: Pourquoi je déteste votre Single Page App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-13T19:33:51.000Z'
originalURL: https://freecodecamp.org/news/why-i-hate-your-single-page-app-f08bb4ff9134
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb965740569d1a4caf1ec.jpg
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Pourquoi je déteste votre Single Page App
seo_desc: 'By Stefan Tilkov

  Okay, now that I have your attention, let me say that I don’t really hate your single
  page app. I just find it highly annoying, unless it is one of the very, very few
  exceptional cases that actually merit being developed in this styl...'
---

Par Stefan Tilkov

D'accord, maintenant que j'ai votre attention, laissez-moi dire que je ne déteste pas vraiment votre single page app. Je la trouve simplement très agaçante, sauf si elle fait partie des très rares cas exceptionnels qui méritent vraiment d'être développés de cette manière. Comme ceux-ci sont rares, il est raisonnable de supposer que la vôtre ne qualifie pas.

Peut-être que votre single page app est différente, mais celles que je connais brisent la plupart des fonctionnalités de mon navigateur, comme les boutons de retour et d'avance, le rafraîchissement de la page, les favoris, l'envoi d'un lien, ou l'ouverture d'un lien dans une nouvelle fenêtre ou un nouvel onglet. Elles n'offrent aucun moyen de lier à quelque chose que je regarde. (Oh, je sais qu'il y a des exceptions à cette règle, mais elles nécessitent généralement des efforts — bien plus que ce que beaucoup de développeurs sont prêts à investir). Elles sont gonflées et lentes à charger, même si les informations qu'elles affichent et les interactions qu'elles offrent sont très simples.

Suis-je juste un vieux grincheux ? Oui, mais ce n'est pas le sujet. Mon point est que, d'un point de vue architectural, la plupart des single page apps sont le résultat de mauvais choix et de l'omission d'opportunités importantes.

Mon principal problème avec les single page apps, ou SPA en abrégé, est qu'elles ne sont pas "sur le web". À cet égard, elles sont très similaires à un service web SOAP. Elles ont une URI, mais seulement pour l'ensemble, pas pour toutes ces choses précieuses qui sont à l'intérieur. (Encore une fois, je sais que vous pouvez construire votre SPA différemment, mais la plupart des gens ne le font pas.) Je crois que si vous construisez une application web, elle devrait avoir une interface utilisateur web qui mérite ce nom, de la même manière qu'un service web devrait avoir quelque chose à voir avec le web.

Si tout cela vous semble très abstrait, pensez à ce qui fait du web le web. La caractéristique la plus importante du web est que vous pouvez lier des choses individuelles. Chaque concept important au sein de votre application devrait être un point d'entrée possible. Cela permet à n'importe qui, n'importe où, de l'utiliser comme cible d'un lien. Le fait qu'un utilisateur puisse avancer et reculer dans l'historique des choses qu'il a visitées n'est pas un bug, c'est une fonctionnalité essentielle. Il est crucial que chacune de ces cibles retourne une réponse rapidement, car tout surcoût que vous créez devra être payé plusieurs fois. Les boutons de retour et d'avance ne sont pas censés naviguer entre les applications.

Je peux presque vous entendre dire : "Mais je ne me soucie pas du web. Je construis une application, pas un site web." À quoi je réponds : Allez-y alors, construisez une application, en utilisant le kit de développement natif de votre système d'exploitation de bureau ou mobile, ou construisez une applet, ou une application Flash ou Silverlight. Cela me convient parfaitement. Je n'ai même pas d'objection à ce que vous construisiez la même chose en utilisant le navigateur comme environnement d'exécution d'application. Soyez simplement conscient que lorsque vous faites les choses de cette manière, votre application est sur le web autant que si vous l'aviez construite comme une applet Java. Soyez conscient de ce que vous sacrifiez.

C'est là que, selon moi, les mauvais choix des gens interviennent. Il semble que pour beaucoup de gens, construire une SPA est devenu synonyme de construire une application web moderne. Toute personne qui critique cette approche architecturale n'a évidemment pas fait le pas vers le monde moderne. Je ne pourrais pas être plus en désaccord. Les gens choisissent une SPA sans être conscients des inconvénients, y compris des choses comme des frameworks qui sortent de la maintenance, une complexité presque ingérable dans le code côté client, ainsi que des problèmes de performance et d'accessibilité.

Mais plus important encore, ils passent à côté des avantages de ne pas choisir une SPA. Ils ne sont pas conscients des avantages de l'alternative. Quelle est cette alternative, alors ? C'est de construire une application web classique, y compris le rendu côté serveur de HTML, et d'utiliser JavaScript uniquement avec parcimonie, pour améliorer les fonctionnalités du navigateur lorsque cela est possible. Dans cette approche architecturale, il est absolument clair que la responsabilité de la logique métier réelle réside complètement sur le serveur. Cela inclut la machine à états côté serveur qui régit les transitions entre les pages. Et encore une fois, ce n'est pas un bug, mais une fonctionnalité : c'est ce qui permet à un changement rapide côté serveur de prendre effet immédiatement, partout — y compris les autres types de clients que vous pourriez finir par construire en plus de votre interface utilisateur web. La logique métier ne appartient pas au client, sauf si vous aimez devoir maintenir de manière redondante la même logique dans chaque type de client que vous supportez (en plus de la maintenir sur le serveur, bien sûr — rappelez-vous que vous ne pouvez jamais faire confiance à un client). D'un point de vue côté serveur, la meilleure architecture que vous pouvez avoir est celle que vous auriez pu (et dû) construire il y a une décennie : en suivant les principes REST, y compris la communication sans état et l'identification des ressources.

Certaines personnes s'opposent à cela parce qu'elles croient que les SPA offrent une meilleure architecture. Je ne suis pas d'accord : avec une SPA, votre architecture est typiquement celle suggérée par votre framework parce que, d'un point de vue web, votre SPA est une seule chose qui concerne le web. Avec une approche non-SPA (que je vais appeler [ROCA](http://roca-style.org) à partir de maintenant), l'architecture qui régit vos applications est celle du web lui-même. Encore une fois, le fait que votre serveur prenne en charge la tâche ennuyeuse de rendre le HTML est un atout, pas un fardeau. Pour ma part, je n'ai pas beaucoup de confiance dans la stabilité et la maintenabilité à long terme de l'un des frameworks JavaScript côté client actuellement existants.

Un exemple fantastique des problèmes créés par l'approche SPA est la parallélisation du travail. Si vous avez une équipe de plusieurs personnes, ou pire, plusieurs équipes travaillant sur la même SPA, vous devez trouver un bon moyen de supporter cela. Au lieu de cela, vous pouvez simplement avoir chacune de ces équipes construire sa propre application web. Chacune de ces applications peut être connectée à toutes les autres construites en même temps par la même organisation (ainsi qu'à toutes les autres applications web résidant ailleurs, si vous le souhaitez) — en fait, en s'appuyant sur la force centrale du web.

En termes d'accessibilité, le rendu de HTML sémantique côté serveur fournit un support prêt à l'emploi. Il n'y a qu'un ensemble limité de choses que vous pouvez faire avec HTML, et encore une fois, c'est une fonctionnalité, pas un bug.

Vous pouvez aborder certains de ces problèmes au sein d'une SPA, aussi. Mais cela prend des efforts. Avec l'approche ROCA, vous avez une architecture bien connue, extrêmement mature et éprouvée sur laquelle vous appuyer.

Bien sûr, cela ne suggère pas du tout que vous n'utilisez pas JavaScript et Ajax. Je suis parfaitement conscient que vous ne pouvez pas construire une interface utilisateur moderne sans JavaScript pour permettre certaines modifications dans la page. Mais cela est une amélioration optionnelle, pas le facteur déterminant de votre architecture. (Même d'un point de vue REST, l'utilisation de JavaScript est parfaitement acceptable : elle est en fait mentionnée comme une contrainte optionnelle dans la dissertation REST sous le nom de "code on demand". Mais son but est de servir de moyen pour étendre le navigateur afin de supporter du contenu qu'il ne supporte pas nativement.) Dans presque tous les cas dont je suis conscient, votre SPA n'a aucun avantage pour l'utilisateur, et il n'y a que des côtés positifs à adopter les fonctionnalités du navigateur à la place. Vous pourriez croire qu'il y a des avantages pour le développeur, mais tout d'abord, vous devriez mettre ceux-ci derrière l'intérêt de l'utilisateur, et deuxièmement, ils sont surtout imaginaires, surtout à long terme.

Alors construisez vos SPA, cela ne me dérange pas, tant que je n'ai pas à les utiliser. Soyez simplement conscient de ce que vous abandonnez.