---
title: Comment développer vos superpouvoirs React avec le motif HOC
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T20:35:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-your-react-superpowers-with-the-hoc-pattern-61293651d59
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca70d740569d1a4ca7491.jpg
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
seo_title: Comment développer vos superpouvoirs React avec le motif HOC
seo_desc: 'By Eduardo Vedes

  Hey everyone! ? I hope you had a Merry, Merry Christmas and a Happy New Year!

  2018 has reached its end and it makes sense for me to start the new year with an
  article about Higher-Order Components!

  I’ve promised you to write about it...'
---

Par Eduardo Vedes

Salut à tous ! ? J'espère que vous avez passé un joyeux, joyeux Noël et une bonne année !

2018 a atteint sa fin et il est logique pour moi de commencer la nouvelle année avec un article sur les composants d'ordre supérieur !

Je vous ai promis d'écrire à ce sujet depuis que nous avons abordé le sujet lorsque nous avons parlé des props de rendu et des motifs de conteneur, il est donc logique d'approfondir un peu et de prêter attention à cela !

Personnellement, ce n'est pas l'un de mes motifs préférés, mais c'est un outil puissant à connaître, maîtriser et ajouter à votre ceinture à outils.

Gardez simplement à l'esprit que vous ne devez pas en abuser. Presque tout ce que vous pouvez encapsuler dans un HOC, vous pouvez certainement l'implémenter en utilisant le motif des props de rendu — vérifiez mon article sur les props de rendu [ici](https://medium.freecodecamp.org/how-to-develop-your-react-superpowers-with-the-render-props-pattern-b74e68c6d053) — et vice-versa.

### 01. Qu'est-ce qu'un composant d'ordre supérieur ?

Un composant d'ordre supérieur (HOC) est une technique avancée dans React pour réutiliser la logique des composants. Les HOC ne font pas partie de l'API React. Ils sont un motif qui découle de la nature de React qui privilégie la composition sur l'héritage.

JavaScript est un langage bien adapté à la programmation fonctionnelle car il peut accepter des fonctions d'ordre supérieur. Une fonction d'ordre supérieur est une fonction qui peut prendre une autre fonction comme argument et/ou qui retourne une fonction comme résultat.

De la même manière, un **composant d'ordre supérieur** est une fonction qui **prend (enveloppe) un composant et retourne un nouveau composant**.

Les fonctions d'ordre supérieur nous permettent d'abstraire des actions, et pas seulement des valeurs.

Les HOC sont courants dans les bibliothèques React tierces, telles que Redux ou React Router. Je parie que vous en avez utilisé certains, peut-être sans en être conscient.

Le but principal d'un composant d'ordre supérieur dans React est de partager des fonctionnalités communes entre les composants sans répéter de code.

### 02. Types de composants d'ordre supérieur

En gros, il existe deux principaux types de mise en œuvre de HOC : **Props Proxy** et **Inheritance Inversion**.

#### Props Proxy (ppHOC)

Les HOC Props Proxy sont élémentairement exprimés comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/mT3fcX7TeDvnJTfpgaBCFa-2cCYebKgfSHps)
_propsProxyHOC (implémentation standard)_

Ce n'est rien de plus qu'une fonction, propsProxyHOC, qui reçoit un composant comme argument (dans ce cas, nous avons appelé l'argument WrappedComponent) et retourne un nouveau composant avec le WrappedComponent à l'intérieur.

Gardez à l'esprit que lorsque nous retournons le WrappedComponent, nous passons également les props que le HOC reçoit. Cela explique le nom donné à ce type : **props proxy**.

Lorsque nous retournons le Wrapped Component, nous avons la possibilité de manipuler les props et d'abstraire l'état, même en passant l'état comme une prop dans le Wrapped Component.

Vous pouvez également envelopper le Wrapped Component avec d'autres éléments JSX en changeant son UI selon les besoins de votre application.

Les HOC Props Proxy sont utiles dans les situations suivantes :

1. Manipulation des props
2. Accès à l'instance via les Refs (soyez prudent, [évitez d'utiliser les refs](https://reactjs.org/docs/refs-and-the-dom.html))
3. Abstraction de l'état
4. Enveloppement/Composition du WrappedComponent avec d'autres éléments

#### Inheritance Inversion (iiHOC)

Les HOC Inheritance Inversion sont élémentairement exprimés comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Wra7dgCf7jTWM51gKNERjEHIeyygj0wipllh)
_inheritanceInversionHOC (implémentation standard)_

Dans cette situation, la classe retournée **étend** le WrappedComponent. Il est appelé Inheritance Inversion, car au lieu que le WrappedComponent étende une classe Enhancer, il est étendu passivement. De cette manière, la relation entre eux semble **inverse**.

L'Inheritance Inversion donne au HOC l'accès à l'instance du WrappedComponent via _this_, ce qui signifie que vous pouvez utiliser l'état, les props, le cycle de vie du composant et **même la méthode de rendu**.

Les HOC Inheritance Inversion sont utiles pour les situations suivantes :

1. Détournement de rendu
2. Manipulation de l'état

### 03. Mettons les mains dans le cambouis

D'accord tout le monde ? pour illustrer un peu les concepts présentés ci-dessus, faisons un peu de code.

Si vous voulez jouer plus tard avec le code que nous faisons, vous pouvez le récupérer ici depuis ce [dépôt](https://github.com/evedes/higher-order-components) à moi ?.

Essayons d'implémenter un composant qui retourne un message de bienvenue selon l'utilisateur qui est connecté au système.

![Image](https://cdn-media-1.freecodecamp.org/images/YcaqLE7b82RUK5xZVvIKaSngnecv94UCeQ1G)
_composant principal App.js_

J'ai modifié mon composant App.js pour afficher du texte et pour rendre un composant appelé Welcome auquel je passe la prop user.

Ok, nous pouvons faire cela avec un simple composant comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/gJJJLEEcQg1UI93W-9JjxutVqpz6hZARjQIv)
_Composant Welcome_

Mais...

Que faire si je veux que le composant retourne Welcome Guest si aucun utilisateur n'est connecté ?

Eh bien... Je peux faire cela dans le même composant Welcome, avec un simple if qui vérifie si la prop user existe et si ce n'est pas le cas, il retourne simplement "Welcome Guest".

Mais supposons que je veux encapsuler cette logique pour l'utiliser avec plusieurs / différents composants Welcome.

Donc, la solution est de créer un HOC Props Proxy :

![Image](https://cdn-media-1.freecodecamp.org/images/yyE5v1YvE9NmKyYI2jCqq8GQDZ09iUoV2kRP)
_propsProxy HOC_

Qu'avons-nous fait ici ? Nous avons gardé notre composant Welcome simple et nous avons créé une fonction JavaScript appelée withUser qui prend le composant Welcome (WrappedComponent) comme argument et vérifie si la prop user existe. Si ce n'est pas le cas, il retourne simplement un message "Welcome Guest !".

C'est très utile. Imaginez que vous avez 30 composants Welcome dans différentes langues (exemple idiot mais cela illustre l'encapsulation de la logique dans un HOC).

Bien, donc maintenant nous avons un HOC pour vérifier s'il y a un utilisateur connecté, sinon il affiche un message Welcome Guest !

Imaginons maintenant que les informations de l'utilisateur proviennent d'une API externe (Auth0 par exemple) et arrivent dans notre application frontend via un réducteur Redux qui gère l'état de l'application.

Donc, avant de vérifier s'il y a un utilisateur, nous devons vérifier si les données sont chargées dans le système !

Wow ! De cette manière, nous pourrions afficher un message de chargement pendant que les données ne sont pas chargées !

Donc... pour ce cas d'utilisation, je suppose que nous voulons faire un peu de détournement de rendu et rendre autre chose si les données ne sont pas chargées.

Pour le détournement de rendu, nous devons utiliser un iiHOC. Wow ! Quelle coïncidence ! Donc, faisons-le et composons les deux HOC ensemble tout le monde ? Cela va frapper fort sur le clou.

![Image](https://cdn-media-1.freecodecamp.org/images/AMxMlFa26czQe0fX2rqOira-XunoS2rDeGyE)
_propsProxy + inheritanceInversion HOCs composés_

Faites attention à ce que nous avons fait :

Nous avons créé un withLoader iiHOC qui étend le WrappedComponent. De cette manière, il peut accéder à ses props et déclencher différents rendus.

Dans cette situation, nous obtenons la prop isLoaded et si elle n'est pas chargée, nous retournons simplement un message de chargement ! Sinon, nous laissons le WrappedComponent se rendre en retournant simplement super.render().

Dans l'instruction export, nous composons simplement deux fonctions JavaScript telles que f1(f2(f3)). Rien de plus que cela !

Il existe des outils pour composer des fonctions de manière plus élégante, mais c'est une autre histoire pour un autre article !

### 04. Dernier point mais non des moindres

J'ai essayé d'utiliser des exemples simples pour que vous compreniez les concepts de la manière la plus claire possible.

Mon conseil pour vous est que si vous ne maîtrisez pas ces concepts, veuillez tirer mon dépôt [ici](https://github.com/evedes/higher-order-components) et jouer un peu avec.

Vérifiez le code et essayez de le comprendre ligne par ligne.

Il faut un certain temps pour s'habituer et se sentir à l'aise avec ce type d'abstraction, alors ne perdez pas votre motivation ou votre concentration avec les HOC.

De plus, comme je l'ai dit auparavant, tout ce que nous avons fait ici peut être atteint avec les props de rendu ou le motif de conteneur, donc ce n'est pas une obligation de choisir un HOC ou deux pour faire du code propre avec ce type d'encapsulation !

J'espère que vous avez eu autant de plaisir à lire cet article que j'en ai eu à l'écrire ! Si vous l'avez vraiment apprécié, donnez-moi quelques applaudissements (pas moins de 50 s'il vous plaît) ? et n'oubliez jamais de "Rester fort et continuer à coder !".

De plus, si vous voulez des explications plus approfondies et complexes, n'hésitez pas à lire les liens que j'ai ajoutés à la section Bibliographie ci-dessous ?

### 05. Bibliographie

1. [Documentation React](https://reactjs.org/docs/getting-started.html)

2. [Eloquent JavaScript](https://eloquentjavascript.net/)

3. [React Higher Order Components in depth](https://medium.com/@franleplant/react-higher-order-components-in-depth-cf9032ee6c3e)

Merci beaucoup !

evedes, Déc 2018