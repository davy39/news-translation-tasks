---
title: Ce que j'ai appris en créant ma première application React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-24T08:38:40.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-from-my-first-react-app-3c4ebb740399
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z2OuKxUwqnO-o8i7D8UxYQ.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Ce que j'ai appris en créant ma première application React
seo_desc: 'By ellereeeee

  I’m going to share the things I wish I knew, wish I had done, or was glad I did
  when I made my first React app. It’s a Pomodoro Clock, or a productivity timer.
  I built it for a freeCodeCamp project and to practice the React I learned fo...'
---

Par ellereeeee

Je vais partager les choses que j'aurais aimé savoir, que j'aurais aimé faire ou que j'étais content d'avoir faites lorsque j'ai créé ma première application React. C'est une horloge Pomodoro, ou un minuteur de productivité. Je l'ai construite pour un projet [freeCodeCamp](https://www.freecodecamp.org/) et pour pratiquer React dans le cadre d'une cohort de [Chingu](https://chingu.io/).

Vous pouvez la voir en direct [ici](https://ellereeeee-pomodoro-clock.netlify.com/), et le code est [ici](https://github.com/ellereeeee/pomodoro-clock).

J'espère pouvoir aider certains débutants en React.

### Lire la documentation React

Si vous commencez tout juste à apprendre React, commencez par les [docs officiels](https://reactjs.org/docs/hello-world.html). En ce qui concerne les docs, celles de React sont faciles à comprendre et fournissent de nombreux exemples.

Ne faites pas ce que j'ai fait et ne commencez pas par un tutoriel React. J'ai commencé avec le [Guide du Débutant pour React](https://egghead.io/courses/the-beginner-s-guide-to-react) de egghead.io ("Débutant" est un nom impropre à mon avis) et c'était difficile. Pour être honnête, j'ai entendu dire que egghead.io est destiné aux développeurs plus expérimentés cherchant à se mettre à niveau avec un nouveau framework.

J'ai définitivement appris beaucoup, mais il y avait beaucoup de pauses dans les vidéos, de retours en arrière de 10 secondes pour entendre une explication encore et encore, et de simples regards sur le code en se sentant perdu. Les choses ont finalement cliqué, mais je ne peux m'empêcher de penser que j'aurais été mieux de commencer par les docs officiels puis de consulter un tutoriel.

Je suis sûr que vous pouvez trouver un tutoriel plus adapté aux débutants. Cependant, regarder les docs officiels en premier est une bonne pratique et je pense que vous serez mieux lotis dans le cas de l'apprentissage de React.

### Connaître JavaScript ou être prêt à apprendre

Regardez ce court extrait de code :

```
class Counter extends React.Component {  constructor(props) {    super(props)    this.state = {count: 0}    this.handleClick = this.handleClick.bind(this)  }
```

Ci-dessus, nous avons une déclaration de classe ES6 (qui n'est que du sucre syntaxique pour l'héritage prototypal). Qu'est-ce que l'héritage prototypal ? Que sont les fonctions `constructor` et `super` ? Pourquoi faisons-nous un binding dur de `handleClick` à `this` ? Connaissez-vous quelque chose sur la portée lex-time en JavaScript ?

Maintenant, vous n'avez pas besoin de connaître les réponses à ces questions pour créer quelque chose en React. Vous pourriez simplement supposer que vous avez besoin de tel ou tel morceau de code pour faire fonctionner les choses et en rester là. Cependant, je pense qu'il est important de comprendre les choses à un niveau plus profond.

Ce modèle de code est le pain et le beurre de React. Ne voulez-vous pas savoir ce qui se passe ?

Ce n'est qu'un exemple dans React où vous aurez besoin d'une connaissance décente de JavaScript.

Connaissez-le bien, ou soyez prêt à apprendre.

### Pensez en React

Concevez votre application sous forme de wireframe ou de maquettes et décomposez-la en composants. Cela rendra le processus de codage beaucoup plus fluide.

Par exemple, j'ai commencé avec cette maquette.

![Image](https://cdn-media-1.freecodecamp.org/images/gngLwubDKZ5fad4lRVQXmLdQUS48wzvPByqV)

J'ai changé certaines choses dans mon application finale, mais en regardant la maquette, vous pouvez voir :

1. l'application orange englobant tout

2. un bouton d'information en haut à gauche

3. un bouton d'historique pour les tâches terminées en haut à droite

4. un message/entrée au centre en haut

5. un minuteur radial, une horloge, et des boutons haut et bas au centre

6. un bouton de lecture au centre en bas

Ensuite, j'ai séparé mon interface utilisateur en composants. Chaque partie doit représenter une fonction ou une donnée.

![Image](https://cdn-media-1.freecodecamp.org/images/zdebvVFnZctVdhdofTvq-iCRy-bt767ovFgd)

À partir de cela, j'ai pu organiser mes composants dans une hiérarchie :

![Image](https://cdn-media-1.freecodecamp.org/images/Y-83Lzbd2RRQkovtab-w-8WfVHImCByxG-lp)

Assez simple. Tout est imbriqué dans le composant PomodoroTimer. L'important ici est d'illustrer où l'état doit être. L'état doit être à un seul endroit dans React et "descendre" vers les composants imbriqués. J'ai décidé qu'il devait être dans le composant PomodoroTimer.

J'aurais pu avoir l'état `time` dans le composant Timer. Cependant, je veux changer la couleur de PomodoroTimer en bleu si l'utilisateur fait une pause. Cela signifie que j'aurai un état `timerType` qui change la couleur de fond et aussi le temps initial (25 minutes pour travailler et 5 minutes pour se reposer).

Le flux de données est plus direct si j'ai à la fois l'état `timerType` et l'état `time` dans PomodoroTimer et que je transmets `time` à Timer. `timerType` passerait de `"Pomodoro"` à `"Rest"` une fois que `time` atteint 0. Il est plus facile de comprendre comment l'état circule dans mon application s'il est tout au même endroit. Cela facilite également le débogage.

Consultez l'article ["Penser en React"](https://reactjs.org/docs/thinking-in-react.html) des docs officiels de React pour une explication plus détaillée sur la création d'une application React, de la maquette à l'application finale.

### Vérifiez la console pour les erreurs

J'ai fait une grosse erreur dans mon code, et je l'aurais repérée si j'avais vérifié la console pour les erreurs. Vous devriez toujours faire cela, quel que soit le langage ou le framework dans lequel vous codez.

On m'a signalé l'erreur après avoir posté mon code sur des forums pour révision :

```
./src/components/PomodoroTimer.jsx  Ligne 17 :   Ne modifiez pas l'état directement. Utilisez setState()  react/no-direct-mutation-state  Ligne 21 :   Ne modifiez pas l'état directement. Utilisez setState()  react/no-direct-mutation-state
```

Cela signifie que je modifiais l'état directement, ce qui est un grand non-non dans React.

J'ai donc changé mon code de ceci :

```
handleIncrementTime = () => {    this.setState({ state: (this.state.time += 300000) });  };  handleDecrementTime = () => {    if (this.state.time > 300000) {      this.setState({ time: (this.state.time -= 300000) });    }  };
```

à ceci :

```
handleIncrementTime = () =>    this.setState(prevState => ({ time: (prevState.time + 300000) }));  handleDecrementTime = () => {    if (this.state.time > 300000) {      this.setState(prevState => ({ time: (prevState.time - 300000) }));    }  };
```

J'avais besoin d'utiliser la deuxième forme de `setState` pour mettre à jour l'état. Passez une fonction à `setState` qui utilise l'argument `prevState` pour mettre à jour l'état. Vous pouvez lire à propos de la deuxième forme de `setState` [ici](https://reactjs.org/docs/state-and-lifecycle.html).

### TL;DR

1. Si vous apprenez React, commencez par les docs React.
2. Connaissez bien JavaScript ou soyez prêt à apprendre.
3. Prenez le temps de planifier votre application. Décomposez votre interface utilisateur en composants et réfléchissez à l'endroit où l'état résidera.
4. Vérifiez la console pour les erreurs.

J'ai eu beaucoup de plaisir à coder ma première application React et j'espère que vous aussi. Bonne chance !

Merci à l'utilisateur Reddit codethesite pour m'avoir aidé à [refactoriser mes opérateurs d'assignation de gestionnaires](https://www.reddit.com/r/reactjs/comments/8tinqo/lessons_learned_from_my_first_react_app/e18vqtw/)!