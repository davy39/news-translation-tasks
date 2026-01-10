---
title: Après avoir construit ma première application React Native, je suis maintenant
  convaincu que c'est l'avenir.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-11T21:01:19.000Z'
originalURL: https://freecodecamp.org/news/after-building-my-first-react-native-app-im-now-convinced-it-s-the-future-d3c5e74f8fa8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FAZF7OhcN7P53L32co7NDw.png
tags:
- name: JavaScript
  slug: javascript
- name: mobile
  slug: mobile
- name: mobile app development
  slug: mobile-app-development
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Après avoir construit ma première application React Native, je suis maintenant
  convaincu que c'est l'avenir.
seo_desc: 'By Taylor Milliman

  After a few weeks of playing around with React Native, I just came away with my
  first real mobile app. It’s fairly simple, but it only took me a few days to build
  and I had a blast doing it.

  I created a mobile app for my favorite f...'
---

Par Taylor Milliman

Après quelques semaines à jouer avec React Native, je viens de terminer ma première vraie application mobile. Elle est assez simple, mais il ne m'a fallu que quelques jours pour la construire et je me suis beaucoup amusé à le faire.

J'ai créé une application mobile pour mon blog culinaire préféré, [Smitten Kitchen](https://smittenkitchen.com/).

L'application permet aux utilisateurs de rechercher dans une base de données de plus de 1 000 recettes, et d'afficher de manière concise les ingrédients nécessaires et les instructions pour chacune d'entre elles.

Les utilisateurs peuvent également marquer des recettes et les partager facilement avec un ami.

J'attends toujours la permission du blog pour publier cette application, mais vous pouvez consulter tout le code [ici](https://github.com/twmilli/smitten-kitchen). Notez que l'URL de mon API a été désactivée pour le moment par respect pour Smitten Kitchen.

### React Native n'est pas prêt de disparaître

Une réserve courante parmi les développeurs est qu'ils ne veulent pas investir du temps pour apprendre une nouvelle technologie s'il y a une forte chance qu'elle devienne obsolète dans un avenir proche.

Même avec mon expérience relativement limitée avec React Native, je l'ai trouvé être un outil extrêmement puissant. Je suis convaincu qu'il sera utilisé dans les années à venir.

Facebook, Instagram et Airbnb ont tous construit les dernières versions de leurs applications mobiles en utilisant React Native. Et voici une [liste](https://facebook.github.io/react-native/showcase.html) de certaines autres applications populaires qui ont été construites avec.

[Jeff Meyerson](https://www.freecodecamp.org/news/after-building-my-first-react-native-app-im-now-convinced-it-s-the-future-d3c5e74f8fa8/undefined), créateur du podcast [Software Engineering Daily](https://softwareengineeringdaily.com/2017/04/11/the-future-of-react-native-with-brent-vatne-and-adam-perry/), a beaucoup parlé de la plateforme React Native. Il croit qu'elle survivra et continuera à capturer la majorité de l'écosystème mobile.

Il a même spéculé que Facebook pourrait créer son propre téléphone mobile, qui serait construit spécifiquement pour supporter les applications faites avec React Native.

### Comment React Native est différent des autres outils cross-platform

Si vous êtes nouveau dans [React Native](https://facebook.github.io/react-native/releases/next/), c'est un projet open source lancé par Facebook. Il permet aux développeurs de construire des applications mobiles cross-platform en utilisant JavaScript. Il fonctionne très similaire à React, la bibliothèque JavaScript populaire de Facebook pour construire des applications web single page.

J'ai toujours été sceptique quant aux outils qui se présentent comme cross-platform pour le mobile. Trop souvent, on obtient un look, une sensation et des performances qui ne correspondent pas tout à fait à la plateforme native.

React Native n'est pas comme les autres frameworks de développement d'applications mobiles, tels que Ionic ou Cordova. Ceux-ci s'exécutent à l'intérieur d'une vue web, ou d'une "application HTML5", ou d'une "application hybride".

Vous construisez une application mobile haute performance qui est indiscernable de celle construite en utilisant Swift/Objective-C ou Java.

Cela dit, il est toujours important de comprendre les intricacies et les différences entre les plateformes. L'expérience utilisateur pour Android et iOS sont fondamentalement différentes, et vous devez toujours construire votre application de manière à ce qu'elle soit naturelle sur les deux plateformes.

De plus, si jamais il y a une fonctionnalité que vous devez ajouter qui n'est pas encore supportée par la bibliothèque React Native, React Native facilite l'écriture de votre propre [Native Module](https://facebook.github.io/react-native/docs/native-modules-ios.html) dans le langage correspondant, qui peut ensuite être lié à votre base de code React Native.

### Comment commencer

Personnellement, j'ai utilisé [ce cours Udemy](https://www.udemy.com/the-complete-react-native-and-redux-course/learn/v4/overview) pour commencer. Il a servi de bon rappel sur React et Redux, et a été utile pour la configuration.

Et récemment, Facebook a publié [Create React Native App](https://facebook.github.io/react-native/blog/2017/03/13/introducing-create-react-native-app.html). Cet outil simplifie encore davantage le processus de configuration initiale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n7zU2gvP181GNJZWMG6hlg.png)
_En train de travailler sur le cours Udemy_

Si vous êtes déjà familier avec React, vous pouvez probablement plonger directement dans la [documentation](https://facebook.github.io/react-native/docs/getting-started.html). Pour seulement 10 $, cependant, le cours est une aubaine et vous guide à travers le processus de création de quatre applications mobiles ainsi que des composants communs que vous pouvez réutiliser dans de futurs projets.

Udemy propose également un cours couvrant les [Concepts Avancés de React Native](https://www.udemy.com/react-native-advanced/), pour ceux qui sont déjà familiers avec la plateforme.

### Styling dans React Native

Le styling dans React Native prend un peu de temps pour s'y habituer. React Native utilise largement CSS flexbox, quelque chose avec lequel je n'étais pas particulièrement à l'aise, même venant d'un background web.

Heureusement, il existe déjà quelques ressources fantastiques pour apprendre flexbox :

[Comment fonctionne flexbox — expliqué avec de grands, colorés, gifs animés](https://medium.freecodecamp.com/an-animated-guide-to-flexbox-d280cf6afc35)

[Exemples de mise en page React Native](http://browniefed.com/blog/react-native-layout-examples/)

Un jeu amusant pour vous aider à pratiquer : [Flexbox Froggy](http://flexboxfroggy.com/)

Après avoir travaillé avec React Native pendant quelques semaines, j'ai maintenant une bien meilleure compréhension de flexbox, que je peux appliquer à mon prochain projet web.

La meilleure pratique actuelle est de créer un objet de styles pour chaque composant, puis de l'appliquer via des styles en ligne. Gardez à l'esprit que vous n'écrivez pas réellement de CSS, donc la nomination des propriétés est également un peu différente.

Une autre différence clé est que vous ne pouvez pas utiliser de balises HTML dans votre JavaScript, car vous écrivez du code pour qu'il s'exécute sur un téléphone, plutôt que dans un navigateur. Au lieu de cela, les composants sont construits avec un ensemble de composants de base fournis par la bibliothèque React Native.

Cela prend un peu de temps pour s'y habituer, mais avant que vous ne le sachiez, vous vous retrouverez à utiliser accidentellement une balise `<View></View>` à la place d'une balise `<div></div>` dans votre prochaine application web.

Pour mieux comprendre comment tout cela fonctionne, jetez un coup d'œil au code d'un simple composant de bouton ci-dessous.

Voici le [GitHub gist](https://gist.github.com/twmilli/5d2bace1faa1d04b1d4b5217c553a671#file-button-js).

### Navigation

La navigation est l'un des rares domaines de React Native où il n'y a pas de consensus sur une solution claire.

React Router est devenu la bibliothèque standard de choix pour la communauté React, mais il existe un certain nombre de bibliothèques qui circulent dans la communauté React Native.

Personnellement, j'ai utilisé la bibliothèque [React Native Router Flux](https://github.com/aksonov/react-native-router-flux) pour mon projet, ce qui a très bien fonctionné. Mais je peux voir comment vous pourriez rencontrer des problèmes plus importants sur des projets plus complexes.

Heureusement, React Native a déjà développé une communauté massive. De nouvelles versions du projet sont publiées chaque mois, donc je suis convaincu que des problèmes comme la navigation seront résolus avec le temps.

### L'expérience du développeur compte

La capacité de partager du code entre les applications Android et iOS est sans aucun doute un attrait de React Native, mais ce n'est qu'une petite partie de ce qui rend l'outil si incroyable.

Ma partie préférée de l'utilisation de React Native est la capacité de recharger immédiatement. J'ai utilisé Android Studio dans le passé, et j'ai souvent dû faire face à des temps de construction de 30 à 60 secondes.

Cela fait gagner du temps et j'ai trouvé plus facile d'entrer dans un [état de flux](https://fr.wikipedia.org/wiki/Flow_(psychologie)) sans ces temps de construction ennuyeux pour me perturber.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UKfvFMsbyhhEgf6XBZnfvg.gif)
_Salut, je suis Taylor. Le rechargement à chaud a changé ma vie. Source : [Facebook](https://facebook.github.io/react-native/blog/2016/03/24/introducing-hot-reloading.html" rel="noopener" target="_blank" title=")_

React Native rend le développement mobile amusant à nouveau, et cela seul est une raison suffisante pour l'essayer pour votre prochain projet.

### Soyez prêt à explorer

React Native est un exemple parfait de ce qui peut se produire lorsque nous appliquons des idées qui ont fait leurs preuves dans un domaine du logiciel (le web), à un domaine apparemment séparé (le mobile).

Comme [Haseeb Quereshi](https://medium.com/@hosseeb) l'a argumenté de manière convaincante dans son [discours sur la convergence](https://softwareengineeringdaily.com/2017/02/24/convergence-with-haseeb-qureshi/), en tant qu'ingénieurs logiciels, nous devrions converger vers certains principes, langues et outils qui peuvent être appliqués avec succès universellement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2CEqay0FT0neAHDvGUu9OQ.jpeg)
_Source : [ThoughtCo](https://www.thoughtco.com/philosophy-of-mind-250531" rel="noopener" target="_blank" title=")_

Nous devrions vouloir trouver ce qui est vraiment la solution optimale.

> « Gardez votre identité petite » — Paul Graham

Souvent, nous devenons trop dogmatiques au sein d'une communauté, ce qui se fait au détriment de gains importants d'autres communautés.

Allez explorer d'autres domaines.

Si vous essayez React Native, vous verrez à quel point les résultats peuvent être impressionnants.

Merci beaucoup d'avoir pris le temps de lire mon article.

Pour lire plus de mes écrits sur le développement de logiciels et le développement personnel, visitez [taylormilliman.me](http://taylormilliman.me/).

Si vous souhaitez des articles/tutoriels plus détaillés sur React Native, cliquez sur le ? ci-dessous et n'hésitez pas à laisser un commentaire ci-dessous.