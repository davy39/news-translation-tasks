---
title: Comment développer vos superpouvoirs React avec le motif Render Props
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-24T19:02:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-your-react-superpowers-with-the-render-props-pattern-b74e68c6d053
coverImage: https://cdn-media-1.freecodecamp.org/images/0*SkjBUognKSY8KiNG
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment développer vos superpouvoirs React avec le motif Render Props
seo_desc: 'By Eduardo Vedes

  Hey everybody! This time I’m going to tell you about this great superpower called
  “render props”.

  The term “render prop” refers to a technique for sharing code between React components
  using a prop whose value is a function.

  The conc...'
---

Par Eduardo Vedes

Salut à tous ! Cette fois, je vais vous parler de ce superpouvoir appelé **"render props"**.

Le terme **"render prop"** fait référence à une technique pour partager du code entre des composants React en utilisant une prop dont la valeur est une fonction.

Le concept impliqué est également connu sous le nom de **"children as a function"** ou **"child as a function"**. Les composants qui implémentent ce motif peuvent être appelés **"render prop components"**.

C'est l'un des motifs avancés de React qu'il est indispensable de maîtriser dans votre vie quotidienne de programmeur.

Alors, j'espère que votre JavaScript est en forme car c'est un motif génial et super cool à implémenter !

Commençons :

![Image](https://cdn-media-1.freecodecamp.org/images/G3S9a2SFCGj1WJku6iQOXr2U1RzOpBvr1AT6)
_Composant Temperature_

Qu'avons-nous ici ?? Décodons !

Nous avons un composant qui reçoit des enfants en tant que prop (il les déstructure à partir des props) et les retourne sous forme de fonction, avec des arguments. Ici, les enfants sont retournés avec l'entier 30.

Juste pour être sûr que nous sommes sur la même longueur d'onde, le code ci-dessus est le même que d'écrire :

![Image](https://cdn-media-1.freecodecamp.org/images/m1VCbXfI6k411uj9oiMyUsgJ5quZgrgXjAv9)
_Composant Temperature recevant des props génériques_

Ou dans un composant de classe plus élaboré :

![Image](https://cdn-media-1.freecodecamp.org/images/UjXx9CvadH2O2UBQEa6MCXzRG3luRLBDP-t2)
_Exemple de composant de classe Temperature._

OK ! Revenons à ce que nous faisions.

Pour invoquer ce composant, nous écrivons une fonction en tant qu'enfants :

![Image](https://cdn-media-1.freecodecamp.org/images/ezNH-u5L4kntGNE3TT2F8ab6c4gDnbxg8udS)

D'accord, améliorons un peu le code.

![Image](https://cdn-media-1.freecodecamp.org/images/vJ3jNJGa-4dFN-Uz-e-poU7U3JSdsFLRec05)
_Composant Temperature et composant principal App_

J'utilise toujours un peu de style bootstrap pour rendre mes exemples simples, propres et un peu polies.

Gardez à l'esprit que les enfants sont tout ce qui se trouve à l'intérieur de l'invocation <Temperature> </Temperature>.

Le composant Temperature est totalement transparent sur ce que sont les enfants, il se contente de les rendre en passant 30 comme entier.

Donc le résultat que nous avons dans le navigateur est celui-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/Qiml1WaNrlpdyKIExuzDlWK3PjTo6vqd296V)
_rendu des composants_

Disons quelque chose sur la météo ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/qhL9Wvw-4BLdVpJ8zJDCHxZl5bYFrePZenNU)
_fonction pour dire quelque chose sur la météo_

![Image](https://cdn-media-1.freecodecamp.org/images/wrjNkS4582AgA0Q7CyeF-M5zpqX4nYSELxor)
_Mon cerveau fond !!!_

D'accord ! Belle fonctionnalité, dites-vous !

Mais pourquoi est-ce une belle fonctionnalité ? Gardons votre cerveau au frais ! ?

Nous avons séparé le contrôleur de la vue ! Maintenant, nous avons un composant appelé Temperature qui est capable de recevoir des températures d'une API "loin loin" et de rendre ses enfants, quels qu'ils soient, en leur passant la valeur de température.

Assurez-vous de comprendre ce grand avantage et ce superpouvoir ! Le composant Temperature ne connaît pas ses enfants à l'avance. Il sait seulement que, indépendamment des enfants, il les rendra et leur passera la valeur de température.

Bien sûr, nous pourrions utiliser la composition et encapsuler la logique des enfants dans un autre composant, par exemple ShowTemperature en Celsius.

Faisons-le.

![Image](https://cdn-media-1.freecodecamp.org/images/3tymqxQamDuMCADbxZcMgLE6tEgInKkNenlj)
_encapsuler ShowTemperatureInCelsius_

Et c'est tout ! Pourquoi est-ce génial ? Parce que maintenant je vais réutiliser les mêmes choses et faire un ShowTemperatureInFahrenheit !

![Image](https://cdn-media-1.freecodecamp.org/images/O3Hrc8R-rsZw-VyFyPPDQjmURIkakRiforfS)
_ShowTemperatureInFahrenheit et refactorisation du composant App_

Oui ! C'est si bien ! Nous avons encapsulé le rendu dans des composants en utilisant la composition. Nous pourrions continuer à faire un nouveau composant ShowTemperature à invoquer à l'intérieur de ShowTemperatureInCelsius ou ShowTemperatureInFahrenheit.

![Image](https://cdn-media-1.freecodecamp.org/images/QKg5UuoS3onEzVo9c2LScbJELTMOLjKRlA3t)
_Mon cerveau fond et mon cerveau ne fond pas en même temps ! C'est de la physique quantique !_

Mais si nous voulons appliquer à nouveau le motif render props pour montrer différentes couleurs que nous obtenons des préférences de l'utilisateur, par exemple ?

Essayons.

![Image](https://cdn-media-1.freecodecamp.org/images/cFXHJgi8f3TzdZQE5tGoWGkX7TrPTmcF3Jsb)
_Composant Colors_

![Image](https://cdn-media-1.freecodecamp.org/images/0VVn4YeeD7n7Zd35n5H5R7Btcsx0hci0IndL)
_Temps est rouge ou temp est noir ?_

D'accord les amis, c'est un excellent outil mais... "Un grand pouvoir implique de grandes responsabilités".

Si nous faisons un ou deux composants render prop de plus, nous plongerons dans un enfer de rappels plus tôt que nous ne le pensons !

Lorsque nous devons extraire quelque chose ou obtenir d'autres props qui viennent mélangées dans le flux de cascade React, nous allons commencer à nous confondre et le code deviendra désordonné et plus explicite ou déclaratif.

Alors... comment pouvons-nous éviter cela ?

Eh bien... peut-être y avez-vous déjà pensé. Render props est très similaire dans son but aux HOC (Higher Order Components).

En fait, nous pouvons utiliser l'un ou l'autre pour presque le même but. Beaucoup d'encre a déjà été dépensée sur ce sujet.

Si vous ne savez rien sur les HOC, vous pouvez lire mon article sur le motif container [ici](https://medium.freecodecamp.org/react-superpowers-container-pattern-20d664bdae65) où je vous montre comment faire un HOC simple.

Je promets d'écrire un article sur les HOC dans un avenir proche, car c'est aussi un motif qui mérite une certaine attention.

Alors, juste pour tester, faisons évoluer notre abstraction Color vers un HOC :

![Image](https://cdn-media-1.freecodecamp.org/images/3yEmQhNe-WaHeS-k6Aou3GMPrLCtm8SDFVcj)
_withColor HOC (Higher Order Component)_

Bien ! Le même résultat ! Nous avons fait une fonction JavaScript qui reçoit un composant et retourne une classe qui rend le WrappedComponent avec la prop souhaitée que nous pouvons obtenir ailleurs !

C'est un exemple un peu idiot mais je pense qu'il aide à souligner la différence entre ces deux motifs.

Alors... quand devez-vous utiliser l'un ou l'autre ?

Eh bien, tout a un coût. Je dirais que je trouve les HOC beaucoup plus propres que les render props.

Le problème est que les HOC coupent un peu le flux de composition qui rend React si génial. De plus, dans certaines circonstances, ils ne sont pas si performants et ils tendent à déclencher plus de rendus dans vos composants — alors méfiez-vous de cet écueil.

En règle générale, j'essaie généralement d'utiliser les render props car c'est un motif gagnant-gagnant qui privilégie la composition.

Si vous trouvez que vous tombez dans un enfer de rappels, alors passez aux HOC comme deuxième étape.

Si vous connaissez, par exemple, React Router, vous avez facilement l'impression de savoir pourquoi **withRouter** est un **HOC** et **<Switch/> ou <Router/>** sont des composants render props. Cela dépend beaucoup du contexte dans lequel vous travaillez et de la manière dont vous voulez que le code soit expressif et fluide.

Si vous ne connaissez pas React Router, gardez tout ce que je vous ai dit à l'esprit. Ensuite, pendant que vous écrivez du code, essayez ces motifs jusqu'à ce que vous décidiez facilement lequel est le meilleur selon le contexte ou l'objectif.

Enfin, vous pouvez jouer un peu avec le code dans mon dépôt GitHub [ici](https://github.com/evedes/renderprops-pattern).

Et c'est tout le monde ! ? ? J'espère que vous avez apprécié cette petite introduction aux render props. Pour plus d'informations, veuillez consulter la bibliographie ci-dessous !

### Bibliographie

1. [Documentation React](https://reactjs.org/docs/getting-started.html)
2. [reactpatterns.com](https://reactpatterns.com)

Merci beaucoup !

evedes, Nov 2018