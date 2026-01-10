---
title: Comment mettre à jour une prop d'un composant dans ReactJS — oh oui, c'est
  possible
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-17T05:37:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-update-a-components-prop-in-react-js-oh-yes-it-s-possible-f9d26f1c4c6d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Rzaf_TyulUee7xEdDs3bRw.png
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
seo_title: Comment mettre à jour une prop d'un composant dans ReactJS — oh oui, c'est
  possible
seo_desc: 'By Dheeraj DeeKay

  If you have read the official React docs (and you should, as it is one great resource
  on React) you’d notice [these lines](http://this.props.onNameChanged(''New name'')):


  Whether you declare a component as a function or a class, it m...'
---

Par Dheeraj DeeKay

Si vous avez lu la documentation officielle de React (et vous devriez, car c'est une excellente ressource sur React), vous auriez remarqué [ces lignes](http://this.props.onNameChanged('New name')):

> Que vous déclariez un composant [comme une fonction ou une classe](https://reactjs.org/docs/components-and-props.html#function-and-class-components), il ne doit jamais modifier ses propres props.  
> React est assez flexible, mais il a une règle stricte :  
> **Tous les composants React doivent se comporter comme des fonctions pures par rapport à leurs props.**

Les props ne doivent jamais être mises à jour. Nous devons les utiliser telles quelles. Cela semble rigide, n'est-ce pas ? Mais React a ses raisons derrière cette règle et je suis assez convaincu par leur raisonnement. Le seul bémol est que, parfois, nous pourrions avoir besoin d'initier la mise à jour d'une prop. Et nous allons bientôt savoir comment.

Considérez la ligne de code suivante d'un composant parent :

`<MyChild childName={this.state.parentName}` />

Il s'agit d'une ligne simple avec laquelle chaque développeur React est probablement familier. Vous appelez un composant enfant. En faisant cela, vous passez également l'état du parent (`parentName`) à l'enfant. Dans le composant enfant, cet état sera accessible via `this.props.childName`. C'est bien.

Maintenant, si un changement de nom est nécessaire, `parentName` sera modifié dans le parent et ce changement sera automatiquement communiqué à l'enfant, comme c'est le cas avec le mécanisme de React. Cette configuration fonctionne dans la plupart des scénarios.

Mais que faire si vous devez mettre à jour la prop du composant enfant, et que la connaissance du changement requis et le déclencheur pour le changer ne sont connus que de l'enfant ? En considérant les méthodes de React, les données ne peuvent circuler que de haut en bas, c'est-à-dire du parent à l'enfant. Alors, comment communiquer au parent qu'un changement de prop est nécessaire ?

Eh bien, bien que cela soit un anti-pattern et non recommandé, les développeurs qui ont écrit le langage nous ont couvert. Surprise !

Nous pouvons le faire avec des Callbacks. Je sais, pas de surprise là ! Ils semblent venir à bout de chaque problème que nous rencontrons ici. D'accord, d'accord, mais comment ?

![Image](https://cdn-media-1.freecodecamp.org/images/zdcDnVK0Okw3GBfFb8vzE3Ofi0uKUpD5KRRN)

Imaginez si l'appel ci-dessus à l'enfant était modifié de cette manière :

`<MyChild childName={this.state.parentName} onNameChange={this.onChange}` />

Maintenant, en plus d'une prop `childName`, notre enfant besoin a également un événement appelé `onNameChange` exposé. C'est la façon de résoudre le problème. Notre enfant a fait sa part. Maintenant, c'est au tour du parent de faire ce qui est requis. Et il n'a pas à s'inquiéter. Tout ce qu'il a à faire est de définir une fonction `onChange` comme suit :

```
function onChange(newName) {   this.setState({ parentName: newName });}
```

C'est tout. Maintenant, chaque fois et partout dans le composant enfant où nous souhaitons mettre à jour la prop `parentName`, tout ce que nous avons à faire est d'appeler `this.props.onNameChange('Mon Nouveau nom')` et voilà ! Vous aurez ce que vous désirez. C'est tout. Fini.

J'espère que c'était facile à comprendre. Faites-moi savoir dans les commentaires si vous avez des difficultés ou des façons différentes de rendre cela plus facile. Merci.

**_Une dernière chose._**

React s'oppose à cela et ils ont tout à fait raison. C'est un anti-pattern. Donc, chaque fois que vous vous trouvez dans une situation comme celle-ci, vérifiez si vous pouvez remonter votre état ou s'il existe un moyen de décomposer votre composant. Cela peut sembler un peu fastidieux, mais sachez que c'est ainsi que cela est censé être dans React !

Bon codage.