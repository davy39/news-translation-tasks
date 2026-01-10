---
title: La collection de conseils et astuces puissants pour les débutants en React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-24T18:13:15.000Z'
originalURL: https://freecodecamp.org/news/the-beginners-collection-of-powerful-tips-and-tricks-for-react-f2e3833c6f12
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s9b85nv7ZKzqxCkg6ps0QA.jpeg
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
seo_title: La collection de conseils et astuces puissants pour les débutants en React
seo_desc: 'By Jérémy Bardon


  This is part of my “React for beginners” series on introducing React, its core features
  and best practices to follow. More articles are coming!

  << Start over | < Previous


  As you can tell from the title of this article, it’s aimed a...'
---

Par Jérémy Bardon

> Ceci fait partie de ma série "React pour les débutants" sur l'introduction à React, ses fonctionnalités principales et les meilleures pratiques à suivre. D'autres articles arrivent !

> [<< Recommencer](https://www.freecodecamp.org/news/p/2994c09b-d550-4eb6-b281-a83e553240c7/) | [< Précédent](https://www.freecodecamp.org/news/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4/)

Comme vous pouvez le voir d'après le titre de cet article, il est destiné aux débutants.

En fait, j'ai commencé à apprendre React il y a quelques mois. Lire la documentation React, les projets open source et les articles Medium m'a beaucoup aidé.

Sans aucun doute, je ne suis pas un expert en React. Et donc je lis beaucoup sur ce sujet. De plus, construire de petits projets m'a aidé à mieux connaître React. En cours de route, j'ai adopté certaines bonnes pratiques — et je veux les partager avec vous ici. Alors commençons.

### Nommez vos composants

Pour identifier quel composant a un bug, il est important de toujours donner un nom à votre composant.

D'autant plus lorsque vous commencez à utiliser React Router ou des bibliothèques tierces.

```js
// Évitez ces notations
export default () => {};
export default class extends React.Component {};
```

Il y a un débat sur l'utilisation d'un import par défaut ou nommé. Notez qu'un **import par défaut** ne garantit pas que le nom du composant soit cohérent dans le projet. De plus, le [tree-shaking](https://en.wikipedia.org/wiki/Tree_shaking) sera moins efficace.

#### Peu importe comment vous exposez votre composant, nommez-le

Vous devez définir le nom de la classe ou le nom de la variable (pour les composants fonctionnels) qui héberge le composant.

React va en fait [inférer le nom du composant](https://reactjs.org/docs/react-component.html#displayname) à partir de celui-ci dans les messages d'erreur.

```js
export const Component = () => <h1>Je suis un composant</h1>;
export default Component;

// Définir un nom personnalisé pour le composant
Component.displayName = 'Mon Composant';
```

Voici mon dernier conseil concernant les imports (tiré de [ici](https://medium.freecodecamp.org/the-most-important-eslint-rule-for-redux-applications-c10f6aeff61d)) : Si vous utilisez ESLint, vous devriez envisager de définir les deux règles suivantes :

```js
"rules": {
    // Vérifie que l'import nommé existe
    "import/named": 2, 
  
    // Désactivé dans le preset airbnb
    "import/prefer-default-export": "off"
}
```

### Préférez les composants fonctionnels

Si vous avez de nombreux composants dont le seul but est d'afficher des données, tirez parti des nombreuses façons de [définir un composant React](https://reactjs.org/docs/components-and-props.html#functional-and-class-components) :

```js
class Watch extends React.Component {
  render () {
    return <div>{this.props.hours}:{this.props.minutes}</div>
  }
}

// Composant fonctionnel équivalent
const Watch = (props) =>
  <div>{props.hours}:{props.minutes}</div>;
```

Les deux extraits définissent le même composant `Watch`. Pourtant, le second est bien plus court et supprime même `this` pour accéder aux props dans le template JSX.

### Remplacez les divs par des fragments

Chaque composant doit exposer un élément racine unique en tant que template. Pour respecter cette règle, la solution courante est d'envelopper le template dans une `div`.

React 16 nous apporte une nouvelle fonctionnalité appelée [_Fragments_](https://reactjs.org/docs/fragments.html). Maintenant, vous pouvez remplacer ces `div` inutiles par des `React.Fragment`.

Le template de sortie sera le contenu du fragment sans aucun enveloppeur.

```js
const Login = () => 
  <div><input name="login"/><input name="password"/></div>;

const Login = () =>
  <React.Fragment><input name="login"/><input name="password"/></React.Fragment>;

const Login = () => // Syntaxe abrégée
  <><input name="login"/><input name="password"/></>;
```

### Soyez prudent lors de la définition de l'état

Dès que votre application React est dynamique, vous devez gérer les états des composants.

L'utilisation des états semble assez simple. Initialisez le contenu de l'état dans le `constructor` puis appelez `setState` pour mettre à jour l'état.

Pour une raison quelconque, vous pourriez avoir besoin d'utiliser les valeurs actuelles de l'**état** ou des **props** lors de l'appel à `setState` pour définir la valeur de l'état suivant.

```js
// Très mauvaise pratique : n'utilisez pas this.state et this.props dans setState !
this.setState({ answered: !this.state.answered, answer });

// Avec des états assez grands : la tentation devient plus grande
// Ici, conservez l'état actuel et ajoutez la propriété answer
this.setState({ ...this.state, answer });
```

Le problème est que React ne garantit pas que `this.state` et `this.props` ont la valeur à laquelle vous vous attendez. `setState` est asynchrone, car les mises à jour de l'état sont regroupées pour optimiser les manipulations du DOM (voir les détails dans la [documentation React](https://reactjs.org/docs/state-and-lifecycle.html#state-updates-may-be-asynchronous) et ce [problème](https://github.com/facebook/react/issues/11527#issuecomment-360199710)).

```js
// Notez la notation () autour de l'objet qui fait que le moteur JS
// l'évalue comme une expression et non comme le bloc de la fonction fléchée
this.setState((prevState, props) 
              => ({ ...prevState, answer }));
```

Pour éviter les états corrompus, vous devez utiliser `setState` avec le paramètre de fonction. Il fournit des valeurs d'état et de props appropriées.

### Liaison des fonctions de composant

Il existe de nombreuses façons de lier les événements d'un élément à son composant, et certaines ne sont pas recommandées.

La première et légitime solution apparaît dans la [documentation React](https://reactjs.org/docs/handling-events.html) :

```js
class DatePicker extends React.Component {
   handleDateSelected({target}){
     // Faire des choses
   }
   render() {   
     return <input type="date" onChange={this.handleDateSelected}/>
   }
 }
```

Cela pourrait vous décevoir lorsque vous découvrirez que cela ne fonctionne pas.

La raison est que lors de l'utilisation de JSX, la valeur de `this` n'est pas liée à l'instance du composant. Voici trois alternatives pour que cela fonctionne :

```js
// #1 : utiliser une fonction fléchée
<input type="date" onChange={(event) => this.handleDateSelected(event)}/>

// OU #2 : lier this à la fonction dans le constructeur du composant
constructor () { 
  this.handleDateSelected = this.handleDateSelected.bind(this); 
}

// OU #3 : déclarer la fonction comme un champ de classe (syntaxe de fonction fléchée)
handleDateSelected = ({target}) => {
   // Faire des choses
}
```

Utiliser une fonction fléchée dans JSX comme dans le premier exemple semble attrayant au premier abord. Mais ne le faites pas. En réalité, votre fonction fléchée sera [recréée à chaque rendu du composant](https://reactjs.org/docs/handling-events.html) et cela nuira aux performances.

De plus, soyez prudent avec la dernière solution. Elle utilise la syntaxe des champs de classe qui n'est qu'une [proposition pour ECMAScript](https://github.com/tc39/proposal-class-fields).

Cela signifie que vous devez utiliser [Babel](https://babeljs.io/docs/plugins/transform-class-properties) pour [transpiler](https://en.wikipedia.org/wiki/Source-to-source_compiler) le code. Si la syntaxe n'est pas finalement adoptée, votre code ne fonctionnera plus.

### Adoptez le modèle de conteneur (même avec Redux)

Dernier point mais non des moindres, le modèle de conception de conteneur. Cela vous permet de suivre le principe de [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns) dans le composant React.

```js
export class DatePicker extends React.Component {
  state = { currentDate: null };

  handleDateSelected = ({target}) =>
     this.setState({ currentDate: target.value });

  render = () => 
     <input type="date" onChange={this.handleDateSelected}/>
}
```

Un seul composant gère le rendu du template et les actions de l'utilisateur au même endroit. Utilisons plutôt deux composants :

```js
const DatePicker = (props) => 
  <input type="date" onChange={props.handleDateSelected}/>
        
export class DatePickerController extends React.Component { 
  // ... Aucune modification sauf la fonction render ...
  render = () => 
     <DatePicker handleDateSelected={this.handleDateSelected}/>;
}
```

Voici l'astuce. `DatePickerContainer` gère les interactions de l'utilisateur et les appels API si nécessaire. Ensuite, il rend un `DatePicker` et fournit des props.

Grâce à ce modèle, le composant conteneur remplace le composant de présentation. Ce composant fonctionnel devient inutile sans props.

```js
export const DatePickerContainer = 
 connect(mapStateToProps, mapDispatchToProps)(DatePickerController);
```

De plus, si vous utilisez Redux comme gestionnaire d'état pour votre application, il s'intègre également bien avec ce modèle.

La fonction `connect` injecte des props dans le composant. Dans notre cas, elle alimentera le contrôleur qui transmettra ces props au composant.

Ainsi, les deux composants pourront accéder aux données Redux. Voici le code complet pour le modèle de conception de conteneur (sans Redux ou syntaxe des champs de classe).

%[https://codepen.io/jbardon/pen/oNXOWEy]

### Bonus : Corriger le perçage de props

En écrivant mon projet d'apprentissage pour React, j'ai remarqué un mauvais modèle qui m'a dérangé avec les props. Sur chaque page, j'avais un composant principal qui utilisait le store et rendait certains composants imbriqués.

Comment les composants imbriqués peuvent-ils accéder aux données du composant principal ? En fait, ils ne peuvent pas — mais vous pouvez le corriger en :

* enveloppant le composant dans un conteneur (il devient intelligent)
* ou en passant les props du composant principal

La deuxième solution implique que les composants entre le composant principal et le composant imbriqué devront passer des props dont ils n'ont pas besoin.

```js
const Page = props => <UserDetails fullName="John Doe"/>;
   
const UserDetails = props => 
<section>
    <h1>Détails de l'utilisateur</h1>
    <CustomInput value={props.fullName}/> // <= Pas besoin de fullName mais le passer
</section>;

const inputStyle = {
   height: '30px',
   width: '200px',
	fontSize: '19px',
   border: 'none',
   borderBottom: '1px solid black'
};
const CustomInput = props => // v Enfin utiliser la valeur fullName du composant Page
   <input style={inputStyle} type="text" defaultValue={props.value}/>;
```

La communauté React a nommé ce problème **prop drilling**.

`Page` est le composant principal qui charge les détails de l'utilisateur. Il est nécessaire de passer ces données à travers `UserDetails` pour les amener à `CustomInput`.

Dans cet exemple, la prop ne passe que par un composant qui n'en a pas besoin. Mais cela peut être bien plus si vous avez des composants réutilisables. Par exemple, la base de code de Facebook contient quelques milliers de composants réutilisables !

Ne vous inquiétez pas, je vais vous apprendre trois façons de le corriger. Les deux premières méthodes apparaissent dans la [documentation de l'API Context](https://reactjs.org/docs/context.html#before-you-use-context) : **children prop** et **render prop**.

```js
// #1: Utiliser la prop children
const UserDetailsWithChildren = props => 
<section>
    <h1>Détails de l'utilisateur (avec children)</h1>
    {props.children /* <= utiliser children */} 
</section>;

// #2: Modèle de prop render
const UserDetailsWithRenderProp = props => 
<section>
    <h1>Détails de l'utilisateur (avec render prop)</h1>
    {props.renderFullName() /* <= utiliser la fonction render passée */}
</section>;

const Page = () => 
<React.Fragment>
    {/* #1: Prop children */}
    <UserDetailsWithChildren>
        <CustomInput value="John Doe"/> {/* Définit props.children */}
    </UserDetailsWithChildren>
  
    {/* #2: Modèle de prop render */}
    {/* Rappel : passer des fonctions fléchées est une mauvaise pratique, faites-en une méthode de la classe Page à la place */}
    <UserDetailsWithRenderProp renderFullName={() => <CustomInput value="John Doe"/>}/>
</React.Fragment>;
```

Ces solutions sont assez similaires. Je préfère utiliser children, car cela fonctionne bien dans la méthode render. Notez que vous pouvez également étendre ces modèles en fournissant des composants imbriqués plus profondément.

```html
const Page = () =>  
<PageContent>
  <RightSection> 
    <BoxContent>
      <UserDetailsWithChildren>
          <CustomInput value="John Doe"/>
      </UserDetailsWithChildren>
    </BoxContent>
  </RightSection>
</PageContent>
```

Le troisième exemple utilise l'API de contexte expérimentale.

```js
const UserFullNameContext = React.createContext('userFullName');

const Page = () => 
<UserFullNameContext.Provider value="John Doe"> {/* Remplir le contexte avec une valeur */}
    <UserDetailsWithContext/>
</UserFullNameContext.Provider>;

const UserDetailsWithContext = () => // Aucune prop à fournir
<section>
    <h1>Détails de l'utilisateur (avec contexte)</h1>
    <UserFullNameContext.Consumer> {/* Obtenir la valeur du contexte */}
        { fullName => <CustomInput value={fullName}/> }
    </UserFullNameContext.Consumer>
</section>;
```

Je ne recommande pas cette méthode, car elle utilise une fonctionnalité expérimentale. (Et c'est pourquoi l'API a récemment [changé sur une version mineure](https://reactjs.org/blog/2018/03/29/react-v-16-3.html).) De plus, elle vous oblige à créer une variable globale pour stocker le contexte, et votre composant obtient une nouvelle dépendance peu claire (le contexte peut contenir n'importe quoi).

#### C'est tout !

Merci d'avoir lu. J'espère que vous avez appris quelques conseils intéressants sur React !

**Si vous avez trouvé cet article utile, veuillez cliquer sur le bouton** ? **plusieurs fois pour aider les autres à trouver l'article et montrer votre soutien !** ?

**N'oubliez pas de me suivre pour être informé de mes prochains articles** ?

> Ceci fait partie de ma série "React pour les débutants" sur l'introduction à React, ses fonctionnalités principales et les meilleures pratiques à suivre.

> [<< Recommencer](https://www.freecodecamp.org/news/p/2994c09b-d550-4eb6-b281-a83e553240c7/) | [< Précédent](https://www.freecodecamp.org/news/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4/)

### Consultez mes [Autres](https://www.freecodecamp.org/news/author/jbardon/) Articles

#### ➡ JavaScript

* [Comment améliorer vos compétences en JavaScript en écrivant votre propre Framework de développement Web](https://medium.freecodecamp.org/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190) ?
* [Erreurs courantes à éviter lors de l'utilisation de Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)

#### ➡ Astuces et conseils

* [Arrêtez le débogage douloureux de JavaScript et adoptez Intellij avec Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [Comment réduire les bundles JavaScript énormes sans effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)