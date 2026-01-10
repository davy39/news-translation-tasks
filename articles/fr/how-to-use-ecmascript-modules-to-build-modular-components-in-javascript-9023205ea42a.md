---
title: Comment utiliser les modules ECMAScript pour créer des composants modulaires
  en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T19:36:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-ecmascript-modules-to-build-modular-components-in-javascript-9023205ea42a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7O9pHIC30rAhpdrbaPrTWw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les modules ECMAScript pour créer des composants modulaires
  en JavaScript
seo_desc: 'By Said Hayani

  JavaScript modules are now supported by the browser. This means you can use this
  great addition in JavaScript, introduced by ECMAScript 2015, in the browser. Previously,
  you had to use a bundler such as a webpack in order to use module...'
---

Par Said Hayani

Les modules [JavaScript](https://www.zeolearn.com/javascript-training) sont désormais pris en charge par le navigateur. Cela signifie que vous pouvez utiliser cette excellente fonctionnalité en JavaScript, introduite par ECMAScript 2015, dans le navigateur. Auparavant, vous deviez utiliser un bundler tel que [webpack](https://www.zeolearn.com/magazine/beginning-with-webpack-4) pour utiliser les modules. Mais ce n'est plus nécessaire. N'est-ce pas génial !

Ainsi, dans cet article, nous allons explorer les modules JavaScript et voir comment nous pouvons les utiliser dans notre application web.

### Qu'est-ce que les modules JavaScript et pourquoi les utiliser au lieu d'un script classique ?

Les modules JavaScript nous permettent essentiellement d'importer un fichier dans un autre fichier en utilisant les méthodes import et export. Ils nous permettent également de créer des composants modulaires qui peuvent être réutilisables.

#### Pourquoi utiliser les modules JavaScript ?

Il y a de nombreux avantages à utiliser les modules JavaScript dans votre application au lieu d'un script classique :

* **Séparer votre application en modules** : Construire votre application avec des modules la rend plus efficace et améliore les performances de votre code. En utilisant ces modules, vous pouvez charger paresseusement votre code et n'utiliser que le code dont vous avez besoin, évitant ainsi le code inutilisé.
* **Utilisation du mode Strict par défaut** : Oui, le mode strict est activé par défaut dans les modules JavaScript.
* **La méthode defer est utilisée par défaut**
* Cela signifie que **votre code [HTML](https://www.zeolearn.com/magazine/material-design-tooltip-with-css-html) est chargé en parallèle avec JavaScript**. Vous n'avez donc plus besoin d'ajouter l'attribut defer à votre balise script lorsque vous utilisez ECMAScript.
* **Il importe vos modules dynamiquement**
* Avec les modules JavaScript, vous pouvez **personnaliser le chargement de vos modules** en exécutant une fonction dynamique qui importe un module uniquement si vous en avez besoin. Cela suppose que lorsque l'utilisateur visite votre site web, vous devez charger uniquement le module qui gère le profil, au cas où l'utilisateur se connecterait. Cela est clairement expliqué dans l'exemple ci-dessous :

`usermodule.js`

![Image](https://cdn-media-1.freecodecamp.org/images/1*BBSJbj100sGSvDf_QtSZLQ.png)

`profile.js`

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZMJhiekLpIo6CNUzwbo7mg.png)

### Comment utiliser les modules

Maintenant, dans cette partie, nous allons explorer les différentes façons d'utiliser les modules JavaScript. Vous pouvez [utiliser facilement un module JavaScript](https://www.zeolearn.com/magazine/learn-javascript-from-scratch-tutorials) en spécifiant l'attribut type à module dans la balise script qui implémente votre fichier JavaScript principal. Maintenant, vous pouvez utiliser les méthodes import et export pour importer vos modules.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oGuFFmwMqRp_UFui2o4nvg.png)

Et à l'intérieur de votre `main.js`, vous pouvez importer et exporter vos modules :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hzQ-Yhnz6BPpjNB7c6JSXA.png)

Utilisation de la méthode **export** dans `profile.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DS0f7mgYekI2QxlYbSZV9g.png)

Comme le montre l'exemple ci-dessus, il est facile d'utiliser les modules ECMAScript — il n'y a pas de code complexe dans ce cas.

Lorsque vous définissez le type dans le module, le navigateur détecte automatiquement que le fichier est un module et le traite comme un module JavaScript.

D'une autre manière, vous pouvez définir l'extension `.mjs` au fichier afin que le navigateur puisse identifier le module. Mais cela ne fait pas de grands changements si vous définissez l'attribut type comme module dans la balise script.

### Support des navigateurs

![Image](https://cdn-media-1.freecodecamp.org/images/1*C-JPouX9w-nzK25EBHZpeQ.png)

Il semble que seuls les navigateurs modernes supportent les modules JavaScript. Mais ce n'est pas grave si vous utilisez de grands navigateurs comme Chrome, Edge et Firefox.

#### Je n'ai plus besoin d'utiliser des bundlers ?

[Addy Osmani](https://twitter.com/addyosmani) et [Mathias Bynens](https://twitter.com/mathias) expliquent dans cet [article](https://developers.google.com/web/fundamentals/primers/modules?utm_source=ESnextNews.com&utm_medium=Weekly+Newsletter&utm_campaign=2018-06-19) que vous n'avez probablement pas besoin d'un bundler web tel que webpack si vous développez une application web avec moins de 100 modules. Vous pouvez consulter l'article où ils ont exposé les meilleures pratiques et le bon usage des modules ECMAScript [ici](https://developers.google.com/web/fundamentals/primers/modules?utm_source=ESnextNews.com&utm_medium=Weekly+Newsletter&utm_campaign=2018-06-19).

Retrouvez le code dans le dépôt GitHub [ici](https://github.com/hayanisaid/JavaScript-modules-in-browser).

### Conclusion

Les modules JavaScript sont un excellent moyen d'augmenter les performances de votre application. Ils vous permettent de faire de nombreuses choses qui rendent votre application plus performante, comme le chargement dynamique de vos modules, le chargement paresseux, et plus encore. De plus, la grande chose est qu'ils sont pris en charge par le navigateur. Donc, n'hésitez pas à en profiter si vous n'utilisez pas de bundler de fichiers.

_Publié à l'origine sur [Zeolearn](https://www.zeolearn.com/magazine/javascript-modules-are-now-supported-by-the-browsers)_

[_Rejoignez ma classe pour apprendre Bootstrap sur Skill Share_](https://skl.sh/2OZZhxs)

**_Articles précédents :_**

* [JavaScript ES6 — Écrire moins, faire plus](https://medium.freecodecamp.org/write-less-do-more-with-javascript-es6-5fd4a8e50ee2)
* [Apprendre Bootstrap 4 en 30 minutes en créant une page de destination](https://medium.freecodecamp.org/learn-bootstrap-4-in-30-minute-by-building-a-landing-page-website-guide-for-beginners-f64e03833f33)
* [Angular 6 et ses nouvelles fonctionnalités, tout expliqué en trois minutes](https://medium.freecodecamp.org/angular-what-is-the-new-briefly-e6837348dd3a)
* [Comment utiliser le routage dans Vue.js pour créer une meilleure expérience utilisateur](https://medium.freecodecamp.org/how-to-use-routing-in-vue-js-to-create-a-better-user-experience-98d225bbcdd9)
* [Voici les méthodes les plus populaires pour faire une requête HTTP en JavaScript](https://medium.freecodecamp.org/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa)
* [Apprenez à créer votre première application Angular en 20 minutes](https://medium.freecodecamp.org/learn-how-to-create-your-first-angular-app-in-20-min-146201d9b5a7)