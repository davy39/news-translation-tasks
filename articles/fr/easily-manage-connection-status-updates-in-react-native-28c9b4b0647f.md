---
title: Comment gérer facilement les mises à jour du statut de connexion dans React
  Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T20:28:52.000Z'
originalURL: https://freecodecamp.org/news/easily-manage-connection-status-updates-in-react-native-28c9b4b0647f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Sp2YoeR7ngda2gFD5MkBKw.jpeg
tags:
- name: internet
  slug: internet
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment gérer facilement les mises à jour du statut de connexion dans React
  Native
seo_desc: 'By Jordy van den Aardweg

  Every now and then I like to create and explore technologies I do not have the time
  for in my daily life as a Freelance Frontend Developer. Lately, I’m exploring React
  Native and taking a dive in some new tools and APIs.

  But ...'
---

Par Jordy van den Aardweg

De temps en temps, j'aime créer et explorer des technologies pour lesquelles je n'ai pas le temps dans ma vie quotidienne en tant que développeur frontend freelance. Récemment, j'explore React Native et je plonge dans certains nouveaux outils et APIs.

Mais construire une application native est un peu différent de construire une application web. Je me suis récemment retrouvé dans un scénario où l'utilisateur n'a pas de connexion internet active.

Comment allons-nous informer l'utilisateur que notre application a des capacités limitées dans ce cas ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sp2YoeR7ngda2gFD5MkBKw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/ZYecenZy7o4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Galen Crout</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Lorsque vous construisez une application nécessitant une connectivité réseau, vous devez gérer correctement les requêtes échouées. Par exemple, lorsque la connexion internet de l'utilisateur décide de jouer à cache-cache. Ainsi, notre application peut informer l'utilisateur pourquoi une requête échoue ou même empêcher la requête de se déclencher. Et encore mieux : afficher un message utilisable à nos utilisateurs expliquant ce qui se passe, afin qu'ils puissent agir en conséquence.

En d'autres termes, nous pouvons donner un certain _contexte_ à nos utilisateurs sur pourquoi l'application ne peut pas effectuer une certaine requête.

#### Redux vs. Context API

La communauté React Native fournit un module [NetInfo](https://github.com/react-native-community/react-native-netinfo) pour exposer des informations sur la connexion réseau de l'utilisateur, comme si elle est en ligne ou hors ligne. Nous avons besoin que ces données soient globalement disponibles dans notre application.

Une idée générale serait d'utiliser Redux pour cela. Mon application utilise déjà Redux, alors pourquoi ne pas l'utiliser pour cela ?

Bien sûr, nous pourrions le faire. Mais cela nécessite que chaque composant soit connecté au store Redux si nous voulons utiliser ces informations de connectivité. Se connecter à Redux crée des frais généraux, plus de lignes de code et pourrait rendre notre application plus compliquée que nécessaire.

Explorons d'autres possibilités...

L'API Context de React fournit un moyen **plus simple**, **plus propre** de partager des données de type état à travers nos composants :

> Le contexte est conçu pour partager des données qui peuvent être considérées comme "globales" pour un arbre de composants React, telles que l'utilisateur authentifié actuel, le thème ou la langue préférée. — [Source](https://reactjs.org/docs/context.html#when-to-use-context)

Il semble que nous ayons un cas d'utilisation parfait pour utiliser la nouvelle API Context de React !

### Plongeons-nous

Tout d'abord, nous devons installer les packages requis, car dans React Native 0.59, le module `NetInfo` est dans un package séparé. React 16.6 ou une version ultérieure est également requis car il permet au contexte d'être disponible en dehors des méthodes de rendu. Très utile, car cela nous donne une plus grande flexibilité sur l'endroit où nous utilisons ce contexte.

Je ne vous ennuyerai pas avec la configuration d'une application React Native et je suppose simplement que vous en avez déjà une.

Installons le package `NetInfo` :

```
npm install @react-native-community/netinfo --save
```

Une fois installé, nous pouvons créer nos composants.

**Création du Fournisseur de Contexte**  
Configurons le composant `<NetworkProvider>`. Ce composant transmet notre statut de connectivité à tous nos composants enfants :

Comme montré ci-dessus, nous écoutons simplement l'événement `connectionChange`. Cet événement retourne `true` lorsqu'il y a une connexion internet active ou `false` lorsque l'utilisateur n'a pas de connexion internet active. Nous mettons à jour l'état lorsque le statut de connectivité change.

Dès que nous mettons à jour l'état, le contexte dans notre arbre de composants change. Ainsi, chaque composant a accès à la valeur mise à jour de `isConnected`. Similaire à Redux, mais avec beaucoup moins de code boilerplate.

**Enveloppement du Fournisseur de Contexte**  
Pour que l'API Context de React fonctionne, nous devons envelopper ce composant `<NetworkProvider>` que nous venons de créer autour de nos autres composants, comme ceci :

En faisant cela, nous rendons le `context` disponible dans chaque composant à l'intérieur du `<NetworkProvider>`.

La dernière étape consiste à utiliser le contexte dans un composant. Nous utilisons un `<ExampleComponent>` pour l'instant :

Maintenant, notre composant utilise l'API Context et `this.context.isConnected` est disponible pour que nous l'utilisions.

Nous pouvons maintenant afficher un message à nos utilisateurs dans le `<ExampleComponent>` lorsque la connexion internet de l'utilisateur est en ligne ou hors ligne.

Dans les versions précédentes de React, le `context` n'était pas disponible en dehors de votre méthode de rendu. [Depuis React 16.6.0](https://reactjs.org/blog/2018/10/23/react-v-16-6.html#static-contexttype), il est disponible en utilisant `static contextType` comme montré dans l'exemple ci-dessus. L'utiliser de cette manière nous donne une plus grande flexibilité sur l'endroit où nous voulons utiliser ce contexte à l'intérieur de nos composants.

#### Une note finale

Nous avons donc montré que l'API Context est parfaite pour définir et utiliser ces valeurs globales dans ce cas d'utilisation. Le statut de connectivité est important à avoir disponible dans toute notre application, afin que nous puissions informer nos utilisateurs lorsqu'une action nécessitant une connexion internet active va échouer.

Nous pourrions faire la même chose avec Redux, mais cela nécessiterait beaucoup plus de code. Utilisons les API natives de React lorsque cela est possible, car cela limite les dépendances !

Le Gist complet peut être trouvé sur [mon GitHub](https://gist.github.com/jvandenaardweg/58ed91e3c33de0b75a15d38853b23d7d).

### Merci d'avoir lu !

J'utilise Medium depuis quelques années maintenant, mais généralement je me contentais de lire et d'apprendre du contenu des autres. Des tutoriels comme celui-ci m'ont beaucoup aidé au fil des ans. Alors, écrire le mien est ma façon de rendre à cette communauté de développeurs géniale !

**Ce tutoriel vous a-t-il aidé ? Faites-le moi savoir dans les commentaires ?**

**Vous avez des commentaires pour que je puisse améliorer mes articles ? Je suis impatient de m'améliorer et de partager davantage de mes connaissances.**