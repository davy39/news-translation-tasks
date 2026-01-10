---
title: Animation de bulle avec React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-02T07:35:02.000Z'
originalURL: https://freecodecamp.org/news/bubble-animation-with-react-native-72674eab073a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TRtgLab0Tjd7bLg6.
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
seo_title: Animation de bulle avec React Native
seo_desc: 'By Narendra N Shetty

  Lessons learned while building a React Native App using Animated and PanResponder


  In this article, I’ll talk about how I implemented an app transition which I found
  on Dribbble by Ramotion.


  _[https://dribbble.com/shots/2694049-...'
---

Par Narendra N Shetty

#### Leçons apprises lors de la création d'une application React Native en utilisant `Animated` et `PanResponder`

![Image](https://cdn-media-1.freecodecamp.org/images/0*TRtgLab0Tjd7bLg6.)

Dans cet article, je vais parler de la manière dont j'ai implémenté une transition d'application que j'ai trouvée sur Dribbble par [Ramotion](https://dribbble.com/Ramotion).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GZVRK8qxfuLU4AUrUNry5g.gif)
_[https://dribbble.com/shots/2694049-Pagination-Controller-App-Interface](https://dribbble.com/shots/2694049-Pagination-Controller-App-Interface" rel="noopener" target="_blank" title=")_

Ce contrôleur de pagination peut être utilisé pour un flux d'intégration ou pour un tutoriel.

La version complète est publiée dans Expo, et vous pouvez l'obtenir en ouvrant l'application Expo et en scannant ce code QR :

![Image](https://cdn-media-1.freecodecamp.org/images/1*esBhVm4dAnaXERC-coIrVQ.png)
_[https://expo.io/@narendrashetty/onboarding-blog](https://expo.io/@narendrashetty/onboarding-blog" rel="noopener" target="_blank" title=")_

### Commençons, d'accord ?

Voici comment j'ai construit l'arrière-plan :

J'avais une `View` contenant la couleur d'arrière-plan. Cela inclut `Animated.View` pour l'animation de la bulle. Sa position était absolue afin qu'elle reste en haut de l'écran. J'ai également ajouté quelques styles de base.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lwk_IdAAzEKX5Hb1tj4JNQ.png)

Ensuite, j'ai animé la bulle en l'expansant de 0 à max en utilisant la transformation CSS scale avec `Animated.timing`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CtAMCroXo5AvBiwOZlc63Q.gif)

L'animation ci-dessus devait être déclenchée en fonction de l'interaction de l'utilisateur. J'ai d'abord utilisé `TouchableWithoutFeedback`. Ensuite, je l'ai changé avec des gestes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sIcR0RdmQA7SK2fSUcu7MA.gif)

J'ai positionné la bulle selon le gif, qui animait depuis le bas. Je l'ai fait en utilisant les propriétés `top` et `left`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*keM44KHgufeyR5s-aviqaA.gif)

Propre ! Les résultats sont ceux attendus, sauf pour la couleur. Nous y reviendrons plus tard.

J'ai ensuite restructuré le code en déplaçant la logique de la bulle dans un composant séparé appelé `CircleTransition`. Ensuite, j'ai déclenché l'animation depuis le composant parent.

Ensuite, il était temps de s'attaquer à la couleur. Pour faire animer la bulle avec la nouvelle couleur, j'ai passé la nouvelle couleur dans le composant. Et après la transition, j'ai masqué la bulle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OF0UIS4xMaHb5vXg0k6_bQ.gif)

Pouvez-vous voir quelque chose de bizarre dans la transition ci-dessus ?

Lors de la deuxième transition de la bulle, la couleur d'arrière-plan est revenue à la première couleur. Je devais mettre à jour la couleur d'arrière-plan avec la nouvelle couleur lorsque la bulle était en transition.

J'ai passé un callback à la méthode `start` qui s'exécutait lorsque la transition était terminée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oo83AYeag2TPn43k6ApHXg.gif)

Voilà ! Tout est prêt. J'avais maintenant l'animation de base qui fonctionnait.

Ensuite, je me suis penché sur les gestes. Les transitions de bulle se produisent lorsque l'utilisateur balaye vers la gauche ou la droite selon le gif.

J'ai créé un nouveau composant appelé `Swipe`. Il contient toute la logique pour le geste et remplace `TouchableWithoutFeedback`.

J'ai utilisé `PanResponder` qui reconcile plusieurs touches en un seul geste. Il rend les gestes à touche unique résistants aux touches supplémentaires. Il peut également reconnaître des gestes multi-touch simples. Pour plus d'informations, vous pouvez consulter [ici](https://facebook.github.io/react-native/docs/panresponder.html) et [ici](https://facebook.github.io/react-native/docs/gesture-responder-system.html).

Maintenant, pour la logique des gestes.

D'abord, je devais déterminer dans quelle direction l'utilisateur balayait. Je devais seulement animer lorsque l'utilisateur balayait vers la gauche ou la droite. Je devais également établir un seuil pour déterminer si c'était réellement un balayage ou non.

Si c'était un balayage valide, je déclenchais l'action appropriée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RAoguSe8-rcAvnCx2vkCIg.gif)

Oui ! Vous avez deviné juste. J'ai obtenu ce que je voulais réaliser avec le geste. Ensuite, j'ai ajouté une action pour `swipeRight`. Le geste a été complété avec un peu de refactoring.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ENwNGJeMT2zODhYm1-WIzg.gif)

C'est tout ! C'était la partie la plus complexe de l'application.

Je ne vais pas montrer tout mon travail sur cette application. Les informations dans cet article devraient être suffisantes pour vous aider à construire la vôtre. Fork [ce projet](https://github.com/narendrashetty/onboarding-RN) et essayez de compléter votre application pour qu'elle corresponde au gif ci-dessus.

Si vous êtes bloqué et avez besoin d'aide, la version finale est dans la branche `result`, jetez un coup d'œil. Vous pouvez également me contacter sur Twitter [@narendra_shetty](https://twitter.com/narendra_shetty) ou commenter ci-dessous.

Et lorsque vous aurez terminé, veuillez partager votre lien Expo/GitHub.

Si cet article vous a été utile, veuillez applaudir pour moi. Cela me motivera à écrire davantage :)