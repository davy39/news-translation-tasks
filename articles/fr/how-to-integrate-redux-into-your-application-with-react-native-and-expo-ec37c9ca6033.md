---
title: Comment intégrer Redux dans votre application avec React Native et Expo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-09T22:33:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-redux-into-your-application-with-react-native-and-expo-ec37c9ca6033
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_5uIwZnr1Yhwq1PnBv7C7A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: Web Development
  slug: web-development
seo_title: Comment intégrer Redux dans votre application avec React Native et Expo
seo_desc: 'By Aman Mittal

  Redux is an important part of the React Native ecosystem. If your world revolves
  around JavaScript, you’ve probably heard about Redux. Before reading the rest of
  the tutorial and going further, just try to remember that you are only le...'
---

Par Aman Mittal

Redux est une partie importante de l'écosystème React Native. Si votre monde tourne autour de JavaScript, vous avez probablement entendu parler de Redux. Avant de lire le reste du tutoriel et d'aller plus loin, essayez simplement de vous souvenir que vous n'apprenez Redux que parce que cela vous facilitera les choses, et non pas pour les compliquer. Maintenant, apprenons pourquoi vous avez besoin de Redux dans votre application.

### Besoin de Redux

Construire une application React ou React Native dans le monde réel peut devenir complexe s'il n'y a pas de moyen approprié pour gérer les données. Si à un moment donné les données ne sont pas gérées, les choses vont devenir ingérables. Si vous êtes familier avec React ou React Native, vous connaissez la manière par défaut de gérer les données, qui consiste à les conserver dans l'état d'un composant et à les transmettre aux composants enfants sous forme de props.

L'état et les props sont les deux seuls moyens de contrôler les données dans un composant. Props est l'abréviation de **propriétés**. C'est une règle simple à suivre dans le monde React : nous ne devons pas muter ou changer la valeur des props. Dans React, le flux de données est unidirectionnel ou à sens unique. Cela signifie que les données peuvent toujours être transmises d'un parent à un composant enfant. Jetez un coup d'œil ci-dessous à cet exemple simple :

![Image](https://cdn-media-1.freecodecamp.org/images/X7XHOBi5wO0Yn4bEBdWMEMcS0kZlFT34Rxjy)

Dans l'exemple ci-dessus, nous créons deux composants (Parent et Enfant) dans des fichiers séparés. Le composant Parent consiste en une vue où le composant Enfant est rendu. Dans le composant enfant, la vue rend un message texte qui provient des props. Le message entrant est disponible sous forme de données dans l'état du composant parent.

De cette manière, le composant enfant peut être réutilisé avec d'autres composants parents de sorte que chaque composant parent peut avoir ses propres données à rendre. Notez que nous ne modifions pas la valeur de `this.props` à aucun moment.

L'état est là pour muter les données. C'est la seule raison pour laquelle l'état existe dans chaque composant. Chaque fois que nous voulons changer l'état, nous utilisons la méthode `this.setState()` dans un composant. Cette méthode ré-affiche le composant et tous ses composants enfants pour refléter les changements. Cela fonctionne de manière similaire dans React et React Native, mais les mécanismes internes sont différents.

![Image](https://cdn-media-1.freecodecamp.org/images/jTJ3lW05YTXLnkicAx0Zoz8YiTpvznDZacR8)

Puisque nous pouvons gérer l'état et les props si efficacement dans une application React Native, pourquoi Redux est-il nécessaire ? Eh bien, l'exemple ci-dessus représente le strict minimum et non un scénario en temps réel. Imaginez une application comme Instagram ou Twitter. Vous avez différents écrans, et chaque écran peut dépendre d'un ou deux composants comme le Parent et les composants Enfant réutilisables de notre exemple. Il serait difficile de suivre l'état de chaque composant.

Redux est l'une des méthodes les plus largement adoptées pour gérer les données. Il permet à l'état d'être partagé comme un attribut global qu'une application React Native entière peut utiliser et recevoir sous forme de props. Cela est connu sous le nom de création d'un store dans Redux. Redux simplifie l'état en le déplaçant à un seul endroit.

Redux utilise un mécanisme React sous-jacent appelé contexte. Nous n'allons pas nous attarder sur ce qu'est le contexte, car cela est hors du cadre de cet article. Je voulais simplement que vous sachiez qu'il ne se passe rien de magique en coulisses.

Retenez simplement les termes suivants, car nous allons les voir en action dans le tutoriel ci-dessous :

* Actions
* Réducteurs
* Store

La clé pour apprendre Redux est la pratique. Je ne veux pas partager trop d'informations et submerger les choses tout de suite. Alors commençons par créer une application de démonstration pour apprendre Redux.

### Construction d'une application Pomodoro

#### Getting Started with Expo-CLI ?

Pour construire cette application, je vais utiliser le dernier outil introduit par l'équipe [Expo](https://www.freecodecamp.org/news/how-to-integrate-redux-into-your-application-with-react-native-and-expo-ec37c9ca6033/undefined) appelé [expo-cli](https://www.npmjs.com/package/expo-cli). Installez-le comme une dépendance globale, puis initialisez un nouveau projet React Native en l'utilisant.

![Image](https://cdn-media-1.freecodecamp.org/images/4GZRQSXWn5wCAjmiwUYhnILw8uvZhH1XFDHF)

Pour voir si tout fonctionne correctement à cet état initial, exécutez la commande suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/SjDkbrwoU5rCqYm7KT62qE7bTEsYLymhqMIF)

Vous serez invité avec l'interface suivante. Prenez le temps de la parcourir. Si vous avez déjà construit des applications en utilisant Expo XDE ou Create-React-Native-App, vous verrez que peu de choses ont changé, sauf que maintenant Expo-CLI utilise le navigateur Chrome.

![Image](https://cdn-media-1.freecodecamp.org/images/nZH9NiAh1Bq1LtWo64t4eXptdwUgW75w6haQ)

Choisissez un simulateur ou un appareil qui peut exécuter Expo Client comme marqué dans l'image ci-dessus. Si vous obtenez l'écran ci-dessous, cela signifie que notre projet React Native a été initialisé sans aucune difficulté.

![Image](https://cdn-media-1.freecodecamp.org/images/7HI7BGLwOwN-8p55RBd77tV367-2551uqvjw)

Avec cela, créez les fichiers et dossiers suivants à l'intérieur du répertoire `components`. Je discuterai plus tard de la raison pour laquelle nous suivons cette structure de répertoire. Pour l'instant, notre configuration initiale est complète et nous pouvons commencer à construire notre application.

![Image](https://cdn-media-1.freecodecamp.org/images/Jm2jjrxqFuGKGIbROq0sxbZ9p1l3QqYx6fkh)

#### Composant Timer ⏱

Tout d'abord, nous allons créer un composant Timer simple et le connecter avec `App.js`. Ajoutez le code suivant à `Timer/index.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/YWNtoexuaX5Nv2MnP0-G0fB4QaqweuUvjjCX)

Ensuite, modifiez le fichier `App.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/dFthuKqcZKpECgVps3jXSLFP7bVleoRYbt3i)

![Image](https://cdn-media-1.freecodecamp.org/images/A5vxhakws61cLI6mISsgdKmR2Ca-mYSyWc9s)

Nous allons maintenant créer un composant Timer statique pour voir comment les choses s'emboîtent. Nous commencerons par modifier la `StatusBar`. Ensuite, nous définissons deux éléments `Text` de la bibliothèque `react-native` pour spécifier où le timer réel sera affiché et où les boutons pour démarrer et arrêter le timer seront affichés. Pour l'instant, les deux sont des champs de texte.

![Image](https://cdn-media-1.freecodecamp.org/images/VpxLf9bYCP1sLdfR2BUUAU2wWApLLEidkXYO)

![Image](https://cdn-media-1.freecodecamp.org/images/HwnZhyXMrvTccyXbApmC9uPKVJRf7ndUS9pd)

#### Ajout de boutons ?

Dans cette section, nous allons remplacer la section qui affiche `Start and Stop Buttons!` par des boutons réels. Nous allons utiliser `TouchableOpactiy` pour faire fonctionner cela. Un composant `TouchableOpacity` agit comme un wrapper pour faire en sorte que les vues répondent correctement aux touches. L'opacité de la vue enveloppée (ou le bouton dans notre cas) diminue chaque fois qu'un utilisateur la touche.

Nous créons un composant réutilisable puisque nous avons besoin de deux boutons : Start et Stop.

![Image](https://cdn-media-1.freecodecamp.org/images/km0-Zyv3Tyg4o8XoazPbpDRzje98onNZT15A)

Il s'agit d'un composant sans état, donc il n'a pas de classe — nous avons seulement besoin qu'il représente le bouton dans l'interface utilisateur de notre application. Nous importons également les icônes FontAwesome depuis `@expo/vector-icons`, qui est un fork de react-native-vector-icons et vient directement avec le SDK expo. Pas besoin de l'installer comme une dépendance séparée. Pour afficher une icône, nous devons définir sa `size`.

Enfin, dans le composant sans état ci-dessus, nous définissons `propTypes`. Je discuterai de la manière et de la raison pour laquelle nous devrions utiliser PropTypes dans une application React Native dans un autre article.

Dans une application mobile, les événements sont déclenchés par le toucher. Pour gérer ces événements, nous allons utiliser `onPress`. Nous n'aurons que deux événements ici, Start et Stop. Les deux boutons de notre application vont utiliser `onPressOut` qui diffère de `onPress`. `onPressOut` est appelé chaque fois que le toucher est relâché par l'utilisateur (quand l'utilisateur arrête de presser le bouton). Il est appelé avant `onPress` et est plus précis dans une situation comme la nôtre où nous devons démarrer ou arrêter le timer en appuyant sur le bouton dès que l'utilisateur a terminé.

Nous allons maintenant avoir besoin de ce composant `Button` dans notre composant Timer.

![Image](https://cdn-media-1.freecodecamp.org/images/buCkAigjLxhgQkvMIBOfwodSO0p4I0mkCxCS)

![Image](https://cdn-media-1.freecodecamp.org/images/cIumY-jfK1zPYQG8Qn9ZU8sABf8whJsV2MBU)

### Intégration de Redux ?

Jusqu'à présent, notre application Timer ne fait rien d'autre que d'afficher une interface utilisateur minimale. Pour la faire fonctionner, nous commençons par ajouter quelques dépendances Redux nécessaires.

![Image](https://cdn-media-1.freecodecamp.org/images/wvZ64BnNHI8mJMMnSJi4uwa27YukF07aqnYo)

Maintenant, commençons à intégrer Redux dans notre application.

#### Actions ?

Dans Redux, l'état de l'ensemble de l'application est représenté par un objet JavaScript. Considérez cet objet comme étant en lecture seule, puisque nous ne pouvons pas apporter de modifications à cet état (qui est représenté sous la forme d'un arbre) directement. Nous avons besoin d'`actions` pour le faire.

Les actions sont comme des événements dans Redux. Elles peuvent être déclenchées sous la forme de clics de souris, de presses de touches, de temporisateurs ou de requêtes réseau. La nature de chaque événement mentionné est mutable. Une action est un objet JavaScript. Pour définir une action, il y a une exigence : chaque action doit avoir sa propre propriété de type. Nous définissons ces types dans un fichier appelé `types.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/IVm7vvhTO3PcoLzGW3JrgWMZ3UTi5OTUwhKI)

Notre application n'a besoin que de trois actions pour l'instant. Le type de toute action est une valeur de chaîne et est défini comme une constante.

Dans le fichier `actions.js`, nous allons nécessiter ces types pour définir les créateurs d'actions. Les créateurs d'actions sont des fonctions qui créent des actions.

![Image](https://cdn-media-1.freecodecamp.org/images/FRPSp-IPWO5KlLX6yKCqQKBUdXBgdN9m5t71)

#### Réducteurs ?

Le récepteur de l'action est connu sous le nom de réducteur. Chaque fois qu'une action est déclenchée, l'état de l'application change. La gestion de l'état de l'application est effectuée par les réducteurs.

Un réducteur est une fonction pure qui calcule l'état suivant en fonction de l'état initial ou précédent. Il produit toujours la même sortie si l'état est inchangé. Il prend deux entrées, et l'état et l'action doivent retourner l'état par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/MyhoWXMag-F8DkaEFAfTXBBrmdVG8YqXv0c3)

Dans notre état initial, nous définissons trois attributs : `isPlaying`, `elapsedTime` et `timerDuration`. Le timer a actuellement une valeur par défaut de 6 (secondes) à des fins de test, mais la valeur réelle que nous allons changer plus tard est `25` (ou 1500 secondes).

Ensuite, il y a trois fonctions d'assistance :

* `applyStartTimer` démarrera le timer
* `applyRestartTimer` arrêtera la fonction du timer et tout remettra à zéro
* et enfin, `applyAddSecond` vérifiera si le temps écoulé est inférieur à la durée totale du timer. Si c'est le cas, il ajoutera une seconde de plus pour augmenter sa valeur. Si ce n'est pas le cas, il retournera l'état par défaut et arrêtera la fonction du timer.

Après cela, nous définissons notre fonction de réducteur et exportons la même fonction. Observez comment la fonction de réducteur est organisée. Il s'agit d'un modèle suivi par la plupart des membres de la communauté que j'ai vus sur Internet.

[Ceci](https://egghead.io/courses/getting-started-with-redux) est une bonne ressource pour commencer avec Redux en général par [Dan Abramov](https://www.freecodecamp.org/news/how-to-integrate-redux-into-your-application-with-react-native-and-expo-ec37c9ca6033/undefined) et c'est GRATUIT !

#### Création du Store Redux ?

Avec l'aide du réducteur et de l'état initial, nous pouvons créer l'objet store.

![Image](https://cdn-media-1.freecodecamp.org/images/H7SgqQg0H2U9PhdlNRWC6nZdE-vFTu5yXhku)

Un store est un objet qui rassemble les actions et les réducteurs. Il fournit et maintient l'état au niveau de l'application plutôt qu'au niveau des composants individuels. Redux n'est pas une bibliothèque opinionnée en termes de framework ou de bibliothèque qui devrait l'utiliser ou non.

Pour lier une application React ou React Native avec Redux, vous le faites avec le module `react-redux`. Cela se fait en utilisant le composant d'ordre supérieur `Provider`. Il transmet essentiellement le store au reste de l'application.

Nous devons lier les créateurs d'actions avec notre fonction Timer afin de la rendre pleinement fonctionnelle (de sorte qu'elle réponde aux événements tactiles ou au démarrage ou au redémarrage du timer). Nous allons faire cela dans la fonction `Timer/index.js`.

Tout d'abord, nous importons les dépendances requises pour lier les créateurs d'actions.

![Image](https://cdn-media-1.freecodecamp.org/images/Bf8plFKT3MiMQZLmC6Ndn5IjRLFW5vXwPLrj)

`bindActionCreators` mappe les fonctions d'action à un objet en utilisant les noms des fonctions d'action. Ces fonctions envoient automatiquement l'action au store lorsque la fonction est appelée. Pour changer les données, nous devons envoyer une action. Pour activer cela, nous avons besoin de deux choses : `mapStateToProps` et `mapDispatchToProps`, et nous devons connecter les deux avec notre composant. Il s'agit du code standard que vous allez réécrire.

Nous définissons ces deux fonctions et modifions notre instruction `export default` après avoir défini les styles pour nos vues React Native.

![Image](https://cdn-media-1.freecodecamp.org/images/g8SnUFvB9t4nDcc2ltNLK9Q4Z-6v1sFwZvqe)

`mapStateToProps` est un objet qui vit dans le store dont les clés sont transmises au composant sous forme de props. Voici le code complet pour le composant Timer.

### Compléter l'application ⚒ + ?

![Image](https://cdn-media-1.freecodecamp.org/images/XmkxE9VFSSyhjfTQQrSa-vzDMZwfvPI4np9C)

J'ai créé une fonction personnalisée appelée `formatTime` pour afficher l'heure dans le bon format, mais vous pouvez utiliser n'importe quelle bibliothèque de timer. Ensuite, pour incrémenter la valeur du temps, j'utilise la méthode de cycle de vie React `componentWillReceiveProps`. Je sais qu'elle va bientôt être obsolète, mais pour l'instant, elle fonctionne. Voyez notre mini-application en action ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/AojvxCzJ-eF1d943Owepa7qy0IQErcbAcGRx)

Pour des raisons de brièveté et de cette démonstration, j'utilise uniquement des secondes pour afficher le timer. Vous pouvez augmenter la valeur du timer en modifiant la valeur de la constante `TIMER_DURATION` dans `reducers.js`.

Nous avons atteint la fin de l'article. Espérons que vous avez eu autant de plaisir à le lire que j'en ai eu à l'écrire. Vous pouvez trouver le code complet de cet article dans ce dépôt Github :

[**amandeepmittal/rn-pomodoro-example**](https://github.com/amandeepmittal/rn-pomodoro-example)  
[_rn-pomodoro-example - React Native + Redux integaration_github.com](https://github.com/amandeepmittal/rn-pomodoro-example)

_Vous souvenez-vous que je vous ai parlé d'une structure de fichiers particulière que j'ai suivie pour implémenter l'architecture Redux ? Eh bien, elle s'appelle le modèle **re-ducks** et vous pouvez trouver plus de détails dans cet article informatif d'[Alex Moldovan](https://www.freecodecamp.org/news/how-to-integrate-redux-into-your-application-with-react-native-and-expo-ec37c9ca6033/undefined) :_

[**Scaling your Redux App with ducks**](https://medium.freecodecamp.org/scaling-your-redux-app-with-ducks-6115955638be)  
[_How does your front-end application scale? How do you make sure that the code youre writing is maintainable 6 months_medium.freecodecamp.org](https://medium.freecodecamp.org/scaling-your-redux-app-with-ducks-6115955638be)

**? Pour plus de questions, contactez-moi sur [Twitter](https://twitter.com/amanhimself), ou lisez plus sur moi sur mon [site web](https://amanhimself.dev).**

[**Si vous souhaitez recevoir des mises à jour sur mon prochain article sur React Native, envisagez de vous inscrire à ma newsletter.**](https://upscri.be/e51a31/)