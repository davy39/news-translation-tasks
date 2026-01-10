---
title: Testons les composants React avec TDD, Mocha, Chai et jsdom
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-18T16:47:16.000Z'
originalURL: https://freecodecamp.org/news/simple-react-testing-d9e25ec87e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CrB6isZN6YXeM1rWmnjxHw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: Testons les composants React avec TDD, Mocha, Chai et jsdom
seo_desc: 'By Anthony Ng

  In this tutorial, we’ll learn how to write tests for React Components.

  By keeping things simple, we’ll end up with a webpack.config.js and a package.json
  file that we can still understand.

  Why I recommend Test Driven Development

  What’s ...'
---

Par Anthony Ng

Dans ce tutoriel, nous allons apprendre à écrire des tests pour les composants React.

En gardant les choses simples, nous aurons un fichier webpack.config.js et un fichier package.json que nous pouvons encore comprendre.

### Pourquoi je recommande le Développement Piloté par les Tests

Qu'est-ce qui est si important avec le Développement Piloté par les Tests (TDD) ? Il existe de nombreux articles et livres excellents sur le TDD, mais voici quelques avantages que j'en vois :

#### **Avantage #1 : Vous créez un meilleur code.**

Lorsque vous écrivez les tests en premier, vous gardez votre code concentré sur ce que vous faites.

Je me suis retrouvé dans des situations où je codais par coïncidence. Je continue à écrire du code jusqu'à ce qu'il fonctionne... en supposant que je me souvienne de l'objectif de mon code.

Le TDD vous gardera sur la bonne voie et éliminera le superflu de votre code.

#### **Avantage #2 : Vous créez un code plus propre.**

Lorsque vous avez des tests bien conçus qui passent, vous savez que vous pouvez refactoriser en toute sécurité. Combien de fois avez-vous refactorisé votre code fonctionnel, pour tout casser ensuite ?

Le TDD vous donne les signes vitaux de votre code et vous avertit lorsque quelque chose ne va pas. C'est un moyen efficace de détecter les régressions dans votre code.

#### **Avantage #3 : C'est amusant.**

Créer du code est un processus long et difficile. Il peut vous falloir un certain temps pour voir des progrès dans votre projet.

Le TDD vous donne un retour instantané que vous allez dans la bonne direction. Voir vos tests passer vous donne de petites victoires et rend le codage (pour moi, en tout cas) beaucoup plus agréable.

Notez que le TDD ne concerne pas uniquement les tests unitaires. J'aime penser au TDD comme à un état d'esprit où vous créez un code propre, concis et intentionnel. Les tests unitaires ne sont qu'un effet secondaire du TDD.

### Outils que nous allons utiliser

Tester les composants React est relativement simple car les composants React sont des fonctions pures. Lorsque vous avez des composants sans état/présentation, ce sont simplement des fonctions qui doivent retourner le même résultat étant donné certaines entrées.

#### Mocha

Pour ce tutoriel, nous allons utiliser Mocha. Assurez-vous de le télécharger globalement afin de pouvoir exécuter mocha depuis votre ligne de commande.

```
$ npm install -g mocha
```

Nous allons ajouter un script dans notre package.json pour exécuter nos tests. Notez les drapeaux supplémentaires que nous utilisons pour exécuter mocha depuis notre ligne de commande.

```
--watch // Mocha surveillera nos fichiers source et de test et relancera automatiquement les tests lorsque les fichiers changeront. --compilers // Nous utiliserons Babel pour compiler notre code ES6/JSX dans nos tests. --require // Nous exécuterons notre fichier "test_helper.js" avant que nos tests ne commencent. Notre fichier "test_helper.js" configurera un environnement DOM fictif dans Node.js dont nous aurons besoin pour tester nos composants React.
```

#### Chai

Chai est une bibliothèque d'assertion qui nous aidera à écrire nos tests dans quelque chose qui se lit plus comme l'anglais.

```
// Au lieu que nos tests se lisent comme... assert.equal(2 + 1, 3);
```

```
// ...en utilisant Chai, nous pouvons écrire... expect(2 + 1).to.equal(3);
```

#### jsdom

jsdom est une implémentation JavaScript du DOM et du HTML que nous pouvons utiliser dans Node.js.

Lorsque nous testons nos composants React, nous les monterons sur un DOM. Node.js ne vient pas avec un DOM, donc c'est là que jsdom intervient : il configure un environnement de navigateur fictif pour nous.

### Code Source

Nous avons trois composants à tester :

1. Un élément Todo qui affiche du texte.  
2. Une TodoList qui affiche une liste de composants Todo.  
3. Un composant TodoInput qui a un champ de saisie et un bouton. Ce composant appelle un callback lorsque le bouton est cliqué.

Commençons les tests.

### Tests à Exécuter

Au fait, vous pouvez voir les fichiers de test complets sur [Github](https://github.com/newyork-anthonyng/tutorials/tree/master/Simple_React_Testing/test).

#### 1. Composant Todo. Que voulons-nous tester ?

Avec ce composant, nous testerons pour voir si la balise <div> avec une classe "todo" est rendue, et si elle a rendu le texte correct.

Nous utiliserons "react-addons-test-utils" de l'équipe React dans nos tests. Il nous fournit une fonction "renderIntoDocument" pour rendre notre composant Todo dans notre faux DOM :

```
const component = renderIntoDocument(   <Todo       todo={'Promener le chien'}   />);
```

"react-addons-test-utils" nous donne également quelques outils pour parcourir notre DOM. Le premier que nous allons examiner est "findRenderedDOMComponentWithClass", qui recherchera dans notre composant un élément avec une classe "todo" :

```
const todo = findRenderedDOMComponentWithClass(component, 'todo');expect(todo).to.be.ok;
```

Maintenant, vérifions que le contenu textuel est ce que nous attendons :

```
const todoText = todo.textContent;expect(todoText).to.equal('Promener le chien');
```

Passons à la TodoList.

#### 2. Composant TodoList. Que voulons-nous tester ?

Assurons-nous que nous obtenons un composant Todo pour chaque todo.

Tout d'abord, nous allons créer un composant TodoList et passer trois éléments todo. Nous nous attendrions à ce que trois composants Todo soient créés.

Utilisons une autre méthode des utils react, "scryRenderedComponentsWithType", pour parcourir notre composant et trouver des composants enfants dont le type est d'une classe React donnée.

```
const todosEle = scryRenderedComponentsWithType(component, Todo);expect(todosEle.length).to.equal(3);
```

#### 3. Composant TodoInput. Que voulons-nous tester ?

Nous voulons tester si le champ de saisie et le bouton sont correctement rendus sur le DOM.

Les utils React nous fournissent une méthode, "findRenderedDOMComponentWithTag", qui recherche un élément avec une balise HTML donnée.

```
const inputField = findRenderedDOMComponentWithTag(component, 'input');const button = findRenderedDOMComponentWithTag(component, 'button');
```

```
expect(inputField).to.be.ok;expect(button).to.be.ok;
```

Maintenant, nous voulons tester si le bouton exécutera notre méthode de callback.

C'est là qu'il est bon d'avoir des composants sans état. Nous pouvons simuler les props de notre composant et tester que le composant fonctionne.

```
let addTodoInvoked = false;let addTodo = (todo) => { addTodoInvoked = todo };const component = renderIntoDocument(   <TodoInput       addTodo={addTodo}   />);
```

Nous passons la fonction "addTodo" en tant que callback au composant TodoInput. Chaque fois que le callback est exécuté, il doit mettre à jour la variable "addTodoInvoked" avec le texte à l'intérieur du champ de saisie.

Vous vous demandez peut-être comment nous allons cliquer sur ce bouton pour tester si le callback a été exécuté. Encore une fois, react-utils a une méthode, "Simulate", pour nous aider. "Simulate" fait ce qu'il semble faire — il simule des actions DOM (comme un "click") pour nous.

Tout d'abord, entrons une valeur dans le champ de texte. Nous faisons cela en mettant à jour la valeur du champ de saisie lui-même, puis en utilisant Simulate.change pour mettre à jour la valeur dans le DOM :

```
inputField.value = 'Tondre la pelouse';Simulate.change(inputField);
```

Ensuite, nous utiliserons Simulate.click pour cliquer sur le bouton :

```
Simulate.click(button);
```

Notre test doit vérifier que le callback a été exécuté :

```
expect(addTodoInvoked).to.equal('Tondre la pelouse');
```

Et c'est tout — nous venons de tester des composants React sans état. Maintenant, il est plus simple de configurer des tests et de simuler des callbacks, puisque nous avons gardé nos fonctions pures.

### Tester les Reducers

Si nous voulions utiliser Redux, nous pourrions tester les reducers de manière similaire, puisqu'ils sont également des fonctions pures.

Cela est en fait encore plus facile que de tester les composants React, car les états sont simplement des types de données JavaScript vanilla. Nous n'avons pas besoin d'utilitaires supplémentaires comme nous l'avons fait pour les composants React.

Supposons que nous avons un reducer dans notre projet, comme ci-dessous :

```
const initialState = [];
```

```
const reducer = (state = initialState, action) => {   let newTodos;
```

```
switch(action.type) {   case 'ADD_TODO':     newTodos = state.slice();     newTodos.push(action.data);     return newTodos;   default:     return state;   };
};
```

Pour tester cela, nous devons stub un état initial et une action. Un exemple de test ressemblerait à ce qui suit :

```
const initialState = ['Tondre la pelouse'];const action = {   type: 'ADD_TODO',   data: 'Promener le chien'};const nextState = reducer(initialState, action);
```

```
expect(nextState).to.deep.equal(['Tondre la pelouse', 'Promener le chien']);
```

### Tester AJAX

Travailler avec des appels AJAX est une autre fonctionnalité courante que vous pourriez vouloir tester.

Je recommande d'utiliser "axios" pour vos besoins AJAX. Axios est un client HTTP que vous pouvez utiliser dans le navigateur ou avec Node.js. Cela signifie que vous aurez une API cohérente, peu importe d'où vous effectuez vos appels AJAX.

Une requête GET de base dans axios ressemblerait à ceci :

```
axios.get('myUrl');
```

Il existe différentes approches pour tester cela. Pour ce tutoriel, nous allons utiliser "sinon", une bibliothèque de test qui nous donne de nombreuses fonctions utilitaires de test. C'est similaire à ce que react-addons-test-utils a fourni.

Nous allons examiner une méthode appelée "stub", qui nous permettra de voir des informations sur une méthode, comme le nombre de fois où la méthode a été appelée.

Notre code pour vérifier que nous utilisons axios pour faire une requête ressemblerait à ceci :

```
// stub sur la méthode axios.get() pour voir combien de fois elle a été appelée sinon.stub(axios, 'get');
```

```
// faire une requête en utilisant axios.get() utility.makeAjax();
```

```
// s'attendre à ce que axios.get() ait été appelé une fois expect(axios.get.callCount).to.equal(1);
```

Sinon nous donne beaucoup de fonctionnalités, y compris des espions, des mocks, et la création de faux XMLHttpRequests et de faux serveurs.

Lorsque vous commencez, soyez conscient de l'endroit où vous exécutez vos tests (navigateur vs Node.js). Si vous exécutez vos tests dans Node.js (comme nous l'avons fait dans ce tutoriel), notez que vous n'aurez pas accès à XMLHttpRequest et à d'autres objets du navigateur parce que... eh bien... vous n'êtes pas dans un navigateur.

Certaines des fonctionnalités de sinon s'attendent à un environnement de navigateur. Si c'est le cas, vous pourriez vouloir envisager d'exécuter vos tests via un navigateur.

Vous pourriez également regarder [Karma](https://karma-runner.github.io/1.0/index.html) pour exécuter vos tests via un navigateur headless à travers votre ligne de commande.

Avez-vous des questions ? Faites-vous des tests différemment ? N'hésitez pas à commenter ci-dessous.

Consultez certains de mes autres articles sur les tests.

[Tester l'état des composants React](https://medium.com/@newyork.anthonyng/testing-react-components-state-b57bfc712b90)