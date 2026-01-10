---
title: Leçons apprises lors du développement avec React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T18:17:18.000Z'
originalURL: https://freecodecamp.org/news/lessons-i-learned-while-building-in-react-native-917cb7bb5993
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gLt2OppZEywjKDYKkfsBQw.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Leçons apprises lors du développement avec React Native
seo_desc: 'By Amanda Bullington

  When I received an offer for a software engineering role to build an app in React
  Native, I wasn’t sure what to expect.

  On one hand, it sounded exciting to be able to build a mobile application for iOS
  and Android using a single ...'
---

Par Amanda Bullington

Lorsque j'ai reçu une offre pour un poste d'ingénierie logicielle afin de construire une application en React Native, je ne savais pas trop à quoi m'attendre.

D'un côté, cela semblait excitant de pouvoir construire une application mobile pour iOS et Android en utilisant une seule base de code. De l'autre, en entendant que des entreprises comme Airbnb avaient [testé la plateforme et finalement décidé de ne pas l'utiliser](https://medium.com/airbnb-engineering/react-native-at-airbnb-the-technology-dafd0b43838), je me suis dit qu'il y aurait probablement un certain nombre de défis à relever.

Maintenant, après quelques mois, voici quelques-unes des leçons que j'ai apprises en cours de route.

#### **Choisir les bonnes bibliothèques**

L'une des premières choses que j'ai apprises sur React Native est que le choix des bibliothèques tierces est souvent limité. En tant que développeur web JavaScript, j'avais un large choix de bibliothèques que je pouvais personnaliser pour divers projets.

Les bibliothèques React Native sont plus complexes à construire. Elles nécessitent une connaissance du code natif pour iOS et Android pour fonctionner sur plusieurs plateformes. Pour cette raison, il n'y a pas autant de personnes qui développent des bibliothèques pour React Native.

![Image](https://cdn-media-1.freecodecamp.org/images/4j9MuYQpj3Qzl6q9BkQnkh8FGCCEF1qyeTLh)
_Il n'y a vraiment pas autant de choix dans React Native_

Après quelques recherches infructueuses sur GitHub, j'ai fini par choisir la plupart des bibliothèques de mon application à partir du [dépôt React Native Community](https://github.com/react-native-community). Ce sont généralement les mieux maintenues et presque garanties pour fonctionner avec la dernière version de React. Le [Native Directory](https://native.directory/) était un autre endroit utile pour rechercher rapidement ce qui est disponible dans React Native.

Même au sein du dépôt de la communauté RN, toutes les bibliothèques ne fonctionnaient pas directement. Parfois, je devais fork le dépôt et faire quelques ajustements moi-même. D'autres fois, je devais rétrograder vers une version qui corrigait le bug particulier qui apparaissait dans mon application. Le contrôle de version est d'autant plus important lorsqu'il y a peu de bibliothèques et peu de mainteneurs.

#### **Se familiariser avec Flexbox**

Avec plus de 10 000 types d'appareils pour Android seul, il peut être difficile de construire une application qui fonctionne pour toutes les tailles d'écran. J'avais besoin que mon application ait une bonne apparence sur des appareils aussi petits que l'iPhone SE et aussi grands que le Pixel 2XL.

Au début, j'ai essayé de styliser mon application en utilisant la classe Dimensions intégrée de React Native pour trouver la largeur et la hauteur de chaque écran. Finalement, cela était trop compliqué à maintenir à mesure que l'application grandissait. Au lieu de cela, Flexbox est la clé pour pouvoir aborder le stylisme sur différentes tailles d'écran avec grâce. Un rapide passage par l'outil [Flexbox Froggy](https://flexboxfroggy.com/) est un bon moyen de se mettre à niveau.

Flexbox n'a pas résolu tous mes problèmes de style. J'ai encore rencontré des tailles d'écran particulières qui nécessitaient leurs propres solutions de style comme [SafeAreaView](https://facebook.github.io/react-native/docs/safeareaview) pour la série iPhone X. J'ai également dû utiliser des instructions conditionnelles pour différents styles iOS et Android sur de nombreux écrans. Mais dans l'ensemble, c'est un excellent outil pour concevoir des applications dans React Native.

#### **Éteindre et rallumer**

Une fois que j'ai installé une nouvelle bibliothèque tierce et exécuté `react-native link`, j'ai souvent rencontré l'erreur "undefined is not an object". React Native est connu pour ses messages d'erreur non descriptifs. Il m'a fallu un certain temps pour comprendre ce que cela signifiait. Au début, je pensais qu'il y avait un problème avec la bibliothèque. Ou qu'elle ne fonctionnait pas avec la version de React Native que j'avais installée.

Ensuite, au fond d'un fil de discussion GitHub pour une bibliothèque particulière, j'ai trouvé [ce commentaire](https://github.com/react-native-community/react-native-image-picker/issues/269#issuecomment-326609908) qui a finalement éclairé pourquoi aucune de mes bibliothèques ne fonctionnait correctement.

Comme beaucoup de développeurs, j'avais pris l'habitude de simplement recharger mon projet tout en exécutant `react-native run-android` ou `react-native run-ios`. Le rechargement à chaud est génial pour gagner du temps tout en faisant de petits ajustements de style à l'application et en vérifiant les écrans. Cependant, cela n'aide pas à intégrer de nouvelles bibliothèques dans l'application. Mes nouvelles bibliothèques ne fonctionneraient pas tant que je n'aurais pas fermé tous mes simulateurs/émulateurs, déconnecté mes appareils et relancé `npm start` pour redémarrer le Metro bundler.

En d'autres termes, je devais tout éteindre et rallumer pour intégrer correctement les bibliothèques tierces sans messages d'erreur trompeurs.

#### **Travailler sans débogueur**

![Image](https://cdn-media-1.freecodecamp.org/images/Hu2yf4yDMQizsYlGJGLbGTjMoNrOxFLKNj75)
_Photo par [Pexels](https://www.pexels.com/@mikebirdy?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener" target="_blank" title="">Mikes Photos</a> from <a href="https://www.pexels.com/photo/ladybug-plastic-toy-198101/?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener" target="_blank" title=")_

En tant que développeur web, j'étais habituée à rechercher des bugs dans le débogueur Google Chrome. Dans React Native, il n'a fallu que quelques semaines avant que je ne perde ma capacité à déboguer dans Chrome.

L'une des contraintes de mon application était que je devais utiliser Realm comme base de données principale. Cependant, Realm a un [problème fréquemment signalé](https://github.com/realm/realm-js/issues/2128) où il cannibalise le débogueur Chrome, le rendant impossible à utiliser. Je devais trouver une autre solution.

React Native dispose d'un [débogueur intégré](https://facebook.github.io/react-native/docs/debugging) où vous pouvez enregistrer les console.logs dans le terminal avec `react-native log-android` ou `react-native log-ios`. Bien que cela fonctionne bien sur Android, j'ai rencontré des [problèmes](https://github.com/facebook/react-native/issues/9441) en utilisant ce débogueur pour iOS. J'ai commencé à adopter une approche de développement d'abord pour Android, où je construisais et testais tout sur Android pour accéder facilement aux console.logs, puis je faisais des ajustements à la version iOS si nécessaire. J'ai également investi dans l'écriture de meilleurs messages d'erreur dans mon application, ce qui a bénéficié à la fois à mes utilisateurs et à moi-même.

J'ai également expérimenté l'utilisation de XCode et Android Studio pour le débogage, mais j'ai finalement trouvé que mon approche d'abord pour Android était la solution la plus facile avec le moins de changement d'écran.

#### **Exécuter des builds de production tôt**

Des développeurs expérimentés de React Native m'ont dit qu'ils rencontraient rarement des problèmes en mode production qu'ils n'avaient pas déjà vus et résolus en développement. Ce n'était pas mon expérience. Lorsque j'ai exécuté mes builds de production sur des appareils physiques, j'ai pu détecter quelques erreurs que je n'avais pas remarquées auparavant.

![Image](https://cdn-media-1.freecodecamp.org/images/w4OEUSr1hMms6sjVU1eUO7CRFthO3B93JJoG)
_Prêt, installé, production_

Un exemple était la navigation. La configuration de la navigation dans une application mobile était difficile à comprendre au début, et j'ai dû apporter quelques modifications à la façon dont j'ai configuré ma bibliothèque react-navigation pour livrer les données à l'utilisateur au bon moment. L'utilisation d'un appareil physique m'a permis de simuler toutes les façons dont un utilisateur pourrait parcourir mon application (c'est-à-dire lorsqu'ils passeraient à un nouvel écran ou appuieraient sur le bouton de retour) et de configurer la navigation en conséquence.

Un autre problème que j'ai trouvé en production impliquait des [permissions Android](https://facebook.github.io/react-native/docs/permissionsandroid) dangereuses. Les nouveaux téléphones Android nécessitent des demandes de permission plus explicites, et une fois que j'ai testé sur un appareil physique, j'ai réalisé que la galerie photo de mon application avait besoin de ces permissions pour se charger correctement.

#### **Conclusion**

React Native est bien documenté et relativement rapide à apprendre, surtout si vous connaissez déjà React. C'est immensément satisfaisant de construire une application mobile qui fonctionne à la fois sur iOS et Android avec une seule base de code.

Les défis que j'ai rencontrés ci-dessus étaient certaines des parties les plus délicates — mais dans l'ensemble, il n'y avait pas d'obstacles majeurs au développement d'une application en React Native. Principalement, je devais comprendre les particularités du développement mobile et me familiariser avec certains des messages d'erreur maladroits. Maintenant que j'ai passé ces premières courbes d'apprentissage et adopté une approche d'abord pour Android, le développement est beaucoup plus rapide.

Est-ce que je développerais à nouveau avec React Native ? Absolument.