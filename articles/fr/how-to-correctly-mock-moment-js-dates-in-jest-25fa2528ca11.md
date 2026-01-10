---
title: Comment bien simuler Moment.js/dates dans Jest
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T21:50:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-correctly-mock-moment-js-dates-in-jest-25fa2528ca11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W26Jdk8ZEo4QDC797b7smA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Jest
  slug: jest
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Testing
  slug: testing
seo_title: Comment bien simuler Moment.js/dates dans Jest
seo_desc: 'By Iain Nash

  Times and dates are infamously hard to correctly implement in code. This makes testing
  date and time code correctly important. Testing allows for reasoning around logic
  in code and also to allow catching edge cases or errors before they ...'
---

Par Iain Nash

Les heures et les dates [sont notoirement difficiles](https://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time) à implémenter correctement dans le code. Cela rend le test du code de date et d'heure correctement important. Les tests permettent de raisonner autour de la logique dans le code et aussi de permettre de capturer les cas limites ou les erreurs avant qu'ils n'impactent les utilisateurs.

Une erreur courante lors du test du code de date et d'heure est de ne pas définir l'heure actuelle à une heure statique. Si le code dans l'UI rend la date d'aujourd'hui et est testé correctement, ce test ne fonctionne que jusqu'à ce que l'heure actuelle change trop. JavaScript expose l'objet `Date` intégré qui permet de récupérer l'heure actuelle via la construction sans arguments ou un appel à la propriété `now()`.

[Moment.js](https://momentjs.com/) est une bibliothèque populaire de manipulation de dates côté front-end qui est couramment utilisée pour manipuler, charger, formater et décaler le temps. Il utilise un constructeur vide pour obtenir l'heure actuelle. Jest est souvent utilisé en conjunction avec Moment et les applications React. De plus, les tests de snapshot de Jest introduisent de nouvelles dépendances à la date et à l'heure qui sont importantes à considérer. Voici un exemple de composant problématique qui rend le jour actuel :

Un test initial pour le composant `TodayIntro` pourrait ressembler à :

Cependant, ce test échouera n'importe quel jour qui n'est pas le 23 janvier. Une solution à cela est de remplacer la fonction de date de JavaScript pour retourner une date connue à utiliser lors de l'écriture des tests.

Ce code remplace le constructeur Date pour définir une date "actuelle" statique :

Une solution inefficace est de faire soi-même les calculs de date par rapport à l'heure actuelle à laquelle le test est exécuté. Ce n'est pas un test efficace car vous exécutez le même code que vous testez pour tester la valeur de retour. Par exemple, si vous testez en comparant les dates formatées via moment, vous ne remarquerez pas si le code de formatage de moment change `MMM` en `JAN` au lieu de `Jan`.

#### Façons de définir une heure et un fuseau horaire statiques pour Jest/JS

1. Utiliser une bibliothèque pour simuler l'objet Date afin de retourner une date et un fuseau horaire statiques (nous recommandons [MockDate](https://github.com/boblauer/MockDate) pour les cas simples, mais lisez la suite pour une analyse des alternatives)
2. Simuler `moment().format()` pour retourner une chaîne statique
3. Simuler le constructeur `Date` et la fonction `now()` pour retourner une heure statique

L'utilisation d'une bibliothèque dans ce cas est préférable car ces bibliothèques sont bien testées, n'introduisent pas de code boilerplate et gèrent de manière transparente les deux cas où les dates peuvent être créées (`Date.now()` vs `new Date()` etc.). De plus, l'utilisation d'une bibliothèque permet de suivre facilement le code de test et de définir une heure spécifique par test, ce qui permet de meilleures pratiques de test.

* `[MockDate](https://github.com/boblauer/MockDate)` fournit des fonctionnalités supplémentaires pour les fuseaux horaires et est facile à utiliser
* `[sinon](https://sinonjs.org/releases/v7.2.4/fake-timers/)` fournit des simulations de Date et de minuterie (`setTimeout` etc.)
* La définition manuelle de la simulation peut être utile dans des environnements limités, cependant, cela peut devenir plutôt compliqué
* `[jasmine](https://jasmine.github.io/)` (non inclus dans jest), vient avec un [jasmine.clock()](https://jasmine.github.io/api/2.6/Clock.html)

Les exemples ci-dessous utilisent [MockDate](https://github.com/boblauer/MockDate), qui se concentre uniquement sur la simulation de l'objet Date simplement et gère également les décalages de fuseau horaire pour les tests de conversion de fuseau horaire local.

Un [test de snapshot](https://jestjs.io/docs/en/snapshot-testing), ainsi, est simple à tester avec des dates simulées :

Puisque [enzyme](https://airbnb.io/enzyme/) est une bibliothèque géniale, un exemple de shallow d'enzyme :

### Comment (mieux) tester la logique des dates

Les dates ont beaucoup de cas limites et de logique derrière elles. Lors du test des dates, assurez-vous de couvrir les cas limites et ne vous contentez pas de définir une date spécifique à tester et passez à autre chose. Les dates peuvent également varier selon la locale et le fuseau horaire.

Tester correctement les dates nécessite de raisonner autour des cas limites qui pourraient se produire et d'écrire des tests pour s'assurer que ces cas limites se comportent comme prévu et que les modifications futures du code ou des bibliothèques utilisées dans votre application ne brisent pas ces hypothèses. De plus, ajouter du code pour définir la date et l'heure actuelles à une date et une heure statiques dans tout le code de test peut être plus facile, mais empêche un bon raisonnement autour des tests de Dates et cache les hypothèses de test dans le code de la bibliothèque.

Voici quelques hypothèses incorrectes et souvent implicites sur les dates :

1. Tous les clients existent dans un seul fuseau horaire et une heure d'été
2. Tous les clients existent dans le fuseau horaire du développeur
3. La longueur d'un nom de mois est relativement similaire
4. Les horloges des serveurs sont toujours correctes
5. Le serveur connaît le fuseau horaire/les paramètres d'heure du client

Ce test suppose que le serveur est toujours dans le bon fuseau horaire et que le fuseau horaire est défini correctement. Au lieu de cela, définissez le fuseau horaire et assurez-vous que la date correspond correctement au fuseau horaire local.

Il est important de s'assurer que lorsque les tests accèdent à l'heure actuelle, l'heure "actuelle" est définie sur une valeur statique. Si la valeur est dynamique, soit les tests finissent par échouer, soit un test est testé contre des valeurs dynamiques. Les valeurs dynamiques ne sont pas efficaces pour tester le comportement puisque un bug ne sera pas exposé en comparant la valeur de retour de deux fonctions qui sont les mêmes par rapport à la comparaison avec une valeur statique qui ne change pas lorsque le code est modifié.

### Perspectives d'avenir : Stockage et conception de la date et de l'heure

Avoir une exigence d'ajouter des tests à une base de code ne fournit pas nécessairement de valeur à moins que ces tests ne soient examinés, exécutés et raisonnés aussi strictement que le code en cours d'exécution.

La logique de date et d'heure introduit un grand ensemble de possibilités en termes de comportement et de sortie, ce qui constitue une forte incitation à tester efficacement pour la date et l'heure. Au-delà des tests, la reconnaissance et la conservation des données pertinentes ainsi qu'une stratégie pour synchroniser et stocker les dates et heures de manière cohérente à travers les systèmes dès le début aident les tests et améliorent l'expérience utilisateur.

Ces conseils et approches s'appliquent à plus que simplement les tests JavaScript & Jest pour les dates et les heures. Ils fonctionnent également dans un contexte NodeJS et dans un sens général autour des choses clés à tester dans les systèmes qui gèrent la date et l'heure en général. Dans de nombreux cas, stocker l'heure sur le serveur en UTC (temps universel coordonné) puis convertir en fuseau horaire local basé sur les paramètres du client/navigateur est idéal. Si le client est inaccessible, stocker à la fois l'heure UTC et le fuseau horaire réel de l'utilisateur est un moyen efficace de traiter de manière cohérente les dates et les heures.