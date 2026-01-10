---
title: Comment apporter de la réactivité dans React avec les états
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T19:26:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yVuEqJEkG2-r_gKzdLHl5g.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment apporter de la réactivité dans React avec les états
seo_desc: 'By Jérémy Bardon


  This is part of my “React for beginners” series on introducing React, its core features
  and best practices to follow. More articles are coming!

  < Previous | Next >


  If you know how to display a React component — that’s great. Now, l...'
---

Par Jérémy Bardon

> Cela fait partie de ma série "React pour débutants" sur l'introduction à React, ses fonctionnalités principales et les meilleures pratiques à suivre. D'autres articles arrivent !

> [< Précédent](https://www.freecodecamp.org/news/p/2994c09b-d550-4eb6-b281-a83e553240c7/) | [Suivant >](https://www.freecodecamp.org/news/the-beginners-collection-of-powerful-tips-and-tricks-for-react-f2e3833c6f12/)

Si vous savez [comment afficher un composant React](https://medium.freecodecamp.org/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44) — c'est génial. Maintenant, donnons à nos composants leurs propres données.

**Avertissement :** Cet article se concentre sur l'état intégré de React. Notez que l'état du composant et Redux ne sont pas incompatibles, car leur but est différent.

À mon avis, l'état du composant est spécifique à la portée du composant (pour la complétion de formulaires). De plus, l'état Redux aide à partager le même état parmi de nombreux composants.

### Ai-je besoin d'un état ?

Pour apprendre les états, créons un composant `Question`. Il affichera une question oui/non et demandera une réponse.

```js
class Question extends React.Component {
  constructor(props) { // Init props et state
      super(props);
      this.state = { answered: false };
      this.answerQuestion = this.answerQuestion.bind(this);
  }
  answerQuestion({target}){ // Mise à jour de l'état (l'utilisateur répond à la question)
      let answer = target.value === 'true' ? true : false;
      this.setState({ answered: true, answer });
  }
  render() { // Modèle du composant en JSX
    if(this.state.answered) {
      return <p>Vous avez déjà répondu à cette question ({this.state.answer ? 'oui' : 'non'})</p>
    }
    return (
      <p>
        <span>{this.props.label}</span>
        <label><input type="radio" name="answer" value="true" onChange={this.answerQuestion}/>Oui</label>
        <label><input type="radio" name="answer" value="false" onChange={this.answerQuestion}/>Non</label>
      </p>
    );
  }
}
```

Notre composant `Question` contient seulement trois fonctions :

* `_constructor_` pour l'initialisation (props et state),
* `_answerQuestion_` est un callback déclenché lorsque l'utilisateur répond
* `render` que vous connaissez probablement déjà — il génère le modèle du composant.

Ce composant a deux états distincts. La question n'est pas répondue, ou la question a une réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PH4UwIimwdmSGGCS.png)

Les props sont uniquement utilisées pour l'étiquette de la question, et surtout, le but de l'**état** est bien plus intéressant.

L'état est la mémoire du composant qui se souvient si la question a une réponse. Si c'est le cas, il connaît également la réponse.

### Transformer l'état en props

Utiliser un état dans un composant est facile. Vous devez initialiser l'état et appeler la fonction `setState` chaque fois que vous voulez mettre à jour son contenu.

Imaginez être un composant. Si votre état change, votre réaction serait de vérifier si vous devez mettre à jour votre affichage.

C'est ainsi que cela fonctionne. React appelle `shouldComponentUpdate` avant d'appeler `render` ([voir la documentation](https://reactjs.org/docs/react-component.html#shouldcomponentupdate)). Cette deuxième fonction générera le prochain état du Virtual DOM ([mon dernier article](https://medium.freecodecamp.org/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44) en parle).

```js
class Survey extends React.Component { 
  // Quelque part dans la fonction constructor
  this.state = { 
    questions: [ 'Aimez-vous les bananes ?', 'Êtes-vous un développeur ?' ]
  };
  // Quelque part dans la fonction render 
  this.state.questions.map(question => <Question label={question}/>)
}
```

Les composants reçoivent des props d'autres composants. Si ces props changent, alors le composant sera mis à jour.

En fait, vous savez déjà comment cela fonctionne — mais prenons l'exemple d'un `Survey` contenant quelques `Question`.

Le `Survey` contient les étiquettes des questions dans son état et les donne à `Question` en tant que propriété.

Lorsque le `Survey` met à jour son état (appelle `setState`), la fonction `render` est déclenchée. Si c'est le cas, elle envoie une demande de rendu pour `Question` ([détails dans la doc React](https://reactjs.org/docs/optimizing-performance.html#avoid-reconciliation)).

### Adopter le modèle de conteneur

Découpler la vue et le reste du code a toujours été une grande préoccupation parmi les développeurs. C'est pourquoi la plupart des modèles de conception utilisés dans les frameworks étendent le modèle MVC.

Si vous utilisez React avec Redux, vous connaissez déjà le modèle **conteneur**. En fait, c'est une fonctionnalité intégrée de Redux via la fonction connect.

```js
/* 
  Question et QuestionContainer sont tous deux des composants React réguliers
  QuestionContainer rend un seul composant Question 
  et fournit l'accès aux éléments redux via les props
*/
const QuestionContainer = 
  connect(mapStateToProps, mapDispatchToProps)(Question);
```

Il est temps de diviser le composant `Question` en deux composants.

`Question` sera responsable du rendu des props. Ce type de composant est appelé soit fonctionnel, de présentation, ou un composant dumb.

`QuestionContainer` gérera la gestion de l'état.

```js
const Question = (props) => 
  <p>
    <span>{props.label}</span>
    <label><input type="radio" name="answer" value="true" onChange={props.answerQuestion}/>Oui</label>
    <label><input type="radio" name="answer" value="false" onChange={props.answerQuestion}/>Non</label>
  </p>
        
class QuestionContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = { answered: false };
    this.answerQuestion = this.answerQuestion.bind(this);
  }
  answerQuestion({target}){
    let answer = target.value === 'true' ? true : false;
    this.setState({ answered: true, answer });
  }
  render() {
    if(props.answered) {
      return <p>Vous avez déjà répondu à cette question (props.answer ? 'oui' : 'non'})</p>
    }
    // Voici l'astuce
    return <Question label={this.props.label} answerQuestion={this.answerQuestion}/>
  }
}
```

Pour comparaison avec le modèle de conception MVC, `Question` est une **Vue** et `QuestionContainer` est un **Contrôleur**.

D'autres composants qui ont besoin de `Question` utiliseront maintenant `QuestionContainer` au lieu de `Question`. Cette considération est assez acceptée dans la communauté.

### Attention à l'anti-pattern setState

Utiliser `setState` est assez simple.

Passez le prochain état comme premier et seul paramètre. Il mettra à jour les propriétés de l'état actuel avec les nouvelles valeurs passées.

```js
// Très mauvaise pratique : n'utilisez pas this.state et this.props dans setState !
this.setState({ answered: !this.state.answered, answer });

// Avec des états assez grands : la tentation devient plus grande 
// Ici, gardez l'état actuel et ajoutez la propriété answer
this.setState({ ...this.state, answer });
```

En résumé, n'utilisez pas `this.state` et `this.props` à l'intérieur des appels `setState`.

Ces variables peuvent ne pas avoir les valeurs que vous attendez. React optimise les changements d'état. Il écrase plusieurs changements en un seul pour des raisons de performance (avant les optimisations du Virtual DOM).

```js
// Notez la notation () autour de l'objet qui fait que le moteur JS
// évalue comme une expression et non comme le bloc de la fonction fléchée
this.setState((prevState, props) 
              => ({ ...prevState, answer}));
```

Vous devriez préférer l'autre forme de `setState`. Fournissez une fonction comme seul paramètre et utilisez les paramètres `prop` et `state` ([voir la documentation](https://reactjs.org/docs/state-and-lifecycle.html#state-updates-may-be-asynchronous)).

### Le composant de sondage complet

Dans cet article, nous avons couvert les principales utilisations de l'état dans React. Vous pouvez trouver le code complet pour le composant `Survey` dans le Codepen suivant.

%[https://codepen.io/jbardon/pen/RQedrv]

C'était tout sur les états. Vous avez rencontré des composants, des props et des états, et maintenant vous avez le kit de débutant pour jouer avec React.

J'espère que vous avez apprécié la lecture de cet article et appris beaucoup de choses !

**Si vous avez trouvé cet article utile, veuillez cliquer sur le bouton** ? **plusieurs fois pour aider les autres à trouver l'article et montrer votre soutien ! ?**

**N'oubliez pas de me suivre pour être informé de mes prochains articles** ?

> Cela fait partie de ma série "React pour débutants" sur l'introduction à React, ses fonctionnalités principales et les meilleures pratiques à suivre.

> [< Précédent](https://www.freecodecamp.org/news/p/2994c09b-d550-4eb6-b281-a83e553240c7/) | [Suivant >](https://www.freecodecamp.org/news/the-beginners-collection-of-powerful-tips-and-tricks-for-react-f2e3833c6f12/)

### Consultez mes [autres](https://medium.com/@jbardon/latest) articles

#### ➡ JavaScript

* [Comment améliorer vos compétences en JavaScript en écrivant votre propre framework de développement web](https://medium.freecodecamp.org/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190) ?
* [Erreurs courantes à éviter lors de l'utilisation de Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)

#### ➡ Astuces et conseils

* [Arrêtez le débogage JavaScript douloureux et adoptez Intellij avec Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [Comment réduire les bundles JavaScript énormes sans effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)